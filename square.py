limit = int (input ("Enter an integer limit: "))

##squares = []
##
##for i in range (1, limit+1):
##    if i % 2:
##        squares.append (i**2)
##
##for i in squares:
##    print (i)
##
##print ("Length", len(squares))

print (f'{a} is the list, {(len(a))} is the length'.format ({'a':[s**2 for s in range (1, limit+1) if s % 2]}))
