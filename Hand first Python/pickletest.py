import pickle

with open( 'z:\pickletest.pickle', 'wb') as mydatawrite :
    pickle.dump( [1,2,'three'], mydatawrite)

with open( 'z:\\pickletest.pickle', 'rb') as mydataread :
    a_list = pickle.load( mydataread )

print( 'print : ', a_list, end='' )