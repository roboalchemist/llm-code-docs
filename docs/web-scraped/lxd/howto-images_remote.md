# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/images_remote/

[]

# How to use remote images[¶](#how-to-use-remote-images "Link to this heading")

The [[[`lxc`]]](../../reference/manpages/lxc/#lxc-md) CLI command is pre-configured with several remote image servers. See [[Remote image servers]](../../reference/remote_image_servers/#remote-image-servers) for an overview.

Note

-   If you are using the API, you can interact with different LXD servers by using their exposed API addresses. See [[Authenticate with the LXD server]](../server_expose/#server-authenticate) for instructions on how to authenticate with the servers.

    [[How to manage images]](../images_manage/#images-manage) describes how to interact with images on any LXD server through the API.

-   The UI is pre-configured with several remote image servers, but does not currently support adding other servers or managing remote images.

    You can see the available remote images (and which server they are hosted on) when you select the base image for a new instance.

## List configured remotes[¶](#list-configured-remotes "Link to this heading")

To see all configured remote servers, enter the following command:

    lxc remote list

Remote servers that use the [simple streams format](https://git.launchpad.net/simplestreams/tree/) are pure image servers. Servers that use the [`lxd`] format are LXD servers, which either serve solely as image servers or might provide some images in addition to serving as regular LXD servers. See [[Remote server types]](../../reference/remote_image_servers/#remote-image-server-types) for more information.

## List available images on a remote[¶](#list-available-images-on-a-remote "Link to this heading")

To list all remote images on a server, enter the following command:

    lxc image list <remote>:

You can filter the results. See [[Filter available images]](../images_manage/#images-manage-filter) for instructions.

## Add a remote server[¶](#add-a-remote-server "Link to this heading")

How to add a remote depends on the protocol that the server uses.

### Add a simple streams server[¶](#add-a-simple-streams-server "Link to this heading")

To add a simple streams server as a remote, enter the following command:

    lxc remote add <remote_name> <URL> --protocol=simplestreams

The URL must use HTTPS.

### Add a remote LXD server[¶](#add-a-remote-lxd-server "Link to this heading")

To add a LXD server as a remote, enter the following command:

    lxc remote add <remote_name> <IP|FQDN|URL|token> [flags]

Some authentication methods require specific flags (for example, use [[[`lxc`]` `[`remote`]` `[`add`]` `[`<remote_name>`]` `[`<IP|FQDN|URL>`]` `[`--auth-type=oidc`]]](../../reference/manpages/lxc/remote/add/#lxc-remote-add-md) for OIDC authentication). See [[Authenticate with the LXD server]](../server_expose/#server-authenticate) and [[Remote API authentication]](../../authentication/#authentication) for more information.

For example, enter the following command to add a remote through an IP address:

    lxc remote add my-remote 192.0.2.10

You are prompted to confirm the remote server fingerprint and then asked for the token.

## Reference an image[¶](#reference-an-image "Link to this heading")

To reference an image, specify its remote and its alias or fingerprint, separated with a colon. For example:

    ubuntu:24.04
    ubuntu-minimal:24.04
    images:alpine/edge
    local:ed7509d7e83f

[]

## Select a default remote[¶](#select-a-default-remote "Link to this heading")

If you specify an image name without the name of the remote, the default image server is used.

To see which server is configured as the default image server, enter the following command:

    lxc remote get-default

To select a different remote as the default image server, enter the following command:

    lxc remote switch <remote_name>