# Source: https://docs.espressosys.com/network/concepts/espresso-in-the-modular-stack.md

# Using Espresso

The Espresso Network has been designed with multiple use cases in mind. We have seen that developers are best able to innovate when they have flexibility around designing their stack.

Espresso offers several benefits for chain operators and their developers to choose from:

* Fast finality: All chains that leverage Espresso benefit from fast, reliable [confirmations](https://hackmd.io/@EspressoSystems/bft-and-proposer-promised-preconfirmations)—replacing the need for users, bridges, and beyond to depend on preconfirmations that come from centralized sequencers.
* Data availability: All chains using Espresso also benefit from highly efficient [data availability](https://hackmd.io/@EspressoSystems/HotShot-and-Tiramisu) offered by the Espresso Network. However, many of the chains that are using Espresso also choose to leverage another form of DA, such as EigenDA, Celestia, Avail, or Ethereum itself. We have designed Espresso to respect and to be additively compatible with these choices.
* Decentralized sequencing: Rollups can use Espresso to set up their own decentralized sequencer, gaining better censorship resistance and liveness guarantees without sacrificing on latency, while using their own token to elect their sequencer set.

<figure><img src="https://1421932799-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FBeiHaL4yXVSdD2dUzh9N%2Fuploads%2Fgit-blob-429159b1a8ae5ddcba95b585a6f2d43e206c4195%2FModularity%20Scratch%20(6).png?alt=media" alt=""><figcaption></figcaption></figure>

A few examples of how Ethereum rollups can use the Espresso network include:

* A standard rollup or validium that uses the L1 or an alternative data availability solution, leverages its own centralized sequencer, and settles to Ethereum may leverage Espresso for confirmations.
* A based rollup that uses Ethereum for DA, relies on the Ethereum proposer for sequencing, and looks to the L1 for settlement may also use Espresso for fast, reliable confirmations.
* A validium that leverages its own centralized sequencer can use Espresso for data availability and also for more robust confirmations than the preconfirmations that its sequencer could offer.
* A rollup or validium that wants to decentralize its sequencing without using the L1 proposer may use the Espresso leader as its sequencer for any given round and use Espresso for confirmations – while using its own choice of data availability.
* A rollup that uses Espresso for DA, sequencing, and confirmations is what we like to call a caffeinated chain.

While we only cover Ethereum rollups here, this also applies to sovereign rollups and beyond.
