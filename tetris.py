import turtle, random, math
# I've Implemented Option 2 featuring different tetrominoes, Option 3 with one method that instantly drops the block using spacebar, and another which drops it faster using down key, and Option 6, featuring the game over screen.
SCALE = 32 #Controls how many pixels wide each grid ssudo apt install tk-devquare is
execute = True
class Game:
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
        self.timer_id = None  # Store the timer ID
        self.is_game_over = False
        self.border_turtle = turtle.Turtle()  # Create a separate turtle for the border
        self.score_turtle = turtle.Turtle()  # Create a separate turtle for the score
        self.draw_border()  # Draw the border
        self.score = 0  # Initialize score
        self.update_score_display()
            
        #Draw rectangular play area, height 20, width 10
        turtle.bgcolor('black')
        # turtle.pencolor('white')
        # turtle.penup()
        # turtle.setpos(-0.525, -0.525)
        # turtle.pendown()
        for i in range(2):
            turtle.forward(10.05)
            turtle.left(90)
            turtle.forward(20.05)
            turtle.left(90)
        self.score = 0  # Initialize the score
        self.score_display = turtle.Turtle()  # Turtle for showing the score
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.color("white")
        self.update_score_display()

        # Initialize game loop and controls
        self.active = Block()
        self.schedule_game_loop()  # Start the game loop
        turtle.onkeypress(self.rotate, 'Up')
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        turtle.onkeypress(self.down,'Down')
        turtle.onkeypress(self.downfast,'space ')
        turtle.onkeypress(self.restart, 'r')  # Add a restart key

        # turtle.onkeypress(self.downfast, 'Space')
        #These three lines must always be at the BOTTOM of __init__
        turtle.update()
        turtle.listen()
        turtle.mainloop()
    def draw_border(self):
        """Draw the game border with the border turtle."""
        self.border_turtle.hideturtle()
        self.border_turtle.speed(0)
        self.border_turtle.penup()
        self.border_turtle.pencolor('white')
        self.border_turtle.setpos(-0.525, -0.525)
        self.border_turtle.pendown()
        for i in range(2):
            self.border_turtle.forward(10.05)
            self.border_turtle.left(90)
            self.border_turtle.forward(20.05)
            self.border_turtle.left(90)
        self.border_turtle.penup()
    def update_score_display(self):
        """Update the score display turtle."""
        self.score_turtle.clear()  # Clear previous score display
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.goto(8, 19.75)  # Position above the play area
        self.score_turtle.color("white")
        self.score_turtle.write(f"Score: {self.score}", align="center", font=("Arial", 24, "bold"))


    def gameloop(self):
        # Game logic here
        if self.active.valid(0, -1, self.occupied):
            self.active.move(0, -1)
        elif self.check_none():
            self.display_game_over()
            self.disable_input()
            return False
        else:
            self.lock_block()
            self.check_complete_lines()
            self.active = Block()
            self.score += 10  # Increment score as an example
            self.update_score_display()  # Update score display
        
        turtle.update()
        self.schedule_game_loop()
    def schedule_game_loop(self):
        if self.timer_id:
            turtle.ontimer(None, self.timer_id)  # Cancel the previous timer
        self.timer_id = turtle.ontimer(self.gameloop, 300)  # Set the game loop and store the timer ID

    def display_game_over(self):
        self.is_game_over = True
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.goto(4.5, 11)
        t.color("black")
        t.write("GAME OVER", align="center", font=("Deja Vu Sans Mono", 40, "bold"))
        t.color("red")
        t.write("GAME OVER", align="center", font=("Deja Vu Sans Mono", 40, "normal"))
        t.goto(4.5, 9)
        t.color("black")
        t.write("Press 'R' to Restart", align="center", font=("Deja Vu Sans Mono", 24, "bold"))
        t.color("red")
        t.write("Press 'R' to Restart", align="center", font=("Deja Vu Sans Mono", 24, "normal"))
    def disable_input(self):
        turtle.onkeypress(None, 'Left')
        turtle.onkeypress(None, 'Right')
        turtle.onkeypress(None, 'Down')
        turtle.onkeypress(None, 'space')
    def check_none(self):
        for i in self.occupied[18]:
            if i is not None:
                return True
        return False
    def lock_block(self):
        for square in self.active.squares:
            x, y = int(square.xcor()), int(square.ycor())
            if y < 20 and x < 10:
                self.occupied[y][x] = square

    def check_complete_lines(self):
        lines_cleared = 0
        for i in range(20):
            if all(self.occupied[i]):
                self.clear_line(i)
                self.shift_down(i)
                lines_cleared += 1
        if lines_cleared > 0:
            self.score += lines_cleared * 100  # Increase score by 100 points per line cleared
            self.update_score_display()

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
        if self.active.is_square_shape:
            return
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
    def restart(self):
        if self.is_game_over:
            self.is_game_over = False
            self.score = 0
            self.update_score_display()
            self.occupied = [[None for _ in range(10)] for _ in range(20)]
            self.clear_all_turtles(exclude_border=True, exclude_score=True)  # Clear all but border and score
            self.active = Block()
            self.schedule_game_loop()  # Reset the game loop
            self.enable_input()
            turtle.update()
            return
    def enable_input(self):
        turtle.onkeypress(self.move_left, 'Left')
        turtle.onkeypress(self.move_right, 'Right')
        turtle.onkeypress(self.down, 'Down')
        turtle.onkeypress(self.downfast, 'space')
    def clear_all_turtles(self, exclude_border=False, exclude_score=False):
        turtles = turtle.turtles()
        for t in turtles:
            if exclude_border and t == self.border_turtle:
                continue  # Skip clearing the border turtle
            if exclude_score and t == self.score_turtle:
                continue  # Skip clearing the score turtle
            t.hideturtle()
            t.clear()
            t.goto(-1000, -1000)





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
        self.is_square_shape = False 
        for i in rand:
            self.squares.append(i)
        if len(self.squares) == 4 and self.squares[0].fillcolor() == 'yellow':
            self.is_square_shape = True
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
