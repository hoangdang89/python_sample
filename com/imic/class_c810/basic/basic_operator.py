# Created by pyrrolni
# last updated 3rd June 2018

# Operator @ Description
# Comment!!
# Forget precedence, use parentheses 


# Just initialize my variable
x=-6
y=2
z=5
letters = ["a","b", "c","d"]

print ("x=",x)
print ("y=",y)
print ("z=",z)

# () @ Parentheses (grouping)
print ("result = ", x*y+z,"") 

print ("() With parentheses, x*(y+z)=", x*(y+z),"")

# ** @ Exponentiation
print ("** Exponentiation, x**y=", x**y)

# ~x @ Bitwise not
# ~x= -x - 1
print("~ Bitwise not, ~x=",~x)
print("~ Bitwise not, ~y=",~y)
print("~x= -x - 1=",-x - 1)
print("~y= -y - 1=",-y - 1)
# +x, -x @ Positive, negative
print ("+ Positive, +x=",+x,"")

print ( "- Negative, -x=", -x,"")

# *, /, %, // @ Multiplication, division, remainder=what is left after division, floor division=how many times does a fit into b
print ("* Multiplication, x*y=", x*y)
print ("/ Division, x/y=", x/y)
print ("% Remainder, x%z=", x%z)
print ("% Remainder, z%y=", z%y)
print ("// Floor, x//z=", x//z)
print ("// Floor, z//y=", z//y)

# +, - @ Addition, subtraction
print ("+ Addition, x+y=", x+y)
print ("- Substraction, x-y=", x-y)

# <<, >> @ Bitwise shifts
# z<<y = z*(2**y)
# z>>y = z//(2**y)
#more info here https://wiki.python.org/moin/BitwiseOperators
print ("<< Bitwise shift, z<<y=",z<<y)
print ("z<<y=z*(2**y)=", z*(2**y) )
print (">> Bitwise shift, z>>y=",z>>y)
print ("z>>y=z//(2**y)=", z//(2**y) )
# & @ Bitwise AND
print (">> Bitwise shift, z>>y=",z>>y)
print ("z>>y=z//(2**y)=", z//(2**y) )

# ^ @ Bitwise XOR
print ("^ Bitwise XOR, z^y=",z^y)
print ("^ Bitwise XOR, x^y=",x^y)

# | @ Bitwise OR
print ("| Bitwise OR, z|y=",z|y)
print ("| Bitwise OR, x|y=",x|y)
# in
if ("b" in letters):
    print ("'b' in letters: True")
else:
    print ("'b' in letters: False")


# not in
if ("x" not in letters):
    print ("'x' not in letters: True")
else:
    print ("'x' in letters: True")
    
# is
# check help("is")
print ( "5 is 7 gives",5 is 7)
print ( "5 is 5 gives",5 is 5)
print ( "x is x gives",x is x)


# is not 
print ( "5 is not 7 gives",5 is not 7)
print ( "5 is not 5 gives",5 is not 5)
print ( "x is not x gives",x is not x)

# <, <=,  >,  >=
print ( "5 > 7 gives",5 > 7)
print ( "5 <= 5 gives",5 <= 5)
print ( "x >= y gives",x >= y)

# <> (not equal, deprecated), != (not equal, newer version), == (equal)
print ( "not equal: 5 != 7 gives",5 != 7)
print ( "equal: 5 == 5 gives",5 == 5)
print ( " not equal x <> y gives error as <> was replaced by !=")

# /=, //=, +=, -=, %=, *=, **=
# e.g x /= 3 
# equivalent to x = x / 3
z/=3
print ( "z/=3 gives",z)
z=5
z//=3
print ( "z//=3 gives",z)
z=5
z+=3
print ( "z+=3 gives",z)
z=5
z-=3
print ( "z-=3 gives",z)
z=5
z%=3
print ( "z%=3 gives",z)
z=5
z*=3
print ( "z*=3 gives",z)
z=5
z**=3
print ( "z**=3 gives",z)
z=5


# not x @ Boolean NOT
print (" not (x==-6) gives ",not (x==-6))

# and @ Boolean AND
print (" (x==-6) and (y==2) gives ",(x==(-6)) and (y==2))

# or @ Boolean OR
print (" (x==-5) and (y==2) gives ",(x==-5) and (y==2))
