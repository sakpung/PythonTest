print( '5.6 Looping Techniques', '시작' )

knights = {'gallahad': 'the pure', 'robin': 'the brave'} # dictionaries 등록
for k, v in knights.items():
    print(k, v)

for i, v in enumerate( ['tic', 'tac', 'toe' ] ):
    print( i, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
answers2 = ['lancelot', 'the holy grail', 'blue']
tu = zip(questions, answers)
print('zip(questions, answers) = ', tu)
for q, a, a2 in zip(questions, answers, answers2):
    print('What is your {0}?  It is {1}.'.format(q, a))
    print( a2 )

for i in range(1, 10, 2):
    print( i )
for i in reversed( range(1, 10, 2) ):
    print( i )

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for b in sorted( basket ): # list전체를 반복 한다
    print( b )
for b in sorted( set( basket ) ): #집합으로 치환 후 반복 한다
    print( b )

import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8] # 목록 생성
filltered_data = []
for value in raw_data:
    if not math.isnan( value ):  #nan이 아닌 data만 목록에 저장하게 한다.
        filltered_data.append( value )
print( filltered_data )
print( '5.6 Looping Techniques', '완료' )