# Text Files

file = open("random.txt", "w")
print(file.write("jatin katyal"))

a = ["jatin", "samarth", "sujith", "saransh"]
print(file.writelines(a))
print(file.close())

# STREAMS
# --> Iterables which iterated in single direction
# --> They don't have starting and ending point

# CONTENT PROGRAMMING

class A():
    def __enter__(self):
        print("Entetred")
        return 1

    def __exit__(self, *args):
        print("Exitted")
        print(args)
        return True

with A() as x:
    print(x)
    print("inside context")
    raise Exception

print("outside context")

# JSON RULE
# --> keys can only be strings and numbers
# --> values can only be array, json, strings, numbers, boolean, null





