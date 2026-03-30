
`dht.*` commands
^^^^^^^^^^^^^^^^

See the Github wiki for an example of `enabling DHT in rTorrent`_.


> dht.add_node

```ini

            dht.port ≫ value ‹port›
            dht.mode.set = value ‹port› ≫ 0
            dht_port = value ‹port› ≫ 0

        Controls which port DHT will listen on. Note that ``dht_port`` is an alias for ``dht.port.set``,
        not ``dht.port``.

    dht.statistics

        Returns ``{'active': 0, 'dht': 'disable', 'throttle': ''}`` when DHT is off,
        and …

        **TODO**

    dht.throttle.name
    dht.throttle.name.set

        **TODO**



```

`pieces.*` commands
^^^^^^^^^^^^^^^^^^^


> pieces.hash.on_completion
> pieces.hash.on_completion.set

```ini

            pieces.sync.timeout_safe ≫ value ‹seconds›
            pieces.sync.timeout_safe.set = value ‹seconds› ≫ 0

        **TODO** This does not appear to be in use.



```

`protocol.*` commands
^^^^^^^^^^^^^^^^^^^^^


> protocol.choke_heuristics.down.leech
> protocol.choke_heuristics.down.leech.set
> protocol.choke_heuristics.down.seed
> protocol.choke_heuristics.down.seed.set
> protocol.choke_heuristics.up.leech
> protocol.choke_heuristics.up.leech.set
> protocol.choke_heuristics.up.seed
> protocol.choke_heuristics.up.seed.set

> **TODO**

> protocol.connection.leech
> protocol.connection.leech.set
> protocol.connection.seed
> protocol.connection.seed.set

> **TODO**

> protocol.encryption.set

```ini

            protocol.pex ≫ bool (0 or 1)
            protocol.pex.set = bool (0 or 1) ≫ 0

        Controls whether `peer exchange`_ is enabled.





```

`throttle.*` commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

Throttles are names for bandwidth limitation rules (for upload, download, or both).
The throttle assigned to the item in focus can be changed using `Ctrl-T`
– it will rotate through all defined ones.

There are two system throttles, `NULL` and the one with an empty name.
`NULL` is a special throttle for *unlimited*, and the latter is the *global* throttle,
which is the default for new items and what's shown in the status bar on the left
as `[Throttle ‹UP›/‹DOWN› KB]`.

**TODO** Explain how throttles work, borrowing from the global throttle.

Other commands in this group determine the limits for upload / download slots,
and the amount of peers requested in tracker announces.


> Note that since named throttles *borrow* from the global throttle,
> the global one has to be set to a non-zero value for the named ones to work
> (because borrowing from ∞ means there is no limit).



> throttle.down
> throttle.up

```

            $ rtxmlrpc --repr throttle.names
            ['', 'NULL', 'kb500', 'lo_up', 'onemb']

```