test = "abcdefghijklmnopqrstuvwxyzABCDEFGH"
def reverse_string(test: str) -> str:
    temp = ""
    for i in test:
        temp = i + temp
    return temp

def comprehend(test: str) -> str:
    pass

print(reverse_string(test))