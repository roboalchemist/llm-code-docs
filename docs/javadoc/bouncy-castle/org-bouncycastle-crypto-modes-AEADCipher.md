JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

**Bouncy Castle Cryptography Library 1.83**

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

org.bouncycastle.crypto.modes

## Interface AEADCipher

- 

All Known Subinterfaces:
AEADBlockCipher, CCMModeCipher, GCMModeCipher

All Known Implementing Classes:
AsconAEAD128, AsconEngine, CCMBlockCipher, ChaCha20Poly1305, EAXBlockCipher, ElephantEngine, GCMBlockCipher, GCMSIVBlockCipher, GiftCofbEngine, Grain128AEADEngine, ISAPEngine, KCCMBlockCipher, KGCMBlockCipher, OCBBlockCipher, PhotonBeetleEngine, RomulusEngine, SparkleEngine, XoodyakEngine

---

```
public interface AEADCipher
```

A cipher mode that includes authenticated encryption with a streaming mode and optional associated data.
 

 Implementations of this interface may operate in a packet mode (where all input data is buffered and 
 processed during the call to `doFinal(byte[], int)`), or in a streaming mode (where output data is
 incrementally produced with each call to `processByte(byte, byte[], int)` or 
 `processBytes(byte[], int, int, byte[], int)`.
 
 This is important to consider during decryption: in a streaming mode, unauthenticated plaintext data
 may be output prior to the call to `doFinal(byte[], int)` that results in an authentication
 failure. The higher level protocol utilising this cipher must ensure the plaintext data is handled 
 appropriately until the end of data is reached and the entire ciphertext is authenticated.

See Also:
`AEADParameters`

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method and Description

`int`
`doFinal(byte[] out,
       int outOff)`
Finish the operation either appending or verifying the MAC at the end of the data.

`java.lang.String`
`getAlgorithmName()`
Return the name of the algorithm.

`byte[]`
`getMac()`
Return the value of the MAC associated with the last stream processed.

`int`
`getOutputSize(int len)`
return the size of the output buffer required for a processBytes plus a
 doFinal with an input of len bytes.

`int`
`getUpdateOutputSize(int len)`
return the size of the output buffer required for a processBytes
 an input of len bytes.

`void`
`init(boolean forEncryption,
    CipherParameters params)`
initialise the underlying cipher.

`void`
`processAADByte(byte in)`
Add a single byte to the associated data check.

`void`
`processAADBytes(byte[] in,
               int inOff,
               int len)`
Add a sequence of bytes to the associated data check.

`int`
`processByte(byte in,
           byte[] out,
           int outOff)`
encrypt/decrypt a single byte.

`int`
`processBytes(byte[] in,
            int inOff,
            int len,
            byte[] out,
            int outOff)`
process a block of bytes from in putting the result into out.

`void`
`reset()`
Reset the cipher.

- 

  - 

### Method Detail

    - 

#### init

```
void init(boolean forEncryption,
          CipherParameters params)
   throws java.lang.IllegalArgumentException
```

initialise the underlying cipher. Parameter can either be an AEADParameters or a ParametersWithIV object.

Parameters:
`forEncryption` - true if we are setting up for encryption, false otherwise.
`params` - the necessary parameters for the underlying cipher to be initialised.
Throws:
`java.lang.IllegalArgumentException` - if the params argument is inappropriate.

    - 

#### getAlgorithmName

```
java.lang.String getAlgorithmName()
```

Return the name of the algorithm.

Returns:
the algorithm name.

    - 

#### processAADByte

```
void processAADByte(byte in)
```

Add a single byte to the associated data check.
 
If the implementation supports it, this will be an online operation and will not retain the associated data.

Parameters:
`in` - the byte to be processed.

    - 

#### processAADBytes

```
void processAADBytes(byte[] in,
                     int inOff,
                     int len)
```

Add a sequence of bytes to the associated data check.
 
If the implementation supports it, this will be an online operation and will not retain the associated data.

Parameters:
`in` - the input byte array.
`inOff` - the offset into the in array where the data to be processed starts.
`len` - the number of bytes to be processed.

    - 

#### processByte

```
int processByte(byte in,
                byte[] out,
                int outOff)
         throws DataLengthException
```

encrypt/decrypt a single byte.

Parameters:
`in` - the byte to be processed.
`out` - the output buffer the processed byte goes into.
`outOff` - the offset into the output byte array the processed data starts at.
Returns:
the number of bytes written to out.
Throws:
`DataLengthException` - if the output buffer is too small.

    - 

#### processBytes

```
int processBytes(byte[] in,
                 int inOff,
                 int len,
                 byte[] out,
                 int outOff)
          throws DataLengthException
```

process a block of bytes from in putting the result into out.

Parameters:
`in` - the input byte array.
`inOff` - the offset into the in array where the data to be processed starts.
`len` - the number of bytes to be processed.
`out` - the output buffer the processed bytes go into.
`outOff` - the offset into the output byte array the processed data starts at.
Returns:
the number of bytes written to out.
Throws:
`DataLengthException` - if the output buffer is too small.

    - 

#### doFinal

```
int doFinal(byte[] out,
            int outOff)
     throws java.lang.IllegalStateException,
            InvalidCipherTextException
```

Finish the operation either appending or verifying the MAC at the end of the data.

Parameters:
`out` - space for any resulting output data.
`outOff` - offset into out to start copying the data at.
Returns:
number of bytes written into out.
Throws:
`java.lang.IllegalStateException` - if the cipher is in an inappropriate state.
`InvalidCipherTextException` - if the MAC fails to match.

    - 

#### getMac

```
byte[] getMac()
```

Return the value of the MAC associated with the last stream processed.

Returns:
MAC for plaintext data.

    - 

#### getUpdateOutputSize

```
int getUpdateOutputSize(int len)
```

return the size of the output buffer required for a processBytes
 an input of len bytes.
 

 The returned size may be dependent on the initialisation of this cipher
 and may not be accurate once subsequent input data is processed - this method
 should be invoked immediately prior to input data being processed.
 

Parameters:
`len` - the length of the input.
Returns:
the space required to accommodate a call to processBytes
 with len bytes of input.

    - 

#### getOutputSize

```
int getOutputSize(int len)
```

return the size of the output buffer required for a processBytes plus a
 doFinal with an input of len bytes.
 

 The returned size may be dependent on the initialisation of this cipher
 and may not be accurate once subsequent input data is processed - this method
 should be invoked immediately prior to a call to final processing of input data
 and a call to `doFinal(byte[], int)`.
 

Parameters:
`len` - the length of the input.
Returns:
the space required to accommodate a call to processBytes and doFinal
 with len bytes of input.

    - 

#### reset

```
void reset()
```

Reset the cipher. After resetting the cipher is in the same state
 as it was after the last init (if there was one).

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

**Bouncy Castle Cryptography Library 1.83**

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method