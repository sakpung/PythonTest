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

print( 'We are the {} who say "{}!"'.format('knights', 'Ni') )

print( '{0} and {1}'.format('spam', 'eggs') )
print( '{1} and {0}'.format('spam', 'eggs') )
print( '{1} and {0} or {0} and {1}'.format('spam', 'eggs') )

print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred',other='Georg'))

contents = 'eels'
print('My hovercraft is full of {}.'.format(contents))
print('My hovercraft is full of {!r}.'.format(contents))

import math
print( 'The value of PI is approximately {0:.4f}.'.format( math.pi ), '\n' )

table = {'Sjoerd':4127, 'Jack':4098, 'Dcab':7678}
for name, phone in table.items():
    print( '{0:10} ==> {1:10d}'.format(name, phone) )
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))    

print('The value of PI is approximately %5.3f.' % math.pi)

print( '7.1 Fancier Output Formatting', '완료' )