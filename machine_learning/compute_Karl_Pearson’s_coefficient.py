from math import *

x = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

# Calculating the mean
x_mean = sum(x)/len(x)
y_mean = sum(y)/len(y)

diff_x_mean = [(i - x_mean) for i in x]
diff_y_mean = [(i - y_mean) for i in y]

# Calculating standard deviation
x_var = sum([(i - x_mean)**2 for i in x])
y_var = sum([(i - y_mean)**2 for i in y])
x_std = sqrt(x_var)
y_std = sqrt(y_var)

sum_diff = []
for i in range(len(x)):
    sum_diff.append(diff_x_mean[i] * diff_y_mean[i])

r = sum(sum_diff)/x_std * y_std
result = round(r, 3)
print(result)
