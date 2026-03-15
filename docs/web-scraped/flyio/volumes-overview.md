# Source: https://fly.io/docs/volumes/overview/

\*)\]:mx-auto \[body\_:where(&\>\*)\]:max-w-2xl \[body:not(.toc)\_:where(&\>\*)\]:lg:mx-\[calc(50%-min(50%,35rem))\] \[body\_:where(&\>\*)\]:lg:max-w-3xl min-w-0 relative\"\>

# Fly Volumes overview 

<figure class="flex justify-center">
<img src="/static/images/volumes.png" class="w-full max-w-lg mx-auto" alt="Illustration by Annie Ruygt of a filing cabinet" />
</figure>

The root file systems of a Fly Machine are ephemeral and should only be used for temporary data, application code, and runtime files that can be rebuilt from scratch during deployments or restarts. The performance of these ephemeral disks are heavily limited regardless of the Machine type you choose, with the maximum of 2000 IOPs and 8MiB/s bandwidth.

Fly Volumes are local persistent storage for [Fly Machines](/docs/machines/). You can access and write to a volume on a Machine just like a regular directory. Use volumes to store your database files, to save your app's state, such as configuration and session or user data, or for any information that needs to persist after deploy or restart. Maximum volume performance varies by Machine type and noted in [Volume limits](/docs/volumes/overview#volume-limits)

A Fly Volume is a slice of an NVMe drive on the same physical server as the Machine on which it's mounted and it's tied to that hardware. Fly Volumes are similar to the disk inside your laptop, accessible from a mount point in your file system. Using volumes tied to hardware has both advantages and disadvantages.

## [](#volume-considerations)[Volume considerations] 

-   **A volume belongs to one app**: Every Fly Volume belongs to a [Fly App](/docs/apps/overview/) and you can't share a volume between apps.
-   **A volume exists on one server**: Each volume exists on one server in a single region. It is not network storage.
-   **A volume can attach to one Machine**: You need to run as many volumes as there are Machines. There's a one-to-one mapping between Machines and volumes. A Machine can only mount one volume at a time and a volume can be attached to only one Machine.
-   **Develop your app to handle replication**: Volumes are independent of one another; Fly.io does not automatically replicate data among the volumes on an app, so if you need the volumes to sync up, then your app has to make that happen.
-   **Create redundancy in your primary region**: If your app needs a volume to function, and the NVMe drive hosting your volume fails, then that instance of your app goes down. There's no way around that. You can run multiple Machines with volumes in your app's primary region to mitigate hardware failures.
-   **Create and store backups**: If you only have a single copy of your data on a single volume, and that drive fails, then the data is lost. Fly.io takes daily snapshots and can retain them from 1 to 60 days (5 days by default), but the snapshots shouldn't be your primary backup method.

Explore other options for data storage in [Databases & Storage](/docs/database-storage-guides/).

## [](#volume-attachment)[Volume attachment] 

Fly Volumes and Fly Machines are meant to be paired together, but they are not always found in pairs. A Fly Volume can be created without a Fly Machine, or a Machine can be destroyed without destroying its volume. In these cases, the volume that's left is called an "unattached" volume.

A Fly Machine that does not require a volume will never attach itself to one. A Fly Machine that does require a volume will always be attached to one. When a volume is required according to the app or Machine configuration, any method of creating a new Fly Machine will pick up an unattached volume, create a new volume to attach, or it will fail (in the case of `fly machine` commands or create Machine API calls).

## [](#volume-redundancy)[Volume redundancy] 

**Warning: Always provision at least two volumes per app.** Running an app with a single Machine and volume leaves you at risk for downtime and data loss. Volumes donâ€™t have built-in replication between them, so your app or database needs to take care of replicating data between volumes.

We try to keep individual Fly Machines up for as long as possible, but hardware failures happen. That's why we recommend running at least two Machines per app to increase availability. You can run two or more Machines in one region, or better yet, one or more Machines in multiple regions. If you only have one Machine and volume, then you'll have downtime if there's a host or network failure, and whenever you deploy your app.

You'll also need to replicate data between volumes. Some options for replicating databases include [LiteFS - Distributed SQLite](/docs/litefs/) and [Supabase Postgres](/docs/supabase/).

In a few cases, you can run a single Machine with an attached volume. For example, if your app is in development and you're not yet worried about downtime or if you're running an app that can handle downtime and has a custom backup procedure.

## [](#volume-placement)[Volume placement] 

You can create volumes at the same time you create Machines, or ahead of time. If you try to create new Machines through [`flyctl scale count`](/docs/apps/scale-count/#scale-an-app-with-volumes), then `flyctl` will first check if you have any unattached volumes in the region you are creating new Machines in. If it finds unattached volumes, it will try to create the new Machines on the same servers. If it does not find any unattached volumes, then it will create new ones together with the Machines. You can also create unattached volumes through [`fly volumes create`](/docs/flyctl/volumes-create/).

Volumes exist on a single server in a single [region](/docs/reference/regions/). For redundancy within a region, you can run multiple Machines with attached volumes. Remember that volumes don't automatically replicate data between them.

To prevent a single server hardware failure from taking down your app, it is better if each volume is placed in a separate hardware zone. A separate hardware zone is just another way of saying a different server. We default to separate hardware zones when you create volumes with the [`fly volumes create`](/docs/flyctl/volumes-create/) command, but this is not guaranteed when creating Fly Volumes through other methods. Note that having each volume in a separate hardware zone limits the number of volumes your app can have in a region. If you need more volumes in a region than there are distinct hardware zones, you can set `--require-unique-zone` to `false` when you run [`fly volumes create`](/docs/flyctl/volumes-create/).

You can hint what type of compute load you expect to use the volume for by using the `--vm-XXX` options with the [`fly volumes create`](/docs/flyctl/volumes-create/) command. For example, to create a volume you want to use with an L40S GPU Machine, set `--vm-gpu-kind=l40s` to ensure that your new volume is placed on GPU hardware.

## [](#volume-encryption)[Volume encryption] 

Volumes are, by default, created with encryption-at-rest enabled for additional protection of the data on the volume. Use `--no-encryption` to instead create an unencrypted volume.

## [](#volume-size)[Volume size] 

The default volume size is 1GB when you create a volume with the `fly volumes create` command, and when you use the `fly launch` command to [launch an app with a volume](/docs/apps/volume-storage/#launch-a-new-app-with-a-fly-volume). The maximum volume size is 500GB.

You can extend a volume's size---either [manually](/docs/volumes/volume-manage/#extend-a-volume) or [automatically](/docs/reference/configuration/#the-mounts-section)---to make it larger, but you can't shrink a volume.

## [](#volume-limits)[Volume limits] 

The following table outlines the maximum IOPs and bandwidth for Fly Volumes, determined by the Machine type:

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idy01IGgtNSBwb2ludGVyLWV2ZW50cy1ub25lIiB2aWV3Ym94PSIwIDAgMjAgMjAiIGZpbGw9Im5vbmUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+PHBhdGggZD0iTTExLjkxMiAxMC4wMzdoMi43MzJjMS4yNzcgMCAyLjMxNS0uOTYyIDIuMzE1LTIuMjM3YTIuMzE0IDIuMzE0IDAgMDAtMi4zMTUtMi4zMUg0Ljk1OU0xNS4xODcgMTQuNUg0Ljk1OU04LjgwMiAxMEg0Ljk1OSI+PC9wYXRoPjxwYXRoIGQ9Ik0xMy4wODEgOC40NjZsLTEuNTQ4IDEuNTcxIDEuNTQ4IDEuNTcxIj48L3BhdGg+PC9nPjwvc3ZnPg==)[Wrap text]

  VM Size           Max IOPs   Max Bandwidth
  ----------------- ---------- ---------------
  shared-cpu-1x     4000       16MiB/s
  shared-cpu-2x     4000       16MiB/s
  shared-cpu-4x     8000       32MiB/s
  shared-cpu-8x     8000       32MiB/s
  performance-1x    12000      48MiB/s
  performance-2x    16000      64MiB/s
  performance-4x    16000      64MiB/s
  performance-8x    32000      128MiB/s
  performance-16x   32000      128MiB/s

## [](#volume-forks)[Volume forks] 

When you [fork a volume](/docs/volumes/volume-manage/#create-a-copy-of-a-volume-fork-a-volume), you create a new volume with an exact copy of the data from the source volume to use for testing, backups, or whatever you like. If you don't specify a region, then the new volume is in the same region, but on a different physical host. The forked volume isn't attached to a Machine until you scale or clone a new Machine in the same region. The new volume and the source volume are independent, and changes to their contents are not synchronized.

## [](#volume-snapshots)[Volume snapshots] 

Fly.io takes daily block-level snapshots of volumes. We keep snapshots for five days by default, but you can configure the snapshot retention to be from 1 to 60 days. Daily automatic snapshots may not have your latest data. You should still implement your own backup plan for important data.

You can also [create a snapshot of a volume](/docs/volumes/snapshots/#create-a-volume-snapshot) on demand.

You can [restore a volume snapshot](/docs/volumes/snapshots/#restore-a-volume-from-a-snapshot) into a new volume of equal or greater size.

You can also [disable automatic daily snapshots](/docs/volumes/snapshots/#disable-automatic-daily-snapshots).

## [](#when-volumes-are-not-available)[When volumes are not available] 

There are some instances where volumes are not available.

-   **Build Time**: When building a Docker image for deploying an application (e.g. `flyctl deploy`), volumes are not accessible.
-   **Release Command**: Volumes are also not mounted to the temporary Machine created when using a [release_command](/docs/reference/configuration/#run-one-off-commands-before-releasing-a-deployment).

## [](#related-topics)[Related topics] 

-   [Create and manage volumes](/docs/volumes/volume-manage/)
-   [Manage volume snapshots](/docs/volumes/snapshots/)
-   [Add volume storage to a Fly Launch app](/docs/apps/volume-storage/)
-   [Scale an app with volumes](/docs/apps/scale-count/#scale-an-app-with-volumes)

![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSIgc3R5bGU9IndpZHRoOiAxNnB4OyBoZWlnaHQ6IDE2cHg7IHBvaW50ZXItZXZlbnRzOiBub25lOyIgdmlld2JveD0iMCAwIDIwOCAxMjgiIGZpbGw9ImN1cnJlbnRDb2xvciI+CiAgPHJlY3Qgd2lkdGg9IjE5OCIgaGVpZ2h0PSIxMTgiIHg9IjUiIHk9IjUiIHJ5PSIxMCIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMTAiIGZpbGw9Im5vbmUiPjwvcmVjdD4KICA8cGF0aCBkPSJNMzAgOThWMzBoMjBsMjAgMjUgMjAtMjVoMjB2NjhIOTBWNTlMNzAgODQgNTAgNTl2Mzl6bTEyNSAwbC0zMC0zM2gyMFYzMGgyMHYzNWgyMHoiPjwvcGF0aD4KPC9zdmc+) [Copy page as markdown]

[or] [![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1yLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE2cHg7IGhlaWdodDogMTZweDsiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8cGF0aCBkPSJNMjIuMjgyIDkuODIxYTUuOTg1IDUuOTg1IDAgMCAwLS41MTYtNC45MSA2LjA0NiA2LjA0NiAwIDAgMC02LjUxLTIuOUE2LjA2NSA2LjA2NSAwIDAgMCA0Ljk4MSA0LjE4YTUuOTg1IDUuOTg1IDAgMCAwLTMuOTk4IDIuOSA2LjA0NiA2LjA0NiAwIDAgMCAuNzQzIDcuMDk3IDUuOTggNS45OCAwIDAgMCAuNTEgNC45MTEgNi4wNTEgNi4wNTEgMCAwIDAgNi41MTUgMi45QTUuOTg1IDUuOTg1IDAgMCAwIDEzLjI2IDI0YTYuMDU2IDYuMDU2IDAgMCAwIDUuNzcyLTQuMjA2IDUuOTkgNS45OSAwIDAgMCAzLjk5Ny0yLjkgNi4wNTYgNi4wNTYgMCAwIDAtLjc0Ny03LjA3M3pNMTMuMjYgMjIuNDNhNC40NzYgNC40NzYgMCAwIDEtMi44NzYtMS4wNGwuMTQxLS4wODEgNC43NzktMi43NThhLjc5NS43OTUgMCAwIDAgLjM5Mi0uNjgxdi02LjczN2wyLjAyIDEuMTY4YS4wNzEuMDcxIDAgMCAxIC4wMzguMDUydjUuNTgzYTQuNTA0IDQuNTA0IDAgMCAxLTQuNDk0IDQuNDk0ek0zLjYgMTguMzA0YTQuNDcgNC40NyAwIDAgMS0uNTM1LTMuMDE0bC4xNDIuMDg1IDQuNzgzIDIuNzU5YS43NzEuNzcxIDAgMCAwIC43OCAwbDUuODQzLTMuMzY5djIuMzMyYS4wOC4wOCAwIDAgMS0uMDMzLjA2Mkw5Ljc0IDE5Ljk1YTQuNSA0LjUgMCAwIDEtNi4xNC0xLjY0NnpNMi4zNCA3Ljg5NmE0LjQ4NSA0LjQ4NSAwIDAgMSAyLjM2Ni0xLjk3M1YxMS42YS43NjYuNzY2IDAgMCAwIC4zODguNjc2bDUuODE1IDMuMzU1LTIuMDIgMS4xNjhhLjA3Ni4wNzYgMCAwIDEtLjA3MSAwbC00LjgzLTIuNzg2QTQuNTA0IDQuNTA0IDAgMCAxIDIuMzQgNy44NzJ6bTE2LjU5NyAzLjg1NWwtNS44MzMtMy4zODdMMTUuMTE5IDcuMmEuMDc2LjA3NiAwIDAgMSAuMDcxIDBsNC44MyAyLjc5MWE0LjQ5NCA0LjQ5NCAwIDAgMS0uNjc2IDguMTA1di01LjY3OGEuNzkuNzkgMCAwIDAtLjQwNy0uNjY3em0yLjAxLTMuMDIzbC0uMTQxLS4wODUtNC43NzQtMi43ODJhLjc3Ni43NzYgMCAwIDAtLjc4NSAwTDkuNDA5IDkuMjNWNi44OTdhLjA2Ni4wNjYgMCAwIDEgLjAyOC0uMDYxbDQuODMtMi43ODdhNC41IDQuNSAwIDAgMSA2LjY4IDQuNjZ6bS0xMi42NCA0LjEzNWwtMi4wMi0xLjE2NGEuMDguMDggMCAwIDEtLjAzOC0uMDU3VjYuMDc1YTQuNSA0LjUgMCAwIDEgNy4zNzUtMy40NTNsLS4xNDIuMDhMOC43MDQgNS40NmEuNzk1Ljc5NSAwIDAgMC0uMzkzLjY4MXptMS4wOTctMi4zNjVsMi42MDItMS41IDIuNjA3IDEuNXYyLjk5OWwtMi41OTcgMS41LTIuNjA3LTEuNXoiPjwvcGF0aD4KPC9zdmc+) Open in ChatGPT ![](data:image/svg+xml;base64,PHN2ZyBhcmlhLWhpZGRlbj0idHJ1ZSIgY2xhc3M9Im1sLTEuNSBwb2ludGVyLWV2ZW50cy1ub25lIiBzdHlsZT0id2lkdGg6IDE0cHg7IGhlaWdodDogMTRweDsiIHZpZXdib3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSI+CiAgPHJlY3Qgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2IiByeD0iMyIgZmlsbD0iY3VycmVudENvbG9yIiBvcGFjaXR5PSIwLjEiPjwvcmVjdD4KICA8cGF0aCBkPSJNNiA1aDV2NU0xMSA1bC01IDUiIHN0cm9rZT0iY3VycmVudENvbG9yIiBzdHJva2Utd2lkdGg9IjEuNSIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIj48L3BhdGg+Cjwvc3ZnPg==)](https://chatgpt.com/?hints=search&q=Read+https%3A%2F%2Fraw.githubusercontent.com%2Fsuperfly%2Fdocs%2Fmain%2Fvolumes%2Foverview.html.markerb)

[![](data:image/svg+xml;base64,PHN2ZyByb2xlPSJpbWciIGNsYXNzPSJtci0xLjUiIHZpZXdib3g9IjAgMCAyNCAyNCIgc3R5bGU9InBvaW50ZXItZXZlbnRzOiBub25lOyB3aWR0aDogMjBweDsgaGVpZ2h0OiAyMHB4OyIgZmlsbD0iY3VycmVudENvbG9yIj4KICA8ZyBidWZmZXJlZC1yZW5kZXJpbmc9InN0YXRpYyI+CiAgICA8cGF0aCBkPSJNMTEuOTk5IDEuMjcxQzUuOTI1IDEuMjcxIDEgNi4xOTYgMSAxMi4yNzNjMCA0Ljg1OSAzLjE1MiA4Ljk4MiA3LjUyMyAxMC40MzcuNTUuMS43NTEtLjIzOS43NTEtLjUzbC0uMDE1LTEuODcyYy0zLjA2LjY2Ni0zLjcwNi0xLjQ3NC0zLjcwNi0xLjQ3NC0uNS0xLjI3MS0xLjIyMS0xLjYwOS0xLjIyMS0xLjYwOS0uOTk5LS42ODMuMDc1LS42NjguMDc1LS42NjggMS4xMDUuMDc3IDEuNjg1IDEuMTMzIDEuNjg1IDEuMTMzLjk4MSAxLjY4MSAyLjU3NSAxLjE5NiAzLjIwMi45MTQuMS0uNzExLjM4NC0xLjE5Ni42OTgtMS40NzEtMi40NDItLjI3Ny01LjAxMS0xLjIyMS01LjAxMS01LjQzNiAwLTEuMjAxLjQyOS0yLjE4MyAxLjEzMy0yLjk1Mi0uMTE0LS4yNzgtLjQ5MS0xLjM5Ny4xMDgtMi45MTEgMCAwIC45MjMtLjI5NiAzLjAyNSAxLjEyN0ExMC41NiAxMC41NiAwIDAgMSAxMiA2LjU5MWMuOTM1LjAwNCAxLjg3Ni4xMjcgMi43NTQuMzcgMi4xLTEuNDIzIDMuMDIyLTEuMTI3IDMuMDIyLTEuMTI3LjYgMS41MTQuMjIzIDIuNjMzLjExIDIuOTExLjcwNS43NjkgMS4xMzEgMS43NTEgMS4xMzEgMi45NTIgMCA0LjIyNS0yLjU3MyA1LjE1NS01LjAyMyA1LjQyNy4zOTUuMzQuNzQ3IDEuMDExLjc0NyAyLjAzOCAwIDEuNDcxLS4wMTQgMi42NTctLjAxNCAzLjAxOCAwIC4yOTMuMTk5LjYzNi43NTYuNTI4QzE5Ljg1MSAyMS4yNTEgMjMgMTcuMTMgMjMgMTIuMjczYzAtNi4wNzctNC45MjYtMTEuMDAyLTExLjAwMS0xMS4wMDJ6Ij48L3BhdGg+CiAgPC9nPgo8L3N2Zz4=) Report an issue](https://github.com/superfly/docs/issues/new?body=I+found+an+issue+with+this+document.%0A%0ATitle%3A+Fly+Volumes+overview%0ALocation%3A+https%3A%2F%2Ffly.io%2Fdocs%2Fvolumes%2Foverview%2F%0ASource%3A+https%3A%2F%2Fgithub.com%2Fsuperfly%2Fdocs%2Fblob%2Fmain%2Fvolumes%2Foverview.html.markerb%0A%0A%23%23%23+Describe+the+issue%0A%0A%3C%21--+Describe+the+issue+and+include+the+section+you%27re+referring+to%2C+if+applicable.+Provide+lots+of+detail+about+the+issue+that+you+found.++--%3E%0A%0A%23%23%23+Additional+info%0A%0A%3C%21--+Add+any+other+context+about+the+issue+here.+If+applicable%2C+add+screenshots+to+help+explain+the+issue.+--%3E%0A&title=Issue+with+the+%22Fly+Volumes+overview%22+doc) or [edit this page on GitHub](https://github.com/superfly/docs/edit/main/volumes/overview.html.markerb)