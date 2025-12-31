# Source: https://rich.readthedocs.io/en/latest/syntax.html

# Syntax[](#syntax "Link to this heading")

Rich can syntax highlight various programming languages with line numbers.

To syntax highlight code, construct a [[`Syntax`]](reference/syntax.html#rich.syntax.Syntax "rich.syntax.Syntax") object and print it to the console. Here's an example:

    from rich.console import Console
    from rich.syntax import Syntax

    console = Console()
    with open("syntax.py", "rt") as code_file:
        syntax = Syntax(code_file.read(), "python")
    console.print(syntax)

You may also use the [[`from_path()`]](reference/syntax.html#rich.syntax.Syntax.from_path "rich.syntax.Syntax.from_path") alternative constructor which will load the code from disk and auto-detect the file type. The example above could be re-written as follows:

    from rich.console import Console
    from rich.syntax import Syntax

    console = Console()
    syntax = Syntax.from_path("syntax.py")
    console.print(syntax)

## Line numbers[](#line-numbers "Link to this heading")

If you set [`line_numbers=True`], Rich will render a column for line numbers:

    syntax = Syntax.from_path("syntax.py", line_numbers=True)