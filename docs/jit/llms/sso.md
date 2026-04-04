# Source: https://docs.jit.io/docs/sso.md

# SSO

# SSO Configuration

If your organization uses SSO, you can login to the Jit platform with it. The SSO feature is not enabled by default, and you’ll need to [contact us](https://www.jit.io/contact) to enable it.

Once SSO is enabled, go to the **Side bar → Users and permissions:**

![](https://files.readme.io/4275072-image.png)

This will open the user management popup, in which you should now see an SSO section:

![](https://files.readme.io/960b975-image.png)

Once there, click on “Setup SSO connection”. You will then need to choose your SAML / OpenID provider, and follow the instructions in the set up wizard.

Note that the setup required admin access to your SSO provider account, as well as permissions / access to adding the relevant DNS record for your SSO domain name.

![](https://files.readme.io/4f8c379-image.png)

![](https://files.readme.io/21ff37b-image.png)

Once you completed the process, you’ll be able to map groups from your SSO provider to roles in Jit:

![](https://files.readme.io/e9b36f8-image.png)

From now on, any user with an email in that SSO will be able to login to Jit, provided they were given a fitting role.