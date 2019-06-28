import random as rd
otp = rd.randrange(10000)
print("OTP is: ", otp)

otp = rd.randrange(20000, 60000, 10)   # 10 is for intervals
# This will give random no between the given range with interval of 10
print("OTP Now is: ",otp)

otp = rd.randint(1000, 9000)
print("OTP Lastly is: ",otp)