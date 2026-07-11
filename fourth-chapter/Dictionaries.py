info = {
    "name": "Neeharika Desai",
    "subjects": ["Java", "C++", "Python"],
    "age": 19,
    "is_adult": True
}
print(info)

print(info["age"])
print(type(info))

print(type(info["age"]))

info.update({
    "Address": "Maharashtara"
})
print(info)

if "name" in info:
    print("Name is present in the dictionary")
else:
    print("Name is not present in the dictionary")

print(info.keys())
print(info.values())
print (info.items())

print(info.get("name"))

print(list(info.keys()))