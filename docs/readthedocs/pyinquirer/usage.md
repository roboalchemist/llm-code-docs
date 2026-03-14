# Usage

The idea is quite simple:

- 

Create an array of `Questions`

- 

Call the prompt render.

Each `Question` require some common arguments. So, you just need to know which kind of `Questions` and `Arguments` are available.

## Question types

**TEXT**

Expects a text answer.

**EDITOR**

Expects a text answer, entered through external editor.

**PASSWORD**

Do not prompt the answer.

**CONFIRM**

Requires a boolean answer.

**LIST**

Show a list and allow to select just one answer.

**CHECKBOX**

Show a list and allow to select a bunch of them.

**PATH**

Requires valid path and allows additional validations.

There are pictures of some of them in the Examples section.

## Question Arguments

The main object is `Question`, but it should not be
instantiated. You must use any of the subclasses, listed below. All of
them have the next attributes that can be set in the initialization:

### name

It will be the key in the hash of answers. So, it is **mandatory**.

You can use any `String` or `hashable` code as value.

### message

Contains the prompt to be shown to the user, and is **mandatory** too.

You can use a new style formatted string, using the previous answers, and it will be replaced automatically:

```
questions = [
    Text(name='name', message="What's your name?"),
    Text(name='surname', message="What's your surname, {name}")
]

```