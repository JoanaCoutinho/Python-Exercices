dict = {3: "Fizz", 5: "Buzz"}

def printNumbers(dict):
    s = ""
    for i in range(1,101):
        for j in dict.keys():
            if i%j == 0:
                s += dict[j] + " "
        if s != "":
            print(s)
        else:
            print(i)
        s = ""

printNumbers(dict)
