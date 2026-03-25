# Source: https://docs.pyinvoke.org/en/stable/concepts/watchers.html

Title: Automatically responding to program output — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/concepts/watchers.html

Markdown Content:
Background[¶](https://docs.pyinvoke.org/en/stable/concepts/watchers.html#background "Permalink to this headline")
-----------------------------------------------------------------------------------------------------------------

Command-line programs tend to be designed for interactive shells, which frequently manifests as waiting around for user input, or “prompts”. Well-designed programs offer options for pre-empting such prompts, resulting in an easily automated workflow – but with the rest, interactivity is unavoidable.

Thankfully, Invoke’s [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") class not only forwards your standard input to the running program (allowing you to manually respond to prompts) but it can also be configured to respond automatically on your behalf.

Basic use[¶](https://docs.pyinvoke.org/en/stable/concepts/watchers.html#basic-use "Permalink to this headline")
---------------------------------------------------------------------------------------------------------------

The mechanism for this automation is the `watchers` kwarg to the [`Runner.run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") method (and its wrappers elsewhere, such as [`Context.run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run") and [`invoke.run`](https://docs.pyinvoke.org/en/stable/api/__init__.html#invoke.run "invoke.run")), which is a list of [`StreamWatcher`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.StreamWatcher "invoke.watchers.StreamWatcher")-subclass instances configured to watch for patterns & respond accordingly. The simplest of these is [`Responder`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder "invoke.watchers.Responder"), which just replies with its configured response every time its pattern is seen; others can be found in the [watchers module](https://docs.pyinvoke.org/en/stable/api/watchers.html).

Note

As with all other arguments to `run`, you can also set the default set of watchers globally via [configuration files](https://docs.pyinvoke.org/en/stable/concepts/configuration.html).

Take for example this program which expects a manual response to a yes/no prompt:

$ excitable-program
When you give the OK, I'm going to do the things. All of them!!
Are you ready? [Y/n] y
OK! I just did all sorts of neat stuff. You're welcome! Bye!

You _could_ call `run("excitable-program")`, manually watch for the prompt, and mash Y by hand. But if you instead supply a [`Responder`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder "invoke.watchers.Responder") like so:

@task
def always_ready(c):
    responder = Responder(
        pattern=r"Are you ready? \[Y/n\] ",
        response="y\n",
    )
    c.run("excitable-program", watchers=[responder])

Then [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") passes the program’s `stdout` and `stderr` through `responder`, which watches for `"Are you ready? [Y/n] "` and automatically writes `y` (plus `\n` to simulate hitting Enter/Return) to the program’s `stdin`.

Note

The pattern argument to [`Responder`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.Responder "invoke.watchers.Responder") is treated as a [`regular expression`](https://docs.python.org/2.7/library/re.html#module-re "(in Python v2.7)"), requiring more care (note how we had to escape our square-brackets in the above example) but providing more power as well.
