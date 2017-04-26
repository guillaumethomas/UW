def counting_backward():
    # language is python 3.6
     for i in range(100,-1,-2):
         print(i)

def div_4_5():
    # language is python 3.6
    for i in range(101):
        beta = ""
        if i % 4 == 0:
            beta ="Go"
        if i % 5 == 0:
            beta = beta + "Figure"
        if beta != "":
            print(beta)



if __name__ == "__main__":
    counting_backward()
    print('')
    div_4_5()

