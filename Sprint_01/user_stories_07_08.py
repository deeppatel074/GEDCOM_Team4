import json
from dateutil.parser import parse
from Sprint_01 import families_json
from Sprint_01 import individuals_json

def US07():
    error_story7 = []

    for item in individuals_json:
        item = json.loads(item)
        if int(item["current_age"])>=150 and item["death_date"] == "N/A":
            error_story7.append("ERROR: Birthday of Individual with id " + item["id"] + " is of age greater than 150.")
        elif int(item["current_age"])>=150 and item["death_date"] !="N/A":
            error_story7.append("ERROR: Birthday of Individual with id " + item["id"] + " is no longer alive is of age greater than 150.")
    return error_story7
    
US07()

def US08():
    error_story8 = []
    for item in families_json: 
        item = json.loads(item)
        fam_child = item["children"]
        marriage_date = item["marriage_date"]
        divorce_date = item["divorced_date"]
        error = []
        convert_string = eval(fam_child) if fam_child!="N/A" else "N/A"
        if marriage_date!="N/A" and divorce_date == "N/A" and convert_string!="N/A":
            for i in individuals_json:
                i = json.loads(i)
                if i["id"] in convert_string:
                    if parse(i["birth_date"]) < parse(marriage_date):
                        error_story8.append("ERROR: Birth date for individual " + i["id"] + " is before the parents marriage date")
        elif marriage_date != "N/A" and divorce_date!= "N/A" and convert_string!="N/A":
            for i in individuals_json:
                i = json.loads(i)
                if i["birth_date"]!="N/A":
                    x = parse(i["birth_date"]) - parse(divorce_date)
                    arr = str(x)
                    days = int(arr.split(" ")[0])
                    if i["id"] in convert_string:
                        if parse(i["birth_date"]) < parse(marriage_date):
                            error_story8.append("ERROR: Birth date for individual " + i["id"] + " is before the parents marriage date")
                        elif days>270:
                            error_story8.append("ERROR: Birth date for individual " + i["id"] + " is 9 months after the parents divorce date")
    
    return error_story8

US08()