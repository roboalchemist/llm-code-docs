# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/partnerships/partner-onboarding-requirements.mdx

***

## stoplight-id: 40d8fd1ab2c13

# Onboarding Requirements

Cash App Pay's Partner engineering team requires the following details from you to complete this integration:

* **Account configuration details:** You must send the Partner Engagement team these details, so that they can get started on creating a developer account for you:

  * **App Display Name:** The formal name of the integration. It should be representative of your brand to preserve continuity between your application and Cash App authorization screens. It is shown to Cash App customers during the Authorization flow and then subsequently in their list of authorized integrations.
  * **App Icon:** It should match graphical assets used for your existing application but formatted to be 512x512, in PNG format and be representative of your brand to preserve continuity between your application and Cash App authorization screens. It is shown to Cash App customers during the Authorization flow and then subsequently in their list of authorized integrations.

* **SFTP server details for settlement configuration:** Cash App settles captured payments with the PSP (Payment Service Provider) via ACH using a batch process. Cash App captures the transaction-level details of each settlement as a reconciliation report and this report is uploaded daily to a client-provided SFTP server.
  To enable this for you, we require the following details:
  * **SFTP Hostname:** The host address for the partner-owned SFTP server.
  * **SFTP Port:** The port for the partner-owned SFTP server.
  * **Username:** The username for the partner-owned SFTP server.
  * **SFTP user’s private key:** The private RSA key of the provided user for the partner-owned SFTP server.
  * **SFTP server host’s public key:** The public RSA key of the server host for the partner-owned SFTP server.
  * **Destination folder path for settlement reports:** The file path where settlement reconciliation files will be uploaded to on a daily basis.(relative path from your home directory)
  * **Destination folder path for dispute reports:** The file path where dispute reconciliation files will be uploaded to on a daily basis.(relative path from your home directory)

* **Bank account details (Production only):** In Production, you must connect a bank account to receive incoming funds. Our Partner Engineers will work directly with you to securely collect and store these details:
  * **Account Name:** The name of the destination bank where the funds will be deposited via ACH (required).
  * **Account Number:** The account number of the destination bank where the funds will be deposited via ACH (required).
  * **Routing Number:** The routing number of the destination bank where the funds will be deposited via ACH (required).
  * **ACH Company ID:** The 10-digit unique identifier used for identifying entities collecting payments via ACH debit.

## Partner Certification

To take payments from Cash App Pay in production, Cash App’s Partner Engineering team will certify your integration to ensure that integration best practices are followed. This ensures that our mutual merchants and customers have a delightful commerce experience while using Cash App Pay.

<Note>
  Ask the Partner Engineering team for the Partner Certification checklist file.
</Note>
