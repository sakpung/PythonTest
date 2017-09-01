print( 'function, 임의의 agument 설정, 시작' )

def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))

#write_multiple_items('asdfasdf','#', 'asdfasdf', 'da') #실행 않됨

def concat(*args, sep="/"):
    return sep.join(args)

print( concat("earth", "mars", "venus") )
print( concat("earth", "mars", "venus", sep=".") )
print("-" * 40)
print( '\n\n\n' )



print( 'function, 임의의 agument 설정, 완료' )