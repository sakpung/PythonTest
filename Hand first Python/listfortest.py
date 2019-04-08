print('시간 계산\n')
mine = [1, 2, 3]
secs = [m * 60 for m in mine]
print( secs, end='' )

print('\n\n미터를 피트로 변환\n')
meters = [3, 4, 2]
feet = [m * 3.281 for m in meters]
print('feet : ', feet, end='')

print('\n\n소문자를 대문자로 치환\n')
lower = ['I', 'asdfasdf', 'Like', 'tEst']
upper = [s.upper() for s in lower]
print('Upper : ', upper, end='\n')

aa = sorted( lower )
print( 'sort : ', aa, end= '\n' )

print('\n\nSet Test', end='\n')
testlist = [1,3,4,5,6,4,2,2,1,2,3,4]
setlist = set( testlist )
print('Set : ', setlist, end='\n')
calcsetlist = [v*10 for v in setlist]
print('Set( v*10 ) :', calcsetlist, end='\n' )
