
# (21) 단어 1개를 입력받아 나누어 출력하기

a=str(input())
for i in a:
    print(i)


# (22) 연월일 입력받아 나누어 출력하기 

s=input()
print(s[0:2],s[2:4],s[4:6])


# (23) 시,분,초 입력받아 분만 출력하기

s=input()
print(s.split(":")[1])


# (24) 단어 2개를 입력받아 이어붙이기

a,b=input().split()
print(a+b)

# (25) 정수 2개를 입력받아 합 계산하기

a,b=input().split()
c=int(a)+int(b)
print(c)

# (26) 실수 2개를 입력받아 합 계산하기

a=input()
b=input()
c=float(a)+float(b)
print(c)

# (27) 10진수 정수 입력받아 16진수로 출력하기

#oct()함수-10진수를 8진수 문자열로 변환
#hex()함수-10진수를 16진수 문자열로 변환
#bin()함수-10진수를 2진수 문자열로 변환

a=input()
n=int(a)
print('%x'%n)


# (28) 10진수 정수 입력받아 16진수 대문자로 출력하기

a=input()
n=int(a)
print('%X'%n)

# (29) 16진 정수 입력받아 8진수로 출력하기

a=input()
n=int(a,16) # 입력된 a를 16진수로 인식해 변수 n에 저장
print('%o'%n)

# (30) 영문자 1개를 입력받아 10진수로 변환하기

n = ord(input())
print(n)

# ord()는 어떤 문자의 순서위치(ordinal position) 값을 의미한다.
# 실제로는 각각의 문자들에는 연속된 정수 값이 순서에 따라 부여되어 있다. A:65, B:66, C:67
# ord(): 문자C를 10진수로 변환한 값

# 컴퓨터로 저장되고 처리되는 모든 데이터들은 2진수 형태로 정수화되어야 하는데,
# 컴퓨터에 문자를 저장하는 방법은 아스키코드(ASCII Code)나 유니코드(Unicode)가 자주 사용된다.

# 예를 들어, 영문 대문자 'A'는 10진수 값 65로 표현하고, 2진수(binary digit)값 1000001로 바꾸어 컴퓨터 내부에 저장한다.
# 유니코드(unicode)는 세계 여러나라의 문자를 공통된 코드 값으로 저장할 때 사용하는 표준코드이다.

# (31) 정수 입력받아 유니코드 문자로 변환하기

c=int(input())
print(chr(c))

# chr()는 정수값을 문자로, ord()는 문자를 정수값 형태로 바꿔준다.

# (32) 정수 1개를 입력받아 부호 바꾸기

a=input()
print(-int(a))

# (33) 문자 1개를 입력받아 다음 문자 출력하기

a=ord(input())  # ord: 문자를 10진수로 변환
b=chr(a+1)
print(b)

# (34) 정수 2개를 입력받아 차 계산하기

a,b=input().split()
c=int(a)-int(b)
print(c)

# (35) 실수 2개를 입력받아 곱 계산하기

a,b=input().split()
c=float(a)*float(b)
print(c)

# (36) 단어 여러번 출력하기

w,n=input().split()
print(w*int(n))

# (37) 문장 여러번 출력하기

n=input()
s=input()
print(int(n)*s)

# (38) 정수 2개 입력받아 거듭제곱 계산하기

a,b=input().split()
c=int(a)**int(b)
print(c)

# (39) 실수 2개 입력받아 거듭제곱 계산하기

a,b=input().split()
c=float(a)**float(b)
print(c)

# (40) 정수 2개 입력받아 나눈 몫 계산하기 

# 몫은 //로 

a,b=input().split()
print(int(a)//int(b))

# (41) 정수 2개 입력받아 나눈 나머지 계산하기

# 나머지 %로

a,b=input().split()
print(int(a)%int(b))

# (42) 실수 1개 입력받아 소수점이하 두 번째자리 반올림 

a=float(input())
print(format(a,".2f"))

# (43) 실수 2개 입력받아 나눈 결과 소수점 넷째자리에서 반올림하여 소수점 셋째자리까지 출력한다.

# 파이썬에서 나눗셈(division)을 계산하는 연산자(/)가 있다.

a,b=input().split()
c=float(a)/float(b)
print(format(c,'.3f'))

# (44) 정수 2개 입력받아 합,차,곱,나머지,나눈값(소수점 둘째자리까지)

a,b=input().split()
a=int(a)
b=int(b)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(format(a/b,'.2f'))

# (45) 정수 3개 입력받아 합과 평균 출력하기

a,b,c=input().split()

sum=int(a)+int(b)+int(c)
ave=sum/3

print(str(sum)+" "+format(ave,'.2f'))

# (46) 정수 1개 입력받아 2배 곱해서 출력하기

# *2를 계산한 값을 출력해도 되지만, 정수를 2배 곱하거나 나워 계산해주는 비트단위시프트연산자 <<,>>를 이용할 수 있다.
# 컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에, 2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로 지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데
# 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고, 
# 오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0이나 1이 개수만큼 추가되고 가장 오른쪽에 있는 1비트는 사라진다.

# <예시>
n=10
print(n<<1) # 20
print(n>>1) # 5
print(n<<2) # 40
print(n>>2) # 2

a=input()
print(int(a)<<1)

# (47) 2의 거듭제곱 배로 곱해 출력하기

a,b=input().split()
a=int(a)
b=int(b)

print(a*(2**b))

# (48) 정수 2개 입력받아 a가 b보다 작으면 True, a가 b보다 크거나 같으면 False 출력

a,b=input().split()
a=int(a)
b=int(b)

if a<b:
    print("True")
else:
    print("False")

# (49) 정수 2개를 입력받아 a와 b의 값이 같으면 True, 같지않으면 False를 출력

a,b=input().split()
a=int(a)
b=int(b)

if a==b:
    print("True")

else:
    print("False")

# (50) 정수 2개를 입력받아 b의 값이 a의 값보다 크거나 같으면 True, 같지 않으면 False를 출력

a,b=input().split()
a=int(a)
b=int(b)

if b>=a:
    print("True")
else:
    print("False")










