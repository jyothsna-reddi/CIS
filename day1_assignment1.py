list_a=['J','V','S','S']
list_b=['D','D','R','V']
new_list=[]
for each1 in list_a:
    for each2 in list_b:
        new_list.append(each1+each2)
        list_b.remove(each2)
        break

print(new_list)