from prettytable import PrettyTable
import datetime
x = PrettyTable()
y = PrettyTable()

x.field_names = ["ID","Name", "Gender", "Birthday", "Age","Alive","Death","Child","Spouse"]

file = open('./gedcom.ged',mode='r') 
content = file.readlines()
dict_name = {}
sex = "N/A"
name = "N/A"
birth_date = "N/A"
family_spouse = "N/A"
family_child = "N/A"
current_age = "N/A"
alive = "TRUE"
death_date = "N/A"
zero_arr = []    
for i in range(len(content)):
    arr = content[i].split(" ")
    if len(arr)>2:
        arr[2] = arr[2].strip("\n")
        if arr[0] == "0" and arr[1]!= "FAM" and arr[2] == "INDI":
            zero_arr.append(i)
        if arr[0] == "0" and arr[2] == "FAM":
            last_variable = i
            break

i = zero_arr[0]
id = content[i].split(" ")[1].strip("@")
i+=1
while i<=last_variable:
    a = content[i].split(" ")
    a[-1] = a[-1].strip("\n")
    
    if a[0]!="0":
        if a[1] == "NAME":
            name = ' '.join(a[2:])
            i+=1
        elif a[1] == "SEX":
            if a[2] == "M":
                sex = "MALE"
            if a[2] == "F":
                sex = "FEMALE"
            i+=1
        elif a[1] == "GIVN":
            i+=1
        elif a[1] == "SURN":
            i+=1
        elif a[1] == "_MARN":
            i+=1 
        elif a[1] == "PLAC":
            i+=1
        elif a[1] == "FAMC":
            b = a[2].strip("@")
            family_child = "{" + "'" + b + "'" + "}"
            i+=1
        elif a[1] == "FAMS":
            b = a[2].strip("@")
            family_spouse = "{" + "'" + b + "'" + "}"
            i+=1
        elif a[1] == "BIRT":
            i+=1
            birth = content[i].split(" ")
            birth[-1] = birth[-1].strip("\n")
            if birth[1] == "DATE":
                birth_date = ' '.join(birth[2:])
                current_age = datetime.date.today().year - int(birth_date.split(" ")[2])
            i+=1
        elif a[1] == "DEAT":
            i+=1
            death = content[i].split(" ")
            death[-1] = death[-1].strip("\n")
            if death[1] == "DATE":
                death_date = ' '.join(death[2:])
                alive = "FALSE"
            i+=1
        else:
            i+=1   
            
    elif a[0] == "0":
        x.add_row([id,name,sex,birth_date,current_age,alive,death_date,family_child,family_spouse])
        dict_name[id] = name
        arr = content[i].split(" ")
        id = arr[1].strip("@")
        name = "N/A"
        sex = "N/A"
        birth_date = "N/A"
        family_spouse = "N/A"
        family_child = "N/A"
        death_date = "N/A"
        alive = "TRUE"
        i+=1

y.field_names = ["ID","Married","Divorced","HUSBAND ID","HUSBAND NAME","Wife ID","Wife Name","Children"]
i = last_variable + 1
end_index = len(content)


marriage_date = "N/A"
divorced_date = "N/A"
husband_id = "N/A"
husband_name = "N/A"
wife_id = "N/A"
wife_name = "N/A"
children = set()
family_id = content[last_variable].split(" ")[1].strip("@")

while i<end_index:
    arr = content[i].split(" ")
    arr[-1] = arr[-1].strip("\n")
    if arr[0]!="0":
        if arr[1] == "HUSB":
            husband_id = arr[2].strip("@")
            husband_name = dict_name[husband_id]
            i+=1
        elif arr[1] == "WIFE":
            wife_id = arr[2].strip("@")
            wife_name = dict_name[wife_id]
            i+=1
        elif arr[1] == "CHIL":
            children.add(arr[2].strip("@"))
            i+=1
        elif arr[1] == "MARR":
            i+=1
            marr_arr = content[i].split(" ")
            marr_arr[-1] = marr_arr[-1].strip("\n")
            if marr_arr[1] == "DATE":
                marriage_date = ' '.join(marr_arr[2:])
            i+=1
        elif arr[1] == "DIV":
            i+=1
            div_arr = content[i].split(" ")
            div_arr[-1] = div_arr[-1].strip("\n")
            if div_arr[1] == "DATE":
                divorced_date = ' '.join(div_arr[2:])
            i+=1
        else:
            i+=1
    elif arr[0] == "0":
        y.add_row([family_id,marriage_date,divorced_date,husband_id,husband_name,wife_id,wife_name,children])
        arr = content[i].split(" ")
        family_id = arr[1].strip("@")
        marriage_date = "N/A"
        divorced_date = "N/A"
        husband_id = "N/A"
        husband_name = "N/A"
        wife_id = "N/A"
        wife_name = "N/A"
        children = set()
        i+=1


print("Individual Table ----------------------------------------------------------------------------------->")
print(x)
print("\n")
print("Family Table ---------------------------------------------------------------------------------------------------->")
print(y)

        
        
        
        

    






