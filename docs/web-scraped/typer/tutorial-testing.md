# Source: https://typer.tiangolo.com/tutorial/testing/

# Testing[¶](#testing "Permanent link")

Testing **Typer** applications is very easy with [pytest](https://docs.pytest.org/en/latest/).

Let\'s say you have an application `app/main.py` with:

Python 3.9+

So, you would use it like:

    $ python main.py Camila --city Berlin

    Hello Camila
    Let's have a coffee in Berlin

And the directory also has an empty `app/__init__.py` file.

So, the `app` is a \"Python package\".

## Test the app[¶](#test-the-app "Permanent link")

### Import and create a `CliRunner`[¶](#import-and-create-a-clirunner "Permanent link")

Create another file/module `app/test_main.py`.

Import `CliRunner` and create a `runner` object.

This runner is what will \"invoke\" or \"call\" your command line application.

Python 3.9+

Tip

It\'s important that the name of the file starts with `test_`, that way pytest will be able to detect it and use it automatically.

### Call the app[¶](#call-the-app "Permanent link")

Then create a function `test_app()`.

And inside of the function, use the `runner` to `invoke` the application.

The first parameter to `runner.invoke()` is a `Typer` app.

The second parameter is a `list` of `str`, with all the text you would pass in the command line, right as you would pass it:

Python 3.9+

Tip

The name of the function has to start with `test_`, that way pytest can detect it and use it automatically.

### Check the result[¶](#check-the-result "Permanent link")

Then, inside of the test function, add `assert` statements to ensure that everything in the result of the call is as it should be.

Python 3.9+

Here we are checking that the exit code is 0, as it is for programs that exit without errors.

Then we check that the text printed to \"standard output\" contains the text that our CLI program prints.

Tip

You could also check the output sent to \"standard error\" (`stderr`) or \"standard output\" (`stdout`) independently by accessing `result.stdout` and `result.stderr` in your tests.

Info

If you need a refresher about what is \"standard output\" and \"standard error\" check the section in [Printing and Colors: \"Standard Output\" and \"Standard Error\"](../printing/#standard-output-and-standard-error).

### Call `pytest`[¶](#call-pytest "Permanent link")

Then you can call `pytest` in your directory and it will run your tests:

    $ pytest

    ================ test session starts ================
    platform linux -- Python 3.10, pytest-5.3.5, py-1.8.1, pluggy-0.13.1
    rootdir: /home/user/code/superawesome-cli/app
    plugins: forked-1.1.3, xdist-1.31.0, cov-2.8.1
    collected 1 item

    ---> 100%

    test_main.py <span style="color: green; white-space: pre;">.                                 [100%]</span>

    <span style="color: green;">================= 1 passed in 0.03s =================</span>

## Testing input[¶](#testing-input "Permanent link")

If you have a CLI with prompts, like:

Python 3.9+

🤓 Other versions and variants

Python 3.9+ - non-Annotated

    import typer

    app = typer.Typer()

    @app.command()
    def main(name: str, email: str = typer.Option(..., prompt=True)):
        print(f"Hello , your email is: ")

    if __name__ == "__main__":
        app()

That you would use like:

    $ python main.py Camila

    # Email: $ camila@example.com

    Hello Camila, your email is: camila@example.com

You can test the input typed in the terminal using `input="camila@example.com\n"`.

This is because what you type in the terminal goes to \"**standard input**\" and is handled by the operating system as if it was a \"virtual file\".

Info

If you need a refresher about what is \"standard output\", \"standard error\", and \"standard input\" check the section in [Printing and Colors: \"Standard Output\" and \"Standard Error\"](../printing/#standard-output-and-standard-error).

When you hit the [ENTER] key after typing the email, that is just a \"new line character\". And in Python that is represented with `"\n"`.

So, if you use `input="camila@example.com\n"` it means: \"type `camila@example.com` in the terminal, then hit the [ENTER] key\":

Python 3.9+ - non-Annotated

🤓 Other versions and variants

Python 3.9+

## Test a function[¶](#test-a-function "Permanent link")

If you have a script and you never created an explicit `typer.Typer` app, like:

Python 3.9+

\...you can still test it, by creating an app during testing:

Python 3.9+

Of course, if you are testing that script, it\'s probably easier/cleaner to just create the explicit `typer.Typer` app in `main.py` instead of creating it just during the test.

But if you want to keep it that way, e.g. because it\'s a simple example in documentation, then you can use that trick.

### About the `app.command` decorator[¶](#about-the-appcommand-decorator "Permanent link") 

Notice the `app.command()(main)`.

If it\'s not obvious what it\'s doing, continue reading\...

You would normally write something like:

    @app.command()
    def main(name: str = "World"):
        # Some code here

But `@app.command()` is just a decorator.

That\'s equivalent to:

    def main(name: str = "World"):
        # Some code here

    decorator = app.command()

    new_main = decorator(main)
    main = new_main

`app.command()` returns a function (`decorator`) that takes another function as it\'s only parameter (`main`).

And by using the `@something` you normally tell Python to replace the thing below (the function `main`) with the return of the `decorator` function (`new_main`).

Now, in the specific case of **Typer**, the decorator doesn\'t change the original function. It registers it internally and returns it unmodified.

So, `new_main` is actually the same original `main`.

So, in the case of **Typer**, as it doesn\'t really modify the decorated function, that would be equivalent to:

    def main(name: str = "World"):
        # Some code here

    decorator = app.command()

    decorator(main)

But then we don\'t need to create the variable `decorator` to use it below, we can just use it directly:

    def main(name: str = "World"):
        # Some code here

    app.command()(main)

\...that\'s it. It\'s still probably simpler to just create the explicit `typer.Typer` in the `main.py` file 😅.