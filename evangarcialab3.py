#import turtle from turtle class.
import turtle

# Main method
def main():
    # Part 0: for loop that will print "Hello!" five times.
    
    for i in range(5):
        print("Hello!")
        
    # Creates a screen for my turtle, then turtle is created and named "evun".
    
    world = turtle.Screen()
    evun = turtle.Turtle()
    
    # Part 1: Creates evun the turtle and goes forward, turns right 90 degrees, then goes forward again.
    
    evun.forward(100)
    evun.right(90)
    evun.forward(100)

    # Part 2: Uses a for loop to make evun the turtle create a Square.
    
    for i in range(4):
         evun.forward(100)
         evun.right(90)
         
    evun.up()
    evun.goto(-100, 100)
    evun.down()
         
    # Part 3: Uses a for loop to make evun the turtle create a Equilateral Triangle.

    evun.left(90)
    for i in range(3):
        evun.forward(100)
        evun.left(120)
        
    evun.up()
    evun.goto(-200, 100)
    evun.down()

    # Part 4: Uses a Class method to define a circle using "evun" the turtle.
    
    evun.circle(50)
    
    evun.up()
    evun.goto(100, 150)
    evun.down()

    # Part 5: Uses for loop with iteration's four times to create the base of the house, then uses a for loop with the interation of three times to create the roof which is simulated with a triangle. All of this is done with the
    # creation of "evun" the turtle.
    
    for i in range(4):
        evun.forward(150)
        evun.right(90)
        
    for i in range(3):
        evun.forward(150)
        evun.left(120)
        
# Call for main method.
main()
