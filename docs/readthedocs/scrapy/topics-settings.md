# Settings

The Scrapy settings allows you to customize the behaviour of all Scrapy
components, including the core, extensions, pipelines and spiders themselves.

The infrastructure of the settings provides a global namespace of key-value mappings
that the code can use to pull configuration values from. The settings can be
populated through different mechanisms, which are described below.

The settings are also the mechanism for selecting the currently active Scrapy
project (in case you have many).

For a list of available built-in settings see: Built-in settings reference.

## Designating the settings

When you use Scrapy, you have to tell it which settings you’re using. You can
do this by using an environment variable, `SCRAPY_SETTINGS_MODULE`.

The value of `SCRAPY_SETTINGS_MODULE` should be in Python path syntax, e.g.
`myproject.settings`. Note that the settings module should be on the
Python import search path [https://docs.python.org/3/tutorial/modules.html#tut-searchpath].

## Populating the settings

Settings can be populated using different mechanisms, each of which has a
different precedence:

- 

Command-line settings (highest precedence)

- 

Spider settings

- 

Project settings

- 

Add-on settings

- 

Command-specific default settings

- 

Global default settings (lowest precedence)