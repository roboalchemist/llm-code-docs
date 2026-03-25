# Source: https://docs.espressosys.com/network/releases/mainnet-0.md

# Mainnet 0

Mainnet 0 marks the production release of the Espresso Network. This release is an important step towards enabling Espresso's vision of an ecosystem of open, composable and permissionless applications.

Espresso’s Global Confirmation Layer will support applications such as rollups with faster bridging, and lays the groundwork for chains to improve coordination amongst each other, enhancing cross-chain interoperability.

Underpinning the Espresso Network is HotShot, which will be run in a production setting for the first time. During the initial stages of Mainnet 0, HotShot will be run by a set of 20 node operators, running 100 nodes in total. An important upcoming milestone will be to open up participation to more node operators and increase economic security through proof-of-stake.

During the initial release, block size has conservatively been set to 1 MB, with plans to scale up to 5 MB in the short term if there is sufficient demand. We expect it to take around \~8 seconds for a transaction to be confirmed in the initial release. In the short term, an update to HotShot will implement ideas from HotStuff-2 to reduce this time to \~5-6 seconds. In the medium term, [a VID update is in the works](https://espresso.discourse.group/t/faster-vid-on-espresso-s-critical-path/39) that will enable confirmation latency of \~3 seconds, even as we scale to thousands of consensus nodes. This will also enable us to increase the blocksize further without greatly impacting latency.

You can track activity on Mainnet in our [block explorer](https://explorer.main.net.espresso.network), and you can interact with it via the [public API endpoint](https://query.main.net.espresso.network).
