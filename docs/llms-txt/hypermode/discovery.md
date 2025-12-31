# Source: https://docs.hypermode.com/dgraph/concepts/discovery.md

# Discovery

<Info>
  We're overhauling Dgraph's docs to make them clearer and more approachable. If
  you notice any issues during this transition or have suggestions, please
  [let us know](https://github.com/hypermodeinc/docs/issues).
</Info>

### New servers and discovery

Dgraph clusters detects new machines allocated to the
[cluster](/dgraph/self-managed/cluster-setup), establish connections, and
transfer data to the new server based on the group the new machine is in.
