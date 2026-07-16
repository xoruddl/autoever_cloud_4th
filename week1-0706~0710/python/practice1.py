# 간단한 문제 (26.07.09)

# 평균으로 합불 나누기
def solve1():
    li = list(map(int, input("표준 입력: ").split()))
    avg = sum(li) / len(li)
    print(avg)

    if (avg > 100 or avg < 0):
        print("잘못된 점수")
    elif (avg >= 80):
        print("합격")
    else:
        print("불합격")

# solve1()

# 별찍기
def solve2():
    n = int(input())
    for i in range(n):
        for j in range(i + 1):
            print("*", end="")
        print()

# solve2()

''''''
# 4 - 1) log.txt 파일을 읽어서 트래픽의 전체 합계를 구하시오

def solve3():
    try:
        f = open("/Users/itaekyung/공부/현대오토에버 클라우드 4기/공부자료/log.txt")
        sum = 0
        for line in f:
            li = list(line.split(" "))
            if (li[-1][:-1] == "-" or li[-1][:-1] == "\"-\""):
                continue
            sum += int(li[-1][:-1])
        print(sum)
    except Exception:
        print(str(Exception) + "예외 발생")

# solve3() # 29992323 출력


# 4 - 2) log.txt 파일을 읽어서 IP 별 트래픽의 합계를 구하시오

def solve4():
    try:
        di = {}
        f = open("/Users/itaekyung/공부/현대오토에버 클라우드 4기/공부자료/log.txt")
        for line in f:
            li = list(line.split(" "))
            if (li[-1][:-1] == "-" or li[-1][:-1] == "\"-\""):
                continue
            
            ip = li[0]
            if (ip) not in di:
                di[ip] = int(li[-1][:-1])
            else:
                di[ip] = int(di[li[0]]) + int(li[-1][:-1])

        print(di)
    except:
        print("예외 발생")

solve4()

''''''