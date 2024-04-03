#   ссылка на 'django-seed': https://github.com/Brobin/django-seed?ysclid=lucuhq95p147909136

from django.core.management.base import BaseCommand
from django_seed import Seed
from im.models import Role


class Command(BaseCommand):
    _tables = [
        {'table_name': Role, 'table_dada': [{'id': 1, 'name': "Admin"}, {'id': 2, 'name': "User"}],}
    ]

    def handle(self, *args, **options):
        # очистка и запись служебной таблицы Role
        for table in self._tables:
            if len(table['table_name'].objects.all()) != 0:
                TableClearing(table['table_name'])
            self._write_data_to_table(table['table_name'], table['table_dada'])

    def _write_data_to_table(self, table_name, table_dada):
        seeder = Seed.seeder()
        for data_element in table_dada:
            seeder.add_entity(table_name, 1, data_element)
        seeder.execute()


class TableClearing:
    def __init__(self, table):
        table.objects.all().delete()
