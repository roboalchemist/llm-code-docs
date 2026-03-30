# Crate pgp 
Source 
## Re-exports§
`pub use bytes;`
## Modules§
adapterAn abstraction to provide a signer that is compatible with rPGP, but backed by a Rust Crypto
`signature::Signer`.armorHandling of OpenPGP ASCII Armorbase64Handle base64, as used in `crate::armor`composedHandle OpenPGP objects that are composed of multiple packets, such as
Transferable Public Keys and Messages.cryptoLow-level cryptographic building blockserrorsrPGP errorsline_writerLine writer modulenormalize_linesLine ending normalization modulepacketPacket moduleserSerialize trait moduletypesrPGP types
## Constants§
MAX_BUFFER_SIZEDefault maximum size that gets buffered.VERSIONThe version of this crate.