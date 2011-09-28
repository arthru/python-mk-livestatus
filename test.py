#!/usr/bin/python
from pprint import pprint
from mk_livestatus import Socket

s = Socket("/var/lib/icinga/rw/live")
q = s.query(
"""GET hosts
Columns: name groups
Filter: state = 0
Limit: 1
""")

pprint(q.get_dict('name'))
pprint(q.get_list())

q = s.query(
"""GET hosts
Columns: parents state name
Filter: state = 2
Limit: 1
""")

pprint(q.get_list())
pprint(q.get_dict('name'))

