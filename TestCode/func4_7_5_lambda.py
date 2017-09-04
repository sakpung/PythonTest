print( 'function, lambda, 시작' )

def make_incrementor( n ):
    return lambda x : x + n

f = make_incrementor(20)
print( f(10) )
print( f(30) )

f2 = make_incrementor(100)
print( f2(10) )
print( f2(30) )

print( '-' * 50 )
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
print( pairs )

#pairs.sort()
#print( pairs )

pairs.sort( key=lambda pair:pair[0] )
print( pairs )

print( 'function, lambda, 완료' )