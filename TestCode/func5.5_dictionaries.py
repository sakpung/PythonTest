print( '5.5 Dictionaries', '시작' )

tel = { 'jack':4098, 'sape':4139 }
tel['guido'] = 6542
print( tel )
print( tel['jack'] )
#print( tel['test'] ) # 없는 key를 찾으면 error 발생

del tel['sape']
tel['irv'] = '345345345'
print( tel )

l = list( tel.keys() )
print( l )
l2 = list( tel.values() )
print( l2 )

l3 = sorted( l )
print( l3 )

print( 'jack' in tel )
print( 'jack' not in tel )
print( 'sape' in tel )

d = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print( d )

r = { x:x**2 for x in (2,4,6) }
print( r )

d2 = dict(sape=4139, guido=4127, jack=4098)
print( d2 )
print( '5.5 Dictionaries', '완료' )