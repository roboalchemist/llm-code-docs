# Source: https://docs.pyinvoke.org/en/stable/invoke.html

Title: inv[oke] core usage — Invoke documentation

URL Source: https://docs.pyinvoke.org/en/stable/invoke.html

Markdown Content:
See also

This page documents `invoke`’s core arguments, options and behavior (which includes options present in [custom Invoke-based binaries](https://docs.pyinvoke.org/en/stable/concepts/library.html#reusing-as-a-binary)). For details on invoking user-specified tasks and other parser-related details, see [Invoking tasks](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html).

Core options and flags[¶](https://docs.pyinvoke.org/en/stable/invoke.html#core-options-and-flags "Permalink to this headline")
------------------------------------------------------------------------------------------------------------------------------

`invoke`’s usage looks like:

$ inv[oke] [--core-opts] task1 [--task1-opts] ... taskN [--taskN-opts]

All core options & flags are below; almost all of them must be given _before_ any task names, with a few (such as [`--help`](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-h)) being specially looked for anywhere in the command line. (For parsing details, see [Basic command line layout](https://docs.pyinvoke.org/en/stable/concepts/invoking-tasks.html#basic-cli-layout).)

--complete[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-complete "Permalink to this definition")
Print (line-separated) valid tab-completion options for an Invoke command line given as the ‘remainder’ (i.e. after a `--`). Used for building [shell completion scripts](https://docs.pyinvoke.org/en/stable/invoke.html#tab-completion).

For example, when the local tasks tree contains tasks named `foo` and `bar`, and when `foo` takes flags `--foo-arg` and `--foo-arg-2`, you might use it like this:

# Empty input: just task names
$ inv --complete --
foo
bar

# Input not ending with a dash: task names still
$ inv --complete -- foo --foo-arg
foo
bar

# Input ending with a dash: current context's flag names
$ inv --complete -- foo -
--foo-arg
--foo-arg-2

For more details on how to make best use of this option, see [`--print-completion-script`](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-print-completion-script).

--hide=STRING[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-hide "Permalink to this definition")
Set default value of run()’s ‘hide’ kwarg.

--no-dedupe[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-no-dedupe "Permalink to this definition")
Disable task deduplication.

--print-completion-script=SHELL[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-print-completion-script "Permalink to this definition")
Print a completion script for desired `SHELL` (e.g. `bash`, `zsh`, etc). This can be sourced into the current session in order to enjoy [tab-completion for tasks and options](https://docs.pyinvoke.org/en/stable/invoke.html#tab-completion).

These scripts are bundled with Invoke’s distributed codebase, and internally make use of [`--complete`](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-complete).

--prompt-for-sudo-password[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-prompt-for-sudo-password "Permalink to this definition")
Prompt at the start of the session (before executing any tasks) for the `sudo.password` configuration value. This allows users who don’t want to keep sensitive material in the config system or their shell environment to rely on user input, without otherwise interrupting the flow of the program.

--write-pyc[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-write-pyc "Permalink to this definition")
By default, Invoke disables bytecode caching as it can cause hard-to-debug problems with task files and (for the kinds of things Invoke is typically used for) offers no noticeable speed benefit. If you really want your `.pyc` files back, give this option.

-c STRING,--collection=STRING[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-c "Permalink to this definition")
Specify collection name to load.

-d,--debug[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-d "Permalink to this definition")
Enable debug output.

--dry[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-dry "Permalink to this definition")
Echo commands instead of actually running them; specifically, causes any `run` calls to:

*   Act as if the `echo` option has been turned on, printing the command-to-be-run to stdout;

*   Skip actual subprocess invocation (returning before any of that machinery starts running);

*   Return a dummy [`Result`](https://docs.pyinvoke.org/en/stable/api/runners.html#invoke.runners.Result "invoke.runners.Result") object with ‘blank’ values (empty stdout/err strings, `0` exit code, etc).

-D,--list-depth=INT[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-D "Permalink to this definition")
Limit [`--list`](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-l) display to the specified number of levels, e.g. `--list-depth 1` to show only top-level tasks and namespaces.

If an argument is given to `--list`, then this depth is relative; so `--list build --list-depth 1` shows everything at the top level of the `build` subtree.

Default behavior if this is not given is to show all levels of the entire task tree.

-e,--echo[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-e "Permalink to this definition")
Echo executed commands before running.

-f,--config[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-f "Permalink to this definition")
Specify a [runtime configuration file](https://docs.pyinvoke.org/en/stable/concepts/configuration.html#config-hierarchy) to load.

Note that you may instead use the `INVOKE_RUNTIME_CONFIG` environment variable in place of this option. If both are given, the CLI option will win out.

-F,--list-format=STRING[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-F "Permalink to this definition")
Change the format used to display the output of [`--list`](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-l); may be one of:

*   `flat` (the default): single, flat vertical list with dotted task names.

*   `nested`: a nested (4-space indented) vertical list, where each level implicitly includes its parent (with leading dots as a strong visual clue that these are still subcollection tasks.)

*   `json`: intended for consumption by scripts or other programs, this format emits JSON representing the task tree, with each ‘node’ in the tree (the outermost document being the root node, and thus a JSON object) consisting of the following keys:

    *   `name`: String name of collection; for the root collection this is typically the module name, so unless you’re supplying alternate collection name to the load process, it’s usually `"tasks"` (from `tasks.py`.)

    *   `help`: First line of collection’s docstring, if it came from a module; null otherwise (or if module lacked a docstring.)

    *   `tasks`: Immediate children of this collection; an array of objects of the following form:

        *   `name`: Task’s local name within its collection (i.e. not the full dotted path you might see with the `flat` format; reconstructing that path is left up to the consumer.)

        *   `help`: First line of task’s docstring, or null if it had none.

        *   `aliases`: An array of string aliases for this task.

    *   `default`: String naming which task within this collection, if any, is the default task. Is null if no task is the default.

    *   `collections`: An array of any sub-collections within this collection, members of which which will have the same structure as this outermost document, recursively.

The JSON emitted is not pretty-printed, but does end with a trailing newline.

-h STRING,--help=STRING[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-h "Permalink to this definition")
When given without any task names, displays core help; when given with a task name (may come before _or_ after the task name) displays help for that particular task.

-l,--list=STRING[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-l "Permalink to this definition")
List available tasks. Shows all tasks by default; may give an explicit namespace to ‘root’ the displayed task tree to only that namespace. (This argument may contain periods, as with task names, so it’s possible to show only a small, deep portion of the overall tree if desired.)

-p,--pty[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-p "Permalink to this definition")
Use a pty when executing shell commands.

-r STRING,--search-root=STRING[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-r "Permalink to this definition")
Change root directory used for finding task modules.

-T INT,--command-timeout=INT[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-T "Permalink to this definition")
Set a default command execution timeout of INT seconds. Maps to the `timeouts.command` config setting.

-V,--version[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-V "Permalink to this definition")
Show version and exit.

-w,--warn-only[¶](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-w "Permalink to this definition")
Warn, instead of failing, when shell commands fail.

Shell tab completion[¶](https://docs.pyinvoke.org/en/stable/invoke.html#shell-tab-completion "Permalink to this headline")
--------------------------------------------------------------------------------------------------------------------------

### Generating a completion script[¶](https://docs.pyinvoke.org/en/stable/invoke.html#generating-a-completion-script "Permalink to this headline")

Invoke’s philosophy is to implement generic APIs and then “bake in” a few common use cases built on top of those APIs; tab completion is no different. Generic tab completion functionality (outputting a shell-compatible list of completion tokens for a given command line context) is provided by the [`--complete`](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-complete) core CLI option described above.

However, you probably won’t need to use that flag yourself: we distribute a handful of ready-made wrapper scripts aimed at the most common shells like `bash` and `zsh` (plus others). These scripts can be automatically generated from Invoke or [any Invoke-driven command-line tool](https://docs.pyinvoke.org/en/stable/concepts/library.html#reusing-as-a-binary), using [`--print-completion-script`](https://docs.pyinvoke.org/en/stable/invoke.html#cmdoption-print-completion-script); the printed scripts will contain the correct binary name(s) for the program generating them.

For example, the following command prints (to stdout) a script which works for `zsh`, instructs `zsh` to use it for the `inv` and `invoke` programs, and calls `invoke --complete` at runtime to get dynamic completion information:

$ invoke --print-completion-script zsh

Note

You’ll probably want to source this command or store its output somewhere permanently; more on that in the next section.

Similarly, the [Fabric](https://fabfile.org/) tool inherits from Invoke, and only has a single binary name (`fab`); if you wanted to get Fabric completion in `bash`, you would say:

$ fab --print-completion-script bash

In the rest of this section, we’ll use `inv` in examples, but please remember to replace it with the program you’re actually using, if it’s not Invoke itself!

### Sourcing the script[¶](https://docs.pyinvoke.org/en/stable/invoke.html#sourcing-the-script "Permalink to this headline")

There are a few ways to utilize the output of the above commands, depending on your needs, where the program is installed, and your shell:

*   The simplest and least disruptive method is to `source` the printed completion script inline, which doesn’t place anything on disk, and will only affect the current shell session:

$ source <(inv --print-completion-script zsh) 
*   If you’ve got the program available in your system’s global Python interpreter (and you’re okay with running the program at the startup of each shell session - Python’s speed is admittedly not its strong point) you could add that snippet to your shell’s startup file, such as `~/.zshrc` or `~/.bashrc`.

*   If the program’s available globally but you’d prefer to _avoid_ running an extra Python program at shell startup, you can cache the output of the command in its own file; where this file lives is entirely up to you and how your shell is configured. For example, you might just drop it into your home directory as a hidden file:

$ inv --print-completion-script zsh > ~/.invoke-completion.sh 
and then perhaps add the following to the end of `~/.zshrc`:

source ~/.invoke-completion.sh 
But again, this is entirely up to you and your shell.

Note

If you’re using `fish`, you _must_ use this tactic, as our fish completion script is not suitable for direct sourcing. Fish shell users should direct the output of the command to a file in the `~/.config/fish/completions/` directory. 
*   Finally, if your copy of the needing-completion program is only installed in a specific environment like a virtualenv, you can use either of the above techniques:

> *   Caching the output and referencing it in a global shell startup file will still work in this case, as it does not require the program to be available when the shell loads – only when you actually attempt to tab complete.
> 
>     *   Using the `source <(inv --print-completion-script yourshell)` approach will work _as long as_ you place it in some appropriate per-environment startup file, which will vary depending on how you manage Python environments. For example, if you use `virtualenvwrapper`, you could append the `source` line in `/path/to/virtualenv/bin/postactivate`.

### Utilizing tab completion itself[¶](https://docs.pyinvoke.org/en/stable/invoke.html#utilizing-tab-completion-itself "Permalink to this headline")

You’ve ensured that the completion script is active in your environment - what have you gained?

*   By default, tabbing after typing `inv` or `invoke` will display task names from your current directory/project’s tasks file.

*   Tabbing after typing a dash (`-`) or double dash (`--`) will display valid options/flags for the current context: core Invoke options if no task names have been typed yet; options for the most recently typed task otherwise.

> *   Tabbing while typing a partial long option will complete matching long options, using your shell’s native substring completion. E.g. if no task names have been typed yet, `--e<tab>` will offer `--echo` as a completion option.

*   Hitting tab when the most recent typed/completed token is a flag which takes a value, will ‘fall through’ to your shell’s native filename completion.

> *   For example, prior to typing a task name, `--config <tab>` will complete local file paths to assist in filling in a config file.
