print( 'function, argument의 keyword 기본값 설정, 시작' )

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'): # agument의 이름을 직접사용하여 value를 넘길 수 있다.
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

#parrot(1000)                                          # 1 positional argument
#parrot(voltage=1000)                                  # 1 keyword argument
#parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
#parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments, 순서는 중요하지 않다.
#parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
#parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


#parrot()                     # error, required argument missing, 기본값이 지정되어 있지 않는 놈은 반드시 value를 지정 해줘야 한다.
#parrot(voltage=5.0, 'dead')  # error, non-keyword argument after a keyword argument, SyntaxError: positional argument follows keyword argument
#parrot(voltage=5.0 )         # 잘됨, non-keyword argument after a keyword argument
#parrot(110, voltage=220)     # error, duplicate value for the same argument, voltage의 값이 두번 지정되어 있다. TypeError: parrot() got multiple values for argument 'voltage'
#parrot(actor='John Cleese')  # error, unknown keyword argument, 

print( ' ', end='\n\n\n' )

def function( a ):
    pass

#function( 0, a=0)  # error, a에 해당하는 arument를 두번 선언 했다. TypeError: function() got multiple values for argument 'a'

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    print("-" * 40)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    print( 'keywords : ' , keywords )
    print( 'length : ' , len( keywords ) )
    keys = sorted(keywords.keys())
    print( 'keys : ', keys )
    print( 'length : ' , len( keys ) )
    for kw in keys:
        print(kw, ":", keywords[kw])
    print("-" * 40)

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch", aa=3)        

print( '\n\n\n' )



print( 'function, argument의 keyword 기본값 설정, 완료' )