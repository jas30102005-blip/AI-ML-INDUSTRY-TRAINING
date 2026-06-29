x = 100      # Global variable

def demo():
    x = 50   # Local variable
    print("Inside Function:", x)

demo()

print("Outside Function:", x)