# Source: https://rebar3.org/docs/testing/eunit/

Title: EUnit

URL Source: https://rebar3.org/docs/testing/eunit/

Markdown Content:
To run all EUnit test suites:

```
$ rebar3 eunit
```

Console

Rebar3 will compile all project modules with the macros `{d, TEST, true}` and `{d, EUNIT, true}` defined so you can safely hide your test code within `-ifdef(TEST).` or `-ifdef(EUNIT).` sections. It will also automatically compile any source files in your application’s `test` directory, if present. By default, Rebar3 runs tests by calling `eunit:test([{application, App}])` for each application in your project.

The `eunit` command runs as the `test` profile, by default. See [Profiles](https://rebar3.org/docs/configuration/profiles) for details.

For available options and their usage see [Commands](https://rebar3.org/docs/commands) or:

```
$ rebar3 help eunit
```

Console

Test Selection
--------------

The following flags can be provided standalone or combined.

### Apps

To run tests for specific apps only:

```
$ rebar3 eunit --application=app1,app2
```

Console

The format is a comma separated list of application names.

Alias: `--app`.

### Modules

To run tests for specific modules only:

```
$ rebar3 eunit --module=mod1,mod2,mod3
```

Console

The format is a comma separated list of module names.

Alias: `--suite`.

### Test Cases

To run specific test cases only:

```
$ rebar3 eunit --test=mod1:test1+test2,mod2:test1
```

Console

The format is a [comma separated list of test functions](https://rebar3.org/docs/testing/eunit/#test-function-format).

### Generators

To run specific test case generators only:

```
$ rebar3 eunit --generator=mod1:gen1+gen2,mod2:gen1
```

Console

The format is a [comma separated list of test functions](https://rebar3.org/docs/testing/eunit/#test-function-format).

### Files

To run tests for specific files only:

```
$ rebar3 eunit --file="test/mod1.erl,test/mod2.erl"
```

Console

The format is a comma separated list of file paths.

### Directories

To run tests for specific directories only:

```
$ rebar3 eunit --dir="test,extra_tests"
```

Console

The format is a comma separated list of directory paths.

Test Function Format
--------------------

The format to select specific test functions is a comma separated list of `Module:Func` specifications. Multiple functions in the same module can be selected by separating them with a plus `+` sign, e.g. `Module:Func1+Func2` (alternatively they can be separated with a semicolon `;`).

Configuration Options
---------------------

The following configuration options can be set in `rebar.config`.

### `eunit_tests`

You can change the default tests `eunit:test/1` is called with when running `rebar3 eunit` (instead of the default which are all tests in all applications).

The configuration must be a list with EUnit test representations, as documented [here](https://www.erlang.org/doc/apps/eunit/chapter.html#EUnit_test_representation). Rebar3 will do its best to ensure any modules specified in tests are compiled and made available on the code path.

Examples:

```
{eunit_tests, [{module, smoke_tests}]}.
```

Erlang

```
{eunit_tests, [{inparallel, mod1}]}.
```

Erlang

### `eunit_opts`

The default EUnit options can be configured, as documented [here](https://www.erlang.org/doc/man/eunit.html#test-2).

Interesting undocumented options are:

*   `no_tty` completely disables the default EUnit reporter output

*   `{report, {Module, Args}}` runs a custom EUnit reporter (the functionality that prints results to the shell). The reporter module needs the following callbacks implemented:

```
-export([start/0]).
-export([start/1]).
-export([init/1]).
-export([handle_begin/3]).
-export([handle_end/3]).
-export([handle_cancel/3]).
-export([terminate/2]).
```
Erlang  

`no_tty` and `report` can be combined to replace the EUnit reporter with a custom one:

```
{eunit_opts, [no_tty, {report, {my_reporter, Opts}}]}.
```

Erlang

Last modified January 9, 2023: [Fix broken link (da4612d)](https://github.com/tsloughter/rebar3.org/commit/da4612dd0f1f0fee737b205b6e2392bdd08c55ab)
