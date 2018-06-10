dict = {3: "Fizz", 5: "Buzz"}
n = 100
def printNumbers(dict,n):
    """
    Imprime a string "value" do dicionario se a sua "key" for multipla de
    um numero de 1 a n. Imprime o proprio numero caso contrario. Se houver
    mais de 1 multiplo, este e tambem impresso.
    """
    s = ""
    for i in range(1, n+1):
        for j in dict.keys():
            if i%j == 0:
                s += dict[j] + " "
        if s != "":
            print(s)
        else:
            print(i)
        s = ""

printNumbers(dict,n)
