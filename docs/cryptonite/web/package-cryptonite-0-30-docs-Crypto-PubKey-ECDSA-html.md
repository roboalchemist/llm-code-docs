# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html

Title: Crypto.PubKey.ECDSA

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html

Markdown Content:
Documentation
-------------

class[EllipticCurveBasepointArith](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:EllipticCurveBasepointArith "Crypto.ECC") curve =>[EllipticCurveECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html) curve where[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#EllipticCurveECDSA)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:EllipticCurveECDSA)

Elliptic curves with ECDSA capabilities.

#### Instances

Instances details
[EllipticCurveECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:EllipticCurveECDSA "Crypto.PubKey.ECDSA")[Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#line-121)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:EllipticCurveECDSA)
Instance details
Defined in [Crypto.PubKey.ECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html)

Methods

[scalarIsValid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsValid) :: proxy [Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#scalarIsValid)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsValid)

[scalarIsZero](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsZero) :: proxy [Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#scalarIsZero)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsZero)

[scalarInv](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarInv) :: proxy [Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ([Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#scalarInv)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarInv)

[pointX](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:pointX) :: proxy [Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Point "Crypto.ECC")[Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ([Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P521R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P521R1 "Crypto.ECC")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#pointX)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:pointX)
[EllipticCurveECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:EllipticCurveECDSA "Crypto.PubKey.ECDSA")[Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#line-112)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:EllipticCurveECDSA)
Instance details
Defined in [Crypto.PubKey.ECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html)

Methods

[scalarIsValid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsValid) :: proxy [Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#scalarIsValid)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsValid)

[scalarIsZero](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsZero) :: proxy [Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#scalarIsZero)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsZero)

[scalarInv](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarInv) :: proxy [Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ([Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#scalarInv)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarInv)

[pointX](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:pointX) :: proxy [Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Point "Crypto.ECC")[Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ([Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P384R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P384R1 "Crypto.ECC")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#pointX)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:pointX)
[EllipticCurveECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:EllipticCurveECDSA "Crypto.PubKey.ECDSA")[Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#line-101)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:EllipticCurveECDSA)
Instance details
Defined in [Crypto.PubKey.ECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html)

Methods

[scalarIsValid](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsValid) :: proxy [Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#scalarIsValid)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsValid)

[scalarIsZero](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsZero) :: proxy [Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#scalarIsZero)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarIsZero)

[scalarInv](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarInv) :: proxy [Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC") ->[Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ([Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#scalarInv)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:scalarInv)

[pointX](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:pointX) :: proxy [Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC") ->[Point](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Point "Crypto.ECC")[Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC") ->[Maybe](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Maybe.html#t:Maybe "Data.Maybe") ([Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC")[Curve_P256R1](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Curve_P256R1 "Crypto.ECC")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#pointX)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:pointX)

[Public keys -----------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#g:1)[Private keys ------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#g:2)[Signatures ----------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#g:3)

data[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html) curve [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#Signature)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature)

Represent a ECDSA signature namely R and S.

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") ([Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC") curve) =>[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") ([Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#line-74)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.ECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:-61--61-) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:-47--61-) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:-47--61-)
[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show") ([Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC") curve) =>[Show](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:Show "Text.Show") ([Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#line-75)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.ECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html)

Methods

[showsPrec](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:showsPrec) :: [Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int") ->[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:showsPrec)

[show](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:show) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:show)

[showList](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:showList) :: [[Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve] ->[ShowS](https://hackage.haskell.org/package/base-4.14.1.0/docs/Text-Show.html#t:ShowS "Text.Show")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:showList)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq") ([Scalar](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-ECC.html#t:Scalar "Crypto.ECC") curve) =>[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq") ([Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.PubKey.ECDSA.html#line-77)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature)
Instance details
Defined in [Crypto.PubKey.ECDSA](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:rnf) :: [Signature](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#t:Signature "Crypto.PubKey.ECDSA") curve -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#v:rnf)

[Generation and verification ---------------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-PubKey-ECDSA.html#g:4)
