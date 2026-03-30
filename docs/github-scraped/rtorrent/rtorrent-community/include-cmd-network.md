
`network.*` commands
^^^^^^^^^^^^^^^^^^^^


> network.bind_address
> network.bind_address.set

> **TODO**

> network.http.dns_cache_timeout
> network.http.dns_cache_timeout.set

```ini

            # rTorrent-PS 0.*+ only!

            # Show traffic of the last hour (112*32 = 3584 ≈ 3600)
            network.history.depth.set = 112

            method.insert = network.history.auto_scale.toggle, simple|private,\
                "branch=(network.history.auto_scale),\
                    ((network.history.auto_scale.set, 0)),\
                    ((network.history.auto_scale.set, 1))"
            method.insert = network.history.auto_scale.ui_toggle, simple|private,\
                "network.history.auto_scale.toggle= ; network.history.refresh="

            schedule2 = network_history_sampling, 1, 32, "network.history.sample="
            schedule2 = bind_auto_scale, 0, 0,\
                "ui.bind_key=download_list, =, network.history.auto_scale.ui_toggle="

        This will add the graph above the footer,
        you get the upper and lower bounds of traffic
        within your configured time window, and each bar of the graph
        represents an interval determined by the sampling schedule.

        Pressing ``=`` toggles between a graph display with base line 0,
        and a zoomed view that scales it to the current bounds.


```

`ip_tables.*` commands
^^^^^^^^^^^^^^^^^^^^^^^^^^


> ip_tables.add_address
> ip_tables.get
> ip_tables.insert_table
> ip_tables.size_data

> **TODO**


`ipv4_filter.*` commands
^^^^^^^^^^^^^^^^^^^^^^^^^^


> ipv4_filter.add_address
> ipv4_filter.dump
> ipv4_filter.get
> ipv4_filter.load
> ipv4_filter.size_data

> **TODO**
