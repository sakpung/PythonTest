print( '5.1.3 List Comprehensions', '시작' )

squares = []
for x in range( 10 ):
    squares.append( x**2 )

print( squares )

squares2 = list( map(lambda x: x**2, range(10)) )
print( squares2 )

squares3 = [x**2 for x in range(10)]
print( squares3 )

squares4 = [(x,y) for x in [1,2,3] for y in [3,2,1] if x!=y]
print( squares4 )
combs = []
for x in [1,2,3]:
    for y in [3,2,1]:
        if x != y:
            combs.append((x,y))
print(combs)

vec = [-4, -2, 0, 2, 4]
print( [x*2 for x in vec] )
print( [x for x in vec if x >= 0] )
print( [abs(x) for x in vec] )

freshfruit = ['banana', 'loganberry ', 'passion fruit']
print( [weapon.strip() for weapon in freshfruit] )

print( [(x, x**2) for x in range(6)] )
#print( [x, x**2 for x in range(6)] ) # SyntaxError: invalid syntax 발생

vec = [[1,2,3], [4,5,6], [7,8,9]]
print( vec )
print( [num for elem in vec for num in elem] ) # 2차원  list를 1차원으로 만든다
cc = [num for elem in vec for num in elem];
print( cc )

aa = []
bb = []
for elem in vec:
    bb.append( elem )
    for num in elem:
        aa.append( num )
    print( 'bb = ', bb )
print( 'aa = ', aa )

from math import pi
print( 'Pi = ', pi )
print( [str(round(pi,i)) for i in range(1, 10)] )

print( '5.1.3 List Comprehensions', '완료' )