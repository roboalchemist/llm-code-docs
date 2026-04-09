# Crate bellman 
Source 
## Modules§
domainThis module contains an `EvaluationDomain` abstraction for performing
various kinds of polynomial arithmetic on top of the scalar field.gadgetsSelf-contained sub-circuit implementations for various primitives.groth16The Groth16 proving system.multicoreAn interface for dealing with the kinds of parallel computations involved in
`bellman`. It’s currently just a thin wrapper around `rayon` but may be
extended in the future to allow for various parallelism strategies.multiexp
## Structs§
LinearCombinationThis represents a linear combination of some variables, with coefficients
in the scalar field of a pairing-friendly elliptic curve group.NamespaceThis is a “namespaced” constraint system which borrows a constraint system (pushing
a namespace context) and, when dropped, pops out of the namespace context.VariableRepresents a variable in our constraint system.
## Enums§
IndexRepresents the index of either an input variable or
auxiliary variable.SynthesisErrorThis is an error that could occur during circuit synthesis contexts,
such as CRS generation or proving.VerificationErrorAn error during verification.
## Traits§
CircuitComputations are expressed in terms of arithmetic circuits, in particular
rank-1 quadratic constraint systems. The `Circuit` trait represents a
circuit that can be synthesized. The `synthesize` method is called during
CRS generation and during proving.ConstraintSystemRepresents a constraint system which can have new variables
allocated and constrains between them formed.