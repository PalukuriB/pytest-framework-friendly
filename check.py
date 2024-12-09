import tables_function as chinnu
import re
a = chinnu.print_tables(8)
l = []
for i in a:
    l.append(i) 
string_1 =""
for i in l:
    string_1=(string_1 +",") + i 
gang = string_1.lstrip(',') 

output = re.findall('([0-9]{1,2}\sX\s[0-9]{1,2}\s=\s[0-9]{1,2}).?',gang)
print(output) 
