import csv
import socket


class Query(object):
    def __init__(self, conn, resource):
        self._conn = conn
        self._resource = resource
        self._columns = []
        self._filter = []

    def call(self):
        if self._columns:
            return self._conn.call(str(self), self._columns)
        return self._conn.call(str(self))

    def __str__(self):
        request = 'GET %s' % (self._resource)
        if self._columns:
            request += '\nColumns: %s' % (' '.join(self._columns))
        if self._filter:
            for filter_line in self._filter:
                request += '\nFilter: %s' % (filter_line)
        return request + '\n\n'

    def columns(self, *args):
        self._columns = args
        return self

    def filter(self, filter_str):
        self._filter.append(filter_str)
        return self


class NagiosSocket(object):
    def __init__(self, hostname, port):
        self.hostname = hostname
        self.port = port

    def __getattr__(self, name):
        return Query(self, name)

    def call(self, request, columns=None):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.hostname, self.port))
            s.send(request)
            s.shutdown(socket.SHUT_WR)
            csv_lines = csv.DictReader(s.makefile(), columns, delimiter=';')
            return list(csv_lines)
        finally:
            s.close()
