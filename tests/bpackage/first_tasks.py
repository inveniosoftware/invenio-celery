# SPDX-FileCopyrightText: 2015-2018 CERN.
# SPDX-License-Identifier: MIT

"""Demo task module with one task."""

from celery import shared_task


@shared_task
def first_task():
    """First example task."""
