from collections import deque
print( '5.1.2 Using lists as Queues', '시작' )

queue = deque( ["Eric", "John", "Michael"] )
queue.append( "Terry" )
queue.append( "Graham" )
print( 'Queue List : ', queue )
print( 'Popleft : ', queue.popleft() ) # 먼저 입력된 data가 pop된다.
print( 'Queue List : ', queue )
print( 'Pop : ', queue.pop() )  # 마지막에 입력된 data가 pop된다.
print( 'Queue List : ', queue )

print( '5.1.2 Using lists as Queues', '완료' )