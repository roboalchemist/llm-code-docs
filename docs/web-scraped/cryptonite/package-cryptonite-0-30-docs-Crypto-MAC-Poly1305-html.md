# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html

Title: Crypto.MAC.Poly1305

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html

Markdown Content:
Contents

*   [Incremental MAC Functions](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#g:1)
*   [One-pass MAC function](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#g:2)

Description

Poly1305 implementation

Synopsis
*   type[Ctx](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Ctx) = [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:State "Crypto.MAC.Poly1305")
*   data[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:State)
*   newtype[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth) = [Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:Auth)[Bytes](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:Bytes "Data.ByteArray")
*   [authTag](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:authTag) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") b => b ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305")
*   [initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:initialize) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key => key ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:State "Crypto.MAC.Poly1305")
*   [update](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:update) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:State "Crypto.MAC.Poly1305") -> ba ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:State "Crypto.MAC.Poly1305")
*   [updates](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:updates) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba =>[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:State "Crypto.MAC.Poly1305") -> [ba] ->[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:State "Crypto.MAC.Poly1305")
*   [finalize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:finalize) :: [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:State "Crypto.MAC.Poly1305") ->[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305")
*   [auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:auth) :: ([ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba) => key -> ba ->[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305")

Documentation
-------------

type[Ctx](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html) = [State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:State "Crypto.MAC.Poly1305")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.Poly1305.html#Ctx)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Ctx)

Deprecated: use Poly1305 State instead

Poly1305 State. use State instead of Ctx

data[State](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.Poly1305.html#State)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:State)

Poly1305 State

This type is an instance of `ByteArrayAccess` for debugging purpose. Internal layout is architecture dependent, may contain uninitialized data fragments, and change in future versions. The bytearray should not be used as input to cryptographic algorithms.

newtype[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.Poly1305.html#Auth)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth)

Poly1305 Auth

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.Poly1305.html#line-57)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth)
Instance details
Defined in [Crypto.MAC.Poly1305](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:-61--61-) :: [Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305") ->[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:-47--61-) :: [Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305") ->[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:-47--61-)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq")[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.Poly1305.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth)
Instance details
Defined in [Crypto.MAC.Poly1305](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:rnf) :: [Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305") -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray")[Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.Poly1305.html#line-50)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth)
Instance details
Defined in [Crypto.MAC.Poly1305](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:length) :: [Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:withByteArray) :: [Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305") -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:copyByteArrayToPtr) :: [Auth](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#t:Auth "Crypto.MAC.Poly1305") ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#v:copyByteArrayToPtr)

[Incremental MAC Functions -------------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#g:1)[One-pass MAC function ---------------------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-Poly1305.html#g:2)
