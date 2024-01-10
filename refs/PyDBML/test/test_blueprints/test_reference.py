from unittest import TestCase
from unittest.mock import Mock

from pydbml.classes import Column
from pydbml.classes import Reference
from pydbml.classes import Table
from pydbml.exceptions import ColumnNotFoundError
from pydbml.exceptions import TableNotFoundError
from pydbml.parser.blueprints import ReferenceBlueprint


class TestReferenceBlueprint(TestCase):
    def test_build_minimal(self) -> None:
        bp = ReferenceBlueprint(
            type='>',
            inline=True,
            table1='table1',
            col1='col1',
            table2='table2',
            col2='col2',
        )

        t1 = Table(
            name='table1'
        )
        c1 = Column(name='col1', type='Number')
        t1.add_column(c1)
        t2 = Table(
            name='table2'
        )
        c2 = Column(name='col2', type='Varchar')
        t2.add_column(c2)

        with self.assertRaises(RuntimeError):
            bp.build()

        parserMock = Mock()
        parserMock.locate_table.side_effect = [t1, t2]
        bp.parser = parserMock
        result = bp.build()
        self.assertIsInstance(result, Reference)
        self.assertEqual(result.type, bp.type)
        self.assertEqual(result.inline, bp.inline)
        self.assertEqual(parserMock.locate_table.call_count, 2)
        self.assertEqual(result.col1, [c1])
        self.assertEqual(result.col2, [c2])

    def test_tables_and_cols_are_not_set(self) -> None:
        bp = ReferenceBlueprint(
            type='>',
            inline=True,
            table1=None,
            col1='col1',
            table2='table2',
            col2='col2'
        )
        with self.assertRaises(TableNotFoundError):
            bp.build()

        bp.table1 = 'table1'
        bp.table2 = None
        with self.assertRaises(TableNotFoundError):
            bp.build()

        bp.table2 = 'table2'
        bp.col1 = None
        with self.assertRaises(ColumnNotFoundError):
            bp.build()

        bp.col1 = 'col1'
        bp.col2 = None
        with self.assertRaises(ColumnNotFoundError):
            bp.build()

    def test_tables_and_cols_are_set(self) -> None:
        bp = ReferenceBlueprint(
            type='>',
            inline=True,
            table1='table1',
            col1='col1',
            table2='table2',
            col2=None
        )
        with self.assertRaises(ColumnNotFoundError):
            bp.build()
