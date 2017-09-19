print( '7.1 Fancier Output Formatting', '시작' )
s = 'Hello, world'

print( 's =', s )

print( 'str( s )=', str( s ) )
print( 'repr( s ) = ', repr( s ) )
print('str( 1/7)=', str( 1/7) )

x = 10 *3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# s = 'The value of x is ' + x + ', and y is ' + y + '...' # error 발생, TypeError: must be str, not float
print( s )

hello = 'hello, world\n'
hellos = repr(hello)
print(hellos)
print( str( hello ) )
print( hello )

print( repr((x, y, ('spam', 'eggs'))) )

for z in range(1, 11):
    print( repr(z).rjust(5), repr(z*z).rjust(3), end= ' ')
    print( repr(z*z*z).rjust(4) )

for z in range(1, 11) :
    print('{0:2d} {1:3d} {2:4d}'.format(z, z*z, z*z*z) )

print( '12'.zfill( 5 ) )    
print( '-3.14'.zfill(7) )
print( '3.14159265359'.zfill(5) )

print( '7.1 Fancier Output Formatting', '완료' )