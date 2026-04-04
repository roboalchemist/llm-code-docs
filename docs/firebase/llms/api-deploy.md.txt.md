# Source: https://firebase.google.com/docs/hosting/api-deploy.md.txt

<br />

The [Firebase Hosting REST API](https://firebase.google.com/docs/reference/hosting/rest) enables
programmatic and customizable deployments to your Firebase-hosted sites.
Use this REST API to deploy new or updated Hosting content and
configuration.

As an alternative to using the [Firebase CLI](https://firebase.google.com/docs/hosting/quickstart) for
deployments, you can use the Firebase Hosting REST API to programmatically
create a new [`version`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions) of
assets for your site, upload files to the version, then deploy the version to
your site.

For example, with the Firebase Hosting REST API, you can:

- **Schedule deploys.** By using the REST API in conjunction with a cron job,
  you can change Firebase-hosted content on a regular schedule (for example, to
  deploy a special holiday or event-related version of your content).

- **Integrate with developer tools.** You can create an option in your tool to
  deploy your web app projects to Firebase Hosting using just one click (for
  example, clicking a deploy button within an IDE).

- **Automate deploys when static content is generated.** When a process
  generates static content programmatically (for example, user-generated content
  such as a wiki or a news article), you can deploy the generated content as
  static files rather than serving them dynamically. This saves you expensive
  compute power and serves your files in a more scalable way.

This guide first describes how to enable, authenticate, and authorize the API.
Then this guide walks through an example to create a Firebase Hosting
version, to upload required files to the version, then finally to deploy the
version.

You can also learn more about this REST API in the
[full Hosting REST API reference documentation](https://firebase.google.com/docs/reference/hosting/rest).

## Before you begin: Enable the REST API

You must enable the Firebase Hosting REST API in the Google APIs console:

1. Open the
   [Firebase Hosting API page](https://console.cloud.google.com/apis/library/firebasehosting.googleapis.com?project=_)
   in the Google APIs console.

2. When prompted, select your Firebase project.

   > [!NOTE]
   > **Note:** Every Firebase project has a corresponding project in the Google APIs console.

3. Click **Enable** on the Firebase Hosting API page.

## Step 1: Get an access token to authenticate and authorize API requests

Firebase projects support Google
[service accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk),
which you can use to call Firebase
server APIs from your app server or trusted environment. If you're developing
code locally or deploying your application on-premises,
you can use credentials obtained
via this service account to authorize server requests.

To authenticate a service account and authorize it
to access Firebase services, you must generate a private key file in JSON
format.

**To generate a private key file for your service account:**

1. In the Firebase console, open
   **Settings \> [Service Accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk)**.

2. Click **Generate New Private Key** , then confirm by clicking **Generate Key**.

3. Securely store the JSON file containing the key.

Use your Firebase credentials together with
the [Google Auth Library](https://github.com/googleapis?q=auth)
for your preferred language to retrieve a short-lived OAuth 2.0 access token:

### node.js

```javascript
const {google} = require('googleapis');
function getAccessToken() {
  return new Promise(function(resolve, reject) {
    var key = require('./service-account.json');
    var jwtClient = new google.auth.JWT(
      key.client_email,
      null,
      key.private_key,
      SCOPES,
      null
    );
    jwtClient.authorize(function(err, tokens) {
      if (err) {
        reject(err);
        return;
      }
      resolve(tokens.access_token);
    });
  });
}
```

In this example, the Google API client library authenticates the request with
a JSON web token, or JWT. For more information, see
[JSON web tokens](https://github.com/googleapis/google-auth-library-nodejs/blob/d8c70b9d858e1ef07cb8ef2b5d5d560ac2b2600a/README.md#json-web-tokens).

### Python

```python
def _get_access_token():
  """Retrieve a valid access token that can be used to authorize requests.

  :return: Access token.
  """
  credentials = ServiceAccountCredentials.from_json_keyfile_name(
      'service-account.json', SCOPES)
  access_token_info = credentials.get_access_token()
  return access_token_info.access_token
```

### Java

```java
private static String getAccessToken() throws IOException {
  GoogleCredential googleCredential = GoogleCredential
      .fromStream(new FileInputStream("service-account.json"))
      .createScoped(Arrays.asList(SCOPES));
  googleCredential.refreshToken();
  return googleCredential.getAccessToken();
}
```

After your access token expires, the token refresh method is called
automatically to retrieve an updated access token.

> [!NOTE]
> **Note:** While using a service account is appropriate for *automated* tasks in server environments, there are other ways to obtain authorization to use the Firebase Hosting REST API. For example, project members can use the API if they (1) are assigned the Admin or Editor role for a project and (2) provide access tokens with the appropriate scope. Review the [other scenarios](https://developers.google.com/identity/protocols/OAuth2#scenarios) for different OAuth flows that will allow you to obtain authorization to use the Firebase Hosting REST API.

## Step 2: Ensure that your project has a default Hosting site

Before your first deployment to Firebase Hosting, your Firebase project must
have a default
[Hosting `SITE`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites).

> [!NOTE]
> **Note:** You can deploy to a non-default Hosting site, but your project must have at minimum a *default* Hosting site before you can deploy to Firebase Hosting at all.

1. Check if your project already has a default Hosting site by calling the
   [`sites.list`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/list)
   endpoint.

   For example:

   ### cURL command

   ```
   curl -H "Content-Type: application/json" \
          -H "Authorization: Bearer ACCESS_TOKEN" \

   https://firebasehosting.googleapis.com/v1beta1/projects/PROJECT_ID/sites
   ```

   ### Raw HTTPS request

   ```
   Host: firebasehosting.googleapis.com

   POST /v1beta1/projects/PROJECT_ID/sites HTTP/1.1
   Authorization: Bearer ACCESS_TOKEN
   Content-Type: application/json
   ```
   - If one of the sites has `"type": "DEFAULT_SITE"`, then your project
     already has a default Hosting site. Skip the remainder of this step,
     and move onto the next step:
     [Create a new version for your site](https://firebase.google.com/docs/hosting/api-deploy#create-version).

   - If you get an empty array, then you don't have a default Hosting
     site. Complete the remainder of this step.

2. Decide on the `SITE_ID` for your default Hosting site. Keep the
   following in mind when deciding this `SITE_ID`:

   - This `SITE_ID` is used to create your default Firebase subdomains:  

     `SITE_ID.web.app` and
     `SITE_ID.firebaseapp.com`.

   - A `SITE_ID` has the following requirements:

     - Must be a valid hostname label, meaning it cannot contain `.`, `_`, etc.
     - Must be 30 characters or fewer
     - Must be globally unique within Firebase

   Note that we often recommend using your project ID as the `SITE_ID` for your
   default Hosting site. Learn how to find this ID in
   [Understand Firebase projects](https://firebase.google.com/docs/projects/learn-more#project-id).
3. Create your default Hosting site by calling the
   [`sites.create`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/projects.sites/create)
   endpoint using your desired `SITE_ID` as the
   `siteId` parameter.

   For example:

   ### cURL command

   ```
   curl -H "Content-Type: application/json" \
          -H "Authorization: Bearer ACCESS_TOKEN" \

   https://firebasehosting.googleapis.com/v1beta1/projects/PROJECT_ID/sites?siteId=SITE_ID
   ```

   ### Raw HTTPS request

   ```
   Host: firebasehosting.googleapis.com

   POST /v1beta1/projects/PROJECT_ID/sites?siteId=SITE_ID
   Authorization: Bearer ACCESS_TOKEN
   Content-Type: application/json
   ```

   This API call to `sites.create` returns the following JSON:

   ```
   {
     "name": "projects/PROJECT_ID/sites/SITE_ID",
     "defaultUrl": "https://SITE_ID.web.app",
     "type": "DEFAULT_SITE"
   }
   ```

   > [!NOTE]
   > If you decide to use your project ID as the `SITE_ID`, note the following:
   >
   > In rare cases, your project ID has already been used by another project
   > to create a Hosting site. In these cases, the call to
   > `sites.create` returns a 400 error message that says the
   > provided `SITE_ID` is
   > `reserved by another project`. To resolve this error, try
   > calling `sites.create` again either using the suggested
   > string in the error message or another string until the call succeeds.

## Step 3: Create a new version for your site

Your first API call is to create a new
[`Version`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions) for your site.
Later in this guide, you'll upload files to this version, then deploy it to your
site.

1. Determine the <var translate="no">SITE_ID</var> for the site to which you want to deploy.

   > [!NOTE]
   > **Note:** For your default Hosting site, the <var translate="no">SITE_ID</var> is your Firebase project ID (which is used to create your Firebase subdomains `SITE_ID.web.app` and `SITE_ID.firebaseapp.com`).  
   > If you've created [multiple sites](https://firebase.google.com/docs/hosting/multisites) in your Firebase project, make sure that you're using the <var translate="no">SITE_ID</var> of the site to which you'd like to deploy.

2. Call the
   [versions.create](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/create)
   endpoint using your <var translate="no">SITE_ID</var> in the call.

   *(Optional)* You can also pass a
   [Firebase Hosting configuration object](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions#servingconfig)
   in the call, including setting a header that caches all files for a specified
   length of time.

   For example:

   ### cURL command

   ```
   curl -H "Content-Type: application/json" \
          -H "Authorization: Bearer ACCESS_TOKEN" \
          -d '{
                "config": {
                  "headers": [{
                    "glob": "**",
                    "headers": {
                      "Cache-Control": "max-age=1800"
                    }
                  }]
                }
              }' \
   https://firebasehosting.googleapis.com/v1beta1/sites/SITE_ID/versions
   ```

   ### Raw HTTPS request

   ```
   Host: firebasehosting.googleapis.com

   POST /v1beta1/sites/SITE_ID/versions HTTP/1.1
   Authorization: Bearer ACCESS_TOKEN
   Content-Type: application/json
   Content-Length: 134

   {
     "config": {
       "headers": [{
         "glob": "**",
         "headers": {
           "Cache-Control": "max-age=1800"
         }
       }]
     }
   }
   ```

This API call to `versions.create` returns the following JSON:

```
{
  "name": "sites/SITE_ID/versions/VERSION_ID",
  "status": "CREATED",
  "config": {
    "headers": [{
      "glob": "**",
      "headers": {
        "Cache-Control": "max-age=1800"
      }
    }]
  }
}
```

This response contains a unique identifier for the new version, in the format:
`sites/SITE_ID/versions/VERSION_ID`. You'll
need this unique identifier throughout this guide to reference this specific
version.

## Step 4: Specify the list of files you want to deploy

Now that you have your new version identifier, you need to tell
Firebase Hosting which files you want to eventually deploy in this new
version.

Note that Hosting has a maximum size limit of 2 GB for
individual files.

This API requires that you identify files by a SHA256 hash. So, before you can
make the API call, you'll first need to calculate a hash for each static file by
Gzipping the files then taking the SHA256 hash of each newly compressed file.

> [!NOTE]
> **Important:** In this call, you need to list *all* files that you want to include in the new version, including both new files and any existing files from previous versions (both modified *and* unmodified).
>
> You can send a maximum of 1000 file hashes in each API request. So, to list
> all the files for the version, you can call this endpoint multiple times;
> the files in each call will be added to the version.

Continuing our example, let's say that you want to deploy three files in the new
version: `file1`, `file2`, and `file3`.

1. Gzip the files:

   ```
   gzip file1 && gzip file2 && gzip file3
   ```

   You now have three compressed files `file1.gz`, `file2.gz`, and `file3.gz`.
2. Get the SHA256 hash of each compressed file:

   ```
   cat file1.gz | openssl dgst -sha256

   66d61f86bb684d0e35f94461c1f9cf4f07a4bb3407bfbd80e518bd44368ff8f4
   ```

   ```
   cat file2.gz | openssl dgst -sha256

   490423ebae5dcd6c2df695aea79f1f80555c62e535a2808c8115a6714863d083
   ```

   ```
   cat file3.gz | openssl dgst -sha256

   59cae17473d7dd339fe714f4c6c514ab4470757a4fe616dfdb4d81400addf315
   ```

   You now have the three SHA256 hashes of the three compressed files.
3. Send these three hashes in an API request to the
   [`versions.populateFiles`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/populateFiles)
   endpoint. List each hash by the desired path for the uploaded file (in this
   example, `/file1`, `/file2`, and `/file3`).

   For example:

   ### cURL command

   ```
   $ curl -H "Content-Type: application/json" \
            -H "Authorization: Bearer ACCESS_TOKEN" \
            -d '{
                  "files": {
                    "/file1": "66d61f86bb684d0e35f94461c1f9cf4f07a4bb3407bfbd80e518bd44368ff8f4",
                    "/file2": "490423ebae5dcd6c2df695aea79f1f80555c62e535a2808c8115a6714863d083",
                    "/file3": "59cae17473d7dd339fe714f4c6c514ab4470757a4fe616dfdb4d81400addf315"
                  }
                }' \
   https://firebasehosting.googleapis.com/v1beta1/sites/SITE_ID/versions/VERSION_ID:populateFiles
   ```

   ### Raw HTTPS Request

   ```
   Host: firebasehosting.googleapis.com

   POST /v1beta1/sites/SITE_ID/versions/VERSION_ID:populateFiles HTTP/1.1
   Authorization: Bearer ACCESS_TOKEN
   Content-Type: application/json
   Content-Length: 181

   {
     "files": {
       "/file1": "66d61f86bb684d0e35f94461c1f9cf4f07a4bb3407bfbd80e518bd44368ff8f4",
       "/file2": "490423ebae5dcd6c2df695aea79f1f80555c62e535a2808c8115a6714863d083",
       "/file3": "59cae17473d7dd339fe714f4c6c514ab4470757a4fe616dfdb4d81400addf315"
     }
   }
   ```

This API call to `versions.populateFiles` returns the following JSON:

```
{
  "uploadRequiredHashes": [
    "490423ebae5dcd6c2df695aea79f1f80555c62e535a2808c8115a6714863d083",
    "59cae17473d7dd339fe714f4c6c514ab4470757a4fe616dfdb4d81400addf315"
  ],
  "uploadUrl": "https://upload-firebasehosting.googleapis.com/upload/sites/SITE_ID/versions/VERSION_ID/files"
}
```

This response includes:

- The **hash of each file** that needs to be uploaded. For instance, in this
  example `file1` had already been uploaded in a previous version, so its hash
  is not included in the `uploadRequiredHashes` list.

  > [!NOTE]
  > **Note:** Some files in your new version don't need to be uploaded, for example, if the file was already in a previous version and is unmodified for the new version.

- The `uploadUrl` which is specific to the new version.

In the next step to upload the two new files, you'll need the hashes and the
`uploadURL` from the `versions.populateFiles` response.

## Step 5: Upload required files

You need to individually upload each required file (those files which are listed
in `uploadRequiredHashes` from the `versions.populateFiles` response in the
previous step). For these file uploads, you'll need the file hashes and the
`uploadUrl` from the previous step.

1. Append a **forward slash** and the **hash of the file** to the `uploadUrl` to
   create a file-specific URL in the format:
   `https://upload-firebasehosting.googleapis.com/upload/sites/SITE_ID/versions/VERSION_ID/files/FILE_HASH`.

2. Upload all the required files one-by-one (in this example, only `file2.gz`
   and `file3.gz`) to the file-specific URL using a series of requests.

   For example, to upload the compressed `file2.gz`:

   ### cURL command

   ```
   curl -H "Authorization: Bearer ACCESS_TOKEN" \
          -H "Content-Type: application/octet-stream" \
          --data-binary @./file2.gz \
   https://upload-firebasehosting.googleapis.com/upload/sites/SITE_ID/versions/VERSION_ID/files/FILE_HASH
   ```

   ### Raw HTTPS Request

   ```
   Host: upload-firebasehosting.googleapis.com

   POST /upload/sites/SITE_ID/versions/VERSION_ID/files/FILE_HASH HTTP/1.1
   Authorization: Bearer ACCESS_TOKEN
   Content-Type: application/octet-stream
   Content-Length: 500

   content-of-file2.gz
   ```

Successful uploads return a `200 OK` HTTPS response.

## Step 6: Update the status of the version to FINALIZED

After you've uploaded all the files which are listed in the
`versions.populateFiles` response, you can update the status of your version to
`FINALIZED`.

Call the [`versions.patch`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.versions/patch)
endpoint with the `status` field in your API request set to `FINALIZED`.

For example:

### cURL command

```
curl -H "Content-Type: application/json" \
       -H "Authorization: Bearer ACCESS_TOKEN" \
       -X PATCH \
       -d '{"status": "FINALIZED"}' \
https://firebasehosting.googleapis.com/v1beta1/sites/SITE_ID/versions/VERSION_ID?update_mask=status
```

### Raw HTTPS Request

```
Host: firebasehosting.googleapis.com

PATCH /v1beta1/sites/SITE_ID/versions/VERSION_ID?update_mask=status HTTP/1.1
Authorization: Bearer ACCESS_TOKEN
Content-Type: application/json
Content-Length: 23

{"status": "FINALIZED"}
```

This API call to `versions.patch` returns the following JSON. Check that
`status` has been updated to `FINALIZED`.

```
{
  "name": "sites/SITE_ID/versions/VERSION_ID",
  "status": "FINALIZED",
  "config": {
    "headers": [{
      "glob": "**",
      "headers": {"Cache-Control": "max-age=1800"}
    }]
  },
  "createTime": "2018-12-02T13:41:56.905743Z",
  "createUser": {
    "email": "SERVICE_ACCOUNT_EMAIL@SITE_ID.iam.gserviceaccount.com"
  },
  "finalizeTime": "2018-12-02T14:56:13.047423Z",
  "finalizeUser": {
    "email": "USER_EMAIL@DOMAIN.tld"
  },
  "fileCount": "5",
  "versionBytes": "114951"
}
```

## Step 7: Release the version for deployment

Now that you have a finalized version, release it for deployment. For this step,
you need to create a
[`Release`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases) of your version
that contains the hosting configuration and all the content files for your new
version.

Call the [`releases.create`](https://firebase.google.com/docs/reference/hosting/rest/v1beta1/sites.releases/create)
endpoint to create your release.

For example:

### cURL command

```
curl -H "Authorization: Bearer ACCESS_TOKEN" \
       -X POST
https://firebasehosting.googleapis.com/v1beta1/sites/SITE_ID/releases?versionName=sites/SITE_ID/versions/VERSION_ID
```

### Raw HTTPS Request

```
Host: firebasehosting.googleapis.com

POST /v1beta1/sites/SITE_ID/releases?versionName=sites/SITE_ID/versions/VERSION_ID HTTP/1.1
Authorization: Bearer ACCESS_TOKEN
```

This API call to `releases.create` returns the following JSON:

```
{
  "name": "sites/SITE_ID/releases/RELEASE_ID",
  "version": {
    "name": "sites/SITE_ID/versions/VERSION_ID",
    "status": "FINALIZED",
    "config": {
    "headers": [{
      "glob": "**",
      "headers": {"Cache-Control": "max-age=1800"}
    }]
  }
  },
  "type": "DEPLOY",
  "releaseTime": "2018-12-02T15:14:37Z"
}
```

The hosting configuration and all the files for the new version should now be
deployed to your site, and you can access your files using the URLs:

- `https://SITE_ID.web.app/file1`
- `https://SITE_ID.web.app/file2`
- `https://SITE_ID.web.app/file3`

These files are also accessible on URLs associated with your
`SITE_ID.firebaseapp.com` domain.

You can also see your new release listed in the
[Hosting dashboard](https://console.firebase.google.com/project/_/hosting/sites)
of the Firebase console.