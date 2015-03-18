import mock

from mk_livestatus import Socket


@mock.patch('mk_livestatus.livestatus.socket.socket')
def test_socket(socket_mock):
    socket_mock.return_value.makefile.return_value.read.return_value = (
        '[["name","groups","perf_data"],'
        '["hbops",["archlinux","linux","hashbang"],'
        '"rta=0.168000ms;1000.000000;3000.000000;0.000000 pl=0%;100;100;0"]]'
    )
    s = Socket("/var/lib/icinga/rw/live")
    q = s.hosts
    r = q.call()
    expected = [{
        'name': 'hbops',
        'groups': ['archlinux', 'linux', 'hashbang'],
        'perf_data': "rta=0.168000ms;1000.000000;3000.000000;0.000000 pl=0%;"
                     "100;100;0",
    }]
    assert r == expected
