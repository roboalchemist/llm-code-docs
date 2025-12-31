# Source: https://typer.tiangolo.com/tutorial/progressbar/

# Progress Bar[¶](#progress-bar "Permanent link")

If you are executing an operation that can take some time, you can inform it to the user. 🤓

## Progress Bar[¶](#progress-bar_1 "Permanent link") 

You can use [Rich\'s Progress Display](https://rich.readthedocs.io/en/stable/progress.html) to show a progress bar, for example:

Python 3.9+

You put the thing that you want to iterate over inside of Rich\'s `track()`, and then iterate over that.

Check it:

    $ python main.py

    ---> 100%

    Processed 100 things.

\...actually, it will look a lot prettier. ✨ But I can\'t show you the animation here in the docs. 😅

The colors and information will look something like this:

    $ python main.py

    Processing... <font color="#F92672">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸</font><font color="#3A3A3A">━━━━━━━━━━</font> <font color="#AE81FF"> 74%</font> <font color="#A1EFE4">0:00:01</font>

## Spinner[¶](#spinner "Permanent link")

When you don\'t know how long the operation will take, you can use a spinner instead.

Rich allows you to display many things in complex and advanced ways.

For example, this will show two spinners:

Python 3.9+

I can\'t show you the beautiful animation here in the docs. 😅

But at some point in time it will look like this (imagine it\'s spinning). 🤓

    $ python main.py

    <font color="#A6E22E">⠹</font> Processing...
    <font color="#A6E22E">⠹</font> Preparing...

You can learn more about it in the [Rich docs for Progress Display](https://rich.readthedocs.io/en/stable/progress.html).

## Typer `progressbar`[¶](#typer-progressbar "Permanent link")

If you can, you should use **Rich** as explained above, it has more features, it\'s more advanced, and can display information more beautifully. ✨

Tip

If you can use Rich, use the information above, the Rich docs, and skip the rest of this page. 😎

But if you can\'t use Rich, Typer (actually Click) comes with a simple utility to show progress bars.

Info

`typer.progressbar()` comes directly from Click, you can read more about it in [Click\'s docs](https://click.palletsprojects.com/en/8.1.x/utils/#showing-progress-bars).

### Use `typer.progressbar`[¶](#use-typerprogressbar "Permanent link") 

Tip

Remember, you are much better off using [Rich](https://rich.readthedocs.io/) for this. 😎

You can use `typer.progressbar()` with a `with` statement, as in:

    with typer.progressbar(something) as progress:
        pass

And you pass as function argument to `typer.progressbar()` the thing that you would normally iterate over.

Python 3.9+

So, if you have a list of users, this could be:

    users = ["Camila", "Rick", "Morty"]

    with typer.progressbar(users) as progress:
        pass

And the `with` statement using `typer.progressbar()` gives you an object that you can iterate over, just like if it was the same thing that you would iterate over normally.

But by iterating over this object **Typer** (actually Click) will know to update the progress bar:

    users = ["Camila", "Rick", "Morty"]

    with typer.progressbar(users) as progress:
        for user in progress:
            typer.echo(user)

Tip

Notice that there are 2 levels of code blocks. One for the `with` statement and one for the `for` statement.

Info

This is mostly useful for operations that take some time.

In the example above we are faking it with `time.sleep()`.

Check it:

    $ python main.py

    ---> 100%

    Processed 100 things.

### Setting a Progress Bar `length`[¶](#setting-a-progress-bar-length "Permanent link")

Tip

Remember, you are much better off using [Rich](https://rich.readthedocs.io/) for this. 😎

The progress bar is generated from the length of the iterable (e.g. the list of users).

But if the length is not available (for example, with something that fetches a new user from a web API each time) you can pass an explicit `length` to `typer.progressbar()`.

Python 3.9+

Check it:

    $ python main.py

    ---> 100%

    Processed 100 user IDs.

#### About the function with `yield`[¶](#about-the-function-with-yield "Permanent link")

If you hadn\'t seen something like that `yield` above, that\'s a \"[generator](https://docs.python.org/3/glossary.html#term-generator)\".

You can iterate over that function with a `for` and at each iteration it will give you the value at `yield`.

`yield` is like a `return` that gives values multiple times and let\'s you use the function in a `for` loop.

For example:

    def iterate_user_ids():
        # Let's imagine this is a web API, not a range()
        for i in range(100):
            yield i

    for i in iterate_user_ids():
        print(i)

would print each of the \"user IDs\" (here it\'s just the numbers from `0` to `99`).

### Add a `label`[¶](#add-a-label "Permanent link")

Tip

Remember, you are much better off using [Rich](https://rich.readthedocs.io/) for this. 😎

You can also set a `label`:

Python 3.9+

Check it:

[python main.py] [] [Processed 100 things.]

## Iterate manually[¶](#iterate-manually "Permanent link")

If you need to manually iterate over something and update the progress bar irregularly, you can do it by not passing an iterable but just a `length` to `typer.progressbar()`.

And then calling the `.update()` method in the object from the `with` statement:

Python 3.9+

Check it:

[python main.py] [] [Processed 1000 things in batches.]