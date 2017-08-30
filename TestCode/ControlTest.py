# if문 
print( 'IF Statements 시작')
x = int( input('정수형 숫자를 입력 후 Enter를 치세요!') )
if x < 0 :
    x = 0
    print( 'x가 0보다 작아서 0으로 변경' )
elif x == 0:
    print( 'x는 0이다' )
elif x == 1:
    print( 'x는 1이다' )
else:
    print( 'x는 그 외 숫자이다. x=', x )
    print( 'else문 완료' )

print( 'if statements test 완료' )

print( '\nwhile statements test 시작' )
a, b = 0, 1
while b < 10:
    print( b, '  while문의 조건식이 True일 동안 실행 한다', b < 10 )
    a, b = b, a+b
print( b, '  while문의 조건식이 True일 동안 실행 한다', b < 10 )    
print( 'while statements test 완료' )

print( '\nfor statements test 시작' )
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len( w ) ); #words에 들어 있는 문자열과 해당 문자열의 길이를 출력 한다
print( words )
for w in words[:]:
    if len( w ) > 6:
        words.insert( 0, w )  #문자열의 길이가 6이상인 것을 다시 배열에 추가 한다
print( words )

# 소수 구하기...
for n in range( 2, 10 ):
    for x in range( 2, n ):
        if n % x == 0:   # n % x -> 나머지 연산인가?
            print( n, 'equals', x, '*', n//x )  # n//x -> 몫 연산인가?
            break
        else:
            print( n, 'is a prime number')
print( 'for statements test 완료' )

print( '\nrange function 시작' )
for i in range( 5 ):
    print('rang(5)에서 i값 출력 : ',  i )  #range값 출력 0부터 시작해서 n-1까지 실행됨

for i in range( 5, 10 ):
    print('rang(5, 10)에서 i값 출력 : ',  i )  #range값 출력 범위값 형식, 5부터 10까지 1씩 증가

for i in range( 0, 10, 3 ):
    print('rang(0, 10, 3)에서 i값 출력 : ',  i )  #range값 출력 범위값, step 형식, 0부터 10까지 3씩 증가

for i in range( -10, -100, -30 ):
    print('rang( -10, -100, -30)에서 i값 출력 : ',  i )  #range값 출력 범위값, step 형식, 음수도 됨

for i in range( 10, -10, -1 ):
    print('rang( 10, -10, -1)에서 i값 출력 : ',  i )  #range값 출력 범위값, step 형식, 감소일 경우 감소값을 반드시 입력 해야 한다.
    
for i in range( -10, 10 ):
    print('rang( -10, 10)에서 i값 출력 : ',  i )  #range값 출력 범위값, step 형식, 

for i in range( len( words ) ) :
    print( i, words[ i ] )

print( list( range(5) ) )
print( range(5) )
print( 'range function 완료')