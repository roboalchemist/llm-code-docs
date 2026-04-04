# Source: https://docs.vespa.ai/en/reference/applications/hosts.html.md

# hosts.xml

 

_hosts.xml_ is a configuration file in an [application package](application-packages.html). Elements:

```
hosts[host [name]](#host)[alias](#alias)
```

The purpose of _hosts.xml_ is to add aliases for real hostnames to self-defined aliases. The aliases are used in [services.xml](services/services.html) to map service instances to hosts. It is only needed when deploying to multiple hosts.

## host

Sub-elements:

- [`alias`](#alias)

Example:

```
```
<hosts>
    <host name="myserver0.mydomain.com">
        <alias>SEARCH0</alias>
        <alias>CONTAINER0</alias>
    </host>
    <host name="myserver1.mydomain.com">
        <alias>SEARCH1</alias>
        <alias>CONTAINER1</alias>
    </host>
</hosts>
```
```

## alias

Alias used in [services.xml](services/services.html) to refer to the host.

 Copyright © 2026 - [Cookie Preferences](#)

