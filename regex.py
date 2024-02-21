# regex topic


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