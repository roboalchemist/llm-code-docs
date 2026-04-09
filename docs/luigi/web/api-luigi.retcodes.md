# luigi.retcodes

Module containing the logic for exit codes for the luigi binary. It’s useful
when you in a programmatic way need to know if luigi actually finished the
given task, and if not why.

Functions

`run_with_retcodes`(argv)

Run luigi with command line parsing, but raise `SystemExit` with the configured exit code.

Classes

`retcode`(*args, **kwargs)

See the return codes configuration section.

class luigi.retcodes.retcode(**args*, ***kwargs*)

See the return codes configuration section.

unhandled_exception

Parameter whose value is an `int`.

missing_data

Parameter whose value is an `int`.

task_failed

Parameter whose value is an `int`.

already_running

Parameter whose value is an `int`.

scheduling_error

Parameter whose value is an `int`.

not_run

Parameter whose value is an `int`.

luigi.retcodes.run_with_retcodes(*argv*)

Run luigi with command line parsing, but raise `SystemExit` with the configured exit code.

Note: Usually you use the luigi binary directly and don’t call this function yourself.

Parameters:

**argv** – Should (conceptually) be `sys.argv[1:]`