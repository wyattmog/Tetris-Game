import turtle, random, math
# I've Implemented Option 2 featuring different tetrominoes, Option 3 with one method that instantly drops the block using spacebar, and another which drops it faster using down key, and Option 6, featuring the game over screen.
SCALE = 32 #Controls how many pixels wide each grid ssudo apt install tk-devquare is

class Game:
    execute = True
    def __init__(self):
        #Setup window size based on SCALE value.
        turtle.setup(SCALE*12+20, SCALE*22+20)
        self.occupied = [
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,],
                         [None, None, None, None, None, None, None, None, None, None,]]
        # self.occupied = [
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,],
        #                  [False, False, False, False, False, False, False, False, False, False,]]
        #Bottom left corner of screen is (-1.5,-1.5)
        #Top right corner is (10.5, 20.5)
        turtle.setworldcoordinates(-1.5, -1.5, 10.5, 20.5)
        cv = turtle.getcanvas()
        cv.adjustScrolls()

        #Ensure turtle is running as fast as possible
        turtle.hideturtle()
        turtle.delay(0)
        turtle.speed(0)
        turtle.tracer(0, 0)

        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        turtle.pencolor('white')
        turtle.penup()
        turtle.setpos(-0.525, -0.525)
        turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)
        
        self.active = Block()
        turtle.ontimer(self.gameloop, 300)
        turtle.onkeypress(self.rotate, 'Up')
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        turtle.onkeypress(self.down,'Down')
        turtle.onkeypress(self.downfast,'space ')
        # turtle.onkeypress(self.downfast, 'Space')
        #These three lines must always be at the BOTTOM of __init__
        turtle.update()
        turtle.listen()
        turtle.mainloop()
    def gameloop(self):
        print("start\n")
        for i in self.occupied:
            print(i)
        print("end\n")
        # row = self.active.valid(0, -1, self.occupied)
        if self.active.valid(0, -1, self.occupied):
            self.active.move(0, -1)
        elif self.check_none():
            t = turtle.Turtle()
            t.speed(0)
            t.penup()
            t.goto(4.5,11)
            t.color("red")
            t.write("GAME OVER", align="center", font=("Arial", 40, "bold"))
            return False
        else:
            self.lock_block()
            self.check_complete_lines()
            self.active = Block()

        turtle.update()
        turtle.ontimer(self.gameloop, 300)

    def check_none(self):
        for i in self.occupied[19]:
            if i is not None:
                return True
        return False
    def lock_block(self):
        for square in self.active.squares:
            x, y = int(square.xcor()), int(square.ycor())
            if y < 20 and x < 10:
                self.occupied[y][x] = square

    def check_complete_lines(self):
        for i in range(20):
            if all(self.occupied[i]):
                self.clear_line(i)
                self.shift_down(i)

    def clear_line(self, row):
        for square in self.occupied[row]:
            square.hideturtle()
        for i in range(len(self.occupied[row])):
            self.occupied[row][i] = None

    def shift_down(self, row):
        for i in range(row, len(self.occupied) - 1, 1):  # Start from the row to shift down and move upwards
            for j in range(len(self.occupied[i])):  # Iterate through each column
                if self.occupied[i+1][j] != None:  # Check the block above the current row
                    square = self.occupied[i+1][j]
                    # Move the block down visually
                    x = square.xcor()
                    y = square.ycor() - 1
                    square.goto(x, y)
                    # Update the grid by shifting the block down
                    self.occupied[i][j] = square
                    self.occupied[i+1][j] = None
        turtle.update()

    def move_left(self):
        if self.active.valid(-1, 0, self.occupied) == True:
            self.active.move(-1, 0)
        turtle.update()   
    def rotate(self):
    # Choose the first square as the pivot for simplicity (you can change this logic)
        total_x = sum(square.xcor() for square in self.active.squares) / len(self.active.squares)
        total_y = sum(square.ycor() for square in self.active.squares) / len(self.active.squares)
    
    # Find the closest square to the geometric center to use as the pivot
        pivot = min(self.active.squares, key=lambda square: abs(square.xcor() - total_x) + abs(square.ycor() - total_y))
        pivot_x, pivot_y = pivot.xcor(), pivot.ycor()
        
        # Calculate new positions based on 90-degree rotation around the pivot
        new_positions = []
        for square in self.active.squares:
            old_x, old_y = square.xcor(), square.ycor()
            
            # Apply 90-degree rotation matrix around the pivot square
            new_x = pivot_y - old_y + pivot_x
            new_y = -(pivot_x - old_x) + pivot_y
            new_positions.append((new_x, new_y))
        
        # Check if all new positions are valid
        if all(0 <= new_x <= 9 and new_y >= 0 and (new_y >= 20 or self.occupied[int(new_y)][int(new_x)] is None)
            for new_x, new_y in new_positions):
            # If valid, move squares to the new positions
            for square, (new_x, new_y) in zip(self.active.squares, new_positions):
                square.goto(new_x, new_y)

    def move_right(self):
        if self.active.valid(1, 0, self.occupied) == True:
            self.active.move(1, 0)
        turtle.update()
    def down(self):
        if self.active.valid(0, -1, self.occupied) == True:
            self.active.move(0, -1)
        turtle.update()
    def downfast(self):
        while self.active.valid(0, -1, self.occupied) == True:
            self.active.move(0, -1)
        turtle.update()
        
            




class Square(turtle.Turtle):
    def __init__(self, x, y, color):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.shapesize(SCALE/20)
        self.speed(0)
        self.fillcolor(color)
        self.pencolor('gray')
        self.penup()
        self.goto(x,y)


class Block:
    def __init__(self):
        self.shapes = [ [Square(3,22,'cyan'), Square(4,22,'cyan'), Square(5,22,'cyan'), Square(6,22,'cyan')], 
                        [Square(3,23,'blue'), Square(3,22,'blue'), Square(4,22,'blue'), Square(5,22,'blue')], 
                        [Square(3,22,'orange'), Square(4,22,'orange'), Square(5,22,'orange'), Square(5,23,'orange')], 
                        [Square(4,23,'yellow'), Square(4,22,'yellow'), Square(5,23,'yellow'), Square(5,22,'yellow')], 
                        [Square(4,22,'green'), Square(5,22,'green'), Square(5,23,'green'), Square(6,23,'green')], 
                        [Square(3,22,'purple'), Square(4,22,'purple'), Square(4,23,'purple'), Square(5,22,'purple')], 
                        [Square(3,23,'red'), Square(4,23,'red'), Square(4,22,'red'), Square(5,22,'red')]]
        self.squares = []
        rand = random.choice(self.shapes)
        for i in rand:
            self.squares.append(i)
    def move(self, dx, dy):
        for square in self.squares:
            x = square.xcor() + dx
            y = square.ycor() + dy
            square.goto(x, y)
    def square_valid(self, square, occupied):
        x = square.xcor() + 0
        y = square.ycor() + -1
        if x < 0 or x > 9:
            return False
        elif y < 0:
            return False
        elif y <= 19 and occupied[y][x] != None:
            return False
        return True
    def valid(self, dx, dy, occupied):
        for square in self.squares:
            x = square.xcor() + dx
            y = square.ycor() + dy
            if x < 0 or x > 9 or y < 0 or (y < 20 and occupied[int(y)][int(x)]):
                return False
        return True
if __name__ == '__main__':
    Game()
