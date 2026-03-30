# Python Prompt Toolkit 3.0

prompt_toolkit is a library for building powerful interactive command line
and terminal applications in Python.

It can be a very advanced pure Python replacement for GNU readline [https://tiswww.case.edu/php/chet/readline/rltop.html], but it can also be
used for building full screen applications.

Some features:

-

Syntax highlighting of the input while typing. (For instance, with a Pygments lexer.)

-

Multi-line input editing.

-

Advanced code completion.

-

Selecting text for copy/paste. (Both Emacs and Vi style.)

-

Mouse support for cursor positioning and scrolling.

-

Auto suggestions. (Like fish shell [http://fishshell.com/].)

-

No global state.

Like readline:

-

Both Emacs and Vi key bindings.

-

Reverse and forward incremental search.

-

Works well with Unicode double width characters. (Chinese input.)

Works everywhere:

-

Pure Python. Runs on all Python versions starting at Python 3.6.
(Python 2.6 - 3.x is supported in prompt_toolkit 2.0; not 3.0).

-

Runs on Linux, OS X, OpenBSD and Windows systems.

-

Lightweight, the only dependencies are Pygments and wcwidth.

-

No assumptions about I/O are made. Every prompt_toolkit application should
also run in a telnet/ssh server or an asyncio [https://docs.python.org/3/library/asyncio.html] process.

Have a look at the gallery to get an idea of what is possible.

## Getting started

Go to getting started and build your first prompt.
Issues are tracked on the Github project [https://github.com/prompt-toolkit/python-prompt-toolkit].

## Thanks to

A special thanks to all the contributors [https://github.com/prompt-toolkit/python-prompt-toolkit/graphs/contributors]
for making prompt_toolkit possible.

Also, a special thanks to the Pygments [http://pygments.org/] and wcwidth [https://github.com/jquast/wcwidth] libraries.

## Table of contents

- Gallery

  - Ptpython, a Python REPL

  - Pyvim, a Vim clone

  - Pymux, a terminal multiplexer (like tmux) in Python

- Getting started

  - Installation

  - Several use cases: prompts versus full screen terminal applications

  - A simple prompt

  - Learning prompt_toolkit

- Upgrading

  - Upgrading to prompt_toolkit 2.0

  - Upgrading to prompt_toolkit 3.0

- Printing (and using) formatted text

  - Printing plain text

  - Formatted text

- Asking for input (prompts)

  - Hello world

  - The PromptSession object

  - Syntax highlighting

  - Colors

  - Autocompletion

  - Input validation

  - History

  - Auto suggestion

  - Adding a bottom toolbar

  - Adding a right prompt

  - Vi input mode

  - Adding custom key bindings

  - Other prompt options

  - Cursor shapes

  - Adding a frame

  - Prompt in an asyncio application

  - Reading keys from stdin, one key at a time, but without a prompt

- Asking for a choice

  - Coloring the options

  - Adding a frame

  - Adding a bottom toolbar

- Dialogs

  - Message box

  - Input box

  - Yes/No confirmation dialog

  - Button dialog

  - Radio list dialog

  - Checkbox list dialog

  - Styling of dialogs

  - Styling reference sheet

- Progress bars

  - Simple progress bar

  - Multiple parallel tasks

  - Adding a title and label

  - Formatting the progress bar

  - Adding key bindings and toolbar

- Building full screen applications

  - A simple application

  - I/O objects

  - The layout

  - Key bindings

  - More about the Window class

  - More about buffers and BufferControl

- Tutorials

  - Tutorial: Build an SQLite REPL

- Advanced topics

  - More about key bindings

  - More about styling

  - Filters

  - The rendering flow

  - Running on top of the asyncio event loop

  - Unit testing

  - Input hooks

  - Architecture

  - The rendering pipeline

- Reference

  - Application

  - Formatted text

  - Buffer

  - Selection

  - Clipboard

  - Auto completion

  - Document

  - Enums

  - History

  - Keys

  - Style

  - Shortcuts

  - Validation

  - Auto suggestion

  - Renderer

  - Lexers

  - Layout

  - Widgets

  - Filters

  - Key binding

  - Eventloop

  - Input

  - Output

  - Data structures

  - Patch stdout

- Related projects
