# Source: https://help.cloudsmith.io/docs/upload-via-postman.md

# Upload via Postman

## Upload a raw package via the Cloudsmith APIs using Postman

##

In the following examples:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Identifier
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        OWNER
      </td>

      <td>
        Your Cloudsmith account name or organisation name (namespace)
      </td>
    </tr>

    <tr>
      <td>
        REPOSITORY
      </td>

      <td>
        Your Cloudsmith Repository name (also called "slug")
      </td>
    </tr>

    <tr>
      <td>
        USERNAME
      </td>

      <td>
        Your Cloudsmith username
      </td>
    </tr>

    <tr>
      <td>
        PASSWORD
      </td>

      <td>
        Your Cloudsmith password
      </td>
    </tr>

    <tr>
      <td>
        API-KEY
      </td>

      <td>
        Your Cloudsmith API Key
      </td>
    </tr>

    <tr>
      <td>
        PACKAGE\_NAME
      </td>

      <td>
        The name of your package
      </td>
    </tr>

    <tr>
      <td>
        PACKAGE\_VERSION
      </td>

      <td>
        The version number of your package
      </td>
    </tr>

    <tr>
      <td />

      <td />
    </tr>
  </tbody>
</Table>

Uploading a raw package to Cloudsmith via the URL is a 2 step process:

1. A PUT req against the upload URL: [https://upload.cloudsmith.io/OWNER/REPOSITORY/PACKAGE\_NAME](https://upload.cloudsmith.io/OWNER/REPOSITORY/PACKAGE_NAME).\
   The response to this PUT req gives you an identifier that you will need for the next stage.
2. A POST req to [https://help.cloudsmith.io/reference/packages\_upload\_raw](https://help.cloudsmith.io/reference/packages_upload_raw)

Postman is an application used for API testing. You can install Postman [here](https://www.postman.com/)

Lets see how you can upload a raw package using Postman:

## PUT req against the upload URL

##

1. Populate the PUT request URL [https://upload.cloudsmith.io/CLOUDSMITH\_ORG/CLOUDSMITH\_REPO/PACKAGE\_NAME](https://upload.cloudsmith.io/CLOUDSMITH_ORG/CLOUDSMITH_REPO/PACKAGE_NAME)
2. Switch to the ‘Authorization’ tab and populate your credentials with either Basic Auth or your API Key
3. Switch to the ‘Body’ tab and upload the file as a binary.
4. Press send and receive the response.
5. Read the identifier from the response to use in the next stage

![1555](https://files.readme.io/2728021-Screenshot_2022-03-28_at_18.05.32.png "Screenshot 2022-03-28 at 18.05.32.png")

## POST Raw package

##

1. Populate the request with the POST url: [https://api-prd.cloudsmith.io/v1/packages/CLOUDSMITH\_ORG/CLOUDSMITH\_REPO/upload/raw/](https://api-prd.cloudsmith.io/v1/packages/CLOUDSMITH_ORG/CLOUDSMITH_REPO/upload/raw/)
2. Select the ‘Body’ tab and populate it with your JSON (NOTE: the package\_file value should be populated with the identifier from the PUT response above):\
   \{"package\_file": "IDENTIFIER", "name": "test-package", "description": "Everything about packaging files.", "summary": "My Package File", "version": "1.0"}\
   package\_file value has to be the same as the response from the PUT req above- it is populated in the identifier value.
3. Switch to the ‘Authorization’ tab and populate your credentials with either Basic Auth or your API Key
4. Press send to upload the raw package.

![1531](https://files.readme.io/fc5e591-Screenshot_2022-03-28_at_18.07.04.png "Screenshot 2022-03-28 at 18.07.04.png")