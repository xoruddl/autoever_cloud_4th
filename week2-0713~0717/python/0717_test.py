def solve1():
    li = list(map(int, input().split()))
    for n in li:
        if (n < 0 or n > 100):
            print("잘못된 점수")
            return
        
    result = sum(li) / 4
    if (result >= 80):
        print("합격")
    else:
        print("불합격")

# solve1()



def solve2():
    li = list(map(int, input().split(";")))
    li.sort(reverse = True)

    for i in li:
        print(f"{i:,}")

# 51900;83000;158000;367500;250000;59200;128500;1304000
# solve2()

def isPalindrome(s, start, end):
    flag = True
    while (start <= end):
        if (s[start] != s[end]):
            flag = False
            break
        start += 1
        end -= 1
    
    return flag
        

def solve3():
    with open("words.txt") as f:
        words = [line.strip() for line in f]

    for word in words:
        if (isPalindrome(word, 0, len(word) - 1)):
            print(word)

# solve3()


