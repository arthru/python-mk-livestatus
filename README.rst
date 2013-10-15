Python MK Livestatus parser
===========================

:Author: Michael Fladischer
:Version: 0.2

.. contents::

Access the data returned from MK Livestatus queries as Python lists or dictionaries. 
It does this by sending queries to the MK Livestatus UNIX socket and parses the returned rows. 
Read/write permission to the UNIX socket are required.

Usage
-----

Here a simple example to fetch the name and hostgroups for all servers in the UP (0) state:

    >>> from mk_livestatus import Socket
    >>> s = Socket("/var/lib/icinga/rw/live")
    >>> q = s.hosts.columns('name', 'groups').filter('state = 0')
    >>> print q
    GET hosts
    Columns: name groups
    Filter: state = 0
	
	
    >>> q.call()
    [{'name': 'example.com', 'groups': ['ssh', 'snmp', 'smtp-server', 'ping-server', 'http-server', 'debian-server', 'apache2']}]

``s.hosts`` returns a Query to the ``hosts`` resources on Nagios. The ``columns`` and ``filter`` methods modify our query and return it, so we can chain the calls. The call to `call` method returns the rows as a list of dictionaries. 

If you use xinetd to bind the Unix socket to a TCP socket (like explained `here <http://mathias-kettner.de/checkmk_livestatus.html#Livestatus%20via%20xinetd>`_), you can create the socket like :

    >>> s = Socket(('192.168.1.1', 6557))

For more information please visit the `python-mk-livestatus website`_. Information about MK Livestatus and it's query syntax is available at the `mk-livestatus website`_.

.. _python-mk-livestatus website: https://github.com/arthru/python-mk-livestatus
.. _mk-livestatus website: http://mathias-kettner.de/checkmk_livestatus.html

