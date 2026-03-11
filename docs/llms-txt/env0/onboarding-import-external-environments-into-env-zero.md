# Source: https://docs.envzero.com/guides/admin-guide/environment-discovery/onboarding-import-external-environments-into-env-zero.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Importing External Environments into env zero

> Import and bulk-migrate existing external infrastructure environments into env zero using environment discovery

If you're advanced in your IaC journey and have decided to adopt env zero, you likely have existing environments that you want to import and manage within the platform.

The [Environment Discovery](/guides/admin-guide/environment-discovery) feature simplifies this process by scanning your external environments and offering the ability to import them directly into env zero.

Bulk imports allow you to select and configure multiple environments simultaneously, reducing manual work and lowering the chances of human error. This process helps minimize the time required to migrate your environments into env zero.

## Discover

Activate the Environment Discovery feature within your project and configure it to detect your existing environments.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/f5d8a3b9ede0790fb4d42d8fcae363621dd73a151bbb688aa4d44067b0e42f5d-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=2d2cc1c53987aad098b34983f6338545" alt="" width="2714" height="1462" data-path="images/guides/admin-guide/environment-discovery/f5d8a3b9ede0790fb4d42d8fcae363621dd73a151bbb688aa4d44067b0e42f5d-image.png" />

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/eda24ef3bc7eb0e0c0ed686e38c081f7e0b17eeb1ec9fc01dccc2ecc10ab3549-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=a7eccca4007c8fb3fecd18a2f044fb13" alt="" width="872" height="470" data-path="images/guides/admin-guide/environment-discovery/eda24ef3bc7eb0e0c0ed686e38c081f7e0b17eeb1ec9fc01dccc2ecc10ab3549-image.png" />

Once configured, env zero will display all detected environments in the Discovered Environments table. Each discovered environment will include the following details:

* **Path:** The environment’s location within your Git repository.
* **Target Project:** The project where the environment will be placed (as defined by your Environment Placement configuration).
* **Target Environment:** The generated name for the new environment, based on your Environment Placement configuration.

<img src="https://mintcdn.com/envzero-b61043c8/pcx_nh6zT3at7dYL/images/guides/admin-guide/environment-discovery/36c75ee4f60eda1031d0c0ff5480a40314221f5130cbf3ee5f60fc46b899f6e1-image.png?fit=max&auto=format&n=pcx_nh6zT3at7dYL&q=85&s=2a1d59f673cbe2aa0ccdf8cad9cfe27a" alt="" width="2720" height="1438" data-path="images/guides/admin-guide/environment-discovery/36c75ee4f60eda1031d0c0ff5480a40314221f5130cbf3ee5f60fc46b899f6e1-image.png" />

## Initiate Import Batch

Once env zero has discovered your environments, you can initiate the import by selecting the desired environments and clicking the 'Import' button.

<img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/09/8e22b7c8b6ed8441e2a1ee4ee318f28c5e7b69e44591d5dd5fa356e126024a6e-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=1d2e65a01deecaeeca909d7b4b45aa08" alt="" width="1424" height="654" data-path="images/changelogs/2024/09/8e22b7c8b6ed8441e2a1ee4ee318f28c5e7b69e44591d5dd5fa356e126024a6e-image.png" />

Next, you'll need to configure each environment, including shared settings that can be defined at the Project level. The following configurations must be provided:

* **Workspace Name (required)** Enter the workspace name for each selected environment to ensure that env zero references the same environment and state, rather than creating a new one.
* **Variables:** Define the necessary Terraform or environment variables. These can be set at either the Environment or Project level.
* **Deployment Credentials (recommended but not required):** Specify the credentials env zero will use to deploy your environment and connect to your cloud account successfully.

<img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/09/c221ac4b7a774b89e34a4d9da8be6e708eecade991bae927ef598fa299a5c74b-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=97b96306d4c5aea4ea5582ca369c9b93" alt="" width="2748" height="1672" data-path="images/changelogs/2024/09/c221ac4b7a774b89e34a4d9da8be6e708eecade991bae927ef598fa299a5c74b-image.png" />

<Info>
  **Pre-filled Terraform Variables**

  During the environment discovery process, env zero scanned your Git repository and reviewed the Terraform environments and variables in use.

  env zero will automatically pre-fill your Terraform variable keys with those defined in the environment. If a `default` value was specified for a variable, env zero will pre-fill the corresponding value as well.
</Info>

Once you’ve completed the configuration, click the ‘Import’ button in the bottom-right corner to initiate the batch import process.

<img src="https://mintcdn.com/envzero-b61043c8/hr9e779VSnIZk8JC/images/changelogs/2024/09/54b3981c13b40eb3872cb3be1ed0a3240308c6a3ea86dc92ccf3ff5ab82edc8d-image.png?fit=max&auto=format&n=hr9e779VSnIZk8JC&q=85&s=706b9d0d14b642b1e6cae6b1fa4daf8e" alt="" width="1490" height="825" data-path="images/changelogs/2024/09/54b3981c13b40eb3872cb3be1ed0a3240308c6a3ea86dc92ccf3ff5ab82edc8d-image.png" />

<Info>
  **What is considered a Successful Import?**

  An import is considered successful and its status will update to "Imported" when the following conditions are met:

* The deployment completes successfully, with no errors during the process
* The Terraform plan shows **0 changes**, meaning env zero deployed the environment in the same workspace without attempting to create new resources. It successfully uses the existing resources

  If these conditions are not met, the status will change to "Error."
</Info>

## Rerun Imports

Mistakes can happen - whether it's a missed variable, incorrect credentials, or other human errors. These issues can cause an import to fail. To address this, env zero provides a Rerun option.

You can select the environments that encountered errors, adjust their configurations as needed, and run the import process again.

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/fcb54a513a8baddbfb4b38a12a083df22ec062f16822d3eba7c772594bbc584a-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=ae273aa38cb39658510bb828a02ad309" alt="" width="1424" height="596" data-path="images/guides/admin-guide/environment-discovery/fcb54a513a8baddbfb4b38a12a083df22ec062f16822d3eba7c772594bbc584a-image.png" />

<img src="https://mintcdn.com/envzero-b61043c8/T2JW_alZSK9mPIUs/images/guides/admin-guide/environment-discovery/fcb54a513a8baddbfb4b38a12a083df22ec062f16822d3eba7c772594bbc584a-image.png?fit=max&auto=format&n=T2JW_alZSK9mPIUs&q=85&s=ae273aa38cb39658510bb828a02ad309" alt="" width="1424" height="596" data-path="images/guides/admin-guide/environment-discovery/fcb54a513a8baddbfb4b38a12a083df22ec062f16822d3eba7c772594bbc584a-image.png" />

Built with [Mintlify](https://mintlify.com).
