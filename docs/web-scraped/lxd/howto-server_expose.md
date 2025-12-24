# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/server_expose/

[]

# How to expose LXD to the network[¶](#how-to-expose-lxd-to-the-network "Link to this heading")

By default, LXD can be used only by local users through a Unix socket and is not accessible over the network.

To expose LXD to the network, you must configure it to listen to addresses other than the local Unix socket. To do so, set the [[`core.https_address`]](../../server/#server-core:core.https_address) server configuration option.

For example, allow access to the LXD server on port [`8443`]:

CLI

API

UI

    lxc config set core.https_address :8443

    lxc query --request PATCH /1.0 --data '
    }'

Note

The UI requires LXD to be exposed to the network. Therefore, you must use the CLI or API to originally expose LXD to the network.

Once you have access to the UI, you can use it to update the setting. However, be careful when changing the configured value, because using an invalid value might cause you to lose access to the UI.

Go to [Settings] and edit the value for [`core.https_address`].

To allow access through a specific IP address, use [`ip`]` `[`addr`] to find an available address and then set it. For example:

[`user@host:~$`]` `

[[`ip`]` `[`addr`]` `]

    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
           valid_lft forever preferred_lft forever
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever
    2: enp5s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000
        link/ether 00:16:3e:e3:f3:3f brd ff:ff:ff:ff:ff:ff
        inet 10.68.216.12/24 metric 100 brd 10.68.216.255 scope global dynamic enp5s0
           valid_lft 3028sec preferred_lft 3028sec
        inet6 fd42:e819:7a51:5a7b:216:3eff:fee3:f33f/64 scope global mngtmpaddr noprefixroute
           valid_lft forever preferred_lft forever
        inet6 fe80::216:3eff:fee3:f33f/64 scope link
           valid_lft forever preferred_lft forever
    3: lxdbr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
        link/ether 00:16:3e:8d:f3:72 brd ff:ff:ff:ff:ff:ff
        inet 10.64.82.1/24 scope global lxdbr0
           valid_lft forever preferred_lft forever
        inet6 fd42:f4ab:4399:e6eb::1/64 scope global
           valid_lft forever preferred_lft forever

[`user@host:~$`]` `

[[`lxc`]` `[`config`]` `[`set`]` `[`core.https_address`]` `[`10.68.216.12`]` `]

All remote clients can then connect to LXD and access any image that is marked for public use.

[]

## Authenticate with the LXD server[¶](#authenticate-with-the-lxd-server "Link to this heading")

To be able to access the remote API, clients must authenticate with the LXD server. There are several authentication methods; see [[Remote API authentication]](../../authentication/#authentication) for detailed information.

The recommended method is to add the client's TLS certificate to the server's trust store through a trust token. There are two ways to create a token. Create a *pending fine-grained TLS identity* if you would like to manage client permissions via [[Fine-grained authorization]](../../explanation/authorization/#fine-grained-authorization). Create a *certificate add token* if you would like to grant the client full access to LXD, or manage their permissions via [[Restricted TLS certificates]](../../explanation/authorization/#restricted-tls-certs).

See [[How to access the LXD web UI]](../access_ui/#access-ui) for instructions on how to authenticate with the LXD server using the UI. To authenticate a CLI or API client using a trust token, complete the following steps:

1.  On the server, generate a trust token.

    ::: 
    ::: 
    CLI
    API
    :::

    ::: 
    There are currently two ways to retrieve a trust token in LXD.

    **Create a certificate add token**

    To generate a trust token, enter the following command on the server:

    ::: 
    ::: highlight
        lxc config trust add
    :::
    :::

    Enter the name of the client that you want to add. The command generates and prints a token that can be used to add the client certificate.

    ::: 
    Note

    The recipient of this token will have full access to LXD. To restrict the access of the client, you must use the [`--restricted`] flag. See [[Confine users to specific projects on the HTTPS API]](../projects_confine/#projects-confine-https) for more details.
    :::

    **Create a pending fine-grained TLS identity**

    To create a pending fine-grained TLS identity, enter the following command on the server:

    ::: 
    ::: highlight
        lxc auth identity create tls/<client_name>
    :::
    :::

    The command generates and prints a token that can be used to add the client certificate.

    ::: 
    Note

    The recipient of this token is not authorized to perform any actions in the LXD server. To grant access, the identity must be added to one or more groups with permissions assigned. See [[Fine-grained authorization]](../../explanation/authorization/#fine-grained-authorization).
    :::
    :::

    ::: 
    **Create a certificate add token**

    To generate a trust token, send a POST request to the [`/1.0/certificates`] endpoint:

    ::: 
    ::: highlight
        lxc query --request POST /1.0/certificates --data ''
    :::
    :::

    See [[`POST`]` `[`/1.0/certificates`]](/lxd/latest/api/#/certificates/certificates_post) for more information.

    The return value of this query contains an operation that has the information that is required to generate the trust token:

    ::: 
    ::: highlight
        ,
         ...
        }
    :::
    :::

    Use this information to generate the trust token:

    ::: 
    ::: highlight
        echo -n '' | base64 -w0
    :::
    :::

    **Create a pending fine-grained TLS identity**

    To generate a trust token, send a POST request to the [`/1.0/auth/identities/tls`] endpoint:

    ::: 
    ::: highlight
        lxc query --request POST /1.0/auth/identities/tls --data ''
    :::
    :::

    See [[`POST`]` `[`/1.0/auth/identities/tls`]](/lxd/latest/api/#/auth/identitites/identities_post_tls) for more information.

    The return value of this query contains the information that is required to generate the trust token:

    ::: 
    ::: highlight
        
    :::
    :::

    Use this information to generate the trust token:

    ::: 
    ::: highlight
        echo -n '' | base64 -w0
    :::
    :::
    :::
    :::

2.  Authenticate the client.

    ::: 
    ::: 
    CLI
    API
    :::

    ::: 
    On the client, add the server with the following command:

    ::: 
    ::: highlight
        lxc remote add <remote_name> <token>
    :::
    :::

    ::: 
    Note

    If your LXD server is behind NAT, you must specify its external public address when adding it as a remote for a client:

    ::: 
    ::: highlight
        lxc remote add <name> <IP_address>
    :::
    :::

    When you are prompted for the token, specify the generated token from the previous step. Alternatively, use the [`--token`] flag:

    ::: 
    ::: highlight
        lxc remote add <name> <IP_address> --token <token>
    :::
    :::

    When generating the token on the server, LXD includes a list of IP addresses that the client can use to access the server. However, if the server is behind NAT, these addresses might be local addresses that the client cannot connect to. In this case, you must specify the external address manually.
    :::
    :::

    ::: 
    On the client, generate a certificate to use for the connection:

    ::: 
    ::: highlight
        openssl req -x509 -newkey rsa:2048 -keyout "<keyfile_name>" -nodes \
        -out "<crtfile_name>" -subj "/CN=<client_name>"
    :::
    :::

    **Trust store entries**

    Then send a POST request to the [`/1.0/certificates?public`] endpoint to authenticate:

    ::: 
    ::: highlight
        curl -k -s --key "<keyfile_name>" --cert "<crtfile_name>" \
        -X POST https://<server_address>/1.0/certificates \
        --data ''
    :::
    :::

    See [[`POST`]` `[`/1.0/certificates?public`]](/lxd/latest/api/#/certificates/certificates_post_untrusted) for more information.

    **TLS identities**

    Send a POST request to the [`/1.0/auth/identities/tls?public`] endpoint to authenticate:

    ::: 
    ::: highlight
        curl --insecure --key "<keyfile_name>" --cert "<crtfile_name>" \
        -X POST https://<server_address>/1.0/auth/identities/tls \
        --data ''
    :::
    :::

    See [[`POST`]` `[`/1.0/auth/identities/tls?public`]](/lxd/latest/api/#/auth/identities/identities_post_tls_untrusted) for more information.
    :::
    :::

See [[Remote API authentication]](../../authentication/#authentication) for detailed information and other authentication methods.