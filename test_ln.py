import os
import ln


def test_ln(tmpdir):
    a_file = tmpdir.ensure("a_file", file=True)
    a_link = tmpdir.join("a_link")
    ln.ln(from_=a_link, to="a_file")
    assert os.path.islink(a_link)
    realpath = os.path.realpath(a_link)
    assert os.path.samefile(realpath, a_file)
