import pyConTextNLP.itemData as itemData
from pathlib import PurePath
import os
import pytest


@pytest.fixture(scope="session")
def get_tmp_dirs():
    pass

def test_get_fileobj_1():
    fobj = PurePath(PurePath(os.path.abspath(__file__)).parent, "..", "..", "KB", "test.yml")
    yaml_fo = itemData.get_fileobj(str(fobj))
    assert yaml_fo

def test_get_fileobj_2():
    wdir = PurePath(os.path.abspath(__file__))#, "..", "..", "KB")
    fobj = PurePath(wdir.parent, "..", "..", "KB", "test.yml")
    yfo = itemData.get_fileobj("file://"+str(fobj))
    assert yfo

def test_get_fileobj_3():
    yfo = itemData.get_fileobj(
            "https://raw.githubusercontent.com/chapmanbe/pyConTextNLP/master/KB/test.yml")
    assert yfo
