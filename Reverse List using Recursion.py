def revList(l):
   if len(l) != 0:
       print l.pop()
       revList(l) 
   else:
       print "End of List"


revList([1,2,3])

    