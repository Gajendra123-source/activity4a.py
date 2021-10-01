#Jendra Poudel
#ISQA_3900-851, 09/25/2021


#This program will remove dublicates (repeated) data/char from a list and publish
#a new list with no dublicates
def Remove_dublicate(namesList):
    print("Initial List of Names\n ['barry','belinda','george','hank','kahn','karthik','maria','maria',"
          "'maria',,'maria','sam','sam','will']\n")

    print("List of unique names after removing dublicated names")

    final_list = []
    for num in namesList:
        if num not in final_list:
            final_list.append(num)
    return final_list

names = ['mary','bill','sam','maria','kahn','bill','barry','george','hank','belinda','maria','karthik']

print(Remove_dublicate(names))