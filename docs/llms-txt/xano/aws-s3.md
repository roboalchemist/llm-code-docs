# Source: https://docs.xano.com/xanoscript/function-reference/cloud-services/aws-s3.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AWS S3

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> AWS S3: List Directory of

```javascript  theme={null}
cloud.aws.s3.list_directory {
  bucket = ""
  region = ""
  key = ""
  secret = ""
  prefix = ""
  next_page_token = ""
} as x1
```

| Parameter         | Purpose                         | Example                              |
| ----------------- | ------------------------------- | ------------------------------------ |
| bucket            | S3 bucket name                  | `"my-bucket"`                        |
| region            | AWS region                      | `"us-east-1"`                        |
| key               | AWS access key ID               | `"AKIAXXXXXXXXXXXXXXXX"`             |
| secret            | AWS secret access key           | `"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"` |
| prefix            | Directory prefix to list        | `"folder/"`, `"uploads/"`            |
| next\_page\_token | Token for pagination            | `"eyJ2IjoiMiIsInMiOjB9"`             |
| as                | Alias for the directory listing | `x1`, `directory_contents`           |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.aws.s3.list_directory {
    bucket = "my-app-uploads"
    region = "us-west-2"
    key = $env.AWS_KEY_ID
    secret = $env.AWS_SECRET_KEY
    prefix = "users/images/"
  } as folder_contents
  ```

  * Lists contents of an S3 directory
  * Supports pagination for large directories
  * Returns file metadata and continuation token
  * Can filter by prefix path
</Accordion>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> AWS S3: Get Signed URL of

```javascript  theme={null}
cloud.aws.s3.sign_url {
  bucket = ""
  region = ""
  key = ""
  secret = ""
  file_key = ""
  ttl = 300
} as x2
```

| Parameter | Purpose                  | Example                              |
| --------- | ------------------------ | ------------------------------------ |
| bucket    | S3 bucket name           | `"my-bucket"`                        |
| region    | AWS region               | `"us-east-1"`                        |
| key       | AWS access key ID        | `"AKIAXXXXXXXXXXXXXXXX"`             |
| secret    | AWS secret access key    | `"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"` |
| file\_key | Path to file in bucket   | `"folder/file.pdf"`                  |
| ttl       | Time-to-live in seconds  | `300`, `3600`, `86400`               |
| as        | Alias for the signed URL | `x2`, `download_url`                 |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.aws.s3.sign_url {
    bucket = "my-app-files"
    region = "us-west-2"
    key = $env.AWS_KEY_ID
    secret = $env.AWS_SECRET_KEY
    file_key = "private/document.pdf"
    ttl = 3600
  } as temporary_url
  ```

  * Generates a pre-signed URL for temporary access
  * URL expires after specified TTL
  * Useful for secure file sharing
  * Supports private bucket access
</Accordion>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> AWS S3: Upload File to

```javascript  theme={null}
cloud.aws.s3.upload_file {
  bucket = ""
  region = ""
  key = ""
  secret = ""
  file_key = ""
  file = ""
  metadata =
  object_lock_mode = ""
  object_lock_retain_until = ""
} as x3
```

| Parameter                   | Purpose                    | Example                              |
| --------------------------- | -------------------------- | ------------------------------------ |
| bucket                      | S3 bucket name             | `"my-bucket"`                        |
| region                      | AWS region                 | `"us-east-1"`                        |
| key                         | AWS access key ID          | `"AKIAXXXXXXXXXXXXXXXX"`             |
| secret                      | AWS secret access key      | `"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"` |
| file\_key                   | Destination path in bucket | `"uploads/file.jpg"`                 |
| file                        | File to upload             | `$input.file`, `$file_data`          |
| metadata                    | Custom metadata for file   | `{contentType: "image/jpeg"}`        |
| object\_lock\_mode          | S3 Object Lock mode        | `"GOVERNANCE"`, `"COMPLIANCE"`       |
| object\_lock\_retain\_until | Lock retention date        | `"2024-12-31"`                       |
| as                          | Alias for upload result    | `x3`, `upload_result`                |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.aws.s3.upload_file {
    bucket = "my-app-uploads"
    region = "us-west-2"
    key = $env.AWS_KEY_ID
    secret = $env.AWS_SECRET_KEY
    file_key = "users/"|add:$user.id|add:"/profile.jpg"
    file = $input.profile_photo
    metadata = {
      contentType: "image/jpeg",
      userId: $user.id
    }
  } as upload_response
  ```

  * Uploads file to S3 bucket
  * Supports custom metadata
  * Optional Object Lock configuration
  * Returns upload confirmation
</Accordion>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> AWS S3: Delete File

```javascript  theme={null}
cloud.aws.s3.delete_file {
  bucket = ""
  region = ""
  key = ""
  secret = ""
  file_key = ""
}
```

| Parameter | Purpose                | Example                              |
| --------- | ---------------------- | ------------------------------------ |
| bucket    | S3 bucket name         | `"my-bucket"`                        |
| region    | AWS region             | `"us-east-1"`                        |
| key       | AWS access key ID      | `"AKIAXXXXXXXXXXXXXXXX"`             |
| secret    | AWS secret access key  | `"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"` |
| file\_key | Path to file to delete | `"folder/file.txt"`                  |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.aws.s3.delete_file {
    bucket = "my-app-uploads"
    region = "us-west-2"
    key = $env.AWS_KEY_ID
    secret = $env.AWS_SECRET_KEY
    file_key = "temp/"|add:$file.path
  }
  ```

  * Deletes a file from S3 bucket
  * Permanent deletion (not recoverable)
  * No response alias needed
  * Use with caution
</Accordion>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> AWS S3: Create Var From File Resource

```javascript  theme={null}
cloud.aws.s3.read_file {
  bucket = ""
  region = ""
  key = ""
  secret = ""
  file_key = ""
} as x4
```

| Parameter | Purpose                 | Example                              |
| --------- | ----------------------- | ------------------------------------ |
| bucket    | S3 bucket name          | `"my-bucket"`                        |
| region    | AWS region              | `"us-east-1"`                        |
| key       | AWS access key ID       | `"AKIAXXXXXXXXXXXXXXXX"`             |
| secret    | AWS secret access key   | `"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"` |
| file\_key | Path to file to read    | `"folder/file.txt"`                  |
| as        | Alias for file contents | `x4`, `file_data`                    |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.aws.s3.read_file {
    bucket = "my-app-data"
    region = "us-west-2"
    key = $env.AWS_KEY_ID
    secret = $env.AWS_SECRET_KEY
    file_key = "documents/"|add:$doc.id|add:".pdf"
  } as document_contents
  ```

  * Reads file contents from S3
  * Returns file data
  * Useful for processing file contents
  * Supports all file types
</Accordion>

## <Icon icon="https://mintcdn.com/xano-997cb9ee/l34pjCw6QluB5NGI/images/icons/xs_temp.svg?fit=max&auto=format&n=l34pjCw6QluB5NGI&q=85&s=a93a487e986548b85069518b76869a5f" size={46} width="371" height="137" data-path="images/icons/xs_temp.svg" /> AWS S3: Get File Metadata

```javascript  theme={null}
cloud.aws.s3.get_file_info {
  bucket = ""
  region = ""
  key = ""
  secret = ""
  file_key = ""
} as x5
```

| Parameter | Purpose                 | Example                              |
| --------- | ----------------------- | ------------------------------------ |
| bucket    | S3 bucket name          | `"my-bucket"`                        |
| region    | AWS region              | `"us-east-1"`                        |
| key       | AWS access key ID       | `"AKIAXXXXXXXXXXXXXXXX"`             |
| secret    | AWS secret access key   | `"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"` |
| file\_key | Path to file            | `"folder/file.txt"`                  |
| as        | Alias for file metadata | `x5`, `file_info`                    |

<Accordion title="Example">
  ```javascript  theme={null}
  cloud.aws.s3.get_file_info {
    bucket = "my-app-storage"
    region = "us-west-2"
    key = $env.AWS_KEY_ID
    secret = $env.AWS_SECRET_KEY
    file_key = "uploads/"|add:$file.path
  } as file_metadata
  ```

  * Retrieves file metadata from S3
  * Returns size, last modified, etc.
  * Does not download file contents
  * Useful for file verification
</Accordion>


Built with [Mintlify](https://mintlify.com).