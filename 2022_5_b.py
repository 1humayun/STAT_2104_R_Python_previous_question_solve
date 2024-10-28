
import pandas as pd
#.............(i)...........
data = {
    "names": ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    "score": [59, 51, 72, 79, 79, 83, 69, 81, 51, 87]
}

df = pd.DataFrame(data)
print(df)

#................(ii)............

names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(names , "\n", type(names))

score = [59, 51, 72, 79, 79, 83, 69, 81, 51, 87]
print(score , "\n", type(score))

#................(iii).............

#accessing names in two ways ...
# Way 1: access by index number
way_1 = names[1]
print("Way 1: ", way_1)

# Way 2: Find the index of "B" and access it
index_of_B = names.index("B")
way_2 = names[index_of_B]
print("Way 2: ", way_2)