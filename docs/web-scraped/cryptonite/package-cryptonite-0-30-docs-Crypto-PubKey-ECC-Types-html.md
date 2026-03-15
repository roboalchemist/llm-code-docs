# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html

Title: Crypto.PubKey.ECC.Types

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html

Markdown Content:
Contents

*   [Recommended curves definition](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#g:1)

Description

Synopsis
*   data[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve)
    *   = [CurveF2m](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:CurveF2m)[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")
    *   | [CurveFP](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:CurveFP)[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")

*   data[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point)
    *   = [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:Point)[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   | [PointO](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:PointO)

*   type[PublicPoint](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:PublicPoint) = [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")
*   type[PrivateNumber](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:PrivateNumber) = [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   data[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary) = [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:CurveBinary)[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")
*   data[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime) = [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:CurvePrime)[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")
*   [common_curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:common_curve) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")
*   [curveSizeBits](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:curveSizeBits) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")
*   [ecc_fx](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:ecc_fx) :: [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   [ecc_p](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:ecc_p) :: [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") ->[Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
*   data[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon) = [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:CurveCommon) {
    *   [ecc_a](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:ecc_a) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [ecc_b](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:ecc_b) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [ecc_g](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:ecc_g) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")
    *   [ecc_n](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:ecc_n) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")
    *   [ecc_h](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:ecc_h) :: [Integer](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Integer "Prelude")

}
*   data[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName)
    *   = [SEC_p112r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p112r1)
    *   | [SEC_p112r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p112r2)
    *   | [SEC_p128r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p128r1)
    *   | [SEC_p128r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p128r2)
    *   | [SEC_p160k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p160k1)
    *   | [SEC_p160r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p160r1)
    *   | [SEC_p160r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p160r2)
    *   | [SEC_p192k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p192k1)
    *   | [SEC_p192r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p192r1)
    *   | [SEC_p224k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p224k1)
    *   | [SEC_p224r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p224r1)
    *   | [SEC_p256k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p256k1)
    *   | [SEC_p256r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p256r1)
    *   | [SEC_p384r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p384r1)
    *   | [SEC_p521r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_p521r1)
    *   | [SEC_t113r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t113r1)
    *   | [SEC_t113r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t113r2)
    *   | [SEC_t131r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t131r1)
    *   | [SEC_t131r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t131r2)
    *   | [SEC_t163k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t163k1)
    *   | [SEC_t163r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t163r1)
    *   | [SEC_t163r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t163r2)
    *   | [SEC_t193r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t193r1)
    *   | [SEC_t193r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t193r2)
    *   | [SEC_t233k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t233k1)
    *   | [SEC_t233r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t233r1)
    *   | [SEC_t239k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t239k1)
    *   | [SEC_t283k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t283k1)
    *   | [SEC_t283r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t283r1)
    *   | [SEC_t409k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t409k1)
    *   | [SEC_t409r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t409r1)
    *   | [SEC_t571k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t571k1)
    *   | [SEC_t571r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:SEC_t571r1)

*   [getCurveByName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:getCurveByName) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")

Documentation
-------------

data[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#Curve)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve)

Define either a binary curve or a prime curve.

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") -> c [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") -> m [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") -> m [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") -> m [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-36)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show) :: [Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList) :: [[Curve](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Curve "Crypto.PubKey.ECC.Types")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList)

data[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#Point)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point)

Define a point on a curve.

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") -> c [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") -> m [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") -> m [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") -> m [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-47)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList) :: [[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-49)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:rnf) :: [Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:Point "Crypto.PubKey.ECC.Types") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:rnf)

data[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#CurveBinary)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary)

Define an elliptic curve in 𝔽(2^m). The firt parameter is the Integer representatioin of the irreducible polynomial f(x).

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-56)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-) :: [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-) :: [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-56)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") -> c [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr) :: [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf) :: [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") -> m [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") -> m [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") -> m [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-56)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-56)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show) :: [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList) :: [[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-58)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:rnf) :: [CurveBinary](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveBinary "Crypto.PubKey.ECC.Types") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:rnf)

data[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#CurvePrime)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime)

Define an elliptic curve in 𝔽p. The first parameter is the Prime Number.

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-64)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-) :: [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-) :: [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-64)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") -> c [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr) :: [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf) :: [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") -> m [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") -> m [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") -> m [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-64)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-64)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show) :: [CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList) :: [[CurvePrime](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurvePrime "Crypto.PubKey.ECC.Types")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList)

data[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#CurveCommon)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon)

Define common parameters in a curve definition of the form: y^2 = x^3 + ax + b.

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-87)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-) :: [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-) :: [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-87)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") -> c [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr) :: [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf) :: [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") -> m [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") -> m [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") -> m [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-87)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-87)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show) :: [CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList) :: [[CurveCommon](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveCommon "Crypto.PubKey.ECC.Types")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList)

[Recommended curves definition -----------------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#g:1)

data[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#CurveName)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName)

Define names for known recommended curves.

Constructors

[SEC_p112r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p112r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p128r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p128r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p160k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p160r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p160r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p192k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p192r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p224k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p224r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p256k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p256r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p384r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_p521r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t113r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t113r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t131r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t131r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t163k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t163r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t163r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t193r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t193r2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t233k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t233r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t239k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t283k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t283r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t409k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t409r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t571k1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)
[SEC_t571r1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

#### Instances

Instances details
[Bounded](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Bounded "Prelude")[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-124)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[minBound](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:minBound) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:minBound)

[maxBound](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:maxBound) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:maxBound)
[Enum](https://hackage.haskell.org/package/base-4.14.1.0/docs/Prelude.html#t:Enum "Prelude")[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-124)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[succ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:succ) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:succ)

[pred](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:pred) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:pred)

[toEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toEnum) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toEnum)

[fromEnum](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:fromEnum) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:fromEnum)

[enumFrom](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:enumFrom) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> [[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:enumFrom)

[enumFromThen](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:enumFromThen) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> [[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:enumFromThen)

[enumFromTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:enumFromTo) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> [[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:enumFromTo)

[enumFromThenTo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:enumFromThenTo) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> [[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:enumFromThenTo)
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-124)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-47--61-)
[Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data")[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-124)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[gfoldl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl) :: (forall d b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (d -> b) -> d -> c b) -> (forall g. g -> c g) ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> c [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gfoldl)

[gunfold](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold) :: (forall b r. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => c (b -> r) -> c r) -> (forall r. r -> c r) ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data") -> c [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gunfold)

[toConstr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[Constr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Constr "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:toConstr)

[dataTypeOf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[DataType](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:DataType "Data.Data")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataTypeOf)

[dataCast1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => c (t d)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast1)

[dataCast2](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2) :: [Typeable](https://hackage.haskell.org/package/base-4.14.1.0/docs/Type-Reflection.html#t:Typeable "Type.Reflection") t => (forall d e. ([Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d, [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") e) => c (t d e)) ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") (c [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")) [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:dataCast2)

[gmapT](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT) :: (forall b. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") b => b -> b) ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapT)

[gmapQl](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl) :: (r -> r' -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQl)

[gmapQr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr) :: forall r r'. (r' -> r -> r) -> r -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> r') ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> r [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQr)

[gmapQ](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ) :: (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> [u] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQ)

[gmapQi](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") -> (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> u) ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> u [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapQi)

[gmapM](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM) :: [Monad](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:Monad "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> m [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapM)

[gmapMp](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> m [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMp)

[gmapMo](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo) :: [MonadPlus](https://hackage.haskell.org/package/base-4.14.1.0/docs/Control-Monad.html#t:MonadPlus "Control.Monad") m => (forall d. [Data](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Data.html#t:Data "Data.Data") d => d -> m d) ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") -> m [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:gmapMo)
[Ord](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ord "Data.Ord")[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-124)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[compare](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:compare) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[Ordering](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Ord.html#t:Ordering "Data.Ord")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:compare)

[(<)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-60-) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-60-)

[(<=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-60--61-) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-60--61-)

[(>)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-62-) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-62-)

[(>=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-62--61-) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:-62--61-)

[max](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:max) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:max)

[min](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:min) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:min)
[Read](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Read.html#t:Read "Text.Read")[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-124)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[readsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP")[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readsPrec)

[readList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList) :: [ReadS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadP.html#t:ReadS "Text.ParserCombinators.ReadP") [[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readList)

[readPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec")[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readPrec)

[readListPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec) :: [ReadPrec](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-ParserCombinators-ReadPrec.html#t:ReadPrec "Text.ParserCombinators.ReadPrec") [[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")] [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:readListPrec)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show")[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECC.Types.html#line-124)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName)
Instance details
Defined in [Crypto.PubKey.ECC.Types](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show) :: [CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList) :: [[CurveName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#t:CurveName "Crypto.PubKey.ECC.Types")] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECC-Types.html#v:showList)
