# Source: https://docs.nomad.xyz/developers/node-operators/running-agents-guide/troubleshooting.md

# Troubleshooting

## Common Errors

### ProverSync found new root but could not find leaf under it

The `eth_getLogs` RPC call is used by Agents to query for events from a given EVM-compatible blockchain. This error manifests when an Agent is unable to locate a `Dispatch` event for a given message. This sometimes manifests on some novel EVM-compatible networks non-deterministically and can be hard to debug. \
\
The error lists the current root and the leaf index of the message that was not properly indexed. \
\
A special case of this Error is when the Agent cannot locate the first leaf with index `0`. This usually indicates a deviation from the behavior of an Ethereum Geth node, which has event data indexed in a separate data structure than block data.\
\
This is generally fixed by switching your RPC to an Archive node, such that all the required data to format the response to `eth_getLogs` is available at query-time. \
\
Below is an example of an error in this special case: &#x20;

> ProverSync found new root 0x6f46…504c but could not find leaf under it. Leaf index of missing leaf: 0.
