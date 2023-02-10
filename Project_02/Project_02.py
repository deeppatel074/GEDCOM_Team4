import logging

def fileReader(path):
    with open(path,'r') as file:
        for line in file.readlines():
            line = line.strip()
            words = line.split()
            wordLength = len(words)
            if 1<wordLength<=2:
                words.append('')
            elif wordLength > 2:
                words = line.split(" ", 2)
            else:
                logging.error('Inappropriate value')
            yield words


def processFile(path,tagList,subTagList):
    for level, tag, argument in fileReader(path):
        print("-->", level, tag, argument)
        output = list()
        tagListLevel = False
        subTagListLevel = False
        if argument not in ['INDI', 'FAM']:
            for selectedTag, selectedLevel in tagList.items():
                if level == selectedLevel and tag == selectedTag:
                    tagListLevel = True
                    break


        else:
            subTagListLevel = True
            for selectedTag, selectedLevel in subTagList.items():
                if level == selectedLevel and argument == selectedTag:
                    tagListLevel = True
                    break

        if (tagListLevel and subTagListLevel) or (tagListLevel and not subTagListLevel) or (not tagListLevel and subTagListLevel):
            output.append(level)
            elem = argument if (tagListLevel and subTagListLevel) or (not tagListLevel and subTagListLevel) else tag
            output.append(elem)

            elem = "Y" if (tagListLevel and subTagListLevel) or (tagListLevel and not subTagListLevel) else 'N'
            output.append(elem)

            elem = argument if tagListLevel and not subTagListLevel else tag
            output.append(elem)

        else:
            output= [level + " " + tag,'N',argument]
        output = "|".join(output)
        print("<-- {0}".format(output))


path = './Nirav_CS555_Gedcom.ged'
tagList = {'DIV': '1', 'DATE': '2', 'HEAD': '0', 'TRLR': '0', 'NOTE': '0', 'NAME': '1', 'SEX': '1',
                  'MARR': '1', 'HUSB': '1', 'WIFE': '1', 'CHIL': '1', 'BIRT': '1', 'DEAT': '1', 'FAMC': '1',
                  'FAMS': '1'}
subTagList = {'FAM': '0', 'INDI': '0'}
processFile(path,tagList,subTagList)