# Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html

Title: Crypto.Cipher.DES

URL Source: https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html

Markdown Content:
| License | BSD-style |
| --- |
| Maintainer | Vincent Hanquez <vincent@snarc.org> |
| Stability | stable |
| Portability | good |
| Safe Haskell | None |
| Language | Haskell2010 |

Crypto.Cipher.DES

Description

Documentation
-------------

data[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html)[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.DES.html#DES)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES)

DES Context

#### Instances

Instances details
[Eq](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Eq.html#t:Eq "Data.Eq")[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.DES.html#line-22)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES)
Instance details
Defined in [Crypto.Cipher.DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html)

Methods

[(==)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:-61--61-) :: [DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:-61--61-)

[(/=)](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:-47--61-) :: [DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[Bool](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Bool.html#t:Bool "Data.Bool")[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:-47--61-)
[Cipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:Cipher "Crypto.Cipher.Types")[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.DES.html#line-24)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES)
Instance details
Defined in [Crypto.Cipher.DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html)

Methods

[cipherInit](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cipherInit) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") key => key ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error")[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Base.html#cipherInit)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cipherInit)

[cipherName](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cipherName) :: [DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[String](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-String.html#t:String "Data.String")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Base.html#cipherName)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cipherName)

[cipherKeySize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cipherKeySize) :: [DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[KeySizeSpecifier](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:KeySizeSpecifier "Crypto.Cipher.Types")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Base.html#cipherKeySize)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cipherKeySize)
[BlockCipher](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:BlockCipher "Crypto.Cipher.Types")[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.DES.html#line-29)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES)
Instance details
Defined in [Crypto.Cipher.DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html)

Methods

[blockSize](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:blockSize) :: [DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[Int](https://hackage.haskell.org/package/base-4.14.1.0/docs/Data-Int.html#t:Int "Data.Int")[Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#blockSize)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:blockSize)

[ecbEncrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:ecbEncrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#ecbEncrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:ecbEncrypt)

[ecbDecrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:ecbDecrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#ecbDecrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:ecbDecrypt)

[cbcEncrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cbcEncrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[IV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:IV "Crypto.Cipher.Types")[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#cbcEncrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cbcEncrypt)

[cbcDecrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cbcDecrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[IV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:IV "Crypto.Cipher.Types")[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#cbcDecrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cbcDecrypt)

[cfbEncrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cfbEncrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[IV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:IV "Crypto.Cipher.Types")[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#cfbEncrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cfbEncrypt)

[cfbDecrypt](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cfbDecrypt) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[IV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:IV "Crypto.Cipher.Types")[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#cfbDecrypt)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:cfbDecrypt)

[ctrCombine](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:ctrCombine) :: [ByteArray](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArray "Data.ByteArray") ba =>[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") ->[IV](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:IV "Crypto.Cipher.Types")[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") -> ba -> ba [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#ctrCombine)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:ctrCombine)

[aeadInit](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:aeadInit) :: [ByteArrayAccess](https://hackage.haskell.org/package/memory-0.17.0/docs/Data-ByteArray.html#t:ByteArrayAccess "Data.ByteArray") iv =>[AEADMode](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:AEADMode "Crypto.Cipher.Types") ->[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES") -> iv ->[CryptoFailable](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Error.html#t:CryptoFailable "Crypto.Error") ([AEAD](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-Types.html#t:AEAD "Crypto.Cipher.Types")[DES](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#t:DES "Crypto.Cipher.DES")) [Source](https://hackage.haskell.org/package/cryptonite-0.30/docs/src/Crypto.Cipher.Types.Block.html#aeadInit)[#](https://hackage.haskell.org/package/cryptonite-0.30/docs/Crypto-Cipher-DES.html#v:aeadInit)
