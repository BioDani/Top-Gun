def reverse(word = str):
    if len(word) == 0:
        return ""
    else:
        return word[-1] + reverse(word[0:-1])
    
    
def reverse2(word = str):
    if word:
        return word[-1] + reverse(word[0:-1])
    return ""
    

print(reverse("Daniel"))
print(reverse2("Daniel"))
        