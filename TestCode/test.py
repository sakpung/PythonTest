# 이거는 주서이다.
the_world_is_flat = False # True  # 이렇게 주석을 달 수 있다.
text = "#는 주석이 아니고 문자열이다"
변수 = "한글 변수명도 된다."
print("출력은 디버그 콘솔에서 출력 된다")
if the_world_is_flat :
    print("be careful not fall off!" + "\n" + text)
    print( 변수 )

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print( 3 * "un" + "test")

print( text[4:8] )
print( text[2:] )
print( text[:8] )
# print( "문자열 길이 : " + len(text) )
print( "문자열 길이 : %d" %  len(text) )
# print( "문자열 길이 : %d %s" % {len(text) % text} ) # error 발생
print( "UTF-8을 기본적으로 사용하여 한글도 1byte처럼 사용된다" )

a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b

quit    