import inflect
import argparse
from typing import Any, Dict, List
import math
from flask_appbuilder.forms import DynamicForm
from wtforms import HiddenField
from sqlalchemy import (Boolean, Date, DateTime, Enum, Float,
                        Integer, Numeric, String, Text, Time,
                        ForeignKey, Table, ForeignKeyConstraint,
                        PrimaryKeyConstraint, MetaData, create_engine, inspect)
from sqlalchemy.orm import RelationshipProperty
from sqlalchemy.sql import sqltypes
from flask import g, flash, redirect, url_for, session
# from flask_appbuilder.models.sqla.interface import SQLAInterface
from utils import snake_to_pascal, snake_to_words, pascal_to_words

p = inflect.engine()

def generate_views(database_uri):
    """
    Generate Flask-AppBuilder views for all tables in the database.

    :param database_uri: SQLAlchemy database URI
    :return: String containing the generated views code
    """
    engine = create_engine(database_uri)
    metadata = MetaData()
    metadata.reflect(bind=engine)
    inspector = inspect(engine)

    views = []

    # Add necessary imports
    views.extend([
        "from flask_appbuilder import ModelView, MasterDetailView, MultipleView",
        "from flask_appbuilder.models.sqla.interface import SQLAInterface",
        "from flask_appbuilder.fields import AJAXSelectField, QuerySelectField",
        "from flask_appbuilder.fieldwidgets import Select2AJAXWidget, Select2SlaveAJAXWidget",
        "from flask_appbuilder.actions import action",
        "from flask_appbuilder.security.decorators import has_access",
        "from flask_appbuilder.forms import DynamicForm",
        "from flask_appbuilder import AppBuilder, BaseView, expose, has_access",
        "from flask_appbuilder.models.mixins import ImageColumn, FileColumn",
        "from flask_appbuilder.api import ModelRestApi",
        "from flask import g, flash, redirect, url_for",
        "from flask_appbuilder.actions import action",
        "from sqlalchemy.orm import session",
        "from wtforms import StringField, BooleanField, IntegerField, DateField, DateTimeField, HiddenField, validators",
        "from flask_appbuilder.models.sqla.filters import SearchWidget, FilterStartsWith",
        "from flask_appbuilder.fieldwidgets import BS3TextFieldWidget, BS3PasswordFieldWidget, DatePickerWidget, DateTimePickerWidget, Select2Widget",
        "from wtforms import StringField, BooleanField, DecimalField",
        "from . import appbuilder, db",
        "from .models import *\n\n"
    ])

    # Generate regular ModelViews
    model_views = generate_model_views(metadata, inspector)
    views.extend(model_views)

    # Generate MasterDetailViews
    master_detail_views = generate_master_detail_views(metadata, inspector)
    views.extend(master_detail_views)

    # Generate MultipleViews
    multiple_views = generate_multiple_views(metadata)
    views.extend(multiple_views)

    # Add view registration functions
    views.extend(generate_view_registration_functions())

    return "\n".join(views)




def generate_model_views(metadata, inspector):
    model_views = []
    for table in metadata.sorted_tables:
        model_name = snake_to_pascal(table.name)
        view_class = f"{model_name}View"

        # Skip Flask-AppBuilder system tables
        if table.name.lower().startswith('ab_'):
            continue

        if len(get_columns(table, 'add')) > 10:  # Threshold for multi-step form
            model_views.append(generate_multistep_view(table, model_name, view_class, inspector, metadata))
        else:
            model_views.append(generate_model_view(table, model_name, view_class, inspector, metadata))

    return model_views



def generate_model_view(table: Table, model_name: str, view_class: str, inspector: Any, metadata: Any) -> str:
    """Generate a comprehensive ModelView for a table."""
    list_columns = get_columns(table, 'list')
    show_columns = get_columns(table, 'show')
    add_columns = get_columns(table, 'add')
    edit_columns = get_columns(table, 'edit')
    search_columns = get_search_columns(table)
    label_columns = get_label_columns(table)

    view_code = [
        f"class {view_class}(ModelView):",
        f"    datamodel = SQLAInterface('{model_name}')",
        f"    list_title = '{snake_to_words(table.name)} List'",
        f"    show_title = '{snake_to_words(table.name)} Details'",
        f"    add_title = 'Add {snake_to_words(table.name)}'",
        f"    edit_title = 'Edit {snake_to_words(table.name)}'",
        f"    list_columns = {list_columns}",
        f"    show_columns = {show_columns}",
        f"    add_columns = {add_columns}",
        f"    edit_columns = {edit_columns}",
        f"    list_exclude_columns = []",
        f"    show_exclude_columns = []",
        f"    add_exclude_columns = []",
        f"    edit_exclude_columns = []",
        f"    search_columns = {search_columns}",
        f"    label_columns = {label_columns}",
        generate_description_columns(table, inspector),
        generate_fieldsets(table),
        generate_show_fieldsets(table),
        generate_add_fieldsets(table),
        generate_edit_fieldsets(table),
        generate_validators(table, inspector),
        "    # Base Order",
        "    # base_order = ('name', 'asc')",
        "",
        "    # Base Filters",
        "    # base_filters = [['name', FilterStartsWith, 'A']]",
        "",
        generate_form_query_rel_fields(table),
        "    # Forms",
        "    # add_form = None",
        "    # edit_form = None",
        "",
        "    # Widgets",
        "    # show_widget = None",
        "    # add_widget = None",
        "    # edit_widget = None",
        "    # list_widget = None",
        "",
        generate_custom_actions(),
        "",
        "    # Form fields",
        "    form_extra_fields = {",
        generate_form_fields(table, metadata),
        generate_relationship_fields(table, metadata),
        "    }",
        "",
        generate_search_widget(),
        "    # Related Views",
        "    # related_views = []",
        "",
        "    # List Widgets",
        "    # list_template = 'appbuilder/general/model/list.html'",
        "    # list_widget = ListWidget",
        "",
        "    # Show Widget",
        "    # show_template = 'appbuilder/general/model/show.html'",
        "    # show_widget = ShowWidget",
        "",
        "    # Add Widget",
        "    # add_template = 'appbuilder/general/model/add.html'",
        "    # add_widget = FormWidget",
        "",
        "    # Edit Widget",
        "    # edit_template = 'appbuilder/general/model/edit.html'",
        "    # edit_widget = FormWidget",
        "",
        "    # Query Select Fields",
        "    # query_select_fields = {}",
        "",
        "    # Pagination",
        "    # page_size = 10",
        "",
        "    # Inline Forms",
        "    # inline_models = None",
        "",
        "    # Custom Templates",
        "    # list_template = 'my_list_template.html'",
        "    # show_template = 'my_show_template.html'",
        "    # add_template = 'my_add_template.html'",
        "    # edit_template = 'my_edit_template.html'",
        generate_repr_method(table),
        ""
    ]
    return "\n".join(view_code)

def generate_master_detail_views(metadata, inspector):
    """Generate MasterDetailViews for tables with foreign key relationships."""
    master_detail_views = []

    for table in metadata.sorted_tables:
        if table.name.lower().startswith('ab_'):
            continue
        for fk in table.foreign_keys:
            parent_table = fk.column.table
            parent_model_name = snake_to_pascal(parent_table.name)
            child_model_name = snake_to_pascal(table.name)
            view_class = f"{parent_model_name}{child_model_name}MasterDetailView"

            view_code = [
                f"class {view_class}(MasterDetailView):",
                f"    datamodel = SQLAInterface('{parent_model_name}')",
                f"    related_views = [{child_model_name}View]",
                f"    list_title = '{snake_to_words(parent_table.name)} with {snake_to_words(table.name)}'",
                f"    show_title = '{snake_to_words(parent_table.name)} Detail'",
                f"    add_title = 'Add {snake_to_words(parent_table.name)}'",
                f"    edit_title = 'Edit {snake_to_words(parent_table.name)}'",
                generate_description_columns(parent_table, inspector),
                generate_fieldsets(parent_table),
                generate_show_fieldsets(parent_table),
                generate_add_fieldsets(parent_table),
                generate_edit_fieldsets(parent_table),
                "",
                "    # Base Order",
                "    # base_order = ('name', 'asc')",
                "",
                "    # Base Filters",
                "    # base_filters = [['name', FilterStartsWith, 'A']]",
                "",
                "    # Forms",
                "    # add_form = None",
                "    # edit_form = None",
                "",
                "    # Widgets",
                "    # show_widget = None",
                "    # add_widget = None",
                "    # edit_widget = None",
                "    # list_widget = None",
                "",
                "    # List Widgets",
                "    # list_template = 'appbuilder/general/model/list.html'",
                "    # list_widget = ListWidget",
                "",
                "    # Pagination",
                "    # page_size = 10",
                "",
                "    # Custom Templates",
                "    # list_template = 'my_list_template.html'",
                "    # show_template = 'my_show_template.html'",
                "    # add_template = 'my_add_template.html'",
                "    # edit_template = 'my_edit_template.html'",
                "",
            ]
            master_detail_views.extend(view_code)

    return master_detail_views

# def generate_multiple_views(metadata):
#     """Generate MultipleViews for tables with multiple related tables."""
#     multiple_views = []
#
#     for table in metadata.sorted_tables:
#         related_tables = set()
#         for fk in table.foreign_keys:
#             related_tables.add(fk.column.table)
#         # for fk in metadata.tables.values():
#         #     if table in [fk.column.table for fk in fk.foreign_keys]:
#         #         related_tables.add(fk)
#         for other_table in metadata.sorted_tables:
#             for fk in other_table.foreign_keys:
#                 if fk.column.table == table:
#                     related_tables.add(other_table)
#
#         if len(related_tables) > 1:
#             model_name = snake_to_pascal(table.name)
#             view_class = f"{model_name}MultipleView"
#             related_views = [f"{snake_to_pascal(t.name)}View" for t in related_tables]
#
#             view_code = [
#                 f"class {view_class}(MultipleView):",
#                 f"    datamodel = SQLAInterface('{model_name}')",
#                 f"    views = [{', '.join(related_views)}]",
#                 "",
#                 "    # Base Order",
#                 "    # base_order = ('name', 'asc')",
#                 "",
#                 "    # List Widgets",
#                 "    # list_template = 'appbuilder/general/model/list.html'",
#                 "    # list_widget = ListWidget",
#                 "",
#                 "    # Pagination",
#                 "    # page_size = 10",
#                 "",
#                 "    # Custom Templates",
#                 "    # list_template = 'my_list_template.html'",
#                 "",
#             ]
#             multiple_views.extend(view_code)
#
#     return multiple_views
def generate_multiple_views(metadata):
    """Generate MultipleViews for tables with multiple related tables."""
    multiple_views = []

    for table in metadata.sorted_tables:
        if table.name.lower().startswith('ab_'):
            continue
        related_tables = set()

        # Identify tables that this table references
        for fk in table.foreign_keys:
            related_tables.add(fk.column.table)

        # Identify tables that reference this table
        for other_table in metadata.sorted_tables:
            for fk in other_table.foreign_keys:
                if fk.column.table == table:
                    related_tables.add(other_table)

        # Only generate MultipleView if there are more than one related tables
        if len(related_tables) > 1:
            model_name = snake_to_pascal(table.name)
            view_class = f"{model_name}MultipleView"
            related_views = [f"{snake_to_pascal(t.name)}View" for t in related_tables]

            view_code = [
                f"class {view_class}(MultipleView):",
                f"    datamodel = SQLAInterface('{model_name}')",
                f"    views = [{', '.join(related_views)}]",
                "",
                "    # Base Order",
                "    # base_order = ('name', 'asc')",
                "",
                "    # List Widgets",
                "    # list_template = 'appbuilder/general/model/list.html'",
                "    # list_widget = ListWidget",
                "",
                "    # Pagination",
                "    # page_size = 10",
                "",
                "    # Custom Templates",
                "    # list_template = 'my_list_template.html'",
                "",
            ]
            multiple_views.extend(view_code)

    return multiple_views

def generate_api_view(table: Any, model_name: str) -> str:
    """Generate an API view for a table."""
    columns = get_columns(table)
    api_view_code = [
        f"class {model_name}API(ModelRestApi):",
        f"    resource_name = '{snake_to_words(table.name).lower()}'",
        f"    datamodel = SQLAInterface('{model_name}')",
        f"    list_columns = {columns}",
        f"    show_columns = {columns}",
        f"    add_columns = {[col for col in columns if col != 'id']}",
        f"    edit_columns = {[col for col in columns if col != 'id']}",
        "    # Add any API-specific configuration here",
        ""
    ]
    return "\n".join(api_view_code)

def generate_view_registration_functions():
    """Generate functions for registering different types of views."""
    registration_functions = [
        "def register_model_views():",
        "    # Register regular model views",
        "    for table_name, model_class in db.Model._decl_class_registry.items():",
        "        if isinstance(model_class, type) and issubclass(model_class, db.Model):",
        "            view_class = globals().get(f'{model_class.__name__}View')",
        "            if view_class:",
        "                appbuilder.add_view(view_class, f'{pascal_to_words(model_class.__name__)}', icon='fa-table', category='Data')",
        "",
        "def register_master_detail_views():",
        "    # Register master-detail views",
        "    for name, obj in globals().items():",
        "        if isinstance(obj, type) and issubclass(obj, MasterDetailView):",
        "            appbuilder.add_view(obj, f'{pascal_to_words(name)}', icon='fa-link', category='Master-Detail')",
        "",
        "def register_multiple_views():",
        "    # Register multiple views",
        "    for name, obj in globals().items():",
        "        if isinstance(obj, type) and issubclass(obj, MultipleView):",
        "            appbuilder.add_view(obj, f'{pascal_to_words(name)}', icon='fa-cubes', category='Multiple Views')",
        "",
        "def register_all_views():",
        "    register_model_views()",
        "    register_master_detail_views()",
        "    register_multiple_views()",
        "",
        "# Call this function to register all views",
        "register_all_views()",
        ""
    ]
    return registration_functions




def generate_multistep_view(table: Table, model_name: str, view_class: str, inspector: Any, metadata: Any) -> str:
    """Generate a multi-step view for models with many fields."""
    columns = get_columns(table, 'add')
    step_size = 5  # Number of fields per step
    num_steps = math.ceil(len(columns) / step_size)

    view_code = [
        f"class {view_class}(ModelView):",
        f"    datamodel = SQLAInterface('{model_name}')",
        f"    list_title = '{snake_to_words(table.name)} List'",
        f"    add_title = 'Add {snake_to_words(table.name)}'",
        f"    edit_title = 'Edit {snake_to_words(table.name)}'",
        f"    list_columns = {get_columns(table, 'list')}",
        f"    show_columns = {get_columns(table, 'show')}",
        f"    search_columns = {get_search_columns(table)}",
        f"    label_columns = {get_label_columns(table)}",
        generate_description_columns(table, inspector),
        "",
        "    class AddForm(DynamicForm):",
        "        step = HiddenField('step')",
        "",
        "    add_form = AddForm",
        "",
        "    def add_form_get(self, form):",
        "        form.step.data = session.get('form_step', 1)",
        "        return form",
        "",
        "    def add_form_post(self, form):",
        "        if form.step.data:",
        "            session['form_step'] = int(form.step.data)",
        "        return form",
        "",
        "    def form_get(self, form):",
        "        form = super().form_get(form)",
        "        step = int(session.get('form_step', 1))",
        "        start = (step - 1) * 5",
        "        end = step * 5",
        f"        visible_fields = {columns}[start:end]",
        "        for field in form._fields:",
        "            if field not in visible_fields and field != 'step':",
        "                form._fields[field].render_kw = {'style': 'display:none;'}",
        "        return form",
        "",
        "    def form_post(self, form):",
        "        step = int(form.step.data)",
        f"        if step < {num_steps}:",
        "            session['form_step'] = step + 1",
        "            return self.update_redirect(), False  # Keep user on the same form",
        "        else:",
        "            session.pop('form_step', None)",
        "            return super().form_post(form)",
        "",
    ]

    fieldsets_code = []
    for i in range(num_steps):
        start = i * step_size
        end = (i + 1) * step_size
        step_columns = columns[start:end]
        fieldset_code = f"    ('Step {i+1}', {{'fields': ['step'] + {step_columns}, 'expanded': True}})"
        fieldsets_code.append(fieldset_code)

    view_code.append(f"    add_fieldsets = [{', '.join(fieldsets_code)}]")
    view_code.append(f"    edit_fieldsets = add_fieldsets")
    view_code.append("")
    view_code.append(generate_repr_method(table))
    view_code.append("")

    return "\n".join(view_code)

# def generate_multistep_view(table: Table, model_name: str, view_class: str, inspector: Any, metadata: Any) -> str:
#     """Generate a multi-step view for models with many fields."""
#     columns = get_columns(table, 'add')
#     step_size = 5  # Number of fields per step
#     num_steps = math.ceil(len(columns) / step_size)
#
#     view_code = [
#         f"class {view_class}(ModelView):",
#         f"    datamodel = SQLAInterface('{model_name}')",
#         f"    list_title = '{snake_to_words(table.name)} List'",
#         f"    add_title = 'Add {snake_to_words(table.name)}'",
#         f"    edit_title = 'Edit {snake_to_words(table.name)}'",
#         f"    list_columns = {get_columns(table, 'list')}",
#         f"    show_columns = {get_columns(table, 'show')}",
#         f"    search_columns = {get_search_columns(table)}",
#         f"    label_columns = {get_label_columns(table)}",
#         generate_description_columns(table, inspector),
#         "",
#         "    class AddForm(DynamicForm):",
#         "        step = HiddenField('step')",
#         "",
#         "    add_form = AddForm",
#         "",
#         "    def add_form_get(self, form):",
#         "        form.step.data = session.get('form_step', 1)",
#         "        return form",
#         "",
#         "    def add_form_post(self, form):",
#         "        if form.step.data:",
#         "            session['form_step'] = int(form.step.data)",
#         "        return form",
#         "",
#         "    def form_get(self, form):",
#         "        form = super().form_get(form)",
#         "        step = int(session.get('form_step', 1))",
#         "        start = (step - 1) * 5",
#         "        end = step * 5",
#         f"        visible_fields = {columns}[start:end]",
#         "        for field in form._fields:",
#         "            if field not in visible_fields and field != 'step':",
#         "                form._fields[field].render_kw = {'style': 'display:none;'}",
#         "        return form",
#         "",
#         "    def form_post(self, form):",
#         "        step = int(form.step.data)",
#         f"        if step < {num_steps}:",
#         "            session['form_step'] = step + 1",
#         "            return None",
#         "        else:",
#         "            session.pop('form_step', None)",
#         "            return super().form_post(form)",
#         "",
#     ]
#
#     for i in range(num_steps):
#         start = i * step_size
#         end = (i + 1) * step_size
#         step_columns = columns[start:end]
#         view_code.extend([
#             f"    add_fieldsets = [",
#             f"        ('Step {i+1}', {{'fields': ['step'] + {step_columns}, 'expanded': True}}),",
#             "    ]" if i == num_steps - 1 else "    ]",
#             "",
#         ])
#
#     view_code.extend([
#         "    edit_fieldsets = add_fieldsets",
#         "",
#         generate_repr_method(table),
#         ""
#     ])
#
#     return "\n".join(view_code)


def get_columns(table: Any, purpose: str = 'list') -> List[str]:
    """
    Generate list of columns for a table, handling different column types intelligently.

    :param table: SQLAlchemy Table object
    :param purpose: 'list', 'show', 'add', or 'edit'
    :return: List of column names
    """
    columns = []
    for column in table.columns:
        # Skip 'id' for add and edit forms
        if purpose in ['add', 'edit'] and column.name == 'id':
            continue

        # Handle different column types
        if isinstance(column.type, Boolean):
            columns.append(column.name)
        elif isinstance(column.type, (String, Text)):
            columns.append(column.name)
        elif isinstance(column.type, (Integer, Float, Numeric)):
            columns.append(column.name)
        elif isinstance(column.type, (Date, DateTime)):
            columns.append(column.name)
        elif isinstance(column.type, Time):
            columns.append(column.name)
        elif isinstance(column.type, Enum):
            columns.append(column.name)
        elif isinstance(column.type, ForeignKey):
            if purpose in ['add', 'edit']:
                # For add and edit forms, use the relationship name instead of the foreign key column
                columns.append(column.name.replace('_id', ''))
            else:
                columns.append(column.name)
        else:
            # For any other types, include the column as is
            columns.append(column.name)

        # Add specific handling for certain column names
        if purpose in ['add', 'edit']:
            if column.name in ['created_at', 'updated_at', 'created_by', 'updated_by']:
                columns.remove(column.name)

    return columns

def get_search_columns(table):
    """Generate list of searchable columns."""
    return [col.name for col in table.columns if isinstance(col.type, (sqltypes.String, sqltypes.Text))]

def get_label_columns(table):
    """Generate dictionary of user-friendly labels for columns."""
    return {col.name: snake_to_words(col.name) for col in table.columns}

def generate_description_columns(table, inspector):
    """Generate description_columns dictionary with column comments as hints."""
    descriptions = {}
    for column in inspector.get_columns(table.name):
        if column['comment']:
            descriptions[column['name']] = column['comment']

    if descriptions:
        return f"    description_columns = {descriptions}"
    else:
        return "    description_columns = {}"

def generate_fieldsets(table):
    """Generate fieldsets for a table."""
    columns = get_columns(table)
    return f"""
    list_fieldsets = [
        ('Summary', {{'fields': {columns}}})
    ]
    """

def generate_show_fieldsets(table):
    """Generate show_fieldsets for a table."""
    columns = get_columns(table)
    return f"""
    show_fieldsets = [
        ('Summary', {{'fields': {columns}}})
    ]
    """

def generate_add_fieldsets(table):
    """Generate add_fieldsets for a table."""
    columns = [col for col in get_columns(table) if col != 'id']
    return f"""
    add_fieldsets = [
        ('Add {snake_to_words(table.name)}', {{'fields': {columns}}})
    ]
    """

def generate_edit_fieldsets(table):
    """Generate edit_fieldsets for a table."""
    columns = [col for col in get_columns(table) if col != 'id']
    return f"""
    edit_fieldsets = [
        ('Edit {snake_to_words(table.name)}', {{'fields': {columns}}})
    ]
    """

def generate_repr_method(table):
    """Generate __repr__ method for the view."""
    display_column = next((col.name for col in table.columns if col.name in ['name', 'title', 'label']), table.columns[0].name)
    return f"""
    def __repr__(self):
        return self.{display_column}
    """

def generate_validators(table: Any, inspector: Any) -> str:
    """Generate form validators based on column constraints."""
    validators = {}
    for column in table.columns:
        column_validators = []
        if not column.nullable and not column.primary_key:
            column_validators.append('validators.DataRequired()')
        if column.unique:
            column_validators.append('validators.Unique()')
        if isinstance(column.type, sqltypes.String) and column.type.length:
            column_validators.append(f'validators.Length(max={column.type.length})')
        if column_validators:
            validators[column.name] = f"[{', '.join(column_validators)}]"

    if validators:
        return f"    validators_columns = {validators}"
    return ""

def generate_form_query_rel_fields(table: Any) -> str:
    """Generate form_query_rel_fields for foreign key relationships."""
    form_query_rel_fields = {}
    for fk in table.foreign_keys:
        referred_table = fk.column.table
        form_query_rel_fields[fk.parent.name] = f"db.session.query({snake_to_pascal(referred_table.name)})"

    if form_query_rel_fields:
        return f"    form_query_rel_fields = {form_query_rel_fields}"
    return ""

def generate_custom_actions() -> str:
    """Generate placeholders for custom actions including print, export, and bookmark."""
    return """
    @action("muldelete", "Delete", "Delete all Really?", "fa-trash")
    def muldelete(self, items):
        if isinstance(items, list):
            self.datamodel.delete_all(items)
            self.update_redirect()
        else:
            self.datamodel.delete(items)
        return redirect(self.get_redirect())

    @action("print", "Print", "Print selected items", "fa-print")
    def print_items(self, items):
        if not isinstance(items, list):
            items = [items]

        print_view = f"{self.__class__.__name__}PrintView"
        return redirect(url_for(print_view, pks=[item.id for item in items]))

    @action("export", "Export", "Export as CSV", "fa-file-excel-o")
    def export(self, items):
        if not isinstance(items, list):
            items = [items]

        # Here you would implement the logic to export the items
        # This is a placeholder and should be customized based on your needs
        return redirect(url_for('export_items', model=self.datamodel.obj.__name__, ids=[item.id for item in items]))

    @action("bookmark", "Bookmark", "Bookmark selected items", "fa-bookmark")
    def bookmark(self, items):
        if not isinstance(items, list):
            items = [items]

        # Here you would implement the logic to bookmark the items
        # This is a placeholder and should be customized based on your needs
        for item in items:
            # Assuming you have a Bookmark model
            bookmark = Bookmark(user_id=g.user.id, item_id=item.id, item_type=self.datamodel.obj.__name__)
            db.session.add(bookmark)

        db.session.commit()
        flash(f"{len(items)} item(s) bookmarked successfully.", "success")
        return redirect(self.get_redirect())

    @expose('/print/<pks>')
    @has_access
    def print_view(self, pks):
        pks = pks.split(',')
        items = self.datamodel.get_many(pks)
        self.update_redirect()
        return self.render_template('print_view.html',
                                    items=items,
                                    title=self.list_title,
                                    widgets=self.show_columns)
    """

def generate_search_widget() -> str:
    """Generate search widget configuration."""
    return """
    search_widget = SearchWidget(
        labels={"name": "Name", "description": "Description"},
        search_columns=["name", "description"],
        filters=[{"name": "name", "op": "ilike"}],
        filter_rel_fields={"category": [["name", FilterStartsWith, ""]]}
    )
    """


def generate_form_fields(table: Any, metadata: Any) -> str:
    """Generate form fields with appropriate widgets and validations based on column types."""
    form_fields = []
    for column in table.columns:
        if column.name in ['id', 'created_at', 'updated_at', 'created_by', 'updated_by']:
            continue  # Skip special fields

        if isinstance(column.type, String):
            if 'password' in column.name:
                form_fields.append(
                    f"    '{column.name}': StringField('{column.name.capitalize()}', widget=BS3PasswordFieldWidget(), validators=[validators.DataRequired(), validators.Length(max={column.type.length})]),"
                )
            else:
                form_fields.append(
                    f"    '{column.name}': StringField('{column.name.capitalize()}', widget=BS3TextFieldWidget(), validators=[validators.DataRequired(), validators.Length(max={column.type.length})]),"
                )
        elif isinstance(column.type, Text):
            form_fields.append(
                f"    '{column.name}' : TextAreaField('{column.name.capitalize()}', widget=BS3TextFieldWidget(), validators=[validators.DataRequired()]),"
            )
        elif isinstance(column.type, Boolean):
            form_fields.append(
                f"    '{column.name}' : BooleanField('{column.name.capitalize()}'),"
            )
        elif isinstance(column.type, Integer):
            form_fields.append(
                f"    '{column.name}' : IntegerField('{column.name.capitalize()}', validators=[validators.DataRequired()]),"
            )
        elif isinstance(column.type, Float):
            form_fields.append(
                f"    '{column.name}' : FloatField('{column.name.capitalize()}', validators=[validators.DataRequired()]),"
            )
        elif isinstance(column.type, Numeric):
            form_fields.append(
                f"    '{column.name}' : DecimalField('{column.name.capitalize()}', validators=[validators.DataRequired()]),"
            )
        elif isinstance(column.type, Date):
            form_fields.append(
                f"    '{column.name}' : DateField('{column.name.capitalize()}', widget=DatePickerWidget(), validators=[validators.DataRequired()]),"
            )
        elif isinstance(column.type, DateTime):
            form_fields.append(
                f"    '{column.name}' : DateTimeField('{column.name.capitalize()}', widget=DateTimePickerWidget(), validators=[validators.DataRequired()]),"
            )
        elif isinstance(column.type, Time):
            form_fields.append(
                f"    '{column.name}' : TimeField('{column.name.capitalize()}'),"
            )
        elif isinstance(column.type, Enum):
            enum_choices = [(choice, choice) for choice in column.type.enums]
            form_fields.append(
                f"    '{column.name}' : SelectField('{column.name.capitalize()}', choices={enum_choices}, validators=[validators.DataRequired()]),"
            )
        elif isinstance(column.type, ForeignKey):
            related_model = column.foreign_keys[0].column.table.name.capitalize()
            relationship_field = column.name.replace('_id', '')
            form_fields.append(
                f"    '{relationship_field}': QuerySelectField('{relationship_field.capitalize()}', query_factory=lambda: db.session.query({related_model}), widget=Select2Widget(), allow_blank=True),"
            )

    # Handle many-to-many relationships
    for related_table_name, related_table in metadata.tables.items():
        if is_association_table(related_table) and table.name in [
            fk.column.table.name for fk in related_table.foreign_keys
        ]:
            related_model = related_table_name.capitalize()
            form_fields.append(
                f"    '{related_table_name}s': QuerySelectMultipleField('{related_model}s', query_factory=lambda: db.session.query({related_model}), widget=Select2ManyWidget()),"
            )

    if not form_fields:
        return "    # No fields to generate"

    return "\n".join(form_fields)


# def generate_form_fields(table: Any) -> str:
#     """Generate form fields with appropriate widgets based on column types."""
#     form_fields = []
#     for column in table.columns:
#         if column.name == 'id':
#             continue
#         if isinstance(column.type, String):
#             if 'password' in column.name:
#                 form_fields.append(f"    '{column.name}': StringField('{column.name.capitalize()}', widget=BS3PasswordFieldWidget()),")
#             else:
#                 form_fields.append(f"    '{column.name}':  StringField('{column.name.capitalize()}', widget=BS3TextFieldWidget()),")
#         elif isinstance(column.type, Text):
#             form_fields.append(f"    '{column.name}' : TextAreaField('{column.name.capitalize()}', widget=BS3TextFieldWidget()),")
#         elif isinstance(column.type, Boolean):
#             form_fields.append(f"    '{column.name}' : BooleanField('{column.name.capitalize()}'),")
#         elif isinstance(column.type, Integer):
#             form_fields.append(f"    '{column.name}' : IntegerField('{column.name.capitalize()}'),")
#         elif isinstance(column.type, Float):
#             form_fields.append(f"    '{column.name}' : FloatField('{column.name.capitalize()}'),")
#         elif isinstance(column.type, Numeric):
#             form_fields.append(f"    '{column.name}' : DecimalField('{column.name.capitalize()}'),")
#         elif isinstance(column.type, Date):
#             form_fields.append(f"    '{column.name}' : DateField('{column.name.capitalize()}', widget=DatePickerWidget()),")
#         elif isinstance(column.type, DateTime):
#             form_fields.append(f"    '{column.name}' : DateTimeField('{column.name.capitalize()}', widget=DateTimePickerWidget()),")
#         elif isinstance(column.type, Time):
#             form_fields.append(f"    '{column.name}' : TimeField('{column.name.capitalize()}'),")
#         elif isinstance(column.type, Enum):
#             enum_choices = [(choice, choice) for choice in column.type.enums]
#             form_fields.append(f"    '{column.name}' : SelectField('{column.name.capitalize()}', choices={enum_choices}),")
#         elif isinstance(column.type, ForeignKey):
#             related_model = column.foreign_keys[0].column.table.name
#             form_fields.append(f"    {column.name.replace('_id', '')} : QuerySelectField('{column.name.capitalize()}', query_factory=lambda: db.session.query({related_model.capitalize()}), widget=Select2Widget())")
#     return "\n".join(form_fields)


def generate_relationship_fields(table: Table, metadata: Any) -> str:
    """
    Generate relationship fields using Select2 widgets for foreign key fields.

    :param table: SQLAlchemy Table object
    :param metadata: SQLAlchemy MetaData object
    :return: String containing the generated relationship fields
    """
    relationship_fields = []

    # Handle one-to-many and many-to-one relationships
    for fk in table.foreign_keys:
        related_table = fk.column.table
        related_model = snake_to_pascal(related_table.name)  # Use consistent PascalCase conversion
        field_name = fk.parent.name.replace('_id', '')

        relationship_fields.append(
            f"    '{field_name}': QuerySelectField('{field_name.capitalize()}', "
            f"query_factory=lambda: db.session.query({related_model}), "
            f"widget=Select2Widget(), "
            f"allow_blank=True),"
        )

    # Check for many-to-many relationships
    for other_table in metadata.tables.values():
        if is_association_table(other_table):
            # Check if this table is referenced in the association table
            foreign_keys = [fk for fk in other_table.foreign_keys if fk.column.table == table]
            if foreign_keys:
                # Identify the other related table in the many-to-many relationship
                other_related_table = [fk.column.table for fk in other_table.foreign_keys if fk.column.table != table][0]
                related_model = snake_to_pascal(other_related_table.name)
                field_name = f"{snake_to_pascal(other_related_table.name).lower()}s"  # Pluralize the relationship field name

                relationship_fields.append(
                    f"    '{field_name}': QuerySelectMultipleField('{field_name.capitalize()}', "
                    f"query_factory=lambda: db.session.query({related_model}), "
                    f"widget=Select2ManyWidget()),"
                )

    if not relationship_fields:
        return "    # No relationship fields found"

    return "\n".join(relationship_fields)


# def generate_relationship_fields(table: Table, metadata: Any) -> str:
#     """
#     Generate relationship fields using Select2 widgets for foreign key fields.
#
#     :param table: SQLAlchemy Table object
#     :param metadata: SQLAlchemy MetaData object
#     :return: String containing the generated relationship fields
#     """
#     relationship_fields = []
#
#     for fk in table.foreign_keys:
#         related_table = fk.column.table
#         related_model = related_table.name.capitalize()
#         field_name = fk.parent.name.replace('_id_fk', '')
#
#         relationship_fields.append(
#             f"    {field_name} = QuerySelectField('{field_name.capitalize()}', "
#             f"query_factory=lambda: db.session.query({related_model}), "
#             f"widget=Select2Widget(), "
#             f"allow_blank=True)"
#         )
#
#     # Check for many-to-many relationships
#     for table_name, other_table in metadata.tables.items():
#         if is_association_table(other_table):
#             if table.name in [fk.column.table.name for fk in other_table.foreign_keys]:
#                 other_table_name = [fk.column.table.name for fk in other_table.foreign_keys if fk.column.table.name != table.name][0]
#                 related_model = other_table_name.capitalize()
#                 field_name = f"{other_table_name.lower()}s"
#
#                 relationship_fields.append(
#                     f"    {field_name} = QuerySelectMultipleField('{field_name.capitalize()}', "
#                     f"query_factory=lambda: db.session.query({related_model}), "
#                     f"widget=Select2ManyWidget())"
#                 )
#
#     if not relationship_fields:
#         return "    # No relationship fields found"
#
#     return "\n,".join(relationship_fields)

def is_association_table(table: Table) -> bool:
    """
    Check if a table is an association table (for many-to-many relationships).

    :param table: SQLAlchemy Table object
    :return: Boolean indicating if the table is an association table
    """
    if len(table.columns) != 2:
        return False

    return all(isinstance(constraint, ForeignKeyConstraint) for constraint in table.constraints
               if isinstance(constraint, ForeignKeyConstraint))

def get_related_model_columns(model: Any) -> List[str]:
    """
    Get the columns of a related model that could be used for display.

    :param model: SQLAlchemy Model class
    :return: List of column names
    """
    return [col.name for col in model.__table__.columns
            if col.name in ['name', 'title', 'label', 'description']]

def generate_api_views(metadata: MetaData, inspector: Any) -> List[str]:
    """
    Generate API views for all tables in the database.

    :param metadata: SQLAlchemy MetaData object
    :param inspector: SQLAlchemy Inspector object
    :return: List of strings containing the generated API view code
    """
    api_views = []
    for table in metadata.sorted_tables:
        model_name = snake_to_pascal(table.name)

        # Skip Flask-AppBuilder system tables
        if model_name.lower().startswith('ab_'):
            continue

        api_views.append(generate_api_view(table, model_name))
    return api_views

def generate_charts(metadata: MetaData, inspector: Any) -> List[str]:
    """
    Generate chart views for suitable tables in the database.

    :param metadata: SQLAlchemy MetaData object
    :param inspector: SQLAlchemy Inspector object
    :return: List of strings containing the generated chart view code
    """
    chart_views = []
    for table in metadata.sorted_tables:
        if is_suitable_for_chart(table):
            chart_views.append(generate_chart_view(table))
    return chart_views

def is_suitable_for_chart(table: Table) -> bool:
    """
    Check if a table is suitable for generating a chart view.

    :param table: SQLAlchemy Table object
    :return: Boolean indicating if the table is suitable for a chart
    """
    # This is a simple heuristic and can be expanded based on specific requirements
    numeric_columns = [col for col in table.columns if isinstance(col.type, (Integer, Float, Numeric))]
    date_columns = [col for col in table.columns if isinstance(col.type, (Date, DateTime))]
    return len(numeric_columns) > 0 and len(date_columns) > 0

def generate_chart_view(table: Table) -> str:
    """
    Generate a chart view for a suitable table.

    :param table: SQLAlchemy Table object
    :return: String containing the generated chart view code
    """
    model_name = snake_to_pascal(table.name)
    chart_type = determine_chart_type(table)
    x_axis = get_suitable_x_axis(table)
    y_axis = get_suitable_y_axis(table)

    chart_view_code = f"""
class {model_name}ChartView(ChartView):
    datamodel = SQLAInterface('{model_name}')
    chart_title = '{snake_to_words(table.name)} Chart'
    chart_type = '{chart_type}'
    definitions = [
        {{
            'label': '{y_axis} by {x_axis}',
            'group': '{x_axis}',
            'series': ['{y_axis}']
        }}
    ]
"""
    return chart_view_code

def determine_chart_type(table: Table) -> str:
    """
    Determine the most suitable chart type for a table.

    :param table: SQLAlchemy Table object
    :return: String representing the chart type
    """
    # This is a simple heuristic and can be expanded based on specific requirements
    date_columns = [col for col in table.columns if isinstance(col.type, (Date, DateTime))]
    if date_columns:
        return 'LineChart'
    else:
        return 'BarChart'

def get_suitable_x_axis(table: Table) -> str:
    """
    Determine a suitable x-axis for a chart based on the table structure.

    :param table: SQLAlchemy Table object
    :return: String representing the column name for the x-axis
    """
    date_columns = [col.name for col in table.columns if isinstance(col.type, (Date, DateTime))]
    if date_columns:
        return date_columns[0]
    else:
        # Fallback to the first string column or the first column
        string_columns = [col.name for col in table.columns if isinstance(col.type, (String, Text))]
        return string_columns[0] if string_columns else table.columns[0].name

def get_suitable_y_axis(table: Table) -> str:
    """
    Determine a suitable y-axis for a chart based on the table structure.

    :param table: SQLAlchemy Table object
    :return: String representing the column name for the y-axis
    """
    numeric_columns = [col.name for col in table.columns if isinstance(col.type, (Integer, Float, Numeric))]
    return numeric_columns[0] if numeric_columns else table.columns[0].name


def main():
    parser = argparse.ArgumentParser(description='Generate Flask-AppBuilder views from database schema.')
    parser.add_argument('--uri', type=str, required=True, help='Database URI')
    parser.add_argument('--output', type=str, default='views.py', help='Output file name')
    args = parser.parse_args()

    views_code = generate_views(args.uri)

    with open(args.output, "w") as f:
        f.write(views_code)

    print(f"Views generated successfully in {args.output}")

if __name__ == '__main__':
    main()


