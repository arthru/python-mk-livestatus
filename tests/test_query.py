from mk_livestatus import Query


def test_query_1():
    q = Query(None, 'hosts')
    q.columns('name', 'groups')
    q.filter('state = 0')
    expected = '''GET hosts
Columns: name groups
Filter: state = 0
OutputFormat: json
ColumnHeaders: on
'''
    assert str(q) == expected


def test_query_2():
    q = Query(None, 'services')
    q.columns('host_name', 'service_description', 'plugin_output', 'state')
    q.filter('host_name = localhost')
    expected = '''GET services
Columns: host_name service_description plugin_output state
Filter: host_name = localhost
OutputFormat: json
ColumnHeaders: on
'''
    assert str(q) == expected
