# Source: https://docs.envzero.com/guides/admin-guide/private-registry/providers.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Providers Overview

> Publish and manage private Terraform providers in the env zero provider registry

## env zero Provider Registry

The **env zero Provider Registry** is a private registry for [Terraform providers](https://developer.hashicorp.com/terraform/language/providers), allowing you to privately share and reuse Terraform providers within your organization.

You can access your organization’s provider registry through the `Registry` link in the left sidebar, and choosing the `Providers` tab:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/c338ad3-regisrty_ui_1_fix.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=d19c914489004d36a29b3bebea4cbdff" alt="Interface screenshot showing configuration options" width="3456" height="1674" data-path="images/guides/admin-guide/private-registry/c338ad3-regisrty_ui_1_fix.png" />
</Frame>

# Publishing A Provider

<Note>
  NOTE

  This guide assumes you already have a provider set up, preferably with `goreleaser`.
</Note>

## Creating A Provider

As an env zero admin (or with a custom role with the `Create & Edit Providers` permission), you should have permission to create a provider.

Navigate to `Registry` on the navigation bar, and click the `Providers` tab. There you will see the `Create New Provider` button:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/97f42dd-regisrty_providers_1_fix.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=53c8e29ef2c5eed825a665aa74bf8df6" alt="Interface screenshot showing configuration options" width="3456" height="1676" data-path="images/guides/admin-guide/private-registry/97f42dd-regisrty_providers_1_fix.png" />
</Frame>

<Info>
  **Provider's type**

  Your provider’s type is essentially its name, and should match your provider’s files. For example, if your binaries look like `terraform-provider-aws_1.1.1_linux_amd64.zip`, then your provider’s type should be `aws`.
</Info>

<Note>
  Note

  Your binaries' names should match this format - `<type>_<semver>_<anything>_<you>_<want>.zip`, like the example above `terraform-provider-aws_1.1.1_linux_amd64.zip`
</Note>

## Creating A GPG Key

Terraform uses GPG keys in order to authenticate the identity of the entity that complied and signed the binaries of the provider.\
Normally, when creating a release, you should provide goreleaser with your GPG\_FINGERPRINT, which should also be set on env zero. For more information regarding how to generate your GPG Key, check out [GitHub's guide](https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key).

Once you have your key generated, you'll need to create it on env zero. Navigate to `Organization Settings > Keys` and scroll down to `GPG Keys`. You will see the `Add GPG Key` button:

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/a4e07ac-gcp_fix.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=8e831dd31f23bab1624ae0b6712dea49" alt="Interface screenshot showing configuration options" width="2866" height="1392" data-path="images/guides/admin-guide/private-registry/a4e07ac-gcp_fix.png" />
</Frame>

<Info>
  **GPG Key ID**

  GPG Key ID is referring to the GPG\_FINGERPRINT, the same one you provided `goreleaser` with.  its a 16 charecters hexadecimal string, that is calculated by summerizing your key content, and it should be unique per key.
</Info>

## Releasing A Version

As part of your CI you should have a version releaser setup.

Terraform recommends using `goreleaser`, and so do we. You can make sure your `.goreleaser` file is configured correctly following [this guide by Terraform](https://developer.hashicorp.com/terraform/tutorials/providers-plugin-framework/providers-plugin-framework-release-publish#add-goreleaser-configuration)

Assuming you have a version complied and ready to ship, you will need to upload the binaries you wish to support.

### Creating A Version

The first step on the release is creating a version in env zero, following the [Version API Reference](/api-reference/provider-registry/create-a-new-provider-version).

### Uploading A Version

If creating a version was done correctly, you will receive a URL (valid for 1 hour) to which you can upload your `zip`, `SHA256SUMS` and `SHA256SUMS.sig` files. Note that for each file type you will need a specific `content-type` header:

* `zip` - `application/zip`
* `SHA256SUMS` - `application/octet-stream`
* `SHA256SUMS.sig` - `application/pgp-signature`

and then with a simple `cURL` request:

```bash  theme={null}
curl --request PUT \
    --header "Content-Type: $CONTENT_TYPE" \
    --upload-file "$FILEPATH" \
    "$UPLOAD_URL"
```

To ease the process we suggest using the following script to **create and upload all the binaries at once**:

```bash  theme={null}
#!/bin/bash

# usage: upload-provider-versions.sh <dist_folder_path>

# required environment variables:
# 1. ENV0_API_KEY - env zero's api key. you can create one at
# 2. ENV0_API_SECRET - env zero's api secretd
# 3. PROVIDER_ID - your provider's ID as created by env zero
# 4. GPG_KEY_ID - your GPG key's fingerprint (16 hexadecimal charecters)


# The folder containing the files to upload
FOLDER=$1

# Assert FOLDER argument is passed
if [[ -z "$FOLDER" ]]; then
  echo "Usage: upload-provider-versions.sh <dist_folder_path>"
  exit 1
fi

AUTH_HEADER="Authorization: Basic $(echo -n "$ENV0_API_KEY:$ENV0_API_SECRET" | base64)"

ENV0_API_ENDPOINT=${ENV0_API_ENDPOINT:-"https://api.env0.com"}

function upload_file {
  FILEPATH="$1"
    # Get the filename without the path
  FILENAME=$(basename "$FILEPATH")

  # Determine the content type based on the file extension
  if [[ $FILENAME == *.zip ]]; then
    CONTENT_TYPE="application/zip"
  elif [[ $FILENAME == *_SHA256SUMS ]]; then
    CONTENT_TYPE="application/octet-stream"
  elif [[ $FILENAME == *_SHA256SUMS.sig ]]; then
    CONTENT_TYPE="application/pgp-signature"
  else
    continue
  fi


  # Make the POST request to create a new version
  RESPONSE=$(curl --fail --silent --show-error --request POST \
    --header "Content-Type: application/json" \
    --header "$AUTH_HEADER" \
    --data "{\"filename\":\"$FILENAME\",\"gpgKeyId\":\"$GPG_KEY_ID\"}" \
    "$ENV0_API_ENDPOINT/providers/$PROVIDER_ID/versions")
  # Check for errors
  if [ $? -ne 0 ]; then
    echo "Error creating new version for $FILENAME"
    continue
  fi

  # Parse the response for the upload URL
  UPLOAD_URL=$(echo "$RESPONSE" | sed -n 's/.*"url":[[:space:]]*"\([^"]*\)".*/\1/p')

  # Make the PUT request to upload the file
  curl --fail --silent --show-error --request PUT \
    --header "Content-Type: $CONTENT_TYPE" \
    --upload-file "$FILEPATH" \
    "$UPLOAD_URL"

  # Check for errors
  if [ $? -ne 0 ]; then
    echo "Error uploading $FILENAME"
    continue
  fi

  echo "Uploaded $FILENAME"
}

# Find all files in the folder and run the upload_file function for each one in the background
for FILEPATH in "$FOLDER"/*; do
  upload_file "$FILEPATH" &
done

# Wait for all background processes to finish
wait
```

**That's it!** Your first version should be released.\
To watch your provider's versions, navigate to its page on env zero by clicking its card.

<img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/d7432ce-provider_card.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=53cda229830c2ed78dac544f3fab817e" alt="" width="2662" height="314" data-path="images/guides/admin-guide/private-registry/d7432ce-provider_card.png" />

On the top right, you can see your uploaded versions. Clicking on versions then navigating to `Platforms` tab will show you the supported binaries.

<Frame>
  <img src="https://mintcdn.com/envzero-b61043c8/pvGFjFxaiqGDTFG3/images/guides/admin-guide/private-registry/8548265-platforms_1_fix.png?fit=max&auto=format&n=pvGFjFxaiqGDTFG3&q=85&s=76eecaa2cccb23113ee63bb506df8721" alt="Interface screenshot showing configuration options" width="1920" height="834" data-path="images/guides/admin-guide/private-registry/8548265-platforms_1_fix.png" />
</Frame>

## Using A Provider

Now that your provider is set up every user in your organization with the `View Providers` permission (available by default to organization user) can start using it from within env zero, or outside of it.

Set up the provider in your Terraform file by copying and pasting the following block.

```hcl  theme={null}
terraform {
   required_providers {
     <provider-type> = {
       source = "api.env0.com/<organization-id>/<provider-type>"
       version = "<version>"
     }
   }
}
```

You are all set! You can deploy your Terraform code through env zero and it will deploy as expected.

### Outside env zero

If you would like to use your provider outside env zero, you will have to set up Terraform's authorization. Follow the guide on [how to authorize when using a private registry](/guides/admin-guide/private-registry/#authorization) for more info.

Built with [Mintlify](https://mintlify.com).
