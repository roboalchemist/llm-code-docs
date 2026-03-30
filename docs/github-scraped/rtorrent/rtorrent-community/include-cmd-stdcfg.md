The following sections explain some major commands added by well-known configuration sets.

If you want other setups (`rtinst`, `QuickBox`, …) to be documented, we accept pull requests.


Examples in This Manual
^^^^^^^^^^^^^^^^^^^^^^^

These commands are from snippets presented in other chapters.


> cfg.drop_in

> The directory to import snippets from, see **ref:** `drop-in-config`. This is a *private* command.

> event.download.finished_delayed
> event.download.finished_delayed.interval
> event.download.finished_delayed.interval.set

> Events for delayed completion processing,
> see **ref:** `event.download.finished_delayed` for a full explanation.


`rTorrent` Wiki Template
^^^^^^^^^^^^^^^^^^^^^^^^

The `CONFIG Template`_ wiki page defines a few commands in its configuration snippet.
See **ref:** `config-deconstructed` for a detailed tour.



> cfg.basedir
> cfg.watch
> cfg.logs

> These define important base paths in the file system layout of a `rTorrent` instance,
> and are all private. They are used where appropriate to define further paths
> like the session directory, and allow easy changes at just one place.

> By default, `cfg.watch` and `cfg.logs` are sub-dirs of `cfg.basedir`.


> system.startup_time

> A constant value that holds the **term:** `system.time` when the client was started.


> d.data_path

> Return path to an item's data – this is never empty, unlike **term:** `d.base_path`.
> Multi-file items return a path ending with a `/`.


```ini

            method.insert = d.data_path, simple,\
                "if=(d.is_multi_file),\
                    (cat, (d.directory), /),\
                    (cat, (d.directory), /, (d.name))"





```

`pyrocore` Configuration
^^^^^^^^^^^^^^^^^^^^^^^^

In addition to the commands listed here, `pyrocore` also defines **term:** `d.data_path`.



> startup_time

> The **term:** `system.time` the client was started at.
> Used in the message shown by `rTorrent-PS` when pressing `u`,
> and for similar purposes throughout `rtcontrol`.

> This is an alias for **term:** `system.startup_time`.


> d.session_file

> Return path to an items's session file.


```ini

            pyro.view.toggle_visible = ‹view name› ≫ 0

        Toggle visibility of an item for the given view.


    pyro.color_theme.name

        Used in color theme files of `rTorrent-PS` to announce switching to a different theme
        (defined in `pyrocore`'s `rtorrent.d/theming.rc`_).


    pyro.watchdog

        **TODO**

        This is a *private* command.





```

`pimp-my-box` Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

**TODO**

In addition to the commands listed here, `pimp-my-box` also defines
**term:** `cfg.basedir`, :term:`cfg.watch`, and :term:`cfg.logs`,
and includes anything from **ref:** `pyrocore-cfg`.



> quit

> **TODO** `disable-control-q.rc`


> pyro.extended

> Set `pyro.extended` to `1` to activate `rTorrent-PS` features.
> Note that this *tells* the rest of the configuration that it can
> safely use the extended command set – it *won't* magically make a
> vanilla `rTorrent` an extended one.

> Starting with `rTorrent-PS 1.1+`, this setting is detected automatically,
> thanks to **term:** `system.has`.


> pyro.bin_dir

> A constant that should be set to the `bin` directory
> where you installed the `pyrocore` tools.

> Make sure you end it with a `/`;
> if this is left empty, then the shell's path is searched.


> pyro.logfile_path

> **TODO**