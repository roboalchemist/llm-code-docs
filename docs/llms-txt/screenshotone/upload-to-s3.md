# Source: https://screenshotone.com/docs/guides/upload-to-s3/

# Upload to S3

You can use [ScreenshotOne screenshot API](https://screenshotone.com/) to take website screenshots and upload them directly to Amazon S3 and any other S3-compatible storage like [Cloudflare R2](https://www.cloudflare.com/products/r2/), [Backblaze](https://www.backblaze.com/), and others.

I will guide through a few simple steps of how you can do it.

Today's UI for Amazon AWS console or ScreenshotOne might be a bit different, and things can change after a while, but you should sense the overall approach from the post you need to apply to make it work.

If you are familiar with AWS, you can go straight away to [configure access to S3 in ScreenshotOne](#configure-access-to-s3-in-screenshotone).

## Prepare the bucket and credentials

Open the [S3 console](https://console.aws.amazon.com/s3/) and click on the "Create bucket" button:

![Create bucket](create_bucket_button.png)

Type the bucket name, choose a region, and other important for you settings:

![A bucket form](create_bucket_form.png)

Now, let's create access keys to upload to the S3 bucket.

:::danger
Never, ever, don't share the access key to your main account with ScreenshotOne or another service. Create an IAM user with as narrow access as possible and share its keys.
:::

> [AWS Identity and Access Management (IAM) user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users.html) is an entity that you create in AWS to represent the person or application that uses it to interact with AWS. A user in AWS consists of a name and credentials.

Before creating a user, we will create a narrow policy to restrict access to the bucket we created and only for putting objects into it.

> You manage access in AWS by creating [policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) and attaching them to IAM identities (users, groups of users, or roles) or AWS resources. A policy is an object in AWS that, when associated with an identity or resource, defines their permissions. AWS evaluates these policies when an IAM principal (user or role) makes a request. Permissions in the policies determine whether the request is allowed or denied.

Open [the IAM management console](https://console.aws.amazon.com/iam/), navigate to "Policies", then click on the "Create policy" button. And one the following screen, select `S3` as a service, then allow only `PutObject` operation for the bucket with the name `screenshotone`:

![Create policy](policy_s3_put_object.png)

After clicking on the "Create policy" button and entering the policy name:

![Create policy](policy_s3_review_policy.png)

I gave a clear name to the policy as an example. You can provide whatever you like.

Then open [the IAM management console](https://console.aws.amazon.com/iam/) again and navigate to users. Once you are here, click on the "Add users" button:

![Add users](iam_console.png)

After that, type username and select "Access key - Programmatic access":

![Username and credentials](username_and_access.png)

We need to select and attach the policy we created earlier to the user:

![Select policy](select_policy.png)

The user is primarily ready, so we can skip the following steps and get to the end, where we can see credentials:

![Credentials](user_is_created.png)

Copy the credentials and store them in safe place like password manager. We will need them in the next step to configure ScreenshotOne to upload screenshots.

I will save the credentials for our example to use in the next section:

```
Access key ID: AKIAURGNZP6VM5HASWIF
Secret access key: wVd8OgAnGIEdlQaWxDwzVcOQNO03G1dgFiDyHLPT
```

## Configure access to S3 in ScreenshotOne

:::caution
If you haven't created the bucket in the `us-east-1` AWS region, please, specify your bucket region through an endpoint in a format like `https://s3.<your-region>.amazonaws.com`.
:::

You can set credentials ([Access Key ID](https://screenshotone.com/docs/options/#storage_access_key_id) and [Secret Access Key](https://screenshotone.com/docs/options/#storage_secret_access_key)) when sending an API request or you cat to go to the [access page](https://dash.screenshotone.com/access). And put all the credentials you got from Amazon AWS for S3 into the "S3 access" configuration form:

![Access page](access_page.png)

I specified the default bucket, but you can use many buckets to upload screenshots and then override the target bucket with [the storage_bucket option](https://screenshotone.com/docs/options/#storage_bucket) when using API. But for example, I use only one bucket—it is enough.

## Take a website screenshot through API with `storing` options

ScreenshotOne API has [a bunch of options related to uploading screenshots to S3 storage](https://screenshotone.com/docs/options/#storing):

-   [store](https://screenshotone.com/docs/options/#store) triggers upload of the taken screenshot, rendered HTML or PDF to the configured S3 bucket.
-   [storage_path](https://screenshotone.com/docs/options/#storage_path)—specifies the key for the file, but not an extension. The extension will be added automatically based on the specified [format](https://screenshotone.com/docs/options/#format).
-   [storage_bucket](https://screenshotone.com/docs/options/#storage_bucket)—overrides the default bucket configured in the [access page](https://dash.screenshotone.com/access).
-   [storage_class](https://screenshotone.com/docs/options/#storage_class)—allows to specify [the object storage class](https://aws.amazon.com/s3/storage-classes/).

Let's take a screenshot and upload it to S3:

```
https://api.screenshotone.com/take?access_key=0MpjJxw8Vk7ZAw&url=https://nextjs.org&store=true&storage_path=nextjs.org
```

The result is:

![Next.js](nextjs.org.jpg)

And let's check S3:

![S3 results](s3_nextjs.png)

In case you don't need to return the resulting image and speed up uploading, add `response_type=empty` to the request:

```
https://api.screenshotone.com/take?access_key=0MpjJxw8Vk7ZAw&url=https://example.com&store=true&storage_path=example.com&response_type=empty
```

The result is a white screen—zero bytes sent from the ScrenshotOne API in response. And let's again check that the screenshot is uploaded:

![S3 results](s3_all.png)

That's it. But if you want to do it asynchronously?

## Async and Webhooks

ScreenshotOne supports [asynchronous screenshot rendering and webhooks](/docs/async-and-webhooks/). You can upload your screenshots to S3 asynchronously without waiting and then receive the resulting upload URL to your server.

To do that, specify additional parameters `async`, `webhook_url`, `storage_return_location`. And only JSON response type is supported.

So the full request might look like:

```
https://api.screenshotone.com/take?access_key=0MpjJxw8Vk7ZAw&url=https://example.com&store=true&storage_path=example.com&response_type=json&async=true&webhook_url=https://example.com&storage_return_location=true
```

Read more about [asynchronous screenshot rendering and webhooks](/docs/async-and-webhooks/).

## Why upload to S3

I don't know your use case and would be happy to know it, but there are a few reasons why customers of ScreenshotOne upload website screenshots to S3.

One is to use CDN that pulls images from S3 storage, and the other is to archive screenshots, process them later, or even compare them.

## Instead of summary

It makes me happy to help people solve their problems. And even happier when people pay for that. I hope today I solved yours. Have a good day or even night, and be happy 👌