import json 
print( '7.2 Reading and Writing Files', '시작' )

f = open('workfile', 'w')
f.write('test ok\n')
f.write('test ok2\n')
f.close

with open('workfile', 'r') as f:
    read_data = f.readline()
# f.close   with를 사용해서 open한 것은 해당 block이 끝나면서 자동으로 close된다.

print( read_data )

#read_data = f.readline()  # error 발생   ValueError: I/O operation on closed file.
#print( read_data )

json.dumps( [1, 'simple', 'list'] )

print( '7.1 Reading and Writing Files', '완료' )