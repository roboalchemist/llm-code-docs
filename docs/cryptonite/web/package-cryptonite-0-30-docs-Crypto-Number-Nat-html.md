# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Nat.html

Title: Crypto.Number.Nat

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Nat.html

Markdown Content:
Description

Numbers at type level.

This module provides extensions to [GHC.TypeLits](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeLits.html) and [GHC.TypeNats](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html) useful to work with cryptographic algorithms parameterized with a variable bit length. Constraints like `IsDivisibleBy8 n` ensure that the type-level parameter is applicable to the algorithm.

Functions are also provided to test whether constraints are satisfied from values known at runtime. The following example shows how to discharge `IsDivisibleBy8` in a computation `fn` requiring this constraint:

withDivisibleBy8 :: Integer
                 -> (forall proxy n . (KnownNat n, IsDivisibleBy8 n) => proxy n -> a)
                 -> Maybe a
withDivisibleBy8 len fn = do
    SomeNat p <- someNatVal len
    Refl <- isDivisibleBy8 p
    pure (fn p)
Function `withDivisibleBy8` above returns `Nothing` when the argument `len` is negative or not divisible by 8.

Synopsis
*   type[IsDivisibleBy8](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Nat.html#t:IsDivisibleBy8) bitLen = IsDiv8 bitLen bitLen ~ '[True](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#v:True "Data.Bool")
*   type[IsAtMost](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Nat.html#t:IsAtMost) (bitlen :: [Nat](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:Nat "GHC.TypeNats")) (n :: [Nat](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:Nat "GHC.TypeNats")) = IsLE bitlen n (bitlen [<=?](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:-60--61--63- "GHC.TypeNats") n) ~ '[True](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#v:True "Data.Bool")
*   type[IsAtLeast](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Nat.html#t:IsAtLeast) (bitlen :: [Nat](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:Nat "GHC.TypeNats")) (n :: [Nat](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:Nat "GHC.TypeNats")) = IsGE bitlen n (n [<=?](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:-60--61--63- "GHC.TypeNats") bitlen) ~ '[True](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#v:True "Data.Bool")
*   [isDivisibleBy8](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Nat.html#v:isDivisibleBy8) :: [KnownNat](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:KnownNat "GHC.TypeNats") n => proxy n ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (IsDiv8 n n [:~:](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Type-Equality.html#t::-126-: "Data.Type.Equality") '[True](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#v:True "Data.Bool"))
*   [isAtMost](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Nat.html#v:isAtMost) :: ([KnownNat](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:KnownNat "GHC.TypeNats") value, [KnownNat](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:KnownNat "GHC.TypeNats") bound) => proxy value -> proxy' bound ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ((value [<=?](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:-60--61--63- "GHC.TypeNats") bound) [:~:](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Type-Equality.html#t::-126-: "Data.Type.Equality") '[True](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#v:True "Data.Bool"))
*   [isAtLeast](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Number-Nat.html#v:isAtLeast) :: ([KnownNat](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:KnownNat "GHC.TypeNats") value, [KnownNat](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:KnownNat "GHC.TypeNats") bound) => proxy value -> proxy' bound ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ((bound [<=?](https://hackage.haskell.org/package/base-4.14.1.0/docs/GHC-TypeNats.html#t:-60--61--63- "GHC.TypeNats") value) [:~:](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Type-Equality.html#t::-126-: "Data.Type.Equality") '[True](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#v:True "Data.Bool"))
