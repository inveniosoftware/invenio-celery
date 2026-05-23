# SPDX-FileCopyrightText: 2015-2018 CERN.
# SPDX-License-Identifier: MIT

"""Demo task module with two tasks."""

from celery import shared_task


@shared_task
def second_task_a():
    """Second example task A."""


@shared_task
def second_task_b():
    """Second example task B."""
