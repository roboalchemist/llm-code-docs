# Source: https://docs.salad.com/container-engine/explanation/infrastructure-platform/health-probes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Health Probes

*Last Updated: October 30, 2024*

# Overview

Health probes provide an automated way for SaladCloud users to trigger certain actions based on the status of the
containers in a container group deployment. SCE supports three types of probes: Startup, Liveness, and Readiness probes.

These probes run for each container deployed in the container group. If configured, the Startup probe runs first, and
the Liveness/Readiness probes (if configured) are suspended until after the Startup probe is successful.

> ⚠️ Caution
>
> Health probes can be extremely useful for catching deadlocks in an application, recovering from errors during
> container initialization, and ensuring local resources are available before exposing nodes via the Container Gateway.
>
> However, misconfigured health probes can easily cause unnecessary termination of containers, leading to slower
> deployment and less reliable application uptime. It is important to first understand the normal behavior of your own
> containers on SaladCloud in order to minimize false positives when configuring health probes.

# Probe Protocols

Salad Container Engine (SCE) supports four probe protocols: `exec`,` TCP`, `gRPC`, and` HTTP/1.X`. These protocols
provide a way to check the health of containers and trigger actions based on the results of the probes.

## `Exec Protocol`

The exec protocol executes a command inside the container and checks the exit code. If the exit code is zero, the probe
is considered successful. If the exit code is non-zero, the probe is considered a failure.

Parameters for this protocol include:

* **Command :** The command to be executed within the container.
  * *Example:* Command : `cat`and argument `/etc/hostname`

## `TCP Protocol`

The TCP probe checks whether a TCP port inside the container is open and ready to accept the traffic. The probe sends a
SYN packet to the port and checks the response code. If the response code indicates that the port is open, the probe is
considered successful.

Note that using TCP probes without a Container Gateway enabled may result in unexpected behavior.

Parameters for this protocol include:

* **Port:** The port number for the TCP connection (between 1 to 65535).
  * *Example:* `8080`

## `gRPC Protocol`

The gRPC probe checks the health of a gRPC service running inside the container. The probe sends a request to the
service and checks the response code. Parameters for this protocol include:

* **Service:** The service field used to distinguish between different types of probes or features.
  * *Example:* `"liveness"` service field in gRPC allows you to differentiate between probes of different types or for
    different features.
* **Port:** The port number for the gRPC connection (between 1 to 65535).
  * *Example:* `50051`

## `HTTP/1.X Protocol`

The HTTP/1.X probe checks the health of an HTTP service running inside the container. The probe sends an HTTP GET
request and checks the response code.

Parameters for this protocol include:

* **Path**: The path for the HTTP request.
  * *Example*: `/healthz`
* **Port**: The port number for the HTTP connection (between 1 to 65535).
  * *Example*: `80`

## Common Probe Protocol Parameters

* `Initial Delay Seconds`: Number of seconds after the container starts before probes are initiated.
* `Period Seconds`: How often (in seconds) to perform the probe.
* `Timeout Seconds`: Number of seconds after which the probe times out.
* `Success Threshold`: Minimum consecutive successes for the probe to be considered successful.
* `Failure Threshold`: Number of consecutive failures of the probe before the container is reallocated.

# Probe States

Each probe can be in 1 of 3 states:

* `Unknown`- The container is neither in a success or failure state yet. Causes no change to the system.
* `Success` - The probe has met the `successThreshold` and has not yet failed.
* `Failure` - The container failed the diagnostic. In the case of a failed Startup or Liveness probe, the container will
  be automatically reallocated to a new node. In the case of a failed Readiness probe, the container will continue to
  run on the node, but no networking traffic will be routed to it.

# Probe Timing

## Startup Probe

### Successful Startup Probe

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5abc4db02f375ea8a7fd8c62282d7cb6" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/startup-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b4fde9a2c1ab848c8e91ebe2fe5a6fdd 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1dbf1039f3bccfb8537fced2e3254761 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=f5545b764cad2cef89f32144799b2a27 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=2beedb87e16c2b3d4d57bc4c3b7ff237 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ed95e848f66445e9989a0e48fef22cf0 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=473906d3ee36338cd24fa511f41438f5 2500w" />

### Failed Startup Probe

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b0f17053349bdf0303f331e853a6204d" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/startup-failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=39afa691c64678b699d249bd3c4aae2f 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=423a01e8190a445695d8e54478d53fc0 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=2f1707e2b34a4de5e5e9f983a6cedb2f 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=45eecb9153599ff4ea3418832c0e749a 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c314606bbc54a62e5233676501555b37 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e6da7697252966bbea94e0b409adbd74 2500w" />

## Liveness Probe

### Successful Liveness Probe

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=17bc3df45d4143c26e353b734a23f0d2" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/liveness-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=6ff6ed9357815440eec898f0ca79ce15 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=3bfdd20e11e3a5f37a8d0ca2417858c0 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=c630cb4b3f4e2e50558fed839b4d6e55 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=fe55e61b2a349d0bfeb8d72fb2613c1f 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=5c1e5ab336fb224d3b70e2f9a7149c68 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=4bfadbd5ef7f6de4811784a787bf300f 2500w" />

### Failed Liveness Probe

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=1318ba39d2101ed92fd565ed2a2f269c" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/liveness-failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=0fdfc043ae759ff17d5d73074210a0d7 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=81013b6f62997ba9d00fb4c5bc5bab38 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=6020fd7c19fa6f0227046c73091b9de1 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=835240251829a2eb27e9be609bea0ca3 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=46ad9200815505966499d22e8bf3ab45 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=e9d2ba6d6696a8be1522629b9791becf 2500w" />

## Readiness Probe

### Successful Readiness Probe

<br />

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=952d31cbda9b336b07fe2a7249bb770b" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/readiness-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=6ddf409668c4fb87dba5501bd4a49264 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9e935ae3ccdd13dbf1737612ef041de0 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=044da92acfbdfa6c9410c053d810dbf0 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=8bfcb5b04c5bd77009d7b5e21a464b50 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e70209c2f378f5cc03f6af59c64c2fd4 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=630887132796b6756b56b7a0f0ae7296 2500w" />

### Failed Readiness Probe

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=69c6f8b248a78903bf184769d4dcd111" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/readiness-failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=973acf53bd7e76bbce9bbc17caf516ff 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=a17cfc2831a3c44e7e2f4d9c60c4a644 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9663d302eddcea9eb9980f98495f0ef9 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b6838fb816be4126b5f7429157877e1a 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ce122b58715b62ff4f376100c24d36bb 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3d82dbc7ea04f0189465612f09036632 2500w" />

<br />

<br />

# Enabling Health Probes

Each of these probes can be configured from the container group configuration page by clicking the edit button beside
each probe section.

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-probes.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=4e27e4d1cd0a0d0cc52545f7a75a317d" data-og-width="1870" width="1870" data-og-height="1416" height="1416" data-path="container-engine/images/portal-edit-probes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-probes.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=4ca13c361bc605e537ace32a111edd02 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-probes.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=e2c5d3f878947b95cb8a318d5e0efc11 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-probes.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=e84b1acb9c358977a75966d5262bcc29 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-probes.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=ace1036a7c12436776ebe8f52700d560 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-probes.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=738229826972d3e40f54a8ba2d5fa81a 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/portal-edit-probes.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=ce496e441a7b046a7b6849d1ea1b3a16 2500w" />

# Probe Configuration

SaladCloud provides comprehensive protocol support, including `exec`, `gRPC`, `TCP`, and `HTTP`.

To perform a probe, SaladCloud executes the command you specify in the target container. To configure a command, press
the Edit link as shown below.

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-edit-command.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=3d4272a6d8f95974aeed7f0a04532262" data-og-width="946" width="946" data-og-height="712" height="712" data-path="container-engine/images/startup-exec-edit-command.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-edit-command.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=cc06e7be28ca9cca32a8cc9c201ab09b 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-edit-command.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=8ce769e198eae6cfac5a2b2b81b78c32 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-edit-command.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=9338ff35fe00bc6ee8107b3602274d9b 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-edit-command.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=dd4d6d2187d2225083a60d035a5cb943 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-edit-command.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=2d8867bb30f2992a8d2b5c3f6b29974e 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-edit-command.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e61c2a0b59ca31e47767607b90949c5e 2500w" />

Configure the command and any additional arguments. In this example, the container will attempt to read a file located
at `/tmp/healthy` exactly `Initial Delay Seconds` after startup. If it successfully executes the command within
`Timeout Seconds`, the probe returns an exit code 0. Once this has happened `Success Threshold` times, the Startup probe
is 'done' and the Liveness and Readiness probes (if configured) are initiated.

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-config-command.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=d1bcbd02aae1990d49fad3a57adcde64" data-og-width="422" width="422" data-og-height="574" height="574" data-path="container-engine/images/startup-exec-config-command.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-config-command.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=f893ef093140514bb9c8d1d5746f2dee 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-config-command.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=cb33499b20ac1211ac9084ff7818299b 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-config-command.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e777e151dfaf4f9832d906b136ee081d 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-config-command.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1064988f42223492f7502ecb095e2eb7 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-config-command.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=bb9c13a2d4dfcadd4354ce69d185c694 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-exec-config-command.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=06b6235b6d5fcc880e5fd26ead3d1f72 2500w" />

## Standard Probe Properties

All probes (Startup, Liveness, and Readiness) share the following properties.

| Property                  | Type (Min, Max)      | Details                                                                                                                                                                                                                                              |
| :------------------------ | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Initial Delay Seconds** | Integer (0 - 10,000) | The number of seconds after the container has started before the probe is initiated. If a Startup probe is configured, the initial delay for Liveness and Readiness probes begins counting when the Startup probe has reached the success threshold. |
| **Period Seconds**        | Integer (1 - 10,000) | How often, in seconds, to perform the probe.                                                                                                                                                                                                         |
| **Timeout Seconds**       | Integer (1 - 10,000) | After a probe initiates, the number of seconds to wait for a successful response before timing out (failing).                                                                                                                                        |
| **Success Threshold**     | Integer (1 - 10,000) | The minimum consecutive successes for the probe to return a 0 (success) for the probe to be considered successful.                                                                                                                                   |
| **Failure Threshold**     | Integer (1 - 10,000) | The number of consecutive failures of the probe before the container is reallocated (in the case of Startup and Liveness probes) or Container Gateway (networking) is disabled (in the case of Readiness probes).                                    |

# Further Reading

In SCE, the Startup, Liveness, and Readiness probes were designed based on the Kubernetes specifications. For additional
information on how probes work under the hood, as well as excellent examples of configured probes and common pitfalls,
check out the Kubernetes documentation on
[configuring probes ](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/)and
[when to use each one](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/).

[Health Probe Deep Dive](https://cloud.redhat.com/blog/liveness-and-readiness-probes)
