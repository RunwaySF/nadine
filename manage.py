#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nadine.settings")

    from django.core.management.commands.runserver import Command as runserver
    if 'PORT' in os.environ and os.environ['PORT']:
      runserver.default_port = os.environ['PORT']
    else:
      runserver.default_port = "8080"

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
