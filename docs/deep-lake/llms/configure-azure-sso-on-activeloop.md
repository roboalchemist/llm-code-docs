# Source: https://docs-v3.activeloop.ai/setup/storage-and-creds/managed-credentials/microsoft-azure/configure-azure-sso-on-activeloop.md

# Configure Azure SSO on Activeloop

### Configure Azure SSO on Activeloop

### 1. Creating Application

* **Go to App registration page in** [**🌐Azure portal**](https://portal.azure.com/#view/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)
* **Click on add New Registration**

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2F27dGrs7Z5kgIGhNU9Csb%2Fimage.png?alt=media&#x26;token=361ef49f-1ce7-453f-afff-0b1276df675f" alt=""><figcaption></figcaption></figure>

1. Put name for the application
2. For application type, select `Default Directory only - Single tenant`
3. For Redirect URI select the type `Web`
4. For Callback URL put `https://auth.activeloop.ai/login/callback`
5. Click on `Register`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FV8fIW2kawFgNIJ3dhS1j%2Fimage.png?alt=media&#x26;token=7113ceb0-7c1e-46f6-91b5-c0a1ac1d22dd" alt=""><figcaption></figcaption></figure>

#### Once it is created go to `Overview` page, copy and send us the `Application (client) ID` and the `Directory (tenant) ID`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FTZwGsAeMYMwCrejOvInL%2Fimage.png?alt=media&#x26;token=5232c389-5cd7-4e36-80a6-d38599680cbd" alt=""><figcaption></figcaption></figure>

#### Client secret creation

Go to `Certificates & Secrets` → `Client secrets` →`New client secret`

Name the secret, select preferred expiration and click `Add`

`NOTE: The secret need to be updated before it get expired`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FunO6OgJTvEPHloYJ14IW%2Fimage.png?alt=media&#x26;token=35997572-f307-4a30-8872-20d0a69890fd" alt=""><figcaption></figcaption></figure>

#### Send us the secret value

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FVOMuK1UzLwR3eXPw55UZ%2Fimage.png?alt=media&#x26;token=03be1998-30df-4ee4-8e1d-6955c336b306" alt=""><figcaption></figcaption></figure>

### 2. Granting Permissions

1. **Go to `API permissions` → `Microsoft Graph` → `Delegated Permissions` and select following permissions:**
   1. `email`
   2. `openid`
   3. `profile`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FtMvO1PUkmTGIs6K695yj%2Fimage.png?alt=media&#x26;token=9fa58e95-ddbd-43d3-9392-9d59e4ab694c" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FsSuqMxw7JzmPXcuYxdh1%2Fimage.png?alt=media&#x26;token=5954a0d1-b47c-43b0-8edb-1f52ee6baeca" alt=""><figcaption></figcaption></figure>

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FgyyycW0hQazFzf0tUUd3%2Fimage.png?alt=media&#x26;token=c81eefc8-2120-4445-823f-ac3072239380" alt=""><figcaption></figcaption></figure>

2. **In the search bar search `Directory.Read.All` and select the permission as well**

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2F5lGg04O7OJ2W26XCHq3e%2Fimage.png?alt=media&#x26;token=0c136c69-7873-415d-bf8d-cb170a0505fc" alt=""><figcaption></figcaption></figure>

#### Click on `Add permissions`

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2Fr6Xa66c0laZyJjItAoCP%2Fimage.png?alt=media&#x26;token=68839a7f-7444-4a70-b9b1-f04e8b9afc03" alt=""><figcaption></figcaption></figure>

### 3. Domain Name Validation in our side

We also will be needing domain of the azure tenant to authorize the SSO clients

1. Go to [🌐Domain Names](https://portal.azure.com/#view/Microsoft_AAD_IAM/DomainsList.ReactView) in Azure portal
2. Copy the domain name that will be used for SSO and send us

<figure><img src="https://3470044769-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FWOs95B2h3lcO4dwXDRJ3%2Fuploads%2FKedHnaMe4FkUUcWtNITt%2Fimage.png?alt=media&#x26;token=35e066e8-73d9-4fb3-a8d1-42995902bdf9" alt=""><figcaption></figcaption></figure>
