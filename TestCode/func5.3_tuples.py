print( '5.3 Tuples and Sequences', '시작' )

t = 12345, 65324, 'hello!'
print( t, '\n', t[0] )

u = t, ( 1,2,4,5,6 )
print( u, '\n', u[1][1] )

#t[0] = 99999  # tuple은 값을 변경 할 수 없다. TypeError: 'tuple' object does not support item assignment
#t[1] = '문자열'
#print( t )

v  =  ( [ 1 ,  2 ,  3 ],  [ 3 ,  2 ,  1 ]) 
print( v, '\n', v[0][1] )
v[0][1] = 9  # tuple내에 list는 수정 가능 하네...
print( v, '\n', v[0][1] ) 

empty = ()
singleton = 'hello',  # 뒤에 comma가 없으면 singleton변수는 문자열 변수가 된다.
print( len( empty ) )
print( len( singleton ) )
print( singleton )

x, y, z = t  # tuple의 내용을 각 변수에 할당 한다.  변수의 갯수가 모자르면 error발생  ValueError: too many values to unpack (expected 2)
print(x, '\n', y, '\n', z)

print( '5.3 Tuples and Sequences', '완료' )