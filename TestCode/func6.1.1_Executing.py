print( '6.1.1 Executing modules as scripts', '시작' )
print( '모듈을 스크립트로 실행하기' )

def fib( n ):
    a, b = 0, 1
    while b < n:
        print( b, end=' ')
        a, b = b, a+b
    print()

def fib2( n ):
    result = []
    a, b = 0, 1
    while b < n:
        result.append( b )
        a, b = b, a + b
    return result

print( __name__ )  # "__main__"  을 출력함

if __name__ == "__main__":
    import sys
    fib( int(sys.argv[1] ) )



print( '6.1.1 Executing modules as scripts', '완료' )