import subprocess 

result = (subprocess.check_output("python Basic.py").decode()).split('\n')
print(result)

def test_first_character():
    out = result[0].rstrip('\r')
    print(out)
    assert out == chr(1) 

def test_second_character():
    out_1 = result[1].rstrip('\r')
    print(out_1)
    assert out_1 == chr(2) 

def test_third_character():
    out_2 = result[2].rstrip('\r')
    print(out_2)
    assert out_2 == chr(3) 