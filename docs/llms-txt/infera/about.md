# Source: https://docs.infera.org/about.md

# About

## Introducing Infera

<img width="100%" src="https://mintlify.s3.us-west-1.amazonaws.com/infera-a106b685/images/zap.png" />

**Infera** is building a decentralized network for LLM inference allowing developers API access to dozens of open source and custom fine tuned models.

In an era where AI is increasingly central to our digital lives, concerns have risen around the concentration of decision-making power within a few hands for the industry. An example of this is OpenAI and it’s closed decision making for their AI products.

Infera Network is dedicated to revolutionizing the field of artificial intelligence by promoting the decentralization of AI inference for LLMs. Our mission is to democratize access to cutting-edge AI technologies through the provision of cost-effective, open-source modes that are improved on via community and individual contributions to the Infera ecosystem.

Beginning with Large Language Models (LLMs), Infera Network is committed to constructing a more inclusive, equitable, and community-driven AI landscape. This will be achieved by nurturing and harnessing advanced technologies developed in-house, ensuring that our efforts pave the way for a future where AI not only serves but also empowers Infera Network’s global communities.

## Network Architecture

<img width="100%" src="https://mintlify.s3.us-west-1.amazonaws.com/infera-a106b685/images/network-architecture.png" />

*   **API Gateway** Acts as the entry point for all requests, directing them to the dynamic load balancer.

*   **Flow Harmonizer** This component is responsible for routing requests to nodes based on the node reputation, hardware capabilities, and current load. It ensures the responses are returned efficiently to the API gateway.

*   **Infera Nodes** These are individual nodes that perform the actual computational work. Each node’s performance and reliability are tracked, influencing their future-assigned tasks and ratings.

*   **Verification Nodes** These nodes validate the computational output of other nodes, ensuring accuracy and preventing malicious behavior. Verification nodes report their findings to the database for caching.

*   **Result Storage** It stores processed requests, verification outcomes, and logs taken from usage by each node.

*   **Oracle** The oracle is responsible for passing data on-chain, such as payments and scores for nodes.

*   **Staking Contract Nodes** commit stakes, ensuring reliability and integrity in their computation.

## Why Infera?

**Infera** offers a unique solution by leveraging the power of decentralized GPU resources to provide efficient AI inference. Here’s why Infera stands out:

*   **Decentralized AI Power:** Tap into a network of worldwide GPUs, reducing reliance on centralized cloud services and fostering a more democratic AI infrastructure.
*   **Earn Rewards:** By contributing your GPU power, you can earn rewards as you help fuel AI applications, making your idle resources work for you.
*   **Cost-Efficient:** Infera harnesses existing GPU capacity, offering a more cost-effective and scalable option compared to traditional cloud-based solutions.
*   **Enhanced Privacy:** With data processing distributed across multiple nodes, Infera ensures better data privacy and security for AI applications.
*   **Scalable and Resilient:** As more nodes join the network, Infera becomes increasingly powerful, ensuring faster and more reliable AI inference for a variety of applications.
