
`d.*` commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

See the hint at the start of this chapter regarding the (sometimes implicit) *target* argument.


> d.multicall2
> d.multicall.filtered
> download_list


```ini

            d.tracker_scrape.downloaded = ‹target› ≫ value ‹amount›
            d.tracker_scrape.complete = ‹target› ≫ value ‹amount›
            d.tracker_scrape.incomplete = ‹target› ≫ value ‹amount›

        Returns the number of downloads, complete peers and incomplete peers from scrapes to the
        active trackers, respectively. See :term:`t.scrape_downloaded` for the respective tracker methods.







```

`f.*` commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

These commands can be used as arguments in a **term:** `f.multicall`.
They can also be called directly, but you need to pass `‹infohash›:f‹index›` as the first argument.
Index counting starts at `0`, the array size is **term:** `d.size_files`.


```ini

            f.size_bytes = ‹infohash› ≫ value ‹bytes›
            f.size_chunks = ‹infohash› ≫ value ‹chunks›

        Returns the number of bytes and chunks in the file respectively. If the file is only partially in some chunks,
        those are included in the count. This means the sum of all ``f.size_chunks`` can be
        larger than :term:`d.size_chunks`.



```

`p.*` commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

These commands can be used as arguments in a **term:** `p.multicall`.
They can also be called directly, but you need to pass `‹infohash›:p‹peerhash›` as the first argument
(referenced as `target` from here on out). The `‹peerhash›` is the ID as returned by
**term:** `p.id`, which is encoded as a hexadecimal string.



```ini

            p.up_rate = ‹target› ≫ value ‹rate [bytes/s]›
            p.up_total = ‹target› ≫ value ‹total [bytes]›

        Returns the rate and total of the bytes you are uploading to the peer.



```

`t.*` commands
^^^^^^^^^^^^^^^^^^^^^^^^^^

These commands can be used as arguments in a **term:** `t.multicall`.
They can also be called directly, but you need to pass `‹infohash›:t‹index›` as the first argument.
Index counting starts at `0`, the array size is **term:** `d.tracker_size`.


```ini

            t.url = ‹target› ≫ string ‹url›

        Returns the full URL of the tracker.




```

`load.*` commands
^^^^^^^^^^^^^^^^^

The client may be configured to check a directory for new metafiles and load them.
Items loaded in this manner will be tied to the metafile's path (see **term:** `d.tied_to_file`).

This means when the metafile is deleted, the item may be stopped (see **term:** `stop_untied`),
and when the item is removed the metafile is also.
Note that you can untie an item by using the `U` key (which will also delete the tied file),
and using `Ctrl-K` also implicitly unties an item.


> load.normal
> load.verbose
> load.start
> load.start_verbose

```console

            $ mktor -q README.md local
            $ rtxmlrpc --debug load.raw_verbose '' @README.md.torrent | egrep 'xmlrpclib|stats'
            DEBUG    load.raw_verbose('', <xmlrpclib.Binary instance at 0x15e1200>) took 0.000 secs
            DEBUG    XMLRPC stats: 3 req, out 795 bytes [564 bytes max], in 445 bytes [153 bytes max], …
            $ rtxmlrpc d.multicall.filtered '' 'string.contains=$d.name=,README' \
                       d.name= d.tied_to_file= d.loaded_file=
            ['README.md', '', '']



```

`session.*` commands
^^^^^^^^^^^^^^^^^^^^


> session.name
> session.name.set

```

            session.use_lock ≫ bool (0 or 1)
            session.use_lock.set = bool (0 or 1) ≫ 0

        By default, a lockfile is created in the session directory to prevent multiple instances of
        *rTorrent* from using the same session simultaneously.


```