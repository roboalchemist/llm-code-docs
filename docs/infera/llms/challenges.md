# Source: https://docs.infera.org/challenges.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.infera.org/llms.txt
> Use this file to discover all available pages before exploring further.

# Challenges and Solutions

## Challenges

### AI Censorship

New models are developed in secret and most users has little or no influence in the ethics or the decisions powering the LLMs. With the current standard of centralized decision making with ai models, users have no impact on the development and direction of the model, but the model has a direct impact on users themselves.

1. **Limiting Freedom of Speech** \
   The current regime of available LLMs are heavily censored within the industry. Infera Network aims to build an LLM for all to use and contribute to - without censorship.

2. **Manipulation of Information** \
   Due to non-deterministic nature of LLMs they have been historically centralized for “safety” reasons.

3. **Impact on Innovation** \
   By limiting the use cases of AI through censorship, we hold back innovation. Uncensored AI will push the world forward.

### GPU usage for AI inference

While the AI community is heavily focused on addressing challenges in data handling and model training, a significantly greater opportunity lies within the inference sector, potentially exceeding current focuses by an order of magnitude. The prevalent model of renting GPUs by the hour is not aligned with developers’ needs, who prefer a pay-per-use approach for querying existing open-source models. Our initiative introduces a groundbreaking open-source model, co-developed with the community, enabling us to offer decentralized nodes. This allows developers to access computational power for inference tasks beyond traditional data center constraints, substantially reducing costs.

Currently, the technology required to parallelize and train models across thousands of globally distributed GPUs is still under development. However, inference tasks, which form the backbone of real-world AI applications, usually require only a single GPU. Unlike training, inference processes do not benefit from, nor necessitate, multi-GPU setups; even in environments designed for parallel operations, inference tasks are typically handled by a singular core. This distinction underscores the efficiency and potential cost-effectiveness of our decentralized approach for inference, marking a pivotal advancement in making AI more accessible and economically viable for developers worldwide.

### Data Center GPU Cost

Nvidia H100 GPUs sell for \~\$40,000 USD which are specific to data centers.

Nvidia RTX 4090 GPUs sell for \~\$2,500 which can be used in the home.

The cost disparity in utilizing data centers for AI applications is profound, often exceeding a 10x difference. We recognize an immense opportunity in harnessing idle GPUs found within personal home computers. By tapping into this dormant resource, we can drastically lower the cost per inference for developers, unlocking a new realm of efficiency and affordability in AI development.

### It is not enough to just buy a GPU

While it's possible for individuals to run a model on their own, scaling this operation presents a significant challenge. At present, the primary means to surmount this barrier to entry involves leveraging GPUs housed within data centers and learning complex tech stacks in order to even start simple model inferencing.

## Solutions

### Community Aligned Development and Open-source models

For each model we develop, our approach begins with our user community, prioritizing their needs and working backwards from there. Our commitment is to operate transparently, ensuring that all decisions are made with community consensus and support. We endeavor to co-create new models alongside our token holders, ensuring that these innovations align with community standards and expectations.

### Decentralized nodes for inference

Decentralizing inference through networked GPUs offers a transformative approach akin to data center capabilities but without the associated costs. A single 4090 GPU, capable of handling multiple concurrent requests with rapid token streaming, exemplifies this potential. By interconnecting these powerful GPUs globally, we can establish a decentralized system for Large Language Model (LLM) inference that rivals traditional data center performance. This system leverages the untapped power of idle GPUs worldwide, offering data center-level infrastructure at a fraction of the cost.

Transitioning to a decentralized model is straightforward, relying on readily available tools and a clear methodology:

1. **Requests Allocation:** \
   Infera will distribute requests from the mempool to ecosystem nodes in a randomized manner, ensuring each request is handled by at least three different nodes to foster redundancy and reliability.
2. **Output Verification:** \
   Outputs from nodes will be assessed using a semantic similarity score to evaluate their accuracy. Outputs that surpass a specific threshold will be deemed verified, ensuring high-quality responses.
3. **Settlement and Response:** \
   Verified responses will be conclusively recorded on the blockchain, with a randomly selected response sent back to the requester, completing the cycle of decentralized inference.

### Unlocking Latent GPU Supply

Leveraging the untapped potential of idle GPUs, we unlock new revenue opportunities for individuals who previously had no means to monetize their hardware. This initiative introduces a compelling revenue stream for GPU owners, enabling them to recoup some of their hardware investment costs.

As part of our strategic roadmap, Infera is set to release a downloadable node compatible with any GPU. This node is designed to intelligently utilize the GPU only during idle periods. For instance, Infera’s operations are paused while you engage in GPU-intensive activities, such as gaming. Conversely, when your computer is on but not in use—like during the night—Infera activates to perform AI inference tasks. This operation not only supports the network’s AI capabilities but also compensates the node operators with \$INFER tokens, seamlessly turning idle time into valuable assets.

Additionally, the plug and play aspect of Infera allows immediate usage of your hardware, without spending your own time to learn how to do so.
