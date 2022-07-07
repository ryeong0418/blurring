#(51) 정수 두 개를 입력받아 서로 다르면 True, 같으면 False 출력 

a,b=input().split()
a=int(a)
b=int(b)

if a!=b:
    print("True")
else:
    print("False")


# (52) 정수 입력받아 참,거짓 평가하기

n=int(input())
print(bool(n))

# (53) 참,거짓 바꾸기

a=bool(int(input())) # --> 이런경우에 input(), int(), bool() 한 번에 한 단계씩 계산,처리,평가된다.
print(not a)

# (54) 둘다 참일 경우만 참 출력하기

a,b=input().split()
print(bool(int(a)) and bool(int(b)))

# (55) 하나라도 참이면 참 출력하기
a,b=input().split()
print(bool(int(a)) or bool(int(b)))

# (56) 참/거짓이 서로 다를때에만 참 출력하기

a,b=map(int, input().split())
if (a!=b):
    print(True)
else:
    print(False)

# (57) 참/거짓이 서로 같을때에만 참 출력하기

a,b=map(int, input().split())
if (a==b):
    print(True)
else:
    print(False)

# (58) 정수 2개가 입력될 때, 그 bool값(True, False)이 모두 False일 경우에만 True를 출력
a,b=map(int,input().split())
print(bool(a) is False and bool(b) is False)

# (59) 비트단위로 not하여 출력하기
print(~int(input()))
#** 비트단위(bitwise) 연산자는 ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor), <<(bitwise left shift), >>(bitwise right shift)가 있다.

# (60) 비트단위로 and하여 출력하기
a,b=map(int,input().split())
print(a&b)

# (61) 비트단위로 or하여 출력하기
a,b=map(int,input().split())
print(a|b)

# (62) 비트단위로 xor하여 출력하기
a,b=map(int,input().split())
print(a^b)

#(63) 두 정수(a,b) 중 큰 값을 출력하기
a,b=map(int,input().split())
print(max(a,b))

#(64) 정수 3개를 입력받아 가장 작은 값 출력하기
a,b,c=map(int,input().split())
print(min(a,b,c))

# (65) 정수 3개를 입력받아 짝수만 출력하기

a,b,c=map(int,input().split())
if a%2==0:
    print(a)

if b%2==0:
    print(b)

if c%2==0:
    print(c)

#(66) 정수 3개를 입력받아 짝/홀 출력하기

###### 방법1 ######
a,b,c=map(int,input().split())

if a%2==0:
    print("even")
else:
    print("odd")

if b%2==0:
    print("even")
else:
    print("odd")

if c%2==0:
    print("even")
else:
    print("odd")

###### 방법2 ######
data=input().split()

for i in data:
    if (int(i)%2==0):
        print("even")
    else:
        print("odd")

# (67) 0이 아닌 정수 1개를 입력받았을때 음, 양, 홀, 짝 구분하기

data=int(input())

if data<0 and (data%2==0):
    print("A")
if data<0 and (data%2==1):
    print("B")
if data>0 and (data%2==0):
    print("C")
if data>0 and (data%2==1):
    print("D")


# (68) 점수를 입력받아 평가 출력하기

data=int(input())

if 90<=data<=100:
    print("A")
if 70<=data<=89:
    print("B")
if 40<=data<=69:
    print("C")
if 0<=data<=39:
    print("D")

# (69) 평가를 입력받아 다르게 출력하기

data=input()

if data=="A":
    print("best!!!")

elif data=="B":
    print("good!!")

elif data=="C":
    print("run!")

elif data=="D":
    print("slowly~")

else:
    print("what?")

#(70) 월 입력받아 계절 출력하기
data=input()

if data in ["12","1","2"]:
    print("winter")

elif data in ["3","4","5"]:
    print("spring")

elif data in ["6","7","8"]:
    print("summer")

else:
    print("fall")

# (71) 임의의 정수가 줄을 바꿔 계속 입력되다가 0이 되면 종료

i=True
while(i):
    num=int(input())
    if num==0:
        i=False
    else:
        print(num)

# (72) 정수 1개 입력받아 카운트다운 출력하기

data=int(input())

while data>0:
    print(data)
    data=data-1
    
# (73) 정수 1개 입력받아 카운트다운 출력하기

data=int(input())
while data>0:
    data=data-1
    print(data)


# (74) 영문자 (a~z) 1개를 입력받았을때 a부터 그 문자까지의 알파벳을 순서대로 출력하기

c=ord(input())
t=ord('a')  ### ord('a')는 정수 97을 반환한다.

while t<=c:
    print(chr(t),end=' ')
    t+=1


# (75) 정수 1개를 입력받아 그 수까지 줄을 바꿔 한 개씩 출력한다.

i=0
data=int(input())

while i<=data:
    
    print(i)
    i+=1

    if i>data:
        break

# (76) 정수 1개 입력받아 0부터 그 수까지 순서대로 출력하기

i=0
data=int(input())
while i<=data:
    print(i)
    i+=1
    if i>data:
        break 

# (77) 짝수 합 구하기

data=int(input())
sum=0
for i in range(1,data+1):
    if i%2==0:
        sum=sum+i
print(sum)

#(78) 영문 소문자'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램 작성

c = ''
while(c != 'q'):
    c = input()
    print(c)

# (79) 1부터 순차적으로 더해 합을 만들어갈때, 입력된 정수와 같거나 커졌을때 마지막에 더한 정수를 출력한다.

data=int(input())
sum=0
total_sum=0

while total_sum<data:
    sum=sum+1
    total_sum=total_sum+sum


    if total_sum>=data:
        print(sum)
        break

# (80) 주사위 2개 던지기

n,m=map(int, input().split())
for i in range(1,n+1):
    for j in range(1,m+1):
        print(i,j)

# (81) 16진수 구구단 출력하기

n=input()
for i in range(1,16):
    print('%X*%X=%X' %(int(n, 16), int(hex(i), 16), (int(n, 16) * int(hex(i), 16))))

