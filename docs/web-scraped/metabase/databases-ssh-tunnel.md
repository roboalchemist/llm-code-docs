# Source: https://www.metabase.com/docs/latest/databases/ssh-tunnel

<div>

1.  [Home](/docs/latest/)
2.  [Databases](/docs/latest/databases/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# SSH tunneling

Metabase can connect to some databases by first establishing a connection to a server in between Metabase and a data warehouse, then connecting to the data warehouse using that connection as a bridge. This makes connecting to some data warehouses possible in situations that would otherwise prevent the use of Metabase.

## When to use SSH tunneling

In general, there are two basic use cases for an SSH tunnel:

-   When a direct connection is impossible.
-   When a direct connection is forbidden due to a security policy.

Sometimes when a data warehouse is inside an enterprise environment, direct connections are blocked by security devices such as firewalls and intrusion prevention systems. Bastion hosts offer the option to first connect to a computer on the edge of the protected network, then, from that bastion host computer, establish a second connection to the data warehouse within the internal network, essentially patching these two connections together. Using the SSH tunneling feature, Metabase can automate this process.

> [Metabase Cloud](/cloud/) does not currently support VPN connections to databases. To connect to databases in private networks, you can instead use SSH tunneling.

## How to use SSH tunneling

When connecting though a bastion host:

-   Answer yes to the "Use an SSH-tunnel for database connections" parameter.
-   Enter the hostname for the data warehouse as it is seen from inside the network in the `Host` parameter.
-   Enter the data warehouse port as seen from inside the network into the `Port` parameter.
-   Enter the external name of the bastion host as seen from the outside of the network (or wherever you are) into the `SSH tunnel host` parameter.
-   Enter the SSH port as seen from outside the network into the `SSH tunnel port` parameter. This is usually 22, regardless of which data warehouse you are connecting to.

For authentication, you have two options:

-   **Using a username and password:**

    -   In the `SSH tunnel username` and `SSH tunnel password` fields, enter the username and password you use to log in to the bastion host.

-   **Using SSH key (PKI authentication):**

    -   Select SSH Key for the `SSH authentication` option.
    -   Paste the contents of your SSH private key into the `SSH private key` field.
    -   If your key has a passphrase, enter it into the `Passphrase for the SSH private key` field.

If you're unable to connect test your SSH credentials by connecting to the SSH server/Bastion Host using ssh directly:

``` highlight
ssh <SSH tunnel username>@<SSH tunnel host> -p <SSH tunnel port>
```

Another common case where direct connections are impossible is when connecting to a data warehouse that is only accessible locally and does not allow remote connections. In this case you will be opening an SSH connection to the data warehouse, then from there connecting back to the same computer.

-   Answer yes to the "Use an SSH-tunnel for database connections" parameter.
-   Enter `localhost` in the `Host` parameter. This is the name the server.
-   Enter the same value in the `Port` parameter that you would use if you where sitting directly at the data warehouse host system.
-   Enter the external name of the data warehouse, as seen from the outside of the network (or wherever you are) into the `SSH tunnel host` parameter.
-   Enter the SSH port as seen from outside the network into the `SSH tunnel port` parameter. This is usually 22, regardless of which data warehouse you are connecting to.
-   Choose your authentication method as described above (username and password or SSH key).

If you have problems connecting, verify the SSH host port and password by connecting manually using ssh or PuTTY on older windows systems.

NOTE: the SSH server needs to have "AllowTcpForwarding" configuration set to "yes" for the tunneling to work.

NOTE: the best practice with SSH Tunnel Hosts is to deny all traffic except from approved clients. Metabase lists our Metabase [Cloud IPs to whitelist here](/docs/latest/cloud/ip-addresses-to-whitelist).

## Disadvantages of indirect connections

While using an SSH tunnel makes it possible to use a data warehouse that is otherwise inaccessible, it's almost always preferable to use a direct connection when possible.

There are several inherent limitations to connecting through a tunnel:

-   If the enclosing SSH connection is closed because you put your computer to sleep or change networks, all established connections will be closed as well. This can cause delays resuming connections after suspending your laptop.
-   It's almost always slower. The connection has to go through an additional computer.
-   Opening new SSH connections takes longer.
-   Multiple operations over the same SSH tunnel can block each other. This can increase latency.
-   The number of connections through a bastion host is often limited by organizational policy.
-   Some organizations have IT security policies forbidding using SSH tunnels to bypass security perimeters.

## Running SSH directly

The SSH tunneling feature in Metabase exists as a convenient wrapper around SSH, and automates the common cases of connecting through a tunnel. It also makes connections possible with systems that don't give shell access. Metabase uses a built-in SSH client that doesn't depend on the installed system's SSH client. This allows connections from systems where you can't run SSH manually. It also means that Metabase can't take advantage of authentication services provided by the system, such as Windows Domain Authentication or Kerberos Authentication.

If you need to connect using a method not enabled by Metabase, you can often accomplish this by running SSH directly:

``` highlight
ssh -Nf -L input-port:internal-server-name:port-on-server username@bastion-host.domain.com
```

This allows you to use the full array of features included in SSH. If you find yourself doing this often, please let us know so we can see about making your process more convenient through Metabase.

## Further reading

-   [Adding and managing databases](./connecting).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/databases/ssh-tunnel.md) ]