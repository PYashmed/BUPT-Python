#
# * int float in py
print(2004)  # int
print(3.24)  # float
# * scientific notation
print(3E2)  # 300.0
print(3e2)  # 300.0
print(3E-1)  # 0.3
print(3e-2)  # 0.03

# * number systems
# ^ binary : 0btt/0Btt
print(0b11)  # 3
print(0B11)  # 3

# ^ octonary : 0ott/0Ott
print(0o121)  # 81
print(0O121)  # 81

# ^ hexadecimal : 0xtt/0Xtt
print(0xab)  # 171
print(0Xab)  # 171


# * conversion os number system
# ^ convert to decimal
print(0b1010)  # 10

# ^ convert to binary : bin()
print(bin(10))  # 0b1010

# ^ convert to octonary : oct()
print(oct(100))  # 0o144

# ^ convert to hexadecimal : hex()
print(hex(100))  # 0x64
print(hex(0o144))  # 0x64


# * complex number
# ^ 1+1j 2+3j 0.4+2.3j  err:1+j

# * operator
# ^ + - * / //exact division
# ^ ** power
# ^ <<(equal *2) >>(equal /2)
print(1.2*5)  # 6.0
print(12/4)  # 3.0

# * bit operation
# ^ & 1,1->1
print(-1&-4)# -4
# & complement : from right find first 1 ,left of 1 ~
# & -10 -> 10(1010) -> (0110)
# & -4 -> 4(0100) -> (1100)
# ^ | 0,0->0
# ^ ^ 1,0->1 0,1->1 0,0->0 1,1->0
# ^ ~ 0->1 1->0
print(~3)  # -4
print(~-123)  # 122
# ^  ~ x ==  -(x + 1)
