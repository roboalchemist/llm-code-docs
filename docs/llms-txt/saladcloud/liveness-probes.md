# Source: https://docs.salad.com/container-engine/explanation/infrastructure-platform/liveness-probes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Liveness Probes

*Last Updated: October 15, 2024*

# Overview

Liveness probes are similar to startup probes, except that they run after the startup probe has completed successfully.
Typically, Liveness probes are used to evaluate whether the application running in your container is in a healthy state.
If a container's liveness probe reaches the failure state, the container will be reallocated to a different node.
Liveness probes are a good place to put logic that checks for CUDA errors, and other unrecoverable states.

## Successful Liveness Probe

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=17bc3df45d4143c26e353b734a23f0d2" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/liveness-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=6ff6ed9357815440eec898f0ca79ce15 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=3bfdd20e11e3a5f37a8d0ca2417858c0 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=c630cb4b3f4e2e50558fed839b4d6e55 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=fe55e61b2a349d0bfeb8d72fb2613c1f 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=5c1e5ab336fb224d3b70e2f9a7149c68 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-success.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=4bfadbd5ef7f6de4811784a787bf300f 2500w" />

## Failed Liveness Probe

<img src="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=1318ba39d2101ed92fd565ed2a2f269c" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/liveness-failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=280&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=0fdfc043ae759ff17d5d73074210a0d7 280w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=560&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=81013b6f62997ba9d00fb4c5bc5bab38 560w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=840&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=6020fd7c19fa6f0227046c73091b9de1 840w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=1100&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=835240251829a2eb27e9be609bea0ca3 1100w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=1650&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=46ad9200815505966499d22e8bf3ab45 1650w, https://mintcdn.com/salad/FAbpq_8Gi6WzwO0s/container-engine/images/liveness-failure.png?w=2500&fit=max&auto=format&n=FAbpq_8Gi6WzwO0s&q=85&s=e9d2ba6d6696a8be1522629b9791becf 2500w" />

# Configuration

Check the checkbox to enable the liveness probe. Currently, the supported protocols are `exec`, `gRPC`, `TCP`, and
`HTTP/1.X`

<img src="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/liveness-tcp-config.png?fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=192a719974b284a8d01813c64ba1e51c" data-og-width="480" width="480" data-og-height="1134" height="1134" data-path="container-engine/images/liveness-tcp-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/liveness-tcp-config.png?w=280&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=8f7ddfa9f0b7ac13ef6c0eaeed2386b8 280w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/liveness-tcp-config.png?w=560&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=613a9a034a99aeb69852362b1d61b4d4 560w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/liveness-tcp-config.png?w=840&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=a5647dc546a088e1cc338b12118eae9f 840w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/liveness-tcp-config.png?w=1100&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=0b0bff5c344f032ceb2c0285a3c1efa8 1100w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/liveness-tcp-config.png?w=1650&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=6b22ee4fa7f29ebe5598bd14ce5d3835 1650w, https://mintcdn.com/salad/pEBrSzH4UQRtJw00/container-engine/images/liveness-tcp-config.png?w=2500&fit=max&auto=format&n=pEBrSzH4UQRtJw00&q=85&s=c9d00312d025c32d5f2ca36267ebc8b6 2500w" />
