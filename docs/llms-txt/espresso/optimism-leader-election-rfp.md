# Source: https://docs.espressosys.com/network/releases/testnets/cortado-testnet-release/op-stack-integration/optimism-leader-election-rfp.md

# Optimism Leader Election RFP

The OP-Espresso integration is a result of our work on Optimism's [request for proposals](https://github.com/ethereum-optimism/ecosystem-contributions/issues/63) of a leader election proof-of-concept against the OP Stack.

On 1 June 2023, Optimism solicited proposals for this RFP, with submitted proposals due June 28. [Espresso Systems' proposal](https://github.com/ethereum-optimism/ecosystem-contributions/issues/63#issuecomment-1610795492) to the RFP divided the project into several tasks:

* [T1: contract interface](https://github.com/EspressoSystems/op-leader-election/issues/2)
* [T2: basic PoC contract](https://github.com/EspressoSystems/op-leader-election/issues/3)
* [T3: batch submission updates](https://github.com/EspressoSystems/op-leader-election/issues/4)
* [T4: derivation pipeline updates](https://github.com/EspressoSystems/op-leader-election/issues/11)
* T5: basic testing

Several non-required extras were added as stretch tasks T6-T10:

* [T6: batch inbox address in system config](https://github.com/EspressoSystems/op-leader-election/issues/15)
* [T7: specification of a fee address set by sequencer](https://github.com/EspressoSystems/op-leader-election/issues/16)
* [T8: hardfork flag](https://github.com/EspressoSystems/op-leader-election/issues/17)
* [T9: alternative contract implementing interface](https://github.com/EspressoSystems/op-leader-election/issues/18)
* [T10: documentation](https://github.com/EspressoSystems/op-leader-election/issues/19)

Espresso's proposal was [selected](https://github.com/ethereum-optimism/ecosystem-contributions/issues/63#issuecomment-1640457319), and with the Cortado release, we have completed, or are about to complete, the specified tasks for the minimum viable fulfillment of the RFP. Further details and updates can be found in the [same GitHub issue](https://github.com/ethereum-optimism/ecosystem-contributions/issues/63#issuecomment-1668438963).
