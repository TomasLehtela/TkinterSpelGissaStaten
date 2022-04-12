import pandas as pd
import turtle

screen = turtle.Screen()
screen.title("Gissa Staten & Kapitalet - Enter 'Exit' to quit the game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")

x_cord_list = df.x.to_list()
y_cord_list = df.y.to_list()
states = df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"Guess the State {len(guessed_states)}/50", prompt="Name a state's name"
    ).title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        df_states = pd.DataFrame(missing_states, columns=["Wrong Guesses"])
        df_states.to_csv("wrong_guesses.csv")
        screen.bye()

    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, align="center", font=("Verdana", 6, "bold"))

turtle.mainloop()
