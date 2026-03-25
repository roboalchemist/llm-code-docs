# Source: https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release/interacting-with-cortado.md

# Interacting with Cortado

{% hint style="warning" %}
**Note:** The Cortado testnet deployment will be frequently reset, thereby wiping out all user balances and history.
{% endhint %}

1. If not yet set up, install [MetaMask](https://metamask.io/) and set up a new wallet.
2. In MetaMask, click on the upper left icon to select a network.
3. Click "Add network" -> "Add a network manually".

![](https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-e5024f533dcc74f22e547044acecc48925d60376%2Fimage.png?alt=media)

4. To interact with Vienna, the OP Stack rollup, add a network with these parameters:
   * Network name: `Cortado Vienna`
   * New RPC URL: `https://vienna.calderachain.xyz/http`
   * Chain ID: `0xc0ffee1`
   * Block explorer URL: `https://vienna.calderaexplorer.xyz`
   * Currency symbol: `SepoliaETH`
5. To interact with the Polygon zkEVM stack rollup, add a network with these parameters:

   * Network name: `Cortado Polygon`
   * New RPC URL: `https://polygon-preconfirmations.cortado.espresso.network`
   * Chain ID: `0xc0ffee2`

   For "Currency symbol", anything can be set (the native currency on the Polygon zkEVM stack rollup is a dummy testnet token produced by the faucet, and there is no bridge to SepoliaETH). "Block explorer URL" should be left blank.

## Preconfirmations

The Espresso Sequencer uses the HotShot consensus protocol to provide fast confirmations of new blocks. These confirmations are secure, in that a block confirmed by HotShot is guaranteed to execute in the order determined by HotShot unless at least 1/3 of the total value staked in consensus is corrupt. They are also fast: a block may be confirmed by HotShot well before the same block is eventually processed by the layer 1 blockchain.

The RPC node for Cortado Polygon that you connected to above uses these "preconfirmations" from HotShot to achieve low latency, but there is a second RPC node that does not. In MetaMask, try going to Settings -> Networks -> Cortado Polygon and changing RPC URL to `https://polygon.cortado.espresso.network`. Then transfer some ETH on the Cortado Polygon network. Do you notice a difference in the speed with which the transaction gets confirmed?

For the Cortado testnet, the Vienna OP chain is only running a single RPC node, which does use preconfirmations, so you should experience low latency on the order of a few seconds there as well. However, note that MetaMask only refreshes pending transactions every 7 seconds. You may find it easier to observe low latency in the Vienna block explorer. Go to `https://vienna.calderaexplorer.xyz/address/<address>`, replacing `<address>` with your address in MetaMask. At the bottom you will see a section titled "Transactions", showing all the transactions made by this address. Now make a transfer in MetaMask on the Cortado Vienna network. How quickly does the new transaction appear in the block explorer?

## Faucet

For the Cortado Vienna OP stack rollup, you can requests funds from the [faucet](https://vienna.caldera.dev/). You can also directly deposit Sepolia ETH into the rollup using the [Caldera bridge](https://vienna.calderabridge.xyz/). Sepolia ETH can be obtained from the [Sepolia faucet](https://sepoliafaucet.com/).

For the Polygon zkEVM stack rollup, you can request funds in the [Discord](https://discord.com/invite/YHZPk5dbcq) `#faucet` channel with the following command: `/faucet <address>` To copy your MetaMask address, click on the address at the top of the MetaMask panel.
