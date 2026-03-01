# Source: https://docs.curator.interworks.com/curator_api/api_docs/authentication.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Authentication

> API authentication methods and user verification processes for external applications integrating with Curator.

## Introduction

Occasionally, various external applications need to rely on Curator to authenticate users for them.
Curator provides a simple interface to determine which user is currently authenticated to Curator,
and provide information to your external application about that user.

This is particularly helpful for applications that need to keep user authentication in sync with Curator,
such as custom applications embedded within Curator.

Retrieving information about the currently authenticated user requires two API calls to Curator:

1. First, your application must forward the user to Curator's /fetchUser endpoint,
   with a `redirect_url` parameter. Curator returns the user to the redirect\_url with a `payload`
   GET parameter containing a JSON wad containing an identifier token.
2. Next, use the `token` value from this JSON wad to call Curator's `/user/getUser` endpoint to retrieve the user's information.

## Important Setup

In order for the redirect to work, you must whitelist your domain in the Curator Portal Settings.
Navigate to the **Settings** > **Curator** > **Portal Settings** section from the left-hand menu.
Under the **General** tab, expand the **Security** section.

## /fetchUser

`HTTP REDIRECT [your_domain]/fetchUser?redirect_url=[group_name_here]`

## /user/getUser

Returns the currently logged in user's information.
`POST [your_domain]/api/v1/User/getUser?apikey=[your_api_key_here]&token=[token_here]`

**Returns:**
array

## Example Authentication Script

```PHP  theme={null}
<?php
/**
 * This is a basic example of how to authenticate a user with Curator.
 *
 * From a flow perspective, this is what happens:
 *     1. The user is redirected to the Curator authentication system. (/fetchUser)
 *     2. The authenticated user is redirected back to this page with a JSON wad in the "payload" GET variable.
 *     3. The JSON wad contains a "token".
 *     4. The token is used against the Curator REST API to get the user's details.
 *
 * NOTE: VERY IMPORTANT:
 *     In order for the redirect to work, you must whitelist your domain in the Curator Portal Settings.
 *     Go to Settings->Curator->Portal Settings to add your domain. (Look under "security")
 *
 **/

/**
 * API Key: You can get this from the Curator backend.
 * Go to Settings->Curator->API Keys to retrieve and/or create a key.
 */
$api_key = 'YOUR_API_KEY';

/**
 * Curator Domain. This is the domain of your Curator instance.
 * For example: https://curator.example.com
 */
$curator_domain = 'YOUR_CURATOR_DOMAIN';

/**
 * This part is just a very basic session example.
 * You will likely want to customize it.
 */
session_start();

/**
 * If the user is returning from the Curator system, process their token.
 **/
if (!empty($_GET['payload'])) {
    processSessionPayload($_GET['payload'], $api_key, $curator_domain);

/**
 * Otherwise, if we need to start a NEW session, redirect to Curator.
 **/
} elseif (!isset($_SESSION['username'])) {
    // Where to return the user after the redirect.
    $returnURL = 'https://' . $_SERVER['HTTP_HOST'];

    // Redirect the unauthenticated user to the authentication system.
    header('Location: ' . $curator_domain . '/fetchUser?redirect_url=' . $returnURL);
    exit;
}

/**
 * If the user is authenticated, show them their information.
 **/
echo 'Hello, ' . $_SESSION['display_name'] . '!</br><pre>';
print_r($_SESSION);
echo '</pre>';

/**
 * Exchange the redirect session payload for user information.
 *
 * @param string $payload The JSON wad from the redirect.
 * @param string $api_key The API key for the Curator instance.
 * @param string $curator_domain The domain of the Curator instance.
 *
 * @return void
 */
function processSessionPayload($payload, $api_key, $curator_domain)
{
    $payload = json_decode($payload);
    if (isset($payload->token)) {
        // This is a 1-time use token returned from the /fetchUser endpoint.
        $token = $payload->token;

        // This is the REST API endpoint to exchange the token for user information.
        $url = $curator_domain . '/api/v1/user/getUser?apikey=' . $api_key . '&token=' . $token;

        $ch = curl_init($url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        $response = curl_exec($ch);
        curl_close($ch);

        $response = json_decode($response);
        $user = $response->user;

        /**
         * Uncomment the code below to see the user information available.
         *
         * echo "<pre>";
         * print_r($user);
         * echo "</pre>";
        */

        // Store the user information in the session.
        $_SESSION['username']     = $user->name;
        $_SESSION['email']        = $user->email;
        $_SESSION['display_name'] = $user->full_name;

        // The "SAML Attributes" are stored in the "custom_attributes" field.
        if (!empty($user->custom_attributes)) {
            $_SESSION['custom_attributes'] = $user->custom_attributes;
        }
    }
}
```
