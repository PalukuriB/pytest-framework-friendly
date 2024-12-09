import subprocess

    # ------------------------ PROCEDURAL TESTING IN PYTEST ------------------------------

# It will run the (test file) different python file which is not return code in this current file
# Procedural Testing using subprocess package and check_output method and converting byte format into string 
# And Storing the string results in a list for accessing those strings by indexing. thats why used split by new line

result = ((subprocess.check_output("python tables_procedural_testing.py")).decode()).split('\n')
print(len(result))


def test_first_line():
    out = result[0].rstrip('\r')
    assert out == "5 X 1 = 5"

def test_middle_line():
    out_1 = result[4].rstrip('\r')
    assert out_1 == "5 X 5 = 25"

def test_last_line():
    out_2 = result[9].rstrip('\r')
    assert out_2 == "5 X 10 = 50"

def test_membership_check():
    string = "Palukuri Bhashwanth"
    assert "Bhashwanth" in string 

def test_user_line():
    out_3 = result[2].rstrip('\r')
    assert "5 X 3 = 15" in out_3  

def test_total_table():
    assert len(result)-1 == 10 

def test_type_of_result():
    print(type(result))
    assert type(result).__name__  == 'list'
