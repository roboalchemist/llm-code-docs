# Command line tool

Scrapy is controlled through the `scrapy` command-line tool, to be referred to
here as the “Scrapy tool” to differentiate it from the sub-commands, which we
just call “commands” or “Scrapy commands”.

The Scrapy tool provides several commands, for multiple purposes, and each one
accepts a different set of arguments and options.

(The `scrapy deploy` command has been removed in 1.0 in favor of the
standalone `scrapyd-deploy`. See Deploying your project [https://scrapyd.readthedocs.io/en/latest/deploy.html].)

## Configuration settings

Scrapy will look for configuration parameters in ini-style `scrapy.cfg` files
in standard locations:

- 

`/etc/scrapy.cfg` or `c:\scrapy\scrapy.cfg` (system-wide),

- 

`~/.config/scrapy.cfg` (`$XDG_CONFIG_HOME`) and `~/.scrapy.cfg` (`$HOME`)
for global (user-wide) settings, and

- 

`scrapy.cfg` inside a Scrapy project’s root (see next section).

Settings from these files are merged in the listed order of preference:
user-defined values have higher priority than system-wide defaults
and project-wide settings will override all others, when defined.

Scrapy also understands, and can be configured through, a number of environment
variables. Currently these are:

- 

`SCRAPY_SETTINGS_MODULE` (see Designating the settings)

- 

`SCRAPY_PROJECT` (see Sharing the root directory between projects)

- 

`SCRAPY_PYTHON_SHELL` (see Scrapy shell)

## Default structure of Scrapy projects

Before delving into the command-line tool and its sub-commands, let’s first
understand the directory structure of a Scrapy project.

Though it can be modified, all Scrapy projects have the same file
structure by default, similar to this:

```
scrapy.cfg
myproject/
    __init__.py
    items.py
    middlewares.py
    pipelines.py
    settings.py
    spiders/
        __init__.py
        spider1.py
        spider2.py
        ...

```