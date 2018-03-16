================
 Invenio-Celery
================

.. image:: https://img.shields.io/travis/inveniosoftware/invenio-celery.svg
        :target: https://travis-ci.org/inveniosoftware/invenio-celery

.. image:: https://img.shields.io/coveralls/inveniosoftware/invenio-celery.svg
        :target: https://coveralls.io/r/inveniosoftware/invenio-celery

.. image:: https://img.shields.io/github/tag/inveniosoftware/invenio-celery.svg
        :target: https://github.com/inveniosoftware/invenio-celery/releases

.. image:: https://img.shields.io/pypi/dm/invenio-celery.svg
        :target: https://pypi.python.org/pypi/invenio-celery

.. image:: https://img.shields.io/github/license/inveniosoftware/invenio-celery.svg
        :target: https://github.com/inveniosoftware/invenio-celery/blob/master/LICENSE


Celery distributed task queue module for Invenio.

Invenio-Celery is a small discovery layer that takes care of discovering and
loading tasks from other Invenio modules, as well as providing configuration
defaults for Celery usage in Invenio. Invenio-Celery relies on Flask-CeleryExt
for integrating Flask and Celery with application factories.

Further documentation is available on https://invenio-celery.readthedocs.io/
