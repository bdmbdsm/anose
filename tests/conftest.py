import pytest

from os import remove
from tempfile import NamedTemporaryFile


@pytest.fixture
def tmp_file_name():
    """Creates an empty temporary file

    Returns the absolute path to that file.
    """
    fname = NamedTemporaryFile(mode='w', delete=False).name
    yield fname
    remove(fname)
