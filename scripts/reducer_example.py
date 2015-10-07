#!/usr/bin/python

import sys

# Initialize variables

salesTotal = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    # map the data

    thisKey, thisSale = data_mapped

    '''Evaluate the data relative to thisKey.  Bear in mind that for Hadoop there is a sort step after mapping and before reduction, so you will see 
    all keys one row after the other until there is a new key.
      The initial value of oldKey is 'None.'  For some reason the oldKey and oldKey statement helps us out with this, but 
    I don't know why.  Some of this confusing stuff is for the first line of the data doc and isn't needed for the rest.  Anyway, for each new key the first if loop 
    is going to = True and the oldKey will be printed then oldKey will be assigned to thisKey (the new key) and the variable will be re-initialized (so you arent
        aggregating on the oldKey).  When the if statement is False (it is still the same key) then oldKey = thisKey (I think this is only necessary for the first line,
        more on that later). The main thing that happens is the agg/count function updates the key value.'''

'''What is the deal with oldKey and oldKey:  I think this makes the code bypass the if loop the value is None and None so that 
oldKey = thisKey changes it to the value mapped in the first line and then the code does it's thing to the last line.  The way it is
setup ensures that we go onto other lines and the the key None is never printed.  I understand this now, it is a compoud boolean, so 
the first part is if oldKey i.e. does it exist (when None this is a no, it does not exist) and it is not equal to thisKey.  For the None case, we fail
on if oldKey, because it does not exist.  After the first line, it does exist because we assign it a value  '''
    if oldKey and oldKey != thisKey:
        print oldKey, "\t", salesTotal
        oldKey = thisKey;
        salesTotal = 0

    oldKey = thisKey
    salesTotal += float(thisSale)

'''This is for the last line of the data doc at that point we exit the for line in syst.stdin loop and as long as its value isn't none, we print the key and
its value.  If we didn't have this we would lose all info for the last key because it would never print in any of the innner loops.
'''

if oldKey != None:
    print oldKey, "\t", salesTotal