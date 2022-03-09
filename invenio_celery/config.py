# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2018 CERN.
# Copyright (C) 2022 Graz University of Technology.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Default configuration values for Celery integration.

For further Celery configuration variables see
`Celery <http://docs.celeryproject.org/en/3.1/configuration.html>`_
documentation.
"""

broker_url = 'redis://localhost:6379/0'
"""Broker settings."""

result_backend = 'redis://localhost:6379/1'
"""The backend used to store task results."""

accept_content = ['json', 'msgpack', 'yaml']
"""A whitelist of content-types/serializers."""

result_serializer = 'msgpack'
"""Result serialization format. Default is ``msgpack``."""

task_serializer = 'msgpack'
"""The default serialization method to use. Default is ``msgpack``."""
