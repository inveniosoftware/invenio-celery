..
    This file is part of Invenio.
    Copyright (C) 2015-2018 CERN.

    Invenio is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

Changes
=======

Version 1.1.1 (released 2019-11-19)

- pinned version of celery lower than 4.3 due to Datetime serialization
  issues

Version 1.1.0 (released 2019-06-21)

- Changed the ``msgpack-python`` dependency to ``msgpack``.
  Please first uninstall ``msgpack-python`` before installing
  the new ``msgpack`` dependency (``pip uninstall msgpack-python``).


Version 1.0.1 (released 2018-12-06)

- Adds support for Celery v4.2. Technically this change is backward
  incompatible because it is no longer possible to load tasks from bare modules
  (e.g. mymodule.py in the Python root). This is a constraint imposed by Celery
  v4.2. We however do not known of any cases where bare modules have been used,
  and also this design is discouraged so we are not flagging it as a backward
  incompatible change, in order to have the change readily available for
  current Invenio version.

Version 1.0.0 (released 2018-03-23)

- Initial public release.
