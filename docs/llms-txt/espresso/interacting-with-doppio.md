# Source: https://docs.espressosys.com/network/releases/testnets/doppio-testnet-release/interacting-with-doppio.md

# Interacting with Doppio

{% hint style="warning" %}
With the deployment of [Cortado](https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release) (testnet 3), the instructions in this document for connecting to Doppio no longer work. See [*Interacting with Cortado*](https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release/interacting-with-cortado) for instructions for interacting with Cortado.
{% endhint %}

1. If not yet set up, install [MetaMask](https://metamask.io/) and set up a new wallet.
2. In MetaMask, click on the upper left icon to select a network.
3. Click "Add network" -> "Add a network manually".

![](https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-e5024f533dcc74f22e547044acecc48925d60376%2Fimage.png?alt=media)

Use the following parameters:

* Network name: `espresso-polygon-zkevm-0`
* New RPC URL: <https://zkevm-0-preconfirmations.doppio.espresso.network>
* Chain ID: `1001`

To interact with the second rollup, add a network with these parameters:

* Network name: `espresso-polygon-zkevm-1`
* New RPC URL: <https://zkevm-1.doppio.espresso.network>
* Chain ID: `1002`

For "Currency symbol", anything can be set and "Block explorer URL" should be left blank.

## Preconfirmations

The Espresso Sequencer uses the HotShot consensus protocol to provide fast confirmations of new blocks. These confirmations are secure, in that a block confirmed by HotShot is guaranteed to execute in the order determined by HotShot unless at least 1/3 of the total value staked in consensus is corrupt. They are also fast: a block may be confirmed by HotShot well before the same block is eventually processed by the layer 1 blockchain.

The RPC node for zkevm-0 that you connected to above uses these "preconfirmations" from HotShot to achieve low latency, but the RPC node for zkevm-1 does not. Try transferring some ETH on each network. Do you notice a difference in the speed with which the transaction gets confirmed?

For a more direct comparison, Doppio also includes an additional RPC node for zkevm-0 which fetches new blocks from the L1 rollup contract instead of directly from the Espresso Sequencer. You can try this "slow" RPC node to compare the latency with and without preconfirmations on the same L2.

To connect your MetaMask wallet to the slow RPC, go to Settings -> Networks and change the RPC URL for `espresso-polygon-zkevm-0` to <https://zkevm-0.doppio.espresso.network>.

## Faucet

You can request funds in the [Discord](https://discord.com/invite/YHZPk5dbcq) #faucet channel with the following command: `/faucet <address>`

To copy your MetaMask address, click on the address at the top of the MetaMask panel.

## Transaction Submission Using MetaMask

The end-user experience for submitting transactions to an instance of the Polygon zkEVM running on the Espresso Sequencer via MetaMask is identical to the user experience of submitting transactions to Polygon rollup today. Additionally, gas savings are realized by utilizing Espresso DA rather than storing transactions in Ethereum L1 calldata.
