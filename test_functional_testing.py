import tables_function as chinnu
import re 

opt = chinnu.print_tables(10)
l =[]
for i in opt:
    l.append(i)
print(l)

def test_length():
    assert len(l) is 10 

def test_first_index_value():
    out = type(l[0]).__name__
    assert out == 'str' 

def test_check_string_value_in_list():
    assert l[0] in l 

def test_generater_type_of_result():
    assert type(opt).__name__ =="generator"

def test_by_using_re():
    for ram in l:
        assert re.match('([0-9]{1,2}.X.[0-9]{1,2}.=.[0-9]{1,2}).?',ram) 









