# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html

Title: Crypto.MAC.KMAC

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html

Markdown Content:
Description

Provide the KMAC (Keccak Message Authentication Code) algorithm, derived from the SHA-3 base algorithm Keccak and defined in NIST SP800-185.

Synopsis
*   class[HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a =>[HashSHAKE](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:HashSHAKE) a
*   [kmac](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:kmac) :: ([HashSHAKE](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:HashSHAKE "Crypto.MAC.KMAC") a, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") string, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba) => string -> key -> ba ->[KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a
*   newtype[KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC) a = [KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:KMAC) {
    *   [kmacGetDigest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:kmacGetDigest) :: [Digest](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash.html#t:Digest "Crypto.Hash") a

}
*   data[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:Context) a
*   [initialize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:initialize) :: forall a string key. ([HashSHAKE](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:HashSHAKE "Crypto.MAC.KMAC") a, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") string, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") key) => string -> key ->[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:Context "Crypto.MAC.KMAC") a
*   [update](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:update) :: ([HashSHAKE](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:HashSHAKE "Crypto.MAC.KMAC") a, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba) =>[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:Context "Crypto.MAC.KMAC") a -> ba ->[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:Context "Crypto.MAC.KMAC") a
*   [updates](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:updates) :: ([HashSHAKE](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:HashSHAKE "Crypto.MAC.KMAC") a, [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ba) =>[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:Context "Crypto.MAC.KMAC") a -> [ba] ->[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:Context "Crypto.MAC.KMAC") a
*   [finalize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:finalize) :: forall a. [HashSHAKE](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:HashSHAKE "Crypto.MAC.KMAC") a =>[Context](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:Context "Crypto.MAC.KMAC") a ->[KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a

Documentation
-------------

class[HashAlgorithm](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Hash-IO.html#t:HashAlgorithm "Crypto.Hash.IO") a =>[HashSHAKE](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html) a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Hash.SHAKE.html#HashSHAKE)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:HashSHAKE)

Type class of SHAKE algorithms.

Minimal complete definition

cshakeInternalFinalize, cshakeOutputLength

newtype[KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html) a [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.KMAC.html#KMAC)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC)

Represent a KMAC that is a phantom type with the hash used to produce the mac.

The Eq instance is constant time. No Show instance is provided, to avoid printing by mistake.

Constructors

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq") ([KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.KMAC.html#line-81)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC)
Instance details
Defined in [Crypto.MAC.KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:-61--61-) :: [KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a ->[KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:-47--61-) :: [KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a ->[KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:-47--61-)
[NFData](https://hackage.haskell.org/package/deepseq-1.4.4.0/docs/Control-DeepSeq.html#t:NFData "Control.DeepSeq") ([KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.KMAC.html#line-79)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC)
Instance details
Defined in [Crypto.MAC.KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html)

Methods

[rnf](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:rnf) :: [KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a -> () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:rnf)
[ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") ([KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.MAC.KMAC.html#line-79)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC)
Instance details
Defined in [Crypto.MAC.KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html)

Methods

[length](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:length) :: [KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:length)

[withByteArray](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:withByteArray) :: [KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a -> ([Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a0) ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") a0 [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:withByteArray)

[copyByteArrayToPtr](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:copyByteArrayToPtr) :: [KMAC](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#t:KMAC "Crypto.MAC.KMAC") a ->[Ptr](https://hackage.haskell.org/package/base-4.14.1.0/docs/Foreign-Ptr.html#t:Ptr "Foreign.Ptr") p ->[IO](https://hackage.haskell.org/package/base-4.14.1.0/docs/System-IO.html#t:IO "System.IO") () [#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#v:copyByteArrayToPtr)

[Incremental -----------](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-MAC-KMAC.html#g:1)
