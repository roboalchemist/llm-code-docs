# Crate argon2 
Source 
## Re-exports§
`pub use password_hash;``password-hash`
## Structs§
Argon2Argon2 context.AssociatedDataAssociated dataBlockStructure for the (1 KiB) memory block implemented as 128 64-bit words.KeyIdKey identifierParamsArgon2 password hash parameters.ParamsBuilderBuilder for Argon2 `Params`.PasswordHash`password-hash`Password hash.
## Enums§
AlgorithmArgon2 primitive type: variants of the algorithm.ErrorError type.VersionVersion of the algorithm.
## Constants§
ARGON2D_IDENT`password-hash`Argon2d algorithm identifierARGON2ID_IDENT`password-hash`Argon2id algorithm identifierARGON2I_IDENT`password-hash`Argon2i algorithm identifierMAX_PWD_LENMaximum password length in bytes.MAX_SALT_LENMaximum salt length in bytes.MAX_SECRET_LENMaximum secret key length in bytes.MIN_SALT_LENMinimum salt length in bytes.RECOMMENDED_SALT_LENRecommended salt length for password hashing in bytes.
## Traits§
PasswordHasher`password-hash`Trait for password hashing functions.PasswordVerifier`password-hash`Trait for password verification.
## Type Aliases§
ResultResult with argon2’s `Error` type.