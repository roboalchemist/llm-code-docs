#### > This option file is used in:
#### >   podman build, create, farm build, run
#### > If file is edited, make sure the changes
#### > are applicable to all of those.

#### **--dns**=*ipaddr*

Set custom DNS servers.

This option can be used to override the DNS
configuration passed to the container. Typically this is necessary when the
host DNS configuration is invalid for the container (e.g., **127.0.0.1**). When this
is the case the **--dns** flag is necessary for every run.

The special value **none** can be specified to disable creation of */etc/resolv.conf* in the container by Podman.
The */etc/resolv.conf* file in the image is then used without changes.

Note that **ipaddr** may be added directly to the container's */etc/resolv.conf*.
This is not guaranteed though.  For example, passing a custom network whose *dns_enabled* is set to *true* to **--network** will result in */etc/resolv.conf* only referring to the aardvark-dns server.  aardvark-dns then forwards to the supplied **ipaddr** for all non-container name queries.
