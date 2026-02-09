# Source: https://docs.infera.org/about.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# About

## Introducing Infera

<img width="100%" src="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/zap.png?fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=e32c15f29ad3325df7f8643d51490554" data-og-width="3556" data-og-height="2160" data-path="images/zap.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/zap.png?w=280&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=46a893f694552b02b643ea9f2af663b1 280w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/zap.png?w=560&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=32cb2c9aeb12d7f5faa77c98cecd6617 560w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/zap.png?w=840&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=5d4668224781278cd9ac843ae6312a9c 840w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/zap.png?w=1100&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=5f4895a02b694e6e8b2ba18076977c2c 1100w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/zap.png?w=1650&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=7b27586fd124031e3fb9bcfda6c6d2db 1650w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/zap.png?w=2500&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=0d25050322b6728b746bc3a0ce7588ad 2500w" />

**Infera** is building a decentralized network for LLM inference allowing developers API access to dozens of open source and custom fine tuned models.

In an era where AI is increasingly central to our digital lives, concerns have risen around the concentration of decision-making power within a few hands for the industry. An example of this is OpenAI and it’s closed decision making for their AI products.

Infera Network is dedicated to revolutionizing the field of artificial intelligence by promoting the decentralization of AI inference for LLMs. Our mission is to democratize access to cutting-edge AI technologies through the provision of cost-effective, open-source modes that are improved on via community and individual contributions to the Infera ecosystem.

Beginning with Large Language Models (LLMs), Infera Network is committed to constructing a more inclusive, equitable, and community-driven AI landscape. This will be achieved by nurturing and harnessing advanced technologies developed in-house, ensuring that our efforts pave the way for a future where AI not only serves but also empowers Infera Network’s global communities.

## Network Architecture

<img width="100%" src="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/network-architecture.png?fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=ace9041d12927033b34b495d33622e6f" data-og-width="1023" data-og-height="857" data-path="images/network-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/network-architecture.png?w=280&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=887c669ed9cc13c0ccd97344182ed015 280w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/network-architecture.png?w=560&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=7ac52a81bd5150ec53182d876a9d395e 560w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/network-architecture.png?w=840&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=c945e9677a1d8ff5517c5d4c08a710f7 840w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/network-architecture.png?w=1100&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=6f5b58a686c79d2321eecb721e46e69c 1100w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/network-architecture.png?w=1650&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=3cdaad23d319cbbacc8f7216d47f2a18 1650w, https://mintcdn.com/infera-a106b685/uWBCufE3moWDn93L/images/network-architecture.png?w=2500&fit=max&auto=format&n=uWBCufE3moWDn93L&q=85&s=ba276ec19ccf0eda528eee09655aa530 2500w" />

* **API Gateway** Acts as the entry point for all requests, directing them to the dynamic load balancer.

* **Flow Harmonizer** This component is responsible for routing requests to nodes based on the node reputation, hardware capabilities, and current load. It ensures the responses are returned efficiently to the API gateway.

* **Infera Nodes** These are individual nodes that perform the actual computational work. Each node’s performance and reliability are tracked, influencing their future-assigned tasks and ratings.

* **Verification Nodes** These nodes validate the computational output of other nodes, ensuring accuracy and preventing malicious behavior. Verification nodes report their findings to the database for caching.

* **Result Storage** It stores processed requests, verification outcomes, and logs taken from usage by each node.

* **Oracle** The oracle is responsible for passing data on-chain, such as payments and scores for nodes.

* **Staking Contract Nodes** commit stakes, ensuring reliability and integrity in their computation.

## Why Infera?

**Infera** offers a unique solution by leveraging the power of decentralized GPU resources to provide efficient AI inference. Here’s why Infera stands out:

* **Decentralized AI Power:** Tap into a network of worldwide GPUs, reducing reliance on centralized cloud services and fostering a more democratic AI infrastructure.
* **Earn Rewards:** By contributing your GPU power, you can earn rewards as you help fuel AI applications, making your idle resources work for you.
* **Cost-Efficient:** Infera harnesses existing GPU capacity, offering a more cost-effective and scalable option compared to traditional cloud-based solutions.
* **Enhanced Privacy:** With data processing distributed across multiple nodes, Infera ensures better data privacy and security for AI applications.
* **Scalable and Resilient:** As more nodes join the network, Infera becomes increasingly powerful, ensuring faster and more reliable AI inference for a variety of applications.
