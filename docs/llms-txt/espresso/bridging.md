# Source: https://docs.espressosys.com/network/appendix/interacting-with-l1/bridging.md

# Bridging

Rollup state updates facilitate interoperability between the layer 1 and the rollup. If the state of the rollup is verified and stored by the layer 1, then the layer 1 can also validate claims against that state, such as a claim that some tokens have been deposited into a bridge contract on the rollup. The L1 can also *write* to the state which is maintained by the L1, and the rollup can thus receive messages and tokens from the L1.

This is the idea used by the [LX-to-LY bridge](https://docs.hermez.io/zkEVM/Overview/Overview/#the-lx-to-ly-bridge), which [Polygon zkEVM](https://wiki.polygon.technology/docs/zkEVM) uses to bridge ETH between the layer 1 and layer 2. In this design, part of the L1 state, a Merkle tree of messages to be sent to the L2, is represented directly in the L2 VM semantics. Since the canonical execution of L2 transactions happens in a smart contract on the L1, this executor is able to read from the appropriate L1 state when executing operations in the L2 VM.
