# Source: https://firebase.google.com/docs/auth/configure-oauth-rest-api.md.txt

You can use the[Google Cloud Identity Platform REST API](https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects.defaultSupportedIdpConfigs)to programmatically manage a Firebase project's OAuth identity provider (IdP) configuration. With this API, you can configure the identity providers you want to support, and update, enable, and disable your project's current OAuth configurations.

## Get authorization

Before you can call the REST API, you need an OAuth 2.0 access token that grants Editor access to your Firebase project. For example, to get an access token using a service account in Node.js:  

    const googleAuth = require('google-auth-library');
    const SCOPES = ['https://www.googleapis.com/auth/cloud-platform'];

    async function getAccessToken() {
        const serviceAccount = require('/path/to/service_account_key.json');
        const jwtClient = new googleAuth.JWT(
            serviceAccount.client_email,
            null,
            serviceAccount.private_key,
            SCOPES,
            null
        );
        return jwtClient.authorize().then((tokens) => tokens.access_token);
    }

## Add a new OAuth identity provider configuration

To add a new OAuth identity provider (IdP) configuration, POST the new configuration to the[`projects.defaultSupportedIdpConfigs`](https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects.defaultSupportedIdpConfigs/create)endpoint.

You will need to specify the ID of the identity provider and your client ID and client secret, which you typically get from the provider's developer site. Here are the identity providers that Firebase supports and their IDs:

|     Provider      |         IdP ID         |
|-------------------|------------------------|
| Apple             | `apple.com`            |
| Apple Game Center | `gc.apple.com`         |
| Facebook          | `facebook.com`         |
| GitHub            | `github.com`           |
| Google            | `google.com`           |
| Google Play Games | `playgames.google.com` |
| LinkedIn          | `linkedin.com`         |
| Microsoft         | `microsoft.com`        |
| Twitter           | `twitter.com`          |
| Yahoo             | `yahoo.com`            |

For example, using Node.js:  

    const fetch = require('node-fetch');
    const GCIP_API_BASE = 'https://identitytoolkit.googleapis.com/v2';

    async function addIdpConfig(projectId, accessToken, idpId, clientId, clientSecret) {
        const uri = `${GCIP_API_BASE}/projects/${projectId}/defaultSupportedIdpConfigs?idpId=${idpId}`;
        const options = {
            method: 'POST',
            headers: {
                'Authorization': `Bearer ${accessToken}`
            },
            body: JSON.stringify({
                name: `projects/${projectId}/defaultSupportedIdpConfigs/${idpId}`,
                enabled: true,
                clientId: clientId,
                clientSecret: clientSecret,
            }),
        };
        return fetch(uri, options).then((response) => {
            if (response.ok) {
                return response.json();
            } else if (response.status == 409) {
                throw new Error('IdP configuration already exists. Update it instead.');
            } else {
                throw new Error('Server error.');
            }
        });
    }

    (async () => {
        const projectId = 'your-firebase-project-id';
        const accessToken = await getAccessToken();
        const idpId = 'facebook.com';
        const clientId = 'your-facebook-client-id';
        const clientSecret = 'your-facebook-client-secret';
        try {
            await addIdpConfig(projectId, accessToken, idpId, clientId, clientSecret);
        } catch (err) {
            console.error(err.message);
        }
    })().catch(console.error);

If the call succeeds, it returns the newly-created configuration. For example:  

    {
      name: 'projects/your-numerical-project-id/defaultSupportedIdpConfigs/facebook.com',
      enabled: true,
      clientId: 'your-facebook-client-id',
      clientSecret: 'your-facebook-client-secret'
    }

If you try to configure an identity provider that has already been configured for your project, the call returns HTTP error 409. In this situation, you can update the configuration instead, as described below.

## Update an OAuth identity provider configuration

To enable or disable an OAuth identity provider, or update your project's client configuration, first get the provider's current configuration by making a GET request to the the[`projects.defaultSupportedIdpConfigs`](https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects.defaultSupportedIdpConfigs/get)endpoint. Then, make the changes you want to the configuration and PATCH the new configuration to the[`projects.defaultSupportedIdpConfigs`](https://cloud.google.com/identity-platform/docs/reference/rest/v2/projects.defaultSupportedIdpConfigs/patch)endpoint.

For example, using Node.js:  

    async function getIdpCfg(projectId, accessToken, idpId) {
        const uri = `${GCIP_API_BASE}/projects/${projectId}/defaultSupportedIdpConfigs/${idpId}`;
        const options = {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${accessToken}`
            },
        };
        return fetch(uri, options).then((response) => {
            if (response.ok) {
                return response.json();
            } else if (response.status == 404) {
                throw new Error('IdP configuration not found. First add the IdP'
                                + ' configuration to your project.');
            } else {
                throw new Error('Server error.');
            }
        });
    }

    async function updateIdpConfig(accessToken, idpCfg) {
        const uri = `${GCIP_API_BASE}/${idpCfg.name}`;
        const options = {
            method: 'PATCH',
            headers: {
                'Authorization': `Bearer ${accessToken}`
            },
            body: JSON.stringify(idpCfg),
        };
        return fetch(uri, options).then((response) => {
            if (response.ok) {
                return response.json();
            } else if (response.status == 404) {
                throw new Error('IdP configuration not found. First add the IdP'
                                + ' configuration to your project.');
            } else {
                throw new Error('Server error.');
            }
        });
    }

    (async () => {
        const projectId = 'your-firebase-project-id';
        const accessToken = await getAccessToken();
        const idpId = 'facebook.com';
        try {
            // Get the IdP's current configuration.
            const idpCfg = await getIdpCfg(projectId, accessToken, idpId);

            // Update the configuration. (For example, disable the IdP.)
            idpCfg.enabled = false;
            await updateIdpConfig(accessToken, idpCfg);
        } catch (err) {
            console.error(err.message);
        }
    })().catch(console.error);

If you try to update the configuration of an identity provider you've never configured for your project, the calls will return HTTP error 404. Instead, configure a new identity provider as shown in the[previous section](https://firebase.google.com/docs/auth/configure-oauth-rest-api#add-idpcfg).