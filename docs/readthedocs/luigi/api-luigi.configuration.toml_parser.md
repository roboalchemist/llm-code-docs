# luigi.configuration.toml_parser

Classes

`LuigiTomlParser`([defaults, dict_type, ...])

class luigi.configuration.toml_parser.LuigiTomlParser(*defaults=None*, *dict_type=<class 'dict'>*, *allow_no_value=False*, ***, *delimiters=('='*, *': ')*, *comment_prefixes=('#'*, *';')*, *inline_comment_prefixes=None*, *strict=True*, *empty_lines_in_values=True*, *default_section='DEFAULT'*, *interpolation=<object object>*, *converters=<object object>*, *allow_unnamed_section=False*)

NO_DEFAULT = <object object>

enabled = True

data: Dict[str, Any] = {}

read(*config_paths*)

Read and parse a filename or an iterable of filenames.

Files that cannot be opened are silently ignored; this is
designed so that you can specify an iterable of potential
configuration file locations (e.g. current directory, user’s
home directory, systemwide directory), and all existing
configuration files in the iterable will be read.  A single
filename may also be given.

Return list of successfully read files.

get(*section*, *option*, *default=<object object>*, ***kwargs*)

Get an option value for a given section.

If vars is provided, it must be a dictionary. The option is looked up
in vars (if provided), section, and in DEFAULTSECT in that order.
If the key is not found and fallback is provided, it is used as
a fallback value. None can be provided as a fallback value.

If interpolation is enabled and the optional argument raw is False,
all interpolations are expanded in the return values.

Arguments raw, vars, and fallback are keyword only.

The section DEFAULT is special.

getboolean(*section*, *option*, *default=<object object>*)

getint(*section*, *option*, *default=<object object>*)

getfloat(*section*, *option*, *default=<object object>*)

getintdict(*section*)

set(*section*, *option*, *value=None*)

Set an option.  Extends RawConfigParser.set by validating type and
interpolation syntax on the value.

has_option(*section*, *option*)

Check for the existence of a given option in a given section.
If the specified section is None or an empty string, DEFAULT is
assumed. If the specified section does not exist, returns False.