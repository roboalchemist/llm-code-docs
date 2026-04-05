::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#main-content .bd-main role="main"}
::: sbt-scroll-pixel-helper
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-content
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: bd-article-container
:::::::::: {.bd-header-article .d-print-none}
::::::::: {.header-article-items .header-article__inner}
:::: header-article-items__start
::: header-article-item
[]{.fa-solid .fa-bars}
:::
::::

:::::: header-article-items__end
::::: header-article-item
:::: article-header-buttons
[[
]{.btn__icon-container}](https://github.com/ml-explore/mlx "Source repository"){.btn
.btn-sm .btn-source-repository-button target="_blank"
bs-placement="bottom" bs-toggle="tooltip"}

::: {.dropdown .dropdown-download-buttons}

- [[ ]{.btn__icon-container}
  [.rst]{.btn__text-container}](../_sources/usage/distributed.rst "Download source file"){.btn
  .btn-sm .btn-download-source-button .dropdown-item target="_blank"
  bs-placement="left" bs-toggle="tooltip"}
- [ ]{.btn__icon-container} [.pdf]{.btn__text-container}
:::

[ ]{.btn__icon-container}

[]{.fa-solid .fa-list}
::::
:::::
::::::
:::::::::
::::::::::

:::::: {#jb-print-docs-body .onlyprint}
# Distributed Communication

::::: {#print-main-content}
:::: {#jb-print-toc}
::: {}
## Contents
:::

- [Getting Started](#getting-started){.reference .internal .nav-link}
  - [Running Distributed
    Programs](#running-distributed-programs){.reference .internal
    .nav-link}
  - [Selecting Backend](#selecting-backend){.reference .internal
    .nav-link}
- [Distributed Program
  Examples](#distributed-program-examples){.reference .internal
  .nav-link}
- [Getting Started with Ring](#getting-started-with-ring){.reference
  .internal .nav-link}
  - [Defining a Ring](#defining-a-ring){.reference .internal .nav-link}
  - [Thunderbolt Ring](#thunderbolt-ring){.reference .internal
    .nav-link}
- [Getting Started with JACCL](#getting-started-with-jaccl){.reference
  .internal .nav-link}
  - [Enabling RDMA](#enabling-rdma){.reference .internal .nav-link}
  - [Defining a Mesh](#defining-a-mesh){.reference .internal .nav-link}
  - [Putting It All Together](#putting-it-all-together){.reference
    .internal .nav-link}
- [Getting Started with NCCL](#getting-started-with-nccl){.reference
  .internal .nav-link}
- [Getting Started with MPI](#getting-started-with-mpi){.reference
  .internal .nav-link}
  - [Installing MPI](#installing-mpi){.reference .internal .nav-link}
  - [Setting up Remote Hosts](#setting-up-remote-hosts){.reference
    .internal .nav-link}
  - [Tuning MPI All Reduce](#tuning-mpi-all-reduce){.reference .internal
    .nav-link}
- [Distributed Without [`mlx.launch`{.docutils .literal
  .notranslate}]{.pre}](#distributed-without-mlx-launch){.reference
  .internal .nav-link}
  - [Ring](#ring){.reference .internal .nav-link}
  - [JACCL](#jaccl){.reference .internal .nav-link}
  - [NCCL](#id1){.reference .internal .nav-link}
- [Tips and Tricks](#tips-and-tricks){.reference .internal .nav-link}
::::
:::::
::::::

::: {#searchbox}
:::

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: {#distributed-communication .section}
[]{#usage-distributed}

# Distributed Communication[\#](#distributed-communication "Link to this heading"){.headerlink}

MLX supports distributed communication operations that allow the
computational cost of training or inference to be shared across many
physical machines. At the moment we support several different
communication backends introduced below.

::: pst-scrollable-table-container
+---------------------------------------+--------------------------------------------------------+
| Backend                               | Description                                            |
+=======================================+========================================================+
| [[MPI]{.std                           | A full featured and mature distributed communications  |
| .std-ref}](#mpi-section){.reference   | library.                                               |
| .internal}                            |                                                        |
+---------------------------------------+--------------------------------------------------------+
| [[RING]{.std                          | Ring all reduce and all gather over TCP sockets.       |
| .std-ref}](#ring-section){.reference  | Always available and usually faster than MPI.          |
| .internal}                            |                                                        |
+---------------------------------------+--------------------------------------------------------+
| [[JACCL]{.std                         | Low latency communication with RDMA over thunderbolt.  |
| .std-ref}](#jaccl-section){.reference | Necessary for things like tensor parallelism.          |
| .internal}                            |                                                        |
+---------------------------------------+--------------------------------------------------------+
| [[NCCL]{.std                          | The backend of choice for CUDA environments.           |
| .std-ref}](#nccl-section){.reference  |                                                        |
| .internal}                            |                                                        |
+---------------------------------------+--------------------------------------------------------+
:::

The list of all currently supported operations and their documentation
can be seen in the [[API docs]{.std
.std-ref}](../python/distributed.html#distributed){.reference
.internal}.

:::::::::::::::: {#getting-started .section}
## Getting Started[\#](#getting-started "Link to this heading"){.headerlink}

A distributed program in MLX is as simple as:

:::: {.highlight-python .notranslate}
::: highlight
    import mlx.core as mx

    world = mx.distributed.init()
    x = mx.distributed.all_sum(mx.ones(10))
    print(world.rank(), x)
:::
::::

The program above sums the array [`mx.ones(10)`{.docutils .literal
.notranslate}]{.pre} across all distributed processes. However, when
this script is run with [`python`{.docutils .literal
.notranslate}]{.pre} only one process is launched and no distributed
communication takes place. Namely, all operations in
[`mx.distributed`{.docutils .literal .notranslate}]{.pre} are noops when
the distributed group has a size of one. This property allows us to
avoid code that checks if we are in a distributed setting similar to the
one below:

:::: {.highlight-python .notranslate}
::: highlight
    import mlx.core as mx

    x = ...
    world = mx.distributed.init()
    # No need for the check we can simply do x = mx.distributed.all_sum(x)
    if world.size() > 1:
        x = mx.distributed.all_sum(x)
:::
::::

::::::: {#running-distributed-programs .section}
### Running Distributed Programs[\#](#running-distributed-programs "Link to this heading"){.headerlink}

MLX provides [`mlx.launch`{.docutils .literal .notranslate}]{.pre} a
helper script to launch distributed programs. Continuing with our
initial example we can run it on localhost with 4 processes using

:::: {.highlight-shell .notranslate}
::: highlight
    $ mlx.launch -n 4 my_script.py
    3 array([4, 4, 4, ..., 4, 4, 4], dtype=float32)
    2 array([4, 4, 4, ..., 4, 4, 4], dtype=float32)
    1 array([4, 4, 4, ..., 4, 4, 4], dtype=float32)
    0 array([4, 4, 4, ..., 4, 4, 4], dtype=float32)
:::
::::

We can also run it on some remote hosts by providing their IPs (provided
that the script exists on all hosts and they are reachable by ssh)

:::: {.highlight-shell .notranslate}
::: highlight
    $ mlx.launch --hosts ip1,ip2,ip3,ip4 my_script.py
    3 array([4, 4, 4, ..., 4, 4, 4], dtype=float32)
    2 array([4, 4, 4, ..., 4, 4, 4], dtype=float32)
    1 array([4, 4, 4, ..., 4, 4, 4], dtype=float32)
    0 array([4, 4, 4, ..., 4, 4, 4], dtype=float32)
:::
::::

Consult the dedicated [[usage
guide]{.doc}](launching_distributed.html){.reference .internal} for more
information on using [`mlx.launch`{.docutils .literal
.notranslate}]{.pre}.
:::::::

:::::: {#selecting-backend .section}
### Selecting Backend[\#](#selecting-backend "Link to this heading"){.headerlink}

You can select the backend you want to use when calling [[`init()`{.xref
.py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.distributed.init.html#mlx.core.distributed.init "mlx.core.distributed.init"){.reference
.internal} by passing one of [`{'any',`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`'ring',`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`'jaccl',`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`'mpi',`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`'nccl'}`{.docutils .literal .notranslate}]{.pre}. When
passing [`any`{.docutils .literal .notranslate}]{.pre}, MLX will try all
available backends. If they all fail then a singleton group is created.

::: {.admonition .note}
Note

After a distributed backend is successfully initialized [[`init()`{.xref
.py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.distributed.init.html#mlx.core.distributed.init "mlx.core.distributed.init"){.reference
.internal} will return **the same backend** if called without arguments
or with backend set to [`any`{.docutils .literal .notranslate}]{.pre}.
:::

The following examples aim to clarify the backend initialization logic
in MLX:

:::: {.highlight-python .notranslate}
::: highlight
    # Case 1: Initialize MPI regardless if it was possible to initialize the ring backend
    world = mx.distributed.init(backend="mpi")
    world2 = mx.distributed.init()  # subsequent calls return the MPI backend!

    # Case 2: Initialize any backend
    world = mx.distributed.init(backend="any")  # equivalent to no arguments
    world2 = mx.distributed.init()  # same as above

    # Case 3: Initialize both backends at the same time
    world_mpi = mx.distributed.init(backend="mpi")
    world_ring = mx.distributed.init(backend="ring")
    world_any = mx.distributed.init()  # same as MPI because it was initialized first!
:::
::::
::::::
::::::::::::::::

::: {#distributed-program-examples .section}
## Distributed Program Examples[\#](#distributed-program-examples "Link to this heading"){.headerlink}

- [[Data Parallelism]{.std
  .std-ref}](../examples/data_parallelism.html#data-parallelism){.reference
  .internal}

- [[Tensor Parallelism]{.std
  .std-ref}](../examples/tensor_parallelism.html#tensor-parallelism){.reference
  .internal}
:::

::::::::: {#getting-started-with-ring .section}
[]{#ring-section}

## Getting Started with Ring[\#](#getting-started-with-ring "Link to this heading"){.headerlink}

The ring backend does not depend on any third party library so it is
always available. It uses TCP sockets so the nodes need to be reachable
via a network. As the name suggests the nodes are connected in a ring
which means that rank 1 can only communicate with rank 0 and rank 2,
rank 2 only with rank 1 and rank 3 and so on and so forth. As a result
[[`send()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.distributed.send.html#mlx.core.distributed.send "mlx.core.distributed.send"){.reference
.internal} and [[`recv()`{.xref .py .py-func .docutils .literal
.notranslate}]{.pre}](../python/_autosummary/mlx.core.distributed.recv.html#mlx.core.distributed.recv "mlx.core.distributed.recv"){.reference
.internal} with arbitrary sender and receiver are not supported in the
ring backend.

::::: {#defining-a-ring .section}
### Defining a Ring[\#](#defining-a-ring "Link to this heading"){.headerlink}

The easiest way to define and use a ring is via a JSON hostfile and the
[`mlx.launch`{.docutils .literal .notranslate}]{.pre} [[helper
script]{.doc}](launching_distributed.html){.reference .internal}. For
each node one defines a hostname to ssh into to run commands on this
node and one or more IPs that this node will listen to for connections.

For example the hostfile below defines a 4 node ring.
[`hostname1`{.docutils .literal .notranslate}]{.pre} will be rank 0,
[`hostname2`{.docutils .literal .notranslate}]{.pre} rank 1 etc.

:::: {.highlight-json .notranslate}
::: highlight
    [
        {"ssh": "hostname1", "ips": ["123.123.123.1"]},
        {"ssh": "hostname2", "ips": ["123.123.123.2"]},
        {"ssh": "hostname3", "ips": ["123.123.123.3"]},
        {"ssh": "hostname4", "ips": ["123.123.123.4"]}
    ]
:::
::::

Running [`mlx.launch`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`--hostfile`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`ring-4.json`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`my_script.py`{.docutils .literal .notranslate}]{.pre}
will ssh into each node, run the script which will listen for
connections in each of the provided IPs. Specifically,
[`hostname1`{.docutils .literal .notranslate}]{.pre} will connect to
[`123.123.123.2`{.docutils .literal .notranslate}]{.pre} and accept a
connection from [`123.123.123.4`{.docutils .literal .notranslate}]{.pre}
and so on and so forth.
:::::

::::: {#thunderbolt-ring .section}
### Thunderbolt Ring[\#](#thunderbolt-ring "Link to this heading"){.headerlink}

Although the ring backend can have benefits over MPI even for Ethernet,
its main purpose is to use Thunderbolt rings for higher bandwidth
communication. Setting up such thunderbolt rings can be done manually,
but is a relatively tedious process. To simplify this, we provide the
utility [`mlx.distributed_config`{.docutils .literal
.notranslate}]{.pre}.

To use [`mlx.distributed_config`{.docutils .literal .notranslate}]{.pre}
your computers need to be accessible by ssh via Ethernet or Wi-Fi.
Subsequently, connect them via thunderbolt cables and then call the
utility as follows:

:::: {.highlight-shell .notranslate}
::: highlight
    mlx.distributed_config --verbose --hosts host1,host2,host3,host4 --backend ring
:::
::::

By default the script will attempt to discover the thunderbolt ring and
provide you with the commands to configure each node as well as the
[`hostfile.json`{.docutils .literal .notranslate}]{.pre} to use with
[`mlx.launch`{.docutils .literal .notranslate}]{.pre}. If password-less
[`sudo`{.docutils .literal .notranslate}]{.pre} is available on the
nodes then [`--auto-setup`{.docutils .literal .notranslate}]{.pre} can
be used to configure them automatically.

If you want to go through the process manually, the steps are as
follows:

- Disable the thunderbolt bridge interface

- For the cable connecting rank [`i`{.docutils .literal
  .notranslate}]{.pre} to rank [`i`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils
  .literal .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`1`{.docutils .literal .notranslate}]{.pre} find the
  interfaces corresponding to that cable in nodes [`i`{.docutils
  .literal .notranslate}]{.pre} and [`i`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils
  .literal .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`1`{.docutils .literal .notranslate}]{.pre}.

- Set up a unique subnetwork connecting the two nodes for the
  corresponding interfaces. For instance if the cable corresponds to
  [`en2`{.docutils .literal .notranslate}]{.pre} on node [`i`{.docutils
  .literal .notranslate}]{.pre} and [`en2`{.docutils .literal
  .notranslate}]{.pre} also on node [`i`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal .notranslate}[`+`{.docutils
  .literal .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`1`{.docutils .literal .notranslate}]{.pre} then we may
  assign IPs [`192.168.0.1`{.docutils .literal .notranslate}]{.pre} and
  [`192.168.0.2`{.docutils .literal .notranslate}]{.pre} respectively to
  the two nodes. For more details you can see the commands prepared by
  the utility script.
:::::
:::::::::

::::::::::::::::::::: {#getting-started-with-jaccl .section}
[]{#jaccl-section}

## Getting Started with JACCL[\#](#getting-started-with-jaccl "Link to this heading"){.headerlink}

Starting from macOS 26.2, RDMA over thunderbolt is available and enables
low-latency communication between Macs with thunderbolt 5. MLX provides
the JACCL backend that uses this functionality to achieve communication
latency an order of magnitude lower than the ring backend.

::: {.admonition .note}
Note

The name JACCL (pronounced Jackal) stands for *Jack and Angelos'
Collective Communication Library* and it is an obvious pun to Nvidia's
NCCL but also tribute to *Jack Beasley* who led the development of RDMA
over Thunderbolt at Apple.
:::

::::: {#enabling-rdma .section}
### Enabling RDMA[\#](#enabling-rdma "Link to this heading"){.headerlink}

Until the feature matures, enabling RDMA over thunderbolt is slightly
more involved and **cannot** be done remotely even with sudo. In fact,
it has to be done in macOS recovery:

1.  [Start your computer in
    recovery](https://support.apple.com/en-us/102518){.reference
    .external}.

2.  Open the Terminal by going to Utilities -\> Terminal.

3.  Run [`rdma_ctl`{.docutils .literal .notranslate}]{.pre}` `{.docutils
    .literal .notranslate}[`enable`{.docutils .literal
    .notranslate}]{.pre}.

4.  Reboot.

To verify that you have successfully enabled Thunderbolt RDMA you can
run [`ibv_devices`{.docutils .literal .notranslate}]{.pre} which should
produce something like the following for an M3 Ultra.

:::: {.highlight-bash .notranslate}
::: highlight
    ~ % ibv_devices
    device                 node GUID
    ------              ----------------
    rdma_en2            8096a9d9edbaac05
    rdma_en3            8196a9d9edbaac05
    rdma_en5            8396a9d9edbaac05
    rdma_en4            8296a9d9edbaac05
    rdma_en6            8496a9d9edbaac05
    rdma_en7            8596a9d9edbaac05
:::
::::
:::::

:::::::: {#defining-a-mesh .section}
### Defining a Mesh[\#](#defining-a-mesh "Link to this heading"){.headerlink}

The JACCL backend supports only fully connected topologies. Namely,
there needs to be a thunderbolt cable connecting all pairs of Macs
directly. For example, in the following topology visualizations, the
left one is valid because there is a connection from any node to any
other node, while for the one on the right M3 Ultra 1 is not connected
to M3 Ultra 2.

::::: {style="display: flex; text-align: center; align-items: end; font-size: 80%;"}
::: {}
![M3 Ultra thunderbolt
mesh](../_static/distributed/m3-ultra-mesh.png){style="width: 55%"}

Fully connected mesh of four M3 Ultra.
:::

::: {}
![M3 Ultra broken thunderbolt
mesh](../_static/distributed/m3-ultra-mesh-broken.png){style="width: 55%"}

Not a valid mesh (M3 Ultra 1 is not connected to M3 Ultra 2).
:::
:::::

Similar to the ring backend, the easiest way to use JACCL with MLX is to
write a JSON hostfile that will be used by [`mlx.launch`{.docutils
.literal .notranslate}]{.pre}. The hostfile needs to contain

- Hostnames to use for launching scripts via ssh

- An IP for rank 0 that is reachable by all nodes

- A list of rdma devices that connect each node to each other node

The following JSON defines the valid 4-node mesh from the image above.

:::: {.highlight-json .notranslate}
::: highlight
    [
        {
            "ssh": "m3-ultra-1",
            "ips": ["123.123.123.1"],
            "rdma": [null, "rdma_en5", "rdma_en4", "rdma_en3"]
        },
        {
            "ssh": "m3-ultra-2",
            "ips": [],
            "rdma": ["rdma_en5", null, "rdma_en3", "rdma_en4"]
        },
        {
            "ssh": "m3-ultra-3",
            "ips": [],
            "rdma": ["rdma_en4", "rdma_en3", null, "rdma_en5"]
        },
        {
            "ssh": "m3-ultra-4",
            "ips": [],
            "rdma": ["rdma_en3", "rdma_en4", "rdma_en5", null]
        }
    ]
:::
::::

Even though TCP/IP is not used when communicating with Thunderbolt RDMA,
disabling the thunderbolt bridge is still required as well as setting up
isolated local networks for each thunderbolt connection.

All of the above can be done instead via
[`mlx.distributed_config`{.docutils .literal .notranslate}]{.pre}. This
helper script will

- ssh into each node

- extract the thunderbolt connectivity

- check for a valid mesh

- provide the commands to configure each node (or run them if sudo is
  available)

- generate the hostfile to be used with [`mlx.launch`{.docutils .literal
  .notranslate}]{.pre}
::::::::

:::::::::: {#putting-it-all-together .section}
### Putting It All Together[\#](#putting-it-all-together "Link to this heading"){.headerlink}

For example launching a distributed MLX script that uses JACCL is fairly
simple if the nodes are reachable via ssh and have password-less sudo.

First, connect all the thunderbolt cables. Then we can verify the
connections by using the [`mlx.distributed_config`{.docutils .literal
.notranslate}]{.pre} script to visualize them.

:::: {.highlight-python .notranslate}
::: highlight
    mlx.distributed_config --verbose \
         --hosts m3-ultra-1,m3-ultra-2,m3-ultra-3,m3-ultra-4 \
         --over thunderbolt --dot | dot -Tpng | open -f -a Preview
:::
::::

After making sure that everything looks right we can auto-configure the
nodes and save the hostfile to [`m3-ultra-jaccl.json`{.docutils .literal
.notranslate}]{.pre} by running:

:::: {.highlight-python .notranslate}
::: highlight
    mlx.distributed_config --verbose \
         --hosts m3-ultra-1,m3-ultra-2,m3-ultra-3,m3-ultra-4 \
         --over thunderbolt --backend jaccl \
         --auto-setup --output m3-ultra-jaccl.json
:::
::::

And now we are ready to run a distributed MLX script such as distributed
inference of a gigantic model using MLX LM.

:::: {.highlight-python .notranslate}
::: highlight
    mlx.launch --verbose --backend jaccl --hostfile m3-ultra-jaccl.json \
         --env MLX_METAL_FAST_SYNCH=1 -- \  # <--- important
         /path/to/remote/python -m mlx_lm chat --model mlx-community/DeepSeek-R1-0528-4bit
:::
::::

::: {.admonition .note}
Note

Defining the environment variable [`MLX_METAL_FAST_SYNCH=1`{.docutils
.literal .notranslate}]{.pre} enables a different, faster way of
synchronizing between the GPU and the CPU. It is not specific to the
JACCL backend and can be used in all cases where the CPU and GPU need to
collaborate for some computation and is pretty critical for low-latency
communication since the communication is done by the CPU.
:::
::::::::::
:::::::::::::::::::::

::::::: {#getting-started-with-nccl .section}
[]{#nccl-section}

## Getting Started with NCCL[\#](#getting-started-with-nccl "Link to this heading"){.headerlink}

MLX on CUDA environments ships with the ability to talk to
[NCCL](https://developer.nvidia.com/nccl){.reference .external} which is
a high-performance collective communication library that supports both
multi-gpu and multi-node setups.

For CUDA environments, NCCL is the default backend for
[`mlx.launch`{.docutils .literal .notranslate}]{.pre} and all it takes
to run a distributed job is

:::: {.highlight-python .notranslate}
::: highlight
    mlx.launch -n 8 test.py

    # perfect for interactive scripts
    mlx.launch -n 8 python -m mlx_lm chat --model my-model
:::
::::

You can also use [`mlx.launch`{.docutils .literal .notranslate}]{.pre}
to ssh to a remote node and launch a script with the same ease

:::: {.highlight-python .notranslate}
::: highlight
    mlx.launch --hosts my-cuda-node -n 8 test.py
:::
::::

In many cases you may not want to use [`mlx.launch`{.docutils .literal
.notranslate}]{.pre} with the NCCL backend because the cluster scheduler
will be the one launching the processes. You can [[see which environment
variables need to be defined]{.std .std-ref}](#no-mlx-launch){.reference
.internal} in order for the MLX NCCL backend to be initialized
correctly.
:::::::

::::::::::::: {#getting-started-with-mpi .section}
[]{#mpi-section}

## Getting Started with MPI[\#](#getting-started-with-mpi "Link to this heading"){.headerlink}

MLX already comes with the ability to "talk" to
[MPI](https://en.wikipedia.org/wiki/Message_Passing_Interface){.reference
.external} if it is installed on the machine. Launching distributed MLX
programs that use MPI can be done with [`mpirun`{.docutils .literal
.notranslate}]{.pre} as expected. However, in the following examples we
will be using [`mlx.launch`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`--backend`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`mpi`{.docutils
.literal .notranslate}]{.pre} which takes care of some nuisances such as
setting absolute paths for the [`mpirun`{.docutils .literal
.notranslate}]{.pre} executable and the [`libmpi.dyld`{.docutils
.literal .notranslate}]{.pre} shared library.

The simplest possible usage is the following which, assuming the minimal
example in the beginning of this page, should result in:

:::: {.highlight-shell .notranslate}
::: highlight
    $ mlx.launch --backend mpi -n 2 test.py
    1 array([2, 2, 2, ..., 2, 2, 2], dtype=float32)
    0 array([2, 2, 2, ..., 2, 2, 2], dtype=float32)
:::
::::

The above launches two processes on the same (local) machine and we can
see both standard output streams. The processes send the array of 1s to
each other and compute the sum which is printed. Launching with
[`mlx.launch`{.docutils .literal .notranslate}]{.pre}` `{.docutils
.literal .notranslate}[`-n`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`4`{.docutils
.literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`...`{.docutils .literal .notranslate}]{.pre} would print
4 etc.

::::::: {#installing-mpi .section}
### Installing MPI[\#](#installing-mpi "Link to this heading"){.headerlink}

MPI can be installed with Homebrew, pip, using the Anaconda package
manager, or compiled from source. Most of our testing is done using
[`openmpi`{.docutils .literal .notranslate}]{.pre} installed with the
Anaconda package manager as follows:

:::: {.highlight-shell .notranslate}
::: highlight
    $ conda install conda-forge::openmpi
:::
::::

Installing with Homebrew or pip requires specifying the location of
[`libmpi.dyld`{.docutils .literal .notranslate}]{.pre} so that MLX can
find it and load it at runtime. This can simply be achieved by passing
the [`DYLD_LIBRARY_PATH`{.docutils .literal .notranslate}]{.pre}
environment variable to [`mpirun`{.docutils .literal
.notranslate}]{.pre} and it is done automatically by
[`mlx.launch`{.docutils .literal .notranslate}]{.pre}. Some environments
use a non-standard library filename that can be specified using the
[`MPI_LIBNAME`{.docutils .literal .notranslate}]{.pre} environment
variable. This is automatically taken care of by [`mlx.launch`{.docutils
.literal .notranslate}]{.pre} as well.

:::: {.highlight-shell .notranslate}
::: highlight
    $ mpirun -np 2 -x DYLD_LIBRARY_PATH=/opt/homebrew/lib/ -x MPI_LIBNAME=libmpi.40.dylib python test.py
    $ # or simply
    $ mlx.launch -n 2 test.py
:::
::::
:::::::

::: {#setting-up-remote-hosts .section}
### Setting up Remote Hosts[\#](#setting-up-remote-hosts "Link to this heading"){.headerlink}

MPI can automatically connect to remote hosts and set up the
communication over the network if the remote hosts can be accessed via
ssh. A good checklist to debug connectivity issues is the following:

- [`ssh`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`hostname`{.docutils .literal .notranslate}]{.pre} works
  from all machines to all machines without asking for password or host
  confirmation

- [`mpirun`{.docutils .literal .notranslate}]{.pre} is accessible on all
  machines.

- Ensure that the [`hostname`{.docutils .literal .notranslate}]{.pre}
  used by MPI is the one that you have configured in the
  [`.ssh/config`{.docutils .literal .notranslate}]{.pre} files on all
  machines.
:::

:::: {#tuning-mpi-all-reduce .section}
### Tuning MPI All Reduce[\#](#tuning-mpi-all-reduce "Link to this heading"){.headerlink}

::: {.admonition .note}
Note

For faster all reduce consider using the ring backend either with
Thunderbolt connections or over Ethernet.
:::

Configure MPI to use N tcp connections between each host to improve
bandwidth by passing [`--mca`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`btl_tcp_links`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal .notranslate}[`N`{.docutils
.literal .notranslate}]{.pre}.

Force MPI to use the most performant network interface by setting
[`--mca`{.docutils .literal .notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`btl_tcp_if_include`{.docutils .literal
.notranslate}]{.pre}` `{.docutils .literal
.notranslate}[`<iface>`{.docutils .literal .notranslate}]{.pre} where
[`<iface>`{.docutils .literal .notranslate}]{.pre} should be the
interface you want to use.
::::
:::::::::::::

:::::::::: {#distributed-without-mlx-launch .section}
[]{#no-mlx-launch}

## Distributed Without [`mlx.launch`{.docutils .literal .notranslate}]{.pre}[\#](#distributed-without-mlx-launch "Link to this heading"){.headerlink}

None of the implementations of the distributed backends require
launching with [`mlx.launch`{.docutils .literal .notranslate}]{.pre}.
The script simply connects to each host. Starts a process per rank and
sets up the necessary environment variables before delegating to your
MLX script. See the [[dedicated documentation
page]{.doc}](launching_distributed.html){.reference .internal} for more
details.

For many use-cases this will be the easiest way to perform distributed
computations in MLX. However, there may be reasons that you cannot or
should not use [`mlx.launch`{.docutils .literal .notranslate}]{.pre}. A
common such case is the use of a scheduler that starts all the processes
for you on machines undetermined at the time of scheduling the job.

Below we list the environment variables required to use each backend.

::::: {#ring .section}
### Ring[\#](#ring "Link to this heading"){.headerlink}

**MLX_RANK** should contain a single 0-based integer that defines the
rank of the process.

**MLX_HOSTFILE** should contain the path to a json file that contains
IPs and ports for each rank to listen to, something like the following:

:::: {.highlight-json .notranslate}
::: highlight
    [
      ["123.123.1.1:5000", "123.123.1.2:5000"],
      ["123.123.2.1:5000", "123.123.2.2:5000"],
      ["123.123.3.1:5000", "123.123.3.2:5000"],
      ["123.123.4.1:5000", "123.123.4.2:5000"]
    ]
:::
::::

**MLX_RING_VERBOSE** is optional and if set to 1 it enables some more
logging from the distributed backend.
:::::

::::: {#jaccl .section}
### JACCL[\#](#jaccl "Link to this heading"){.headerlink}

**MLX_RANK** should contain a single 0-based integer that defines the
rank of the process.

**MLX_JACCL_COORDINATOR** should contain the IP and port that rank 0 can
listen to all the other ranks connect to in order to establish the RDMA
connections.

**MLX_IBV_DEVICES** should contain the path to a json file that contains
the ibverbs device names that connect each node to each other node,
something like the following:

:::: {.highlight-json .notranslate}
::: highlight
    [
       [null, "rdma_en5", "rdma_en4", "rdma_en3"],
       ["rdma_en5", null, "rdma_en3", "rdma_en4"],
       ["rdma_en4", "rdma_en3", null, "rdma_en5"],
       ["rdma_en3", "rdma_en4", "rdma_en5", null]
    ]
:::
::::
:::::

::: {#id1 .section}
### NCCL[\#](#id1 "Link to this heading"){.headerlink}

**MLX_RANK** should contain a single 0-based integer that defines the
rank of the process.

**MLX_WORLD_SIZE** should contain the total number of processes that
will be launched.

**NCCL_HOST_IP** and **NCCL_PORT** should contain the IP and port that
all hosts can connect to to establish the NCCL communication.

**CUDA_VISIBLE_DEVICES** should contain the local index of the gpu that
corresponds to this process.

Of course any [other environment
variable](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html){.reference
.external} that is used by NCCL can be set.
:::
::::::::::

::: {#tips-and-tricks .section}
[]{#id2}

## Tips and Tricks[\#](#tips-and-tricks "Link to this heading"){.headerlink}

This is a small collection of tips to help you utilize better the
distributed communication capabilities of MLX.

- *Test locally first.*

  You can use the pattern [`mlx.launch`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`-n2`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`--`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`my_script.py`{.docutils .literal .notranslate}]{.pre}
  to run a small scale test on a single node first.

- *Batch your communication.*

  As described in the [[training example]{.std
  .std-ref}](../examples/data_parallelism.html#training-example){.reference
  .internal}, performing a lot of small communications can hurt
  performance. Copy the approach of [[`mlx.nn.average_gradients()`{.xref
  .py .py-func .docutils .literal
  .notranslate}]{.pre}](../python/_autosummary/mlx.nn.average_gradients.html#mlx.nn.average_gradients "mlx.nn.average_gradients"){.reference
  .internal} to gather many small communications in a single large one.

- *Visualize the connectivity.*

  Use [`mlx.distributed_config`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`--hosts`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`h1,h2,h3`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`--over`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`thunderbolt`{.docutils .literal
  .notranslate}]{.pre}` `{.docutils .literal
  .notranslate}[`--dot`{.docutils .literal .notranslate}]{.pre} to
  visualize the connnections and make sure that the cables are connected
  correctly. See the [[JACCL section]{.std
  .std-ref}](#jaccl-section){.reference .internal} for examples.

- *Use the debugger.*

  [`mlx.launch`{.docutils .literal .notranslate}]{.pre} is meant for
  interactive use. It broadcasts stdin to all processes and gathers
  stdout from all processes. This makes using [`pdb`{.docutils .literal
  .notranslate}]{.pre} a breeze.
:::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::: prev-next-area
[](numpy.html "previous page"){.left-prev}

::: prev-next-info
previous

Conversion to NumPy and Other Frameworks
:::

[](using_streams.html "next page"){.right-next}

::: prev-next-info
next

Using Streams
:::
:::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

:::::: {#pst-secondary-sidebar .bd-sidebar-secondary .bd-toc}
::::: {.sidebar-secondary-items .sidebar-secondary__inner}
:::: sidebar-secondary-item
::: {#pst-page-navigation-heading-2 .page-toc .tocsection .onthispage}
Contents
:::

- [Getting Started](#getting-started){.reference .internal .nav-link}
  - [Running Distributed
    Programs](#running-distributed-programs){.reference .internal
    .nav-link}
  - [Selecting Backend](#selecting-backend){.reference .internal
    .nav-link}
- [Distributed Program
  Examples](#distributed-program-examples){.reference .internal
  .nav-link}
- [Getting Started with Ring](#getting-started-with-ring){.reference
  .internal .nav-link}
  - [Defining a Ring](#defining-a-ring){.reference .internal .nav-link}
  - [Thunderbolt Ring](#thunderbolt-ring){.reference .internal
    .nav-link}
- [Getting Started with JACCL](#getting-started-with-jaccl){.reference
  .internal .nav-link}
  - [Enabling RDMA](#enabling-rdma){.reference .internal .nav-link}
  - [Defining a Mesh](#defining-a-mesh){.reference .internal .nav-link}
  - [Putting It All Together](#putting-it-all-together){.reference
    .internal .nav-link}
- [Getting Started with NCCL](#getting-started-with-nccl){.reference
  .internal .nav-link}
- [Getting Started with MPI](#getting-started-with-mpi){.reference
  .internal .nav-link}
  - [Installing MPI](#installing-mpi){.reference .internal .nav-link}
  - [Setting up Remote Hosts](#setting-up-remote-hosts){.reference
    .internal .nav-link}
  - [Tuning MPI All Reduce](#tuning-mpi-all-reduce){.reference .internal
    .nav-link}
- [Distributed Without [`mlx.launch`{.docutils .literal
  .notranslate}]{.pre}](#distributed-without-mlx-launch){.reference
  .internal .nav-link}
  - [Ring](#ring){.reference .internal .nav-link}
  - [JACCL](#jaccl){.reference .internal .nav-link}
  - [NCCL](#id1){.reference .internal .nav-link}
- [Tips and Tricks](#tips-and-tricks){.reference .internal .nav-link}
::::
:::::
::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

::::::: {.bd-footer-content__inner .container}
::: footer-item
By MLX Contributors
:::

::: footer-item
© Copyright 2023, Apple.\
:::

::: footer-item
:::

::: footer-item
:::
:::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
