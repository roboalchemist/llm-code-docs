# Source: https://docs.espressosys.com/network/releases/testnets/gibraltar-testnet-release.md

# Gibraltar Testnet Release

{% hint style="warning" %}
With the release of [Cappuccino](https://docs.espressosys.com/network/releases/testnets/cappuccino-testnet-release) (testnet 5), the Cortado testnet is currently paused.
{% endhint %}

In January 2024, we announced the Gibraltar release of Espresso.

Gibraltar includes a number of key highlights. Firstly, we have built an integration with Arbitrum Nitro, allowing anyone to easily deploy an instance of the Arbitrum technology stack on Espresso. Secondly, we have made important progress on [Savoiardi](https://hackmd.io/@EspressoSystems/HotShot-and-Tiramisu#Part-III-Tiramisu-The-Three-Layered-Espresso-DA), an implementation of verifiable information dispersal (VID), which forms the backbone of our Tiramisu DA solution. VID is what allows us to effectively move transaction dissemination from the critical path of consensus, while retaining full DA guarantees. This enables extremely high data throughput and low latency while maintaining a large consensus set.

As part of the Gibraltar public testnet release, Caldera will be deploying an instance of Arbitrum Nitro called [Milan](https://milan.caldera.dev/) onto Espresso. Caldera's OP stack rollup, Vienna, will also be migrated to Gibraltar. This marks the first time these rollup stacks will run alongside each other on Espresso. Cartesi has also made their own integration (of [Rickroll](https://twitter.com/EspressoSys/status/1712199798973972773) fame) even easier to use, and we will be adding docs to easily deploy your own Cartesi rollup on Espresso in the coming weeks.

Gibraltar also marks the first time that Espresso is being run by a set of external node operators, in collaboration with Blockdaemon, marking an important step towards the decentralization of the protocol.
