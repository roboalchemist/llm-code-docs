# Source: https://docs.statsig.com/client/onDeviceOverview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# On Device Client SDKs

## On Device SDK Overview

Statsig's client-side On-Device Eval SDKs provide an alternate client-side architecture where the definition of each experiment or gate is kept in-memory on the device, allowing for faster evaluation with a frequently changing user object (which would require re-initialization on regular client SDKs), at the expense of the privacy of the config definitions.

Generally, we encourage customers to use our traditional client SDKs, unless they have specific requirements making that impossible. If you do choose to use the on-device eval SDKs, we encourage you to speak with our team first and understand the privacy risks.

## Alternatives

An alternative approach to On-Device Eval SDKs is our [Local Eval Adapter](/client/concepts/local-eval-adapter) which allows you to evaluate locally for only a subset of your experiments/gates that might need to be available at startup, rather than exposing all configs in your project.


Built with [Mintlify](https://mintlify.com).