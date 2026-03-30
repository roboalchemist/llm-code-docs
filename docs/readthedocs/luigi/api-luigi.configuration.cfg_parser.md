# luigi.configuration.cfg_parser

luigi.configuration provides some convenience wrappers around Python’s
ConfigParser to get configuration options from config files.

The default location for configuration files is luigi.cfg (or client.cfg) in the current
working directory, then /etc/luigi/client.cfg.

Configuration has largely been superseded by parameters since they can
do essentially everything configuration can do, plus a tighter integration
with the rest of Luigi.

See Configuration for more info.

Classes

`CombinedInterpolation`(interpolations)

Custom interpolation which applies multiple interpolations in series.

`EnvironmentInterpolation`()

Custom interpolation which allows values to refer to environment variables using the `${ENVVAR}` syntax.

`LuigiConfigParser`([defaults, dict_type, ...])

Exceptions

`InterpolationMissingEnvvarError`(option, ...)

Raised when option value refers to a nonexisting environment variable.

exception luigi.configuration.cfg_parser.InterpolationMissingEnvvarError(*option*, *section*, *value*, *envvar*)

Raised when option value refers to a nonexisting environment variable.

class luigi.configuration.cfg_parser.EnvironmentInterpolation

Custom interpolation which allows values to refer to environment variables
using the `${ENVVAR}` syntax.

before_get(*parser*, *section*, *option*, *value*, *defaults*)

class luigi.configuration.cfg_parser.CombinedInterpolation(*interpolations*)

Custom interpolation which applies multiple interpolations in series.

Parameters:

**interpolations** – a sequence of configparser.Interpolation objects.

before_get(*parser*, *section*, *option*, *value*, *defaults*)

before_read(*parser*, *section*, *option*, *value*)

before_set(*parser*, *section*, *option*, *value*)

before_write(*parser*, *section*, *option*, *value*)

class luigi.configuration.cfg_parser.LuigiConfigParser(*defaults=None*, *dict_type=<class 'dict'>*, *allow_no_value=False*, ***, *delimiters=('='*, *': ')*, *comment_prefixes=('#'*, *';')*, *inline_comment_prefixes=None*, *strict=True*, *empty_lines_in_values=True*, *default_section='DEFAULT'*, *interpolation=<object object>*, *converters=<object object>*, *allow_unnamed_section=False*)

NO_DEFAULT = <object object>

enabled = True

optionxform

alias of `str`

classmethod reload()

has_option(*section*, *option*)

modified has_option
Check for the existence of a given option in a given section. If the
specified ‘section’ is None or an empty string, DEFAULT is assumed. If
the specified ‘section’ does not exist, returns False.

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