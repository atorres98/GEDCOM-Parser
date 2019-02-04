def gedParse(file): #function accepts a file and opens/reads it 
    file_object = open(file)
    # iterate through each line in the file
    for line in file_object:
        print ("--> " + line) #print each line
        # split each line into a list
        lineList = line.split(" ")
        print(lineList)
        # assume valid unless proven otherwise
        global valid
        valid = "Y"
        # define level, tag, and arguments in each line
        level = lineList[0]
        global tag
        global ID
        global args
        # arrays of valid level 0/1 tags (based on project doc provided on CANVAS)
        valL0Tags = ["HEAD\n", "TRLR\n", "NOTE", "FAM\n", "INDI\n"]
        valL1Tags = ["NAME", "SEX", "BIRT\n", "DEAT\n", "FAMC", "FAMS", "MARR", "HUSB", "WIFE", "DIV\n", "CHIL"]
        
        #check if each tag for each level is valid
        if int(level) == 0: #apply conditions when level is 0       
            if len(lineList) < 3: #if line is less than 3 elements long, there are no arguments USUALLY TRLR & HEAD
                tag = lineList[1]
                if str(tag) not in valL0Tags:
                    valid = "N"
                else:
                    valid = "Y"
                print ("<-- |" + level + "|" + tag + "|"+ valid +"|")
            elif lineList[2] == "FAM\n" or lineList[2] == "INDI\n": #if tag is FAM or INDI there is an ID in lineList[1]
                tag = lineList[2]
                ID = lineList[1]
                print ("<-- |" + level + "|" + tag + "|"+ valid +"|" + str(ID))
            else: #there are arguments but no ID = "NOTES"
                tag = lineList[1]
                if str(tag) not in valL0Tags:
                    valid = "N"
                else:
                    valid = "Y"
                args = lineList[2:]
                print ("<-- |" + level + "|" + tag + "|"+ valid +"|" + str(' '.join(args)))
        elif int(level) == 1:  #apply conditions when level is 1
            if len(lineList) < 3: #if line is less than 3 elements long, there are no arguments USUALLY DIV, MARR, DEAT, & BIRT
                tag = lineList[1]
                if str(tag) not in valL1Tags:
                    valid = "N"
                else:
                    valid = "Y"
                print ("<-- |" + level + "|" + tag + "|"+ valid +"|")
            # FAM and INDI have IDs that come before the tag
            elif lineList[2] == 'FAM\n' or lineList[2] == 'INDI\n':
                tag = lineList[2]
                ID = lineList[1]
                # print the output
                print ("<-- |" + level + "|" + tag + "|"+ valid + "|" + str(ID))
            else:
                tag = lineList[1]
                if str(tag) not in valL1Tags:
                    valid = "N"
                else:
                    valid = "Y"
                args = lineList[2:]
                print ("<-- |" + level + "|" + tag + "|"+ valid +"|" + str(' '.join(args)))
        elif int(level) == 2: #apply conditions when level is 2
            tag = lineList[1]
            args = lineList[2:]
            if tag != "DATE":
                valid = "N"
            print ("<-- |" + level + "|" + tag + "|"+ valid + "|" + str(' '.join(args)))
        elif int(level) < 0 or int(level) > 2: #apply conditions when level provided is not a valid level
            valid = "N"
            if len(lineList) <3:
                tag = lineList[1]
                print ("<-- |" + level + "|" + tag + "|"+ valid +"|")
            else:
                args = lineList[2:]
                print ("<-- |" + level + "|" + tag + "|"+ valid +"|" + ' '.join(args))


# test with test file
# gedParse('proj02test.ged')
gedParse('Project01.ged')