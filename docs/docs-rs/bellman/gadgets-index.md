bellman
# Module gadgets 
Source 
## Modules§
blake2sThe BLAKE2s hash function with personalization support.booleanGadgets for allocating bits in the circuit and performing boolean logic.lookupWindow table lookup gadgets.multieqmultipackHelpers for packing vectors of bits into scalar field elements.numGadgets representing numbers in the scalar field of the underlying curve.sha256Circuits for the SHA-256 hash function and its internal compression
function.testHelpers for testing circuit implementations.uint32Circuit representation of a `u32`, with helpers for the `sha256`
gadgets.
## Traits§
AssignmentThis basically is just an extension to `Option`
which allows for a convenient mapping to an
error on `None`.