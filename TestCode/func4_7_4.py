print( 'function, argument의 keyword 기본값 설정, 시작' )

def parrot(voltage, state='a stiff', action='voom'): 
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}    
parrot(**d)  #agument값을 key,name형식으로 처리 할수 있네...



print( 'function, argument의 keyword 기본값 설정, 완료' )
