"""
Scope:
1.Enter and 10 names in list
2.Title case them
3.Remove duplicates 
4.Sort those name is acending order of their first name
"""
name_list=[]
title_case_name=[]
duplicates_name=[]
final_name_list=[]
for i in range(5):
    user_name=input("Enter a name : ")
    name_list.append(user_name)
for list_name in name_list:
    first_name, last_name=list_name.split(" ")
    title_case_name.append(first_name.title()+" "+last_name)
print(title_case_name)
for list_name in title_case_name:
    first_name, last_name=list_name.split()
    if first_name not in duplicates_name:
        final_name_list.append(first_name+" "+last_name)
        duplicates_name.append(first_name)
    else:
        continue
print(final_name_list)
print(sorted(final_name_list, key=lambda x: x.split()))






