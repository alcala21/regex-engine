# write your code here
cmd = input()


def regexp(exp, text):
    return (exp == text) or (exp == ".") or not exp


print(regexp(*cmd.split("|")))
