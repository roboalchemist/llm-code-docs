# Asking for a choice

Similar to how the `prompt()` function allows for
text input, prompt_toolkit has a
`choice()` function to ask for a choice
from a list of options:

```
from prompt_toolkit.shortcuts import choice

result = choice(
    message="Please choose a dish:",
    options=[
        ("pizza", "Pizza with mushrooms"),
        ("salad", "Salad with tomatoes"),
        ("sushi", "Sushi"),
    ],
    default="salad",
)
print(f"You have chosen: {result}")

```