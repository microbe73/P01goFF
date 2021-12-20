from data.data_functions_v2 import *

reset_data()

print("Add profile")
print(add_profile("Fish", "tba", "17", "i like chips", "save rock and roll", "can't die if youre dead", "male"))

print("\nProfile Exists")
print(profile_exists("Fish"))

print(get_profile_value("Fish","quote"))

print(get_profiles())