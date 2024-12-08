#FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     #print(a_dict["non_exist_key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The kew {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")

# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 3:
#     raise ValueError("Human Height should not be over 3 meters.")
# bmi = weight / height ** 2
# print(bmi)

fruits = ["Apple", "Pear", "Orange"]
# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

typed_index = int(input("Enter index: "))
try:
    make_pie(typed_index)
except IndexError:
    print("Fruit pie")