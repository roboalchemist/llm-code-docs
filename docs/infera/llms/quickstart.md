# Source: https://docs.infera.org/node/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Running an Infera Node

> Quickstart to how to get an Infera node running on your device.

The **Infera node** serves as an efficient off-chain client, dedicated to handling and completing compute tasks within the Infera network.

<Warning>
  Please check [Hardware Requirements](/node/hardware-requirements) before installing to ensure you have the minimum hardware requirement to get jobs. Otherwise your node will not be given jobs to compute!
</Warning>

***

## What is an Infera Node?

An Infera Node is a software application that allows users to contribute their GPU’s compute power to perform AI inference tasks. Whether you’re a hobbyist with a single GPU or a professional with a network of devices, running an Infera Node enables you to participate in the decentralized AI ecosystem, earning rewards for your contributions.

Learn how to install your own node using the [Mac](/node/macos), [Linux](/node/linux) or [Windows](/node/windows) install guide.

***

## How does it work?

<img width="100%" src="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/node-diagram-white.png?fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=f9651fd5b69546ba695cc33d5a5cef89" data-og-width="2294" data-og-height="896" data-path="images/node/node-diagram-white.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/node-diagram-white.png?w=280&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=6937ce85d1fa5bfade224228aedd43dc 280w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/node-diagram-white.png?w=560&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=990f08f8b17d435c491236f79cac9b32 560w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/node-diagram-white.png?w=840&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=dc484bdcbfc3a51306c29b185b9d68df 840w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/node-diagram-white.png?w=1100&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=20ab05c633263992331a55049f6b384f 1100w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/node-diagram-white.png?w=1650&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=e19bb9db93db89a1da08cce539133397 1650w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/node/node-diagram-white.png?w=2500&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=c77c8e3ca10253de65530a9d1a08fb87 2500w" />

* Nodes listen for inference requests broadcasted from the load balancer.
* When a job is received, the input is passed to the node's inference engine.
* Post-inference, the results are verified with similar outputs from reference nodes.
* Results are then routed back to the load balancer alongside the verification results.

***

## Why run an Infera Node?

* **Earn Rewards:** Contribute your GPU power to the network and receive points or tokens for each successful AI inference job your node processes.
* **Decentralize AI:** Help democratize AI by making high-performance compute power accessible to everyone, reducing the reliance on centralized cloud services.
* **Efficient Usage:** Maximize the use of your idle or underutilized GPU resources by putting them to work on meaningful AI tasks.
* **Scalable Network:** As more nodes join, the network becomes more powerful and resilient, offering even faster and more efficient AI inference.
