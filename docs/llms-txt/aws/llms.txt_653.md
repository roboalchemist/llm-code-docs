# Source: https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/llms.txt

# AWS Payment Cryptography Data Plane API Reference

> You use the AWS Payment Cryptography Data Plane to manage how encryption keys are used for payment-related transaction processing and associated cryptographic operations. You can encrypt, decrypt, generate, verify, and translate payment-related cryptographic operations in AWS Payment Cryptography. For more information, see Data operations in the AWS Payment Cryptography User Guide.

- [Welcome](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/Welcome.html)

## [Actions](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Operations.html)

- [DecryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DecryptData.html): Decrypts ciphertext data to plaintext using a symmetric (TDES, AES), asymmetric (RSA), or derived (DUKPT or EMV) encryption key scheme.
- [EncryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EncryptData.html): Encrypts plaintext data to ciphertext using a symmetric (TDES, AES), asymmetric (RSA), or derived (DUKPT or EMV) encryption key scheme.
- [GenerateAs2805KekValidation](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateAs2805KekValidation.html): Generates a KekValidationRequest or a KekValidationResponse for node-to-node initialization between payment processing nodes using Australian Standard 2805 (AS2805).
- [GenerateCardValidationData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateCardValidationData.html): Generates card-related validation data using algorithms such as Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2), or Card Security Codes (CSC).
- [GenerateMac](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateMac.html): Generates a Message Authentication Code (MAC) cryptogram within AWS Payment Cryptography.
- [GenerateMacEmvPinChange](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GenerateMacEmvPinChange.html): Generates an issuer script mac for EMV payment cards that use offline PINs as the cardholder verification method (CVM).
- [GeneratePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_GeneratePinData.html): Generates pin-related data such as PIN, PIN Verification Value (PVV), PIN Block, and PIN Offset during new card issuance or reissuance.
- [ReEncryptData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_ReEncryptData.html): Re-encrypt ciphertext using DUKPT or Symmetric data encryption keys.
- [TranslateKeyMaterial](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslateKeyMaterial.html): Translates an cryptographic key between different wrapping keys without importing the key into AWS Payment Cryptography.
- [TranslatePinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslatePinData.html): Translates encrypted PIN block from and to ISO 9564 formats 0,1,3,4.
- [VerifyAuthRequestCryptogram](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyAuthRequestCryptogram.html): Verifies Authorization Request Cryptogram (ARQC) for a EMV chip payment card authorization.
- [VerifyCardValidationData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyCardValidationData.html): Verifies card-related validation data using algorithms such as Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2) and Card Security Codes (CSC).
- [VerifyMac](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyMac.html): Verifies a Message Authentication Code (MAC).
- [VerifyPinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VerifyPinData.html): Verifies pin-related data such as PIN and PIN Offset using algorithms including VISA PVV and IBM3624.


## [Data Types](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Types.html)

- [AmexAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_AmexAttributes.html): Parameters to derive the confidentiality and integrity keys for a payment card using Amex derivation method.
- [AmexCardSecurityCodeVersion1](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_AmexCardSecurityCodeVersion1.html): Card data parameters that are required to generate a Card Security Code (CSC2) for an AMEX payment card.
- [AmexCardSecurityCodeVersion2](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_AmexCardSecurityCodeVersion2.html): Card data parameters that are required to generate a Card Security Code (CSC2) for an AMEX payment card.
- [As2805KekValidationType](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_As2805KekValidationType.html): Parameter information for generating a random key for KEK validation to perform node-to-node initialization.
- [As2805PekDerivationAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_As2805PekDerivationAttributes.html): Parameter information to use a PEK derived using AS2805.
- [AsymmetricEncryptionAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_AsymmetricEncryptionAttributes.html): Parameters for plaintext encryption using asymmetric keys.
- [CardGenerationAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardGenerationAttributes.html): Card data parameters that are required to generate Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2), or Card Security Codes (CSC).
- [CardHolderVerificationValue](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardHolderVerificationValue.html): Card data parameters that are required to generate a cardholder verification value for the payment card.
- [CardVerificationAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationAttributes.html): Card data parameters that are requried to verify Card Verification Values (CVV/CVV2), Dynamic Card Verification Values (dCVV/dCVV2), or Card Security Codes (CSC).
- [CardVerificationValue1](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue1.html): Card data parameters that are required to verify CVV (Card Verification Value) for the payment card.
- [CardVerificationValue2](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CardVerificationValue2.html): Card data parameters that are required to verify Card Verification Value (CVV2) for the payment card.
- [CryptogramAuthResponse](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CryptogramAuthResponse.html): Parameters that are required for Authorization Response Cryptogram (ARPC) generation after Authorization Request Cryptogram (ARQC) verification is successful.
- [CryptogramVerificationArpcMethod1](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CryptogramVerificationArpcMethod1.html): Parameters that are required for ARPC response generation using method1 after ARQC verification is successful.
- [CryptogramVerificationArpcMethod2](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CryptogramVerificationArpcMethod2.html): Parameters that are required for ARPC response generation using method2 after ARQC verification is successful.
- [CurrentPinAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_CurrentPinAttributes.html): The parameter values of the current PIN to be changed on the EMV chip card.
- [DerivationMethodAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DerivationMethodAttributes.html): Parameters to derive the payment card specific confidentiality and integrity keys.
- [DiffieHellmanDerivationData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DiffieHellmanDerivationData.html): The shared information used when deriving a key using ECDH.
- [DiscoverDynamicCardVerificationCode](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DiscoverDynamicCardVerificationCode.html): Parameters that are required to generate or verify dCVC (Dynamic Card Verification Code).
- [DukptAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DukptAttributes.html): Parameters that are used for Derived Unique Key Per Transaction (DUKPT) derivation algorithm.
- [DukptDerivationAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DukptDerivationAttributes.html): Parameters required for encryption or decryption of data using DUKPT.
- [DukptEncryptionAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DukptEncryptionAttributes.html): Parameters that are required to encrypt plaintext data using DUKPT.
- [DynamicCardVerificationCode](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DynamicCardVerificationCode.html): Parameters that are required to generate or verify Dynamic Card Verification Value (dCVV).
- [DynamicCardVerificationValue](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DynamicCardVerificationValue.html): Parameters that are required to generate or verify Dynamic Card Verification Value (dCVV).
- [EcdhDerivationAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EcdhDerivationAttributes.html): Parameters required to establish ECDH based key exchange.
- [Emv2000Attributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Emv2000Attributes.html): Parameters to derive the confidentiality and integrity keys for a payment card using EMV2000 deruv.
- [EmvCommonAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EmvCommonAttributes.html): Parameters to derive the confidentiality and integrity keys for an Emv common payment card.
- [EmvEncryptionAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EmvEncryptionAttributes.html): Parameters for plaintext encryption using EMV keys.
- [EncryptionDecryptionAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EncryptionDecryptionAttributes.html): Parameters that are required to perform encryption and decryption operations.
- [Ibm3624NaturalPin](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Ibm3624NaturalPin.html): Parameters that are required to generate or verify Ibm3624 natural PIN.
- [Ibm3624PinFromOffset](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Ibm3624PinFromOffset.html): Parameters that are required to generate or verify Ibm3624 PIN from offset PIN.
- [Ibm3624PinOffset](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Ibm3624PinOffset.html): Pparameters that are required to generate or verify Ibm3624 PIN offset PIN.
- [Ibm3624PinVerification](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Ibm3624PinVerification.html): Parameters that are required to generate or verify Ibm3624 PIN verification PIN.
- [Ibm3624RandomPin](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_Ibm3624RandomPin.html): Parameters that are required to generate or verify Ibm3624 random PIN.
- [IncomingDiffieHellmanTr31KeyBlock](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_IncomingDiffieHellmanTr31KeyBlock.html): Parameter information of a TR31KeyBlock wrapped using an ECDH derived key.
- [IncomingKeyMaterial](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_IncomingKeyMaterial.html): Parameter information of the incoming WrappedKeyBlock containing the transaction key.
- [KekValidationRequest](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_KekValidationRequest.html): Parameter information for generating a KEK validation request during node-to-node initialization.
- [KekValidationResponse](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_KekValidationResponse.html): Parameter information for generating a KEK validation response during node-to-node initialization.
- [MacAlgorithmDukpt](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_MacAlgorithmDukpt.html): Parameters required for DUKPT MAC generation and verification.
- [MacAlgorithmEmv](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_MacAlgorithmEmv.html): Parameters that are required for EMV MAC generation and verification.
- [MacAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_MacAttributes.html): Parameters that are required for DUKPT, HMAC, or EMV MAC generation or verification.
- [MasterCardAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_MasterCardAttributes.html): Parameters to derive the confidentiality and integrity keys for a Mastercard payment card.
- [OutgoingKeyMaterial](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_OutgoingKeyMaterial.html): Parameter information of the outgoing TR31WrappedKeyBlock containing the transaction key.
- [OutgoingTr31KeyBlock](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_OutgoingTr31KeyBlock.html): Parameter information of the TR31WrappedKeyBlock containing the transaction key wrapped using a KEK.
- [PinData](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_PinData.html): Parameters that are required to generate, translate, or verify PIN data.
- [PinGenerationAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_PinGenerationAttributes.html): Parameters that are required for PIN data generation.
- [PinVerificationAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_PinVerificationAttributes.html): Parameters that are required for PIN data verification.
- [ReEncryptionAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_ReEncryptionAttributes.html): Parameters that are required to perform reencryption operation.
- [SessionKeyAmex](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyAmex.html): Parameters to derive session key for an Amex payment card.
- [SessionKeyDerivation](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyDerivation.html): Parameters to derive a session key for Authorization Response Cryptogram (ARQC) verification.
- [SessionKeyDerivationValue](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyDerivationValue.html): Parameters to derive session key value using a MAC EMV algorithm.
- [SessionKeyEmv2000](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyEmv2000.html): Parameters to derive session key for an Emv2000 payment card for ARQC verification.
- [SessionKeyEmvCommon](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyEmvCommon.html): Parameters to derive session key for an Emv common payment card for ARQC verification.
- [SessionKeyMastercard](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyMastercard.html): Parameters to derive session key for Mastercard payment card for ARQC verification.
- [SessionKeyVisa](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SessionKeyVisa.html): Parameters to derive session key for Visa payment card for ARQC verification.
- [SymmetricEncryptionAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_SymmetricEncryptionAttributes.html): Parameters requried to encrypt plaintext data using symmetric keys.
- [TranslationIsoFormats](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslationIsoFormats.html): Parameters that are required for translation between ISO9564 PIN block formats 0,1,3,4.
- [TranslationPinDataAs2805Format0](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslationPinDataAs2805Format0.html): Parameters that are required for translation between AS2805 PIN format 0 translation.
- [TranslationPinDataIsoFormat034](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslationPinDataIsoFormat034.html): Parameters that are required for translation between ISO9564 PIN format 0,3,4 translation.
- [TranslationPinDataIsoFormat1](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_TranslationPinDataIsoFormat1.html): Parameters that are required for ISO9564 PIN format 1 translation.
- [ValidationExceptionField](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_ValidationExceptionField.html): The request was denied due to an invalid request error.
- [VisaAmexDerivationOutputs](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VisaAmexDerivationOutputs.html): The attributes values used for Amex and Visa derivation methods.
- [VisaAttributes](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VisaAttributes.html): Parameters to derive the confidentiality and integrity keys for a Visa payment card.
- [VisaPin](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VisaPin.html): Parameters that are required to generate or verify Visa PIN.
- [VisaPinVerification](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VisaPinVerification.html): Parameters that are required to generate or verify Visa PIN.
- [VisaPinVerificationValue](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_VisaPinVerificationValue.html): Parameters that are required to generate or verify Visa PVV (PIN Verification Value).
- [WrappedKey](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_WrappedKey.html): Parameter information of a WrappedKeyBlock for encryption key exchange.
- [WrappedKeyMaterial](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_WrappedKeyMaterial.html): Parameter information of a WrappedKeyBlock for encryption key exchange.
- [WrappedWorkingKey](https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_WrappedWorkingKey.html): The parameter information of the outgoing wrapped key block.
