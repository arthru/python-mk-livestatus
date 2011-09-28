import socket

class Socket(object):

    def __init__(self, peer):
        self.peer = peer

    def query(self, query):
        if (len(self.peer) == 2):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        s.connect(self.peer)
        return Query(query, s)

class Query(object):

    def __init__(self, query, socket):
        self.query = query
        self.socket = socket
        self.result = None

    def _fetch(self):
        result = list()
        self.socket.send(self.query)
        self.socket.shutdown(socket.SHUT_WR)
        handle = self.socket.makefile()
        colpos = self.query.find("Columns:")
        if colpos > 0:
            compos = self.query.find("\n", colpos)
            if compos < 0:
                compos = len(self.query)
            columns = filter(bool, self.query[colpos+9:compos].split(' '))
        else:
            columns = handle.readline().split(';')
        for line in handle:
            result.append(dict(zip(columns, map(lambda (v): v.find(',') > 0 and v.strip(' \t\n\r').split(',') or v.strip(' \t\n\r'), line.split(';')))))
        self.result = result

    def get_list(self):
        if self.result is None:
            self._fetch()
        return self.result

    def get_dict(self, key):
        return dict(map(lambda (v): (v[key], v), self.get_list()))

