# Source: https://docs.envzero.com/guides/cloud-compass/cloud-compass/configure-cloud-accounts.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Configure an AWS Cloud Account

> Connect your AWS account to env zero Cloud Compass with IAM roles and S3 CloudTrail logs

## Configure a Cloud Account

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/b05512167de1147ec7998cdab31f0f59eedc824976e1093d090e988396f314c6-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=54409d0630b309e681739d1b91e62419" alt="" width="2130" height="1202" data-path="images/guides/cloud-compass/cloud-compass/b05512167de1147ec7998cdab31f0f59eedc824976e1093d090e988396f314c6-image.png" />

<Warning>
  Additional Costs for Using Cloud Compass with AWS

  There could be additional costs for enabling Cloud Compass with AWS that only comes from outbound S3 traffic. This refers to data transferred from S3 buckets to external destinations, which will be charged according to AWS's standard S3 outbound data transfer rates.
</Warning>

### Requirements

#### Ensure Active Cloud Trail

* Open the AWS Console and login to the relevant account
* Go to CloudTrail and in the left hand side menu select `Trails`
* Make sure the trail is in a Logging status

  <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/beb3073-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=1be5719afd8e4ce0d293260920ccaa3d" alt="" width="1629" height="318" data-path="images/guides/cloud-compass/cloud-compass/beb3073-image.png" />

#### Grant Bucket Permissions

* Go to S3 Console and choose the relevant bucket based on the name of the S3 bucket in the Trails. You can also click on the bucket name from the previous image.
* Choose permission tab

  <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/be27527-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=14b6f88188d414e0f1bbf6d07621799c" alt="" width="1582" height="220" data-path="images/guides/cloud-compass/cloud-compass/be27527-image.png" />
* Go To Bucket Policy and click `Edit`
* <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/c60858f-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=e9ac311ab85042dfbc5c618c5afa8205" alt="" width="1600" height="291" data-path="images/guides/cloud-compass/cloud-compass/c60858f-image.png" />

  Add the following policy to the list:

  ```json Policy theme={null}
  {
    "Sid": "AllowEnvZeroToReadCloudTrailEvents",
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::913128560467:role/env0-cloud-scanner"
    },
    "Action": [
      "s3:GetBucketLocation",
      "s3:GetObject",
      "s3:ListBucket"
    ],
    "Resource": [
      "arn:aws:s3:::<REPLACE-BY-BUCKET-NAME>",
      "arn:aws:s3:::<REPLACE-BY-BUCKET-NAME>/*"
    ]
  }
  ```

* Replace the placeholder `<replace-by-bucket-name>`with the bucket name.
* Click on the `Save Changes` button
* Click on the edit button in the Object Ownership section

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/1c934f5-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=494e1a31f80d97ab323c933df038b052" alt="" width="1533" height="214" data-path="images/guides/cloud-compass/cloud-compass/1c934f5-image.png" />

* Select the `ACLs disabled (recommended)` option and click on the `Save Changes` button

<Warning>
  Object Ownership Mode

  We only able to read the cloud trails events when the Object Ownership in mode "ACLs disabled"

    <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/ae3a3b5-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=1111f3c300e735b8060320393b40f3d1" alt="" width="856" height="459" data-path="images/guides/cloud-compass/cloud-compass/ae3a3b5-image.png" />
</Warning>

#### Grant Decrypt Permission

* This requirement is only necessary if encryption is enabled on the trail.
* You can check if it is enabled by opening the trail and check if `Log file SSE-KMS encryption` is Enabled.

  <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/da6f35b-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=91f3a9f630852a4f555ee45d1a7bc0b2" alt="" width="1129" height="610" data-path="images/guides/cloud-compass/cloud-compass/da6f35b-image.png" />
* If it is enabled, you should grant permission to the env zero role to decrypt the logs.
* Open the "KMS Key Policy" - by clicking on the key URL from the previous image.

  <img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/0a7a073-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=79324b1966d33db4e12ae9314ed3f40b" alt="" width="1619" height="259" data-path="images/guides/cloud-compass/cloud-compass/0a7a073-image.png" />
* Click Edit, and add this policy to the list:

  ```json Policy theme={null}
  {
    "Sid": "AllowEnv0ToDecryptTrailLogs",
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::913128560467:role/env0-cloud-scanner"
    },
    "Action": "kms:Decrypt",
    "Resource": "*"
  }
  ```

* Click `Save Changes`

#### Setting Up Bucket Configuration

Here you should specify account config including:

* Account name (for identification only)
* Bucket Name \[1]
* Account ID \[1]
* Prefix \[1] `(optional)` - this should match the prefix (if specified) when configuring the s3 bucket.  See [AWS docs](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-trail.html#:~:text=To%20make%20it%20easier%20to%20find%20your%20logs%2C%20create%20a%20new%20folder%20\(also%20known%20as%20a%20prefix\)%20in%20an%20existing%20bucket%20to%20store%20your%20CloudTrail%20logs).
* Regions

\[1] These fields are used to build the `Scanned Bucket URL` which will be used to fetch your cloud events.

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/89a0617-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=2774c9e43e65b7c3f938fc9003c6780e" alt="" width="2272" height="1267" data-path="images/guides/cloud-compass/cloud-compass/89a0617-image.png" />

Once you have created your account, env zero will start fetching historical data for the past 90 days.

The Insights tab will show that a data fetching run has started. This process might take a few minutes, depending on the amount of events we need to ingest.

<img src="https://mintcdn.com/envzero-b61043c8/DEMw5onAg75H1sCr/images/guides/cloud-compass/cloud-compass/1f52d0c-image.png?fit=max&auto=format&n=DEMw5onAg75H1sCr&q=85&s=239b2c0fb5bbcd7e55bc1f179c8f82c0" alt="" width="2243" height="546" data-path="images/guides/cloud-compass/cloud-compass/1f52d0c-image.png" />

Once the data is ready, you will be able to start exploring the dashboard insights. For more information about using the dashboard, click [here](/guides/cloud-compass/cloud-compass/#utilizing-the-cloud-compass-dashboard).

env zero will now run on a daily basis to fetch new cloud activity, ensuring an accurate and up-to-date view of your cloud environment.

Built with [Mintlify](https://mintlify.com).
