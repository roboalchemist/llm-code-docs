# Source: https://rustdesk.com/docs/en/self-host/rustdesk-server-oss/synology/dsm-6/

# Synology DSM 6

An alternative up-to-date tutorial from third-party is here.

This tutorial is based on latest DSM v6 and v7.

Note

After DSM 7.2 update, the Docker is upgraded to new &ldquo;Container Manager&rdquo;, please check this article instead.

## Install Docker

Open Package CenterInstall Docker
## Install RustDesk Server

Search rustdesk-server in Docker&rsquo;s registry and install by double clickInstalled rustdesk-server image, double click to create rustdesk-server container
## Create hbbs container

As mentioned above, double click on rustdesk-server image to create new container, set it name to `hbbs`.

Click on above `Advanced Settings`.

- 
Enable `Enable auto-restart`.

- 
Enable `Use the same network as Docker Host`. For more about host net, please check.

- 
Mount a host directory (e.g. `/home/rustdesk/`) to `/root`, hbbs will generate some files (database and `key` files) in this directory which need to be persistent over reboots.

MountFiles generated in the host directory
- Set command

Note

Synology&rsquo;s OS is Debian based, so host net (&ndash;net=host) works fine, we do not need to map ports with `-p` option.

- Done

## Create hbbr container

Please repeat above `hbbs` steps, but name the container `hbbr` and command (for Set Command Step) should be `hbbr`.

## hbbr/hbbs containers

Double click on container and check logDouble confirm hbbs/hbbr using host network
## Retrieve your Key

Browse to the folder setup before using File Station, download `id_ed25519.pub` and open with a text editor to via your key.