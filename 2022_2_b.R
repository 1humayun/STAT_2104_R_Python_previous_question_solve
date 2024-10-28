# a vector with missing value(NA)...
roll = c(1, NA, 3, 4, NA, 6, NA)

#find the number of missing value...
num_na = sum(is.na(roll))

"
#  is.na(roll) returns a logical vector, with TRUE for each missing (NA) value and FALSE otherwise.
#   sum(is.na(roll)) counts the number of TRUE values, effectively giving the count of missing values in the vector.
"

#remove missing value...
roll_new = na.omit(roll)
roll_new
