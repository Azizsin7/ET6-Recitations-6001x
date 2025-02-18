#(main.py)

from problem3_1 import area  # Import the area function from problem3_1.py

# Step 1: Calculate the area of a circle with radius 5
radius = 5
circle_area = area(radius)
print(f"Computed area: {circle_area:.2f}")

# Step 2: Write the area to a file
file_name = "circle_area.txt"
file = open(file_name, 'w')  # Open file in write mode
file.write(f"Area of circle with radius {radius}: {circle_area:.2f}\n")
file.close()  # Close the file

# Step 3: Read the file and print its contents
file = open(file_name, 'r')  # Open file in read mode
for line in file:
    print(line.strip())  # Print each line without extra newline characters
file.close()  # Close the file
