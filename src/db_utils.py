import re, string
from sqlalchemy.dialects.postgresql import (
    ARRAY, BIGINT, BIT, BOOLEAN, BYTEA, CHAR, CIDR, CITEXT, DATE, DATEMULTIRANGE,
    DATERANGE, DOMAIN, DOUBLE_PRECISION, ENUM, FLOAT, HSTORE, INET, INT4MULTIRANGE,
    INT4RANGE, INT8MULTIRANGE, INT8RANGE, INTEGER, INTERVAL, JSON, JSONB, JSONPATH,
    MACADDR, MACADDR8, MONEY, NUMERIC, NUMMULTIRANGE, NUMRANGE, OID, REAL, REGCLASS,
    REGCONFIG, SMALLINT, TEXT, TIME, TIMESTAMP, TSMULTIRANGE, TSQUERY, TSRANGE,
    TSTZMULTIRANGE, TSTZRANGE, TSVECTOR, UUID, VARCHAR,
)
def map_dbml_datatypes(datatype: str):
    mapping = {
        'int': 'Integer',
        'tinyint': 'Integer',
        'smallint': 'Integer',
        'mediumint': 'Integer',
        'bigint': 'BigInteger',
        'float': 'Float',
        'double': 'Float',
        'decimal': 'Numeric',
        'numeric': 'Numeric',
        'char': 'String',
        'varchar': 'String',
        'tinytext': 'String',
        'text': 'String',
        'mediumtext': 'String',
        'longtext': 'String',
        'date': 'Date',
        'datetime': 'DateTime',
        'timestamp': 'DateTime',
        'time': 'Time',
        'year': 'Integer',
    }
    return mapping.get(datatype.lower(), datatype.title())


def map_pgsql_datatypes(pg_type: str):
    pg_type = pg_type.lower()
    if pg_type.startswith('interval'):
        return 'Interval'
    elif pg_type.startswith('int'):
        return 'Integer'
    elif pg_type.startswith('smallint'):
        return 'SmallInteger'
    elif pg_type in ('bigint', 'bigserial'):
        return 'BigInteger'
    elif pg_type.startswith('varchar'):
        return 'String'
    elif pg_type in ('text', 'citext'):
        return 'Text'
    elif pg_type.startswith('bool'):
        return 'Boolean'
    elif pg_type in ('real', 'float4'):
        return 'Float'
    elif pg_type in ('double precision', 'float8'):
        return 'Float'
    elif pg_type in ('numeric', 'decimal'):
        return 'Numeric'
    elif pg_type.startswith('numeric'):
        # Extract precision and scale from the PostgreSQL type
        match = re.match(r'numeric\((\d+),(\d+)\)', pg_type)
        if match:
            precision = int(match.group(1))
            scale = int(match.group(2))
            return f'Numeric(precision={precision}, scale={scale})'
        else:
            return 'Numeric'  # Default if precision and scale are not specified
    elif pg_type == 'money':
        return 'Currency'
    elif pg_type == 'date':
        return 'Date'
    elif pg_type in ('time', 'timetz'):
        return 'Time'
    elif pg_type.startswith('timestamp'):  # in ('timestamp', 'timestamptz'):
        return "DateTime, server_default=text('NOW()')"
    elif pg_type in ('bytea', 'byte', 'blob'):
        return 'LargeBinary'
    elif pg_type == 'uuid':
        return 'UUID'
    elif pg_type == 'inet':
        return IPAddressType()
    elif pg_type == 'json':
        return JSONType()
    elif pg_type == 'email':
        return EmailType()
    elif pg_type == 'url':
        return URLType()
    elif pg_type == 'phone':
        return PhoneNumberType()
    elif pg_type == 'color':
        return ColorType()
    elif pg_type == 'choice':
        return ChoiceType()
    else:
        return pg_type


def map_mysql_datatypes(mysql_type):
    """
    Maps a MySQL data type to a Flask-AppBuilder data type.
    """
    mysql_type = mysql_type.lower()
    if mysql_type.startswith('tinyint(1)'):
        return 'Boolean'
    elif mysql_type.startswith('tinyint') or mysql_type.startswith('smallint') or mysql_type.startswith(
            'mediumint') or mysql_type.startswith('int') or mysql_type.startswith('bigint') or mysql_type.startswith(
        'year'):
        return 'Integer'
    elif mysql_type.startswith('float') or mysql_type.startswith('double') or mysql_type.startswith('decimal'):
        return 'Numeric'
    elif mysql_type.startswith('char') or mysql_type.startswith('varchar') or mysql_type.startswith(
            'text') or mysql_type.startswith('mediumtext') or mysql_type.startswith('longtext'):
        return 'String'
    elif mysql_type.startswith('date') or mysql_type.startswith('datetime') or mysql_type.startswith(
            'timestamp') or mysql_type.startswith('time'):
        return 'DateTime'
    elif mysql_type.startswith('enum') or mysql_type.startswith('set'):
        return 'Enum'
    else:
        return 'String'


def map_oracle_datatypes(oracle_type):
    """
    Maps an Oracle data type to a Flask-AppBuilder data type.
    """
    oracle_type = oracle_type.upper()
    if oracle_type.startswith('NUMBER') or oracle_type.startswith('BINARY_FLOAT') or oracle_type.startswith(
            'BINARY_DOUBLE'):
        return 'Numeric'
    elif oracle_type.startswith('VARCHAR2') or oracle_type.startswith('NVARCHAR2') or oracle_type.startswith(
            'CHAR') or oracle_type.startswith('NCHAR') or oracle_type.startswith('CLOB') or oracle_type.startswith(
            'NCLOB'):
        return 'String'
    elif oracle_type.startswith('DATE') or oracle_type.startswith('TIMESTAMP') or oracle_type.startswith(
            'TIMESTAMP WITH TIME ZONE') or oracle_type.startswith('TIMESTAMP WITH LOCAL TIME ZONE'):
        return 'DateTime'
    elif oracle_type.startswith('INTERVAL YEAR TO MONTH') or oracle_type.startswith('INTERVAL DAY TO SECOND'):
        return 'Interval'
    elif oracle_type.startswith('FLOAT'):
        return 'Float'
    elif oracle_type.startswith('BLOB') or oracle_type.startswith('RAW') or oracle_type.startswith('LONG RAW'):
        return 'Binary'
    elif oracle_type.startswith('BOOLEAN'):
        return 'Boolean'
    else:
        return 'String'


def map_sqlite_datatypes(sqlite_type):
    """
    Maps a SQLite data type to a Flask-AppBuilder data type.
    """
    if sqlite_type.startswith('integer') or sqlite_type.startswith('tinyint') or sqlite_type.startswith(
            'smallint') or sqlite_type.startswith('mediumint') or sqlite_type.startswith(
            'int') or sqlite_type.startswith('bigint'):
        return 'Integer'
    elif sqlite_type.startswith('real') or sqlite_type.startswith('float') or sqlite_type.startswith(
            'double') or sqlite_type.startswith('decimal'):
        return 'Numeric'
    elif sqlite_type.startswith('char') or sqlite_type.startswith('varchar') or sqlite_type.startswith(
            'text') or sqlite_type.startswith('clob'):
        return 'String'
    elif sqlite_type.startswith('date') or sqlite_type.startswith('time') or sqlite_type.startswith('timestamp'):
        return 'DateTime'
    elif sqlite_type.startswith('blob') or sqlite_type.startswith('binary') or sqlite_type.startswith('varbinary'):
        return 'Binary'
    elif sqlite_type.startswith('boolean'):
        return 'Boolean'
    else:
        return 'String'


def pg_to_fabtypes(postgres_type):
    postgres_type = postgres_type.lower()
    type_mapping = {
        "bigint": "BigInteger",
        "bigserial": "BigInteger",
        "boolean": "Boolean",
        "box": "String",
        "bytea": "LargeBinary",
        "character": "String",
        "character varying": "String",
        "cidr": "String",
        "circle": "String",
        "date": "Date",
        "double precision": "Float",
        "inet": "String",
        "integer": "Integer",
        "interval": "Interval",
        "json": "JSON",
        "jsonb": "JSON",
        "line": "String",
        "lseg": "String",
        "macaddr": "String",
        "money": "Float",
        "numeric": "Numeric",
        "path": "String",
        "pg_lsn": "String",
        "point": "String",
        "polygon": "String",
        "real": "Float",
        "smallint": "SmallInteger",
        "smallserial": "SmallInteger",
        "serial": "Integer",
        "text": "Text",
        "time": "Time",
        "timestamp": "DateTime",
        "tsquery": "String",
        "tsvector": "String",
        "txid_snapshot": "String",
        "uuid": "String",
        "varchar": "String",
        "xml": "String",
    }
    return type_mapping.get(postgres_type.lower(), "String")

### Using Marshmallow
def get_field_type(column_type):
    type_mapping = {
        String: fields.Str(),
        Text: fields.Str(),
        Unicode: fields.Str(),
        UnicodeText: fields.Str(),
        BIGINT: fields.Int(),
        BIT: fields.Str(),  # or a custom field for bit strings
        BOOLEAN: fields.Bool(),
        BYTEA: fields.Str(),  # or a custom field for binary data
        CHAR: fields.Str(),
        CIDR: fields.Str(),  # or a custom field for network addresses
        CITEXT: fields.Str(),
        DATEMULTIRANGE: fields.List(fields.Date()),  # or a custom field for date ranges
        DATERANGE: fields.Raw(),  # or a custom field for date ranges
        DOMAIN: fields.Raw(),  # handle as per specific domain type
        DOUBLE_PRECISION: fields.Float(),
        ENUM: fields.Str(),  # or a custom field handling specific enums
        FLOAT: fields.Float(),
        HSTORE: fields.Dict(fields.Str(), fields.Str()),
        INET: fields.Str(),  # or a custom field for IP addresses
        INT4MULTIRANGE: fields.List(fields.Int()),  # or a custom field for integer ranges
        INT4RANGE: fields.Raw(),  # or a custom field for integer ranges
        INT8MULTIRANGE: fields.List(fields.Int()),  # or a custom field for integer ranges
        INT8RANGE: fields.Raw(),  # or a custom field for integer ranges
        INTERVAL: fields.TimeDelta(),
        NCHAR: fields.Str(),
        NVARCHAR: fields.Str(),
        VARCHAR: fields.Str(),  # Explicitly handling VARCHAR
        VARBINARY: fields.Str(),  # or a custom field for binary data
        BLOB: fields.Str(),  # or a custom field for binary data
        CLOB: fields.Str(),
        JSONB: fields.Raw(),  # or a custom field for JSONB data
        JSONPATH: fields.Str(),  # or a custom field for JSONPath expressions
        MACADDR: fields.Str(),  # or a custom field for MAC addresses
        MACADDR8: fields.Str(),  # or a custom field for MAC addresses
        MONEY: fields.Decimal(),  # or a custom field for monetary values
        NUMERIC: fields.Decimal(),
        NUMMULTIRANGE: fields.List(fields.Decimal()),  # or a custom field for numeric ranges
        NUMRANGE: fields.Raw(),  # or a custom field for numeric ranges
        OID: fields.Int(),  # or a custom field for object identifiers
        REAL: fields.Float(),
        REGCLASS: fields.Str(),  # or a custom field for regclass type
        REGCONFIG: fields.Str(),  # or a custom field for regconfig type
        SMALLINT: fields.Int(),
        TEXT: fields.Str(),
        TIME: fields.Time(),
        TIMESTAMP: fields.DateTime(),
        TSMULTIRANGE: fields.Raw(),  # or a custom field for timestamp ranges
        TSQUERY: fields.Str(),  # or a custom field for text search queries
        TSRANGE: fields.Raw(),  # or a custom field for timestamp ranges
        TSTZMULTIRANGE: fields.Raw(),  # or a custom field for timestamp with time zone ranges
        TSTZRANGE: fields.Raw(),  # or a custom field for timestamp with time zone ranges
        TSVECTOR: fields.Str(),  # or a custom field for text search vectors
        UUID: fields.UUID(),
        LargeBinary: fields.Str(),  # or a custom field for binary data
        # Binary: fields.Str(),  # or a custom field for binary data
        Integer: fields.Int(),
        BigInteger: fields.Int(),
        SmallInteger: fields.Int(),
        Float: fields.Float(),
        Numeric: fields.Float(),
        DECIMAL: fields.Float(),
        Boolean: fields.Bool(),
        DateTime: fields.DateTime(),
        Date: fields.Date(),
        DATE: fields.Date(),
        Time: fields.Time(),
        INTEGER: fields.Int(),
        Interval: fields.TimeDelta(),
        JSON: fields.Raw(),  # or a custom field for handling JSON
        ARRAY: fields.List(fields.Raw()),  # Adjust the inner field type as needed
        PickleType: fields.Raw(),  # or a custom field for serialized data
        Enum: fields.Str(),  # or a custom field for enum handling

        # Add other SQLAlchemy types and corresponding field types as needed.
    }
    return type_mapping.get(type(column_type))