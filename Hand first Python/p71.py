def print_lol(the_list) :
    for each_item in the_list :
        if isinstance( each_item, list ) :
            print_lol( each_item )
        else :
            print( each_item )


cast = ['aaa', 'bbb', ['zzz', 'yyy', 'xxx'], 'ccc', 'ddd' ]
print_lol( cast )
