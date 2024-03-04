#Task1:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]


#Tasks2:

if sorted(submitted) == sorted(attended):
    print("The two list are identical in terms of their content, regardless of order.")


#Tasks3:
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]


for student in attended:
    if student not in submitted:
        attended.remove(student)
print(attended)