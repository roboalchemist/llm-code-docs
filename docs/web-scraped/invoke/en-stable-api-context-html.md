# Source: https://docs.pyinvoke.org/en/stable/api/context.html

Title: context — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/api/context.html

Markdown Content:
_class_ invoke.context.Context(_config:Optional[[invoke.config.Config](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config")]=None_)[¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "Permalink to this definition")
Context-aware API wrapper & state-passing object.

[`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") objects are created during command-line parsing (or, if desired, by hand) and used to share parser and configuration state with executed tasks (see [Aside: what exactly is this ‘context’ arg anyway?](https://docs.pyinvoke.org/en/stable/getting-started.html#why-context)).

Specifically, the class offers wrappers for core API calls (such as [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run")) which take into account CLI parser flags, configuration files, and/or changes made at runtime. It also acts as a proxy for its `config` attribute - see that attribute’s documentation for details.

Instances of [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") may be shared between tasks when executing sub-tasks - either the same context the caller was given, or an altered copy thereof (or, theoretically, a brand new one).

New in version 1.0.

 __init__ (_config:Optional[[invoke.config.Config](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config")]=None_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.__init__ "Permalink to this definition")Parameters
**config** –

[`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") object to use as the base configuration.

Defaults to an anonymous/default [`Config`](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config") instance.

cd(_path:Union[os.PathLike,[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")]_)→Generator[[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.cd "Permalink to this definition")
Context manager that keeps directory state when executing commands.

Any calls to [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run"), [`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "invoke.context.Context.sudo"), within the wrapped block will implicitly have a string similar to `"cd <path> && "` prefixed in order to give the sense that there is actually statefulness involved.

Because use of [`cd`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.cd "invoke.context.Context.cd") affects all such invocations, any code making use of the [`cwd`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.cwd "invoke.context.Context.cwd") property will also be affected by use of [`cd`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.cd "invoke.context.Context.cd").

Like the actual ‘cd’ shell builtin, [`cd`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.cd "invoke.context.Context.cd") may be called with relative paths (keep in mind that your default starting directory is your user’s `$HOME`) and may be nested as well.

Below is a “normal” attempt at using the shell ‘cd’, which doesn’t work since all commands are executed in individual subprocesses – state is **not** kept between invocations of [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run") or [`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "invoke.context.Context.sudo"):

c.run('cd /var/www')
c.run('ls')

The above snippet will list the contents of the user’s `$HOME` instead of `/var/www`. With [`cd`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.cd "invoke.context.Context.cd"), however, it will work as expected:

with c.cd('/var/www'):
    c.run('ls')  # Turns into "cd /var/www && ls"

Finally, a demonstration (see inline comments) of nesting:

with c.cd('/var/www'):
    c.run('ls') # cd /var/www && ls
    with c.cd('website1'):
        c.run('ls')  # cd /var/www/website1 && ls

Note

Space characters will be escaped automatically to make dealing with such directory names easier.

New in version 1.0.

Changed in version 1.5: Explicitly cast the `path` argument (the only argument) to a string; this allows any object defining `__str__` to be handed in (such as the various `Path` objects out there), and not just string literals.

_property_ cwd _:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_[¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.cwd "Permalink to this definition")
Return the current working directory, accounting for uses of [`cd`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.cd "invoke.context.Context.cd").

New in version 1.0.

prefix(_command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_)→Generator[[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)"),[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")][¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.prefix "Permalink to this definition")
Prefix all nested [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run")/[`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "invoke.context.Context.sudo") commands with given command plus `&&`.

Most of the time, you’ll want to be using this alongside a shell script which alters shell state, such as ones which export or alter shell environment variables.

For example, one of the most common uses of this tool is with the `workon` command from [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/):

with c.prefix('workon myvenv'):
    c.run('./manage.py migrate')

In the above snippet, the actual shell command run would be this:

$ workon myvenv && ./manage.py migrate

This context manager is compatible with [`cd`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.cd "invoke.context.Context.cd"), so if your virtualenv doesn’t `cd` in its `postactivate` script, you could do the following:

with c.cd('/path/to/app'):
    with c.prefix('workon myvenv'):
        c.run('./manage.py migrate')
        c.run('./manage.py loaddata fixture')

Which would result in executions like so:

$ cd /path/to/app && workon myvenv && ./manage.py migrate
$ cd /path/to/app && workon myvenv && ./manage.py loaddata fixture

Finally, as alluded to above, [`prefix`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.prefix "invoke.context.Context.prefix") may be nested if desired, e.g.:

with c.prefix('workon myenv'):
    c.run('ls')
    with c.prefix('source /some/script'):
        c.run('touch a_file')

The result:

$ workon myenv && ls
$ workon myenv && source /some/script && touch a_file

Contrived, but hopefully illustrative.

New in version 1.0.

run(_command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _**kwargs:Any_)→Optional[[invoke.runners.Result](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result")][¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "Permalink to this definition")
Execute a local shell command, honoring config options.

Specifically, this method instantiates a [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") subclass (according to the `runner` config option; default is [`Local`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local "invoke.runners.Local")) and calls its `.run` method with `command` and `kwargs`.

See [`Runner.run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") for details on `command` and the available keyword arguments.

New in version 1.0.

sudo(_command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _**kwargs:Any_)→Optional[[invoke.runners.Result](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result")][¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "Permalink to this definition")
Execute a shell command via `sudo` with password auto-response.

**Basics**

This method is identical to [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run") but adds a handful of convenient behaviors around invoking the `sudo` program. It doesn’t do anything users could not do themselves by wrapping [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run"), but the use case is too common to make users reinvent these wheels themselves.

Note

If you intend to respond to sudo’s password prompt by hand, just use `run("sudo command")` instead! The autoresponding features in this method will just get in your way.

Specifically, [`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "invoke.context.Context.sudo"):

*   Places a [`FailingResponder`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.FailingResponder "invoke.watchers.FailingResponder") into the `watchers` kwarg (see [Automatically responding to program output](https://docs.pyinvoke.org/en/stable/concepts/watchers.html)) which:

> *   searches for the configured `sudo` password prompt;
> 
>     *   responds with the configured sudo password (`sudo.password` from the [configuration](https://docs.pyinvoke.org/en/stable/concepts/configuration.html));
> 
>     *   can tell when that response causes an authentication failure (e.g. if the system requires a password and one was not configured), and raises [`AuthFailure`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.AuthFailure "invoke.exceptions.AuthFailure") if so.

*   Builds a `sudo` command string using the supplied `command` argument, prefixed by various flags (see below);

*   Executes that command via a call to [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run"), returning the result.

**Flags used**

`sudo` flags used under the hood include:

*   `-S` to allow auto-responding of password via stdin;

*   `-p <prompt>` to explicitly state the prompt to use, so we can be sure our auto-responder knows what to look for;

*   `-u <user>` if `user` is not `None`, to execute the command as a user other than `root`;

*   When `-u` is present, `-H` is also added, to ensure the subprocess has the requested user’s `$HOME` set properly.

**Configuring behavior**

There are a couple of ways to change how this method behaves:

*   Because it wraps [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run"), it honors all [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run") config parameters and keyword arguments, in the same way that [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run") does.

> *   Thus, invocations such as `c.sudo('command', echo=True)` are possible, and if a config layer (such as a config file or env var) specifies that e.g. `run.warn = True`, that too will take effect under [`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "invoke.context.Context.sudo").

*   [`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "invoke.context.Context.sudo") has its own set of keyword arguments (see below) and they are also all controllable via the configuration system, under the `sudo.*` tree.

> *   Thus you could, for example, pre-set a sudo user in a config file; such as an `invoke.json` containing 
> ```
> {"sudo": {"user":
> "someuser"}}
> ```
> .

Parameters
*   **password** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Runtime override for `sudo.password`.

*   **user** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Runtime override for `sudo.user`.

New in version 1.0.

_class_ invoke.context.MockContext(_config:Optional[[invoke.config.Config](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config")]=None_, _**kwargs:Any_)[¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext "Permalink to this definition")
A [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context") whose methods’ return values can be predetermined.

Primarily useful for testing Invoke-using codebases.

Note

This class wraps its `run`, etc methods in `unittest.mock.Mock` objects. This allows you to easily assert that the methods (still returning the values you prepare them with) were actually called.

Note

Methods not given [`Results`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") to yield will raise `NotImplementedError` if called (since the alternative is to call the real underlying method - typically undesirable when mocking.)

New in version 1.0.

Changed in version 1.5: Added `Mock` wrapping of `run` and `sudo`.

 __init__ (_config:Optional[[invoke.config.Config](https://docs.pyinvoke.org/en/stable/api/config.html#invoke.config.Config "invoke.config.Config")]=None_, _**kwargs:Any_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.__init__ "Permalink to this definition")
Create a `Context`-like object whose methods yield [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") objects.

Parameters
*   **config** – A Configuration object to use. Identical in behavior to [`Context`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context "invoke.context.Context").

*   **run** –

A data structure indicating what [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") objects to return from calls to the instantiated object’s [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.run "invoke.context.Context.run") method (instead of actually executing the requested shell command).

Specifically, this kwarg accepts:

    *   A single [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") object.

    *   A boolean; if True, yields a [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") whose `exited` is `0`, and if False, `1`.

    *   An iterable of the above values, which will be returned on each subsequent call to `.run` (the first item on the first call, the second on the second call, etc).

    *   A dict mapping command strings or compiled regexen to the above values (including an iterable), allowing specific call-and-response semantics instead of assuming a call order.

*   **sudo** – Identical to `run`, but whose values are yielded from calls to [`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.Context.sudo "invoke.context.Context.sudo").

*   **repeat** ([_bool_](https://docs.python.org/2.7/library/functions.html#bool "(in Python v2.7)")) –

A flag determining whether results yielded by this class’ methods repeat or are consumed.

For example, when a single result is indicated, it will normally only be returned once, causing `NotImplementedError` afterwards. But when `repeat=True` is given, that result is returned on every call, forever.

Similarly, iterable results are normally exhausted once, but when this setting is enabled, they are wrapped in [`itertools.cycle`](https://docs.python.org/2.7/library/itertools.html#itertools.cycle "(in Python v2.7)").

Default: `True`.

Raises
`TypeError`, if the values given to `run` or other kwargs aren’t of the expected types.

Changed in version 1.5: Added support for boolean and string result values.

Changed in version 1.5: Added support for regex dict keys.

Changed in version 1.5: Added the `repeat` keyword argument.

Changed in version 2.0: Changed `repeat` default value from `False` to `True`.

run(_command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _*args:Any_, _**kwargs:Any_)→[invoke.runners.Result](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result")[¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.run "Permalink to this definition")
Execute a local shell command, honoring config options.

Specifically, this method instantiates a [`Runner`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner "invoke.runners.Runner") subclass (according to the `runner` config option; default is [`Local`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Local "invoke.runners.Local")) and calls its `.run` method with `command` and `kwargs`.

See [`Runner.run`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Runner.run "invoke.runners.Runner.run") for details on `command` and the available keyword arguments.

New in version 1.0.

set_result_for(_attname:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _result:[invoke.runners.Result](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result")_)→[None](https://docs.python.org/2.7/library/constants.html#None "(in Python v2.7)")[¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.set_result_for "Permalink to this definition")
Modify the stored mock results for given `attname` (e.g. `run`).

This is similar to how one instantiates [`MockContext`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext "invoke.context.MockContext") with a `run` or `sudo` dict kwarg. For example, this:

mc = MockContext(run={'mycommand': Result("mystdout")})
assert mc.run('mycommand').stdout == "mystdout"

is functionally equivalent to this:

mc = MockContext()
mc.set_result_for('run', 'mycommand', Result("mystdout"))
assert mc.run('mycommand').stdout == "mystdout"

[`set_result_for`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.set_result_for "invoke.context.MockContext.set_result_for") is mostly useful for modifying an already-instantiated [`MockContext`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext "invoke.context.MockContext"), such as one created by test setup or helper methods.

New in version 1.0.

sudo(_command:[str](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")_, _*args:Any_, _**kwargs:Any_)→[invoke.runners.Result](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result")[¶](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.sudo "Permalink to this definition")
Execute a shell command via `sudo` with password auto-response.

**Basics**

This method is identical to [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.run "invoke.context.MockContext.run") but adds a handful of convenient behaviors around invoking the `sudo` program. It doesn’t do anything users could not do themselves by wrapping [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.run "invoke.context.MockContext.run"), but the use case is too common to make users reinvent these wheels themselves.

Note

If you intend to respond to sudo’s password prompt by hand, just use `run("sudo command")` instead! The autoresponding features in this method will just get in your way.

Specifically, [`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.sudo "invoke.context.MockContext.sudo"):

*   Places a [`FailingResponder`](https://docs.pyinvoke.org/en/stable/api/watchers.html#invoke.watchers.FailingResponder "invoke.watchers.FailingResponder") into the `watchers` kwarg (see [Automatically responding to program output](https://docs.pyinvoke.org/en/stable/concepts/watchers.html)) which:

> *   searches for the configured `sudo` password prompt;
> 
>     *   responds with the configured sudo password (`sudo.password` from the [configuration](https://docs.pyinvoke.org/en/stable/concepts/configuration.html));
> 
>     *   can tell when that response causes an authentication failure (e.g. if the system requires a password and one was not configured), and raises [`AuthFailure`](https://docs.pyinvoke.org/en/stable/api/exceptions.html#invoke.exceptions.AuthFailure "invoke.exceptions.AuthFailure") if so.

*   Builds a `sudo` command string using the supplied `command` argument, prefixed by various flags (see below);

*   Executes that command via a call to [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.run "invoke.context.MockContext.run"), returning the result.

**Flags used**

`sudo` flags used under the hood include:

*   `-S` to allow auto-responding of password via stdin;

*   `-p <prompt>` to explicitly state the prompt to use, so we can be sure our auto-responder knows what to look for;

*   `-u <user>` if `user` is not `None`, to execute the command as a user other than `root`;

*   When `-u` is present, `-H` is also added, to ensure the subprocess has the requested user’s `$HOME` set properly.

**Configuring behavior**

There are a couple of ways to change how this method behaves:

*   Because it wraps [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.run "invoke.context.MockContext.run"), it honors all [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.run "invoke.context.MockContext.run") config parameters and keyword arguments, in the same way that [`run`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.run "invoke.context.MockContext.run") does.

> *   Thus, invocations such as `c.sudo('command', echo=True)` are possible, and if a config layer (such as a config file or env var) specifies that e.g. `run.warn = True`, that too will take effect under [`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.sudo "invoke.context.MockContext.sudo").

*   [`sudo`](https://docs.pyinvoke.org/en/stable/api/context.html#invoke.context.MockContext.sudo "invoke.context.MockContext.sudo") has its own set of keyword arguments (see below) and they are also all controllable via the configuration system, under the `sudo.*` tree.

> *   Thus you could, for example, pre-set a sudo user in a config file; such as an `invoke.json` containing 
> ```
> {"sudo": {"user":
> "someuser"}}
> ```
> .

Parameters
*   **password** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Runtime override for `sudo.password`.

*   **user** ([_str_](https://docs.python.org/2.7/library/functions.html#str "(in Python v2.7)")) – Runtime override for `sudo.user`.

New in version 1.0.
