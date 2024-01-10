from unittest import TestCase

from pydbml.classes import Expression


class TestNote(TestCase):
    def test_sql(self):
        e = Expression('SUM(amount)')
        self.assertEqual(e.sql, '(SUM(amount))')

    def test_dbml(self):
        e = Expression('SUM(amount)')
        self.assertEqual(e.dbml, '`SUM(amount)`')
