# Source: https://help.aikido.dev/getting-started/automated-user-management/saml-login/microsoft-azure-custom-attributes-with-saml-entra-id.md

# Microsoft Azure: Custom Attributes with SAML /Entra ID

First, make sure you have SAML login working using following guide:

[https://help.aikido.dev/doc/microsoft-azure-login-with-saml--entra-id/doc74BfKR60Z](https://help.aikido.dev/getting-started/automated-user-management/saml-login/microsoft-azure-login-with-saml-entra-id)

### Setting up Azure Group based SAML custom attributes <a href="#setting-up-azure-group-based-saml-custom-attributes" id="setting-up-azure-group-based-saml-custom-attributes"></a>

1. Go to the application registration

   ![Azure portal view for managing Aikido-SSO enterprise application properties and settings.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-8ae302f9235687b459c2ba2701289c48f38f2aa0%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_62b626cc-9385-45bc-9fff-35344531e015.jpg?alt=media)
2. Create an app role.**value** here should be the value of the claim. In this example, we're setting up for `aikido_role`, so valid values for this are `admin`, `default`, `team_only`.

   ![Creating a new app role "Aikido Admin" in Microsoft Azure for Aikido-SSO.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-78e993105cc638717163210b2b3a28878554aa15%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_88ff497f-e551-4c8e-8abb-445c5d69bf5a.jpg?alt=media)
3. After saving, go back to the app settings, and add a group to 'Users and Groups'

   ![Azure portal: Assign users or groups to the Aikido-SSO enterprise application.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-0faef4fdf1540f2b60462f4241e99cf71d8e5ffb%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_1e4e94af-0c14-4f6f-81a9-30c75166cf58.png?alt=media)
4. Add the Entra group you'd like to give admin access (in this case) and add the role we created in step 2.

   ![Azure Add Assignment: Select users, groups, and roles for directory permissions.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a11449ba5258733300a9c54341186ed6376fb916%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_8e32309f-84be-45d0-87d6-972bb1857a3a.png?alt=media)
5. Back in the Single Sign-on settings of the app, go to the Attributes & Claims -> Edit

   ![Azure portal SAML-based single sign-on configuration for Aikido-SSO application.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-a05c51da649be812679cfc6144889782075725d9%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_ffa0ee52-da46-4747-8542-2cddee420427.png?alt=media)
6. Click 'Add new claim'

   ![Azure portal Attributes & Claims page for adding and managing SAML claims.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-7cd3122ee7a99d6a9941025423a70b7812407d34%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_e7012a33-19d0-4a01-9a12-f17231dff1e4.png?alt=media)
7. Fill in the attribute name & user.assignedroles as source attribute. (this is the `admin` value we set up in step 2)

   ![Azure claim setup: mapping "aikido\_role" to "user.assignedroles" attribute.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-e9f3c593cdd24ba6b70e09564291cedf58661d9d%2Fmicrosoft-azure-custom-attributes-with-saml-entra-id_02e6788a-d5d8-4bc8-b2c8-7f3371441391.png?alt=media)
8. All done. On SAML login, these changes will take effect.
