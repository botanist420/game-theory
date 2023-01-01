import json

lucas_dict = {"test value": "Lucas your dick is so big man",
        "new skill": ["linux command learning", "machine learning process"]}
print(lucas_dict)

with open("test_jj", mode="w", encoding="utf-8") as file:
    json.dump(lucas_dict, file, indent=4)

print("the program is ending, created by Lucas Lee")

