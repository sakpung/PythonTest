print( 'function Annotation', '시작' )

def f(ham: str, eggs: str = 'eggs') -> str:
    print( "Annotations:", f.__annotations__)
    print( "Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print( 'function 실행 : ', f( 'spam' ) )


print( 'function annotation', '완료' )