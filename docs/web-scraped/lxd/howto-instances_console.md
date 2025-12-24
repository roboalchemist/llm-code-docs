# Source: https://documentation.ubuntu.com/lxd/en/latest/howto/instances_console/

[]

# How to access the console[¶](#how-to-access-the-console "Link to this heading")

You can access the instance console to log in to the instance and see log messages. The console is available at boot time already, so you can use it to see boot messages and, if necessary, debug startup issues of a container or VM.

CLI

API

UI

Use the [[[`lxc`]` `[`console`]]](../../reference/manpages/lxc/console/#lxc-console-md) command to attach to instance consoles. To get an interactive console, enter the following command:

    lxc console <instance_name>

To show new log messages (only for containers), pass the [`--show-log`] flag:

    lxc console <instance_name> --show-log

You can also immediately attach to the console when you start your instance:

    lxc start <instance_name> --console
    lxc start <instance_name> --console=vga

Tip

To exit the console, enter [Ctrl]+[a] [q].

To start an interactive console, send a POST request to the [`console`] endpoint:

    lxc query --request POST /1.0/instances/<instance_name>/console --data ''

This query sets up two WebSockets that you can use for connection. One WebSocket is used for control, and the other transmits the actual console data.

See [[`POST`]` `[`/1.0/instances//console`]](/lxd/latest/api/#/instances/instance_console_post) for more information.

To access the WebSockets, you need the operation ID and the secrets for each socket. This information is available in the operation started by the query, for example:

    
      }
    [...]
    }

How to connect to the WebSockets depends on the tooling that you use (see [[`GET`]` `[`/1.0/operations//websocket`]](/lxd/latest/api/#/operations/operation_websocket_get) for general information). To quickly check whether the connection is successful and you can read from the socket, you can use a tool like [[`websocat`]](https://github.com/vi/websocat):

    websocat --text \
    --ws-c-uri=ws://unix.socket/1.0/operations/<operation_ID>/websocket?secret=<data_socket_secret> \
    - ws-c:unix:/var/snap/lxd/common/lxd/unix.socket

Alternatively, if you just want to retrieve new log messages from the console instead of connecting through a WebSocket, you can send a GET request to the [`console`] endpoint:

    lxc query --request GET /1.0/instances/<instance_name>/console

See [[`GET`]` `[`/1.0/instances//console`]](/lxd/latest/api/#/instances/instance_console_get) for more information. Note that this operation is supported only for containers, not for VMs.

Navigate to the instance detail page and switch to the [Console] tab to view the console.

## Access the graphical console (for virtual machines)[¶](#access-the-graphical-console-for-virtual-machines "Link to this heading")

[[▶] [Watch on YouTube]](https://www.youtube.com/watch?v=pEUsTMiq4B4)

On virtual machines, log on to the console to get graphical output. Using the console you can, for example, install an operating system using a graphical interface or run a desktop environment.

An additional advantage is that the console is available even if the [`lxd-agent`] process is not running. This means that you can access the VM through the console before the [`lxd-agent`] starts up, and also if the [`lxd-agent`] is not available at all.

CLI

API

UI

To start the VGA console with graphical output for your VM, you must install a SPICE client (for example, [`virt-viewer`] or [`spice-gtk-client`]). Then enter the following command:

    lxc console <vm_name> --type vga

To start the VGA console with graphical output for your VM, send a POST request to the [`console`] endpoint:

    lxc query --request POST /1.0/instances/<instance_name>/console --data ''

See [[`POST`]` `[`/1.0/instances//console`]](/lxd/latest/api/#/instances/instance_console_post) for more information.

Navigate to the instance detail page and switch to the [Console] tab to view the console.

For virtual machines, you can switch between the graphic console and the text console.