# Source: https://docs.curator.interworks.com/creating_integrations/thoughtspot_connection/integrating_thoughtspot_with_curator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integrating ThoughtSpot with Curator

> Connect and integrate your ThoughtSpot instance with Curator for unified analytics access

You can follow this guide to connect to your ThoughtSpot instance to Curator.

## Preparing ThoughtSpot

1. Verify your ThoughtSpot admin has enabled either [SAML SSO](https://developers.thoughtspot.com/docs/saml-sso) or
   [trusted authentication](https://developers.thoughtspot.com/docs/trusted-auth).  If you are using trusted
   authentication, have the *secret\_key* ready to add to the Curator configuration.
2. Verify your ThoughtSpot admin has configured your Curator domain to be
   [whitelisted for CORS and CSP](https://developers.thoughtspot.com/docs/security-settings).
3. Have the credentials for a user with administrator access on the intended Org ready to add to the Curator configuration.

Note: The user with administrator access to the intended Org must also exist on the "Primary" Org. This is due to a
limitation in the ThoughtSpot REST API where we can only query user details when we know the Org ID the user exists
on. The "Primary" Org ID is always the same so we can confidently pull the user details when they exist there, but
other Orgs have randomly generated ID's that aren't available in the ThoughtSpot UI anywhere. While the user must
exist on the "Primary" Org for Curator to be able to pull its details, it doesn't need to be an admin there, only
on the intended Org.

## Connect to Curator

1. Go to the backend of your Curator instance.  Navigate to Integrations > Connections using the left-hand menu.
2. Click the new New Connection button on the top of the page.
3. Enter a name for the connection (something like "ThoughtSpot" is sufficient) and edit the slug if you'd like (but
   you don't need to).
4. Choose "ThoughtSpot in the Platform dropdown.  If the option is disabled then you already have a ThoughtSpot
   Connection  created.
5. Fill out the form that appears below the Platform dropdown:
   * **ThoughtSpot URL**: The full URL to for your ThoughtSpot instance.
     e.g. [https://example.thoughtspot.cloud](https://example.thoughtspot.cloud)
   * **REST Connection Username**: The username for a ThoughtSpot administrator.
   * **REST Connection Password**: The password for a ThoughtSpot administrator.
   * **Use Trusted Authentication?**: If you ***don't*** have SAML enabled for your ThoughtSpot environment you need
     to use trusted authentication.  Flip this switch on to enable it.
   * **Trusted Authentication Secret Key**: Enter the secret key your ThoughtSpot admin received when enabling trusted authentication.
6. Hit "Save" at the top of the page.
