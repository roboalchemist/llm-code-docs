# Source: https://docs.meson.fi/protocol/system-design.md

# System Design

The original HTLC design only described the process of the on-chain part and did not say how to efficiently and safely conduct the off-chain communication. In Meson, a set of off-chain services can ensure that users' swaps can be responded and completed stably and quickly, bringing a better user experience.

The Meson system architecture primarily consists of 4 components:

![Meson App Architecture.png](https://1966107664-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWJ9Xuoax4XwtI4AskpIb%2Fuploads%2Fgit-blob-e6d8deb5c5b7af0c5f2081299f607d279c06b4cb%2Fmeson_arch.png?alt=media)

* **Frontend apps** are the user-facing frontend applications
  * **Meson app** is the main app for users allowing them to contruct and submit cross-chain swaps on Meson. Users can also track progress of recent swaps.
  * **Meson explorer** is Meson's explorer outlining details of swaps submitted to Meson protocol, including swap information and step details with reference to transactions on each respective chain. The Meson explorer is maintained with persistent data storage of all submitted swaps and display them through the explorer user interface. Users can also search for swaps through the explorer.
* **Relayer** is a distributed messaging API service sitting between Meson app and LP services. Relayer receives initial swap request and following swap release data, performs basic checks and broadcasts to LP services for further processing. It behaves in the similar way to P2P network of Bitcoin or Ethereum blockchains.
* **LP services** are executables that process and issue swap transactions on behalf of LPs. They receive swap data from the relayer, verify checks, process it and post to the respective blockchains. Since LP services are posting the actual on-chain transactions, they will pay gas fees for users. LP services cannot tamper or modify swap data as it has been signed by the user. This service is like the miner program of a public chain.
* **Smart contracts** are the implemenatation of Meson protocol on each blockchain. They will receive swap data, check signatures, and orchestrates the whole Meson swap process on respective chains.

A typical flow of Meson swap across different systems is as follows

* A swap request is inititated and signed by a user on Meson app.
* The swap request along with the signature are submitted to the relayer and consequently be broadcasted to LP services.
* LP services will receive the incoming swap request, construct the respective transaction, and execute the Meson smart contracts. Notice that only one LP will finally match a given swap on chain.
* The same process will be repeated for processing the swap release to finish the entire swap.

Meson protocol also provides a backup plan that users can directly post swap request and release to the blockchain and pay gas fees themselves. In this case, LP services will receive swap data from on-chain events instead of the relayer, and complete their corresponding part of the swap.

## Roles

There are three roles in Meson: users, liquidity providers (LPs) and relayers.

* *Users*, also named *initiators* in swap encoding, are those who demand for cross-chain stablecoin swaps. They usually follow the [User Guide](https://docs.meson.fi/guides/meson) to use Meson.
* *Liquidity Providers (LPs)* provide stablecoin liquidities to Meson and match cross-chain swaps with users. They or their authorized addresses should run LP services to complete swaps. Please refer to [Liquidity Providers](https://github.com/MesonFi/docs/blob/main/protocol/meson/meson-lp/README.md) and [LP service](https://docs.meson.fi/protocol/system-design/lp-service) to learn more details.
* *Relayers* are runnings the Meson relayer service to broadcast swap data. The registration for becoming a relayer is not opened for now, but you can read [Relayer Service](https://docs.meson.fi/protocol/system-design/relayer) and learn more about how it works.
