import sys 
tags = ["INDI","NAME","SEX","BIRT","DEAT","FAMC","FAMS","FAM","MARR","HUSB","WIFE","CHIL","DIV","DATE","HEAD","TRLR","NOTE"]
file = open('./Project_02.ged',mode='r') 
content = file.readlines()
output_array = []
a = "--> " + content[0]
print(a) 
output_array.append(a)

n = len(content)
for i in range(1,n):
    content[i] = content[i].rstrip('\n')
    b = "-->" + content[i]
    print(b)
    output_array.append(b)
    c = content[i].split(" ")
    if int(c[0]) == 0:
        if c[1] in tags:
            bool = "Y"
        else:
            bool = "N"
        if len(c) > 2:
            exception_tags = ["INDI","FAM"]
            if c[2] in exception_tags:
                exception_bool = True
                bool_excep = "Y"
            else:
                exception_bool = False
            if not exception_bool:
                join = ' '.join(c[2:])
                out = "<-- "+c[0] + "|" + c[1] + "|" + bool + "|" + join
                print(out)
                output_array.append(out)
            else:
               out = "<-- "+c[0] + "|" + c[2] + "|" + bool_excep + "|" + c[1]
               print(out)
               output_array.append(out)
        else:
            out = "<--"+c[0] + "|" + c[1] + "|" + bool
            print(out)
            output_array.append(out)

    if int(c[0])!= 0 :
        if c[1] in tags:
            bool = "Y"
        else:
            bool = "N"
        if len(c) > 2:
            join = ' '.join(c[2:])
            out = "<--"+c[0] + "|" + c[1] + "|" + bool + "|" + join
            print(out)
            output_array.append(out)
        else:
            out = "<--"+c[0] + "|" + c[1] + "|" + bool
            print(out)
            output_array.append(out)
file.close()

with open('./output.txt', 'w') as fp:
    for item in output_array:
        fp.write("%s\n" % item)





