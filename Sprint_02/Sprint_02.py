from prettytable import PrettyTable
import datetime
import json
from dateutil.parser import parse
from datetime import date
from collections import defaultdict

x = PrettyTable()
y = PrettyTable()

individuals_json = []
families_json = []
x.field_names = ["ID","Name", "Gender", "Birthday", "Age","Alive","Death","Child","Spouse"]

file = open('gedcom.ged',mode='r') 
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
        j = json.dumps({"id":str(id),
                        "name":str(name),
                        "sex":str(sex),
                        "birth_date":str(birth_date),
                        "current_age":str(current_age),
                        "alive":str(alive),
                        "death_date":str(death_date),
                        "family_child":str(family_child),
                       "family_spouse":str(family_spouse)
                        })
        individuals_json.append(j)
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
        children = children if len(children)>0 else "N/A"
        y.add_row([family_id,marriage_date,divorced_date,husband_id,husband_name,wife_id,wife_name,children])
        z = json.dumps({
            "family_id":str(family_id),
            "marriage_date":str(marriage_date),
            "divorced_date":str(divorced_date),
            "husband_id":str(husband_id),
            "husband_name":str(husband_name),
            "wife_id":str(wife_id),
            "wife_name":str(wife_name),
            "children":str(children)
            })
        families_json.append(z)
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

def US36():
    res = []
    result_us36 = PrettyTable()
    result_us36.field_names = ["ID","Name", "Gender", "Birthday", "Age","Alive","Death","Child","Spouse"]
    for item in individuals_json:
        item = json.loads(item)
        birth_date = item["birth_date"]
        if birth_date!="N/A":
            today = str(date.today())
            x = parse(today) - parse(birth_date)
            arr = str(x)
            days = int(arr.split(" ")[0])
            if days<30 and days>0:
                res.append(([item['id'],item['name'],item['sex'],item['birth_date'],item['current_age'],item['alive'],item['death_date'],item['family_child'],item['family_spouse']]))
                result_us36.add_row([item['id'],item['name'],item['sex'],item['birth_date'],item['current_age'],item['alive'],item['death_date'],item['family_child'],item['family_spouse']])
    print("Individuals born in last 30 days ----------------------------------------------------------->")      
    print(result_us36)
    return res  


US36()

def US37():
    res = []
    result_us37 = PrettyTable()
    result_us37.field_names = ["ID","Name", "Gender", "Birthday", "Age","Alive","Death","Child","Spouse"]
    for item in individuals_json:
        item = json.loads(item)
        death_date = item["death_date"]
        if death_date!="N/A":
            today = str(date.today())
            x = parse(today) - parse(death_date)
            arr = str(x)
            days = int(arr.split(" ")[0])
            if days<30 and days>0:
                res.append(([item['id'],item['name'],item['sex'],item['birth_date'],item['current_age'],item['alive'],item['death_date'],item['family_child'],item['family_spouse']]))
                result_us37.add_row([item['id'],item['name'],item['sex'],item['birth_date'],item['current_age'],item['alive'],item['death_date'],item['family_child'],item['family_spouse']])
    print("Individuals who died in last 30 days ----------------------------------------------------------->")      
    print(result_us37)
    return res      

US37()

def US09():
    error_story9 = []
    for item in families_json: 
        item = json.loads(item)
        fam_child = item["children"]
        convert_string = eval(fam_child) if fam_child!="N/A" else "N/A"
        for i in individuals_json:
            i = json.loads(i)
            if i["id"] == item["wife_id"]:
                if i["death_date"] != 'N/A' and convert_string != "N/A":
                    for j in individuals_json:
                        j = json.loads(j)
                        if j["id"] in convert_string:
                            if j["birth_date"] != "N/A":
                                if parse(j["birth_date"]) > parse(i["death_date"]):
                                    error_story9.append("ERROR: INDIVIDUAL: US09: Birth date for individual " + j["id"] + " is after the mother death date")
            elif i["id"] == item["husband_id"]:
                if i["death_date"] != 'N/A' and convert_string != "N/A":
                    for j in individuals_json:
                        j = json.loads(j)
                        if j["id"] in convert_string:
                            if j["birth_date"] != "N/A":
                                x = parse(j["birth_date"]) - parse(i["death_date"])
                                arr = str(x)
                                days = int(arr.split(" ")[0])
                                if days>270:
                                    error_story9.append("ERROR: INDIVIDUAL: US09: Birth date for individual " + j["id"] + " is after 9 months of the father death date")    
    for i in error_story9:
        print(i)
    return error_story9

US09()

def US10():
    error = []
    for item in families_json: 
        item = json.loads(item)
        if item['marriage_date'] != "N/A":
            hus_id = item["husband_id"]
            wfs_id = item["wife_id"]
            marr_date = item["marriage_date"]
            for i in individuals_json:
                i = json.loads(i)
                if i["birth_date"] != "N/A":
                    if i["id"] == hus_id:
                        x = parse(marr_date) - parse(i["birth_date"])
                        arr = str(x)
                        days = int(arr.split(" ")[0])
                        if days >= 0:
                            if days <= 5110:
                                error.append("ERROR: INDIVIDUAL: US10: Marriage for "+ i["id"]+" should be after 14 year of the age")

                    elif i["id"] == wfs_id:
                        x = parse(marr_date) - parse(i["birth_date"])
                        arr = str(x)
                        days = int(arr.split(" ")[0])
                        if days >= 0:
                            if days <= 5110:
                                error.append("ERROR: INDIVIDUAL: US 10: Marriage for "+ i["id"]+" should be after 14 year of the age")
    for i in error:
        print(i)
    return error

US10()


def US17():
    error = []
    result_us17 = PrettyTable()
    result_us17.field_names = ["ID", "Married", "Divorced", "Husband ID", "Wife ID", "Wife Name", "Children"]
    for record in families_json:
        record = json.loads(record)
        children = record["children"][1:-1].split(",")
        for child_id in children:
            if (child_id == "'" + record["wife_id"] + "'" or child_id == "'" + record["husband_id"] + "'"):
                print("ERROR: FAMILY: US17: No marriages to descendents "+ record["husband_id"]+" "+record["wife_id"]+" "+child_id)
                error.append("ERROR: FAMILY: US17: No marriages to descendents "+ record["husband_id"]+" "+record["wife_id"]+" "+child_id)
    
    return error
US17()


def US18():
    error = []
    result_us18 = PrettyTable()
    result_us18.field_names = ["ID", "Married", "Divorced", "Husband ID", "Wife ID", "Wife Name", "Children"]
    for record in families_json:
        record = json.loads(record)
        children = record["children"][1:-1].split(",")
        for (index, child) in enumerate(children):
            children[index] = child.strip()
        if ("'" + record["wife_id"] + "'" in children or "' " + record["wife_id"] + "'" in children) and ("'" + record["husband_id"] + "'" in children or "' " + record["husband_id"] + "'" in children):
            print("ERROR:","FAMILY:","US18:","No marriages to siblings", "Husband", record["husband_id"], "Wife", record["wife_id"])
            error.append("ERROR: FAMILY: US18: No marriages to siblings Husband" + record["husband_id"] + "Wife" + record["wife_id"])
    
    return error
US18()

def US21():
    errors = []
    for family in families_json:
        family = json.loads(family)
        husband_id = family['husband_id']
        wife_id = family['wife_id']
        for individual in individuals_json:
            individual = json.loads(individual)
            if individual['id'] == husband_id and individual['sex'] != 'MALE':
                errors.append("ERROR: INDIVIDUAL: US21: Husband {} in family {} is not male".format(husband_id, family['family_id']))
            elif individual['id'] == wife_id and individual['sex'] != 'FEMALE':
                errors.append("ERROR: INDIVIDUAL: US21: Wife {} in family {} is not female".format(wife_id, family['family_id']))
    for i in errors:
        print(i)
    return errors

US21()


def US22():
    errors = []
    individual_ids = set()
    family_ids = set()
    
    # Check individual IDs
    for individual in individuals_json:
        individual = json.loads(individual)
        if individual['id'] in individual_ids:
            errors.append("ERROR: INDIVIDUAL: US22: Individual ID {} is not unique".format(individual['id']))
        else:
            individual_ids.add(individual['id'])
    
    # Check family IDs
    for family in families_json:
        family = json.loads(family)
        if family['family_id'] in family_ids:
            errors.append("ERROR: FAMILY: US22: Family ID {} is not unique".format(family['family_id']))
        else:
            family_ids.add(family['family_id'])
    
    for i in errors:
        print(i)
    return errors

US22()












        
        
        
        

    






