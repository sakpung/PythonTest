print( 'function, argument의 기본값 설정, 시작' )
def ask_ok( prompt, retries=4, reminder='Please try again!'):
    while True:
        print( 'retries=', retries )
        ok = input( prompt )
        if ok in ( 'y', 'ye', 'yes'):
            return True
        if ok in ( 'n', 'no', 'nop', 'nope' ):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError( 'invalid user response' )
        print( reminder )

ret = ask_ok( 'Do you really want to quit?' )
print( ret )

ret = ask_ok( 'OK to overwrite the file?', 2)
print( ret )

ret = ask_ok( 'OK to overwrite the file?', 2, 'Come on, only yes or no!')
print( ret )

print( '\n\n\n' )

i = 5
def f( arg = i ):  #기본값은 function 선언 할 때 지정 된다.
    print( arg )

i = 6
f()

print( '\n\n\n' )

def f2( a, L = [] ): 
    L.append( a )
    return L

print( f2( 1 ) )
print( f2( 2 ) )
print( f2( 3 ) )
L0 = [9, 8]
print( f2( 3, L0 ) )
print( L0 )

print( '\n\n\n' )

def f3( a, L = None ): # function선언시에 L은 None으로 설정되어 있어 실행 될때 마다 L의 값은 None이 된다.
                       
    if L is None:
        L = []
    L.append( a )
    return L

print( f3( 1 ) )
print( f3( 2 ) )
print( f3( 3 ) )

L2 = f2( 2 );
print( f3( 4, L2 ) ) # 실행시 별도의 변수를 지정하면 해당 변수의 값을 사용하게 된다.
print( L2 )

print( 'function, argument의 기본값 설정, 완료' )