# Source: https://docs.infera.org/node/quickstart.md

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

<img width="100%" src="https://mintlify.s3.us-west-1.amazonaws.com/infera-a106b685/images/node/node-diagram-white.png" />

*   Nodes listen for inference requests broadcasted from the load balancer.
*   When a job is received, the input is passed to the node's inference engine.
*   Post-inference, the results are verified with similar outputs from reference nodes.
*   Results are then routed back to the load balancer alongside the verification results.

***

## Why run an Infera Node?

*   **Earn Rewards:** Contribute your GPU power to the network and receive points or tokens for each successful AI inference job your node processes.
*   **Decentralize AI:** Help democratize AI by making high-performance compute power accessible to everyone, reducing the reliance on centralized cloud services.
*   **Efficient Usage:** Maximize the use of your idle or underutilized GPU resources by putting them to work on meaningful AI tasks.
*   **Scalable Network:** As more nodes join, the network becomes more powerful and resilient, offering even faster and more efficient AI inference.
