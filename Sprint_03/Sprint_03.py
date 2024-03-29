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

def US15():
    res = []
    for item in families_json:
        item = json.loads(item)
        arr = None
        if item['children']!="N/A":
            arr = item['children'].split(',')
        if arr!= None:
            if len(arr)>=15:
                res.append("ERROR: FAMILY: US 15: Family with Family ID: " + item["family_id"]+" has more than 15 siblings")
    

    for i in res:
        print(i)
    return res
        

US15()


def US16():
    res = []
    name_dict = {}
    for item in individuals_json:
        item = json.loads(item)
        name_dict[item["id"]] = item["name"].split("/")[1].lstrip()
 

    for item in families_json:
        item = json.loads(item)
        if item["husband_name"]!="N/A":
            fam_name = item["husband_name"].split("/")[1].lstrip()
        else:
            fam_name = "N/A"
        if item['children']!="N/A":
            d = item['children']
            d = d[1:-1]
            arr = d.split(',')
            for i in range(len(arr)):
                arr[i] = arr[i].lstrip()
                arr[i] = arr[i].strip(" ' ")
            
            if fam_name!="N/A":
                for ele in arr:
                    if name_dict[ele]!= fam_name:
                        res.append("ERROR: FAMILY: INDIVIDUAL: US 16: Family Name of Individual " + ele + " is different from the family name")
    
    for i in res:
        print(i)
    return res

            
US16()

def US23():
    errors = []
    individuals_dict = {}

    for individual in individuals_json:
        individual = json.loads(individual)
        name = individual['name']
        birth_date = individual['birth_date']

        # check if individual with same name and birth date already exists
        if (name, birth_date) in individuals_dict:
            existing_individual = individuals_dict[(name, birth_date)]
            errors.append("ERROR: INDIVIDUAL: US23: Individual {} ({}) and {} ({}) have the same name and birth date".format(
                individual['id'], name, existing_individual['id'], existing_individual['name']))
        else:
            individuals_dict[(name, birth_date)] = individual

    for i in errors:
        print(i)
    return errors

US23()



def US24():
    errors = []
    families_dict = {}

    for family in families_json:
        family = json.loads(family)
        husband_name = family['husband_name']
        wife_name = family['wife_name']
        marriage_date = family['marriage_date']

        # check if family with same spouses names and marriage date already exists
        key = (husband_name, wife_name, marriage_date)
        if key in families_dict:
            errors.append("ERROR: FAMILY: US24: Family with the same spouse names and marriage date already exists: "  + " Husband Name: " + str(husband_name) +
              ", Wife Name: " + str(wife_name) + ", Marriage Date: " + str(marriage_date))
        else:
           
          families_dict[key] = family
          
    for i in errors:
        print(i)
    return errors

US24()

def US11():
     errors = []
     for family in families_json:
        family = json.loads(family)
        husband_id = family['husband_id']
        wife_id = family['wife_id']
        marriage_date = family['marriage_date']
        divorce_date = family.get('divorce_date')

        # Check if husband or wife is married to another person at the same time
        for other_family in families_json:
            other_family = json.loads(other_family)
            if other_family != family:
                if other_family['husband_id'] == husband_id and not other_family.get('divorce_date') \
                        and is_date_between(other_family['marriage_date'], marriage_date, other_family.get('divorce_date')):
                    errors.append("ERROR: FAMILY: US11: Husband " + str(husband_id) + " is married to two people at the same time")
                elif other_family['wife_id'] == wife_id and not other_family.get('divorce_date') \
                        and is_date_between(other_family['marriage_date'], marriage_date, other_family.get('divorce_date')):
                    errors.append("ERROR: FAMILY: US11: Wife " + str(wife_id) + " is married to two people at the same time")
         # Check if husband or wife is married to another person after divorce from current spouse
        if divorce_date:
            for other_family in families_json:
                other_family = json.loads(other_family)
                if other_family != family:
                    if other_family['husband_id'] == husband_id and other_family.get('divorce_date') \
                            and is_date_between(divorce_date, other_family['marriage_date'], other_family.get('divorce_date')):
                        errors.append("ERROR: FAMILY: US11: Husband " + str(husband_id) + " got married before divorce from previous spouse")
                    elif other_family['wife_id'] == wife_id and other_family.get('divorce_date') \
                            and is_date_between(divorce_date, other_family['marriage_date'], other_family.get('divorce_date')):
                        errors.append("ERROR: FAMILY: US11: Wife " + str(wife_id) + " got married before divorce from previous spouse")
     for i in errors:
        print(i)
     return errors

def is_date_between(start_date, check_date, end_date):
    if start_date and check_date and end_date:
        return start_date <= check_date <= end_date
    elif start_date and check_date:
        return start_date <= check_date
    elif check_date and end_date:
        return check_date <= end_date
    else:
        return False

US11()

def US12():
    errors = []
    for family in families_json:
        family = json.loads(family)
        children = family['children']
        if children != "N/A":
            convert_string = eval(children) if children!="N/A" else "N/A"
            mother_id = family['wife_id']
            father_id = family['husband_id']
            
            mother_birth_date = None
            father_birth_date = None

            for i in individuals_json:
                    i = json.loads(i)
                    if i['id'] == mother_id and i['birth_date'] != "N/A":
                        mother_birth_date = parse(i['birth_date'])
                    if i['id'] == father_id and i['birth_date'] != "N/A":
                        father_birth_date = parse(i['birth_date'])
            if mother_birth_date != None and father_birth_date != None and convert_string != 'N/A':
                for child_id in convert_string:
                    for i in individuals_json:
                        i = json.loads(i)
                        if i['id'] == child_id and i['birth_date'] != "N/A":
                            child_birth_date = parse(i['birth_date'])
                            diff_btw_mother = str(mother_birth_date - child_birth_date)
                            diff_btw_father = str(father_birth_date - child_birth_date)
                            if abs(int(diff_btw_mother.split(" ")[0])) > 21900 :
                                errors.append("ERROR: FAMILY: US12: Mother "+ mother_id +" is more than 60 years older than her child "+ i['id'])
                            if abs(int(diff_btw_father.split(" ")[0])) > 29200 :
                                errors.append("ERROR: FAMILY: US12: Father "+ father_id +" is more than 80 years older than his child "+ i['id'])

    for i in errors:
        print(i)
    return errors


US12()

# First cousions should not marry
def US19():
    errors = set()
    for family in families_json:
        family = json.loads(family)
        # print("FAMILY US19", family)
        husband_id = family['husband_id']
        wife_id = family['wife_id']
        husband_indi_record = {}
        wife_indi_record = {}
        if husband_id and wife_id:
            # print(husband_id, wife_id)
            for individual in individuals_json:
                individual = json.loads(individual)
                # print(individual)
                if individual['id'] == husband_id:
                    husband_indi_record = individual
                elif individual['id'] == wife_id:
                    wife_indi_record = individual
                    # print("INDIVIDUALS", husband_indi_record, wife_indi_record)
                if husband_indi_record and wife_indi_record:
                    husbands_family_id = husband_indi_record['family_child']
                    wifes_family_id = wife_indi_record['family_child']
                    if husbands_family_id != 'N/A' and wifes_family_id != 'N/A':
                        husbands_family_id = husbands_family_id.split("'")[1]
                        wifes_family_id = wifes_family_id.split("'")[1]
                        couples_parents_ids = []
                        for fam in families_json:
                            fam = json.loads(fam)
                            # print("FAM", husbands_family_id, wifes_family_id)
                            if fam['family_id'] in [wifes_family_id, husbands_family_id]:
                                # print("COUPLES PARENTS", couples_parents_ids)
                                couples_parents_ids = couples_parents_ids + [fam['husband_id'], fam['wife_id']]
                        if len(couples_parents_ids) > 0:
                            for each_fam in families_json:
                                siblings = []
                                each_fam = json.loads(each_fam)
                                children = each_fam['children']
                                if children != 'N/A':
                                    children = eval(children)
                                    siblings = list(filter(lambda sibling: sibling in children, couples_parents_ids))
                                if len(siblings) > 1:
                                    error = f"ERROR: FAMILY: US19: Couples with husband id {husband_indi_record['id']} and wife id {wife_indi_record['id']} are first cousins"
                                    errors.add(error)
    for error in errors:
        print(error)
    return errors
US19()

# Aunts and uncles should not marry their nieces or nephews

def validate_us20(prob_siblings, spouse_id, gender):
    for family in families_json:
        family = json.loads(family)
        children = family['children']
        if children != 'N/A':
            children = eval(children)
            siblings = list(filter(lambda sibling: sibling in children, prob_siblings))
            if len(siblings) > 1:
                if gender == "MALE":
                    return f"ERROR: FAMILY: US20: Husband with id {prob_siblings[0]} is uncle of his wife with id {spouse_id}"
                else:
                    return f"ERROR: FAMILY: US20: Wife with id {prob_siblings[0]} is aunt of her husband with id {spouse_id}"


def US20():
    errors = []
    for family in families_json:
        family = json.loads(family)
        # print("FAMILY US19", family)
        husband_id = family['husband_id']
        wife_id = family['wife_id']
        husband_indi_record = {}
        wife_indi_record = {}
        if husband_id and wife_id:
            # print(husband_id, wife_id)
            for individual in individuals_json:
                individual = json.loads(individual)
                # print(individual)
                if individual['id'] == husband_id:
                    husband_indi_record = individual
                elif individual['id'] == wife_id:
                    wife_indi_record = individual
                    # print("INDIVIDUALS", husband_indi_record, wife_indi_record)
                if husband_indi_record and wife_indi_record:
                    husbands_family_id = husband_indi_record['family_child']
                    wifes_family_id = wife_indi_record['family_child']
                    if husbands_family_id != 'N/A' and wifes_family_id != 'N/A':
                        husbands_family_id = husbands_family_id.split("'")[1]
                        wifes_family_id = wifes_family_id.split("'")[1]
                        wifes_parents = []
                        husbands_parents = []
                        for fam in families_json:
                            fam = json.loads(fam)
                            if fam['family_id'] == wifes_family_id:
                                wifes_parents = [fam['husband_id'], fam['wife_id']]
                            elif fam['family_id'] == husbands_family_id:
                                husbands_parents = [fam['husband_id'], fam['wife_id']]
                        error = None
                        if len(husbands_parents) > 0 and len(husbands_parents) > 0:
                            error = validate_us20([wife_indi_record['id']] + husbands_parents, husband_indi_record['id'], "FEMALE")
                            if error is not None:
                                print(error)
                                errors.append(error)
                                error = None
                            error = validate_us20([husband_indi_record['id']] + wifes_parents, wife_indi_record['id'], "MALE")
                            if error is not None:
                                print(error)
                                errors.append(error)
                                error = None
    return errors

US20()





            


        










        
        
        
        

    






