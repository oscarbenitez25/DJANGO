#!/usr/bin/env python
"""Utilitat de línia de comandes de Django per a tasques administratives."""
import os
import sys


def main():
    """Executa tasques administratives."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_site.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No s'ha pogut importar Django. Segur que està instal·lat i "
            "disponible a la teva variable d'entorn PYTHONPATH? Has "
            "oblidat activar un entorn virtual?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()