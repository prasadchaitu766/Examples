start=1
end=100
for x in range(start,end+1):
    if x>1:
        for y in range(2,x):
            if(x%y)==0:
                break
        else:
             print x
# start = 1
# end = 100
#
# for val in range(start, end + 1):
#
#     # If num is divisible by any number
#     # between 2 and val, it is not prime
#     if val > 1:
#         for n in range(2, val):
#             if (val % n) == 0:
#                 break
#         else:
#             print(val)