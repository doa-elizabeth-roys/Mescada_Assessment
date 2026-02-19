def greet(name):
    print(f"Hello {name}")

print("Enter your name")
name = input()
if name == "Alice" or "Bob":
    greet(name)
