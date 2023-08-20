import random

def ProblemMaker(n):
    for _ in range(n):
        random_num_10 = random.randint(1, 1000)
        numdict = {2:bin(random_num_10).lstrip("0b"), 8:oct(random_num_10).lstrip("0o"), 10:str(random_num_10), 16:hex(random_num_10).lstrip("0x")}
        anstypelist = [2, 8, 10, 16]

        extype = random.choice(anstypelist)
        info = str(extype)+"진수 "
        anstypelist.remove(extype)

        anstype = random.choice(anstypelist)
        realans = numdict[anstype]
        print(info, numdict[extype], "을 ", anstype, "진수로 변환하세요.", sep = '')
        ansinput = input()

        print("------------------------")

        if ansinput == realans:
            print("맞았습니다!")
        else:
            print("틀렸습니다. 정답은 ", realans, "입니다.", sep = '')


print("진법 변환 문제 생성기에 오신 것을 환영합니다!\n")
n = int(input("몇 문제를 풀고 싶으신가요? (1~5 추천, 정수로 입력): "))
ProblemMaker(n)

repeat = input("한 세트 더 할까요? (y/n)")
if repeat == "y":
    ProblemMaker(n)
else:
    print("end")
        