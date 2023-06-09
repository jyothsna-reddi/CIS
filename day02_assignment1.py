# list_a=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
# list_b=["monday","tuesday","wednesday","thursday","saturday","sunday"]


list_a=input("Enter input").split(",")
list_b=input("enter input").split(",")

length=len(list_a)
for each in range(length):
    if list_a[each] != list_b[each]:
        out1=list_a[each]
        list_b.insert(each,out1)

print(list_b)
