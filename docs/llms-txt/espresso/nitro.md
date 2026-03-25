# Source: https://docs.espressosys.com/network/guides/rollup-developers/nitro.md

# Source: https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup/nitro.md

# Nitro Chain Integration

TL;DR - Chains and Rollup-as-a-Service (”RaaS”) providers can leverage the Espresso Network to provide users with faster, more secure confirmations on their transactions. The Espresso Network also provides chain operators with information about the state of their own chain and the states of other chains, all of which is important for improved UX and ultimately, cross-chain composability. This document outlines the steps for chains/RaaS to integrate with the Espresso Network.

Integration at a glance - Integrating with the Espresso Network requires minimal changes to Arbitrum Nitro's existing rollup design, and the key change is running the Arbitrum Nitro batch poster inside a Trusted Execution Environment (”TEE”). See [here](https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup/nitro/using-tee-with-nitro) for an explanation of this design and see [here](https://docs.espressosys.com/network/concepts/rollup-developers/integrating-an-optimistic-rollup/nitro/arbitrum-nitro-trust-and-liveness-dependencies) for trust assumptions that partners should be aware of when integrating. Today, Espresso has developed software to run the batch poster using SGX in Microsoft Azure. We plan to release a version compatible with AWS Nitro (not to be confused with Arbitrum Nitro) by EOQ1’25.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-b8a469b05b6ef33da30973e1a68260881fb0180c%2Fimage.png?alt=media" alt=""><figcaption><p>See here for the technical integration diagram</p></figcaption></figure>

### Prerequisites & Requirements (1-3 days\*)

\**Assumes familiarity with TEEs. Teams may want to allocate up to 7 days to upskill and deploy this technology for the first time.*

We will host a kick-off call to walk through your technical architecture, including what cloud providers you work with. In an effort to expedite the integration process, we ask that you please share with Espresso:

1. A config file that we can work from. Note: This is only needed if Espresso is running the batch poster.
2. Direct access to your RPC node (instead of through an intermediary). Note: This is only needed if Espresso is running the batch poster.
3. Confirmation that you are able to run the TEE within your existing infrastructure. Note: Espresso is able to run it on your behalf; however we prefer to support you to run it using your own infrastructure.
4. Confirmation of the integrating chain's current Arbitrum Nitro version.
5. Other pre-requisites include understanding how a TEE operates, if you aren't already familiar:
   * Docs specific to AWS Nitro Enclaves:
     * [Review Hello Enclaves sample application](https://docs.aws.amazon.com/enclaves/latest/user/getting-started.html)
     * [Install AWS Nitro on Linux](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-cli-install.html) OR
     * [Install AWS Nitro on Windows](https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave-cli-install-win.html)
   * Docs specific to SGX:
     * [Guide to determine which hardware/cloud providers support SGX](https://github.com/ayeks/SGX-hardware#hardware-with-sgx2-support)
     * [Guide to enable a prover using SGX](https://docs.taiko.xyz/guides/node-operators/enable-a-prover/) (note this links to Taiko’s docs, as Taiko currently uses SGX)

### Run deployments (2-3 weeks)

We require that teams run a testnet and mainnet deployment; however chains and RaaS providers have the opportunity to also run internal devnet deployments beforehand (this is recommended if it's our first time working together). This process will allow us time to fix any issues and bugs that may occur during testing and will ultimately ensure a more seamless transition to mainnet. An illustrative integration timeline may look like this (see diagram below):

* An internal deployment (3-4 days) is optional but is recommended for new architecture or a RaaS provider that has not previously integrated with Espresso.
* A devnet deployment (3-7 days) is optional but is recommended for new architecture or a RaaS provider that has not previously integrated with Espresso.
* A testnet deployment (5-7 days) is required, and we look to run a testnet for 5-7 days with no incidents before we consider deploying to mainnet.
* A mainnet deployment would follow a successful testnet deployment.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-0904f1d7e0254337da38e830ba4e5caa98cba165%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### Migration Flow (1-3 hours)

1. Run the batch poster inside the TEE (e.g. AWS Nitro or SGX)
2. Deploy the EspressoTEEVerifier contract
3. Stop the batch poster node and copy the batch poster’s databases files to the TEE
4. Perform the sequencer inbox migration
5. New batch poster starts catching up messages and building up state

### Support (0.5-1 hour per week)

* Espresso engineers will support your chain and RaaS provider as you navigate the integration process through relevant devops services, async tech support, and calls to run through integration steps.
* Espresso has a 24x7 support model and tracks the health and frequency of batch posting to ensure that there are no delays. If something isn't working, Espresso will automatically trigger an on-call procedure to investigate the incident. We recommend that our integrated chains also monitor these health metrics and have an incident management procedure.

### FAQ

1. How much does it cost a chain or RaaS provider to integrate with Espresso?
   1. Fees are paid by the builder of each block. Initially, in Mainnet 0.0/Decaf 0.0, Espresso will run a simple builder and cover fees. Fees will not be collected from rollups using Espresso or their users. There will be no third party builders during Mainnet 0.0/Decaf 0.0.
2. What is Espresso’s latency for blocks? How long does it take blocks to reach finality?
   1. Espresso confirmations are faster than waiting for Ethereum finality, which takes 12-15 minutes. Using Espresso, the current latency for blocks is 2-9s (1-3s with transactions, 8s with no transactions) with HotShot finality reached after 3 consecutive blocks, typically in 6-20s (slower when blocks are empty). There are future roadmap improvements to decrease latency and time to finality (including an adjustment to finalize after 2 consecutive blocks, rather than 3, which should result in a 20-30% reduction in latency).
3. What is Espresso’s throughput per second?
   1. During some recent heavy load testing, we achieved \~100 TPS with small transactions (\~200 bytes each). We currently have a 1MB limit on the block size, which performed well under the same load testing. We plan to use our Proof of Stake upgrade in March 2025 to significantly improve network throughput and latency with (i) an increase to the block limit, and (ii) adding erasure coding via [Verifiable Information Dispersal](https://espresso.discourse.group/t/faster-vid-on-espresso-s-critical-path/39).
