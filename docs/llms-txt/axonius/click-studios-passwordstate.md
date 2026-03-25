# Source: https://docs.axonius.com/docs/click-studios-passwordstate.md

# Click Studios Passwordstate

The Click Studios Passwordstate integration enables Axonius to securely pull privileged credentials from  **Click Studios Passwordstate**. The integration helps to ensure that privileged credentials are secured in  **Click Studios Passwordstate**, rotated to meet company guidelines, and meet complexity requirements.

## Description of Product Integration

Axonius uses the Click Studios Passwordstate  API  to fetch credentials from  Passwordstate.
Axonius authenticates to Click Studios Passwordstate token authentication.

The credentials are only fetched by Axonius when:

* Creating a new adapter connection
* Updating an existing adapter connection
* Running an enforcement set
* Fetching asset information for adapters during discovery cycles

Axonius does not store the credentials anywhere and deletes any trace of credentials.

To enable fetching credentials from your Click Studios Passwordstate  Server, you need to:

1. Install and configure **Click Studios Passwordstate**
2. Enable and configure the **[External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords)** in Axonius.
3. Configure adapter connection credential to fetch passwords from Click Studios Passwordstate Server.

## Enable Click Studios Passwordstate Integration

Follow the guidelines in [External Password Managers - Enterprise Password Management Settings](/docs/managing-external-passwords#click-studios-passwordstate) to enable Click Studios Passwordstate integration and allow Axonius to securely pull privileged credentials from Click Studios Passwordstate.

## Working with  Click Studios Passwordstate

Once the [Click Studios Passwordstate integration is enabled](/docs/managing-external-passwords#click-studios-passwordstate) in Axonius, a new Click Studios Passwordstate icon will appear in all password fields when configuring adapters or configuring Enforcement sets, allowing you to enter a password manually or to fetch the secret from Click Studios Passwordstate.

<Image align="center" alt="clickstudio" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/clickstudio.png" />

To fetch the password from Click Studios Passwordstate:

1. In a password field, click the Click Studios Passwordstate icon.  If you have configured more than one password manager, click the vault icon ![](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Vaulticon.png) and select Click Studios Passwordstate from the drop-down. A Click Studios Passwordstate dialog opens.

<Image alt="clickstudipasswordstsate" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/clickstudipasswordstsate.png" />

2. In the dialog, specify the following parameters:
   1. **Password List ID** *(required)* - The ID of the list that contains the relevant password.

   2. **Password Title** *(required)* - The title for the relevant password.

3. Click **Fetch**.

   * If the fetch is successful, a green indication is displayed next to the Click Studios Passwordstate icon.  Hovering over the Click Studios Passwordstatet icon shows the credentials that you input.

   <Image align="center" alt="clickstudio" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/clickstudio.png" />

   * If the fetch is unsuccessful, a red indication is displayed next to the Click Studios Passwordstate icon. Hovering over the Click Studios Passwordstate icon shows the error.

   <Image align="center" alt="ClickSudioError" border={false} width="400px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/ClickSudioError.png" />

<Callout icon="📘" theme="info">
  Note

  Typing or deleting any character in the textbox will change the password field back to a manual password input.
</Callout>