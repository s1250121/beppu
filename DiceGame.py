from random import Random
r=Random()
x=r.randint(1,6)
y=r.randint(1,6)

print'Rolling the dice...'
print'Die 1:', x
print'Die 2:', y
print'Total value:', x+y

if x+y>=8:
    print 'you won!'
else:
    print 'you lost!'
