# Source: https://clickwrap-developer.ironcladapp.com/docs/getting-your-access-token.md

# Authentication (REST API)

Learn how to authenticate with the REST API by generating and using an access token.

In order to access the Ironclad Clickwrap REST API, you’ll need to add an access token as an HTTP authorization header to every API request. Below, you'll find how to create and use an access token for the Ironclad Clickwrap API.

> 🚧 Please Review the Important Notes Section
>
> Please review the "Important Notes" section before beginning to use your access token!

## Create an API Access Token

### Visit Your User Profile

Visit your User Profile by clicking on your initials in the bottom left of the page to open the navigation modal and then selecting “User Profile” at the top.

<Image title="c73533e7171d83edcb2b7fa401266a35bee0e9dec62ce36fa3c02cf5125f705b6e5cf93392262ccb4394d6265f1df94dd61dd49a458b3f71a90af0781e17dd2b75a01da070253f61d893da76fad0a95e9708c82ee76970a2ec037871dd2d961d7e45eedb.jpeg" alt={1600} align="center" src="https://files.readme.io/1298c1c-c73533e7171d83edcb2b7fa401266a35bee0e9dec62ce36fa3c02cf5125f705b6e5cf93392262ccb4394d6265f1df94dd61dd49a458b3f71a90af0781e17dd2b75a01da070253f61d893da76fad0a95e9708c82ee76970a2ec037871dd2d961d7e45eedb.jpeg">
  Visit the User Profile page by clicking on the "User Profile" link.
</Image>

### Create a New API Application

Next to the “API Keys” header, click on the plus sign to open the “Register an API Key” modal.

<Image title="ca070e3cc3996abd8f034115d4fd8d37977d05740f55d54646057ea7155fe51290eadab79b7b3eda5be3818185d7c30812c96e877ce1c397bfcdafd139e38bcc5f09882cc99e011a1defad2a00bcda4c832206ff4e80e030761169ad041cd66ef3d19d22.jpeg" alt={1600} align="center" src="https://files.readme.io/72be868-ca070e3cc3996abd8f034115d4fd8d37977d05740f55d54646057ea7155fe51290eadab79b7b3eda5be3818185d7c30812c96e877ce1c397bfcdafd139e38bcc5f09882cc99e011a1defad2a00bcda4c832206ff4e80e030761169ad041cd66ef3d19d22.jpeg">
  Click on the plus sign to open the modal.
</Image>

With the "Register API Key" modal open, give your API application a name and a description of what you plan to use the access token for. You can then click “Register” to move on to the next step.

<Image title="bd1b44493ef30284faf516f3067c57807cbfd2f029623cf7bc07eef11e0e86c43775cd9179cc2184d38ca53d18f2f39bc954fa74d43c1fe2bee00b0c617cbb83152c8abbe569b7845f25a3fd7194d97e5e0f51daf269266f96512b820274ace96a759f97.jpeg" alt={1600} align="center" src="https://files.readme.io/cc50d43-bd1b44493ef30284faf516f3067c57807cbfd2f029623cf7bc07eef11e0e86c43775cd9179cc2184d38ca53d18f2f39bc954fa74d43c1fe2bee00b0c617cbb83152c8abbe569b7845f25a3fd7194d97e5e0f51daf269266f96512b820274ace96a759f97.jpeg">
  "Register API Key" modal open.
</Image>

Once you have clicked "Register", a client secret and access token will be generated and displayed in a modal.

<Image alt="Generated keys modal open." src="https://files.readme.io/7c33fb2175968d97c27a30cfe3fa4270824b8d424b27f7793d722dde23204375-image.png">
  Generated keys modal open.
</Image>

Be sure to copy your client secret and access token. These values will not be displayed again and cannot be retrieved after this modal is closed.

Alternatively, you can also generate your access token programmatically via the REST API with [this endpoint](https://clickwrap-developer.ironcladapp.com/reference/createregenerate-access-token).

## Using Your Access Token

When making a request to the API, you’ll need to add the access token as an Authorization HTTP Header. It should look like the following:

```http HTTP Header
Authorization: Bearer YOUR_ACCESS_TOKEN
```

<Image title="a1164092d1a728a12e54be7edf2c6d78c741fd34c4d4c6dad5a907d5f936f6bfaa63d412870aefdb8fe701794ca5c13407fe4936ddf10af4749982e99a11758cfaf8914f51e2d8a31d2e31e3e142428c658b827af8ad00648ddef0bb4badafdcd04616c7.jpeg" alt={1600} align="center" src="https://files.readme.io/acb44a3-a1164092d1a728a12e54be7edf2c6d78c741fd34c4d4c6dad5a907d5f936f6bfaa63d412870aefdb8fe701794ca5c13407fe4936ddf10af4749982e99a11758cfaf8914f51e2d8a31d2e31e3e142428c658b827af8ad00648ddef0bb4badafdcd04616c7.jpeg">
  Example of the access token being used in Postman when manually added as an HTTP header.
</Image>

## Important Notes

### Access Token and User Permissions

The API access token is tied to the user who generated it. This means:

1. Access tokens must be created by a user with the appropriate site permissions. For example, the user associated with an access token must have “create” permissions to create resources via the API.
2. When a user is removed from the site, all existing API tokens will by default be transferred to the site's owner—if one exists. If no site owner exists, the removed user's API tokens will be decommissioned. Consider using a persistent service account to create API tokens.

## Best Practices

### API Requests Must Use HTTPS

API requests must only use HTTPS (SSL). Attempting to use without SSL will not succeed and should not be used.

### Secure Your Access Token

Please keep your API key secure! Do not use your API key within client-side code. Additionally, do not share them publicly or store them in any git repositories.

### Rotate Your Access Token

Since access tokens are generated using OAuth 2.0, you have the ability to rotate your keys at your own discretion via the API.