from dateutil.parser import parse
from Sprint_01 import families_json
from Sprint_01 import individuals_json
import json

# User Story 05 - Marriage before death

def US05():
    errors = []
    for family in families_json:
        family = json.loads(family)
        husband_id = family['husband_id']
        wife_id = family['wife_id']
        marriage_date = family['marriage_date']
        husband_death_date = None
        wife_death_date = None
        for individual in individuals_json:
            individual = json.loads(individual)
            if individual['id'] == husband_id:
                if individual['death_date'] != 'N/A':
                    husband_death_date = individual['death_date']
            elif individual['id'] == wife_id:
                if individual['death_date'] != 'N/A':
                    wife_death_date = individual['death_date']
        if marriage_date != 'N/A':
            if husband_death_date and parse(marriage_date) > parse(husband_death_date):
                errors.append("Error: Marriage of family {} occurred after death of husband".format(family['family_id']))
            if wife_death_date and parse(marriage_date) > parse(wife_death_date):
                errors.append("Error: Marriage of family {} occurred after death of wife".format(family['family_id']))
    print(errors)
    return errors

US05()

# User Story 06 - Divorce can only occur before death of both spouses

def US06():
    errors = []
    for family in families_json:
        family = json.loads(family)
        husband_id = family['husband_id']
        wife_id = family['wife_id']
        divorced_date = family['divorced_date']
        husband_death_date = None
        wife_death_date = None
        for individual in individuals_json:
            individual = json.loads(individual)
            if individual['id'] == husband_id:
                if individual['death_date'] != 'N/A':
                    husband_death_date = individual['death_date']
            elif individual['id'] == wife_id:
                if individual['death_date'] != 'N/A':
                    wife_death_date = individual['death_date']
        if divorced_date != 'N/A':
            if husband_death_date and parse(divorced_date) > parse(husband_death_date):
                errors.append("Error: Divorce of family {} occurred after death of husband".format(family['family_id']))
            if wife_death_date and parse(divorced_date) > parse(wife_death_date):
                errors.append("Error: Divorce of family {} occurred after death of wife".format(family['family_id']))
    print(errors)
    return errors

US06()