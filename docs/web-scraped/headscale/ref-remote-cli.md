# Source: https://headscale.net/stable/ref/remote-cli/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/ref/remote-cli.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/ref/remote-cli.md "View source of this page")

# Controlling headscale with remote CLI[¶](#controlling-headscale-with-remote-cli "Permanent link")

This documentation has the goal of showing a user how-to control a headscale instance from a remote machine with the `headscale` command line binary.

## Prerequisite[¶](#prerequisite "Permanent link")

- A workstation to run `headscale` (any supported platform, e.g. Linux).
- A headscale server with gRPC enabled.
- Connections to the gRPC port (default: `50443`) are allowed.
- Remote access requires an encrypted connection via TLS.
- An API key to authenticate with the headscale server.

## Create an API key[¶](#create-an-api-key "Permanent link")

We need to create an API key to authenticate with the remote headscale server when using it from our workstation.

To create an API key, log into your headscale server and generate a key:

    headscale apikeys create --expiration 90d

Copy the output of the command and save it for later. Please note that you can not retrieve a key again, if the key is lost, expire the old one, and create a new key.

To list the keys currently associated with the server:

    headscale apikeys list

and to expire a key:

    headscale apikeys expire --prefix "<PREFIX>"

## Download and configure headscale[¶](#download-and-configure-headscale "Permanent link")

1.  Download the [`headscale` binary from GitHub\'s release page](https://github.com/juanfont/headscale/releases). Make sure to use the same version as on the server.

2.  Put the binary somewhere in your `PATH`, e.g. `/usr/local/bin/headscale`

3.  Make `headscale` executable:

    ::: 
        chmod +x /usr/local/bin/headscale
    :::

4.  Provide the connection parameters for the remote headscale server either via a minimal YAML configuration file or via environment variables:

    ::::::::: 
    ::: tabbed-labels
    Minimal YAML configuration fileEnvironment variables
    :::

    ::::::: tabbed-content
    :::: tabbed-block
    ::: 
    [config.yaml]
        cli:
            address: <HEADSCALE_ADDRESS>:<PORT>
            api_key: <API_KEY_FROM_PREVIOUS_STEP>
    :::
    ::::

    :::: tabbed-block
    ::: 
        export HEADSCALE_CLI_ADDRESS="<HEADSCALE_ADDRESS>:<PORT>"
        export HEADSCALE_CLI_API_KEY="<API_KEY_FROM_PREVIOUS_STEP>"
    :::
    ::::
    :::::::
    :::::::::

    This instructs the `headscale` binary to connect to a remote instance at `<HEADSCALE_ADDRESS>:<PORT>`, instead of connecting to the local instance.

5.  Test the connection

    Let us run the headscale command to verify that we can connect by listing our nodes:

    ::: 
        headscale nodes list
    :::

    You should now be able to see a list of your nodes from your workstation, and you can now control the headscale server from your workstation.

## Behind a proxy[¶](#behind-a-proxy "Permanent link")

It is possible to run the gRPC remote endpoint behind a reverse proxy, like Nginx, and have it run on the *same* port as headscale.

While this is *not a supported* feature, an example on how this can be set up on [NixOS is shown here](https://github.com/kradalby/dotfiles/blob/4489cdbb19cddfbfae82cd70448a38fde5a76711/machines/headscale.oracldn/headscale.nix#L61-L91).

## Troubleshooting[¶](#troubleshooting "Permanent link")

- Make sure you have the *same* headscale version on your server and workstation.
- Ensure that connections to the gRPC port are allowed.
- Verify that your TLS certificate is valid and trusted.
- If you don\'t have access to a trusted certificate (e.g. from Let\'s Encrypt), either:
  - Add your self-signed certificate to the trust store of your OS *or*
  - Disable certificate verification by either setting `cli.insecure: true` in the configuration file or by setting `HEADSCALE_CLI_INSECURE=1` via an environment variable. We do **not** recommend to disable certificate validation.