# Source: https://typer.tiangolo.com/tutorial/printing/

# Printing and Colors[¶](#printing-and-colors "Permanent link")

You can use the normal `print()` to show information on the screen:

Python 3.9+

It will show the output normally:

    $ python main.py World

    Hello World

## Use Rich[¶](#use-rich "Permanent link")

You can also display beautiful and more complex information using [Rich](https://rich.readthedocs.io/). It comes by default when you install `typer`.

### Use Rich `print`[¶](#use-rich-print "Permanent link")

For the simplest cases, you can just import `print` from `rich` and use it instead of the standard `print`:

Python 3.9+

Just with that, **Rich** will be able to print your data with nice colors and structure:

    $ python main.py

    Here's the data
    <b></b>,
            <b></b>
        <b>]</b>,
        <font color="#A6E22E">&apos;active&apos;</font>: <font color="#A6E22E"><i>True</i></font>,
        <font color="#A6E22E">&apos;affiliation&apos;</font>: <font color="#AE81FF"><i>None</i></font>
    <b>}</b>

### Rich Markup[¶](#rich-markup "Permanent link")

Rich also supports a [custom markup syntax](https://rich.readthedocs.io/en/stable/markup.html) to set colors and styles, for example:

Python 3.9+

    $ python main.py

    <font color="#F92672"><b>Alert!</b></font> <font color="#A6E22E">Portal gun</font> shooting! 💥

In this example you can see how to use font styles, colors, and even emojis.

To learn more check out the [Rich docs](https://rich.readthedocs.io/en/stable/markup.html).

### Rich Tables[¶](#rich-tables "Permanent link")

The way Rich works internally is that it uses a `Console` object to display the information.

When you call Rich\'s `print`, it automatically creates this object and uses it.

But for advanced use cases, you could create a `Console` yourself.

Python 3.9+

In this example, we create a `Console`, and a `Table`. And then we can add some rows to the table, and print it.

If you run it, you will see a nicely formatted table:

    $ python main.py

    ┏━━━━━━━┳━━━━━━━━━━━━┓
    ┃<b> Name  </b>┃<b> Item       </b>┃
    ┡━━━━━━━╇━━━━━━━━━━━━┩
    │ Rick  │ Portal Gun │
    │ Morty │ Plumbus    │
    └───────┴────────────┘

Rich has many other features, as an example, you can check the docs for:

-   [Prompt](https://rich.readthedocs.io/en/stable/prompt.html)
-   [Markdown](https://rich.readthedocs.io/en/stable/markdown.html)
-   [Panel](https://rich.readthedocs.io/en/stable/panel.html)
-   \...and more.

### Typer and Rich[¶](#typer-and-rich "Permanent link")

If you are wondering what tool should be used for what, **Typer** is useful for structuring the command line application, with options, arguments, subcommands, data validation, etc.

In general, **Typer** tends to be the entry point to your program, taking the first input from the user.

**Rich** is useful for the parts that need to *display* information. Showing beautiful content on the screen.

The best results for your command line application would be achieved combining both **Typer** and **Rich**.

## \"Standard Output\" and \"Standard Error\"[¶](#standard-output-and-standard-error "Permanent link")

The way printing works underneath is that the **operating system** (Linux, Windows, macOS) treats what we print as if our CLI program was **writing text** to a \"**virtual file**\" called \"**standard output**\".

When our code \"prints\" things it is actually \"writing\" to this \"virtual file\" of \"standard output\".

This might seem strange, but that\'s how the CLI program and the operating system interact with each other.

And then the operating system **shows on the screen** whatever our CLI program \"**wrote**\" to that \"**virtual file**\" called \"**standard output**\".

### Standard Error[¶](#standard-error "Permanent link")

And there\'s another \"**virtual file**\" called \"**standard error**\" that is normally only used for errors.

But we can also \"print\" to \"standard error\". And both are shown on the terminal to the users.

Info

If you use PowerShell it\'s quite possible that what you print to \"standard error\" won\'t be shown in the terminal.

In PowerShell, to see \"standard error\" you would have to check the variable `$Error`.

But it will work normally in Bash, Zsh, and Fish.

### Printing to \"standard error\"[¶](#printing-to-standard-error "Permanent link")

You can print to \"standard error\" creating a Rich `Console` with `stderr=True`.

Tip

`stderr` is short for \"standard error\".

Using `stderr=True` tells **Rich** that the output should be shown in \"standard error\".

Python 3.9+

When you try it in the terminal, it will probably just look the same:

    $ python main.py

    Here is something written to standard error

## \"Standard Input\"[¶](#standard-input "Permanent link")

As a final detail, when you type text in your keyboard to your terminal, the operating system also considers it another \"**virtual file**\" that you are writing text to.

This virtual file is called \"**standard input**\".

### What is this for[¶](#what-is-this-for "Permanent link")

Right now this probably seems quite useless 🤷‍♂.

But understanding that will come handy in the future, for example for autocompletion and testing.

## Typer Echo[¶](#typer-echo "Permanent link")

Warning

In most of the cases, for displaying advanced information, it is recommended to use [Rich](https://rich.readthedocs.io/).

You can probably skip the rest of this section. 🎉😎

**Typer** also has a small utility `typer.echo()` to print information on the screen, it comes directly from Click. But normally you shouldn\'t need it.

For the simplest cases, you can use the standard Python `print()`.

And for the cases where you want to display data more beautifully, or more advanced content, you should use **Rich** instead.

### Why `typer.echo`[¶](#why-typerecho "Permanent link") 

`typer.echo()` (which is actually just `click.echo()`) applies some checks to try and convert binary data to strings, and other similar things.

But in most of the cases you wouldn\'t need it, as in modern Python strings (`str`) already support and use Unicode, and you would rarely deal with pure `bytes` that you want to print on the screen.

If you have some `bytes` objects, you would probably want to decode them intentionally and directly before trying to print them.

And if you want to print data with colors and other features, you are much better off with the more advanced tools in **Rich**.

Info

`typer.echo()` comes directly from Click, you can read more about it in [Click\'s docs](https://click.palletsprojects.com/en/7.x/quickstart/#echoing).

### Color[¶](#color "Permanent link")

Technical Details

The way color works in terminals is by using some codes (ANSI escape sequences) as part of the text.

So, a colored text is still just a `str`.

Tip

Again, you are much better off using [Rich](https://rich.readthedocs.io/) for this. 😎

You can create colored strings to output to the terminal with `typer.style()`, that gives you `str`s that you can then pass to `typer.echo()`:

Python 3.9+

Tip

The parameters `fg` and `bg` receive strings with the color names for the \"**f**ore**g**round\" and \"**b**ack**g**round\" colors. You could simply pass `fg="green"` and `bg="red"`.

But **Typer** provides them all as variables like `typer.colors.GREEN` just so you can use autocompletion while selecting them.

Check it:

[python main.py] [everything is [good]] [python main.py \--no-good] [everything is [bad]]

You can pass these function arguments to `typer.style()`:

-   `fg`: the foreground color.
-   `bg`: the background color.
-   `bold`: enable or disable bold mode.
-   `dim`: enable or disable dim mode. This is badly supported.
-   `underline`: enable or disable underline.
-   `blink`: enable or disable blinking.
-   `reverse`: enable or disable inverse rendering (foreground becomes background and the other way round).
-   `reset`: by default a reset-all code is added at the end of the string which means that styles do not carry over. This can be disabled to compose styles.

Info

You can read more about it in [Click\'s docs about `style()`](https://click.palletsprojects.com/en/7.x/api/#click.style)

### `typer.secho()` - style and print[¶](#typersecho-style-and-print "Permanent link") 

Tip

In case you didn\'t see above, you are much better off using [Rich](https://rich.readthedocs.io/) for this. 😎

There\'s a shorter form to style and print at the same time with `typer.secho()` it\'s like `typer.echo()` but also adds style like `typer.style()`:

Python 3.9+

Check it:

[python main.py Camila] [Welcome here Camila]