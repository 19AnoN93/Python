lis = "хых орн зыз выа нур лол кис сна"
List = lis.split()
for i in List:
    if i[::-1] == i:
        print(i)
    else:
        print("Nothing!")
        
        
