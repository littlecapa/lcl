from lcl.stack import Stack

def test_stack():
    testStr = "Test"
    s = Stack()
    assert s.is_empty() == True
    s.push(testStr)
    assert s.is_empty() == False
    assert s.top() == testStr
    assert s.len() == 1
    assert s.pop() == testStr
    assert s.len() == 0
    assert s.top() == None