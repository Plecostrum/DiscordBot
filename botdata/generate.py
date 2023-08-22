import query


def getFile():
    return open("./botdata/files/dnd.txt", "r")


def populateDatabase(connection , file):
    ruleName=''
    ruleDesc = ''
    ruleType = ''
    temp = ''
    for x in file:
        x = x.strip()
        if "##" in x:
            x = x.split('##')
            if(ruleDesc != ''):
                query.add_rule(connection,ruleName,ruleDesc,ruleType)
                ruleDesc = ''
            ruleType = toString(x)
        elif "++" in x:
            if(ruleDesc != ''):
                query.add_rule(connection,ruleName,ruleDesc,ruleType)
                ruleDesc = ''
            x = x.split('++')
            ruleName = toString(x)
        else:
            ruleDesc += x + '\n'
    ruleDesc += temp
    query.add_rule(connection,ruleName,ruleDesc,ruleType)
    print("Generated")
    
                   
def toString(array):
    return ''.join(array)
    
def main():
    connection = query.connect()
    query.create_tables(connection)
    file = getFile()
    populateDatabase(connection, file)

main()