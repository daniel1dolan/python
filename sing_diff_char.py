str1 = "aabb"
str2 = "aabbc"

def myFun(str1, str2):
    for i in str2:
        if i in str1:
            pass
        else: 
            return i


print(myFun(str1, str2))
    
