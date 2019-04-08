import os

cd = os.getcwd()
print( cd, end ='\n' )

ofn = cd + '\\aa.txt'
print( ofn, end ='\n' )

wfn = cd + '\\out.txt'
print( wfn, end ='\n' )

fh = open( ofn )
wh = open( wfn, 'w' )
try :
    print( fh.readline(), end='\n' )

    fh.seek( 0 )
    for each_line in fh :
        print( each_line, end='\n');

    fh.seek( 0 ) 
    for each_lineq in fh :
        try :  
            if each_lineq.find( ':' ) > 1 :
                (role, line_spoken) = each_lineq.split( ':', 1 )
                print( role )
                print( ' said : ' )
                print( line_spoken, end='\n' )
            else :
                print( each_lineq, end='\n')
        except TypeError:
            print(' typeerror 발생', end='\n');  
        except ValueError:
            print(' ValueError 발생', end='\n');  


    fh.seek( 0 ) 
    for each_lineq in fh :
        try :  
            if each_lineq.find( ':' ) > 1 :
                (role, line_spoken) = each_lineq.split( ':', 1 )
                print( role, file=wh);
                print( ' said : ', file=wh )
                print( line_spoken, file=wh )
            else :
                print( each_lineq, file=wh)
        except TypeError:
            print(' typeerror 발생', end='\n');  
        except ValueError:
            print(' ValueError 발생', end='\n');  
finally :
    wh.close()
    fh.close()

