import datetime
import json
from dateutil.parser import parse
from Sprint_01 import individuals_json
from Sprint_01 import families_json
def US01():
    error = []
    today = datetime.datetime.today()
    for item in individuals_json:
        item = json.loads(item)
        if item["birth_date"] != "N/A":
            if parse(item["birth_date"]) > today :
                error.append("Error: Birthday at "+item['id']+" of "+item['name']+" should before current date")
        if item["death_date"] != "N/A":
            if parse(item["death_date"]) > today :
                error.append("Error: Death at "+item['id']+" of "+item['name']+" should before current date")
    for item in families_json:
        item = json.loads(item)
        if item['marriage_date'] != 'N/A':
            if parse(item["marriage_date"]) > today :
                error.append("Error: Marriage in "+item['family_id']+" of "+item['husband_name']+ " and "+item['wife_name']+" should before current date")
        if item['divorced_date'] != 'N/A':
            if parse(item["divorced_date"]) > today :
                error.append("Error: Divorced in "+item['family_id']+" of "+item['husband_name']+ " and "+item['wife_name']+" should before current date")
    # print(error)
    for i in error:
        print(i)
US01()
def US02():
    error = []
    for family in families_json:
        family = json.loads(family)
        if family['marriage_date'] != 'N/A':
            marriage_date = parse(family["marriage_date"])
        for individual in individuals_json:
            individual = json.loads(individual)
            if individual['birth_date'] != "N/A":
                birth_date = parse(individual["birth_date"])
            if individual['id'] == family['husband_id']:
                if marriage_date < birth_date:
                    error.append("Error: Birth should not occurs after marriage in "+ individual['id'])
            if individual['id'] == family['wife_id']:
                if marriage_date < birth_date:
                    error.append("Error: Birth should not occurs after marriage in "+ individual['id'])
    # print(error)
    for i in error:
        print(i)
US02()
