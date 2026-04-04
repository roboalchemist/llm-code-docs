# Source: https://docs.carv.io/carv-ecosystem/verifier-nodes/how-do-verifier-nodes-work/sgx-attestation-verification.md

# SGX Attestation Verification

## SGX Attestation Verification Flow

A SGX-based Gramine service generates a TEE attestation, which is uploaded to a smart contract. Verifiers are required to read and verify the TEE attestation. The verification process typically includes the following steps:

1. **Extract the Attestation**: Initially, extract the attestation data from the smart contract.
2. **Parse the Attestation**: Parse the extracted attestation data, which usually includes the report body, signature, and signing certificate.
   * **Report Body**: The main part of the report containing information about the execution environment, such as the security version number, attributes, attribute mask, and measurements.
   * **Report Data**: The data section of the report, containing user-defined data.
   * **Signature**: The signature over the report body and report data, used to verify the report's integrity and authenticity.
3. **Verify the Signature**: Check the validity of the attestation's signature. This often involves using the public key from the signing certificate to validate the signature.
4. **Certificate Chain Verification**: Confirm that the signing certificate's chain of trust is valid and issued by a trusted root certificate.
5. **Report Body Verification**: Analyze the information in the report body to ensure it meets the expected criteria, including:
   * **MRENCLAVE Verification**: Ensure the MRENCLAVE value in the report body matches the expected value to confirm the executed code is as intended.
   * **Timestamp**: Verify the timestamp of the report to ensure it is current.
   * **User Data Verification**: If user data is included in the report body, verify that this data meets the expected standards.

### Verification fields and methods

* **Signature Verification**: Validate the signature using the public key to ensure the attestation has not been tampered with.
* **Certificate Chain Verification**: Inspect the certificate chain to ensure the signing certificate is issued by a trusted CA.
* **MRENCLAVE Verification**: Compare the MRENCLAVE value in the report body with the expected value to ensure the correct executable code is loaded (to do in version 1).
* **Timestamp**: Check the report’s generation time to ensure the information is up to date.
* **User Data**: If applicable, verify the user-defined data in the report body.

## References

{% embed url="<https://github.com/intel/SGXDataCenterAttestationPrimitives/blob/main/SampleCode/RustQuoteVerificationSample/src/main.rshttps://github.com/intel/SGXDataCenterAttestationPrimitives/blob/main/QuoteVerification/dcap_quoteverify/sgx-dcap-quoteverify-rs/src/lib.rs>" %}

{% embed url="<https://github.com/intel/SGXDataCenterAttestationPrimitives/blob/main/QuoteVerification/dcap_quoteverify/sgx-dcap-quoteverify-rs/src/lib.rs>" %}
