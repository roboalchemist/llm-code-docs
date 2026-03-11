# Source: https://docs.axonius.com/docs/dropbox.md

# Dropbox

Dropbox is a file hosting service that offers cloud storage, file synchronization, personal cloud, and client software.

## Types of Assets Fetched

This adapter fetches the following types of assets:

* Devices
* Users

The Dropbox adapter connection requires the following parameters:

1. **Account Name** - Enter your Dropbox account name.

2. **App Key** and **App Secret** *(required)* - API credentials associated with a user account that has the [Required Permissions](#required-permissions) to fetch assets.

3. **Refresh Token** *(required)* - An API Refresh Token associated with a user account that has permissions to fetch assets.
   To generate a Refresh Token, see [Generate a Refresh Token](/docs/dropbox#generate-a-refresh-token).

4. **Verify SSL** - Select whether to verify the SSL certificate of the server against the CA database inside of Axonius.  For more details, see [SSL Trust & CA Settings](../certificate-settings#ssl-trust-ca-settings).

5. **HTTPS Proxy** *(optional)* - Connect the adapter to a proxy instead of directly connecting it to the domain.

6. **HTTPS Proxy User Name** *(optional)* - The user name to use when connecting to the value supplied in **Host Name or IP Address** via the value supplied in **HTTPS Proxy**.

7. **HTTPS Proxy Password** *(optional)* - The password to use when connecting to the server using the **HTTPS Proxy**.

8. To learn more about common adapter connection parameters and buttons, see [Adding a New Adapter Connection](/docs/adapters-screen#adding-a-new-adapter-connection).

<Image alt="dropbox.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/dropbox.png" />

## Required Permissions

The value supplied in [App Key](#parameters) must be associated with credentials that have the permission `session.list` enabled.

In additions the application, should be granted the following scopes:

* members.read - For fetching users.
* sessions.list - For fetching devices.

## APIs

Axonius uses the [Dropbox API](https://developers.dropbox.com/oauth-guide).

## Obtain the App Key and App Secret

1. Follow the [Dropbox instructions](https://www.dropbox.com/developers/apps) for creating an application in Dropbox.
2. In Dropbox, navigate to **Settings `>` Apps**.
3. Open the settings for your newly created application.
4. On the bottom of the page, copy the **App Key** and **App Secret**, and paste them into their corresponding fields in Axonius's Dropbox Adapter connection form.
   You will also need your App Key and App Secret for generating the refresh token.

## Generate a Refresh Token

1. Log in to Dropbox.
2. Go to [https://www.dropbox.com/oauth2/authorize?client\_id=APP\_KEY\&response\_type=code\&token\_access\_type=offline](https://www.dropbox.com/oauth2/authorize?client_id=APP_KEY\&response_type=code\&token_access_type=offline), substituting your **APP\_KEY** in the URL.
3. Confirm connecting your account to the Dropbox app. A single-use code is then displayed.
4. Run the following curl command to obtain the Refresh Token:

```
curl https://api.dropbox.com/oauth2/token -d code=ACCESS_CODE_GENERATED -d grant_type=authorization_code  -u APP_KEY:APP_SECRET
```

The input should appear in the following format:
![DropBox\_RefreshToken](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DropBox_RefreshToken.png)

The output of the command should appear similar to the following:

![Screen Shot 2022-11-27 at 13.10.59.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/Screen%20Shot%202022-11-27%20at%2013.10.59.png)

5. From the output, copy the **Refresh Token** value and paste it into the Axonius adapter's **Refresh Token** parameter.