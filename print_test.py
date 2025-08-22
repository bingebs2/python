#입출력문 연습 - print()input()
#주석 - 번역X # - 한줄 주석
#여러줄 주석 """ """ ''' '''
'''
print("hello world")
print("박한올")
message = "안녕하세요 저는 인평자동차고등학교 1학년 전교부회장 박한올입니다."
print(message*10)
message2 = "이건 몰랐지"
print(message2)

# 변수와 자료형
a = 4
b = 2.5
c =" hello"
d = 5672
print("a변수에 입력된 값은 ",a,"입니다")
a = 54
print("a변수에 입력된 값은 ",a,"입니다")
a = "4인 척하는 54"
print("a변수에 입력된 값은 ",a,"입니다")
a = 4

print(type(a))
print(type(b))
print(type(c))
print(type(d))


#입력문 - input()
name = input("이름을 입력하세요: ")
#print("입력한 이름은",name,"입니다")
age = input("나이를 입력하세여: ")

print("내 이름은 ",name,",이고 나이는",age,"살입니다")
'''
# 두 수의 덧셈(키보드로부터 수를 입력받기)
#키보드로부터 입력받으면 모두 문자로 취급
#형 변환
a = int(input("첫번째값 입력: "))
b =int(input("두번째값 입력: "))
c =a*b
print(c)





