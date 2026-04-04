# Source: https://docs.espressosys.com/network/releases/testnets/doppio-testnet-release/polygon-zkevm-stack-integration.md

# Polygon zkEVM Stack Integration

Espresso Systems has created a proof-of-concept integration with the Polygon zkEVM stack in Espresso. This integration highlights Espresso Systems’ vision of connecting and decentralizing rollups without compromising the scale and speed that rollup users have grown accustomed to.

The [integration demo](https://github.com/EspressoSystems/espresso-polygon-zkevm-demo) consists of two instances of the Polygon zkEVM using Espresso for fast confirmations and data availability in tandem. The following section is a brief walkthrough of both the technical architecture and the end-user experience for the integration.

## Integration Architecture Walkthrough

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-134bc6d3f0d23014d9425f066a9ea603e5ba3554%2FzkEVM%20diagram.png?alt=media" alt="" width="563"><figcaption><p>Diagram of the zkEVM integration</p></figcaption></figure>

The transaction flow through Polygon zkEVM-Espresso integration is as follows:

* The user submits transaction to Polygon JSON-RPC interface.
* The EVM transaction is sent to the L2 adapter and then sent to Espresso's submission API.
* The transaction is wrapped in a HotShot transaction and propagated to the [HotShot network](https://medium.com/@espressosys/espresso-hotshot-consensus-designed-for-rollups-8df9654d4213).
* HotShot generates a block that includes the transaction.
* The transaction is available to the [HotShot query service](https://github.com/EspressoSystems/hotshot-query-service/).
* The HotShot commitment service sends the batch commitment and quorum certificate to the L1 HotShot contract, which verifies that quorum certificate is valid and emits the event that a new quorum certificate has been posted.
* The Synchronizer component of the zkEVM node gets the event via Etherman and queries the HotShot query service to obtain the full data for the batch (including the submitted transaction).
* The zkEVM node computes the proof.
* The proof is posted through Etherman library to the Polygon rollup contract.
* The rollup contract verifies the proof and that the transactions are sequenced by HotShot (not yet implemented in Doppio).

## Code Repository

The code for the Polygon zkEVM integration proof-of-concept can be found on GitHub: [`espresso-polygon-zkevm-demo`](https://github.com/EspressoSystems/espresso-polygon-zkevm-demo).
