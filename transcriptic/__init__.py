from past.builtins import basestring
import os
import json
import requests
from transcriptic.objects import Run, Project, Aliquot, Resource, Container, Dataset, ProtocolPreview
from autoprotocol import Protocol
import sys

ctx = None

class AnalysisException(Exception):
  def __init__(self, message):
    self.message = message
  def __str__(self):
    return self.message

def _check_ctx():
  '''
  Check connection context.
  '''
  if not ctx:
    raise Exception("No transcriptic.config.Connection context found!")

def _get_object(id, klass):
  _check_ctx()
  req = ctx.get("/-/%s" % id)
  if req.status_code == 200:
    data = req.json()
    return klass(data['id'], data, connection = ctx)
  elif req.status_code == 404:
    raise Exception("[404] No object found for ID " + id)
  else:
    raise Exception("[%d] %s" % (req.status_code, req.text))

def run(id):
  '''
  Return a Run object based on the id of a run in your organization.

  Parameters
  ----------
  id : str
    13 alphanumeric string representing a run id ("rXXXXXXXXXXXX")

  '''
  return _get_object(id, Run)

def project(id):
  '''
  Return a Project object based on the id of a project in your organization.

  Parameters
  ----------
  id : str
    13 alphanumeric string representing a project id ("pXXXXXXXXXXXX")

  '''
  return _get_object(id, Project)

def resource(id):
  '''
  Return a Resource object based on its id.

  Parameters
  ----------
  id : str
    13 alphanumeric string representing a resource id "rsXXXXXXXXXXX"

  '''
  return _get_object(id, Resource)

def aliquot(id):
  '''
  Return an Aliquot object based on the id of an aliquot in your organization's inventory.

  Parameters
  ----------
  id : str
    13 alphanumeric string representing an aliquot id "aqXXXXXXXXXXX"

  '''
  return _get_object(id, Aliquot)

def container(id):
  '''
  Return a Container object based on the id of a container in your organization's inventory.

  Parameters
  ----------
  id : str
    13 alphanumeric string representing a container id "ctXXXXXXXXXXX"

  '''
  return _get_object(id, Container)

def preview(protocol):
  '''
  Return a ProtocolPreview object based on a Protocol object or Autoprotocol-formatted JSON.

  Parameters
  ----------
  protocol : Protocol, dict
    Protocol object or Autoprotocol-formatted JSON

  '''
  _check_ctx()
  return ProtocolPreview(protocol, connection = ctx)

def analyze(protocol):
  '''
  Analyze a Protocol object or Autoprotocol-formatted JSON protocol

  Parameters
  ----------
  protocol : Protocol, dict
    Protocol object or JSON-formatted protocol to analyze

  '''
  _check_ctx()
  if isinstance(protocol, Protocol):
      protocol = protocol.as_dict()
  if "errors" in protocol:
      raise AnalysisException(("Error%s in protocol:\n%s" %
      (("s" if len(protocol["errors"]) > 1 else ""),
        "".join(["- " + e['message'] + "\n" for
        e in protocol["errors"]]))))

  req = ctx.post('analyze_run', data = json.dumps({
    "protocol": protocol,
    "test_mode": test_mode
  }))
  if req.status_code == 200:
    return req.json()
  elif req.status_code == 422:
    raise AnalysisException(("Error%s in protocol:\n%s" %
      (("s" if len(req.json()['protocol']) > 1 else ""),
        "".join(["- " + e['message'] + "\n" for
        e in req.json()['protocol']]))))
  else:
    raise Exception("[%d] %s" % (req.status_code, req.text))

def submit(protocol, project, title = None, test_mode = False):
  '''
  Submit a protocol or Protocol object to a project

  Parameters
  ----------
  protocol : Protocol, dict
    Protocol object or JSON-formatted protocol to submit
  project : str
    13 alphanumeric string representing a project id to submit the protocol to
  title : str, optional
    Title of resulting run
  test_mode : bool, optional
    Submit run in test mode if set to True. Test mode runs cannot be executed on the workcell.

  '''
  _check_ctx()
  if isinstance(protocol, Protocol):
      protocol = protocol.as_dict()
  req = ctx.post('%s/runs' % project, data = json.dumps({
    "title": title,
    "protocol": protocol,
    "test_mode": test_mode
  }))
  if req.status_code == 201:
    return req.json()
  elif req.status_code == 404:
    raise AnalysisException("Error: Couldn't create run (404). \nAre you sure the project %s "
               "exists, and that you have access to it?" % ctx.url(project))
  elif req.status_code == 422:
    raise AnalysisException("Error creating run: %s" % req.text)
  else:
    raise Exception("[%d] %s" % (req.status_code, req.text))

def dataset(id, key = "*"):
  '''
  Return a dataset based on its id

  Parameters
  ----------
  id : str
    13 alphanumeric string representing a dataset's id
  key : str, optional

  '''
  _check_ctx()
  req = ctx.get("/data/%s.json?key=%s" % (id, key))
  if req.status_code == 200:
    data = req.json()
    return Dataset(id, data, connection = ctx)
  else:
    raise Exception("[%d] %s" % (req.status_code, req.text))
