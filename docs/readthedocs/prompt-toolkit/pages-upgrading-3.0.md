# Upgrading to prompt_toolkit 3.0

There are two major changes in 3.0 to be aware of:

- 

First, prompt_toolkit uses the asyncio event loop natively, rather then using
its own implementations of event loops. This means that all coroutines are
now asyncio coroutines, and all Futures are asyncio futures. Asynchronous
generators became real asynchronous generators as well.

- 

Prompt_toolkit uses type annotations (almost) everywhere. This should not
break any code, but its very helpful in many ways.

There are some minor breaking changes:

- 

The dialogs API had to change (see below).

## Detecting the prompt_toolkit version

Detecting whether version 3 is being used can be done as follows:

```
from prompt_toolkit import __version__ as ptk_version

PTK3 = ptk_version.startswith('3.')

```