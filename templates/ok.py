import turtle
import pygame

# Initialize pygame mixer for playing music
pygame.mixer.init()
pygame.mixer.music.load("background.mp3")  # Load your music file
pygame.mixer.music.play(-1)  # Play on loop (-1 for infinite loop)

# Create a turtle screen and a turtle object
screen = turtle.Screen()
screen.title("Turtle with Background Music")
t = turtle.Turtle()

# Turtle drawing example
t.pensize(5)
t.color("blue")
for _ in range(36):
    t.forward(100)
    t.left(170)

# Close music on turtle screen click
screen.mainloop()
pygame.mixer.music.stop()
