print( '5.2 del', '시작' )

a = [-1, 1, 66.25, 333,333, 1234.5]
print( a )
del a[0]
print( 'del a[0] 실행 후 : ', a )
del a[2:4]
print( 'del a[2:4] 실행 후 : ', a )
del a[:]
print( 'del a[2:4] 실행 후 : ', a )

del a  #변수 a를 삭제 한다

print( '5.2 del', '완료' )