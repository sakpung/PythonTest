print( '5.1 More on Lists', '시작' )

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', ' apple', 'banana']

print( fruits, '\n', '*' * 50 );
print( 'apple의 수 : ', fruits.count( 'apple' ) )
print( 'tangerine의 수 : ', fruits.count( 'tangerine') )
print( 'banana의 위치 : ', fruits.index('banana'))
print( 'banana의 위치(4번째 이후) : ', fruits.index('banana', 4))
fruits.append( 'tomato' )

print('*' * 50 )
fruits.sort() #잘실행되며 function을 실행 할때 ()를 반드시 붙여야 한다
print( 'Sort : ', fruits )
fruits.reverse
fruits.sort(reverse=True) #잘실행되며 function을 실행 할때 ()를 반드시 붙여야 한다
print( 'after reverse, Sort : ', fruits )
print('pop 실행 : ', fruits.pop() )
print( fruits )

print('pop(0) 실행 : ', fruits.pop(0) )
print( fruits )

print('copy 실행 : ', fruits.copy() )
print( fruits )

print( '5.1 More on Lists', '완료' )