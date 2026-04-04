# Source: https://docs.salad.com/container-engine/explanation/infrastructure-platform/readiness-probes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Readiness Probes

*Last Updated: October 15, 2024*

# Overview

Readiness probes are only available if
[Container Gateway](/container-engine/explanation/infrastructure-platform/networking) or
[Job Queues](/container-engine/explanation/job-processing/job-queues) are turned on. They run after the startup probe
has completed successfully. They are typically used to evaluate whether the application running in your container is
ready to accept traffic. If configured, no traffic will be sent from the load balancer until the readiness probe has
passed, so prevent your readiness probe from passing until you have downloaded and warmed up your models. Readiness
probes can flap back between passing and failing. If a container's readiness probe reaches the failure state, the
container will continue to run on the node but the load balancer will not route any networking traffic. Readiness probe
configuration should be fairly strict in order to get that signal out as fast as possible so requests get routed to
other nodes.

<br />

## Successful Readiness Probe

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=952d31cbda9b336b07fe2a7249bb770b" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/readiness-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=6ddf409668c4fb87dba5501bd4a49264 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9e935ae3ccdd13dbf1737612ef041de0 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=044da92acfbdfa6c9410c053d810dbf0 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=8bfcb5b04c5bd77009d7b5e21a464b50 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e70209c2f378f5cc03f6af59c64c2fd4 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-success.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=630887132796b6756b56b7a0f0ae7296 2500w" />

<br />

## Failed Readiness Probe

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=69c6f8b248a78903bf184769d4dcd111" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/readiness-failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=973acf53bd7e76bbce9bbc17caf516ff 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=a17cfc2831a3c44e7e2f4d9c60c4a644 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=9663d302eddcea9eb9980f98495f0ef9 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=b6838fb816be4126b5f7429157877e1a 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ce122b58715b62ff4f376100c24d36bb 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-failure.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3d82dbc7ea04f0189465612f09036632 2500w" />

<br />

# Configuration

Check the checkbox to enable the readiness probe. Currently, the supported protocols are `exec`, `gRPC`, `TCP`, and
`HTTP/1.X`

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-tcp-config.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=c511ec60e4a39fab3152554a5f9246eb" data-og-width="544" width="544" data-og-height="1158" height="1158" data-path="container-engine/images/readiness-tcp-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-tcp-config.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=15df93bb1d0106b441ce08cf368714f6 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-tcp-config.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=5d1863876e6ec14cb644a5c32bac6058 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-tcp-config.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=4cf6647c881e017a459dd48fd944d0a4 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-tcp-config.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=00b9c4ed6ef9b474e23c428cb6c3e187 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-tcp-config.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=da80577860ce6478c00911ac0f44559e 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/readiness-tcp-config.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=80d1b7fa82dd93ad57e1bba5736d9b8e 2500w" />

<br />

# Probe Status

You can see the status of a readiness probe, if configured, on each instance of a container group.

<img src="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-readiness.probe.png?fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=ffed42a010f35735a28dc7664da9dfcf" data-og-width="1312" width="1312" data-og-height="576" height="576" data-path="container-engine/images/portal-view-readiness.probe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-readiness.probe.png?w=280&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=e3ea262c1603f8c4f823f11798eece50 280w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-readiness.probe.png?w=560&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=abc4cfd836975ec57d59581ca1a7b48a 560w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-readiness.probe.png?w=840&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=221f1d8db3c8e53f7f510c9cb26c2ac4 840w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-readiness.probe.png?w=1100&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=3146f78e832f0c10b78920263a254f48 1100w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-readiness.probe.png?w=1650&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=1e3479c697e3aa4d42ce8995135b7325 1650w, https://mintcdn.com/salad/ko38nW-LNf6N2Y1I/container-engine/images/portal-view-readiness.probe.png?w=2500&fit=max&auto=format&n=ko38nW-LNf6N2Y1I&q=85&s=7af92df34327cf533b150e7648557d45 2500w" />
