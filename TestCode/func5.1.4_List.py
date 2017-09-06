print( '5.1.4 Nested List Comprehensions', '시작' )
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

print( matrix )

print( [[row[i] for row in matrix] for i in range(4)] )  # 이해가 잘 않된다...

aa = [ [], [], [], [] ]
for row2 in matrix:
    for i in range( 4 ):
        aa[i].append( row2[i] )
print( 'aa = ', aa )

transposed = []
for i in range( 4 ):
    transposed.append( [row[i] for row in matrix] )
print( transposed )

transposed2 = []
for i in range( 4 ):
    transposed_row = []
    for row in matrix:
        transposed_row.append( row[i] )
    transposed2.append( transposed_row )
print( transposed2 )

print( list( zip( *matrix ) ) )
bb = list( zip( *matrix ) )
print( 'bb = ' , bb )
print( 'bb[2] = ',  bb[2] )
print( 'bb[2][1] = ',  bb[2][1] )

print( '5.1.4 Nested List Comprehensions', '완료' )