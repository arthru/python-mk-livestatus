Python MK Livestatus parser
===========================

:Author: Michael Fladischer
:Version: 0.1

.. contents::

Access the data returned from MK Livestatus queries as Python lists or dictionaries. 
It does this by sending queries to the MK Livestatus UNIX socket and parses the returned rows. 
Read/write permission to the UNIX socket are required.

Usage
-----

Here a simple example to fetch the name and hostgroups for all servers in the UP (0) state:

    >>> from mk_livestatus import Socket
    >>> s = Socket("/var/lib/icinga/rw/live")
    >>> q = s.query(
    ... """GET hosts
    ... Columns: name groups
    ... Filter: state = 0
    ... Limit: 1
    ... """)
    >>> q.get_list()
    [{'name': 'example.com', 'groups': ['ssh', 'snmp', 'smtp-server', 'ping-server', 'http-server', 'debian-server', 'apache2']}]
    >>> q.get_dict('name')
    {'example.com': {'name': 'b4b-highway.com', 'groups': ['ssh', 'snmp', 'smtp-server', 'ping-server', 'http-server', 'debian-server', 'apache2']}}

The call to `get_list` returns the rows as a list of dictionaries while `get_dict` requires one argument which specifies the column name which is to be used as the key for the entries in the dictionaries.

TODO
----

* Implement `get_column_list` to fetch a single column as a list.
* Test with INET sockets.

For more information please visit the `python-mk-livestatus website`_.

.. _python-mk-livestatus website: http://git.fladi.at/python-mk-livestatus.git/

