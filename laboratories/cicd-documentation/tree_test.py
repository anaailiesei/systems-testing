import tree

def test_find():
    t = tree.Tree()
    assert(t.find(1) == None)
    t.add(3)
    t.add(4)
    assert(t.find(2) == None)
    assert(t.find(4).data == 4)