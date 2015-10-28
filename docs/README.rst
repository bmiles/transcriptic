README
======

Transcriptic CLI

The Transcriptic CLI is a command-line tool for managing Transcriptic organizations, projects, runs, datasets and more.

Transcriptic is the robotic cloud laboratory for the life sciences. `https://www.transcriptic.com <https://www.transcriptic.com/>`_

Setup
-----

.. code-block:: shell

    $ pip install transcriptic

or

.. code-block:: shell

    $ git clone https://github.com/transcriptic/transcriptic.git
    $ cd transcriptic
    $ pip install .


to upgrade to the latest version using pip or check whether you're already up to date:

.. code-block:: shell

    $ pip install transcriptic --upgrade


Then, login to your Transcriptic account:

.. code-block:: shell

    $ transcriptic login
    Email: me@example.com
    Password:
    Logged in as me@example.com (example-lab)


Documentation
-------------

See the `Transcriptic Developer Documentation <https://developers.transcriptic.com/docs/getting-started-with-the-cli/>`_ for detailed information about how to use this package, including learning about how to package protocols and build releases.
