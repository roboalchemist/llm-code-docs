# Source: https://docs.xano.com/xanoscript/function-reference/cloud-services/azure-blob-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Azure Blob Storage

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> Azure Blob Storage: List Directory of

```javascript  theme={null}
cloud.azure.storage.list_directory {
  account_name = ""
  account_key = ""
  container_name = ""
  path = ""
} as x1
```

| Parameter       | Purpose                     | Example                     |
| --------------- | --------------------------- | --------------------------- |
| account\_name   | Azure storage account name  | `"mystorageaccount"`        |
| account\_key    | Azure storage account key   | `"XXXXXXXXXXXXXXXXXXXXX=="` |
| container\_name | Storage container name      | `"uploads"`, `"documents"`  |
| path            | Directory path to list      | `"folder/"`, `"images/"`    |
| as              | Alias for directory listing | `x1`, `directory_contents`  |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.azure.storage.list_directory {
    account_name = $env.AZURE_ACCOUNT_NAME
    account_key = $env.AZURE_ACCOUNT_KEY
    container_name = "user-uploads"
    path = "images/2024/"
  } as folder_listing
  ```

  * Lists contents of an Azure storage directory
  * Returns blob names and metadata
  * Supports nested directories
  * Lists all files in specified path
</Accordion>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> Azure Blob Storage: Get Signed URL of

```javascript  theme={null}
cloud.azure.storage.sign_url {
  account_name = ""
  account_key = ""
  container_name = ""
  path = ""
  ttl = 300
} as x2
```

| Parameter       | Purpose                    | Example                     |
| --------------- | -------------------------- | --------------------------- |
| account\_name   | Azure storage account name | `"mystorageaccount"`        |
| account\_key    | Azure storage account key  | `"XXXXXXXXXXXXXXXXXXXXX=="` |
| container\_name | Storage container name     | `"private"`                 |
| path            | Path to file               | `"documents/file.pdf"`      |
| ttl             | Time-to-live in seconds    | `300`, `3600`               |
| as              | Alias for signed URL       | `x2`, `access_url`          |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.azure.storage.sign_url {
    account_name = $env.AZURE_ACCOUNT_NAME
    account_key = $env.AZURE_ACCOUNT_KEY
    container_name = "secure-files"
    path = "private/"|add:$file.path
    ttl = 1800
  } as download_url
  ```

  * Generates SAS token URL for temporary access
  * URL expires after specified TTL
  * Useful for secure file sharing
  * Works with private containers
</Accordion>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> Azure Blob Storage: Upload file to

```javascript  theme={null}
cloud.azure.storage.upload_file {
  account_name = ""
  account_key = ""
  container_name = ""
  filePath = ""
  file = ""
  metadata =
}
```

| Parameter       | Purpose                       | Example                       |
| --------------- | ----------------------------- | ----------------------------- |
| account\_name   | Azure storage account name    | `"mystorageaccount"`          |
| account\_key    | Azure storage account key     | `"XXXXXXXXXXXXXXXXXXXXX=="`   |
| container\_name | Storage container name        | `"uploads"`                   |
| filePath        | Destination path in container | `"folder/file.jpg"`           |
| file            | File to upload                | `$input.file`                 |
| metadata        | Custom metadata for blob      | `{contentType: "image/jpeg"}` |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.azure.storage.upload_file {
    account_name = $env.AZURE_ACCOUNT_NAME
    account_key = $env.AZURE_ACCOUNT_KEY
    container_name = "user-files"
    filePath = $user.id|add:"/profile.jpg"
    file = $input.profile_photo
    metadata = {
      userId: $user.id,
      uploadDate: $now
    }
  }
  ```

  * Uploads file to Azure Blob Storage
  * Supports custom metadata
  * Creates directories automatically
  * Overwrites existing files
</Accordion>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> Azure Blob Storage: Delete file

```javascript  theme={null}
cloud.azure.storage.delete_file {
  account_name = ""
  account_key = ""
  container_name = ""
  filePath = ""
}
```

| Parameter       | Purpose                    | Example                     |
| --------------- | -------------------------- | --------------------------- |
| account\_name   | Azure storage account name | `"mystorageaccount"`        |
| account\_key    | Azure storage account key  | `"XXXXXXXXXXXXXXXXXXXXX=="` |
| container\_name | Storage container name     | `"uploads"`                 |
| filePath        | Path to file to delete     | `"folder/file.txt"`         |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.azure.storage.delete_file {
    account_name = $env.AZURE_ACCOUNT_NAME
    account_key = $env.AZURE_ACCOUNT_KEY
    container_name = "temp-files"
    filePath = "uploads/"|add:$file.name
  }
  ```

  * Deletes a blob from storage
  * Permanent deletion
  * No response needed
  * Use with caution
</Accordion>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> Azure Blob Storage: Create Var From File Resource

```javascript  theme={null}
cloud.azure.storage.read_file {
  account_name = ""
  account_key = ""
  container_name = ""
  filePath = ""
} as x3
```

| Parameter       | Purpose                    | Example                     |
| --------------- | -------------------------- | --------------------------- |
| account\_name   | Azure storage account name | `"mystorageaccount"`        |
| account\_key    | Azure storage account key  | `"XXXXXXXXXXXXXXXXXXXXX=="` |
| container\_name | Storage container name     | `"documents"`               |
| filePath        | Path to file to read       | `"folder/file.txt"`         |
| as              | Alias for file contents    | `x3`, `file_data`           |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.azure.storage.read_file {
    account_name = $env.AZURE_ACCOUNT_NAME
    account_key = $env.AZURE_ACCOUNT_KEY
    container_name = "data"
    filePath = "documents/"|add:$doc.id
  } as document_contents
  ```

  * Reads blob contents
  * Returns file data
  * Supports all file types
  * Useful for processing file contents
</Accordion>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> Azure Blob Storage: Get File Metadata

```javascript  theme={null}
cloud.azure.storage.get_file_info {
  account_name = ""
  account_key = ""
  container_name = ""
  filePath = ""
} as x4
```

| Parameter       | Purpose                    | Example                     |
| --------------- | -------------------------- | --------------------------- |
| account\_name   | Azure storage account name | `"mystorageaccount"`        |
| account\_key    | Azure storage account key  | `"XXXXXXXXXXXXXXXXXXXXX=="` |
| container\_name | Storage container name     | `"files"`                   |
| filePath        | Path to file               | `"folder/file.txt"`         |
| as              | Alias for file metadata    | `x4`, `blob_info`           |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.azure.storage.get_file_info {
    account_name = $env.AZURE_ACCOUNT_NAME
    account_key = $env.AZURE_ACCOUNT_KEY
    container_name = "archives"
    filePath = "backup/"|add:$file.name
  } as file_metadata
  ```

  * Retrieves blob metadata
  * Returns size, last modified, etc.
  * Does not download contents
  * Useful for file verification
</Accordion>


Built with [Mintlify](https://mintlify.com).