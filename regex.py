# write your code here
def match(exp, text):
    if not exp:
        return True
    if not text or (exp[0] != text[0] and exp[0] != "."):
        return False
    return match(exp[1:], text[1:])


def regexp(pattern, string):
    if match(pattern, string):
        return True
    if not string:
        return False
    return regexp(pattern, string[1:])

print(regexp(*input().split("|")))
