# Source: https://docs.hypermode.com/dgraph/concepts/protocol-buffers.md

# Protocol Buffers

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

All data in Dgraph that is stored or transmitted among the Dgraph instances
(servers) is converted into space-optimized byte arrays using
[Protocol Buffers](https://developers.google.com/protocol-buffers/). Protocol
Buffers are a standard, optimized technology to speed up network communications.
