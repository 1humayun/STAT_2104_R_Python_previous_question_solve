#.........(i)....
A = matrix(c(1, 4, 5,-6, 8, 12), nrow = 3, byrow = T)
A

#......(ii)...
DF = data.frame(x1 = seq(1,2,3),         # x1 = 1
                x2 = rep(10,3),          # x2 = 10, 10, 10
                x3 = letters[1:3]        # x3 = a, b, c
                )
DF

#..........(iii)...
DF1 = DF[,2]
DF2 = DF[3,]

#..........(iv)....
x = 2.956004
floor(x)
ceiling(x)
signif(x,3)
