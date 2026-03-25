pgp
# Module composed 
Source 
## Structs§
ArmorOptionsOptions for generating armored content.CleartextSignedMessageImplementation of a Cleartext Signed Message.DecryptionOptionsConfigure which encryption container types to decrypt, besides the standard “SEIPD” (v1 or v2).DetachedSignatureAn OpenPGP data signature that occurs outside an OpenPGP Message,
as a detached signature:EncryptionSeipdV1Configuration for a v1 SEIPD encrypted messageEncryptionSeipdV2Configuration for a v2 SEIPD encrypted messageKeyDetailsThis specifies associated user id and attribute components, plus some metadata for producing
a `SignedSecretKey`.MessageBuilderConstructs message from a given data source.NoEncryptionConfiguration for a message that won’t get encryptedPacketBodyReaderPubPrivIteratorConsumes a series of `Packet`s and transforms them into a series of composed
`PublicOrSecret` objects.RawSessionKeyA raw session key, must be kept secret.RingResultThis is what happens if you use `TheRing`.SecretKeyParamsParameters for the creation of a `SignedSecretKey`SecretKeyParamsBuilderBuilder for `SecretKeyParams`.SignatureParserConsumes a series of `Packet`s and transforms them into a series of `DetachedSignature`
objects.SignedKeyDetailsShared details between secret and public keys.SignedPublicKeyAn OpenPGP public key (“Transferable Public Key”, also known as an “OpenPGP certificate”).SignedPublicKeyParserParse a series of `Packet`s into a series of `SignedPublicKey` (Transferable Public Keys).SignedPublicSubKeyRepresents an OpenPGP public subkey, combined with signatures over it.SignedSecretKeyAn OpenPGP secret key (“Transferable Secret Key”), complete with self-signatures.SignedSecretKeyParserParse a series of `Packet`s into a series of `SignedSecretKey`.SignedSecretSubKeyRepresents an OpenPGP secret subkey, combined with signatures over it.SubkeyParamsParameters for the creation of a subkeySubkeyParamsBuilderBuilder for `SubkeyParams`.SymEncryptedProtectedDataReaderReads and decrypts a `SymEncryptedProtectedData`
packet.TheRingLike a key ring, but better, and more powerful, serving all your decryption needs.TryFromPublicOrSecretErrorError returned when trying to convert `PublicOrSecret` key
into the wrong type.
## Enums§
AnyA flexible representation of armored OpenPGP data.CompressedDataReaderReads and decompresses a `CompressedData` packet.DsaKeySizeDSA key sizeEdataRepresents encrypted dataEncryptionCapsA type to set a configuration for the two key flags
“encrypt communications” and “encrypt storage”.EskEncrypted Session KeyFullSignaturePacketA signature packet after reading the full messageInnerRingResultKeyTypeParameter to set the cipher of a key packetLimitedReaderLiteralDataReaderRead the underlying literal data.MessageAn OpenPGP messageMessageReaderThe inner reader type in a nested messagePlainSessionKeyDecrypted session key.PublicOrSecretA wrapper that contains either a `SignedPublicKey` or a `SignedSecretKey`.SecretKeyParamsBuilderErrorError type for SecretKeyParamsBuilderSignatureManyReaderSignaturePacketA signature packet before reading the full messageSubkeyParamsBuilderErrorError type for SubkeyParamsBuilderSubpacketConfigSubpacket configuration for a data signature (either in the context of a message, or as a
detached signature).SymEncryptedDataReaderReads and decrypts a legacy `SymEncryptedData` packet.VerificationResultThe result of signature verification
## Constants§
DEFAULT_PARTIAL_CHUNK_SIZEThe default chunk size for partial packets.
## Traits§
DebugBufReadDeserializableEncryptionCommon trait for all types of encryption that can happen in the context of a
`MessageBuilder`
## Functions§
decrypt_session_key_with_passwordDecrypts session key from SKESK packet.
## Type Aliases§
DummyReader