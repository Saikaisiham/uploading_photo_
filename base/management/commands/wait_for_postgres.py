import time
import psycopg2
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        max_attempts = 10
        attempts = 0
        connected = False

        while attempts < max_attempts and not connected:
            try:
                connection.ensure_connection()
                connected = True
            except psycopg2.OperationalError:
                attempts += 1
                time.sleep(1) 

        if not connected:
            self.stdout.write(self.style.ERROR("Unable to connect to PostgreSQL after multiple attempts. Exiting..."))
            exit(1)

        self.stdout.write(self.style.SUCCESS("Connected to PostgreSQL successfully!"))
