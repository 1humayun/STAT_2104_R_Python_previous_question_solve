import numpy as np

n = []
# geting input...
print("Enter 20 floating numbers: ")
for i in range(5):
    n.append(float(input()))

# calculating...
max_v = np.max(n)
min_v = np.min(n)
sum_v = np.sum(n)
mean_v = np.mean(n)
var_v = np.var(n)
print(f"Maximum: {max_v} \nMinimum: {min_v} \nSum: {sum_v} \nMean: {mean_v} \nVariance: {var_v}")

# another way of print...
#   print("\nMaximun: ", max_v, "\nMinimun: ", min_v, "\nSum: ", sum_v, "\nMean: ", mean_v, "\nVariance: ", var_v)