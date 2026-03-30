# Source: https://boltons.readthedocs.io/en/latest/mboxutils.html

Title: Unix mailbox utilities — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/mboxutils.html

Markdown Content:
`mboxutils` - Unix mailbox utilities[](https://boltons.readthedocs.io/en/latest/mboxutils.html#module-boltons.mboxutils "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

Useful utilities for working with the [mbox](https://en.wikipedia.org/wiki/Mbox)-formatted mailboxes. Credit to Mark Williams for these.

_class_ boltons.mboxutils.mbox_readonlydir(_path_, _factory=None_, _create=True_, _maxmem=1048576_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mboxutils.html#mbox_readonlydir)[](https://boltons.readthedocs.io/en/latest/mboxutils.html#boltons.mboxutils.mbox_readonlydir "Link to this definition")
A subclass of [`mailbox.mbox`](https://docs.python.org/3/library/mailbox.html#mailbox.mbox "(in Python v3.14)") suitable for use with mboxs insides a read-only mail directory, e.g., `/var/mail`. Otherwise the API is exactly the same as the built-in mbox.

Deletes messages via truncation, in the manner of [Heirloom mailx](http://heirloom.sourceforge.net/mailx.html).

Parameters:
*   **path** ([_str_](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – Path to the mbox file.

*   **factory** ([_type_](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")) – Message type (defaults to `rfc822.Message`)

*   **create** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Create mailbox if it does not exist. (defaults to `True`)

*   **maxmem** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Specifies, in bytes, the largest sized mailbox to attempt to copy into memory. Larger mailboxes will be copied incrementally which is more hazardous. (defaults to 4MB)

Note

Because this truncates and rewrites parts of the mbox file, this class can corrupt your mailbox. Only use this if you know the built-in [`mailbox.mbox`](https://docs.python.org/3/library/mailbox.html#mailbox.mbox "(in Python v3.14)") does not work for your use case.

flush()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mboxutils.html#mbox_readonlydir.flush)[](https://boltons.readthedocs.io/en/latest/mboxutils.html#boltons.mboxutils.mbox_readonlydir.flush "Link to this definition")
Write any pending changes to disk. This is called on mailbox close and is usually not called explicitly.

Note

This deletes messages via truncation. Interruptions may corrupt your mailbox.
