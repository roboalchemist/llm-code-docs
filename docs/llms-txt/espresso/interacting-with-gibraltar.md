# Source: https://docs.espressosys.com/network/releases/testnets/gibraltar-testnet-release/interacting-with-gibraltar.md

# Interacting with Gibraltar

{% hint style="warning" %}
**Note:** The Gibraltar testnet deployment will be frequently reset, thereby wiping out all user balances and history.
{% endhint %}

{% hint style="warning" %}
**Note:** The Vienna OP stack rollup will not be deployed immediately after the release of Gibraltar, but we will make an announcement when it is running soon after. The Milan Arbitrm Nitro rollup will be available to use immediately.
{% endhint %}

1. If not yet set up, install [MetaMask](https://metamask.io/) and set up a new wallet.
2. In MetaMask, click on the upper left icon to select a network.
3. Click "Add network" -> "Add a network manually".

![](https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-e5024f533dcc74f22e547044acecc48925d60376%2Fimage.png?alt=media)

4. To interact with Milan, the Arbitrum Nitro rollup, add a network with these parameters:
   * Network name: `Gibraltar Milan`
   * New RPC URL: `https://milan-devnet.rpc.caldera.xyz/http`
   * Chain ID: `83782`
   * Block explorer URL: `https://milan-devnet.explorer.caldera.xyz/`
   * Currency symbol: `SepoliaETH`
5. To interact with Vienna, the OP Stack rollup, add a network with these parameters:
   * Network name: `Gibraltar Vienna`
   * New RPC URL: `https://vienna.calderachain.xyz/http`
   * Chain ID: `0xc0ffee1`
   * Block explorer URL: `https://vienna.calderaexplorer.xyz`
   * Currency symbol: `SepoliaETH`

## Preconfirmations

As in our previous testnet, Espresso uses the HotShot consensus protocol to provide fast confirmations of new blocks. These confirmations are secure, in that a block confirmed by HotShot is guaranteed to execute in the order determined by HotShot unless at least 1/3 of the total value staked in consensus is corrupt. They are also fast: a block may be confirmed by HotShot well before the same block is eventually processed by the layer 1 blockchain.

For the Gibraltar testnet, the Vienna OP chain as well as the Milan Arbitrum Nitro chain are both using these preconfirmations, so you should experience low latency on the order of a few seconds for both rollups. However, note that MetaMask only refreshes pending transactions every 7 seconds. You may find it easier to observe low latency in the Vienna and Milan block explorers.

For Vienna go to`https://vienna.calderaexplorer.xyz/address/<address>`, replacing `<address>` with your address in MetaMask. For Milan, go to `https://milan-gibraltar.explorer.caldera.xyz/address/<address>` and input your address. At the bottom you will see a section titled "Transactions", showing all the transactions made by this address. Now make a transfer in MetaMask on the Gibraltar Vienna or Milan network and see how fast it appears in the block explorer!

## Faucet

For the Gibraltar Vienna OP stack rollup, you can requests funds from the [faucet](https://vienna.caldera.dev/). Similarly, for the Milan Arbitrum Nitro rollup you can request funds from the [faucet](https://milan.caldera.dev/faucet). You can also directly deposit Sepolia ETH into the rollup using the [Vienna bridge](https://vienna.calderabridge.xyz/) or [Milan bridge](https://milan-gibraltar.calderabridge.xyz/). Sepolia ETH can be obtained from the [Sepolia faucet](https://sepoliafaucet.com/).
