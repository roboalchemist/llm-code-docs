# Source: https://docs.searxng.org/admin/plugins.html

[]

# List of plugins[¶](#list-of-plugins "Link to this heading")

Further reading ..

-   [[SearXNG settings]](settings/settings_plugins.html#settings-plugins)

-   [[Plugin Development]](../dev/plugins/development.html#dev-plugin)

[]

+-------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Name                    | Active | Description                                                                                                                                      |
+=========================+========+==================================================================================================================================================+
| Calculator              | yes    | Parses and solves mathematical expressions.                                                                                                      |
+-------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Hash plugin             | yes    | Converts strings to different hash digests. Available functions: md5, sha1, sha224, sha256, sha384, sha512.                                      |
+-------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Self Information        | yes    | Displays your IP if the query is "ip" and your user agent if the query is "user-agent".                                                          |
+-------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Timezones plugin        | yes    | Display the current time on different time zones.                                                                                                |
+-------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Tor check plugin        | no     | This plugin checks if the address of the request is a Tor exit-node, and informs the user if it is; like check.torproject.org, but from SearXNG. |
+-------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Unit converter plugin   | yes    | Convert between units                                                                                                                            |
+-------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Infinite scroll         | no     | Automatically loads the next page when scrolling to bottom of the current page                                                                   |
+-------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Open Access DOI rewrite | no     | Avoid paywalls by redirecting to open-access versions of publications when available                                                             |
+-------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Tracker URL remover     | yes    | Remove trackers arguments from the returned URL                                                                                                  |
+-------------------------+--------+--------------------------------------------------------------------------------------------------------------------------------------------------+

: [Table 1 ][Plugins configured at built time (defaults)][¶](#id1 "Link to this table")