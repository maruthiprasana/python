# regex topic

#  maruthi=[]#method 1
#  print(type(maruthi))
#  maruthi=list([2,"ace",2.4,False])method 2(built-in function)
#  print(maruthi)

# # slicing in list
# # [start:stop:skip]
# maruthi=[2,2.4,"ace",4.2,44,2.6]
# maruthi[4]=maruthi
# # print(maruthi[-1:-4:-2])#[negitive]
# # print(maruthi[1:4:2])#[positive]
# print(maruthi[:5:3])
# print(maruthi[-3:])
# print(maruthi[:])

new file added









# f='maruthi \n prasanna'
# print(f)

# # raw data
# r=r'maruthi \n prasanna'
# print(r)


# re=regression expression
# syntax
# re.findall(r'\d+',"string")
import re
# maruthi="age 22,height 6,weight 60,karumanchi,andhra_pradesh,guntur,522646"
# x=re.findall(r'\d+','maruthi')
s="maruthi123@gmai.com prasanna24@gamilcom 2426@gmailcom"
mail=re.findall(r"\w+@\w\.\w+",s)
print(f"email details are {mail}")
