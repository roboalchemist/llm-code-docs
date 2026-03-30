# luigi.cmdline_parser

This module contains luigi internal parsing logic. Things exposed here should
be considered internal to luigi.

Classes

`CmdlineParser`(cmdline_args)

Helper for parsing command line arguments and used as part of the context when instantiating task objects.

class luigi.cmdline_parser.CmdlineParser(*cmdline_args*)

Helper for parsing command line arguments and used as part of the
context when instantiating task objects.

Normal luigi users should just use `luigi.run()`.

Initialize cmd line args

classmethod get_instance()

Singleton getter

classmethod global_instance(*cmdline_args*, *allow_override=False*)

Meant to be used as a context manager.

get_task_obj()

Get the task object