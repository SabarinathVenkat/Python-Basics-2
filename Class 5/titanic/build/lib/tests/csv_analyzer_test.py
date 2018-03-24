from nose.tools import *
from adapters.csv_analyzer import CSVAnalyze

df = None

def setup_module():
    global df
    data = ["ID,NAME,PRICE,QTY", "1,A,200,1000", "2,B,400,100"]
    with open('../data/test.csv','w') as f:
        f.write("\n".join(data))
    df = CSVAnalyze ( '../data/test.csv' )

def teardown():
    pass

def test_analyze():

    print df.columns
    assert df.columns == ["ID","NAME","PRICE","QTY"]

def test_maths():
    assert df.count() == 2



