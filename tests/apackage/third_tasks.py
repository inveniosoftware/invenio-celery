# SPDX-FileCopyrightText: 2018 CERN.
# SPDX-License-Identifier: MIT

"""Demo task module with one task."""

from celery import shared_task


@shared_task
def third_task():
    """Third example task."""
