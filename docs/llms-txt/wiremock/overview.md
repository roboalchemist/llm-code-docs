# Source: https://docs.wiremock.io/versioning/overview.md

# Source: https://docs.wiremock.io/runner/overview.md

# Source: https://docs.wiremock.io/overview.md

# Source: https://docs.wiremock.io/import-export/overview.md

# Source: https://docs.wiremock.io/grpc/overview.md

# Source: https://docs.wiremock.io/graphql/overview.md

# Source: https://docs.wiremock.io/dynamic-state/overview.md

# Source: https://docs.wiremock.io/data-sources/overview.md

# Source: https://docs.wiremock.io/cli/overview.md

# Source: https://docs.wiremock.io/audit-events/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Audit Events Overview

> Send WireMock Cloud audit events to an AWS S3 bucket you own

WireMock Cloud generates audit events when you perform various actions within your account.  For example, creating or
deleting Mock APIs, changing settings or logging in and many more.  For our enterprise customers we provide the ability
to push these audit events to an AWS S3 bucket stored within your AWS account.

## Usage

The audit event feature is only available to users on our Enterprise or Enterprise Trial plans and you will need to be
an organisation administrator to create and manage audit event destinations.

To create and manage your S3 bucket destination, navigate to the [Organisation Page](https://app.wiremock.cloud/account/organisation)
on your account. On this page you will see the `Audit Events` section.

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/empty-s3-audit-destination.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f43ec54fb25af30b1bac93e4675dd12c" alt="Empty S3 audit event destination" data-og-width="1375" width="1375" data-og-height="370" height="370" data-path="images/audit-events/empty-s3-audit-destination.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/empty-s3-audit-destination.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=3017be60e27d28a0aa8f1319042f3ff2 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/empty-s3-audit-destination.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=44475a555d1e9b023b996d618715f4d5 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/empty-s3-audit-destination.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=9a023105aca95d13f210c66aaf89fa58 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/empty-s3-audit-destination.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=e5fe43291104220d6abaed40075054cf 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/empty-s3-audit-destination.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=137a6145a3b3091e8c419e9e6ff3a793 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/empty-s3-audit-destination.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=127e58a403ced76e684f7534f77d8f4b 2500w" />

This is where you will create and manage your S3 audit event destination. To set up an S3 audit event destination you
will need to configure your AWS account with an S3 bucket and a role to allow WireMock Cloud to push audit events to that
bucket.

## Configure Your AWS Account

The first step in setting up your S3 audit event destination is to configure your AWS account to allow WireMock Cloud
to save audit events to your bucket.  You can do this in the following way:

* Create the S3 bucket `<your-company-name>-wiremock-cloud-audit-events` (you can use any bucket name if you have your own naming
  convention but be sure to update the bucket name in the examples below)
* Create a policy called `wiremock-cloud-put-audit-events` with `s3:PutObject` on `arn:aws:s3:::<your-company-name>-wiremock-cloud-audit-events/*`

```json  theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "s3:PutObject"
        ],
        "Resource": "arn:aws:s3:::<your-company-name>-wiremock-cloud-audit-events/*"
      }
    ]
}
```

* Create an AWS account role for another AWS account
  * Specify account id `499333472133`.
  * Do **NOT** require external ID or MFA.
  * Choose `wiremock-cloud-put-audit-events` as the policy (the one you created above)
  * Name it `wiremock-cloud-put-audit-events`
  * Set the trust policy as so:

```json  theme={null}
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::499333472133:root"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

Once you have completed the steps above, you can navigate to the [Organisation Page](https://app.wiremock.cloud/account/organisation)
and continue the configuration there.

## Configure Your WireMock Cloud Account

Now you have configured your AWS account with the new bucket and role, you can add those details to the `Audit Events`
section on the Organisations page:

* Enter the bucket name into the `Bucket name` field
* Enter the full role arn into the `Role ARN` field

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/populated-s3-audit-destination.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=2078ffab8778ab49b2f219be05d2c43b" alt="Populated S3 audit event destination" data-og-width="1383" width="1383" data-og-height="368" height="368" data-path="images/audit-events/populated-s3-audit-destination.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/populated-s3-audit-destination.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f07f34c26eb09cbbc554d160aa872ac9 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/populated-s3-audit-destination.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=83142ab93f97b8f3d085ee1f51812a7f 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/populated-s3-audit-destination.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=1f292942db3efe17e40c6f6b0021a2ce 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/populated-s3-audit-destination.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=48795afb0f77f9e4d1cdc20d3953f7ef 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/populated-s3-audit-destination.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=ab26425ec954c61814ab5bda6cd3dea1 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/populated-s3-audit-destination.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=ff66208e1f4b7a1887cce94e2ead66b0 2500w" />

* Click on the `Save` button to add the S3 audit destination to your organisation

Once you have saved the audit destination, you will see some documentation you can copy to make sure the role permission
and trust relationship you created above is correct.  For a newly created audit destination you should see the status
message - `Status: Audit events are yet to be sent to this destination`

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/saved-s3-audit-event-destination.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=77ac28f6e67227e3aadc69aadf6fa9d6" alt="Saved S3 audit event destination" data-og-width="1263" width="1263" data-og-height="963" height="963" data-path="images/audit-events/saved-s3-audit-event-destination.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/saved-s3-audit-event-destination.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=30f04b824760a979ef270bafed124893 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/saved-s3-audit-event-destination.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=f3dbd9a43bd90b817b385493a363819d 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/saved-s3-audit-event-destination.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=358a66755a6a6643b183a1068594905b 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/saved-s3-audit-event-destination.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=411d29beffd35364e17fd438ac930bf1 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/saved-s3-audit-event-destination.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=31dbc320f8e513bf4626210e19084fed 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/saved-s3-audit-event-destination.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=a4dff96be0947b5bd3c3d6c920b104a1 2500w" />

## Testing Your S3 Audit Event Destination

Now you saved the S3 audit event destination you can test it to make sure everything works end to end.  Clicking on the
`Test` button will make WireMock Cloud attempt to post a test file to the bucket you created above.  If all works
correctly the button will turn green and you should have a new file saved to your S3 bucket called `test-wiremock-cloud-integration.txt`.
This file will contain the date and time the test was performed.

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-success-audit-event-destination.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=291f9898196ca9db9f19bc5886301633" alt="S3 audit event destination test success" data-og-width="1236" width="1236" data-og-height="303" height="303" data-path="images/audit-events/test-success-audit-event-destination.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-success-audit-event-destination.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d74513cbc325bf4aa0cb64b25edec7bc 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-success-audit-event-destination.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=aee09ac5029940e3051d85fa423c623d 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-success-audit-event-destination.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=460673ed492dc621c836783476b21e19 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-success-audit-event-destination.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=ac1a23cce89003924feed7aefa30bda5 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-success-audit-event-destination.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=1ed1ca891c1ace48e193336669196c9c 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-success-audit-event-destination.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=b111dedc73d315ff2b297c655346203a 2500w" />

Should an error occur trying to post the file to your S3 bucket, an error will be displayed to help you diagnose the issue.

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-failure-audit-event-destination.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d2eb9db5eeea037f5aaa9943935ed135" alt="S3 audit event destination test failure" data-og-width="1238" width="1238" data-og-height="302" height="302" data-path="images/audit-events/test-failure-audit-event-destination.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-failure-audit-event-destination.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=9ff99c20865c8552c34f54c0f1750e96 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-failure-audit-event-destination.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=efb4b6ddcf8e87070b7b54becb06424e 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-failure-audit-event-destination.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=806bf2d479e23630808143dd958fa42e 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-failure-audit-event-destination.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=6111faab8090ba80a098ecf6e7f80083 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-failure-audit-event-destination.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=e99c24cc1b66db3c2979dacbd3f55b10 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/test-failure-audit-event-destination.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=468f673ff663839ec5ddd472c703a6a0 2500w" />

## Deleting Your S3 Audit Event Destination

If you no longer require audit events to be sent to your S3 bucket you can delete the audit event destination from your
organisation.  This will stop audit events being set to your S3 bucket.  To do this you can click on the `Delete`
button.  This will display a confirmation dialog to allow you to confirm the deletion.

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/delete-audit-sink-confirmation.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=b79b6ef8e5773367cb0f21524f00810b" alt="Delete S3 audit event destination confirmation" data-og-width="735" width="735" data-og-height="233" height="233" data-path="images/audit-events/delete-audit-sink-confirmation.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/delete-audit-sink-confirmation.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d5d6f8dd9634758bbe2e2847f64032ef 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/delete-audit-sink-confirmation.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=c6706ea8dc72e6d1730a52c0c95e3663 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/delete-audit-sink-confirmation.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=409189f76975933e8734f543a5758f86 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/delete-audit-sink-confirmation.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=2b6d6809fcc585bb83b0d75944c5767e 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/delete-audit-sink-confirmation.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=6a13ead9018910051bbaa89b599194f9 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/delete-audit-sink-confirmation.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=02947cf253814744cbea23d81f5a2111 2500w" />

Clicking on `No` will close the dialog and no action will be taken, clicking on `Yes` will delete your S3 audit event
destination and no more audit events will be sent.

## Sending Audit Events To Your S3 Bucket

WireMock Cloud will send audit events to your S3 bucket in batches every 10 minutes.  There is a lookback window of
7 days for audit events.  This means if you are setting up an S3 audit event destination and have been a customer for
a while, the first batch of audit events sent to your bucket will span back 7 days prior to the date you setup the
destination.

Once audit events are successfully being sent to your bucket you will see the status message update on the Organisation page:

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-success.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=ea4ef362d5835819634e628d45af590e" alt="Successfully sent audit events" data-og-width="1231" width="1231" data-og-height="296" height="296" data-path="images/audit-events/audit-events-sent-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-success.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=d2b56b3beb4484ccc1903bc4c97871b1 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-success.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=eab1d01f351e204b59edde4164ca798c 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-success.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=ef0ce0d621319dd53e945d7be0e0cb36 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-success.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=7c33b8b8b41a13b01929e07e5d6ac24d 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-success.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=50012d950e32c2de1b1d3e43ab7b5a97 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-success.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=0ff2cf620d0b5605314a895417f317f6 2500w" />

If WireMock Cloud encounters an error while sending audit events to your S3 bucket, the status will be updated to
highlight the error. If audit events have been successfully sent in the past, the error will also contain the date the
last successful attempt was made:

<img src="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-failure.png?fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=5ded7f252cb5df71934681f007a436b5" alt="Failure to send audit events" data-og-width="1233" width="1233" data-og-height="336" height="336" data-path="images/audit-events/audit-events-sent-failure.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-failure.png?w=280&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=7c1dc80c8d98d193ea4effdd51024e5a 280w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-failure.png?w=560&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=6557a9671c3367e7df24ecba344ffe18 560w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-failure.png?w=840&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=372225fdb1e45d5c75f230338dff3b10 840w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-failure.png?w=1100&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=81caf09f45b3a985c1d0c3e036186d2c 1100w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-failure.png?w=1650&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=39140da7f9449665aac0e6145266b376 1650w, https://mintcdn.com/wiremockinc/46NqgX7QaQdjW6uv/images/audit-events/audit-events-sent-failure.png?w=2500&fit=max&auto=format&n=46NqgX7QaQdjW6uv&q=85&s=c62c7b4baf32f0358176f86bd91c9f47 2500w" />

Audit events are saved in your S3 bucket using the following structure:

```
|── 2025-02
|   |── 01
|   |   |── 2025-02-01T13-45-12-789Z-wjg0yr69.json
|   |── 02
|       |── 2025-02-02T13-32-12-789Z-16oe0mgo.json
|       |── 2025-02-02T14-29-12-789Z-9lrrjdm6.json
|── 2025-03
    |── 02
    |   |── 2025-03-02T13-23-12-789Z-kr731z1.json
    |── 03
        |── 2025-03-03T13-45-12-789Z-9odlj3w3.json
        |── 2025-03-03T14-29-12-789Z-38o4klr7.json
```

Each file follows the [new line delimited JSON specification](https://github.com/ndjson/ndjson-spec).

Audit events for the following items in WireMock Cloud are sent to your S3 bucket:

* Mock APIs
* Users
* Teams
* Organisations
* API Templates
* API Template Catalogues
* Data Sources
* Database Connections
* Keys
* Stub Mappings
* Mock API Settings
* Subscriptions
* Open API Git Integrations
* API Keys
* S3 Audit Destinations

More information about working with the audit event json can be found [here](./working-with-audit-events).

## Limits

You can read more about [plan limits here](./plan-limits/).
