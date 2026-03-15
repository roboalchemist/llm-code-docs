# Crate wolfssl 
Source 
## Structs§
Aes256GcmStruct for encrypt/decrypt using Aes256Gcm cipherChacha20Poly1305AeadStruct for encrypt/decrypt using Chacha20 cipher and authentication
using Poly1305ContextA wrapper around a `WOLFSSL_CTX`.ContextBuilderProduces a `Context` once built.RandomProvides a way to extract random values from WolfSSL.SessionWraps a `WOLFSSL` pointer, as well as the additional fields needed to
write into, and read from, wolfSSL’s custom IO callbacks.SessionConfigStores configurations we want to initialize a `Session` with.
## Enums§
Aes256GcmErrorThe failure result of an operation.CurveGroupCorresponds to the various defined `WOLFSSL_*` curvesErrorThe failure result of an operation.ErrorKindExtracts an error message given a wolfssl error enum.
Abstraction over WolfSSL errorsIOCallbackResultResult type to be returned by methods on `IOCallbacks`MethodCorresponds to the various `wolf*_{client,server}_method()` APIsNewContextBuilderErrorError creating a `ContextBuilder` object.NewSessionErrorError creating a `Session` object.PollThe `Result::Ok` for a non-blocking operation.ProtocolVersionTLS/DTLS protocol versionsRootCertificateDefines a CA certificateSecretDefines either a public or private keySslVerifyModeSSL Verification method
Ref: `https://www.wolfssl.com/doxygen/group__Setup.html#gaf9198658e31dd291088be18262ef2354`
## Traits§
IOCallbacksThe application provided IO callbacks documented at
`EmbedRecieve` (whose inputs and outputs we need to
emulate). See also `wolfSSL_CTX_SetIORecv` which is the best
docs for `wolfSSL_SSLSetIORecv` and `wolfSSL_SSLSetIOSend`,
which are what we actually use.
## Functions§
get_wolfssl_version_stringGet WolfSSL version via `LIBWOLFSSL_VERSION_STRING` header defined in wolfssl/version.h
## Type Aliases§
ResultDescribes an outcome that is synchronous.