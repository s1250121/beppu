from random import Random
r=Random()
x=r.randint(1,6)
y=r.randint(1,6)

print'what is your name?'
s=raw_input('> ')
print'Hello,',s,'!'

print'Rolling the dice...'
print'Die 1:', x
print'Die 2:', y
print'Total value:', x+y

if x+y>=8:
    print s,'won!'
else:
    print s,'lost!'
