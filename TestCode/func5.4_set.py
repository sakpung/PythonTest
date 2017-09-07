print( '5.4 Set', '시작' )

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana', 345}

print( basket, len( basket ) )  #중복 요소가 제거 되어 출력됨

print( 'orange' in basket )
print( 'crabgrass' in basket )

a = set( 'abracadabra' )  #중복된 알파벳이 한개로 통합됨
b = set( 'alacazam' )     #중복된 알파벳이 한개로 통합됨
print( 'a=',a, '\n', 'b=',b)
print('a - b = ', a - b)  #차집합 연산
print('a | b = ', a | b)  #합집합 연산
print('a & b = ', a & b)  #교집합 연산
print('a ^ b = ', a ^ b)  #교집합의 반대(합집합 - 교집합)
print( (a|b)-(a&b) )

c = { x for x in 'abracadabra' if x not in 'abc'}
print( c )
print( '5.4 Set', '완료' )