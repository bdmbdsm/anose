from anose.readers import read_file_at_once


class TestReadFileAtOnce(object):

    def test_ok(self, tmp_file_name):
        TESTDATA = 'otrpotr'
        with open(tmp_file_name, 'w') as f:
            f.write(TESTDATA)

        res = read_file_at_once(tmp_file_name)
        assert res == TESTDATA
