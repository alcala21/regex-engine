# write your code here
def regexp(exp, text):
    if not exp:
        return True
    if not text or (exp[0] != text[0] and exp[0] != "."):
        return False
    return regexp(exp[1:], text[1:])


print(regexp(*input().split("|")))
