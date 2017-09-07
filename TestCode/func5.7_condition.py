print( '5.7 More on Conditions', '시작' )

string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3

print( string1, string2,  string3)

print( non_null )

string4 = 'Hammer Dance'
non_null2 = string3 and string4   #문자열은 걍 문자열을 반환 하네...
print( non_null2 )

print( 2 == 3 )

print( '5.7 More on Conditions', '완료' )