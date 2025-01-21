import subprocess

final = (subprocess.check_output("python Basic.py").decode()).split('\n')
print(final)

def test_start_index_match():
    result = int(final[0].rstrip('\r'))
    assert 1 == result, f"please give the check the input fromat"
