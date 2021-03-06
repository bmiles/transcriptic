## `transcriptic` Changelog

## Unreleased
Fixed
- Fixed bug in _PlateRead that caused data overwrites if multiple instances of the same
group_label were present

## v3.11.0
Updated
- Handling of 403 routes
- Documentation to reflect permissions changes
- Minor rework of launch_request

## v3.10.3
Fixed
- Bug with launch_request

## v3.10.2
Fixed
- AP2EN_test failures still requiring protocol
- object.py requirement for `autoprotocol.container_types`

## v3.10.1
Fixed
- Minor bugfix for `_parse_protocol`

## v3.10.0
Updated
- Removed setup.py requirement for `autoprotocol-python`

## v3.9.2
Fixed
- Bugfix to resolve error caused by attempting to print unicode characters on the CLI.

## v3.9.1
Fixed
- Bugfix to remove `data_keys` from Absorbance function, which is no longer returned from webapp

## v3.9.0
Added
- Add raw_data property to the `Dataset` object
- Add ability to cross reference aliquots with their data using the `Dataset` object

## v3.8.0
Added
- Ability to add `--dye_test` flag to `transcriptic preview` to convert a run into a water/dye test

## v3.7.1
Fixed
- Fixed minor bug in launching local protocols with `transcriptic launch`

## v3.7.0
Added
- Ability to browse your inventory using the `transcriptic inventory` command E.g. `transcriptic inventory water`
- Ability to launch protocols remotely using the `--remote` flag. E.g. `transcriptic launch Pipetting --remote`
- Ability to view available remote protocols for launching using `transcriptic protocols --remote`
- Ability for `transcriptic summarize` to retrieve resource strings with the `--lookup` flag

Fixed
- resources route has been updated to match web return
- Ap2En for dispense and provision
- resources route now accepts resource IDs

## v3.6.0
Added
- Object helpers to allow more natural property access. E.g. `myRun.instructions.Instructions` = `myRun.Instructions`

Updated
- Misc formatting changes for HTML representation

Fixed
- Underyling `handle_response` code to be more robust

## v3.5.1
Added
- Row index of the Container.aliquots DataFrame object now corresponds to the well index

Fixed
- Stored volume in the Container.aliquots DataFrame as a Unit object instead of unicode

## v3.5.0
Added
- timeout property for Run objects
- data_ids property for Run objects

Updated
- data property for Run objects gives more informative errors when failing due to timeout
- `.monitoring` method is now shifted to the Instruction object from the Run object
- Optional parameters can now be handled by `get_route`
Fixed
- Existing route for monitoring data

## v3.4.3
Fixed
- Made local commands robust to lack of internet access

## v3.4.2
Fixed
- Broaden exception clause for general Python compatibility

## v3.4.1
Added
- Usage analytics support to CLI
Updated
- Minor documentation fixes

## v3.4.0
Added
- `transcriptic select_org` in CLI now allows you to switch organizations without re-authenticating
-  `User-agent` information to headers
-  `Run.containers` to return a list of containers used within the run

## v3.3.1
Fixed
- Updated `transcriptic runs` route to reflect reality

## v3.3.0
Added
- Ability for `api.get_zip` to handle larger zip-files by downloading to a local file
- `cover` and `storage` attributes to Container object
- Ability to construct and visualize a given protocol's job tree using a flag on the CLI
Updated
- Updated english's summarize to handle all currently-implemented instructions

## v3.2.5
Fixed
- Fixed initialization of Container object

## v3.2.4
Added
- Helper function `flatmap` into util
Fixed
- Fixed resources route in CLI. `transcriptic resources 'query'` now works

## v3.2.3
Changed
- Simplified `Container._parse_container_type` to use matching AP-Py container-type object whenever possible

## v3.2.2
Added
- additional documentation for `Connection` object
Changed
- update relevant documentation.rst files

## v3.2.1
Changed
- Updated "url" reference in run attributes to use "id" instead, in-line with a web update
Fixed
- Update docs/requirements.txt to be PEP440 compatible

## v3.2.0
Changed
- Reworked `Instruction` object
- Reworked `Run.instructions` to return a Dataframe of `Instruction` objects
- `Aliquot` object has been reworked into Container object as an `aliquots` property

Removed
- `Resource` object has been removed from the library as its currently unused

Fixed
- Change check for ImagePlate to be more generic
- Setup now requires plotly 1.9.6 (for plotly offline/ipython compatibility reasons)

## v3.1.0
Added
- Tab completion for CLI (enabled by sourcing `transcriptic_complete.sh`)
- New API route for getting zipfiles: `api.get_zip`
- Made -h option synonymous with --help

## v3.0.2
Changed
- Setup now requires plotly 1.9.6 or greater

## v3.0.1
Fixed
- Better handling of Datasets with no `well_map` property in kinetics.spectrophotometry

## v3.0.0
Added
- New documentation for the new testing framework and how to write tests
- Added Dockerfile for running Transcriptic containers. Compatible with CI tools (e.g. Jenkins) as well
- New documentation added and hosted on http://transcriptic.readthedocs.io/en/latest/

Changed
- Migrated the test framework from vanilla unittest2 to py.test
- Rewrote documentation structure and added misc. documentation related changes
- `api` module has been removed and merged into `config` module. The Connection object now handles all api calls.
- All references to `ctx` has been renamed to `api`

Fixed
- Fixed bug in spectrophotometry handling attributes
- Fixed compatibility issue with running `transcriptic preview` on python3

## v2.3.1
Changed
- Transcriptic CLI subcommands: compile, init, preview, summarize no longer require login

Fixed
- `transcriptic runs` command now works in CLI

## v2.3.0
Added
- `__version__` variable for checking version. Enable version checking in CLI using `transcriptic --version`
- New Analysis module: Kinetics; `Kinetics` base object and `Kinetics.Spectrophotometry` for analyzing kinetics-based data such as growth curves
- Expose additional properties of Dataset object: `operation`, `container`, `data_type`

## v2.2.1
Changed
- Objects module has been heavily reworked and documentation added. This is especially true for Project, Run and Dataset objects

Fixed
- Fixed package related CLI issues

---
## v2.2.0
Added
- `api` module for handling all calls including responses and exceptions
- `Connection` object now mirrors most of the CLI functionality
- basic test infrastructure and examples for testing API module

Changed
- all separate requests, context or connection object calls are now consolidated and re-routed to go through the api and routes module

Removed
- all direct api calls (get, put, push, pull) are removed from Connection. Users are encouraged to use the corresponding calls from the `api` module instead

## v2.1.2
Fixed
- Change in datasets route

Changed
- Removed additional shadowed variable names

## v2.1.1
Added
- `imaging` module with `ImagePlate` as the first class for representing plate images. Focus is placed on IPython rendering
- PIL dependency for image manipulation

## v2.1.0
Changed
- Major refactor of code to be in-line with PEP8
- Removed unnecessary modules and renamed shadowed variables

## v2.0.11
Changed
- Updated behavior of `transcriptic login` to be clearer and to return appropriate error messages

Fixed
- print statement for launch

## v2.0.10
Added
- pypi tags for setup.py such as `classifiers` and `license`

Fixed
- Updated Container object to automatically populate safe_min_volume_ul

Removed
- Unused dependency: scikit-learn

## v2.0.9
Added
- Updated manifest json parsing to deserialize into an OrderedDict, preserving key order, which enables quick launch inputs to be ordered

## v2.0.8
Added
- `launch` command now supports --save_input option to save the protocol input as a local file

Fixed
- `launch` command now properly supported either a project name or project id for the `project` option
- typo AutoProtocol -> Autoprotocol

## v2.0.7
Added
- `launch` command to configure and run protocols without needing to package and upload them first

## v2.0.6
Fixed
- RMSE calculation in spectrophotometry.py now reports correct RMSE
- transcriptic submit now correctly parses new autopick group
- containter attributes are correctly requested from transcriptic via spectrophotometry.py

## v2.0.5
---
Added
- List runs in a specific project using the `transcriptic runs <project_name_or_id` command

## v2.0.4
---
Added
- Enabled `analyze` and `submit` to work for Protocol objects
- Additional functionality to Container object: Use your favorite autoprotocol ContainerType functions
- Additional properties of Container object exposed: Use wellMap to return a mapping of the well indices to aliquot names

Fixed
- Set plot to default to use mpl=true (not all users have plotly credentials)


## v2.0.3
---
Added
- cost breakdown in `analyze`
- Python 3 compatibility
- use `transcriptic preview --view` to return a URL that displays the instruction cards produced by the run you want to preview (this URL expires after two hours)
- use the 'transcriptic resources <query>' CLI command to search the catalog for a resource's vendor and `id`
- `plotly` and `future` are now required

Fixed
- dataset helpers and embedding

Removed
- ipython module

## v2.0.2
---

Changed
- Refactored analysis.spectrophotometry into `Fluorescence`, `Absorbance` and `Luminescence` classes that inherit from `PlateRead`

Added
- More documentation and related configuration
- Python 3 support
- Added cost breakdown to analyze CLI

Fixed
- bug with initializing runs with Project object

## v2.0.1
---
Added
- project url and description to setup.py
- `Aliquot`, `Resource` and `Container` object types
- documentation setup and configuration

Changed
- moved `submit` from `cli` to `__init__`

Fixed
- critical bug in `submit`
- bug in `analyze`
- bug in `create_project`

## v2.0.0.
---
- migrated content from [transcriptic/runner](https://github.com/transcriptic/runner) to here, converted that code to a Python Client Library,
- CLI functionality has not changed other than renaming some commands:
    - `release` --> `build-release`
    - `upload` --> `upload-release`
    - `new-project` --> `create-project`
    - `new-package` --> `create-package`
    - `run` --> `compile`
