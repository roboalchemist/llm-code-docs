# Source: https://docs.salad.com/container-engine/explanation/infrastructure-platform/startup-probes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.salad.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Startup Probes

*Last Updated: October 15, 2024*

# Overview

Startup probes, when configured, run as soon as the container is created. They are typically used to ensure that the
application has started, and is ready to accept traffic. No traffic will be sent from the load balancer until the
startup probe has passed, so prevent your startup probe from passing until you have downloaded and warmed up your
models.

## Successful Startup Probe

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=5abc4db02f375ea8a7fd8c62282d7cb6" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/startup-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b4fde9a2c1ab848c8e91ebe2fe5a6fdd 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=1dbf1039f3bccfb8537fced2e3254761 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=f5545b764cad2cef89f32144799b2a27 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=2beedb87e16c2b3d4d57bc4c3b7ff237 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=ed95e848f66445e9989a0e48fef22cf0 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-success.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=473906d3ee36338cd24fa511f41438f5 2500w" />

## Failed Startup Probe

<img src="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=b0f17053349bdf0303f331e853a6204d" data-og-width="1323" width="1323" data-og-height="291" height="291" data-path="container-engine/images/startup-failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=280&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=39afa691c64678b699d249bd3c4aae2f 280w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=560&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=423a01e8190a445695d8e54478d53fc0 560w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=840&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=2f1707e2b34a4de5e5e9f983a6cedb2f 840w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=1100&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=45eecb9153599ff4ea3418832c0e749a 1100w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=1650&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=c314606bbc54a62e5233676501555b37 1650w, https://mintcdn.com/salad/oE6Ic7VdFlh4rKXK/container-engine/images/startup-failure.png?w=2500&fit=max&auto=format&n=oE6Ic7VdFlh4rKXK&q=85&s=e6da7697252966bbea94e0b409adbd74 2500w" />

# Configuration

Check the checkbox to enable the startup probe. Currently, the supported protocols are `exec`, `gRPC`, `TCP`, and
`HTTP/1.X`

<img src="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/startup-tcp-config.png?fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=5c919c08e778b15e0320e7ea892c5fd8" data-og-width="493" width="493" data-og-height="1134" height="1134" data-path="container-engine/images/startup-tcp-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/startup-tcp-config.png?w=280&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=5f0b450d97bb21279ac2b506ae2af2c0 280w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/startup-tcp-config.png?w=560&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=514d5fc73986ee2eb07e30f4beb0acb0 560w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/startup-tcp-config.png?w=840&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=a9f89f9f963ce2490ac0c23863e089e7 840w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/startup-tcp-config.png?w=1100&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=60dc1dd65eeebab1f95ee9d81767f6ca 1100w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/startup-tcp-config.png?w=1650&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=851632c237f0f0400c0b8e92c2135f53 1650w, https://mintcdn.com/salad/B_utM-6XUMV1Xhv8/container-engine/images/startup-tcp-config.png?w=2500&fit=max&auto=format&n=B_utM-6XUMV1Xhv8&q=85&s=feec24a268a278ead350d67e06c96bd6 2500w" />

> 📘 Tips for slow-starting containers
>
> SCE attempts to estimate the maximum time the probe can run before resulting in a failure, based on the values in the
> fields above. This guidance is provided below the Configure button. If you expect your container often takes longer
> than this to start, you should adjust the thresholds in the fields above to ensure that you're not prematurely
> reallocating containers that could have reached a successful status.
