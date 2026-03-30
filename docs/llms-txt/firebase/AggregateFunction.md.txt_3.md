# Source: https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction.md.txt

# FirebaseFirestore Framework Reference

# AggregateFunction

    public class AggregateFunction : AggregateBridgeWrapper, @unchecked Sendable

Represents an aggregate function in a pipeline.

An `AggregateFunction` is a function that computes a single value from a set of input values.

`AggregateFunction`s are typically used in the `aggregate` stage of a pipeline.
- `


  ### [init(functionName:args:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction#/s:17FirebaseFirestore17AggregateFunctionC12functionName4argsACSS_SayAA10Expression_pGtcfc)


  ` Creates a new `AggregateFunction`.

  #### Declaration

  Swift

      public init(functionName: String, args: [https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Protocols/Expression.html])

  #### Parameters

  |---|---|
  | ` functionName ` | The name of the aggregate function. |
  | ` args ` | The arguments to the aggregate function. |

- `


  ### [as(_:)](https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Classes/AggregateFunction#/s:17FirebaseFirestore17AggregateFunctionC2asyAA07AliasedC0VSSF)


  ` Creates an `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs.html#/s:17FirebaseFirestore16AliasedAggregateV` from this aggregate function.

  #### Declaration

  Swift

      public func `as`(_ name: String) -> https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs.html#/s:17FirebaseFirestore16AliasedAggregateV

  #### Parameters

  |---|---|
  | ` name ` | The alias for the aggregate function. |

  #### Return Value

  An `https://firebase.google.com/docs/reference/swift/firebasefirestore/api/reference/Structs.html#/s:17FirebaseFirestore16AliasedAggregateV` with the given alias.