# Source: https://docs.datafold.com/integrations/databases/adls.md

# Azure Data Lake Storage (ADLS)

<Note>
  This integration supports both Azure Data Lake Storage and Azure Blob Storage.
</Note>

**Steps to complete:**

1. [Create an app and service principal in Microsoft Entra](#create-an-app-and-service-principal-in-microsoft-entra)
2. [Configure your data connection in Datafold](#configure-your-data-connection-in-datafold)
3. [Create your first file diff](#create-your-first-file-diff)

## Create an app and service principal in Microsoft Entra

Create an app and service principal in Entra using a client secret (not certificate). Check out [Microsoft's documentation](https://learn.microsoft.com/en-us/entra/architecture/service-accounts-principal) on this topic if you need help.

<img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=e710f7b59ebdd0cbe835516cb7419841" alt="Use client secret" data-og-width="1612" width="1612" data-og-height="1008" height="1008" data-path="images/adls-client-secret.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=5f1a774c196aa3ca0a0d94684e2a4f25 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=2cc28f7dad1af49b7c530f5ab0fc9b61 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=12f01e13d8ff8ccb9fa7ac1fb19f2bd1 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=0fd552548c9e3d81ed987c483d28c5c3 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4829d2e4473dffcf074a506b12769400 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-client-secret.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=241ff1a2ff4b3bfc61f4201ca9359f8d 2500w" />

## Configure your data connection in Datafold

<img src="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=3e431654ca4c81a250d38eb240d5cbaa" alt="ADLS Data Connection" data-og-width="2084" width="2084" data-og-height="856" height="856" data-path="images/adls-connection.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=280&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=66bad0a74f27f22f3c6e2762b752838d 280w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=560&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=ec7b672ace0875d685304d00a5322e74 560w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=840&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=29f1f2c17174c58b3f7691fbcfa9c1dd 840w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=1100&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=c1f8754079db110a411fbbc0cd5bd56b 1100w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=1650&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=4f243432651b296c800952cd86e96e03 1650w, https://mintcdn.com/datafold/7pWtpSckJi2T0xZR/images/adls-connection.png?w=2500&fit=max&auto=format&n=7pWtpSckJi2T0xZR&q=85&s=f94b7a55513d23bf3d0fd96c10cbf6b2 2500w" />

| Field Name      | Description                                                                                              |
| --------------- | -------------------------------------------------------------------------------------------------------- |
| Connection name | The name you'd like to give to this connection in Datafold                                               |
| Account Name    | This is in the URL of any filepath in ADLS, e.g. `<account>.dfs.core.windows.net/<container>/<filepath>` |
| Client ID       | The client ID of the app you created in Microsoft Entra                                                  |
| Client Secret   | The client secret of the app you created in Microsoft Entra                                              |
| Tenant ID       | The tenant ID of the app you created in Microsoft Entra                                                  |

## Create your first file diff

For general guidance on how file diffs work in Datafold, check out our [file diffing docs](/data-diff/file-diffing).

When creating a diff, note that the file path you provide may differ depending on whether you're using ADLS or Blob Storage. For example:

* ADLS: `abfss://<my_filesystem>/<path>/<my_file>.<csv, xlsx, parquet, etc.>`
* Blob Storage: `az://<my_container>/<path>/<my_file>.<csv, xlsx, parquet, etc.>`
