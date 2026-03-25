# Source: https://docs.edgeimpulse.com/studio/organizations/data/cloud-data-storage.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cloud data storage

Edge Impulse makes it easy to access data that you have stored in the cloud by offering integrations with several storage providers and the flexibility to connect a storage solution to an [organization](/studio/organizations/dashboard) or directly to a project.

## Connecting to storage

There are two locations within Edge Impulse where you can connect to cloud storage, from within an organization or within a project. These options are described below. For details related to the specific storage provider integration options available, please see the [Storage provider integrations](/studio/organizations/data/cloud-data-storage#storage-provider-integrations) section of this document.

### Organization data bucket

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

Cloud storage can be connected to an organization. By connecting your data to an organization, you are offered the flexibility to pre-process your datasets through the use of [transformation blocks](/studio/organizations/custom-blocks/custom-transformation-blocks) and to feed your datasets into multiple projects.

To connect, access your organization, select **Data** in the left sidebar menu, select the **Buckets** tab at the top of the page, then click the `+ Add new bucket` button. Follow the instructions in the modal window that pops up.

<Frame caption="Connecting a cloud storage provider to an organization">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-storage-connect-organization.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=1763fd277edcabddeb5496e23a264390" width="1538" height="1000" data-path=".assets/images/data-storage-connect-organization.png" />
</Frame>

### Project data source

Cloud storage can be connected directly to a project. To connect, access your project, select **Data acquisition** in the left sidebar menu, select the **Data sources** tab at the top of the page, then click the `+ Add new data source`. Follow the instructions in the modal window that pops up.

Note that some options in the modal will be greyed out if your project is not on the Enterprise plan.

<Tabs>
  <Tab title="Step 1">
    <Frame caption="Connecting a cloud storage provider to a project - step 1">
      <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-storage-connect-project-1.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=a35edd23f6271fc7386617116658d1e1" width="1538" height="1000" data-path=".assets/images/data-storage-connect-project-1.png" />
    </Frame>
  </Tab>

  <Tab title="Step 2">
    <Frame caption="Connecting a cloud storage provider to a project - step 2">
      <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-storage-connect-project-2.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=147208e47026d5b129738539880685b6" width="1538" height="1000" data-path=".assets/images/data-storage-connect-project-2.png" />
    </Frame>
  </Tab>
</Tabs>

## Storage provider integrations

Edge Impulse allows you to integrate with several cloud storage options. These include:

* [Amazon S3 buckets](/studio/organizations/data/cloud-data-storage#amazon-s3-bucket)
* [Google Cloud Storage buckets](/studio/organizations/data/cloud-data-storage#google-cloud-storage-bucket)
* [Microsoft Azure Blob Storage blob containers](/studio/organizations/data/cloud-data-storage#microsoft-azure-blob-storage-blob-container)
* [Other (S3-compatible) buckets](/studio/organizations/data/cloud-data-storage#other-s3-compatible-buckets)

### Amazon S3 bucket

To connect to an Amazon S3 bucket, you will need to provide:

* The bucket name
* The bucket region
* An access key
* A secret key
* A path prefix (optional)

If the credentials provided do not have access to the root of the bucket, the prefix is used to specify the path for which the credentials are valid.

<Warning>
  Currently only long-term credentials from AWS IAM users are supported; temporary credentials provided to AWS SSO users are not supported.
</Warning>

<Frame caption="Connecting an Amazon S3 bucket">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-storage-connect-amazon.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=2324a439bf824b2bd34ef16870426f79" width="1538" height="1000" data-path=".assets/images/data-storage-connect-amazon.png" />
</Frame>

#### CORS policy

For Amazon S3 buckets, you will also need to enable CORS headers for the bucket. You can do this in the S3 console by going to your bucket, going to the permissions tab, and then adding the policy defined below to the cross-origin resource sharing section.

CORS policy (console):

```json  theme={"system"}
[
    {
        "AllowedOrigins": ["https://studio.edgeimpulse.com"],
        "AllowedMethods": ["PUT", "POST"],
        "AllowedHeaders": ["*"],
        "ExposeHeaders": []
    }
]
```

Alternatively, you can save the below CORS policy as a `cors.json` file (note there are some differences in the structure compared to the JSON above) and add it to your bucket using the AWS S3 CLI.

CORS policy (CLI):

```json  theme={"system"}
{
      "CORSRules": [
        {
            "AllowedOrigins": ["https://studio.edgeimpulse.com"],
            "AllowedMethods": ["PUT", "POST"],
            "AllowedHeaders": ["*"],
            "ExposeHeaders": []
        }
    ]
}
```

```bash  theme={"system"}
aws s3api put-bucket-cors --bucket <your-bucket-name> --cors-configuration file://cors.json
```

### Google Cloud Storage bucket

To connect to a Google Cloud Storage bucket, you will need to provide:

* The bucket name
* The bucket region
* An access key
* A secret key
* A path prefix (optional)

If the credentials provided do not have access to the root of the bucket, the prefix is used to specify the path for which the credentials are valid.

<Frame caption="Connecting a Google Cloud Storage bucket">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-storage-connect-google.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=5820ec5325072bcf0f8a2858acea04d0" width="1538" height="1000" data-path=".assets/images/data-storage-connect-google.png" />
</Frame>

#### CORS policy

For Google Cloud Storage buckets, you will also need to enable CORS headers for the bucket. You cannot manage CORS policies using the Google Cloud console; you must use the gcloud CLI instead.

CORS policy:

```json  theme={"system"}
[
    {
        "origin": ["https://studio.edgeimpulse.com"],
        "method": ["PUT", "POST"],
        "responseHeader": ["*"],
        "maxAgeSeconds": 31536000
    }
]
```

Save the above CORS policy as a `cors.json` file and add it to your bucket with the gcloud CLI using the following command:

```bash  theme={"system"}
gcloud storage buckets update gs://<your-bucket-name> --cors-file=cors.json
```

<Warning>
  gsutil is not the recommended CLI tool for Cloud Storage. You may have used this tool before, however, Google now recommends using gcloud storage commands in the Google Cloud CLI instead.
</Warning>

### Microsoft Azure Blob Storage blob container

To connect to a Microsoft Azure Blob Storage blob container, you will need to provide:

* The blob container name
* The storage account name
* A secret key
* A path prefix (optional)

If the credentials provided do not have access to the root of the blob container, the prefix is used to specify the path for which the credentials are valid.

<Frame caption="Connecting a Microsoft Azure Blob Storage blob container">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-storage-connect-microsoft.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=6687600327cb07e349f65f41481b90e9" width="1538" height="1000" data-path=".assets/images/data-storage-connect-microsoft.png" />
</Frame>

#### CORS policy

A CORS policy is not required with Microsoft Azure Blob Storage.

### Other (S3-compatible) buckets

To connect to another (S3-compatible) type of bucket, you will need to provide:

* The bucket name
* The bucket region
* The bucket endpoint
* An access key
* A secret key
* A path prefix (optional)

If the credentials provided do not have access to the root of the bucket, the prefix is used to specify the path for which the credentials are valid.

<Frame caption="Connecting an other (S3-compatible) storage bucket">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-storage-connect-other.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=4649d46e7568096d12c4c8f7ad4e13e0" width="1538" height="1000" data-path=".assets/images/data-storage-connect-other.png" />
</Frame>

#### CORS policy

For other (S3-compatible) buckets, you will also need to enable CORS headers for the bucket. Please refer to your provider documentation for instructions on how to do so.

The items that you will need to set are the following:

* Origin: `["https://studio.edgeimpulse.com"]`
* Method: `["PUT", "POST"]`
* Header: `["*"]`

## Permissions required

For cloud storage integration to work as expected, Edge Impulse needs to be provided with credentials that allow read, write, and delete operations. Please refer to your storage provider documentation for specifics.

## Verifying the connection

In order to verify the connection to the cloud storage provider, Edge Impulse will write an `.ei-portal-check` file that will be subsequently deleted. Once a bucket is successfully connected to your organization, a green dot will appear in the connected column on the buckets overview page.

<Frame caption="Cloud data storage providers successfully connected to an organization">
  <img src="https://mintcdn.com/edgeimpulse/VpF_Einsy6qHCvhZ/.assets/images/data-storage-connected-buckets.png?fit=max&auto=format&n=VpF_Einsy6qHCvhZ&q=85&s=7c0c03effb38d97a8fa7d93ed21e9cfa" width="1538" height="1000" data-path=".assets/images/data-storage-connected-buckets.png" />
</Frame>

## Troubleshooting

<Info>
  No common issues have been identified thus far. If you encounter an issue, please reach out on the [forum](https://forum.edgeimpulse.com) or, if you are on the Enterprise plan, through your support channels.
</Info>

## Additional resources

* [Organization data](/studio/organizations/data)
* [Data sources](/studio/projects/data-acquisition/data-sources)
* [What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)
* [Product overview of Google Cloud Storage](https://cloud.google.com/storage/docs/introduction)
* [Introduction to Azure Blob Storage](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction)


Built with [Mintlify](https://mintlify.com).