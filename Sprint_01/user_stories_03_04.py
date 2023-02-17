import json
from dateutil.parser import parse

from Sprint_01 import families_json
from Sprint_01 import individuals_json

# USER STORY 03 STARTS
# Description - Person's birth date should not be after their date death
def validate_births():
    result = []
    for item in individuals_json:
        item = json.loads(item)
        birth_date = item['birth_date']
        death_date = item['death_date']
        if birth_date == 'N/A':
            result.append(f"Error: Person {item['name']} does not have date of birth")
            # Throw error - birth date cannot be N/A
        elif death_date != 'N/A' and parse(birth_date) > parse(death_date):
            result.append(f"Error: Date of death is before birth date for {item['name']}")
    print(result)
    return result

validate_births()
# USER STORY 03 ENDS *********************

# USER STORY 04 STARTS *******************
# Description - Wedding date should be before divorce date
def validate_relations():
    result = []
    for item in families_json:
        item = json.loads(item)
        marriage_date = item['marriage_date']
        divorced_date = item['divorced_date']
        #[family_id,marriage_date,divorced_date,husband_id,husband_name,wife_id,wife_name,children]
        if divorced_date != 'N/A' and parse(marriage_date) > parse(divorced_date):
            result.append(f"Error: Wedding date is after divorce date for family {item['family_id']}")
    print(result)
    return result

validate_relations()
# USER STORY 04 ENDS
