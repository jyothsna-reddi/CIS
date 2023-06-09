user_input,current_quarter=input("Enter the input in the format of YYYYMM: ").split(',')
current_month=int(user_input[4:])
current_year=int(user_input[:4])

if current_month>12 or current_month==0:
    user_input=input("Please enter valid input: ")
        
dict_a={}
current_month=int(user_input[4:])
current_year=int(user_input[:4])
#current_quarter=input("Enter Current Quarter:")

def example(user_input,current_quarter):
    previous_month=12 if (current_month-3)<1 else current_month-3
    if previous_month>=1 and previous_month<=3:
        previous_quarter="Q1"
    elif previous_month>=3 and previous_month<=6:
        previous_quarter="Q2"
    elif previous_month>=6 and previous_month<=9:
        previous_quarter="Q3"
    else:
        previous_quarter="Q4"
    dict_a["Previous_quarter"]=str(previous_quarter)+"_"+str(current_year) if current_month-1>=3 else str(previous_quarter)+"_"+str(current_year-1)
    dict_a["Previous_month"] = (str(current_year)+" "+str(current_month-1) if (current_month-1)>1 else str(current_year-1)+str(12)) 
    dict_a["Current Quarter"]=str(current_quarter)+"_"+str(current_year)
    dict_a["Future Quarter"] = str(current_year+1)+" "+str(current_month-1) if current_month-1>1 else str(current_year)+str(12)
example(user_input,current_quarter)
print(dict_a)