# Scripting Commands

## `method.*` commands

> method.insert

```ini

            method.redirect = ‹alias›, ‹target› ≫ 0

        Defines an alias for an existing command, the arguments are command names.
        Aliases cannot be changed, using the same alias name twice causes an error.

```

## `event.*` commands

rTorrent events are merely **ref:** `multi commands <multi-type>`
that are called automatically when certain things happen,
like completion of a download item.

You can trigger them manually by calling them on selected items (e.g. via `rtxmlrpc`).
Make sure though that the registered handlers do not have adverse effects when called repeatedly,
i.e. know what you're doing.

The handlers for an event can be listed like so:

```bash

    rtxmlrpc --repr method.get '' event.download.finished

```

Note that practically all the events have pre-registered system handlers,
often starting with a digit, `!`, or `~`, for ordering reasons.

> event.download.closed
> event.download.opened

Download item was closed / opened.

> event.download.paused
> event.download.resumed

Download item was paused / resumed.

> event.download.hash_done
> event.download.hash_failed
> event.download.hash_final_failed

### TODO (hash events)

> event.download.hash_queued
> event.download.hash_removed

### TODO (hash queued/removed)

> event.download.inserted
> event.download.inserted_new
> event.download.inserted_session

`inserted` is *always* called when an item is added to the main downloads list.
After that, `inserted_session` is called when the source of that item is the session state (on startup),
or else `inserted_new` is called for items newly added via a `load` command.

> event.download.finished

Download item is complete.

> event.download.erased

Download item was removed.

See also **term:** `d.erase`.

> event.view.hide
> event.view.show

```ini

            method.set_key = event.view.hide, ~log,\
                ((print, "× ", ((ui.current_view)), " → ", ((argument.0))))'
            method.set_key = event.view.show, ~log,\
                ((print, "⊞ ", ((argument.0)), " → ", ((ui.current_view))))'

```

## Scheduling Commands

The scheduling commands define tasks that call another command or list of commands repeatedly,
just like a cron job, but with a resolution of seconds.

> schedule2

```shell

            rtcontrol -qorealpath d_hashing_failed=1 \
            | xargs --no-run-if-empty -d$'\n' df -h \
            | sort -ru

        See also :term:`d.free_diskspace`.

```

## Importing Script Files

> import
> try_import

```ini

            branch=(not, (system.has, "math.add=")), ((import.return))

        You can do this incrementally ordered from older to younger capabilities,
        using exactly those features a build has to offer.

```

## Conditions (if/branch/do)

> branch
> if

```ini

            branch = (system.has, "do="), \
                ((do, \
                    ((print, "Just")), \
                    ((print, "DO")), \
                    ((print, "it!")) \
                )), \
                ((print, "Awwwwww!"))

            :language: console
            :start-after: # do
            :end-before: # END

```

## Conditional Operators

> false

Ignores any amount of arguments, and always returns `0`.

> and
> or
> not

### TODO (conditional operators)

> less
> equal
> greater

```ini

            view.add = messages
            view.filter = messages, ((d.message))
            view.sort_new = messages, "compare=,d.message=,d.name="

```

## String Functions

> cat

```console

            $ rtxmlrpc string.map '' 'foo' [foo,bar [bar,baz
            baz

            $ rtxmlrpc string.replace '' "it's like 1" [1,2ic [2,ma3 [3,g
            it's like magic

            $ rtxmlrpc -i 'print = (string.map, (cat, (value,1)), {0,off}, {1,low}, {2,""}, {3,high})'
            # prints 'low' as a console message, this is how you map integers

```

## Array Functions

> array.at

```ini

            array.at = «array», «pos» ≫ object (element)

        ### TODO

            :language: console
            :start-at: # array.at
            :end-before: # END

```

## Math Functions

Most of these commands are available in `rTorrent-PS` 1.1+, in `rTorrent-PS-CH`,
and `rTorrent` 0.9.7+. Deviations are explicitly noted.

Values can either be of type *value* or *string* –
strings are automatically converted,
with an error thrown when the string contains something other than digits.

The handled values are restricted to integer arithmetic (as in `bash`),
because `rTorrent` has no floating point type.
Division, average, and median always round down.

All commands support multiple arguments, including lists.
List arguments are handled recursively,
as-if there were a nested `math.*` call of the same type,
with the list as its arguments.

When using multiple list arguments, or mixing them with plain numbers,
this can lead to unexpected results with non-commutative operators,
see the `math.sub` examples below.

> math.add
> math.sub
> math.mul
> math.div
> math.mod

Basic arithmetic operators (+, -, *, /, %).

These share the same code, so the errors shown in the following examples
usually apply to all commands, and are not repeated for each operator.

> **language:** console
> **start-at:** # math.add
> **end-before:** # END
>
> **language:** console
> **start-at:** # math.sub
> **end-before:** # END
>
> **language:** console
> **start-at:** # math.mul
> **end-before:** # END
>
> **language:** console
> **start-at:** # math.div
> **end-before:** # END
>
> **language:** console
> **start-at:** # math.mod
> **end-before:** # END
>
> math.min
> math.max
> math.cnt
> math.avg
> math.med

Functions to calculate the minimum, maximum, element count, average, or median over the input values.

> **language:** console
> **start-at:** # math.min
> **end-before:** # END
>
> **language:** console
> **start-at:** # math.max
> **end-before:** # END
>
> **language:** console
> **start-at:** # math.cnt
> **end-before:** # END
>
> **language:** console
> **start-at:** # math.avg
> **end-before:** # END
>
> **language:** console
> **start-at:** # math.med
> **end-before:** # END

## Value Conversion & Formatting

The `to_*` forms are **deprecated**.

> convert.kb
> convert.mb
> convert.xb
> to_kb
> to_mb
> to_xb

### TODO (value conversion)

> convert.date
> convert.elapsed_time
> convert.gm_date
> convert.gm_time
> convert.time
> to_date
> to_elapsed_time
> to_gm_date
> to_gm_time
> to_time

### TODO (date conversion)

> convert.throttle
> to_throttle

### TODO (throttle conversion)

> convert.time_delta

```shell

            $ rtxmlrpc -qi 'view.filter = rtcontrol, "equal = d.priority=, value=3"'
            # the 'rtcontrol' view will now show all items with priority 'high'
            $ rtxmlrpc --repr value '' 1b 16
            27
            $ rtxmlrpc --repr value '' 1b
            ERROR    While calling value('', '1b'): <Fault -503: 'Junk at end of number: 1b'>

```
