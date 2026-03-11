# Source: https://docs.axonius.com/docs/beyondtrust-password-safe-integration.md

# BeyondTrust Password Safe Integration

The BeyondTrust Password Safe integration enables Axonius to securely pull privileged credentials from the **BeyondTrust Password Safe**. The integration ensures that privileged credentials are secured in the BeyondTrust Password Safe, rotated to meet company guidelines, and meet complexity requirements.

<Callout icon="📘" theme="info">
  Note

  This integration has only been tested and supported with version  22.1.0.441. Please contact [Axonius Support](mailto:support@axonius.com) if you have a different version and it is not functioning as expected.
</Callout>

## Description of Product Integration

Axonius uses the BeyondTrust Password Safe API  to fetch credentials from the BeyondTrust Password Safe. Refer to [Beyond Trust - Password Safe Administration guide](https://www.beyondtrust.com/docs/beyondinsight-password-safe/ps/admin/index.htm)

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your BeyondTrust Password Safe, you need to:

1. Install and configure **Beyond Trust Password Safe**.
2. The managed account must have API access enabled.
3. **Prerequisite**: make sure you  add an **Authentication rule for the API**  as detailed [here](https://www.beyondtrust.com/docs/beyondinsight-password-safe/ps/admin/configure-api-registration.htm)
4. The user (the user who creates the connection in Axonius) must have permission to access the managed account.
5. Enable and configure the [external password managers](/docs/managing-external-passwords) in Axonius.
6. Configure adapter connection credentials to fetch passwords from BeyondTrust Password Safe.

## Enable BeyondTrust Password Safe Integration

Enable BeyondTrust Password Safe integration and allow  Axonius to securely pull privileged credentials from the BeyondTrust Password Safe.
Following the guidelines in [Managing External Passwords](/docs/managing-external-passwords#beyondtrust-privileged-identity).

## Working with BeyondTrust Password Safe

Once the [BeyondTrust Password Safe integration](https://docs.axonius.com/docs/managing-external-passwords#beyondtrust-privileged-identity) is enabled in Axonius, a new BeyondTrust Password Safe icon will appear in all password fields when configuring adapters or Enforcement sets, allowing you to enter a password manually or to fetch the secret from BeyondTrust Password Safe.

<Image alt="BeyondTrustIPasswordSafeIcon" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrustIPasswordSafeIcon.png" />

To fetch the password from BeyondTrust Password Safe:

1. In a password field, click the BeyondTrust Password Safe icon.  If you have configured more than one password manager, click the vault icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select BeyondTrust Password Safe  from the drop-down. A BeyondTrust Password Safe dialog opens.

<Image alt="BeyondTRustPWDSFDial" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTRustPWDSFDial.png" />

2. In the dialog, specify the following parameters:
   1. **System name** *(required)* - The BeyondTrust system Name.
   2. **Account name** *(required)* - Your account name in BeyondTrust.
3. Click **Fetch**.

   * If the fetch is successful, a green indication will be displayed next to the BeyondTrust Password Safe icon.

   <Image alt="BeyondTrustGreen" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BeyondTrustGreen.png" />

   * If the fetch is unsuccessful, a red indication will be displayed next to the BeyondTrust Password Safe icon. Hovering over the BeyondTrust Password Safe icon will show the error.
     ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/BYTrusPWDSafeError.png)

<Callout icon="📘" theme="info">
  NOTE

  Typing or deleting any character in the textbox will change the password field back to a manual password input.
</Callout>