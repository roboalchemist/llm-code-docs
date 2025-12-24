# Source: https://headscale.net/stable/usage/getting-started/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiIC8+PC9zdmc+)](https://github.com/juanfont/headscale/blob/main/docs/usage/getting-started.md "Edit this page") [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTE3IDE4Yy41NiAwIDEgLjQ0IDEgMXMtLjQ0IDEtMSAxLTEtLjQ0LTEtMSAuNDQtMSAxLTFtMC0zYy0yLjczIDAtNS4wNiAxLjY2LTYgNCAuOTQgMi4zNCAzLjI3IDQgNiA0czUuMDYtMS42NiA2LTRjLS45NC0yLjM0LTMuMjctNC02LTRtMCA2LjVhMi41IDIuNSAwIDAgMS0yLjUtMi41IDIuNSAyLjUgMCAwIDEgMi41LTIuNSAyLjUgMi41IDAgMCAxIDIuNSAyLjUgMi41IDIuNSAwIDAgMS0yLjUgMi41TTkuMjcgMjBINlY0aDd2NWg1djQuMDdjLjcuMDggMS4zNi4yNSAyIC40OVY4bC02LTZINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAyIDJoNC41YTguMiA4LjIgMCAwIDEtMS4yMy0yIiAvPjwvc3ZnPg==)](https://github.com/juanfont/headscale/raw/main/docs/usage/getting-started.md "View source of this page")

# Getting started[¶](#getting-started "Permanent link")

This page helps you get started with headscale and provides a few usage examples for the headscale command line tool `headscale`.

Prerequisites

- Headscale is installed and running as system service. Read the [setup section](../../setup/requirements/) for installation instructions.
- The configuration file exists and is adjusted to suit your environment, see [Configuration](../../ref/configuration/) for details.
- Headscale is reachable from the Internet. Verify this by opening client specific setup instructions in your browser, e.g. <https://headscale.example.com/windows>
- The Tailscale client is installed, see [Client and operating system support](../../about/clients/) for more information.

## Getting help[¶](#getting-help "Permanent link")

The `headscale` command line tool provides built-in help. To show available commands along with their arguments and options, run:

NativeContainer

    # Show help
    headscale help

    # Show help for a specific command
    headscale <COMMAND> --help

    # Show help
    docker exec -it headscale \
      headscale help

    # Show help for a specific command
    docker exec -it headscale \
      headscale <COMMAND> --help

## Manage headscale users[¶](#manage-headscale-users "Permanent link")

In headscale, a node (also known as machine or device) is always assigned to a headscale user. Such a headscale user may have many nodes assigned to them and can be managed with the `headscale users` command. Invoke the built-in help for more information: `headscale users --help`.

### Create a headscale user[¶](#create-a-headscale-user "Permanent link")

NativeContainer

    headscale users create <USER>

    docker exec -it headscale \
      headscale users create <USER>

### List existing headscale users[¶](#list-existing-headscale-users "Permanent link")

NativeContainer

    headscale users list

    docker exec -it headscale \
      headscale users list

## Register a node[¶](#register-a-node "Permanent link")

One has to register a node first to use headscale as coordination with Tailscale. The following examples work for the Tailscale client on Linux/BSD operating systems. Alternatively, follow the instructions to connect [Android](../connect/android/), [Apple](../connect/apple/) or [Windows](../connect/windows/) devices.

### Normal, interactive login[¶](#normal-interactive-login "Permanent link")

On a client machine, run the `tailscale up` command and provide the FQDN of your headscale instance as argument:

    tailscale up --login-server <YOUR_HEADSCALE_URL>

Usually, a browser window with further instructions is opened and contains the value for `<YOUR_MACHINE_KEY>`. Approve and register the node on your headscale server:

NativeContainer

    headscale nodes register --user <USER> --key <YOUR_MACHINE_KEY>

    docker exec -it headscale \
      headscale nodes register --user <USER> --key <YOUR_MACHINE_KEY>

### Using a preauthkey[¶](#using-a-preauthkey "Permanent link")

It is also possible to generate a preauthkey and register a node non-interactively. First, generate a preauthkey on the headscale instance. By default, the key is valid for one hour and can only be used once (see `headscale preauthkeys --help` for other options):

NativeContainer

    headscale preauthkeys create --user <USER_ID>

    docker exec -it headscale \
      headscale preauthkeys create --user <USER_ID>

The command returns the preauthkey on success which is used to connect a node to the headscale instance via the `tailscale up` command:

    tailscale up --login-server <YOUR_HEADSCALE_URL> --authkey <YOUR_AUTH_KEY>