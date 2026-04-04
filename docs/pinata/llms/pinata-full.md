# Pinata Documentation

Source: https://docs.pinata.cloud/llms-full.txt

---

# API Keys
Source: https://docs.pinata.cloud/account-management/api-keys



This page is where you can create, record, and delete API keys for the [Pinata API](/api-reference/introduction). Creating an API key is very simple! Just visit the page to start by click on the API Keys button in the left sidebar, then click "New Key" in the top right.

<img />

In the New Key modal you can choose if you want the key to be an Admin key and have full access over every endpoint, or scope the keys by selecting which endpoints you want to use. You can also give it a limited number of uses, and be sure to give it a name to keep track of it. Once you have that filled out click "Create Key" and it will show you the `pinata_api_key`, `pinata_api_secret_key`, and the `JWT`. It's best to click "Copy All" and keep the API key data safe and secure.

<Warning>Once API keys have been created, you will not be able to see the secret or JWT again</Warning>

Once you have created your keys you can go ahead and try testing them! You can even use them in our [API Reference section](/api-reference/endpoint/ipfs/test-authentication) :eyes: Or feel free to paste this into your terminal with your `JWT`

```bash cURL theme={null}
curl --request GET \
     --url https://api.pinata.cloud/data/testAuthentication \
     --header 'accept: application/json' \
     --header 'authorization: Bearer YOUR_PINATA_JWT'
```

If successful you should see this!

```shell bash theme={null}
{
  "message": "Congratulations! You are communicating with the Pinata API!"
}
```

## Managing Keys

From the Keys Page you can see the name of a key, the public key, when it was issues, how many max uses it has, and what permissions it was given.

<img />

At any point you can delete an API key by clicking on the Revoke button

<img />


# Billing
Source: https://docs.pinata.cloud/account-management/billing



The billing page is where you can upgrade your account, view your current usage, or make changes to your billing info.

<img />

## Usage

Heading over to the "Usage" tab, this is where you can view how much of your plan has been used in the month. Gateway Bandwidth and Requests are reset each month on your billing cycle date.

<Warning>
  If you reach 80% percent of your usage available, then you will start to
  receive emails and warnings that you are close to running out of space. If you
  are on the Free plan, then your account will no longer be able to upload or
  use the Dedicated Gateway once your account has gone above the limit by 25%.
</Warning>

<img />

## Payment Info

Clicking the 'Manage Billing' button will show you the current card in use and if it's the default. If you want to remove a card, then you will need to add a new one first and set it as default before removing the old one.

<Note>Pinata currently only accepts standard debit and credit cards</Note>

<img />

## Plan Selection

From the plan selection you can choose a plan that fits your need the most, whether that be upgrading or downgrading.

<Note>
  If you upgrade in the middle of a billing cycle, then you will only be charged
  the prorated amount
</Note>

<img />


# Limits
Source: https://docs.pinata.cloud/account-management/limits



The Private IPFS API and IPFS API have variying limits that users should be aware of.

## API Limits

API rate limits on both the Private IPFS API and IPFS API are currently determined by plan type:

| Plan       | Rate Limit              |
| ---------- | ----------------------- |
| Free       | 60 requests per minute  |
| Picnic     | 250 requests per minute |
| Fiesta     | 500 requests per minute |
| Enterprise | 100 requests per second |

### Exceptions

The following API calls have increased rate limits:

* Endpoints under `api.pinata.cloud/data/` have a rate limit of 30 requests per minute
* The [Pinning Services API endpoint for listing content](/api-reference/pinning-service-api) has a rate limit of 30 requests per minute

## File Restrictions

HTML files can be uploaded on any plan, but can only be retrieved through a Dedicated Gateway with a [Custom Domain](gateways/dedicated-ipfs-gateways).

Binary files are only allowed on a case by case basis, please contact [team@pinata.cloud](mailto:team@pinata.cloud) for assistance.

## Gateway Rate Limits

At this time there are currently no rate limits for users retrieving content from a dedicated gateway.

## Upload Size Limits

There differing limits on file sizes between the Private IPFS API and IPFS API

### Private IPFS API

Files that are over **100MB** will require using [resumable uploads](/files/uploading-files#resumable-uploads) to complete. If you are using the SDK and the method `upload.file()` this will be handled automatically.

Beyond 100MB the max file size is **25GB** at this time.

### IPFS API

<Warning>
  While the upload limit is 25GB we would recommend only uploading up to 15GB per file/folder for reliability reasons. We can try to assist uploads 15GB-25GB but we cannot guarantee success at this time.
</Warning>

There is no aggregate limit for uploads, but each individual upload (whether it is a file or a folder) is limited to **25 GB**.

There is also a file limit size of **10MB** for the pinJSONToIPFS API endpoint.


# Webhooks
Source: https://docs.pinata.cloud/account-management/webhooks

Subscribe to Pinata API events using Webhooks

Through the Pinata App you can create Webhooks for particular events fired from the Pinata API for your account specifically, like uploading or deleting a file.

## Setup

Navigate to the [Webhooks Tab]() inside the Pinata App and click "Add Endpoint" in the top right.

![webhooks create](https://docs.mypinata.cloud/ipfs/bafkreig535s7dg4gokb37cl3khns7uaq5sqauyzdur2picd76xfzowd5m4)

On the New Endpoint page you can put in a URL for your server endpoint that will receive the events. Additionally you can give it a description, which events it will subscribe to, and more advance options like rate limiting. Once you have your options selected click "Create" at the bottom.

<Tip>
  If you don't have an endpoint for your app or server yet, you can create a test one by clicking on the `Svix Play` link below the URL input.
</Tip>

![webhooks form](https://docs.mypinata.cloud/ipfs/bafkreicze5g4n2z7mr4r6o4p6o25lqbswsiytodqe6lwblzk2qmir6bpei)

Once your Webhook is created you will be taken to the dashboard where you can see incoming logs and events that are fired. Try triggering one of the events that you've selected for your webhook either from the Pinata App or from the API. Then come back to the dashboard to see the result!

![webhooks dashboard](https://docs.mypinata.cloud/ipfs/bafybeicvtsffigooqn26s5zpgligxwjodlespt6a4lyfpzljn4h2ypu2jy)

## Event Catalog

Check out the link below to browse all the available webhook events you can subscribe to!

<Card title="Webhook Event Catalog" href="https://event-types.pinata.cloud/" icon="link">
  Visit our Svix page for all Pinata Webhook events!
</Card>

## Signature Verification

Webhook signatures let you verify that webhook messages are actually sent by Pinata and not a malicious actor.

For a more detailed explanation, check out this article on [why you should verify webhooks](https://docs.svix.com/receiving/verifying-payloads/why).

To grab the secret for your Webhook locate it on the Webhook Dashboard on the right sidebar. Click on the reveal icon to view the secret and copy it.

![webhook secret](https://docs.mypinata.cloud/ipfs/bafybeid6jzbykbdoo742rzyq2l6bswahdxbnl7fmdgcraanjeagtokoeb4)

Our webhook partner Svix offers a set of useful libraries that make verifying webhooks very simple. Here is a an example using Javascript:

```typescript theme={null}
import { Webhook } from "svix";

const secret = "whsec_MfKQ9r8GKYqrTwjUPD8ILPZIo2LaLaSw";

// These were all sent from the server
const headers = {
  "webhook-id": "msg_p5jXN8AQM9LWM0D4loKWxJek",
  "webhook-timestamp": "1614265330",
  "webhook-signature": "v1,g0hM9SsE+OTPJTGt/tmIKtSyZlE3uFJELVlNIOLJ1OE=",
};
const payload = '{"test": 2432232314}';

const wh = new Webhook(secret);
// Throws on error, returns the verified content on success
const payload = wh.verify(payload, headers);
```

For more instructions and examples of how to verify signatures, check out their [webhook verification documentation](https://docs.svix.com/receiving/verifying-payloads/how).


# Workspaces
Source: https://docs.pinata.cloud/account-management/workspaces



<Note>Workspaces is only available on the [Picnic and Fiesta plans](https://pinata.cloud/pricing)</Note>

Workspaces is a feature that allows you to add multiple people to your account and collaborate in a natural way. With the Picnic plan, you'll get 3 seats to invite your teammates, and with Fiesta you'll get 5 seats, plus the ability to add more at an extra fee.

<iframe title="YouTube video player" />

## Inviting Members

<Note>
  At this time only Workspace Owners can invite members
</Note>

To get started, login with a paid account and click on the profile button in the top right, then select "Workspaces."

<img />

Once at the Workspaces screen, you can type in the email for the person you want to invite. They could already have a Pinata account or could be someone who hasn't signed up yet. Once they sign into their account, they will be prompted to accept the invite on the Workspaces page.

<img />

## Switching Workspaces

By default, when you login, you will be put in your account with your Workspace, and you can switch to another Workspace you are member of by clicking on the drop-down menu in the top left corner.

<img />

## Removing Members

<Note>
  At this time only Workspace Owners can remove members
</Note>

If you ever need to remove someone from a Workspace, you can do so from the Workspaces page. Click on the three small dots next to the user's email and click "remove member." You can invite them back at any time!

<img />


# Deleting Files
Source: https://docs.pinata.cloud/files/deleting-files



Deleting files from Pinata is simple and easy!

## Deleting Programatically

The SDK has a very simple [delete](/sdk/files/public/delete) method that will allow you to delete an array of files by `id`. Alternatively you can delete a single file with the [API](/api-reference/introduction).

<CodeGroup>
  ```typescript SDK theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const unpin = await pinata.files.public.delete([
    "3c52f1b8-11b1-40d9-849d-5f05a4bbd76d",
    "b72886db-9dd4-434c-a1b2-f9d36781ecee"
  ])
  ```

  ```typescript API {6,9,11} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function delete() {
    try {

      const fileId = "e0b102e9-d481-4192-ab44-b8f7ff010e9a"

      const request = await fetch(
        `https://api.pinata.cloud/v3/files/public/${fileId}`,
      {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${JWT}`,
        }
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### Deleting All Files

If you find yourself in a position where you need to delete most or all of your files you can use the [Auto Paginate](/sdk/files/public/list#auto-paginate) feature on the SDK to fetch all the IDs of your files and delete them in a few lines of code!

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
	pinataJwt: process.env.PINATA_JWT!,
	pinataGateway: "dweb.mypinata.cloud",
});

async function main() {
	try {
		let files = [];
		for await (const item of pinata.files.public.list()) {
			files.push(item.id);
		}
		const res = await pinata.files.public.delete(files);
	} catch (error) {
		console.log(error);
	}
}

main();
```

## Deleting by Web App

If you are trying to delete files, then you can do so by clicking on the on the 3 dots at the end of the row and selecting "Delete"

<img />

Additionally, with our Bulk File Actions tool, you can select and manage multiple files at once - up to 100!

<img />


# Groups
Source: https://docs.pinata.cloud/files/file-groups



Private Groups allow you to organize your Pinata content through the Pinata App, SDK, or API, giving you a clearer picture of what your files are being used for.

## SDK and API

With the [SDK](/sdk/groups/public), you can create groups, add files to groups, list details about a group, and more! You can also manage groups using the [API](/api-reference/endpoint/create-group).

### Create a Group

To create a group you can use the [create](/sdk/groups/public/create) method and passing in the `name` you want to give a group.

<CodeGroup>
  ```typescript SDK theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const group = await pinata.groups.public.create({
  	name: "My New Group",
  });
  ```

  ```typescript API theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function group() {
    try {

      const payload = JSON.stringify({
        name: "My New Group",
      })

      const request = await fetch("https://api.pinata.cloud/v3/groups/public", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${JWT}`,
        },
        body: payload,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

This will return the Group info

<CodeGroup>
  ```typescript SDK theme={null}
  {
    id: "01919976-955f-7d06-bd59-72e80743fb95",
    name: "Test Private Group",
    created_at: "2024-08-28T14:49:31.246596Z"
  }
  ```

  ```json API theme={null}
  {
    "data": {
      "id": "01919976-955f-7d06-bd59-72e80743fb95",
      "name": "Test Private Group",
      "created_at": "2024-08-28T14:49:31.246596Z"
    }
  }
  ```
</CodeGroup>

### Add or Remove Files from a Group

There are two ways you can add files to a group. The first is to add the file to a group on [upload](/sdk/upload/public/file).

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const upload = await pinata.upload.public
    .file(file)
    .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
  ```

  ```typescript API {13} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

      const file = new File(["hello"], "Testing.txt", { type: "text/plain" });

      formData.append("file", file);

      formData.append("network", "public")

      formData.append("group", "b07da1ff-efa4-49af-bdea-9d95d8881103")

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

Another option is to add files after the fact using the [addFiles](/sdk/groups/public/add-files) method.

<CodeGroup>
  ```typescript SDK theme={null}
  const upload = await pinata.groups.public.addFiles({
    groupId: "b07da1ff-efa4-49af-bdea-9d95d8881103",
    files: [
      "0ed5738f-07e7-4587-81fb-f04f8be15d77",
      "a277dc29-2ca3-4dfb-aeb9-3f2b23e956f7"
    ]
  })
  ```

  ```typescript API {6,8,11} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function group() {
    try {

      const groupId = "e0b102e9-d481-4192-ab44-b8f7ff010e9a"

      const fileId = "521f23f3-2749-4611-b757-3155b40ff570"

      const request = await fetch(
        `https://api.pinata.cloud/v3/groups/public/${groupId}/ids/${fileId}`,
      {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${JWT}`,
        }
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

Removing files can be done the exact same way with the [removeFiles](/sdk/groups/public/remove-files) method.

<CodeGroup>
  ```typescript SDK theme={null}
  const upload = await pinata.groups.public.removeFiles({
    groupId: "b07da1ff-efa4-49af-bdea-9d95d8881103",
    files: [
      "0ed5738f-07e7-4587-81fb-f04f8be15d77",
      "a277dc29-2ca3-4dfb-aeb9-3f2b23e956f7"
    ]
  })
  ```

  ```typescript API {6,8,11} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function group() {
    try {

      const groupId = "e0b102e9-d481-4192-ab44-b8f7ff010e9a"

      const fileId = "521f23f3-2749-4611-b757-3155b40ff570"

      const request = await fetch(
        `https://api.pinata.cloud/v3/groups/public/${groupId}/ids/${fileId}`,
      {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${JWT}`,
        }
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### Get a Group

To fetch details of an already existing group you can use the [get](/sdk/groups/public/get) and pass in the `groupId`.

<CodeGroup>
  ```typescript SDK theme={null}
  const groups = await pinata.groups.public.get({
  	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
  });
  ```

  ```typescript API {6,8,11} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function group() {
    try {

      const groupId = "e0b102e9-d481-4192-ab44-b8f7ff010e9a"

      const request = await fetch(
        `https://api.pinata.cloud/v3/groups/public/${groupId}`,
      {
        method: "GET",
        headers: {
          Authorization: `Bearer ${JWT}`,
        }
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

This will return the same group info received upon creation.

<CodeGroup>
  ```typescript SDK theme={null}
  {
    id: "0191997b-ca28-79e8-9dbc-a8044ad3e547",
    name: "My New Group 5",
    created_at: "2024-08-28T14:55:12.448504Z",
  }
  ```

  ```json APi theme={null}
  {
    "data": {
      "id": "0191997b-ca28-79e8-9dbc-a8044ad3e547",
      "name": "My New Group 5",
      "created_at": "2024-08-28T14:55:12.448504Z"
    }
  }
  ```
</CodeGroup>

### List All Groups

If you want to get all Groups or filter through them, you can use the [list](/sdk/groups/public/list) method.

<CodeGroup>
  ```typescript SDK theme={null}
  const groups = await pinata.groups.public.list()
  ```

  ```typescript API theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function group() {
    try {
      const url = "https://api.pinata.cloud/v3/groups/public"
      const request = await fetch(url, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${JWT}`,
        }
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

Results can be filtered with the following queries.

#### name

* Type: `boolean`

Filters groups based on the group name

<CodeGroup>
  ```typescript SDK theme={null}
  const groups = await pinata.groups.public
      .list()
      .name("SDK")
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/groups/public?name=SDK"
  ```
</CodeGroup>

#### limit

* Type: `number`

Limits the number of results

<CodeGroup>
  ```typescript SDK theme={null}
  const groups = await pinata.groups.public
      .list()
      .limit(10)
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/groups/public?limit=10"
  ```
</CodeGroup>

This will return an array of Groups and their respective info:

<CodeGroup>
  ```typescript SDK theme={null}
  {
    groups: [
      {
        id: "0191997b-ca28-79e8-9dbc-a8044ad3e547",
        name: "My New Group 5",
        created_at: "2024-08-28T14:55:12.448504Z",
      }
    ],
    next_page_token: "MDE5MWIzNGMtMWNmNy03MzExLThmMjYtZmZlZDMzYTVlY"
  }
  ```

  ```json API theme={null}
  {
    "groups": [
      {
        "id": "0191997b-ca28-79e8-9dbc-a8044ad3e547",
        "name": "My New Group 5",
        "created_at": "2024-08-28T14:55:12.448504Z"
      }
    ],
    "next_page_token": "MDE5MWIzNGMtMWNmNy03MzExLThmMjYtZmZlZDMzYTVlY"
  }
  ```
</CodeGroup>

### Updating a Group

You can update the name of a group using either the SDK or the API.

<CodeGroup>
  ```typescript SDK theme={null}
  const groups = await pinata.groups.public.update({
  	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
  	name: "My New Group 2",
  });
  ```

  ```typescript API theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function group() {
    try {

      const groupId = "e0b102e9-d481-4192-ab44-b8f7ff010e9a"

      const payload = JSON.stringify({
        name: "My New Group 2",
      })

      const request = await fetch(
        `https://api.pinata.cloud/v3/groups/public/${groupId}`,
      {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${JWT}`,
        },
        body: payload
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

This will return the updated Group info.

<CodeGroup>
  ```typescript SDK theme={null}
  {
    id: "3778c10d-452e-4def-8299-ee6bc548bdb0",
    name: "My New Group 2",
    created_at: "2024-08-28T20:58:46.96779Z"
  }
  ```

  ```json API theme={null}
  {
    "data": {
      "id": "01919ac8-a6f5-7e8e-a8a2-6cfe00122b90",
      "name": "Updated Name",
      "created_at": "2024-08-28T20:58:46.96779Z"
    }
  }
  ```
</CodeGroup>

### Delete a Group

<Note>
  Deleting a Group that has CIDs inside of it will not unpin/delete the files. Please use the [delete](/sdk/files/public/delete) method to actually delete a file from your account
</Note>

To delete a Group you can use the [delete](/sdk/groups/public/delete) method and pass in the `groupId`.

<CodeGroup>
  ```typescript SDK theme={null}
  const groups = await pinata.groups.public.delete({
  	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
  });
  ```

  ```typescript API theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function group() {
    try {

      const groupId = "e0b102e9-d481-4192-ab44-b8f7ff010e9a"

      const request = await fetch(
        `https://api.pinata.cloud/v3/groups/public/${groupId}`,
      {
        method: "DELETE",
        headers: {
          Authorization: `Bearer ${JWT}`,
        }
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

If successful the endpoint will return an `OK` response.


# Key-Values
Source: https://docs.pinata.cloud/files/key-values



A unique and powerful feature included with the IPFS API and Private IPFS API is the key-value store. Anytime you upload or update a file you can store up to 10 key-value pairs.

<CodeGroup>
  ```typescript SDK {3-6} theme={null}
  const upload = await pinata.upload.public
    .file(file)
    .keyvalues({
      env: "prod",
      userId: "abc123"
    })
  ```

  ```typescript API {13-18,20} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

      const file = new File(["hello"], "Testing.txt", { type: "text/plain" });

      formData.append("file", file);

      formData.append("network", "public")

      const keyvalues = JSON.stringify({
        keyvalues: {
          env: "prod",
          userId: "abc123"
        }
      })

      formData.append("keyvalues", keyvalues)

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

This small yet powerful feature allows you to remove the need for an external database in most cases. We like to call this paradigm **[File-Centric Architecture](https://pinata.cloud/blog/using-file-centric-architecture-to-build-simple-and-capable-apps/)**, where apps and their structure revolves around the files themselves. This creates a molecule like structure and keeps the data related to the file close by.

![cover](https://dweb.mypinata.cloud/files/bafybeieo4ww5lykpsegfgmse5o2d5s5onfvlkglzqmvbeldb2dkx26z2ve)

## Creating

Creating a new key-value for a file can be done in two ways:

### Uploading a File

By including the key-values as part of the upload [method](/sdk/upload/public/file) or [endpoint](/api-reference/endpoint/upload-a-file) and the file and the key-values will be created at the same time.

<CodeGroup>
  ```typescript SDK {3-8} theme={null}
  const upload = await pinata.upload.public
    .file(file)
    .keyvalues({
      env: "prod",
      userId: "abc123"
    })
  ```

  ```typescript API {13-18,20} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

      const file = new File(["hello"], "Testing.txt", { type: "text/plain" });

      formData.append("file", file);

      formData.append("network", "public");

      const keyvalues = JSON.stringify({
        keyvalues: {
          env: "prod",
          userId: "abc123"
        }
      })

      formData.append("keyvalues", keyvalues)

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### Updating an Existing File

If you've already uploaded a file and want to add a key-value you can do so with the update [method](/sdk/files/public/update) or [endpoint](/api-reference/endpoint/update-file).

<CodeGroup>
  ```typescript SDK {3-7} theme={null}
  const update = await pinata.files.public.update({
    id: "2b4ee88d-1032-4e4e-a373-97d1ab127f16", // Target File ID
    keyvalues: {
      env: "prod",
      userId: "abc123"
    }
  })
  ```

  ```typescript API {6,8-13,15-21} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function update() {
    try {

      const fileId = "2b4ee88d-1032-4e4e-a373-97d1ab127f16"

      const data = JSON.stringify({
        keyvalues: {
          env: "prod",
          userId: "abc123"
        }
      })

      const request = await fetch(`https://api.pinata.cloud/v3/files/public/${fileId}`, {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: data,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

## Retrieving

Since key-values exist with files, you can retrieve them by listing files either through the SDK [method](/sdk/files/public/list) or API [endpoint](/api-reference/endpoint/list-files), and filtering results by key-value. The operator will always be `===`.

<Tip>
  You can chain multiple key-value queries together and it will only return files that meet both values.
</Tip>

<CodeGroup>
  ```typescript SDK {3-5} theme={null}
  const files = await pinata.files.public
    .list()
    .keyvalues({
      user: "abc123"
    })
  ```

  ```typescript API {5} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function list() {
    try {
      const request = await fetch(`https://api.pinata.cloud/v3/files/public?metadata[user]=123`, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${JWT}`,
        }
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

## Updating

The key-value system will automatically detect if you are replacing an existing value for a given key. For example, if you have a key of `env` with a value of `prod`, if you make an update of `env: "dev"` it will replace the old value. If the key does not exist then it will make a new key-value entry.

<CodeGroup>
  ```typescript SDK {4} theme={null}
  const update = await pinata.files.public.update({
    id: "2b4ee88d-1032-4e4e-a373-97d1ab127f16", // Target File ID
    keyvalues: {
      env: "dev", // Previously `prod`
    }
  })
  ```

  ```typescript API {10} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function update() {
    try {

      const fileId = "2b4ee88d-1032-4e4e-a373-97d1ab127f16"

      const data = JSON.stringify({
        keyvalues: {
          env: "dev", // Previously `prod`
        }
      })

      const request = await fetch(`https://api.pinata.cloud/v3/files/public/${fileId}`, {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: data,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

## Deleting

You can remove a key-value entry by making the value `null`.

<CodeGroup>
  ```typescript SDK {4} theme={null}
  const update = await pinata.files.public.update({
    id: "2b4ee88d-1032-4e4e-a373-97d1ab127f16", // Target File ID
    keyvalues: {
      env: null, // Deletes the `env` key-value entry
    }
  })
  ```

  ```typescript API {6,8-13,15-21} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function update() {
    try {

      const fileId = "2b4ee88d-1032-4e4e-a373-97d1ab127f16"

      const data = JSON.stringify({
        keyvalues: {
          env: null, // Deletes the `env` key-value entry
        }
      })

      const request = await fetch(`https://api.pinata.cloud/v3/files/public/${fileId}`, {
        method: "PUT",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: data,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

## Further Reading

Check out some of our reading material on some of the possibilities of key-values and file-centric architecture!

<CardGroup>
  <Card title="Pinata’s KV Store - A File-Centric Database" href="https://pinata.cloud/blog/pinatas-kv-store-a-file-centric-database" />

  <Card title="Using File-Centric Architecture to Build Simple and Capable Apps" href="https://pinata.cloud/blog/using-file-centric-architecture-to-build-simple-and-capable-apps/" />
</CardGroup>


# List & Query Files
Source: https://docs.pinata.cloud/files/listing-files



Pinata gives you the ability to query uploaded files based on different filters and attributes such as name, [key-values](/files/key-values), date, and more. This is different from retrieving the actual contents of a file, which you can learn more about [here](/gateways/retrieving-files).

## Basic Usage

You can either use the [SDK](/sdk/files/public/list) or the [API](/api-reference/endpoint/list-files) as see in the examples below.

<CodeGroup>
  ```typescript SDK theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const files = await pinata.files.public.list()
  ```

  ```typescript API theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function files() {
    try {
      const url = "https://api.pinata.cloud/v3/files/public",

      const request = await fetch(url, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${JWT}`,
        }
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

This will return an array of file objects

<CodeGroup>
  ```typescript SDK theme={null}
  {
    files: [
      {
        id: "dd5f8888-bf15-4559-b8a2-6c626869507f",
        name: "Hello Files API",
        cid: "bafybeifq444z4b7yqzcyz4a5gspb2rpyfcdxp3mrfpigmllh52ld5tyzwm",
        size: 4861678,
        number_of_files: 1,
        mime_type: "TODO",
        group_id: null,
        created_at: "2024-08-27T14:57:51.485934Z",
      },
      {
        id: "e2057aa3-7b6c-4a45-b785-12ba297bcbd0",
        name: "Quickstart.png",
        cid: "bafkreiebavn2jzkqh3ehy4pkqkdi2otnho6gbcffkeqnunk2lw5nmnwaea",
        size: 223548,
        number_of_files: 1,
        mime_type: "TODO",
        group_id: "5f8adce6-7312-46e0-90f7-13896bed297d",
        created_at: "2024-08-28T23:46:07.823118Z",
      },
      {
        id: "ac5308a1-de49-40a3-9f5c-d20f1bb6206d",
        name: "hello.txt",
        cid: "bafkreiffsgtnic7uebaeuaixgph3pmmq2ywglpylzwrswv5so7m23hyuny",
        size: 11,
        number_of_files: 1,
        mime_type: "TODO",
        group_id: null,
        created_at: "2024-08-29T02:23:02.735018Z",
      }
    ],
    next_page_token: "MDE5MWIzNGMtMWNmNy03MzExLThmMjYtZmZlZDMzYTVlY"
  }
  ```

  ```json API theme={null}
  {
  	"data": {
  		"files": [
  			{
  				"id": "dd5f8888-bf15-4559-b8a2-6c626869507f",
  				"name": "Hello Files API",
  				"cid": "bafybeifq444z4b7yqzcyz4a5gspb2rpyfcdxp3mrfpigmllh52ld5tyzwm",
  				"size": 4861678,
  				"number_of_files": 1,
  				"mime_type": "TODO",
  				"group_id": null,
  				"created_at": "2024-08-27T14:57:51.485934Z"
  			},
  			{
  				"id": "e2057aa3-7b6c-4a45-b785-12ba297bcbd0",
  				"name": "Quickstart.png",
  				"cid": "bafkreiebavn2jzkqh3ehy4pkqkdi2otnho6gbcffkeqnunk2lw5nmnwaea",
  				"size": 223548,
  				"number_of_files": 1,
  				"mime_type": "TODO",
  				"group_id": "5f8adce6-7312-46e0-90f7-13896bed297d",
  				"created_at": "2024-08-28T23:46:07.823118Z"
  			},
  			{
  				"id": "ac5308a1-de49-40a3-9f5c-d20f1bb6206d",
  				"name": "hello.txt",
  				"cid": "bafkreiffsgtnic7uebaeuaixgph3pmmq2ywglpylzwrswv5so7m23hyuny",
  				"size": 11,
  				"number_of_files": 1,
  				"mime_type": "TODO",
  				"group_id": null,
  				"created_at": "2024-08-29T02:23:02.735018Z"
  			}
  		],
  		"next_page_token": "MDE5MWIzNGMtMWNmNy03MzExLThmMjYtZmZlZDMzYTVlY"
  	}
  }
  ```
</CodeGroup>

## Filters

When listing files there a few ways you can filter the results

### name

* Type: `string`

Filter results based on name

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const files = await pinata.files.public
    .list()
    .name("pinnie")
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/files/public?name=pinnie"
  ```
</CodeGroup>

### group

* Type: `string`

Filter results based on group ID

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const files = await pinata.files.public
    .list()
    .group("5b56981c-7e5b-4dff-aeca-de784728dddb")
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/files/public?group=5b56981c-7e5b-4dff-aeca-de784728dddb"
  ```
</CodeGroup>

### noGroup

* Type: `boolean`

Filter results to only show files that are not part of a group

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const files = await pinata.files.public
  		.list()
  		.noGroup(true)
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/files/public?group=null"
  ```
</CodeGroup>

### cid

* Type: `string`

Filter results based on CID

<CodeGroup>
  ```typescript SDK{3} theme={null}
  const files = await pinata.files.public
    .list()
    .cid("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/files/public?cid=bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
  ```
</CodeGroup>

### mimeType

* Type: `string`

Filter results based on mime type

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const files = await pinata.files.public
    .list()
    .mimeType("image/png")
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/files/public?mimeType=image/png"
  ```
</CodeGroup>

### keyvalues

* Type: `Record<string | string>`

Filter results based on keyvalue pairs in metadata

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const files = await pinata.files.public
    .list()
    .keyvalues({
      env: "prod"
    })
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/files/public?keyvalues[env]=prod"
  ```
</CodeGroup>

### order

* Type: `"ASC" | "DESC"`

Order results either ascending or descending by created date

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const files = await pinata.files
    .list()
    .order("ASC")
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/files?order=ASC"
  ```
</CodeGroup>

### limit

* Type: `number`

Limit the number of results

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const files = await pinata.files
    .list()
    .limit(10)
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/files?limit=10"
  ```
</CodeGroup>

### cidPending

* Type: `boolean`

Filters results and only returns files where `cid` is still `pending`

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const files = await pinata.files
    .list()
    .cidPending(true)
  ```

  ```typescript API theme={null}
  const url = "https://api.pinata.cloud/v3/files?cidPending=true"
  ```
</CodeGroup>

## Auto Paginate (SDK)

The `list` method has an auto pagination feature that is triggered when used inside a `for await` iterator

```typescript theme={null}
for await (const item of pinata.files.list() {
  console.log(item.id);
}
```

Works like magic ✨


# Collections
Source: https://docs.pinata.cloud/files/nft-backup/collections

View your NFT collections and their IPFS CIDs

After syncing a wallet, view your NFT collections and their CIDs.

## Viewing Collections

<img alt="Image" />

Each collection shows:

| Field      | Description     |
| ---------- | --------------- |
| Name       | Collection name |
| Chain      | Blockchain      |
| NFTs Owned | Your NFT count  |
| CIDs       | IPFS CIDs found |

## Collection Details

<img alt="Image" />

Click a collection to see:

* Collection metadata (image, description)
* List of CIDs with backup status

### CID Information

| Field     | Description                    |
| --------- | ------------------------------ |
| CID       | IPFS content identifier        |
| Source    | `metadata` or `image`          |
| Backed Up | Whether pinned to your account |

## Filtering

Filter collections by chain using the dropdown.

## Related

* [Wallets](/files/nft-backup/wallets) - Add and sync wallets
* [Sync](/files/nft-backup/sync) - Sync CIDs


# Overview
Source: https://docs.pinata.cloud/files/nft-backup/overview

Backup your NFT collections to Pinata

Pin all IPFS content from your NFT collections to your Pinata account.

## Two Ways to Backup

<CardGroup>
  <Card title="Manual Sync" icon="rotate">
    Sync your wallet on-demand and choose which CIDs to backup. Best for one-time backups or when you want full control over what gets pinned.
  </Card>

  <Card title="Automated Backups" icon="clock">
    Enable auto-backup to automatically pin new CIDs whenever you sync. Set it and forget it—your NFTs stay protected.
  </Card>
</CardGroup>

## How It Works

1. **Connect** - Add your wallet address
2. **Sync** - Pinata scans your wallet across supported chains and extracts IPFS CIDs
3. **Backup** - Pin CIDs to your Pinata account (manually or automatically)

Own multiple NFTs from the same collection? Shared assets are only pinned once, so you won't pay for duplicates.

<iframe title="YouTube video player" />

## Supported Chains

|           |          |           |
| --------- | -------- | --------- |
| Ethereum  | Base     | Polygon   |
| Flow      | Zora     | Arbitrum  |
| Monad     | Optimism | Avalanche |
| Blast     | Sei      | B3        |
| Berachain | ApeChain | Ronin     |
| Abstract  | Shape    | Unichain  |
| Gunzilla  | HyperEVM | Somnia    |

## Next Steps

<CardGroup>
  <Card title="Wallets" icon="wallet" href="/files/nft-backup/wallets">
    Add and sync wallets
  </Card>

  <Card title="Collections" icon="grid-2" href="/files/nft-backup/collections">
    View your collections
  </Card>

  <Card title="Sync" icon="cloud-arrow-up" href="/files/nft-backup/sync">
    Sync CIDs
  </Card>
</CardGroup>


# Sync
Source: https://docs.pinata.cloud/files/nft-backup/sync

Pin your NFT CIDs to Pinata

After syncing a wallet, backup the IPFS CIDs to your Pinata account. Own multiple NFTs from the same collection? Shared assets are only pinned once, so you won't pay for duplicates.

## Backup All

To backup all CIDs for a wallet:

1. Go to [NFT Backup](https://app.pinata.cloud/nft-backup/wallets)
2. Select a wallet
3. Click **Backup All**

Pinata pins all CIDs in the background. This can take a few minutes.

## Auto-Backup

<img alt="Image" />

Enable auto-backup to automatically pin new CIDs when you sync:

1. Select a wallet
2. Toggle **Auto-Backup** on

## Related

* [Wallets](/files/nft-backup/wallets) - Add and sync wallets
* [Collections](/files/nft-backup/collections) - View collections


# Wallets
Source: https://docs.pinata.cloud/files/nft-backup/wallets

Add wallets to backup your NFT collections

Add your wallet address to Pinata, then sync to fetch your NFT collections.

<img alt="Image" />

## Adding a Wallet

1. Go to [NFT Backup](https://app.pinata.cloud/nft-backup/wallets)
2. Click **Add Wallet**
3. Enter your wallet address
4. Click **Register**

## Syncing a Wallet

After adding a wallet, sync it to fetch your NFT collections:

1. Select a wallet
2. Click **Sync**

Syncing scans your wallet across supported chains and extracts any IPFS CIDs from the metadata and images. This can take a few minutes depending on how many NFTs you have.

## Managing Wallets

From the wallets page you can:

* View sync status and CID counts
* Enable auto-backup

## Related

* [Collections](/files/nft-backup/collections) - View synced collections
* [Sync](/files/nft-backup/sync) - Sync CIDs


# Presigned URLs
Source: https://docs.pinata.cloud/files/presigned-urls



There are situations where you may need to upload a file client side instead of server side, but doing so might risk exposing an API key. To solve this you can create a presigned upload URL on the server and then pass it to the client for it to be consumed. Creating signed upload URLs can be done with either the [Files SDK](/sdk/upload/public/create-signed-url) or the [API](/api-reference/endpoint/create-signed-upload-url), and you can designate how long the URL is valid for, how large the file can be, the type of file allowed, or extra metadata like a name and [keyvalues](/files/key-files).

For a more robust example, check out our guides on Hono and React!

<CardGroup>
  <Card href="/frameworks/hono" icon="fire" title="Hono Guide" />

  <Card href="/frameworks/react" icon="react" title="React Guide" />
</CardGroup>

## Usage

Setting up a server side API endpoint might look something like this:

<CodeGroup>
  ```typescript SDK theme={null}
  import { type NextRequest, NextResponse } from "next/server";
  import { pinata } from "@/utils/config"; // Import the Pinata SDK instance

  export const dynamic = "force-dynamic";

  export async function GET() {
    // Handle your auth here to protect the endpoint
    try {
      const url = await pinata.upload.public.createSignedURL({
        expires: 30, // The only required param
        mimeTypes: ["text/*"], // Optional restriction for certain file types
        maxFileSize: 5000000 // Optional file size limit
      })
      return NextResponse.json({ url: url }, { status: 200 }); // Returns the signed upload URL
    } catch (error) {
      console.log(error);
      return NextResponse.json({ text: "Error creating signed URL:" }, { status: 500 });
    }
  }
  ```

  ```typescript API theme={null}
  import { type NextRequest, NextResponse } from "next/server";

  export const dynamic = "force-dynamic";

  export async function GET() {
    // Handle your auth here to protect the endpoint
    try {
      // Prepare payload data for request
      const data = JSON.stringify({
        network: "public",
        expires: 30, // Number of seconds the signed url is good for
        filename: "Client file", // Optional name
        allow_mime_types: [ "text/*" ], // Optional array of allowed file types
        max_file_size: 5000000 // optional max file size
      })
      // send request and parse response
      const urlRequest = await fetch("https://uploads.pinata.cloud/v3/files/sign", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${process.env.PINATA_JWT}`
        },
        body: data
      })
      const urlResponse = await urlRequest.json()
      return NextResponse.json({ url: urlResponse.data }, { status: 200 }); // Returns the key data
    } catch (error) {
      console.log(error);
      return NextResponse.json({ text: "Error creating API Key:" }, { status: 500 });
    }
  }
  ```
</CodeGroup>

Then back on the client side code, you can upload using the signed URL instead of the regular upload endpoint.

<Note>
  If you're using the SDK you can use the `.url()` parameter on any of the upload methods and pass in the signed upload URL there. If you are using the API you can simply make the upload request using the signed URL as the endpoint.
</Note>

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const urlRequest = await fetch("/api/url"); // Fetches the temporary upload URL from your server
  const urlResponse = await urlRequest.json(); // Parse response
  const upload = await pinata.upload.public
    .file(file)
    .url(urlResponse.url); // Upload the file with the signed URL
  ```

  ```typescript API {1-2,13} theme={null}
  const urlRequest = await fetch("/api/url"); // Fetches the temporary upload URL
  const urlResponse = await urlRequest.json(); // Parse response
  async function upload() {
    try {
      const formData = new FormData();

      const file = new File(["hello"], "Testing.txt", { type: "text/plain" });

      formData.append("file", file);

      formData.append("network", "public")

      const request = await fetch(urlResponse.url, {
        method: "POST",
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

## Reference

Below are the availble parameters for presigned URLs

### expires

* Type: `number`

The number of seconds the signed URL should be valid for

```typescript {2} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
});
```

### name (Optional)

* Type: `string`

Name for the file to be uploaded

```typescript {3} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	name: "My Cool File"
});
```

### mimeTypes (Optional)

* Type: `string[]`

Specify allowed file mime types and prevent uploads from files that do not match. Accepts wildcard mime types as well.

```typescript {3-6} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	mimeTypes: [
	  "image/*",
		"application/json"
	]
});
```

### maxFileSize (Optional)

* Type: `number`

Restrict upload to a specified file size in `bytes`

```typescript {3} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	maxFileSize: 50000 // 50kb
});
```

### groupId (Optional)

* Type: `string`

The target groupId the file would be uploaded to

```typescript {3} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	groupId: "ad4bc3bf-8794-49e7-94ff-fea1ce745779"
});
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Keyvalue pairs for the uploaded file

```typescript {3-5} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	keyvalues: {
	  env: "prod"
	}
});
```

### date (Optional)

* Type: `number`

A UNIX timestamp of the date a URL is signed

```typescript {1-2,6} theme={null}
const date = Math.floor(new Date().getTime() / 1000);
//date: 1724943711

const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	date: date
});
```


# Private IPFS
Source: https://docs.pinata.cloud/files/private-ipfs



IPFS has traditionally been a fully public network, so anything you pin can be accessed by anyone if they have the CID. While this is a benefit for a majority of blockchain applications, there are still cases where true privacy is needed. This is why Pinata has built Private IPFS, a new service that allows you to keep content private and only share when authorized.

## Private vs Public Network

Everything in the SDK and API have been separated by two networks: `public` and `private`. This means files and groups will be in separate resources and will be accessed by designating the network in either the SDK method or API route.

### Uploading

<CodeGroup>
  ```typescript SDK theme={null}
  // Uploads a file to Public IPFS
  const publicUpload = await pinata.upload.public.file(file)

  // Uploads a file to Private IPFS
  const privateUpload = await pinata.upload.private.file(file)
  ```

  ```typescript {11} API theme={null}
  const JWT = "PINATA_JWT";

  async function uploadFile() {
    try {
      const text = "Hello World!";
      const blob = new Blob([text], { type: "text/plain" });
      const file = new File([blob], "hello-world.txt");
      const data = new FormData();
      data.append("file", file);
      // Upload a file to Public IPFS
      data.append("network", "public")

      const request = await fetch(
        "https://uploads.pinata.cloud/v3/files",
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${JWT}`,
          },
          body: data,
        }
      );
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### Listing and Querying

<CodeGroup>
  ```typescript SDK theme={null}
  // List public files
  const files = await pinata.files.public.list()

  // List private files
  const files = await pinata.files.private.list()
  ```

  ```typescript {6,8} API theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function files() {
    try {
      // Designate network to list either public or private files
      const network = "public"

      const url = `https://api.pinata.cloud/v3/files/${network}`,

      const request = await fetch(url, {
        method: "GET",
        headers: {
          Authorization: `Bearer ${JWT}`,
        }
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### Groups

<CodeGroup>
  ```typescript SDK theme={null}
  // Create a public group
  const group = await pinata.groups.public.create({
  	name: "My Public Group",
  });

  // Create a private group
  const group = await pinata.groups.private.create({
  	name: "My Private Group",
  });
  ```

  ```typescript {5,7} API theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function group() {
    try {
      const network = "public"

      const endpoint = `https://api.pinata.cloud/v3/groups/${network}`

      const payload = JSON.stringify({
        name: "My Public Group",
      })

      const request = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${JWT}`,
        },
        body: payload,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

## Accessing Private Files

With Public IPFS you can simply access a file through an IPFS Gateway with a CID. Since Private IPFS does not announce to the public IPFS network the only way you can access them is with a temporary access link. This can be generated with either the SDK or the API and set to expire after a designated number of seconds.

<CodeGroup>
  ```typescript SDK theme={null}
  const url = await pinata.gateways.private.createAccessLink({
  	cid: "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq", // CID of the file to access
  	expires: 30, // Number of seconds the link is valid for
  });
  ```

  ```typescript API theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function createAccessLink() {
    try {

      // Endpoint for creating access links
      const url = "https://api.pinata.cloud/v3/files/download_link"

      // CID of the file you want to access
      const cid = "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"

      // Current Date
    	const date = Math.floor(new Date().getTime() / 1000);

      const data = JSON.stringify({
        url: `https://example.mypinata.cloud/files/${cid}`, // Gateway URL for the file using /files/ in the path
        expires: 180, // Number of seconds the link will be valid for
        date: date, // Current date of request
        method: "GET" // GET for accessing file
      })

      const request = await fetch(url, {
        method: "POSt",
        headers: {
          Authorization: `Bearer ${JWT}`,
          "Content-Type": "application/json"
        },
        body: data
      });
      const response = await request.json();
      return response.data
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

## Monetizing Private Files

Want to get paid for access to your private content? Check out [x402 Monetization](/files/x402), which allows you to attach payment requirements to private files using USDC on Base.

## Example Apps

Pinata has built several example apps and tutorials you can reference to see how Private IPFS enables token gated experiences in blockchain and crpto contexts.

<Card title="PinataCloud/concealmint-client" href="https://github.com/PinataCloud/concealmint-client" icon="github">
  GitHub repo for [CONCEALMINT](https://concealmint.com), an app for creating and access Private NFTs
</Card>

<CardGroup>
  <Card title="Making Private NFTs" href="https://pinata.cloud/blog/making-private-nfts/">
    By using Private IPFS you can gate acceess to files based on NFT ownership
  </Card>

  <Card title="How to Build a Farcaster Native Gumroad on Base" href="https://www.pinata.cloud/blog/how-to-build-a-farcaster-native-gumroad-on-base/">
    Sell digital content inside Farcaster frames and keeping it secure through Private IPFS
  </Card>

  <Card title="How To Build Simple Logging For Your Crypto App With Private IPFS" href="https://www.pinata.cloud/blog/how-to-build-simple-logging-for-your-crypto-app-with-private-ipfs/">
    Add simple yet private logging to your crypto app using Private IPFS
  </Card>

  <Card title="Building a Macintosh-Inspired Retro File System in the Browser" href="https://www.pinata.cloud/blog/building-a-macintosh-inspired-retro-file-system-in-the-browser/">
    See the possibilities of file management using Groups and Private IPFS
  </Card>
</CardGroup>


# Signatures
Source: https://docs.pinata.cloud/files/signatures

Learn how to use Pinata to cryptographically sign CIDs

In a post-AI world it will become more and more evident that every piece of content will need a cryptographic signature to verify it's authenticity. Pinata is taking steps in this direction with the [Signatures API](/sdk/signatures/public) and the [Content Addressable Gateway Plugin](/gateways/plugins/content-addressable).

## Signature Standard

Pinata is using the EIP-712 signature standard for signing CIDs with the following domain and types.

```typescript theme={null}
export const domain = {
  name: "Sign Content",
  version: "1.0.0",
  chainId: 1,
} as const;

export const types = {
  Sign: [
    { name: "address", type: "address" },
    { name: "cid", type: "string" },
    { name: "date", type: "string" },
  ],
  EIP712Domain: [
    {
      name: "name",
      type: "string",
    },
    {
      name: "version",
      type: "string",
    },
    {
      name: "chainId",
      type: "uint256",
    },
  ],
};
```

### address

* Type: `address`

The wallet address of the user singing the CID

```
0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826
```

### cid

* Type: `string`

The target CID to be signed

```
bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4
```

### date

* Type: `string`

The date the target CID was first uploaded to Pinata

```
2024-07-29T18:29:47.355Z
```

## Creating a Signature

In order to sign a CID you can use any library that support EIP-712 signing, like the example below with [viem](https://viem.sh/docs/actions/wallet/signTypedData).

<CodeGroup>
  ```typescript example.ts theme={null}
  import { account, walletClient } from './config'
  import { domain, types } from './data'

  const signature = await walletClient.signTypedData({
    account,
    domain,
    types,
    primaryType: 'Sign',
    message: {
      address: '0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826',
      cid: 'bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4',
      date: "2024-07-29T18:29:47.355Z"
    }
  })
  ```

  ```typescript data.ts theme={null}
  export const domain = {
    name: "Sign Content",
    version: "1.0.0",
    chainId: 1,
  } as const;

  export const types = {
    Sign: [
      { name: "address", type: "address" },
      { name: "cid", type: "string" },
      { name: "date", type: "string" },
    ],
    EIP712Domain: [
      {
        name: "name",
        type: "string",
      },
      {
        name: "version",
        type: "string",
      },
      {
        name: "chainId",
        type: "uint256",
      },
    ],
  };
  ```

  ```typescript config.ts theme={null}
  import { createWalletClient, custom } from 'viem'
  import { mainnet } from 'viem/chains'

  export const walletClient = createWalletClient({
    chain: mainnet,
    transport: custom(window.ethereum!),
  })

  export const [account] = await walletClient.getAddresses()
  ↑ JSON-RPC Account

  // export const account = privateKeyToAccount(...)
  ↑ Local Account
  ```
</CodeGroup>

## Adding Signature to CID

In order to attach a signature to a CID the following requirements must be met:

* The CID being signed is owned by the signer
* The CID being signed was first uploaded by the signer
* The CID must not already have an existing signature with Pinata

After creating the signature with the previous step you can add it to the CID with the [add](/sdk/signatures/public/add) method in the SDK.

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signature = await pinata.signatures.public.add({
  cid: "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU",
  signature: "0x1b...911b",
  address: "0xB3899AA8E13172E48D44CE411b0c4c2f08730Dc6"
});
```

## Getting a Signature for a CID

There are two ways you can an existing signature for a CID: the [get](/sdk/signatures/public/get) method in the SDK or the [Content Addressable Gateway Plugin](/gateways/plugins/content-addressable).

### Content Addressable Gateway Plugin

After [installing the plugin](/gateways/plugins/getting-started#installing-plugins) you can simply request a CID through the Dedicated Gateway and get the signature in the header `pinata-signauture`.

```typescript theme={null}
const signatureReq = await fetch(
  `https://<YOUR_GATEWAY_DOMAIN>.mypinata.cloud/ipfs/<CID>`,
  {
    method: "HEAD",
  }
);
const signature = signatureReq.headers.get("pinata-signature");
```

### SDK

You can also use the [get](/sdk/signatures/public/get) method to get a signature for a given CID.

<Note>
  This method will check all CIDs on Pinata and will return a signature if it exists
</Note>

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signature = await pinata.signatures.public.get(
  "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU"
);
```

## Verifying a Signature

Since the signatures are using the EIP-712 standard you can use a library like [Viem](https://viem.sh/docs/utilities/verifyTypedData) to verify with the same typed data used to create it.

<CodeGroup>
  ```typescript example.ts theme={null}
  import { account, walletClient } from './config'
  import { domain, types } from './data'
  import { verifyTypedData } from 'viem'

  const CID = "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"

  const signatureReq = await fetch(
    `https://example-gateway.mypinata.cloud/ipfs/${CID}`,
    {
      method: "HEAD",
    }
  );
  const signature = signatureReq.headers.get("pinata-signature");

  const valid = await verifyTypedData({
    address: account.address,
    domain,
    types,
    primaryType: 'Sign',
    message: {
      address: '0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826',
      cid: 'bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4',
      date: "2024-07-29T18:29:47.355Z"
    },
    signature,
  })
  ```

  ```typescript data.ts theme={null}
  export const domain = {
    name: "Sign Content",
    version: "1.0.0",
    chainId: 1,
  } as const;

  export const types = {
    Sign: [
      { name: "address", type: "address" },
      { name: "cid", type: "string" },
      { name: "date", type: "string" },
    ],
    EIP712Domain: [
      {
        name: "name",
        type: "string",
      },
      {
        name: "version",
        type: "string",
      },
      {
        name: "chainId",
        type: "uint256",
      },
    ],
  };
  ```

  ```typescript config.ts theme={null}
  import { createWalletClient, custom } from 'viem'
  import { mainnet } from 'viem/chains'

  export const walletClient = createWalletClient({
    chain: mainnet,
    transport: custom(window.ethereum!),
  })

  export const [account] = await walletClient.getAddresses()
  ↑ JSON-RPC Account

  // export const account = privateKeyToAccount(...)
  ↑ Local Account
  ```
</CodeGroup>

## Removing a Signature for a CID

To delete an existing signautre for a given CID you can use the [delete](/sdk/signatures/public/delete) method.

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signature = await pinata.signatures.public.delete(
  "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU"
);
```


# Uploading Files
Source: https://docs.pinata.cloud/files/uploading-files



<img />

At the core of Pinata's services is our IPFS APIs which allow you to upload files to either public or private IPFS. You can read more about the difference between the two [here](/files/private-ipfs).

Let's look at the multiple ways you can upload files!

## How to Upload Files

Uploading files with Pinata is simple, whether you want to use the SDK or the API. Key things to know:

* Uploads are done through `multipart/form-data` requests
* The SDK and API accept File objects per the [Web API Standard for Files]()
* You can add additional info to your upload such as a custom name for the file, keyvalue metadata, and a target group destination for organization

Here is a simple example of how you might upload a file in Typescript

<CodeGroup>
  ```typescript SDK theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const file = new File(["hello"], "Testing.txt", { type: "text/plain" });
  const upload = await pinata.upload.public.file(file);
  ```

  ```typescript API theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

      const file = new File(["hello"], "Testing.txt", { type: "text/plain" });

      formData.append("file", file);

      formData.append("network", "public");

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

This will return the following response

<CodeGroup>
  ```typescript SDK theme={null}
  {
      id: "349f1bb2-5d59-4cab-9966-e94c028a05b7",
      name: "file.txt",
      cid: "bafybeihgxdzljxb26q6nf3r3eifqeedsvt2eubqtskghpme66cgjyw4fra",
      size: 4682779,
      number_of_files: 1,
      mime_type: "text/plain",
      group_id: null
  }
  ```

  ```JSON API theme={null}
  {
    "data": {
      "id": "349f1bb2-5d59-4cab-9966-e94c028a05b7",
      "name": "file.txt",
      "cid": "bafybeihgxdzljxb26q6nf3r3eifqeedsvt2eubqtskghpme66cgjyw4fra",
      "size": 4682779,
      "number_of_files": 1,
      "mime_type": "text/plain",
      "group_id": null
    }
  }
  ```
</CodeGroup>

* `id`: The ID of the file used for getting info, updating, or deleting
* `name`: The name of the file or the provided name in the `addMetadata` method
* `cid`: A cryptographic hash based on the contents of the file
* `size`: The size of the file in bytes
* `number_of_files`: The number of files in a reference
* `mime_type`: The mime type of the uploaded file
* `group_id`: The group the file was uploaded to if applicable

### Metadata

When uploading a file you can add additional metadata using the `name` or `keyvalues` methods after the selected upload method. This can include an optional `name` override or `keyvalue` pairs that can be used to searching the file later on

<Tip>
  [Check out the Key-Values doc for more info](/files/key-values)
</Tip>

<CodeGroup>
  ```typescript SDK {3-8} theme={null}
  const upload = await pinata.upload.public
    .file(file)
    .name("hello.txt")
    .keyvalues({
      env: "prod"
    })
  ```

  ```typescript API {13,15-19, 21} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

      const file = new File(["hello"], "Testing.txt", { type: "text/plain" });

      formData.append("file", file);

      formData.append("network", "public");

      formData.append("name", "hello.txt");

      const keyvalues = JSON.stringify({
        keyvalues: {
          env: "prod"
        }
      })

      formData.append("keyvalues", keyvalues);

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### Groups

Pinata offers Private IPFS Groups to organize your content. You can upload a file to a group by using the `group` method.

<Tip>
  [Check out the Groups doc for more info](/files/file-groups)
</Tip>

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const upload = await pinata.upload.public
    .file(file)
    .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
  ```

  ```typescript API {13} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

      const file = new File(["hello"], "Testing.txt", { type: "text/plain" });

      formData.append("file", file);

      formData.append("network", "public");

      formData.append("group", "b07da1ff-efa4-49af-bdea-9d95d8881103");

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### Client Side Uploads

There are situations where you may need to upload a file client side instead of server side. A great example is in Next.js where there is a 4MB file size restriction for files passed through Next's API routes. To solve this you can create a signed upload URL on the server and then pass it to the client for it to be consumed. This way your admin API key stays safe behind a server. Creating signed upload URLs can be done with either the [SDK](/sdk/upload/public/create-signed-url) or the [API](/api-reference/endpoint/create-signed-upload-url), and you can designate how long the URL is valid for or if there is other infromation you want to include such as metadata or a group ID.

Setting up a server side API endpoint might look something like this:

<CodeGroup>
  ```typescript SDK theme={null}
  import { type NextRequest, NextResponse } from "next/server";
  import { pinata } from "@/utils/config"; // Import the Files SDK instance

  export const dynamic = "force-dynamic";

  export async function GET() {
    // Handle your auth here to protect the endpoint
    try {
      const url = await pinata.upload.public.createSignedURL({
        expires: 30, // The only required param
        name: "Client File",
        group: "my-group-id"
      })
      return NextResponse.json({ url: url }, { status: 200 }); // Returns the signed upload URL
    } catch (error) {
      console.log(error);
      return NextResponse.json({ text: "Error creating signed URL:" }, { status: 500 });
    }
  }
  ```

  ```typescript API theme={null}
  import { type NextRequest, NextResponse } from "next/server";

  export const dynamic = "force-dynamic";

  export async function GET() {
    // Handle your auth here to protect the endpoint
    try {
      // Prepare payload data for request
      const data = JSON.stringify({
        network: "public",
        expires: 30,
        filename: "Client file",
        group_id: "my-group-id"
      })
      // send request and parse response
      const urlRequest = await fetch("https://uploads.pinata.cloud/v3/files/sign", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${process.env.PINATA_JWT}`
        },
        body: data
      })
      const urlResponse = await urlRequest.json()
      return NextResponse.json({ url: urlResponse.data }, { status: 200 }); // Returns the key data
    } catch (error) {
      console.log(error);
      return NextResponse.json({ text: "Error creating API Key:" }, { status: 500 });
    }
  }
  ```
</CodeGroup>

Then back on the client side code, you can upload using the signed URL instead of the regular upload endpoint.

<Note>
  If you're using the SDK you can use the `.url()` parameter on any of the upload methods and pass in the signed upload URL there. If you are using the API you can simply make the upload request using the signed URL as the endpoint.
</Note>

<CodeGroup>
  ```typescript SDK {3} theme={null}
  const urlRequest = await fetch("/api/url"); // Fetches the temporary upload URL
  const urlResponse = await urlRequest.json(); // Parse response
  const upload = await pinata.upload.public
    .file(file)
    .url(urlResponse.url); // Upload the file with the signed URL
  ```

  ```typescript API {1-2,13} theme={null}
  const urlRequest = await fetch("/api/url"); // Fetches the temporary upload URL
  const urlResponse = await urlRequest.json(); // Parse response
  async function upload() {
    try {
      const formData = new FormData();

      const file = new File(["hello"], "Testing.txt", { type: "text/plain" });

      formData.append("file", file);

      formData.append("network", "public")

      const request = await fetch(urlResponse.url, {
        method: "POST",
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

<Tip>
  For more information on client side uploads check out our [Presigned URLs Guide](/files/presigned-urls)
</Tip>

### Upload Progress

If you happen to use the API as well as local files you can also track the progress of the upload using a library like `got`. Better support for upload progress will come in later versions of the SDK!

```typescript theme={null}
import fs from "fs";
import FormData from "form-data";
import got from "got";

async function upload() {
  const url = `https://uploads.pinata.cloud/v3/files`;
  try {
    let data = new FormData();
    data.append(`file`, fs.createReadStream("path/to/file"));
    const response = await got(url, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${process.env.PINATA_JWT}`,
      },
      body: data,
    }).on("uploadProgress", (progress) => {
      console.log(progress);
    });
    console.log(JSON.parse(response.body));
  } catch (error) {
    console.log(error);
  }
}
```

If your file is larger than 100MB then a better approach is to follow the [Resumable Upload Guide](#resumable-uploads)

## Common File Recipes

Below are some common recipes for uploading a file.

### Blob

Usually you can pass a Blob directly into the request but to help guarantee success we recommend passing it into a `File` object.

<CodeGroup>
  ```typescript SDK {8-10} theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const text = "Hello World!";
  const blob = new Blob([text]);
  const file = new File([blob], "hello.txt", { type: "text/plain" });
  const upload = await pinata.upload.public.file(file);
  ```

  ```typescript API {7-9} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

      const text = "Hello World!";
      const blob = new Blob([text]);
      const file = new File([blob], "Testing.txt", { type: "text/plain" });

      formData.append("file", file);

      formData.append("network", "public");

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### JSON

Pinata makes it easy to upload JSON objects using the [json](/sdk/upload/public/json) method.

<CodeGroup>
  ```typescript SDK {8-15} theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const upload = await pinata.upload.public.json({
    id: 2,
    name: "Bob Smith",
    email: "bob.smith@example.com",
    age: 34,
    isActive: false,
    roles: ["user"],
  });
  ```

  ```typescript API {7-16} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

      const json = JSON.stringify({
        id: 2,
        name: "Bob Smith",
        email: "bob.smith@example.com",
        age: 34,
        isActive: false,
        roles: ["user"],
      })
      const blob = new Blob([json]);
      const file = new File([blob], "bob.json", { type: "application/json" });

      formData.append("file", file);

      formData.append("network", "public");

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### Local Files

If you need to upload files from a local file source you can use `fs` to feed a file into a `blob`, then turn that `blob` into a `File`. Due to the buffer limit in Node.js you may have issues going beyond 2GB with this approach. Using [Resumable Uploads](#resumable-uploads) with a client side file picker will help increase this.

<Note>
  Support for file streams will be coming in a later version of the SDK.
</Note>

<CodeGroup>
  ```typescript SDK {10-11} theme={null}
  const { PinataSDK } = require("pinata");
  const fs = require("fs");
  const { Blob } = require("buffer");

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const blob = new Blob([fs.readFileSync("./hello-world.txt")]);
  const file = new File([blob], "hello-world.txt", { type: "text/plain" });
  const upload = await pinata.upload.public.file(file);
  ```

  ```typescript API {9} theme={null}
  const JWT = "YOUR_PINATA_JWT";
  const fs = require("fs");
  const { Blob } = require("buffer");

  async function upload() {
    try {
      const formData = new FormData();

      formData.append("file", fs.createReadStream("./hello-world.txt"));

      formData.append("network", "public")

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### Folders

The SDK can accept an array of files using the [fileArray](/sdk/upload/public/file-array) method. Folders can also be uploaded via the API by creating an array of files and mapping over them to add them to the form data. This is different then having a single `file` entry and having multiple files for that one entry, which does not work.

<Warning>
  Folder uploads are currently only supported on Public IPFS
</Warning>

<CodeGroup>
  ```typescript SDK theme={null}
  import { PinataSDK } from "pinata-web3";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const file1 = new File(["hello world!"], "hello.txt", { type: "text/plain" })
  const file2 = new File(["hello world again!"], "hello2.txt", { type: "text/plain" })
  const upload = await pinata.upload.public.fileArray([file1, file2])
  ```

  ```javascript Node.js theme={null}
  import fs from "fs"
  import FormData from "form-data"
  import rfs from "recursive-fs"
  import basePathConverter from "base-path-converter"
  import got from 'got'

  const pinDirectoryToPinata = async () => {
    const url = `https://api.pinata.cloud/pinning/pinFileToIPFS`;
    const src = "PATH_TO_FOLDER";
    var status = 0;
    try {

      const { dirs, files } = await rfs.read(src);

      let data = new FormData();

      for (const file of files) {
        data.append(`file`, fs.createReadStream(file), {
          filepath: basePathConverter(src, file),
        });
      }

      const response = await got(url, {
        method: 'POST',
        headers: {
          "Authorization": "Bearer PINATA_API_JWT"
        },
        body: data
    })
  		.on('uploadProgress', progress => {
  			console.log(progress);
  		});

  	console.log(JSON.parse(response.body));
    } catch (error) {
      console.log(error);
    }
  };

  pinDirectoryToPinata()
  ```

  ```javascript React theme={null}
  import { useState } from "react";
  import { pinata } from "./utils/config"

  function App() {
    const [selectedFiles, setSelectedFiles] = useState<File[]>();

    const changeHandler = (event: React.ChangeEvent<HTMLInputElement>) => {
      setSelectedFiles(event.target?.files);
    };

    const handleSubmission = async () => {
      try {
        const upload = await pinata.upload.public.fileArray(selectedFiles)
        console.log(upload);
      } catch (error) {
        console.log(error);
      }
    };

    return (
      <>
        <label className="form-label"> Choose File</label>
        <input
          directory=""
          webkitdirectory=""
          type="file"
          onChange={changeHandler}
        />
        <button onClick={handleSubmission}>Submit</button>
      </>
    );
  }

  export default App;
  ```

  ```javascript Javascript theme={null}
  import FormData from "form-data"

  const pinDirectoryToIPFS = async () => {
    try {
      const folder = "json";
      const json1 = { hello: "world" };
      const json2 = { hello: "world2" };
      const blob1 = new Blob([JSON.stringify(json1, null, 2)], {
        type: "application/json",
      });
      const blob2 = new Blob([JSON.stringify(json2, null, 2)], {
        type: "application/json",
      });

      const files = [
        new File([blob1], "hello.json", { type: "application/json" }),
        new File([blob2], "hello2.json", { type: "application/json" }),
      ];

      const data = new FormData();

      Array.from(files).forEach((file) => {
        // If you are not using `fs` you might need to specify the folder path along with the filename
        data.append("file", file, `${folder}/${file.name}`);
      });

      const pinataMetadata = JSON.stringify({
        name: `${folder}`,
      });
      data.append("pinataMetadata", pinataMetadata);

      const res = await fetch("https://api.pinata.cloud/pinning/pinFileToIPFS", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${PINATA_JWT}`,
        },
        body: data,
      });
      const resData = await res.json();
      console.log(resData);
    } catch (error) {
      console.log(error);
    }
  };

  pinDirectoryToIPFS();
  ```
</CodeGroup>

<br />

<Info>
  We also have other tools like the [Pinata IPFS CLI](/tools/ipfs-cli) which can be used to upload using [API Keys](/account-managemnet/api-keys)!
</Info>

### URL

To upload a file from an external URL you can stream the contents into an `arrayBuffer`, which then gets passed into a new `Blob` that can then be uploaded to Pinata. This has been abstracted in the SDK using the [url](/sdk/upload/public/url) method.

<CodeGroup>
  ```typescript SDK {8} theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const upload = await pinata.upload.public.url("https://i.imgur.com/u4mGk5b.gif");
  ```

  ```typescript API {7-10} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

      const stream = await fetch("https://i.imgur.com/u4mGk5b.gif")
    	const arrayBuffer = await stream.arrayBuffer();
    	const blob = new Blob([arrayBuffer]);
      const file = new File([blob], "name.gif");

      formData.append("file", file);

      formData.append("network", "public");

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### base64

To upload a file in base64 simply turn the contents into a `buffer` that is passed into a `Blob`. Alternatively you can use the SDK for this as well using the [base64](/sdk/upload/public/base64) method.

<CodeGroup>
  ```typescript SDK {8} theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const upload = await pinata.upload.public.base64("SGVsbG8gV29ybGQh");
  ```

  ```typescript API {7-11} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

     	const buffer = Buffer.from("SGVsbG8gV29ybGQh", "base64");

    	const blob = new Blob([buffer]);

      const file = new File([blob], "hello.txt");

      formData.append("file", file);

      formData.append("network", "public");

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

## Resumable Uploads

The upload endpoint `https://uploads.pinata.cloud/v3/files` is fully [TUS](https://tus.io) compatible, so it can support larger files with the ability to resume uploads. Any file upload larger than 100MB needs to be uploaded through the TUS method, or through the legacy [/pinFileToIPFS](/api-reference/endpoint/ipfs/pin-file-to-ipfs) endpoint. The [SDK](/sdk) handles this automatically when you use `pinata.upload.<network>.file()` by checking the file size before uploading.

<Warning>
  At this time folder uploads must go through [/pinFileToIPFS](/api-reference/endpoint/ipfs/pin-file-to-ipfs). Read the [Folder Guide](#folders) for more info!
</Warning>

```typescript {6} theme={null}
const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const upload = await pinata.upload.public.file(massiveFile);
```

If you want to take advantage of resumable uploads then we would recommend using one of the [TUS clients](https://tus.io/implementations) and taking note of the following:

* Upload chunk size must be smaller than 50MB
* Instead of using the form data fields for `group_id` or `keyvalues` these can be passed directly into the upload metadata (see example below)
* Headers must include the Authorization with your [Pinata JWT](/account-managemnet/api-keys)

Here is an example of an upload to Pinata using the `tus-js-client`

```typescript tus-js-client [expandable] theme={null}
import * as tus from "tus-js-client";

async function resumeUpload(file) {
  try {
    const upload = new tus.Upload(file, {
      endpoint: "https://uploads.pinata.cloud/v3/files",
      chunkSize: 50 * 1024 * 1024, // 50MiB chunk size
      retryDelays: [0, 3000, 5000, 10000, 20000],
      onUploadUrlAvailable: async function () {
        if (upload.url) {
          console.log("Upload URL is available! URL: ", upload.url);
        }
      },
      metadata: {
        filename: "candyroad-demo.mp4", // name
        filetype: "video/mp4",
        group_id: "0192868e-6144-7685-9fc5-af68a1e48f29", // group ID
        network: "public",
        keyvalues: JSON.stringifiy({ env: "prod" }), // keyvalues
      },
      headers: { Authorization: `Bearer ${process.env.PINATA_JWT}` }, // auth header
      uploadSize: fileStats.size,
      onError: function (error) {
        console.log("Failed because: " + error);
      },
      onProgress: function (bytesUploaded, bytesTotal) {
        const percentage = ((bytesUploaded / bytesTotal) * 100).toFixed(2);
        console.log(percentage + "%");
      },
      onSuccess: function () {
        console.log("Upload completed!");
      },
    });

    upload.start();
  } catch (error) {
    console.log(error);
  }
}
```

## Upload by CAR File

You can upload content to Pinata using a raw CAR file. A **CAR (Content Addressed Archive)** file bundles together IPFS blocks in a portable format.

To upload a CAR file, set the `car` parameter to **true** in your upload request. CAR file uploads are supported across all Pinata upload methods.

<CodeGroup>
  ```typescript SDK {4} theme={null}
  const upload = await pinata.upload.public
    .file(file)
    .name("test.car")
    .car()
  ```

  ```typescript API {15} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function upload() {
    try {
      const formData = new FormData();

      const file = new File(["test_car"], "test.car", { type: "application/vnd.ipld.car" });

      formData.append("file", file);

      formData.append("network", "public");

      formData.append("name", "test.car");

      formData.append("car", "true");

      const request = await fetch("https://uploads.pinata.cloud/v3/files", {
        method: "POST",
        headers: {
          Authorization: `Bearer ${JWT}`,
        },
        body: formData,
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

Requirements

* Paid plan required - CAR uploads are not available on free plans
* Public network only - CAR files cannot be uploaded as private content
* Valid structure - Files must be properly formatted CAR files with valid IPFS blocks
* Single Root CID - Pinata does not support CAR files with multiple root CIDs

File Availability

CAR file processing is **asynchronous**. After a successful upload, Pinata validates the CAR file structure and IPFS blocks before preparing the file for indexing. A webhook notification is then sent to report the outcome, indicating whether the CAR file was successfully imported or if the process failed.

## Pin by CID

Another way you can upload content to Pinata is by transferring content that is already on IPFS. This could be CIDs that are on your own local IPFS node or another IPFS pinning service! You can do this with the “Import from IPFS” button in the web app, like so:

<img />

Or you can pin by CID with the SDK using the [cid](/sdk/upload/public/cid) method.

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const pin = await pinata.upload.public.cid("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
```

This will result in a `request_id` and Pinata will start looking for the file. Progress can be checked by using the [queue](/sdk/files/public/queue) method.

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const jobs = await pinata.files.public.queue().status("prechecking")
```

All possible filters are included in the API reference below, but these are the possible "status" filters:

<ParamField type="string">
  Filter by the status of the job in the pinning queue (see potential statuses
  below)

  * `prechecking` Pinata is running preliminary validations on your pin request.
  * `searching` Pinata is actively searching for your content on the IPFS network. This may take some time if your content is isolated.
  * `retrieving` Pinata has located your content and is now in the process of retrieving it.
  * `expired` Pinata wasn't able to find your content after a day of searching the IPFS network. Please make sure your content is hosted on the IPFS network before trying to pin again.
  * `backfilled` Pinata can only search 250 files at a time per account, so if you have more than 250 items in your queue then the extra items will sit in a backfilled status. Once the queue goes down it will automatically start working on the next items in the backfill queue.
  * `over_free_limit` Pinning this object would put you over the free tier limit. Please add a credit card to continue pinning content.
  * `over_max_size` This object is too large of an item to pin. If you're seeing this, please contact us for a more custom solution.
  * `invalid_object` The object you're attempting to pin isn't readable by IPFS nodes. Please contact us if you receive this, as we'd like to better understand what you're attempting to pin.
  * `bad_host_node` You provided a host node that was either invalid or unreachable. Please make sure all provided host nodes are online and reachable.
</ParamField>

## Predetermining the CID

If you find yourself in a position where you want to pre-determine the CID before uploading you can use a combination of the `ipfs-unixfx-importer` and `blockstore-core` libraries.

```typescript theme={null}
import { importer } from "ipfs-unixfs-importer";
import { MemoryBlockstore } from "blockstore-core/memory";

export const predictCID = async (file: File, version: 0 | 1 = 1) => {
    try {
        const arrayBuffer = await file.arrayBuffer();
        const buffer = Buffer.from(arrayBuffer);
        const blockstore = new MemoryBlockstore();

        let rootCid: any;

        for await (const result of importer([{ content: buffer }], blockstore, {
            cidVersion: version,
            hashAlg: "sha2-256",
            rawLeaves: version === 1,
        })) {
            rootCid = result.cid;
        }

        return rootCid.toString();
    } catch (err) {
        return err;
    }
};
```

Usage will just require passing in a file object and the version of the CID you want to predict. Here is an example using a local file.

```typescript theme={null}
import fs from "fs"

const file = new File([fs.readFileSync("path/to-file")], "filename.extension");
const cid = await predictCID(file, 1);
console.log(cid);
```

## Peering with Pinata

If you run IPFS infrastructure and would like to peer with Pinata's nodes you can do so with the [Kubo](https://docs.ipfs.tech/reference/kubo/cli/) commands listed below. Rather than using full multiaddresses for our node IDs we use a DNS setup that is more stable and allows our infrastructure to be flexible.

```bash theme={null}
ipfs swarm connect /dnsaddr/bitswap.pinata.cloud
```

```bash theme={null}
ipfs config --json Peering.Peers '[{ "ID": "Qma8ddFEQWEU8ijWvdxXm3nxU7oHsRtCykAaVz8WUYhiKn", "Addrs": ["/dnsaddr/bitswap.pinata.cloud"] }]'
```

If you have any issues feel free to [reach out](mailto:team@pinata.cloud)!

## Web App

You can also use the **[Pinata App](https://app.pinata.cloud/)** to upload files. It’s as simple as clicking the “Add” button in the top right corner of the **[files page](https://app.pinata.cloud/ipfs/files)**. Select your file, give it a name, then upload. Once it's complete you’ll see it listed in the files page.

<img />

Start uploading by [signing up for a free account](https://app.pinata.cloud/register)!


# File Vectors (Beta)
Source: https://docs.pinata.cloud/files/vectors



<Warning>
  The file vectors feature is still in beta and is only available on Private IPFS. Please contact the team at <a href="mailto:team@pinata.cloud">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

## Overview

A common nusance when building AI apps is context embeddings. If you use a traditional stack you generall have to store an embedding, vectorize it, store the vector, then when you query a vector you'll get another reference to the file which you then have to fetch again. Pinata's solution is much more elegant. With Pinata's file vectoring you can upload a file and vector it at the same time.

```typescript theme={null}
const upload = await pinata.upload.private
  .file(file)
  .group("GROUP_ID")
  .vectorize()
```

When it comes time to query a vector, you have the option to either list your query results and judge the matching score, or just return the highest scoring file itself.

```typescript theme={null}
const { data, contentType } = await pinata.files.private
  .queryVectors({
    groupId: "GROUP_ID",
    query: "Hello World!",
    returnFile: true
  })
```

This enables develops to build AI applications faster and with less code!

### Pinata Vector Storage: Public Beta Limits

During the public beta, Pinata Vector Storage has the following limits:

* File Vectorization Limit: You can vectorize up to 10,000 files.
* Index Limit: You can create a maximum of 5 indexes, managed using Pinata Groups.
* Results Limit: You can query a vector and get a max of 20 files returned in one request.

**What this means**

You can organize your vector embeddings into up to 5 searchable indexes using Pinata Groups. Across all these groups, you can store a total of 10,000 vector embeddings corresponding to files stored on Pinata.

## Vectorizing Files

There are two ways you can vectorize file uploads, and with both options **files must be part of a group** in order for vectors and queries to work.

### Vectorize on Upload

If you use the [Files SDK](/sdk/getting-started) you can vectorize a file on upload.

```typescript {4} theme={null}
const upload = await pinata.upload.private
  .file(file)
  .group("GROUP_ID")
  .vectorize()
```

### Vectorize After Upload

If you already have a file that's been uploaded and it's [part of a group](/files/file-groups) then you can vectorize it.

```typescript theme={null}
const update = await pinata.files.private.vectorize("FILE_ID")
```

## Querying Vectors

After a file has been vectorized and it's part of a group, you can query vectors for a given group.

```typescript theme={null}
const results = await pinata.files.private.queryVectors({
  groupId: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  query: "Hello World"
})
```

This will return the following type:

```typescript theme={null}
type VectorizeQueryResponse = {
	count: number;
	matches: VectorQueryMatch[];
};

type VectorQueryMatch = {
	file_id: string;
	cid: string;
	score: number;
};
```

### Returning the Top Match File

A unique feature in the SDK is if you pass in the `returnFile` flag then you will get the file and it's contents rather than just the reference to the file.

```typescript {4} theme={null}
const { data, contentType }  = await pinata.files.private.queryVectors({
  groupId: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  query: "Hello World",
  returnFile: true
})
```

## Deleting Vectors

If at any point you need to delete vectors for a file you can do so with the `deleteVectors` method in the SDK.

```typescript theme={null}
const update = await pinata.files.private.deleteVectors("FILE_ID")
```


# Introduction
Source: https://docs.pinata.cloud/files/x402/intro



<Note>
  x402 is available on paid Pinata accounts. [Upgrade your account](https://app.pinata.cloud/billing) to access x402 monetization features.
</Note>

Pinata's x402 enables you to monetize your private IPFS files by receiving USDC payments directly to your wallet. You set the price, you receive the payment.

## Overview

Pinata's x402 implementation enables:

* **Monetization of private IPFS content** using Payment Instructions
* **You receive payments directly** to your wallet address. Payments go to you.
* **Flexible payment requirements** configurable per file or group of files
* **USDC payments** on Base (mainnet) and Base Sepolia (testnet). USDC is currently the only supported token.
* **Gateway-level enforcement** through the x402 protocol

## Network Configuration

| Network                | USDC Token Address                           | Use Case                |
| ---------------------- | -------------------------------------------- | ----------------------- |
| Base (Mainnet)         | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` | Production monetization |
| Base Sepolia (Testnet) | `0x036CbD53842c5426634e7929541eC2318f3dCF7e` | Testing payment flows   |

## How It Works

1. **Upload** a private file to Pinata IPFS
2. **Create** a Payment Instruction with your desired payment requirements
3. **Attach** the CID of your private file to the Payment Instruction
4. **Share** your x402 gateway URL: `https://your-gateway.mypinata.cloud/x402/cid/{cid}`
5. **Requesters** make USDC payments through your gateway to access content

<Note>
  You must use your own dedicated Pinata gateway domain. Replace `your-gateway.mypinata.cloud` with your actual gateway domain throughout these examples.
</Note>

## Example Workflow

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "your-gateway.mypinata.cloud",
});

// 1. Upload a private file
const file = new File(["premium content"], "content.pdf", { type: "application/pdf" });
const upload = await pinata.upload.private.file(file);

// 2. Create a payment instruction
const instruction = await pinata.x402.createPaymentInstruction({
  name: "Premium Content",
  payment_requirements: [
    {
      asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
      pay_to: "0xYourWalletAddress", // YOU receive payments here
      network: "base",
      description: "Access fee",
      amount: "10000", // $0.01 in USDC
    },
  ],
});

// 3. Attach CID to payment instruction
await pinata.x402.addCid(instruction.data.id, upload.cid);

// 4. Share the x402 gateway URL
// https://your-gateway.mypinata.cloud/x402/cid/{cid}
```

## Why Use Payment Instructions

Payment Instructions enable you to monetize your private content by setting custom payment requirements and receiving payments directly to your wallet.

Key benefits:

* **You get paid** for your content. Set your own prices and receive USDC payments directly.
* **Flexible pricing** for different files or groups of files
* **Reusable payment instructions** that can be attached to multiple CIDs
* **Full control** over payment requirements, pricing, and access

## SDK Reference

<CardGroup>
  <Card title="x402 Overview" icon="sparkle" href="/sdk/x402/index">
    Get started with x402 monetization
  </Card>

  <Card title="Payment Instructions" icon="code" href="/sdk/x402/payment-instructions/list">
    Create and manage payment instructions
  </Card>

  <Card title="CID Management" icon="link" href="/sdk/x402/cids/list">
    Attach CIDs to payment instructions
  </Card>

  <Card title="Types" icon="brackets-curly" href="/sdk/types/x402">
    TypeScript type definitions
  </Card>
</CardGroup>

## API Reference

For direct API access, see the [x402 API documentation](/api-reference/endpoint/x402/payment-instructions-list).


# Accessing Paid Content
Source: https://docs.pinata.cloud/files/x402/x402-accessing-paid-content



Learn how to access x402-protected content on Pinata.

## Overview

When attempting to access x402-protected content without a payment payload, the gateway returns payment requirements. After making a payment, requesters receive a payment proof that grants access to the content.

## The Payment Flow

<Note>
  The content creator provides their dedicated Pinata gateway URL. Replace `your-gateway.mypinata.cloud` in examples with the actual gateway domain provided.
</Note>

### Step 1: Request the Content

Make a GET request to the x402 gateway URL:

```bash theme={null}
curl https://your-gateway.mypinata.cloud/x402/cid/bafkreih...
```

### Step 2: Receive Payment Requirements (402 Response)

The gateway returns HTTP 402 with payment details:

```json theme={null}
{
  "x402Version": 1,
  "accepts": [
    {
      "scheme": "exact",
      "network": "base",
      "maxAmountRequired": "10000",
      "resource": "https://your-gateway.mypinata.cloud/x402/cid/bafkreih...",
      "description": "Access fee",
      "mimeType": "application/json",
      "payTo": "0x6135561038E7C676473431842e586C8248276AED",
      "maxTimeoutSeconds": 60,
      "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
      "extra": {
        "name": "USD Coin",
        "version": "2"
      }
    }
  ],
  "error": "Provide a valid X-Payment header to access this content"
}
```

**Key Fields:**

* `network`: Blockchain network (e.g., `base`)
* `asset`: Token contract address (USDC on Base)
* `payTo`: Recipient wallet address (content creator receives payment here)
* `maxAmountRequired`: Payment amount in smallest unit (e.g., `10000` = 0.01 USDC)

### Step 3: Access Content with Payment Proof

After successful payment, include the `X-Payment` header in the request:

```bash theme={null}
curl https://your-gateway.mypinata.cloud/x402/cid/bafkreih... \
  -H "X-Payment: eyJ4NDAyVmVyc2lvbiI6MSwic2NoZW1lIjoiZXhhY3QiLCJuZXR3b3..."
```

The gateway will:

1. Validate the `X-Payment` header
2. Verify the payment proof
3. Check that amount, recipient, and network match
4. Serve the private content

**Successful Response:**

```
HTTP/200 OK
Content-Type: application/json

{
  "your": "content"
}
```

## Using x402 Libraries

The x402 protocol has client libraries that automate the payment flow. First, set up your wallet:

## Setting Up Your Wallet

The x402 libraries require a Viem account or Coinbase Developer Platform wallet:

### Option 1: Viem Local Account

```typescript theme={null}
import { privateKeyToAccount } from "viem/accounts";

const account = privateKeyToAccount("0xYOUR_PRIVATE_KEY");
```

### Option 2: Coinbase CDP Wallet

```typescript theme={null}
import { Coinbase, Wallet } from "@coinbase/coinbase-sdk";

const coinbase = new Coinbase({
  apiKeyName: "YOUR_API_KEY_NAME",
  privateKey: "YOUR_PRIVATE_KEY",
});

const wallet = await Wallet.create();
const account = await wallet.getDefaultAddress();
```

## Using the Libraries

Once you have your wallet set up, use the x402 libraries to access paid content:

### @x402/fetch

```typescript theme={null}
import { wrapFetchWithPayment } from "@x402/fetch";
import { privateKeyToAccount } from "viem/accounts";

// Set up your wallet
const account = privateKeyToAccount("0xYOUR_PRIVATE_KEY");
const fetchWithPayment = wrapFetchWithPayment(fetch, account);

// Automatically handles 402 response and payment
const response = await fetchWithPayment(
  "https://your-gateway.mypinata.cloud/x402/cid/bafkreih..."
);

const content = await response.json();
console.log(content);
```

### @x402/axios

```typescript theme={null}
import { wrapAxiosWithPayment } from "@x402/axios";
import axios from "axios";
import { privateKeyToAccount } from "viem/accounts";

// Set up your wallet
const account = privateKeyToAccount("0xYOUR_PRIVATE_KEY");
const axiosWithPayment = wrapAxiosWithPayment(axios, account);

// Automatically handles 402 response and payment
const response = await axiosWithPayment.get(
  "https://your-gateway.mypinata.cloud/x402/cid/bafkreih..."
);

console.log(response.data);
```

## Technical Details (Optional)

<Note>
  Pinata uses Coinbase Facilitator to process x402 payments, which provides access to Coinbase's Discovery Bazaar network for broader content discovery.
</Note>

## Understanding Payment Amounts

USDC uses 6 decimals, so amounts use the token's smallest unit:

| USD Amount | `maxAmountRequired` | Calculation         |
| ---------- | ------------------- | ------------------- |
| \$0.01     | `10000`             | \$0.01 × 1,000,000  |
| \$0.10     | `100000`            | \$0.10 × 1,000,000  |
| \$1.00     | `1000000`           | \$1.00 × 1,000,000  |
| \$10.00    | `10000000`          | \$10.00 × 1,000,000 |

**Formula:** USD Amount × 1,000,000 = token amount

## Error Handling

### 402 Payment Required

Payment has not been made yet. Follow the payment flow above.

### 403 Forbidden

Payment proof is invalid or expired. Make a new payment.

### 404 Not Found

The CID doesn't exist or isn't attached to a payment instruction.

### 500 Internal Server Error

Gateway or facilitator error. Contact the content creator.

## Network Support

**USDC is currently the only supported token.**

| Network                | Status      | Token                                               | Use Case   |
| ---------------------- | ----------- | --------------------------------------------------- | ---------- |
| Base (Mainnet)         | ✅ Available | USDC (`0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`) | Production |
| Base Sepolia (Testnet) | ✅ Available | USDC (`0x036CbD53842c5426634e7929541eC2318f3dCF7e`) | Testing    |

## Best Practices

1. **Handle 402 responses gracefully**: Display payment requirements clearly
2. **Use the x402 libraries**: They handle the complex payment flow automatically
3. **Test on Base Sepolia first**: Verify integration before using mainnet
4. **Store payment proofs**: If accessing content multiple times (check expiry)
5. **Monitor USDC balance**: Ensure sufficient funds for payments

## Example: Complete Integration

```typescript theme={null}
import { wrapFetchWithPayment } from "@x402/fetch";
import { privateKeyToAccount } from "viem/accounts";

// Set up your wallet
const account = privateKeyToAccount(process.env.PRIVATE_KEY);
const fetchWithPayment = wrapFetchWithPayment(fetch, account);

// Access paid content
async function accessPaidContent(cid: string) {
  try {
    const url = `https://your-gateway.mypinata.cloud/x402/cid/${cid}`;

    const response = await fetchWithPayment(url);

    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }

    const content = await response.json();
    console.log("Content accessed successfully:", content);

    return content;
  } catch (error) {
    console.error("Failed to access content:", error);
    throw error;
  }
}

// Usage
accessPaidContent("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4");
```

## Resources

* [@x402/fetch NPM Package](https://www.npmjs.com/package/@x402/fetch)
* [@x402/axios NPM Package](https://www.npmjs.com/package/@x402/axios)
* [Viem Documentation](https://viem.sh)
* [Coinbase Developer Platform](https://docs.cdp.coinbase.com/)

## Support

Need help accessing paid content? Contact the content creator or reach out to [team@pinata.cloud](mailto:team@pinata.cloud).


# Payment Instructions Guide
Source: https://docs.pinata.cloud/files/x402/x402-payment-instructions



Payment Instructions are the core mechanism for monetizing private IPFS content through the x402 protocol. You define payment requirements, attach them to your private files, and receive payments directly to your wallet when requesters access your content.

This guide covers how to create, manage, and use Payment Instructions to monetize your content.

## Prerequisites

* Paid Pinata account
* [Pinata SDK](/sdk/getting-started) installed
* Private files uploaded to Pinata IPFS

## Understanding Payment Instructions

A Payment Instruction is a reusable configuration that defines:

* **Payment requirements** - The amount, token, and recipient for payments
* **Network configuration** - Which blockchain network to use
* **Metadata** - Name and description for organization

<Note>
  The `payment_requirements` field is an array, allowing you to define multiple payment options. Each payment instruction can have multiple requirements, giving requesters flexibility in how they pay.
</Note>

### Payment Instruction Structure

```typescript theme={null}
type PaymentInstruction = {
  id: string;
  version: number;
  payment_requirements: PaymentRequirement[];
  name: string;
  description?: string;
  created_at: string;
};

type PaymentRequirement = {
  asset: string;           // USDC token contract address
  pay_to: string;          // Your wallet address
  network: "base" | "base-sepolia" | "eip155:8453" | "eip155:84532";
  amount: string;          // Amount in USDC smallest units
  description?: string;
};
```

<Note>
  The `version` field is automatically managed by Pinata and increments with each update. You don't need to set this field when creating or updating payment instructions.
</Note>

## Networks and Tokens

Currently supported configurations. **USDC is the only supported token at this time.**

### Base Mainnet (Production)

* **Network**: `base` (or `eip155:8453`)
* **USDC Token Address**: `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`
* **Use for**: Production monetization

### Base Sepolia (Testing)

* **Network**: `base-sepolia` (or `eip155:84532`)
* **USDC Token Address**: `0x036CbD53842c5426634e7929541eC2318f3dCF7e`
* **Use for**: Testing payment flows

## Complete Workflow

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "your-gateway.mypinata.cloud",
});
```

### Step 1: Upload Private Content

First, upload your file as private to Pinata:

```typescript theme={null}
const file = new File(["file contents"], "premium-content.pdf", {
  type: "application/pdf",
});
const upload = await pinata.upload.private.file(file);
const cid = upload.cid;
```

**Important:** The file must be uploaded to the `private` network to be monetized with x402.

### Step 2: Create Payment Instruction

Create a payment instruction with your desired requirements:

```typescript theme={null}
const instruction = await pinata.x402.createPaymentInstruction({
  name: "Premium PDF Access",
  description: "One-time payment for PDF access",
  payment_requirements: [
    {
      asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", // USDC on Base
      pay_to: "0x6135561038E7C676473431842e586C8248276AED", // YOU receive payments here
      network: "base",
      description: "Access fee",
      amount: "10000", // $0.01 in USDC
    },
  ],
});
const instructionId = instruction.data.id;
```

### Step 3: Attach CID to Payment Instruction

Link your private file to the payment instruction:

```typescript theme={null}
await pinata.x402.addCid(instructionId, cid);
```

### Step 4: Share x402 Gateway URL

Your content is now monetized and accessible at:

```
https://your-gateway.mypinata.cloud/x402/cid/{cid}
```

## Managing Payment Instructions

### Listing Instructions

View all your payment instructions with pagination:

```typescript theme={null}
const instructions = await pinata.x402.listPaymentInstructions({ limit: 20 });
```

Filter by specific criteria:

```typescript theme={null}
// Find instruction for a specific CID
const byCid = await pinata.x402.listPaymentInstructions({ cid: "bafkreih..." });

// Filter by name
const byName = await pinata.x402.listPaymentInstructions({ name: "Premium" });

// Get specific instruction by ID
const byId = await pinata.x402.listPaymentInstructions({ id: "019a2b6a..." });
```

### Getting a Single Instruction

```typescript theme={null}
const instruction = await pinata.x402.getPaymentInstruction(instructionId);
```

### Updating Instructions

Modify payment requirements for all attached CIDs:

```typescript theme={null}
const updated = await pinata.x402.updatePaymentInstruction(instructionId, {
  payment_requirements: [
    {
      asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
      pay_to: "0x6135561038E7C676473431842e586C8248276AED",
      network: "base",
      amount: "50000", // Updated to $0.05
    },
  ],
});
```

### Deleting Instructions

Before deleting, remove all CID attachments:

```typescript theme={null}
// 1. List attached CIDs
const { data: cidData } = await pinata.x402.listCids(instructionId);

// 2. Remove each CID
for (const cid of cidData.cids) {
  await pinata.x402.removeCid(instructionId, cid);
}

// 3. Delete the instruction
await pinata.x402.deletePaymentInstruction(instructionId);
```

## CID Management

### CID and Payment Instruction Relationship

* **One Payment Instruction → Multiple CIDs**: A single payment instruction can be attached to multiple CIDs
* **One CID → One Payment Instruction**: Each CID can only have one payment instruction at a time
* **Multiple Requirements**: A payment instruction can have multiple payment requirements in its `payment_requirements` array
* Updating the instruction affects all attached CIDs

### Managing CID Attachments

```typescript theme={null}
// List all CIDs for an instruction
const cids = await pinata.x402.listCids(instructionId);

// Add a CID
await pinata.x402.addCid(instructionId, cid);

// Remove a CID
await pinata.x402.removeCid(instructionId, cid);
```

## Gateway Behavior

When a requester accesses your x402 gateway URL without payment, the gateway returns payment requirements:

### Without Payment (402 Response)

```json theme={null}
{
  "x402Version": 1,
  "accepts": [
    {
      "scheme": "exact",
      "network": "base",
      "maxAmountRequired": "10000",
      "resource": "https://gateway/x402/cid/bafkreig...",
      "payTo": "0x6135561038E7C676473431842e586C8248276AED",
      "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
      "extra": {
        "name": "USD Coin",
        "version": "2"
      }
    }
  ],
  "error": "Provide a valid X-Payment header to access this content"
}
```

### With Valid Payment

The gateway:

1. Validates the `X-Payment` header
2. Verifies the payment proof
3. Checks amount, recipient, and network match requirements
4. Serves the private content

## Best Practices

### Payment Amounts

The `amount` uses USDC's smallest unit. USDC has 6 decimals, so to convert USD to the token amount, multiply by 1,000,000:

| USD Amount | `amount`     | Calculation         |
| ---------- | ------------ | ------------------- |
| \$0.01     | `"10000"`    | \$0.01 × 1,000,000  |
| \$0.10     | `"100000"`   | \$0.10 × 1,000,000  |
| \$1.00     | `"1000000"`  | \$1.00 × 1,000,000  |
| \$5.00     | `"5000000"`  | \$5.00 × 1,000,000  |
| \$10.00    | `"10000000"` | \$10.00 × 1,000,000 |

**Formula:** USD Amount × 1,000,000 = token amount

**Tips:**

* Consider transaction costs when setting minimum amounts
* Test on Base Sepolia before deploying to mainnet

### Instruction Organization

* Use descriptive names for easy management
* Group similar content under one instruction
* Document your payment requirements clearly

### Security Considerations

* Only private files can be monetized
* Ensure your `pay_to` address is correct. **You receive payments directly to this address.**
* Test payment flows on testnet first
* Monitor your gateway analytics

## Troubleshooting

### Common Issues

**409 Conflict when deleting instruction**

* Solution: Remove all CID attachments first

**400 Bad Request when creating instruction**

* Check `asset` and `pay_to` addresses start with `0x`
* Verify `network` is `base`, `base-sepolia`, `eip155:8453`, or `eip155:84532`
* Ensure `amount` is provided

**404 Not Found when accessing CID**

* Verify the CID exists and is private
* Check the CID is attached to a payment instruction
* Ensure the gateway URL format is correct

## SDK Reference

* [List Payment Instructions](/sdk/x402/payment-instructions/list)
* [Create Payment Instruction](/sdk/x402/payment-instructions/create)
* [Get Payment Instruction](/sdk/x402/payment-instructions/get)
* [Update Payment Instruction](/sdk/x402/payment-instructions/update)
* [Delete Payment Instruction](/sdk/x402/payment-instructions/delete)
* [List CIDs](/sdk/x402/cids/list)
* [Add CID](/sdk/x402/cids/add)
* [Remove CID](/sdk/x402/cids/remove)

## API Reference

For direct API access, see the [x402 API documentation](/api-reference/endpoint/x402/payment-instructions-list).


# Quick Start
Source: https://docs.pinata.cloud/files/x402/x402-quick-start



Get started monetizing your private IPFS files with x402 in just a few minutes.

With x402, you monetize your private files by setting payment requirements. Payments go directly to your wallet. You control the price and receive the funds.

<Note>
  x402 is available on paid Pinata accounts. [Upgrade your account](https://app.pinata.cloud/billing) to access x402 monetization features.
</Note>

## Prerequisites

* Paid Pinata account
* [Pinata SDK](/sdk/getting-started) installed
* Ethereum wallet address to receive payments

## Step 1: Upload a Private File

First, upload a file to Private IPFS:

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "your-gateway.mypinata.cloud",
});

const file = new File(["file contents"], "your-file.pdf", {
  type: "application/pdf",
});
const upload = await pinata.upload.private.file(file);
const cid = upload.cid;
```

Save the returned `cid` for the next step.

## Step 2: Create a Payment Instruction

Define your payment requirements:

```typescript theme={null}
const instruction = await pinata.x402.createPaymentInstruction({
  name: "Premium Content Access",
  description: "One-time payment for file access",
  payment_requirements: [
    {
      asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", // USDC on Base
      pay_to: "YOUR_WALLET_ADDRESS", // YOU receive payments here
      network: "base",
      description: "Access fee",
      amount: "10000", // $0.01 in USDC
    },
  ],
});
const instructionId = instruction.data.id;
```

**Understanding Payment Amounts:** The `amount` uses USDC's smallest unit. USDC has 6 decimals, so to convert USD to the token amount, multiply by 1,000,000:

| USD Amount | `amount`     | Calculation         |
| ---------- | ------------ | ------------------- |
| \$0.01     | `"10000"`    | \$0.01 × 1,000,000  |
| \$0.10     | `"100000"`   | \$0.10 × 1,000,000  |
| \$1.00     | `"1000000"`  | \$1.00 × 1,000,000  |
| \$5.00     | `"5000000"`  | \$5.00 × 1,000,000  |
| \$10.00    | `"10000000"` | \$10.00 × 1,000,000 |

**Formula:** USD Amount × 1,000,000 = token amount

**Networks:**

* Production: Use `"base"` (or `"eip155:8453"`) with `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`
* Testing: Use `"base-sepolia"` (or `"eip155:84532"`) with `0x036CbD53842c5426634e7929541eC2318f3dCF7e`

Save the returned `id` for the next step.

## Step 3: Attach CID to Payment Instruction

Link your private file to the payment instruction:

```typescript theme={null}
await pinata.x402.addCid(instructionId, cid);
```

## Step 4: Share Your Monetized Content

Your file is now monetized! Share this URL with requesters:

```
https://your-gateway.mypinata.cloud/x402/cid/{cid}
```

<Note>
  Replace `your-gateway.mypinata.cloud` with your actual dedicated Pinata gateway domain (e.g., `my-gateway.mypinata.cloud`), and `{cid}` with your file's CID.
</Note>

## Step 5: Test the Payment Flow

When a requester accesses your URL without payment, the gateway returns a 402 response with payment requirements:

```typescript theme={null}
const response = await fetch(
  `https://your-gateway.mypinata.cloud/x402/cid/${cid}`
);
const paymentRequirements = await response.json();
console.log(paymentRequirements);
```

Response:

```json theme={null}
{
  "x402Version": 1,
  "accepts": [{
    "scheme": "exact",
    "network": "base",
    "maxAmountRequired": "10000",
    "asset": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    "payTo": "YOUR_WALLET_ADDRESS",
    "resource": "https://your-gateway.mypinata.cloud/x402/cid/{cid}"
  }],
  "error": "Provide a valid X-Payment header to access this content"
}
```

After payment is made, requesters can access the file by including the payment proof in the `X-Payment` header.

## Next Steps

* **Manage Multiple Files**: Attach multiple CIDs to the same payment instruction
* **Update Pricing**: Use [`updatePaymentInstruction`](/sdk/x402/payment-instructions/update)
* **Monitor Access**: Check your gateway analytics to track paid downloads
* **Requester Guide**: Learn how requesters access paid content in the [Accessing Paid Content](/files/x402/x402-accessing-paid-content) guide

## Common Issues

**404 Not Found**: Verify the CID is private and correctly attached to a payment instruction

**403 Forbidden**: Check that your API key has the required permissions

**409 Conflict**: If deleting a payment instruction fails, remove all CID attachments first

Need help? Contact [team@pinata.cloud](mailto:team@pinata.cloud)

## API Reference

For direct API access, see the [x402 API documentation](/api-reference/endpoint/x402/payment-instructions-list).


# x402 Services
Source: https://docs.pinata.cloud/files/x402/x402-services



## Overview

The x402 Services provide streamlined endpoints for crypto-based content monetization using the @x402/axios or @x402/fetch libraries.

## Endpoints

For detailed API specifications, see the API Reference:

<CardGroup>
  <Card title="Upload" icon="upload" href="/api-reference/endpoint/x402/pin">
    Upload files with payment
  </Card>

  <Card title="Retrieve" icon="download" href="/api-reference/endpoint/x402/retrieve">
    Access private files with payment
  </Card>
</CardGroup>

## See Also

For more granular control over payment configurations, see the [Payment Instructions API](/files/x402/x402-payment-instructions), which offers:

* **Flexible pricing** - Define custom payment requirements
* **Separate management** - Configure payments independently from files
* **One-to-many** - Attach one payment instruction to multiple files


# Astro
Source: https://docs.pinata.cloud/frameworks/astro

Get started using Pinata with Astro

This guide will walk you through setting up Pinata with Astro

## Create an API Key and get Gateway URL

To create an API key, visit the [Keys Page](https://app.pinata.cloud/developers/keys) and click the "New Key" button in the top right. Once you do that you can select if you want your key to be admin or if you want to scope the privileges of the keys to certain endpoints or limit the number of uses. Make those selections, then give the key a name at the bottom, and click create key.

<Note>
  If you are just getting started we recommend using Admin privileges, then move
  to scope keys as you better understand your needs
</Note>

<img />

Once you have created the keys you will be shown your API Key Info. This will contain your **Api Key**, **API Secret**, and your **JWT**. Click "Copy All" and save them somewhere safe!

<Note>
  The API keys are only shown once, be sure to copy them somewhere safe!
</Note>

After you have your API key, you will want to get your Gateway domain. When you create a Pinata account, you'll automatically have a Gateway created for you! To see it, simply visit the [Gateways Page](https://app.pinata.cloud/gateway) see it listed there.

<img />

The gateway domains are randomly generated and might look something like this:

```
aquamarine-casual-tarantula-177.mypinata.cloud
```

## Setup Astro

To create a new Astro project go ahead and run this command in the terminal:

```bash theme={null}
npm create astro@latest pinata-astro
```

You can select which options you prefer, but for this exmaple we'll use the following:

```
tmpl   How would you like to start your new project?
       Empty

  ts   Do you plan to write TypeScript?
       Yes

 use   How strict should TypeScript be?
       Strict

deps   Install dependencies?
       Yes

 git   Initialize a new git repository?
       Yes
```

After completing the project setup we can go ahead and `cd` into the repo and install `pinata`.

```bash theme={null}
cd pinata-astro && npm i pinata
```

Since we want to keep our API key private we will need to make sure our code is deployed server side, and we can use several different adapter options which you can view [here](https://docs.astro.build/en/guides/server-side-rendering/). We also need a UI framework to handle our upload form, and there are many to choose from [here](https://docs.astro.build/en/guides/framework-components/). We'll use `vercel` and `svelte` for this tutorial, and you can install them like so.

```bash theme={null}
npx astro add vercel svelte
```

This should install the dependencies and alter the `astro.config.mjs` for us.

## Setup Pinata

In the `src` folder make a new folder called `utils`, and inside there make a file called `pinata.ts` with the following contents:

```typescript src/utils/pinata.ts theme={null}
import { PinataSDK } from "pinata";

export const pinata = new PinataSDK({
	pinataJwt: import.meta.env.PINATA_JWT,
	pinataGateway: import.meta.env.GATEWAY_URL,
});
```

This will create and export an instance of the Files SDK using environment variables, and to set those up make a new file at the root of the project called `.env` with the following values:

```
PINATA_JWT= # The Pinata JWT API key we got earlier
GATEWAY_URL= # The Gateway domain we grabbed earlier, formatting just as we copied it from the app
```

## Create Client Side Form

In the `src` folder make another folder called `components`, then inside there make file called `UploadForm.svelte`.

```html src/components/UploadForm.svelte theme={null}
<script lang="ts">
let url: string;
let isUploading: boolean;

async function submit(e: SubmitEvent) {
	isUploading = true;
	e.preventDefault();
	const formData = new FormData(e.currentTarget as HTMLFormElement);
	const request = await fetch("/api/upload", {
		method: "POST",
		body: formData,
	});
	const response = await request.json();
	url = response.data;
	isUploading = false;
}
</script>

<style>
  img {
    max-width: 500px;
  }
  form {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 2rem;
  }
  button {
   background-color: #6E57FF;
   color: white;
   border: none;
   border-radius: 5px;
   padding: 0.75rem 1.5rem;
   font-weight: bold;
  }
</style>

<form on:submit={submit}>
  <input type="file" id="file" name="file" required />
  <button>{isUploading ? "Uploading..." : "Upload"}</button>
  {#if url}
    <img src={url} alt="pinnie" />
  {/if}
</form>
```

This component creates a `<form>` with a file `<input>` as well as a `<button>` to send it. The form will trigger the `submit` function, which takes our form data and makes an API request to our server side code. Once complete the API will send response with a `url` that we can use in the `<img>` tag to display it on the page.

## Server Side API Route

In the `src/pages` folder make a new folder called `api` and inside there make a file called `upload.ts`. Paste the following code inside it:

```typescript theme={null}
import type { APIRoute } from "astro";
import { pinata } from "../../utils/pinata";

export const POST: APIRoute = async ({ request }) => {
	const data = await request.formData();
	const file = data.get("file") as File;
	if (!file) {
		return new Response(
			JSON.stringify({
				message: "Missing file",
			}),
			{ status: 400 },
		);
	}
	const { cid } = await pinata.upload.public.file(file);
	const url = await pinata.gateways.public.convert(cid)
	return new Response(
		JSON.stringify({
			data: url,
		}),
		{ status: 200 },
	);
};
```

This simple API route will parse the incoming `formData` and get the `file` we attached. If there isn't a file attached we'll send a error response. Otherwise we'll upload the file using the SDK method `pinata.upload.public.file` and deconstruct the response to get the `cid`. With that `cid` we can use the `convert` method to create a URL, which we can then send back to the client.

## Add Component to the Page

The last step here is to update the `src/pages/index.astro` file with our new component!

```html src/pages/index.astro theme={null}
---
import UploadForm from "../components/UploadForm.svelte";
---

<html lang="en">
	<head>
		<meta charset="utf-8" />
		<link rel="icon" type="image/svg+xml" href="/favicon.svg" />
		<meta name="viewport" content="width=device-width" />
		<meta name="generator" content={Astro.generator} />
		<title>Astro</title>
	</head>
	<body>
		<h1>Astro + Pinata</h1>
		<UploadForm client:load />
	</body>
</html>
```


# Hono
Source: https://docs.pinata.cloud/frameworks/hono



[Hono](https://hono.dev) is a lightweight web framework for Deno and Node.js. It is designed to be fast, simple, and easy to use. In this framework guide we'll show you how to create a server that sends [Presigned URLs](/files/presigned-urls) to a client app for a secure client side upload flow. We would highly recommend pairing this guide with the [React framework guide](/frameworks/react)!

## Installation

### Create an API Key and get Gateway URL

To create an API key, visit the [Keys Page](https://app.pinata.cloud/developers/keys) and click the "New Key" button in the top right. Once you do that you can select if you want your key to be admin or if you want to scope the privileges of the keys to certain endpoints or limit the number of uses. Make those selections, then give the key a name at the bottom, and click create key.

<img />

Once you have created the keys, you will be shown your API Key Info. This will contain your **Api Key**, **API Secret**, and your **JWT**. Click "Copy All" and save them somewhere safe!

<Note>
  The API keys are only shown once, so be sure to copy them somewhere safe!
</Note>

After you have your API key, you will want to get your Gateway domain. When you create a Pinata account, you'll automatically have a Gateway created for you! To see it, simply visit the [Gateways Page](https://app.pinata.cloud/gateway) see it listed there.

<img />

The gateway domains are randomly generated and might look something like this:

```
aquamarine-casual-tarantula-177.mypinata.cloud
```

### Start up Hono Project

Run the command below to make a new Hono project:

```bash theme={null}
npm create hono@latest pinata-server
```

After doing so you should see a list of different deployment templates. We would recommend using `Cloudflare Workers` which is what we'll follow through with in this guide. After selecting that `cd` into the project and install the Pinata SDK.

```bash theme={null}
cd pinata-server
npm i pinata
```

After making the project, create a `.dev.vars` file in the root of the project and put in the following variables:

```
PINATA_JWT=
GATEWAY_URL
```

Use the `JWT` from the API key creation in the previous step as well as the `Gateway Domain`. The format of the Gateway domain should be `mydomain.mypinata.cloud`.

### Implement the Server Code

Inside the `src/index.ts` file paste in the following code:

```typescript src/index.ts theme={null}
import { Hono } from 'hono'
import { cors } from 'hono/cors';
import { PinataSDK } from 'pinata'

interface Bindings {
  PINATA_JWT: string;
  GATEWAY_URL: string;
}

const app = new Hono<{ Bindings: Bindings }>()

app.use(cors())

app.get('/', (c) => {
  return c.text('Hello Hono!')
})

app.get('/presigned_url', async (c) => {

	// Handle Auth

  const pinata = new PinataSDK({
    pinataJwt: c.env.PINATA_JWT,
    pinataGateway: c.env.GATEWAY_URL
  })

  const url = await pinata.upload.public.createSignedURL({
    expires: 60 // Last for 60 seconds
  })

  return c.json({ url }, { status: 200 })
})

export default app
```

This creates just two simple endpoints:

* `/` - A home route that just returns `Hello Hono!`
* `/presigned_url` - A route that will return a Presigned URL that is only valid for 60 seconds which our client can use to upload

<Tip>
  As with most server frameworks, you will likely want to protect your API route with an auth layer. You would place there where the comment says `// Handle Auth`
</Tip>

### Usage

Test it out by running the following command in your terminal

```bash theme={null}
npm run dev
```

You should see the console say it's serving at `http://localhost:8787`. While this is running, in a separate terminal window run this curl to test the API endpoint:

```bash theme={null}
curl http://localhost:8787/presigned_url
```

If successful you shoud have a JSON object like the following

```JSON theme={null}
{"url":"https://uploads.pinata.cloud/v3/files/redacted?X-Algorithm=PINATA2&X-Date=1743695529&X-Expires=60&X-Method=%5B%22HEAD%22%2C%22PATCH%22%2C%22POST%22%5D&X-Upload-Option-Network=public&X-User-ID=redacted&X-Signature=redacted"}
```

<Card href="/frameworks/react" icon="react" title="Continue to React Guide">
  To see how you can use Presigned URLs with a client side framework check out the React guide
</Card>


# Next.js
Source: https://docs.pinata.cloud/frameworks/next-js

Get started using Pinata with Next.js

This guide will walk you through setting up Pinata in a Next.js app.

## Create an API Key and get Gateway URL

To create an API key, visit the [Keys Page](https://app.pinata.cloud/developers/keys) and click the "New Key" button in the top right. Once you do that you can select if you want your key to be admin or if you want to scope the privileges of the keys to certain endpoints or limit the number of uses. Make those selections, then give the key a name at the bottom, and click create key.

<Note>
  If you are just getting started we recommend using Admin privileges, then move
  to scope keys as you better understand your needs
</Note>

<img />

Once you have created the keys you will be shown your API Key Info. This will contain your **Api Key**, **API Secret**, and your **JWT**. Click "Copy All" and save them somewhere safe!

<Note>
  The API keys are only shown once, be sure to copy them somewhere safe!
</Note>

After you have your API key, you will want to get your Gateway domain. When you create a Pinata account, you'll automatically have a Gateway created for you! To see it, simply visit the [Gateways Page](https://app.pinata.cloud/gateway) see it listed there.

<img />

The gateway domains are randomly generated and might look something like this:

```
aquamarine-casual-tarantula-177.mypinata.cloud
```

## Server-Side Setup

<Warning>
  Next.js has a limit of how large a file can be passed through the built in API routes, if you need to enable larger uploads follow the client side setup guide
</Warning>

### Start up Next.js Project

As with any Next.js project we can start one up with the following command

```bash theme={null}
npx create-next-app@latest
```

After the project is created `cd` into the repo and install `pinata`

```bash theme={null}
npm i pinata
```

After making the project, create a `.env.local` file in the root of the project and put in the following variables:

```
PINATA_JWT=
NEXT_PUBLIC_GATEWAY_URL=
```

Use the `JWT` from the API key creation in the previous step as well as the `Gateway Domain`. The format of the Gateway domain should be `mydomain.mypinata.cloud`.

### Setup Pinata

Create a directory called `utils` in the root of the project and then make a file called `config.ts` inside of it. In that file we'll export an instance of the Files SDK that we can use throughout the rest of the app.

```typescript utils/config.ts theme={null}
"server only"

import { PinataSDK } from "pinata"

export const pinata = new PinataSDK({
  pinataJwt: `${process.env.PINATA_JWT}`,
  pinataGateway: `${process.env.NEXT_PUBLIC_GATEWAY_URL}`
})
```

### Create Client Side Form

Next we'll want to make an upload form on the client side that will allow someone to select a file and upload it.

In the `/app/page.tsx` file take out the boiler plate code and use the following.

```typescript app/page.tsx theme={null}
"use client";

import { useState } from "react";

export default function Home() {
  const [file, setFile] = useState<File>();
  const [url, setUrl] = useState("");
  const [uploading, setUploading] = useState(false);

  const uploadFile = async () => {
    try {
      if (!file) {
        alert("No file selected");
        return;
      }

      setUploading(true);
      const data = new FormData();
      data.set("file", file);
      const uploadRequest = await fetch("/api/files", {
        method: "POST",
        body: data,
      });
      const signedUrl = await uploadRequest.json();
      setUrl(signedUrl);
      setUploading(false);
    } catch (e) {
      console.log(e);
      setUploading(false);
      alert("Trouble uploading file");
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFile(e.target?.files?.[0]);
  };

  return (
    <main className="w-full min-h-screen m-auto flex flex-col justify-center items-center">
      <input type="file" onChange={handleChange} />
      <button type="button" disabled={uploading} onClick={uploadFile} >
        {uploading ? "Uploading..." : "Upload"}
      </button>
    </main>
  );
}
```

This will take a file from the client side and upload it through an API route we are going to make next.

<Note>
  Next.js does have a file size limitation for what can be passed through the
  API routes, so if you need more than the limit then it is advised to make
  signed JWTs by following [this
  guide](https://www.pinata.cloud/blog/how-to-upload-to-ipfs-from-the-frontend-with-signed-jwts).
</Note>

### Create API Route

Next.js is ideal for file uploads as it's API routes keep keys hidden and unexposed to the client. In the last step we made a function that uploads to `/api/files` so now we need to create that route by making `/app/api/files/route.ts` in our app.

Once you have created that file you can paste in the following code.

```typescript app/api/files/route.ts theme={null}
import { NextResponse, type NextRequest } from "next/server";
import { pinata } from "@/utils/config"

export async function POST(request: NextRequest) {
  try {
    const data = await request.formData();
    const file: File | null = data.get("file") as unknown as File;
    const { cid } = await pinata.upload.public.file(file)
    const url = await pinata.gateways.public.convert(cid);
    return NextResponse.json(url, { status: 200 });
  } catch (e) {
    console.log(e);
    return NextResponse.json(
      { error: "Internal Server Error" },
      { status: 500 }
    );
  }
}
```

This will accept a `POST` request from the client, then send an API request to Pinata with the upload, then make one more request to get a signed URL we can use to see the content. Once complete it will return the URL to the client.

With our URL we can render the image we uploaded by adding the following code to the `page.tsx` file.

```typescript app/page.tsx theme={null}
    return (
		<main className="w-full min-h-screen m-auto flex flex-col justify-center items-center">
			<input type="file" onChange={handleChange} />
			<button type="button" disabled={uploading} onClick={uploadFile}>
				{uploading ? "Uploading..." : "Upload"}
			</button>
			{/* Add a conditional looking for the signed url and use it as the source */}
			{url && <img src={url} alt="Image from Pinata" />}
		</main>
	);
```

And just like that we have uploaded an image to Pinata and recieved a usable URL in return!

## Client-Side Setup

Next.js has a file size limit as to what can be pass through API routes, so another workaround is to upload the file on the client side. To do this securely you can make an API route that generates a temporary upload URL that is used in the upload request.

### Start up Next.js Project

As with any Next.js project we can start one up with the following command

```bash theme={null}
npx create-next-app@latest
```

After the project is created `cd` into the repo and install `pinata`

```bash theme={null}
npm i pinata
```

After making the project, create a `.env.local` file in the root of the project and put in the following variables:

```
PINATA_JWT=
NEXT_PUBLIC_GATEWAY_URL=
```

Use the `JWT` from the API key creation in the previous step as well as the `Gateway Domain`. The format of the Gateway domain should be `mydomain.mypinata.cloud`.

### Setup Pinata

Create a directory called `utils` in the root of the project and then make a file called `config.ts` inside of it. In that file we'll export an instance of the Files SDK that we can use throughout the rest of the app.

```typescript utils/config.ts theme={null}
"server only"

import { PinataSDK } from "pinata"

export const pinata = new PinataSDK({
  pinataJwt: `${process.env.PINATA_JWT}`,
  pinataGateway: `${process.env.NEXT_PUBLIC_GATEWAY_URL}`
})
```

### Create API Route

In order to upload on the client side we need to upload it securely without leaking our admin API key. To avoid this we'll make an API route in our Next project under `app/api/url/route.ts`.

Once you have created that file you can paste in the following code.

```typescript app/api/url/route.ts theme={null}
import { NextResponse } from "next/server";
import { pinata } from "@/utils/config"

export const dynamic = "force-dynamic";

export async function GET() {
  // If you're going to use auth you'll want to verify here
  try {
    const url = await pinata.upload.public.createSignedURL({
      expires: 30, // The only required param
    })
    return NextResponse.json({ url: url }, { status: 200 }); // Returns the signed upload URL
  } catch (error) {
    console.log(error);
    return NextResponse.json({ text: "Error creating API Key:" }, { status: 500 });
  }
}
```

When the client makes a `GET` request to `/api/url` it will return a temporary signed upload URL that is only valid for 30 seconds, which we can use on the client to make the upload request.

### Create Client Side Form

Next we'll want to make an upload form on the client side that will allow someone to select a file and upload it with the signed upload URL

In the `/app/page.tsx` file take out the boiler plate code and use the following.

```typescript app/page.tsx theme={null}
"use client";

import { useState } from "react";
import { pinata } from "@/utils/config";

export default function Home() {
  const [file, setFile] = useState<File>();
  const [uploading, setUploading] = useState(false);

  const uploadFile = async () => {
    if (!file) {
      alert("No file selected");
      return;
    }

    try {
      setUploading(true);
      const urlRequest = await fetch("/api/url"); // Fetches the temporary upload URL
      const urlResponse = await urlRequest.json(); // Parse response
      const upload = await pinata.upload.public
        .file(file)
        .url(urlResponse.url); // Upload the file with the signed URL
      console.log(upload);
      setUploading(false);
    } catch (e) {
      console.log(e);
      setUploading(false);
      alert("Trouble uploading file");
    }
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFile(e.target?.files?.[0]);
  };

  return (
    <main className="w-full min-h-screen m-auto flex flex-col justify-center items-center">
      <input type="file" onChange={handleChange} />
      <button type="button" disabled={uploading} onClick={uploadFile}>
        {uploading ? "Uploading..." : "Upload"}
      </button>
    </main>
  );
}
```

The main thing to understand here is that we are able to use the `url()` method in combination with our upload methods which passes in the signed upload url instead of trying to access the admin key. We can take the response and create a URL to access the file.

```typescript app/page.tsx theme={null}
"use client";

import { useState } from "react";
import { pinata } from "@/utils/config";

export default function Home() {
	const [file, setFile] = useState<File>();
	const [url, setUrl] = useState("");
	const [uploading, setUploading] = useState(false);

	const uploadFile = async () => {
		if (!file) {
			alert("No file selected");
			return;
		}

		try {
			setUploading(true);
			const urlRequest = await fetch("/api/url"); // Fetches the temporary upload URL
      const urlResponse = await urlRequest.json(); // Parse response
      const upload = await pinata.upload.public
        .file(file)
        .url(urlResponse.url); // Upload the file with the signed URL
      const fileUrl = await pinata.gateways.public.convert(upload.cid)
			setUrl(fileUrl);
			setUploading(false);
		} catch (e) {
			console.log(e);
			setUploading(false);
			alert("Trouble uploading file");
		}
	};

	const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		setFile(e.target?.files?.[0]);
	};

	return (
		<main className="w-full min-h-screen m-auto flex flex-col justify-center items-center">
			<input type="file" onChange={handleChange} />
			<button type="button" disabled={uploading} onClick={uploadFile}>
				{uploading ? "Uploading..." : "Upload"}
			</button>
			{url && <img src={url} alt="Image from Pinata" />}
		</main>
	);
}
```


# Node.js
Source: https://docs.pinata.cloud/frameworks/node-js



This Node.js quickstart should get you up and running with your standard backend javascript setup, and by using the API will give you flexibility when it comes to [uploading files](files/uploading-files).

## Generate your API Keys

To create an API key, visit the [Keys Page](https://app.pinata.cloud/developers/keys) and click the "New Key" button in the top right. Once you do that you can select if you want your key to be admin or if you want to scope the privileges of the keys to certain endpoints or limit the number of uses. Make those selections, then give the key a name at the bottom, and click create key.

<Note>
  If you are just getting started, we recommend using Admin privileges, then
  move to scope keys as you better understand your needs
</Note>

<img />

Once you have created the keys you will be shown your API Key Info. This will contain your **Api Key**, **API Secret**, and your **JWT**. Click "Copy All" and save them somewhere safe!

<Note>
  The API keys are only shown once, be sure to copy them somewhere safe!
</Note>

## Setup a Node.js Project

To start you can go to your terminal and put in the following code

```bash theme={null}
mkdir pinata-starter && cd pinata-starter && npm init -y
```

Then install the [Files SDK](/sdk) as well as `dotenv`

```bash theme={null}
npm i pinata dotenv
```

In the root of the directory make a `.env` file where we're pull the following variables.

```
PINATA_JWT=
GATEWAY_URL=
```

Use the `JWT` from the API key creation in the previous step as well as the `Gateway Domain`. The format of the Gateway domain should be `mydomain.mypinata.cloud`.

Now we'll make two files, `index.js` and `hello-world.txt`.

```bash theme={null}
touch index.js && touch hello-world.txt
```

Inside the `hello-world.txt` you can put whatever you'd like such as `Hello World!`.

## Upload a File to Pinata

Once we have our initial project setup we can put the following code into our `index.js` file.

<CodeGroup>
  ```javascript index.js (Node v.20) theme={null}
  const { PinataSDK } = require("pinata")
  const fs = require("fs")
  const { Blob } = require("buffer")
  require("dotenv").config()

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT,
    pinataGateway: process.env.GATEWAY_URL
  })

  async function upload(){
    try {
      const blob = new Blob([fs.readFileSync("./hello-world.txt")]);
      const file = new File([blob], "hello-world.txt", { type: "text/plain"})
      const upload = await pinata.upload.public.file(file);
      console.log(upload)
    } catch (error) {
      console.log(error)
    }
  }

  upload()
  ```

  ```javascript index.js (Node v.18) theme={null}
  const { PinataSDK } = require("pinata")
  const fs = require("fs")
  const { Blob } = require("buffer")
  require("dotenv").config()

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT,
    pinataGateway: process.env.GATEWAY_URL
  })

  async function upload(){
    try {
      const blob: any = new Blob([fs.readFileSync("./hello-world.txt")]);
      const upload = await pinata.upload.public.file(blob);
      console.log(upload)
    } catch (error) {
      console.log(error)
    }
  }

  upload()
  ```
</CodeGroup>

You can run this by using `node index.js` in the terminal. After uploading a file you should get a response that looks like this

```javascript theme={null}
{
    id: "349f1bb2-5d59-4cab-9966-e94c028a05b7",
    name: "file.txt",
    cid: "bafybeihgxdzljxb26q6nf3r3eifqeedsvt2eubqtskghpme66cgjyw4fra",
    size: 4682779,
    number_of_files: 1,
    mime_type: "text/plain",
    group_id: null
}
```

## Fetch the File through a Gateway

With the `cid` you can view the file or fetch the data using your Gateway. Lets make a new file called `fetch.js` and put in the following code.

```javascript fetch.js theme={null}
const { PinataSDK } = require("pinata")
require("dotenv").config()

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT,
  pinataGateway: process.env.GATEWAY_URL
})

async function main() {
  try {
    const file = await pinata.gateways.public.get("bafkreiac3t35fklpiwqonav2vj4x2dh6x2zugkdu7dsh6zkaq5jr33lcwy")
    console.log(file.data)
  } catch (error) {
    console.log(error);
  }
}

main()
```


# React
Source: https://docs.pinata.cloud/frameworks/react



Since React is a client side framework it is recommend to handle uploads using [Presigned URLs](/files/presigned-urls) using a server side framework like [Hono](/frameworks/hono). We would highly recommend following the Hono guide below before doing this React guide!

<Card href="/frameworks/Hono" icon="fire" title="Hono Guide" />

## Installation

### Get Gateway URL

Before we start you'll need your Dedicated Gateway domain. When you create a Pinata account, you'll automatically have a Gateway created for you! To see it, simply visit the [Gateways Page](https://app.pinata.cloud/gateway) see it listed there.

<img />

The gateway domains are randomly generated and might look something like this:

```
aquamarine-casual-tarantula-177.mypinata.cloud
```

### Start up React Project

Run the command below to make a new React project:

```bash theme={null}
npm create vite@latest
```

Give the project a name and select the React framework. Then `cd` into the project and install `pinata`.

```bash theme={null}
npm i pinata
```

After making the project, create a `.env.local` file in the root of the project and put in the following variable:

```
VITE_SERVER_URL=
VITE_GATEWAY_URL=
```

The `VITE_SERVER_URL` is the URL of your server endpoint that will return Presigned URLs. If you don't have one be sure to follow the [Hono guide](/frameworks/hono) first. If you did follow it then you'll remember it was `http://localhost:8787` and we'll need to make sure it's running in order for our flow to work.

The format of the Gateway domain should be `mydomain.mypinata.cloud`.

## Implementation

Now that we have our initial setup, open the `src/App.tsx` file and replace it with the following code.

```typescript src/App.tsx theme={null}
import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { PinataSDK } from 'pinata'

const pinata = new PinataSDK({
  pinataJwt: "",
  pinataGateway: import.meta.env.VITE_GATEWAY_URL
})

function App() {
  const [file, setFile] = useState<File | null>(null)
  const [uploadStatus, setUploadStatus] = useState('')
  const [link, setLink] = useState('')

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0])
    }
  }

  const handleUpload = async () => {
    if (!file) return

    try {
      setUploadStatus('Getting upload URL...')
      const urlResponse = await fetch(`${import.meta.env.VITE_SERVER_URL}/presigned_url`, {
        method: "GET",
        headers: {
          // Handle your own server authorization here
        }
      })
      const data = await urlResponse.json()

      setUploadStatus('Uploading file...')

      const upload = await pinata.upload.public
        .file(file)
        .url(data.url)

      if (upload.cid) {
        setUploadStatus('File uploaded successfully!')
        const ipfsLink = await pinata.gateways.public.convert(upload.cid)
        setLink(ipfsLink)
      } else {
        setUploadStatus('Upload failed')
      }
    } catch (error) {
      setUploadStatus(`Error: ${error instanceof Error ? error.message : String(error)}`)
    }
  }

  return (
    <>
      <div>
        <a href="<https://vite.dev>" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="<https://react.dev>" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React + Pinata</h1>
      <div className="card">
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload} disabled={!file}>
          Upload to Pinata
        </button>
        {uploadStatus && <p>{uploadStatus}</p>}
        {link && <a href={link} target='_blank'>View File</a>}
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App
```

In our code we have a pretty simple form that will trigger `handleSubmit()`. This function will do the following:

* Make a request to our server for a Presigned URL (you will want to handle any server side auth here)
* Use the returned Presigned URL in a client side upload
* Use the upload response to create a link to the file

To try it out make sure your server is running, then in another terminal Run

```bash theme={null}
npm run dev
```

Open up the site on `http://localhost:5173` and upload a file!


# Remix
Source: https://docs.pinata.cloud/frameworks/remix

Get started using Pinata with Remix

This guide will walk you through setting up Pinata in a Remix app.

## Create an API Key and get Gateway URL

To create an API key, visit the [Keys Page](https://app.pinata.cloud/developers/keys) and click the "New Key" button in the top right. Once you do that you can select if you want your key to be admin or if you want to scope the privileges of the keys to certain endpoints or limit the number of uses. Make those selections, then give the key a name at the bottom, and click create key.

<Note>
  If you are just getting started we recommend using Admin privileges, then move
  to scope keys as you better understand your needs
</Note>

<img />

Once you have created the keys you will be shown your API Key Info. This will contain your **Api Key**, **API Secret**, and your **JWT**. Click "Copy All" and save them somewhere safe!

<Note>
  The API keys are only shown once, be sure to copy them somewhere safe!
</Note>

After you have your API key, you will want to get your Gateway domain. When you create a Pinata account, you'll automatically have a Gateway created for you! To see it, simply visit the [Gateways Page](https://app.pinata.cloud/gateway) see it listed there.

<img />

The gateway domains are randomly generated and might look something like this:

```
aquamarine-casual-tarantula-177.mypinata.cloud
```

## Startup Remix Project

We can start a Remix app by entering the command below into the terminal

```bash theme={null}
npx create-remix@latest pinata-remix
```

After it's finished installed we'll want to `cd` into the project and install the `pinata` SDK.

```bash theme={null}
cd pinata-remix && npm i pinata
```

Now let's make a file called `.env` file in the root of the project with the following variables:

```
PINATA_JWT= # The Pinata JWT API key we got earlier
GATEWAY_URL= # The Gateway domain we grabbed earlier, formatting just as we copied it from the app
```

## Setup Pinata

Make a folder in the root of the project called `utils`, and inside make a file called `pinata.ts` with the following code:

```typescript theme={null}
import { PinataSDK } from "pinata";

export const pinata = new PinataSDK({
	pinataJwt: process.env.PINATA_JWT,
	pinataGateway: process.env.GATEWAY_URL,
});
```

This will create an instance of the SDK we can use throughout the app.

## Upload Form and Server Action

In the `app/routes` directory we can remove the boilerplate code and replace it with the code below.

```typescript app/routes/_index.tsx theme={null}
import type { ActionFunctionArgs, MetaFunction } from "@remix-run/node";
import { json } from "@remix-run/node";
import { Form, useActionData, useNavigation } from "@remix-run/react";
import { pinata } from "utils/config";

export const meta: MetaFunction = () => {
	return [
		{ title: "Remix + Pinata" },
		{ name: "description", content: "Upload files on Remix with Pinata!" },
	];
};

// Server side action to handle our upload
export const action = async ({ request }: ActionFunctionArgs) => {
	const formData = await request.formData();
	const file = formData.get("file") as File;
	const { cid } = await pinata.upload.public.file(file);
	const url = await pinata.gateways.public.convert(cid);
	return json({ url });
};

export default function Index() {
	const actionData = useActionData<typeof action>();
	const navigation = useNavigation();
	const isSubmitting = navigation.state === "submitting";

	return (
		<div className="font-sans p-4 flex flex-col gap-4 justify-center items-center min-h-screen max-w-[500px] mx-auto">
			<h1 className="text-3xl font-bold">Remix + Pinata</h1>
			<Form
				encType="multipart/form-data"
				method="post"
				className="flex flex-col gap-4"
			>
				<input type="file" name="file" className="" />
				<button
					className="bg-[#582CD6] text-white rounded-md p-2"
					type="submit"
				>
					{isSubmitting ? "Uploading..." : "Upload"}
				</button>
			</Form>
			{actionData?.url && (
				<div className="mt-4">
					<a
						href={actionData.url}
						target="_blank"
						rel="noreferrer"
						className="text-[#582CD6] underline"
					>
						{actionData.url}
					</a>
				</div>
			)}
		</div>
	);
}
```

Let's walk through what's happening here. To start we have our client side markup:

```typescript theme={null}
<div className="font-sans p-4 flex flex-col gap-4 justify-center items-center min-h-screen max-w-[500px] mx-auto">
			<h1 className="text-3xl font-bold">Remix + Pinata</h1>
			<Form
				encType="multipart/form-data"
				method="post"
				className="flex flex-col gap-4"
			>
				<input type="file" name="file" className="" />
				<button
					className="bg-[#582CD6] text-white rounded-md p-2"
					type="submit"
				>
					{isSubmitting ? "Uploading..." : "Upload"}
				</button>
			</Form>
			{actionData?.url && (
				<div className="mt-4">
					<a
						href={actionData.url}
						target="_blank"
						rel="noreferrer"
						className="text-[#582CD6] underline"
					>
						{actionData.url}
					</a>
				</div>
			)}
		</div>
```

This is a simple `Form` element provided by Remix which lets us make a submission to a server action. The most important piece to notice here is the `encType="multipart/form-data"`, which is crucial to make file / multipart requests work in Remix!

Then we have our server action:

```typescript theme={null}
export const action = async ({ request }: ActionFunctionArgs) => {
	const formData = await request.formData();
	const file = formData.get("file") as File;
	const { cid } = await pinata.upload.public.file(file);
	const url = await pinata.gateways.public.convert(cid);
	return json({ url });
};
```

This will be the default endpoint used when we submit our form. It will parse the incoming `formData`, get the `file` attached, and then we upload it to Pinata using `pinata.upload.public.file()`. From that method we deconstruct the result and return the `cid` which we can use in `convert`. This will make a URL we can return to the client and make accessible to the user, and in our case the `<a>` tag that links to the content.


# SvelteKit
Source: https://docs.pinata.cloud/frameworks/sveltekit



This guide will walk you through setting up Pinata in a SvelteKit app.

## Create an API Key and get Gateway URL

To create an API key, visit the [Keys Page](https://app.pinata.cloud/developers/keys) and click the "New Key" button in the top right. Once you do that you can select if you want your key to be admin or if you want to scope the privileges of the keys to certain endpoints or limit the number of uses. Make those selections, then give the key a name at the bottom, and click create key.

<Note>
  If you are just getting started we recommend using Admin privileges, then move
  to scope keys as you better understand your needs
</Note>

<img />

Once you have created the keys you will be shown your API Key Info. This will contain your **Api Key**, **API Secret**, and your **JWT**. Click "Copy All" and save them somewhere safe!

<Note>
  The API keys are only shown once, be sure to copy them somewhere safe!
</Note>

After you have your API key, you will want to get your Gateway domain. When you create a Pinata account, you'll automatically have a Gateway created for you! To see it, simply visit the [Gateways Page](https://app.pinata.cloud/gateway) see it listed there.

<img />

The gateway domains are randomly generated and might look something like this:

```
aquamarine-casual-tarantula-177.mypinata.cloud
```

## Server-side Setup

This guide will walk you through a server side upload flow in SvelteKit

### Start up SvelteKit Project

The easiest way to start building a SvelteKit app is to run `npm create`

```bash theme={null}
npm create svelte@latest pinata-app
- Which Svelte app template? Skeleton project
- Add type checking with TypeScript? Yes, using TypeScript syntax
- Select additional options (use arrow keys/space bar) <- These are optional

```

After the project is created `cd` into the repo and install `pinata`

```bash theme={null}
npm i pinata
```

In this demo we will be using `tailwindcss` with typography plugin. Follow other CSS Framework guides respectively.

```bash theme={null}
npx svelte-add@latest tailwindcss
```

After making the project, create a `.env.local` file in the root of the project and put in the following variables:

```
PINATA_JWT=
PUBLIC_GATEWAY_URL=
```

Use the `JWT` from the API key creation in the previous step as well as the `Gateway Domain`. The format of the Gateway domain should be `mydomain.mypinata.cloud`.

### Setup Pinata

Create a directory called `server` in the `src/lib` folder of the project and then make a file called `pinata.ts` inside of it. In that file we'll export an instance of the Files SDK that we can use throughout the rest of the app.

<Note>
  The use of the `server` directory prevents it being used client side.
</Note>

```typescript src/lib/server/pinata.ts theme={null}
import { PinataSDK } from "pinata"
import { PINATA_JWT } from "$env/static/private";
import { PUBLIC_GATEWAY_URL } from "$env/static/public";

export const pinata = new PinataSDK({
  pinataJwt: `${PINATA_JWT}`,
  pinataGateway: `${PUBLIC_GATEWAY_URL}`
})
```

### Create Client Side Form

Next we'll want to add a form on our home page that will allow someone to select a file and upload it.
In the `src/routes/+page.svelte` file take out the boiler plate code and use the following.
Lets also restrict the allowed extensions for the file. (e.g. jpg, jpeg, png, webp).

```typescript src/routes/+page.svelte theme={null}
<script lang="ts">
  import { enhance } from '$app/forms';

  let uploading = false;

  function handleUpload() {
    uploading = true;
      return async ({ update }) => {
        await update();
        uploading = false;
      };
  }
</script>

<main class="w-full min-h-screen m-auto flex flex-col justify-center items-center">
  <form method="POST" enctype="multipart/form-data" use:enhance={handleUpload}>
    <input type="file" id="file" name="fileToUpload" accept=".jpg, .jpeg, .png, .webp" />
    <button disabled={uploading} type="submit">
      {uploading ? 'Uploading...' : 'Upload'}
    </button>
  </form>
</main>

```

This will take a file from the client side and upload it through a form Action we are going to make next.

### Create Server Action

Create a server file, `src/routes/+page.server.ts`, so that we can add a form action to use.
Since this demo and page only has 1 form, we will keep the `default` action.

```typescript src/routes/+page.server.ts theme={null}
import { fail, json, type Actions } from "@sveltejs/kit";
import { pinata } from "$lib/server/pinata";

export const actions: Actions = {
  default: async ({ request }) => {
    try {
      const formData = await request.formData();
      const uploadedFile = (formData?.get('fileToUpload') as File);

      if (!uploadedFile.name || uploadedFile.size === 0) {
        return fail(400, {
          error: true,
          message: "You must provide a file to upload"
        })
      }

      const upload = await pinata.upload.public.file(uploadedFile);
      const url = await pinata.gateways.public.convert(upload.cid);
      return { url, filename: uploadedFile.name, status: 200 };
    } catch (error) {
      console.log(error);
      return json(
        { error: "Internal Server Error" },
        { status: 500 }
      );
    }
  }
}
```

The form action will send an API request to Pinata with the upload, then use the resulting CID to create a URL we can use to see the content.
Once complete, we can define the return data sent to the client.

### Access the Returned value of the Form Action

We can access the returned data by exporting the `form` prop on our `+page.svelte`. Now, after submitting the form,
the `form` prop will be updated and we can conditionally render the image we just uploaded.

```typescript src/routes/+page.svelte theme={null}
<script lang="ts">
  import { enhance } from '$app/forms';
  import type { ActionData } from './$types';

  export let form: ActionData;
  let uploading = false;

  function handleUpload() {
    uploading = true;
      return async ({ update }) => {
        await update();
        uploading = false;
      };
  }
</script>

<main class="w-full min-h-screen m-auto flex flex-col justify-center items-center">
  <form method="POST" enctype="multipart/form-data" use:enhance={handleUpload}>
    <input type="file" id="file" name="fileToUpload" accept=".jpg, .jpeg, .png, .webp" />
    <button disabled={uploading} type="submit">
      {uploading ? 'Uploading...' : 'Upload'}
    </button>
  </form>
  {#if form && form.status === 200}
    <img src={form.url} alt={form.filename} />
  {/if}
</main>

```

And just like that we have uploaded an image to Pinata and recieved a usable URL in return!
Remember that the url for the image is ephemeral, once you refresh the page the url and image will be gone.


# Dedicated IPFS Gateways
Source: https://docs.pinata.cloud/gateways/dedicated-ipfs-gateways



Dedicated Gateways are the fastest way to fetch content from IPFS, and are the ideal tool when building decentralized applications. When you create a Pinata account, you'll automatically have a Dedicated Gateway created for you! To see it, simply visit the [Gateways Page](https://app.pinata.cloud/gateway).

<img />

The gateway domains are randomly generated and might look something like this:

```
aquamarine-casual-tarantula-177.mypinata.cloud
```

## Viewing Content Through Your Gateway

To view content through your gateway, grab the CID of the file you'd like to view and add it to your gateway URL, like so:

<img />

Simple as that!

You can also fetch the data programatically using the [get](/sdk/gateways/public/get) method in the [SDK](/sdk).

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const file = await pinata.gateways.public.get("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
```

## Restricted vs Open

All Pinata Dedicated Gateways are restricted by default. This mean they will only serve CIDs that are pinned to your account, which keeps your gateway safe from abuse by outside actors who may want to use it for themselves.

If you plan to upload content to your own account then use your gateway to fetch it, you shouldn't have to touch a thing and it will work as expected! However, lets say you're building a marketplace and you need to fetch content outside your account. In that case, you will want to use [Gateway Access Controls](/gateways/gateway-access-controls). Adding one of these will allow you to access CIDs from the public IPFS network, but it has to meet that access control condition, like a Gateway API Key or Host Origin requirement. Be sure to read our [docs on Gateway Access Controls](/gateways/gateway-access-controls) to learn more.

<img />

<Note>
  The only way to open a Dedicated Gateway and allow any CID to go through is to
  add a Gateway Access Control
</Note>

## Convert IPFS Links or Gateway URLs to use Your Dedicated Gateway

If you're a developer building an app to index the blockchain, it's likely you'll encounter several IPFS URL formats that might not be ideal to work with:

```
ipfs://QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng

https://ipfs.io/ipfs/QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng
```

The Pinata SDK is designed to assist you in scenarios like this. It can take IPFS urls, whether they are the protocol standard (`ipfs://`) or another gateway (`https://ipfs.io`), and turn them into your specified Dedicated Gateway.

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const url = await pinata.gateways.public
  .convert("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")

// Optionally add a different gateway prefix
// const url = await pinata.gateways.public
//   .convert("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng", "https://ipfs.io")
```

## Adding a Custom Domain

Pinata also allows you to create a custom domain for your Dedicated Gateway. Simply visit the [Gateways Page](https://app.pinata.cloud/gateway), click the menu button on the right side of your gateway, then click Add Custom Domain. You'll need to own the domain you want to use. When you enter your domain, you will be prompted to enter DNS information through your registrar.

## Billing and Usage

When it comes to using a Dedicated Gateway, there are a few metrics Pinata uses for billing.

| Metric    | Description                                                                                                                                                                                                                                                                                                                                                                              |
| :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bandwidth | Bandwidth is the amount of data that is being going through your Gateway. For instance, if you have a 10MB file go through your gateway 100 times, that would be 1GB of bandwidth used for the month.                                                                                                                                                                                    |
| Requests  | A request is anytime content is queried through the gateway, so if you run `wget https://mygateway.mypinata.cloud/ipfs/QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng` in your terminal, that would be one request. Or if you had someone visit your app that uses the gateway on the client side, each time the website requests content from IPFS using the gateway, that's a request. |

Both of these metrics reset on a monthly basis based on your billing cycle.

<Note>
  If you're using a Dedicated Gateway for your NFT project, be sure to check out
  [this
  guide](https://knowledge.pinata.cloud/en/articles/6461213-token-uris-in-nft-projects)
  on how you should do that.
</Note>

If you have any questions in regards to billing, please don't hesitate to reach out via our chat in the bottom right of our app or [email us](mailto:team@pinata.cloud)!


# Gateway Access Controls
Source: https://docs.pinata.cloud/gateways/gateway-access-controls



Pinata's Dedicated Gateways make it possible to fetch and serve IPFS content quickly and reliably, however there can be security risks in exposing an open gateway to the world. That's why Pinata has created Gateway Access Controls. These controls will allow you to further limit your gateway, making sure only your platform is using it. This is accomplished with **Gateway Keys, IP Address Restrictions,** and **Host Origin Restrictions.**

By default, your Dedicated Gateway is restricted, it will only serve content pinned to your account. When you add an Access Control, your gateway becomes open and will be able to serve any content from IPFS, but only when requests meet your security requirements.

## Restricted vs Open

When working with IPFS Gateways the behavior usually falls into two categories: Restricted or Open.

### Restricted Gateway

Restricted means the gateway can only load content that is pinned to that user's account. This is the default behavior for Pinata's Dedicated Gateway, as it provides the maximum level of security. Any requests made to a CID outside the user's account will be unauthorized.

<img />

<Info>This check of whether or not a file is pinned or not using `/data/pinList` in the Pinata API, which means recursive CIDs in folders are considered unauthorized. Instead, use the folder CID in the path of the gateway followed by the file name.</Info>

### Open Gateway

<img />

Open means the gateway can access any content on IPFS, not just pinned content. An example might be a public gateway like `ipfs.io/ipfs/` which is open to everyone, but has heavy rate limiting. For Dedicated Gateways, you achieve this open state by adding Access Controls.

### Why Access Controls?

<img />

If someone were to open their Dedicated Gateway without any permissions, anyone who found the domain could use it for themselves and abuse it, leaving the owner with a big bill of overages.

<img />

Because of this Pinata developed Gateway Access Controls to allow users to open their Gateways, but with restrictions that must be met first.

## Access Controls

Pinata currently provides three primary methods for opening your gateway securely:

* [Gateway Keys](#gateway-keys)
* [IP Address](#ip-address)
* [Host Origin](#host-origin)

### Gateway Keys

Adding a Gateway Key restriction means that content served through your gateway will only be served successfully if the key is present with the request. **Importantly, content pinned to your account won't be accessible through your gateway if you've implemented a gateway key restriction and fail to include that token in content requests.**

To create a Gateway Key, click on the button that says "Request Key."

<img />

When you create a key you will have the ability to preview the token by clicking the "eye" icon, or copy the token to your clipboard with the "copy" icon. At any point, you can delete a gateway key by clicking the "trash" icon.

<img />

Once you have the key, there are two ways you can use it in the gateway request.

#### Query Parameter

To use the query parameter method, simply add this to the end of a gateway request url:

```
?pinataGatewayToken=PASTE_IN_ACCESS_TOKEN
```

#### Header

Another way to use the gateway key is in the request header. The Key Value would look like this:

| Key                    | Value        |
| ---------------------- | ------------ |
| x-pinata-gateway-token | GATEWAY\_KEY |

**Please keep in mind that using the gateway key in the request header may not work in a client side application, so consider using IP Address restriction instead for those use cases.**

### IP Address

You can also restrict your gateway by IP Address. You can add up to 100 different IP addresses (individually). When you add this restriction, only content requested from an IP address that you've added will be served through your gateway.

To start, click "Set IP Address" on the right side of the menu.

<img />

You will get window asking for a valid IP Address which will allow any requests being made from the IP Address to go through!

<img />

### Host Origin

With the Host Origin restriction, you can make sure your gateway can only be used on a specific domain (for example, '[https://app.pinata.cloud](https://app.pinata.cloud)'). To get started, click on "Add Host Origin."

<img />

After that, you can add the domain you would like your gateway to be used from!

<img />

<Warning>
  Make sure you include the `https://` protocol prefix in the URL and that there are no trailing slashes! To test localhost use the IP Access control with your public facing IP.
</Warning>

Keep in mind, if you are rendering content on the client side using Host Origins, you will need to include a `crossorigin` tag in your `img`, `video`, `audio`, `link`, or `script` elements. Here is an example with an img element in React:

<CodeGroup>
  ```javascript html theme={null}
  <img
    src="https://pinata-media.mypinata.cloud/ipfs/CID"
    crossorigin="anonymous"
    alt="pinnie"
  />
  ```

  ```javascript React theme={null}
  <img
    src="https://pinata-media.mypinata.cloud/ipfs/CID"
    crossOrigin="anonymous"
    alt="pinnie"
  />
  ```
</CodeGroup>

For more info on `crossorigin` please read this article [here](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin)!

### Multiple Restrictions

You can add multiple Access Controls, and they will perform as an "OR" operator. This means that if you have Host Origins and a Gateway Key set, you can use either one for content to go through.


# Image Optimizations
Source: https://docs.pinata.cloud/gateways/image-optimizations



Pinata image optimizations provides image optimization functionality directly through your [Gateway](/gateways/retrieving-files). These capabilities that can significantly improve the load time and experience when viewing image content.

## Usage

To use image optimizations on files you've uploaded simply add on the queries listed in the [reference](#reference) to your full Gateway url, which might look something like this:

```
https://example-gateway.mypinata.cloud/files/{cid}?img-width=500&img-height=500
```

There are differences when using image optmizations for public files vs private files, so be sure to visit the [retrieving files](/gateways/retrieving-files) for more information!

## Reference

At least one option must be specified. Options are comma-separated (spaces are not allowed anywhere). Names of options can be specified in full or abbreviated.

<ParamField type="string">
  Specifies maximum width of the image in pixels. Exact behavior depends on the fit mode (described below).
</ParamField>

<ParamField type="string">
  Specifies maximum height of the image in pixels. Exact behavior depends on the fit mode (described below).
</ParamField>

<ParamField type="string">
  Device Pixel Ratio. Default 1. Multiplier for width/height that makes it easier to specify higher-DPI sizes in .
</ParamField>

<ParamField type="string">
  Affects interpretation of width and height. All resizing modes preserve aspect ratio. Available modes are:

  * `img-fit=scale-down` Image will be shrunk in size to fully fit within the given width or height, but won’t be enlarged.

  * `img-fit=contain` Image will be resized (shrunk or enlarged) to be as large as possible within the given width or height while preserving the aspect ratio.

  * `img-fit=cover` Image will be resized to exactly fill the entire area specified by width and height, and will cropped if necessary.

  * `img-fit=crop` Image will be shrunk and cropped to fit within the area specified by width and height. The image won’t be enlarged. For images smaller than the given dimensions it’s the same as scale-down. For images larger than the given dimensions, it’s the same as cover.

  * `img-fit=pad` Image will be resized (shrunk or enlarged) to be as large as possible within the given width or height while preserving the aspect ratio, and the extra area will be filled with a background color (white by default). Transparent background may be very expensive, and it’s better to use fit=contain and CSS object-fit: contain property instead.
</ParamField>

<ParamField type="string">
  When cropping with `fit=cover`, specifies the most important side or point in the image that shouldn’t be cropped off.

  * `img-gravity=auto` The point will be guessed by looking for areas that stand out the most from image background

  * `img-gravity=side` and `img-gravity=XxY`
    If a side (left, right, top, bottom) or coordinates specified on a scale from 0.0 (top or left) to 1.0 (bottom or right), 0.5 being the center. The X and Y coordinates are separated by lowercase x, e.g. 0x1 means left and bottom, 0.5x0.5 is the center, 0.5x0.33 is a point in the top third of the image.
</ParamField>

<ParamField type="string">
  Specifies quality for images in JPEG, WebP and AVIF formats. The quality is in 1-100 scale, but useful values are between 50 (low quality, small file size) and 90 (high quality, large file size). 85 is the default. When using the PNG format, an explicit quality setting allows use of PNG8 (palette) variant of the format.
</ParamField>

<ParamField type="string">
  Allows serving of the WebP format to browsers that support it. If this option is not specified, a standard format like JPEG or PNG will be used.
</ParamField>

<ParamField type="string">
  Reduces animations to still images. This setting is recommended to avoid surprisingly large animGIF files, or flashing images.
</ParamField>

<ParamField type="string">
  Specifies strength of sharpening filter. The value is a floating-point number between 0 (no sharpening) and 10 (max). 1 is a recommended value.
</ParamField>

<ParamField type="string">
  In case of a fatal error that prevents the image from being resized use `img-onerror=redirect` to redirect to the unresized source image URL. This may be useful in case some images require user authentication and cannot be fetched. This option shouldn’t be used if the source images may be very large. This option is ignored if the image is from another domain (subdomains are OK).

  * `img-onerror=redirect` Redirects to original source url
</ParamField>

<ParamField type="string">
  Controls amount of invisible metadata (EXIF data) that should be preserved. Color profiles and EXIF rotation are applied to the image even if the metadata is discarded. Note that if the Polish feature is enabled, all metadata may have been removed already and this option may have no effect.

  * `img-metadata=keep` Preserve most of the image metadata (including GPS location) when possible.

  * `img-metadata=copyright` Discard all metadata except EXIF copyright tag. This is the default for JPEG images. img-metadata=none Discard all invisible metadata.
</ParamField>

## Formats and limitations

Read JPEG, PNG, GIF (including animations), and WebP images. SVG is not supported, since this format is inherently scalable and does not need resizing. Resize and generate JPEG and PNG images, and optionally AVIF or WebP. AVIF format is supported on a best-effort basis. Images that cannot be compressed as AVIF will be served as WebP instead.

## SDK Method Reference

Image Optimizations are built into both [`get`](/sdk/gateways/public/get) and [`createAccessLink`](/sdk/gateways/private/create-access-link) methods of the SDK.

```typescript theme={null}
type OptimizeImageOptions = {
  width?: number;
  height?: number;
  dpr?: number;
  fit?: "scaleDown" | "contain" | "cover" | "crop" | "pad";
  gravity?: "auto" | "side" | string;
  quality?: number;
  format?: "auto" | "webp";
  animation?: boolean;
  sharpen?: number;
  onError?: boolean;
  metadata?: "keep" | "copyright" | "none";
};
```

```typescript theme={null}
const data = await pinata.gateways.public
  .get("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
  .optimizeImage({
    width: 500,
    height: 500,
    format: "webp"
  })
```


# Content Addressable
Source: https://docs.pinata.cloud/gateways/plugins/content-addressable

Use the Content Addressable plugin to include CID signatures

The Content Addressable plugin works in tandem with the Signatures API, allowing users to get a signature field in the headers of a Dedicated Gateway request. This can be very useful to help verify content ownership when retrieving files from IPFS.

<Note>
  For more information about adding signatures to CIDs on IPFS please read the [Signatures Guide](/files/signatures)
</Note>

## Installation

Follow the steps in the [Getting Started](/gateways/plugins/getting-started) guide to install the Content Addressable Plugin.

## Usage

Once the plugin is installed the rest is quite simple. If a CID as a signature attached to it, then there will be a `pinata-signature` field in the headers.

```typescript theme={null}
const signatureReq = await fetch(
  `https://<YOUR_GATEWAY_DOMAIN>.mypinata.cloud/ipfs/<CID>`,
  {
    method: "HEAD",
  }
);
const signature = signatureReq.headers.get("pinata-signature");

//0xbe92f9747e1712f2673ff0de6c7058968b869ce14ed6e0949fa3c485e420a27c66695401f56d3d3158fcbb6a5a7809e91acb9660dc00f31673d7efe6f77665b31c
```


# Getting Started
Source: https://docs.pinata.cloud/gateways/plugins/getting-started

Learn how to use Dedicated Gateway plugins to supercharge your IPFS delivery system

Dedicated Gateways are crucial for retrieving and delivering content on IPFS, but there are times you may need additonal functionality. Gateway Plugins serve that purpose, anything from hot swapping CIDs to delivering signatures and more!

## Installing Plugins

You can install plugins either through the Pinata App or the Pinata API.

### Pinata App

To install a plugin navigate to the Plugins Marketplace tab on the right side.

<Frame>
  <img />
</Frame>

Once there you can find the plugin you want to install and click "Install." This will bring up a drop down of your Dedicated Gateways to choose which the plugin is installed to.

<Frame>
  <img />
</Frame>

Once installed you can confirm its there by going to the "My Plugins" tab.

<Frame>
  <img />
</Frame>

### Pinata API

With the Pinata API you can list all available plugins using the [/ipfs/plugins\_marketplace](/api-reference/endpoint/ipfs/list-marketplace-plugins) endpoint.

<CodeGroup>
  ```typescript Get Plugins theme={null}
  const plugins = await fetch("https://api.pinata.cloud/v3/ipfs/plugins_marketplace", {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${PINATA_JWT}`
    }
  })
  ```

  ```json Response theme={null}
  {
    "data": [
      {
        "id": 1,
        "name": "Content Addressable Attestation",
        "description": "Verify the authenticity and ownership of files added to the IPFS network by signing them with your Ethereum wallet.",
        "image": "https://mktg.mypinata.cloud/ipfs/QmVm3jRZ7S2KMmYEvkmkwncRCmBSUEuzNKfm2AgJkfBGKZ",
        "tags": [
          "verifiability",
          "security"
        ]
      },
      {
        "id": 2,
        "name": "Hot Swaps",
        "description": "Make IPFS mutable by pointing your original CID to a new file.",
        "image": "https://mktg.mypinata.cloud/ipfs/QmVpy6v7YASWUQjmqgUxKwbn6zgzuVSRudzdZMynpBjSJo",
        "tags": [
          "files"
        ]
      }
    ]
  }
  ```
</CodeGroup>

To install one you can make a request to [/ipfs/gateway\_plugins/:gateway\_id](/api-reference/endpoint/ipfs/install-gateway-plugin) by using the [gateway\_id](/api-reference/endpoint/ipfs/list-gateways) as a path parameter and the `plugin_id` as body of the request.

<CodeGroup>
  ```typescript Install Plugin theme={null}
  const data = JSON.stringify({
    plugin_id: 1
  })

  const gatewayId = "8673cd80-bf53-4bca-b684-bec1d6bdf004"

  const installPlugin = await fetch(`https://api.pinata.cloud/v3/ipfs/gateway_plugins/${gatewayId}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${PINATA_JWT}`
    },
    body: data
  })
  ```

  ```json Response theme={null}
  {
    "data": {
      "gateway_id": "8673cd80-bf53-4bca-b684-bec1d6bdf004",
      "plugin_id": 1
    }
  }
  ```
</CodeGroup>

You can confirm the plugin is installed by using [/ipfs/gateway\_plugins/:gateway\_id](/api-reference/endpoint/ipfs/list-installed-plugins-for-gateway)

<CodeGroup>
  ```typescript Get Plugins for Gateway theme={null}
  const gatewayId = "8673cd80-bf53-4bca-b684-bec1d6bdf004"
  const installPlugin = await fetch(`https://api.pinata.cloud/v3/ipfs/gateway_plugins/${gatewayId}`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${PINATA_JWT}`
    }
  })
  ```

  ```json Response theme={null}
  {
    "data": {
      "gateway_id": "8673cd80-bf53-4bca-b684-bec1d6bdf004",
      "plugin_id": 1
    }
  }
  ```
</CodeGroup>

## Using Plugins

Each plugin has its own unique use case and usage, please see the appropriate links for each one to see how they are used.

[Content Addressable Plugin](/gateways/plugins/content-addressable)

## Uninstalling Plugins

Just like installing, removing a plugin can be done through the Pinata App or the Pinata API.

### Pinata App

To unintall a plugin first navigate to the Plugin Marketplace tab and then select the "My Plugins" tab.

<Frame>
  <img />
</Frame>

Then locate the target gateway and plugin, then click the action item on the right hand side and select "Uninstall" from the dropdown menu.

<Frame>
  <img />
</Frame>

### Pinata API

To uninstall a plug from the API you can use the [/ipfs/gateway\_plugins/:gateway\_id/plugin/:plugin\_id](/api-reference/endpoint/ipfs/uninstall-gateway-plugin) endpoint, where the `gateway_id` is the target gateway and the `plugin_id` is the target plugin to uninstall.

```typescript Install Plugin theme={null}
const gatewayId = "8673cd80-bf53-4bca-b684-bec1d6bdf004"
const pluginId = 1
const uninstallPlugin = await fetch(`https://api.pinata.cloud/v3/ipfs/gateway_plugins/${gatewayId}/plugin/${pluginId}`, {
  method: "DELETE",
  headers: {
    "Content-Type": "application/json",
    Authorization: `Bearer ${PINATA_JWT}`
  }
})
```


# Hot Swaps
Source: https://docs.pinata.cloud/gateways/plugins/hot-swaps

Use the Hot Swaps plugin to make one CID map to another

The Hot Swaps plugin can be used to "redirect" a CID to another CID. This can be useful when you need to replace content without updaing the CID hash.

While it may seem like this undermines the benefits of IPFS' imutable content system, it should be made clear that this only works on a per gateway level for those who install it. Additionally:

* Any CID can be called by another gateway to view the original content
* Pinata has an [SDK method](/sdk/files/public/get-swap-history) and [API endpoint](/api-reference/endpoint/get-swap-history) that any Pinata user can call to check the history of a swap
* All gateway requests that have the hot swap plugin installed and are serving a swapped CID will have a header of `etag` that will have the CID that is currently being directed to.

To demonstrate how this plugin works, consider the following example:

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example.mypinata.cloud", // Gateway has Hot Swaps installed
});

async function main() {
  try {
    // Upload the first file
    const file = new File(["The original CID"], "cid.txt", {
      type: "text/plain",
    });
    const { IpfsHash: CID1 } = await pinata.upload.public.file(file);
    console.log("This is the original CID hash: ", CID1);

    // Upload a second file
    const file2 = new File(["The new CID"], "cid.txt", { type: "text/plain" });
    const { IpfsHash: CID2 } = await pinata.upload.public.file(file2);
    console.log("This is the new CID hash: ", CID2);

    // Create the swap, so when we visit CID1 we will get the content of CID2
    const swap = await pinata.files.public.addSwap({
      cid: CID1,
      swapCid: CID2,
    });
    console.log("Swap created: ", swap);

    // Fetch CID1 through our gateway that has Hot Swaps installed, get the content of CID2
    const data = await pinata.gateways.public.get(CID1);
    console.log("Result of requestingt CID1 through the gateway: ", data);
  } catch (error) {
    console.log(error);
  }
}

main();
```

## Installation

Follow the steps in the [Getting Started](/gateways/plugins/getting-started) guide to install the Hot Swaps Plugin.

## Usage

After installing the plugin you can then make CID swaps and have them reflect when making Gateway requests. The first parameter `cid` will be the original CID, and `swapCid` will be the content you want it to point to instead.

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const swap = await pinata.files.public.addSwap({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  swapCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu"
})
```

You can fetch the history of CID swaps using the `swapHistory` method, passing in the `cid` of the original CID and the `domain` of the gateway that has the Hot Swaps plugin installed.

```typescript theme={null}
const history = await pinata.files.public.getSwapHistory({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  domain: "discordpinnie.mypinata.cloud"
})

// [
//   {
//     mappedCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu",
//     createdAt: "2024-08-19T14:34:46.492432Z"
//   },
//   { mappedCid: null, createdAt: "2024-08-19T14:25:10.208726Z" },
//   {
//     mappedCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu",
//     createdAt: "2024-08-19T00:23:41.755206Z"
//   }
// ]
```

To delete a CID swap you can simply use the `deleteSwap` method and pass in the CID.

```typescript theme={null}
const deleteSwap = await pinata.files.public.deleteSwap(
  "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske"
)
// OK
```


# Retrieving Files
Source: https://docs.pinata.cloud/gateways/retrieving-files



Gateways are Pinata's tool to deliver your content with speed and security. They're similar to CDNs but with way more features. When you create a Pinata account, you'll automatically have a Gateway created for you! To see it, simply visit the [Gateways Page](https://app.pinata.cloud/gateway).

<img />

The gateway domains are randomly generated and might look something like this:

```
aquamarine-casual-tarantula-177.mypinata.cloud
```

## Retrieving Public Files

If you uploaded or added files to Public IPFS then you can access them with the methods mentioned previously, or just by appending the `cid` to the `gateway` url like so:

```
https://example-gateway.mypinata.cloud/ipfs/{cid}
```

Since these files are public there is no need create a temporary url. At this point you can also use some handy queries such as `?filename=image.png`, `?download=true`.

<Tip>
  By default your gateway will only be able to fetch the files that are pinned to your account. If you want to open your gateway to access any file on IPFS check out our guide for [Access Controls](/gateways/gateway-access-controls).
</Tip>

One of the simplest ways to fetch content is through the [get](/sdk/gateways/private/get) method in the [SDK](/sdk). All content is referenced by the `cid`, a special identifier given to each file based on the cotnent of that file.

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const { data, contentType } = await pinata.gateways.public.get(
  "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq"
)
```

You can also use the SDK to provide a URL for your file using the `pinataGateway` in the config.

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const url = await pinata.gateways.public.convert(
  "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq"
)
```

### Image Optimizations

With public files you can simply append the [Image Optimizations](/gateways/image-optimizations) queries which would look something like this:

```
https://example-gateway.mypinata.cloud/files/{cid}?img-width=500&img-height=500
```

## Adding a Custom Domain

Pinata also allows you to create a custom domain for your Dedicated Gateway. Simply visit the [Gateways Page](https://app.pinata.cloud/gateway), click the menu button on the right side of your gateway, then click Add Custom Domain. You'll need to own the domain you want to use. When you enter your domain, you will be prompted to enter DNS information through your registrar.

## Retrieving Private Files

All content uploaded with Private IPFS is by default private, and there are a few ways you can view it. One of the simplest ways to fetch content is through the [get](/sdk/gateways/private/get) method in the [SDK](/sdk). All content is referenced by the `cid`, a special identifier given to each file based on the cotnent of that file.

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const { data, contentType } = await pinata.gateways.private.get(
  "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq"
)
```

Under the hood this method generates a 30 second access link to access the content with. Alternatively you can also create an access link that can be used to access the content for a specified limited amount of time.

<CodeGroup>
  ```typescript SDK {8-11} theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  const url = await pinata.gateways.private.createAccessLink({
  	cid: "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq",
  	expires: 30, // Number of seconds link is valid for
  });
  ```

  ```typescript API {5-10} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function url() {
    try {
      const payload = JSON.stringify({
        url: "https://example.mypinata.cloud/files/bafybeifq444z4b7yqzcyz4a5gspb2rpyfcdxp3mrfpigmllh52ld5tyzwm",
        expires: 500000,
        date: 1724875300,
        method: "GET"
      })

      const request = await fetch(
        `https://api.pinata.cloud/v3/files/download_link`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${JWT}`,
        },
        body: payload
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

### Image Optmizations

In order ot use [Image Optmizations](/gateways/image-optimizations) with private files the query parameters must be part of the request of getting a signed url.

<CodeGroup>
  ```typescript SDK {3-7} theme={null}
  const data = await pinata.gateways.private
    .createSignedURL("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
    .optimizeImage({
      width: 500,
      height: 500,
      format: "webp"
    })
  ```

  ```typescript API {6} theme={null}
  const JWT = "YOUR_PINATA_JWT";

  async function url() {
    try {
      const payload = JSON.stringify({
        url: "https://example.mypinata.cloud/files/bafybeifq444z4b7yqzcyz4a5gspb2rpyfcdxp3mrfpigmllh52ld5tyzwm?img-width=500&img-height=500&img-format=webp",
        expires: 500000,
        date: 1724875300,
        method: "GET"
      })

      const request = await fetch(
        `https://api.pinata.cloud/v3/files/download_link`,
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${JWT}`,
        },
        body: payload
      });
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>


# How does IPFS work with NFTs?
Source: https://docs.pinata.cloud/ipfs-101/how-does-ipfs-work-with-nfts



Pinata has been empowering the NFT space since 2018 and there's a good reason for that. IPFS is the perfect pairing for NFTs for several reasons.

* **IPFS is Immutable** - Anything that is uploaded to IPFS cannot change, which helps preserve the value of an NFT.
* **IPFS is Decentralized** - Instead of using a centralized server where one person can control the content, IPFS is distributed and makes sure anyone can pin the content and keep it persisted.
* **IPFS is Portable** - Since the [CID](/ipfs-101/what-are-cids) for content will be constant, and IPFS pinning works in a decentralized manner, anyone can take a CID and pin it themselves. This allows content to be "transferred" and kept up on the network as people value it. (read more about that concept [here](https://medium.com/pinata/who-is-responsible-for-nft-data-99fb4e8147e4))

One of the biggest reasons you want to use IPFS for NFTs is to prevent tampering or "rug pulls" where someone can just delete the data for an NFT and make it worthless. NFTs are tokens on the blockchain that have a "Token URI" which is simply a link pointing to data about that NFT off-chain, because putting data on-chain is far too expensive. If this link is a centralized server, like `https://server.com/pinnie.png`, then whoever has control of the server can simply upload totally different content and keep the same name, thus keeping the same link. Or they could just delete it and it would be empty!

<img />

This is where IPFS becomes necessary. Since the address or link to the content on IPFS is the [CID](/ipfs-101/what-are-cids), which is based on the content itself and is immutable, you can't change it or alter it. In addition, the ability for multiple people to [pin](/ipfs-101/what-is-ipfs-pinning) content and help it persist on the network makes it harder for something to just be deleted.

## How to Make an NFT with Pinata

It's important to note that Pinata is currently not providing any minting services. This means you would use Pinata to host the media content and the metadata for the NFT, and then another service or self-deployed smart contract to actually mint the NFT. But don't worry, we'll show you a few different ways you could do that!

### Step 1: Upload the Content

The first thing you need to do is upload the content to Pinata. Since IPFS supports any kind of file, the truth is any kind of file can be an NFT. How that file is referenced in the metadata is a bit of a different story, so be sure to check [metadata standards](https://docs.opensea.io/docs/metadata-standards) to make sure you content will be seen on marketplaces or wallets.

To upload the content you can either do a simple upload through the Pinata App by navigating to the [files page](https://app.pinata.cloud/ipfs/files) and uploading through the UI like so:

<img />

Or you can upload through the [SDK](/sdk) using a script like this:

```typescript theme={null}
const { PinataSDK } = require("pinata")
const fs = require("fs")
const { Blob } = require("buffer")

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud"
})

async function upload(){
  try {
    const blob = new Blob([fs.readFileSync("./path/to/image.png")]);
    const file = new File([blob], "image.png", { type: "image/png"})
    const upload = await pinata.upload.file(file);
    console.log(upload)
  } catch (error) {
    console.log(error)
  }
}
```

In each case you will want to grab the CID for that file, which will look something like this:

<img />

### Step 2: Create and Upload Metadata

Now that we have the CID for our content on IPFS, we need to create a metadata file that will have all the other information about the NFT. You will want to use a JSON format and follow [industry metadata standards](https://docs.opensea.io/docs/metadata-standards) to make sure that it will show up in marketplaces and wallets. You can use the template below as we'll walk through each piece.

```json metadata.json theme={null}
{
  "name": "Name of NFT",
  "description": "Description of NFT",
  "external_url": "https://pinata.cloud",
  "image": "ipfs://CID_GOES_HERE"
}
```

* `name` - This will be the name of this particular NFT, not the collection.
* `description` - Describes the NFT.
* `external_url` - A link to the website of the NFT project or creator.
* `image` - This would be the link to the image, if it was a video or gif then you would want to follow metadata standards and have a backup image, and also add an `animation_url` for the video.

You'll notice that we are using the IPFS protocol URL for the image link. There are other ways to reference CIDs in NFT metadata which you can read about more [here]().

<img />

Once you have that file filled out you will want to save it as something like `metadata.json` (this might be different if you are making a large project using folders). Then you can upload the metadata file to Pinata using the app like before, or if you are using the API we have a [JSON endpoint](/api-reference/endpoint/ipfs/pin-json-to-ipfs) you can use to simplify the process, like so:

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const upload = await pinata.upload.json({
  name: "Pinnie NFT",
  description: "A Pinnie NFT from Pinata",
  image: "ipfs://bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4",
  external_url: "https://pinata.cloud"
})
```

After the metadata is uploaded you should now have a CID for that metadata file; this will be the core identity of your NFT and will act as the **Token URI**.

### Step 3: Mint the NFT

Now that you have the all important Token URI metadata CID, you can mint an NFT! How you go about doing this will depend on multiple factors.

#### Starting an NFT Project

If you are non-technical and you're just looking for the easy way to create an NFT project, you will likely want to use a minting service like [Bueno](https://bueno.art), [Mintplex.xyz](https://mintplex.xyz), or [Manifold](https://manifold.xyz). There are a lot of complexities with smart contracts and making sure the content is setup properly, and using a service like this will make things much easier!

#### Just Exploring NFTs

If you want to get your feet wet with smart contracts you could follow the video below! It covers the Base layer 2 blockchain in particular, but the method will work on other EVM chains.

<iframe title="YouTube video player" />

#### Implementing into an Decentralized App

If you are a developer that is trying to do NFT minting on a larger scale, you could use an NFT minting API like [Crossmint](https://crossmint.com). Lucky for you we have some tutorials on how to do just that!

<iframe title="YouTube video player" />


# What are CIDs?
Source: https://docs.pinata.cloud/ipfs-101/what-are-cids



Content Identifiers (CIDs) are one of the most important parts of IPFS. Whenever you share a file through IPFS, that file or folder gets assigned a CID that looks like this:

<img />

What's happening behind the scenes: IPFS is breaking the file into blocks and running it through a cryptographic hash. It's like a math equation, where if you had `x + 2 = y`, and then you pass in `x = 2`, then `y = 4`. No matter how many times you run it, you will have the same answer if you keep passing in `x = 2`. In the same way,  IPFS creates CIDs for files that are reproducible. If you share a file of `Pinnie.png` you will get the same CID every time. It is through this CID that content is fetched across the IPFS network, which each piece pointing to a blocks on different nodes, altogether building a cohesive piece of content.

<Note>The CID is determined by the content of the file or folder</Note>

Files can be retrieved either with a local IPFS node using a URL like `ipfs://{CID}` or if you don't have an IPFS node, you can use an [IPFS Gateway](/ipfs-101/what-are-ipfs-gateways) like `https://ipfs.io/ipfs/{CID}`. This simple concept of CIDs give them several super powers.

### Verifiability

The CID's uniqueness and dependence on the content it represents make the data inherently verifiable. Suppose a creator shares an image of a digital artwork on the IPFS network: if someone tries to replace the original image with a different one, the CID for the new image will be different. This guarantees that the content cannot be tampered with, reinforcing trust within the network.

### Portability and Addressability

CIDs also facilitate data portability. Because a CID represents the content itself rather than its location, you can move your data across various nodes within the IPFS network without losing access to it. This content-addressed system breaks away from the traditional location-based addressing used in systems like HTTP, leading to a more robust and reliable data sharing network.

### Ownership and Persistence

The CID's capabilities don't stop at verification and portability. They also empower users to take ownership of data they care about. By 'pinning' a CID to a pinning service or their own node, users can ensure the longevity of data, even if the original data owner stops hosting it. This is particularly valuable in the context of non-fungible tokens (NFTs). For instance, if you purchase an NFT, you can pin the CID of the token's metadata and image to a pinning service or a node you control, securing its existence indefinitely. This practice truly underlines the principle of digital ownership.

### Community Preservation

In addition to ownership and persistence, communities can preserve digital content through the practice of pinning much like how traditional art is preserved in museums. CIDs provide an opportunity for groups to maintain access to valuable data, ensuring its longevity.

## V0 & V1

There are two different types of CIDs you might see while using IPFS. The first is V0, which looks something like this:

`QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng`

This was the first kind of IPFS CID that was used for several years, however over time a new version was developed called the V1. This version was more flexible and future proof, and looks something like this:

`bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4`

Both of these CIDs are the same content, a wonderful picture of Pinnie, however the cryptographic algorithm they were put through was different. Pinata has used the V0 for several years but now uses V1 for the previously mentioned reasons.

## How Do I Reference CIDs?

When it comes to providing an IPFS link, there are a few options to choose from.

### IPFS Protocol URL

An IPFS protocol URL looks like this:

<img />

If you copy and paste that into your browser, you may not get anything back. That is because in order to use this one, you have to have a local IPFS node running to participate in the network. Even when you do, it will likely be very very slow since IPFS is still a growing network.

Why use it? Well for a couple of reasons. If you are building on a blockchain that already uses IPFS a lot, like Ethereum or another L2 chain, lots of marketplaces and apps are used to seeing this format. When they see it, they use tools to convert the url into a gateway url so it can display the content on a website. This can be a good thing or a bad thing. If the platform has a dedicated/private gateway, the speed will be very fast (much like our own dedicated gateways). However, if the platform uses a public gateway, the speeds will be very slow. In the end, the platform has control over how well your content is received. Additionally, using the standard IPFS url might help future proof your assets, as public gateways might be stopped down the road (however the CID is still in the url in those cases, so if the platform knows what to do, they can still get the content if pinned).

If you are on a different L1 chain, you may want to test it first.. There are some platforms on other blockchains that expect "https" instead and nothing will load if you use this.

### Public IPFS Gateway URL

A public gateway URL looks something like this:

<img />

This will deliver the content in the browser without the need of a local IPFS node. However, since this gateway is a public gateway, your speed might vary due to the heavy traffic and congestion. Some platforms will see this kind of the url and switch it out with their own faster gateway choice, but not always. Generally you want to assume that if you take this path, the assets will be slow.

### Dedicated IPFS Gateway URL

A [Dedicated Gateway](/gateways/dedicated-ipfs-gateways) URL looks something like this:

<img />

Dedicated Gateways are much much faster than any other method, and should ideally be used when trying to display content on your own platform. However, using them in NFTs should be done in caution. If you use a Dedicated Gateway in your NFT project metadata and image links, your speed will be great, however anytime another marketplace or rarity bot asks the blockchain for the IPFS data, your gateway will be hit. Since most Dedicated Gateways are paid services, this could greatly drive up your costs and usage. You'll get the best performance, control, and flexibility with this method, however you might have to pay more than the other methods.


# What are IPFS Gateways?
Source: https://docs.pinata.cloud/ipfs-101/what-are-ipfs-gateways



Once you have uploaded content to Pinata, naturally the first thing you want to do is view it on the IPFS network! But there's a problem: IPFS is a separate protocol, just like HTTP for regular websites is a protocol. To access that content, we need a gateway to bridge IPFS and HTTP. IPFS gateways help us do exactly that!

An example of accessing content from this gateway can be seen with: `https://ipfs.io/ipfs/bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4`

What's going on here exactly? Let's break it down. First you have the gateway domain. There are lots of different domains out there, like `ipfs.io`, and if you have a Pinata account you get a Dedicated Gateway which might look something like `aquamarine-casual-tarantula-177.mypinata.cloud`. Each of these can be used to bridge files from IPFS to HTTPs. Next you have the IPFS path which looks like `ipfs/` and this is necessary for a gateway to work. Finally we have the CID at the end, which is the actual IPFS address for our content.

<img />

## Folder Paths

Sometimes your CID might be a folder, in which case you might have difficulty loading it through the gateway. This happens because if you do not designate a complete folder path, then the gateway will try to load all of the files and index them into a sheet showing every file. This can be pretty intensive depending what kind of gateway you're using, and will likely stall out due to how long it can take. To remedy this, simply add on the file path of the content you're trying to get inside. For instance, if we have a folder with the CID of `QmWfHgs3nKiyFWx3tFEYvm8DiHTrCsxEHxvDdBh95ZQSLT` and the inside looks something like this:

<img />

Then we could access the files inside by adding on `/pinnie.png` or `clouds.json` to the end of our folder path. In the end we would have something like this.

<img />

## Public Gateways

The most common kind of IPFS Gateways are Public Gateways. These are usually run and maintained by IPFS Pinning Services, protocols, or even smaller groups that want to help build the IPFS ecosystem. They're referred to as "Public" because anyone can access them! You just have to add a CID to the end of one to start using it. You can try that now by adding this CID `bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4` to the end of a Public Gateway:

```text theme={null}
https://ipfs.io/ipfs/
```

There's something you might notice when you start using Public Gateways frequently, and that is the speed and rate limits. Since these are Public, they're used **heavily** by people all around the world. They are constantly getting hammered, and because of that they're just naturally slower. You can think of it like a highway or interstate: if you have a high flow of traffic, its likely going to bottleneck and cause a traffic jam. Same goes for IPFS Gateways!

<Warning>Public Gateways are not meant for production apps, be sure to only use them for testing!</Warning>

## [Dedicated Gateways](/gateways/dedicated-ipfs-gateways)

Thankfully Pinata has you covered! When you sign up for a free Pinata account, you get your own Dedicated Gateway. Dedicated Gateways are like the toll roads on highways and interstates; it's your own private boulevard to get unmatched speeds. Our Dedicated Gateways are well known in the industry as being fast, reliable, and just plain simple to use, and they do that through a large network of IPFS nodes and a built in global CDN that helps cache content to be much faster on subsequent loads. Check on the next few pages to learn more about how they work!


# What is IPFS?
Source: https://docs.pinata.cloud/ipfs-101/what-is-ipfs



[IPFS](https://ipfs.io) (Inter-Planetary File System) is a peer-to-peer distributed file system that is used primarily for data that can't be stored on a blockchain. Unlike HTTP, a more standard file sharing protocol, IPFS has special properties that make it ideal for a decentralized data model that works in tandem with blockchains. Some of those abilities include:

* **Distributed** - IPFS is made of multiple IPFS nodes, so not one entity can control what is shared on the network.
* **Immutability** - Content that is shared on IPFS cannot be changed or altered.
* **Addressability** - Content that is shared on IPFS uses unique addresses to locate content on the network.
* **Portability** - Data that is pinned to IPFS can be re-pinned or transferred to other nodes, helping valued content persevere on the network.
* **Garbage Collection** -  The way IPFS handles data works in such a way that any content that is not pinned by a node will eventually fall off the network, keeping it clean from unwanted data and clutter.

Due to these properties it is ideal for Web3 data storage such as NFTs, DeFi, and other decentralized infrastructures.

## How Does IPFS Work?

The best way to understand IPFS is to see it as an alternative to HTTP. With HTTP server model the end user has a computer which makes a request to see content from a server, then that server sends back the requested content. This is a simple two way communication, and while there are more complex instances, the key is that the data is stored on the server and has ultimate control of that content.

<img />

IPFS on the other hand, is a network is made up of a multitude of different IPFS nodes which share data with each other. Whenever a node wants to share content on IPFS, it runs the content through a cryptographic hash and returns a [CID](/ipfs-101/what-are-cids), or "Content Identifier." This CID serves as both the address and the verification that the content is what it says it is. After the CID has been created the IPFS node will "pin" that content to the network, essentially sharing it and saying it is worth keeping.

<img />

As the CID is requested by other IPFS nodes, the content will pass through other nodes leaving a cache that can be used for faster retrieval the more it is requested. This cache will eventually get pretty big and can cause bloat, and this is where pinning really comes into play. The IPFS node will run a garbage collector from time to time which will clear the contents of the cache, except for any CIDs that are actively being pinned by another IPFS node. As long as one IPFS node is pinning that content, it will stay on the network. If the content is unpinned and there is no other node holding it, eventually the content will fade from the network. This creates a model that can persevere data but not to a point that will cause clutter and bloat.

## Why IPFS?

Blockchains have an incredible ability to keep a long ledger of transactions and who sends or signs them, however blockchains are terrible at storing data. Since blockchains require gas fees to be paid anytime data is stored on the blockchain, larger forms of data can cause astronomical prices. As of 2023, storing 1GB of data on Ethereum would cost around \$250,000,000! This caused a problem in particular for NFTs as they were first taking off.

NFTs, or really anything being used on the blockchain, will usually have a token element that is on chain that has a pointer to data off-chain (referred to as the token URI). This pointer is usually a link to a metadata file in the form of JSON, which has information like the name of the NFT, a description, and usually another link to an image that is also off-chain. Back in the earlier days of NFTs these pointers or token URIs were centralized servers, and that caused a problem. There was nothing stopping the owner of that server from changing the data to be something completely different. A link like `https://drive.google.com/nft/pinnie.png` could be dynamic; at any time the owner of that file could upload a picture of something else and name it `pinnie.png` and the link would still be the same. What was the point of buying a piece of art on the blockchain if it could change and be worthless?

<img />

This is where IPFS steps in, along with it's special abilities of cryptography and distributed nature. Whenever a file is stored on IPFS, it gets a unique CID that is based on the content of the file. If the file is changed by a single pixel or character, then it will receive a completely different CID. It solves the problem of `pinnie.png` being replaced with something else since you couldn't simply just change the name. Due to the cryptographic nature of IPFS, anything shared on IPFS is immutable and cannot be changed.

<img />

Since IPFS is decentralized in the way it stores the data, it also solved the potential crisis of something deleting the data or the server going offline. With IPFS pinning, multiple nodes can pin data to ensure that it stays online. A good metaphor for this is a fridge. If you wanted to put a picture on a fridge, you would likely use a magnet to put it up there. If you have two or three magnets on that picture, you could remove the original magnet and the picture would stay up. IPFS works in a similar way; anyone can take the CID for some content and pin it themselves to help preserve it. Content can persist as long as a single IPFS node is pinning it!

## What Does Pinata Do?

Pinata is an IPFS Pinning Service that provides user with, you guessed it, IPFS services! These range from uploading files and pinning them to IPFS, to blazing fast [Dedicated Gateways](/gateways/dedicated-ipfs-gateways) which come in handy if you need to fetch content from IPFS. Our focus is to provide developers easy to use tools so they can add in IPFS to their Web3 architecture as simply as possible, and to make it reliable and trustworthy. If you're not sure where to start, check out our [Getting Started](/quickstart) page which will have you up and running with Pinata in no time! 🚀

<iframe title="YouTube video player" />


# What is Pinning?
Source: https://docs.pinata.cloud/ipfs-101/what-is-ipfs-pinning



IPFS "Pinning" is the foundation to getting content on IPFS. When you upload a file to IPFS, the IPFS node will create a [CID](/ipfs-101/what-are-cids) for that file which will act as the identifier and the address. Then it will "pin" that file to the IPFS network, making it available for other nodes to request it. At that point any other IPFS node can request the content for a CID, and the content will pass through other nodes leaving a cache on that node. This makes it faster to fetch files again if those nodes are used.

<img />

As the cache on these nodes through, it will soon become bloated with too much data, similar to how your computer can get slow if it's loaded down with too many cache files. IPFS nodes have a way to handle this though, and that's through something called "Garbage Collection." This is a process where the IPFS node will dump any content in the cache that is not being pinned to IPFS. However if there is content in the cache that is still being pinned by at least one IPFS node, then it will stay. Pinning is what keeps content on IPFS, and as long as content is being pinned by one node, it will stay available on the network.

## How Do I Pin Files to IPFS?

With Pinata there are a few ways you can pin files to IPFS

### API & SDKs

If you're a developer that needs to build decentralized applications then you will likely want to use the [Pinata SDK](/sdk) or [Pinata API](/api-reference/endpoint/upload-a-file). These make it simple to upload files or raw JSON to IPFS!

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: "PINATA_JWT",
  pinataGateway: "example-gateway.mypinata.cloud",
});

const file = new File(["Hello IPFS!"], "hello-world.txt", { type: "text/plain" });
const upload = await pinata.upload.file(file);
```

<Note>
  Check out the [Quickstart](/quickstart) guide to upload your first file
  through the SDK!
</Note>

We also have other tools like the [Pinata CLI](/tools/ipfs-cli) or [Next.js Starter](/tools/nextjs-starter) which can be used to upload using [API Keys](/account-management/api-keys).

### Web App

If you're non-technical you can use [Pinata App](https://app.pinata.cloud/ipfs/files) to upload files, perfect if you just want to get started with NFTs and IPFS! It's as simple as clicking the "Add" button in the top right corner of the files page, selecting your file, give it a name, then upload. Once its complete, you'll see it listed in the files page!

<img />

<Note>
  Start uploading by [signing up for a free
  account](https://app.pinata.cloud/register)!
</Note>

### Pin by CID

Another way you can upload content to Pinata is by transferring content that is already on IPFS. This could be CIDs that are on your own local IPFS node or another IPFS pinning service! You can do this with the "Import from IPFS" button in the web app, like so:

<img />

Or you can pin by CID with our API using the [Pin By CID](/api-reference/endpoint/ipfs/pin-by-cid) endpoint with a code snippet like this:

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: "PINATA_JWT",
  pinataGateway: "example-gateway.mypinata.cloud",
});

const pin = await pinata.upload.cid("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
```


# LLM Docs
Source: https://docs.pinata.cloud/llm-docs



The Pinata Docs have multiple ways they can be used in LLMs or AI empowered code editors like Cursor or Zed. Both of these options return raw text that can be pasted into the LLM or used in a prompt/docs feature for an editor.

## Smaller Context

If you are concerned about context tokens then you will want to use our hand crafted [AI Docs](https://ai-docs.pinata.cloud)

```bash theme={null}
curl https://ai-docs.pinata.cloud
```

<iframe title="YouTube video player" />

<br />

<Card title="How to Use Pinata with Cursor, Zed, and other LLMs" href="https://pinata.cloud/blog/how-to-use-pinata-with-cursor-zed-and-other-llms/" />

## Larger Context

Pinata's docs also offer larger contexts if you prefer it. The standard route will return URL routes which make it easy for LLMs to crawl.

```bash Routes theme={null}
curl https://docs.pinata.cloud/llms.txt
```

If you prefer to pull all of the documentaiton you can use the route below.

```bash Full Docs theme={null}
curl https://docs.pinata.cloud/llms-full.txt
```


# Quickstart
Source: https://docs.pinata.cloud/quickstart

Start uploading and retrieving content in no time

<img />

## Getting Started with Pinata

Whether you're brand new or a seasoned developer, Pinata makes it simple to store and retrieve content with speed and security. All you need to kick off your journey is a [free Pinata account](https://app.pinata.cloud/register)!

<CardGroup>
  <Card title="Next.Js" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20width=%22800px%22%20height=%22800px%22%20class=%22h-6%20w-6%22%20viewBox=%220%200%20256%20256%22%20version=%221.1%22%20xmlns=%22http:/www.w3.org/2000/svg%22%20xmlns:xlink=%22http:/www.w3.org/1999/xlink%22%20preserveAspectRatio=%22xMidYMid%22%3E%3Cg%3E%3Cpath%20d=%22M119.616813,0.0688905149%20C119.066276,0.118932037%20117.314565,0.294077364%20115.738025,0.419181169%20C79.3775171,3.69690087%2045.3192571,23.3131775%2023.7481916,53.4631946%20C11.7364614,70.2271045%204.05395894,89.2428829%201.15112414,109.384595%20C0.12512219,116.415429%200,118.492153%200,128.025062%20C0,137.557972%200.12512219,139.634696%201.15112414,146.665529%20C8.10791789,194.730411%2042.3163245,235.11392%2088.7116325,250.076335%20C97.0197458,252.753556%20105.778299,254.580072%20115.738025,255.680985%20C119.616813,256.106338%20136.383187,256.106338%20140.261975,255.680985%20C157.453763,253.779407%20172.017986,249.525878%20186.382014,242.194795%20C188.584164,241.068861%20189.00958,240.768612%20188.709286,240.518404%20C188.509091,240.36828%20179.124927,227.782837%20167.86393,212.570214%20L147.393939,184.922273%20L121.743891,146.965779%20C107.630108,126.098464%2096.0187683,109.034305%2095.9186706,109.034305%20C95.8185728,109.009284%2095.7184751,125.873277%2095.6684262,146.465363%20C95.5933529,182.52028%2095.5683284,183.971484%2095.1178886,184.82219%20C94.4672532,186.048207%2093.9667644,186.548623%2092.915738,187.099079%20C92.114956,187.499411%2091.4142717,187.574474%2087.6355816,187.574474%20L83.3063539,187.574474%20L82.1552297,186.848872%20C81.4044966,186.373477%2080.8539589,185.747958%2080.4785924,185.022356%20L79.9530792,183.896422%20L80.0031281,133.729796%20L80.0782014,83.5381493%20L80.8539589,82.5623397%20C81.25435,82.0369037%2082.1051808,81.3613431%2082.7057674,81.0360732%20C83.7317693,80.535658%2084.1321603,80.4856165%2088.4613881,80.4856165%20C93.5663734,80.4856165%2094.4172043,80.6857826%2095.7434995,82.1369867%20C96.1188661,82.5373189%20110.007429,103.454675%20126.623656,128.650581%20C143.239883,153.846488%20165.962072,188.250034%20177.122972,205.139048%20L197.392766,235.839522%20L198.418768,235.163961%20C207.502639,229.259062%20217.112023,220.852086%20224.719453,212.09482%20C240.910264,193.504394%20251.345455,170.835585%20254.848876,146.665529%20C255.874878,139.634696%20256,137.557972%20256,128.025062%20C256,118.492153%20255.874878,116.415429%20254.848876,109.384595%20C247.892082,61.3197135%20213.683675,20.9362052%20167.288368,5.97379012%20C159.105376,3.32158945%20150.396872,1.49507389%20140.637341,0.394160408%20C138.234995,0.143952798%20121.693842,-0.131275573%20119.616813,0.0688905149%20L119.616813,0.0688905149%20Z%20M172.017986,77.4831252%20C173.219159,78.0836234%20174.195112,79.2345784%20174.545455,80.435575%20C174.74565,81.0861148%20174.795699,94.9976579%20174.74565,126.348671%20L174.670577,171.336%20L166.73783,159.17591%20L158.780059,147.01582%20L158.780059,114.313685%20C158.780059,93.1711423%20158.880156,81.2862808%20159.030303,80.7108033%20C159.430694,79.3096407%20160.306549,78.2087272%20161.507722,77.5581875%20C162.533724,77.0327515%20162.909091,76.98271%20166.837928,76.98271%20C170.541544,76.98271%20171.19218,77.0327515%20172.017986,77.4831252%20Z%22%3E%3C/path%3E%3C/g%3E%3C/svg%3E" href="/frameworks/next-js">
    Quickstart
  </Card>

  <Card title="Hono" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20xmlns=%22http:/www.w3.org/2000/svg%22%20class=%22h-6%20w-6%22%20width=%2224.83%22%20height=%2232%22%20viewBox=%220%200%20256%20330%22%3E%3Cpath%20fill=%22%23FF5B11%22%20d=%22M134.129.029q1.315-.17%202.319.662a1256%201256%200%200%201%2069.573%2093.427q24.141%2036.346%2041.082%2076.862q27.055%2072.162-28.16%20125.564q-48.313%2040.83-111.318%2031.805q-75.312-15.355-102.373-87.133Q-1.796%20217.85.614%20193.51q4.014-41.896%2019.878-80.838q6.61-15.888%2017.228-29.154a382%20382%200%200%201%2016.565%2021.203q3.66%203.825%207.62%207.289Q92.138%2052.013%20134.13.029%22%20opacity=%22.993%22/%3E%3Cpath%20fill=%22%23FF9758%22%20d=%22M129.49%2053.7q36.47%2042.3%2065.93%2090.114a187.3%20187.3%200%200%201%2015.24%2033.13q12.507%2049.206-26.836%2081.169q-38.05%2026.774-83.488%2015.902q-48.999-15.205-56.653-65.929q-1.857-15.993%203.314-31.142a225.4%20225.4%200%200%201%2017.89-35.78l19.878-29.155a5510%205510%200%200%200%2044.726-58.31%22/%3E%3C/svg%3E" href="/frameworks/hono">
    Quickstart
  </Card>

  <Card title="React" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20xmlns=%22http:/www.w3.org/2000/svg%22%20class=%22h-6%20w-6%22%20width=%2228%22%20height=%2232%22%20viewBox=%220%200%20256%20256%22%3E%3Cpath%20fill=%22%2300D8FF%22%20d=%22M210.483%2073.824a172%20172%200%200%200-8.24-2.597c.465-1.9.893-3.777%201.273-5.621c6.238-30.281%202.16-54.676-11.769-62.708c-13.355-7.7-35.196.329-57.254%2019.526a171%20171%200%200%200-6.375%205.848a156%20156%200%200%200-4.241-3.917C100.759%203.829%2077.587-4.822%2063.673%203.233C50.33%2010.957%2046.379%2033.89%2051.995%2062.588a171%20171%200%200%200%201.892%208.48c-3.28.932-6.445%201.924-9.474%202.98C17.309%2083.498%200%2098.307%200%20113.668c0%2015.865%2018.582%2031.778%2046.812%2041.427a146%20146%200%200%200%206.921%202.165a168%20168%200%200%200-2.01%209.138c-5.354%2028.2-1.173%2050.591%2012.134%2058.266c13.744%207.926%2036.812-.22%2059.273-19.855a146%20146%200%200%200%205.342-4.923a168%20168%200%200%200%206.92%206.314c21.758%2018.722%2043.246%2026.282%2056.54%2018.586c13.731-7.949%2018.194-32.003%2012.4-61.268a145%20145%200%200%200-1.535-6.842c1.62-.48%203.21-.974%204.76-1.488c29.348-9.723%2048.443-25.443%2048.443-41.52c0-15.417-17.868-30.326-45.517-39.844m-6.365%2070.984q-2.102.694-4.3%201.345c-3.24-10.257-7.612-21.163-12.963-32.432c5.106-11%209.31-21.767%2012.459-31.957c2.619.758%205.16%201.557%207.61%202.4c23.69%208.156%2038.14%2020.213%2038.14%2029.504c0%209.896-15.606%2022.743-40.946%2031.14m-10.514%2020.834c2.562%2012.94%202.927%2024.64%201.23%2033.787c-1.524%208.219-4.59%2013.698-8.382%2015.893c-8.067%204.67-25.32-1.4-43.927-17.412a157%20157%200%200%201-6.437-5.87c7.214-7.889%2014.423-17.06%2021.459-27.246c12.376-1.098%2024.068-2.894%2034.671-5.345q.785%203.162%201.386%206.193M87.276%20214.515c-7.882%202.783-14.16%202.863-17.955.675c-8.075-4.657-11.432-22.636-6.853-46.752a157%20157%200%200%201%201.869-8.499c10.486%202.32%2022.093%203.988%2034.498%204.994c7.084%209.967%2014.501%2019.128%2021.976%2027.15a135%20135%200%200%201-4.877%204.492c-9.933%208.682-19.886%2014.842-28.658%2017.94M50.35%20144.747c-12.483-4.267-22.792-9.812-29.858-15.863c-6.35-5.437-9.555-10.836-9.555-15.216c0-9.322%2013.897-21.212%2037.076-29.293c2.813-.98%205.757-1.905%208.812-2.773c3.204%2010.42%207.406%2021.315%2012.477%2032.332c-5.137%2011.18-9.399%2022.249-12.634%2032.792a135%20135%200%200%201-6.318-1.979m12.378-84.26c-4.811-24.587-1.616-43.134%206.425-47.789c8.564-4.958%2027.502%202.111%2047.463%2019.835a144%20144%200%200%201%203.841%203.545c-7.438%207.987-14.787%2017.08-21.808%2026.988c-12.04%201.116-23.565%202.908-34.161%205.309a160%20160%200%200%201-1.76-7.887m110.427%2027.268a348%20348%200%200%200-7.785-12.803c8.168%201.033%2015.994%202.404%2023.343%204.08c-2.206%207.072-4.956%2014.465-8.193%2022.045a381%20381%200%200%200-7.365-13.322m-45.032-43.861c5.044%205.465%2010.096%2011.566%2015.065%2018.186a322%20322%200%200%200-30.257-.006c4.974-6.559%2010.069-12.652%2015.192-18.18M82.802%2087.83a323%20323%200%200%200-7.227%2013.238c-3.184-7.553-5.909-14.98-8.134-22.152c7.304-1.634%2015.093-2.97%2023.209-3.984a322%20322%200%200%200-7.848%2012.897m8.081%2065.352c-8.385-.936-16.291-2.203-23.593-3.793c2.26-7.3%205.045-14.885%208.298-22.6a321%20321%200%200%200%207.257%2013.246c2.594%204.48%205.28%208.868%208.038%2013.147m37.542%2031.03c-5.184-5.592-10.354-11.779-15.403-18.433c4.902.192%209.899.29%2014.978.29c5.218%200%2010.376-.117%2015.453-.343c-4.985%206.774-10.018%2012.97-15.028%2018.486m52.198-57.817c3.422%207.8%206.306%2015.345%208.596%2022.52c-7.422%201.694-15.436%203.058-23.88%204.071a382%20382%200%200%200%207.859-13.026a347%20347%200%200%200%207.425-13.565m-16.898%208.101a359%20359%200%200%201-12.281%2019.815a329%20329%200%200%201-23.444.823c-7.967%200-15.716-.248-23.178-.732a310%20310%200%200%201-12.513-19.846h.001a307%20307%200%200%201-10.923-20.627a310%20310%200%200%201%2010.89-20.637l-.001.001a307%20307%200%200%201%2012.413-19.761c7.613-.576%2015.42-.876%2023.31-.876H128c7.926%200%2015.743.303%2023.354.883a329%20329%200%200%201%2012.335%2019.695a359%20359%200%200%201%2011.036%2020.54a330%20330%200%200%201-11%2020.722m22.56-122.124c8.572%204.944%2011.906%2024.881%206.52%2051.026q-.518%202.504-1.15%205.09c-10.622-2.452-22.155-4.275-34.23-5.408c-7.034-10.017-14.323-19.124-21.64-27.008a161%20161%200%200%201%205.888-5.4c18.9-16.447%2036.564-22.941%2044.612-18.3M128%2090.808c12.625%200%2022.86%2010.235%2022.86%2022.86s-10.235%2022.86-22.86%2022.86s-22.86-10.235-22.86-22.86s10.235-22.86%2022.86-22.86%22/%3E%3C/svg%3E" href="/frameworks/react">
    Quickstart
  </Card>

  <Card title="Svelte" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20class=%22h-6%20w-6%22%20xmlns=%22http:/www.w3.org/2000/svg%22%20width=%2226.6%22%20height=%2232%22%20viewBox=%220%200%20256%20308%22%3E%3Cpath%20fill=%22%23FF3E00%22%20d=%22M239.682%2040.707C211.113-.182%20154.69-12.301%20113.895%2013.69L42.247%2059.356a82.2%2082.2%200%200%200-37.135%2055.056a86.57%2086.57%200%200%200%208.536%2055.576a82.4%2082.4%200%200%200-12.296%2030.719a87.6%2087.6%200%200%200%2014.964%2066.244c28.574%2040.893%2084.997%2053.007%20125.787%2027.016l71.648-45.664a82.18%2082.18%200%200%200%2037.135-55.057a86.6%2086.6%200%200%200-8.53-55.577a82.4%2082.4%200%200%200%2012.29-30.718a87.57%2087.57%200%200%200-14.963-66.244%22/%3E%3Cpath%20fill=%22%23FFF%22%20d=%22M106.889%20270.841c-23.102%206.007-47.497-3.036-61.103-22.648a52.7%2052.7%200%200%201-9.003-39.85a50%2050%200%200%201%201.713-6.693l1.35-4.115l3.671%202.697a92.5%2092.5%200%200%200%2028.036%2014.007l2.663.808l-.245%202.659a16.07%2016.07%200%200%200%202.89%2010.656a17.14%2017.14%200%200%200%2018.397%206.828a15.8%2015.8%200%200%200%204.403-1.935l71.67-45.672a14.92%2014.92%200%200%200%206.734-9.977a15.92%2015.92%200%200%200-2.713-12.011a17.16%2017.16%200%200%200-18.404-6.832a15.8%2015.8%200%200%200-4.396%201.933l-27.35%2017.434a52.3%2052.3%200%200%201-14.553%206.391c-23.101%206.007-47.497-3.036-61.101-22.649a52.68%2052.68%200%200%201-9.004-39.849a49.43%2049.43%200%200%201%2022.34-33.114l71.664-45.677a52.2%2052.2%200%200%201%2014.563-6.398c23.101-6.007%2047.497%203.036%2061.101%2022.648a52.7%2052.7%200%200%201%209.004%2039.85a51%2051%200%200%201-1.713%206.692l-1.35%204.116l-3.67-2.693a92.4%2092.4%200%200%200-28.037-14.013l-2.664-.809l.246-2.658a16.1%2016.1%200%200%200-2.89-10.656a17.14%2017.14%200%200%200-18.398-6.828a15.8%2015.8%200%200%200-4.402%201.935l-71.67%2045.674a14.9%2014.9%200%200%200-6.73%209.975a15.9%2015.9%200%200%200%202.709%2012.012a17.16%2017.16%200%200%200%2018.404%206.832a15.8%2015.8%200%200%200%204.402-1.935l27.345-17.427a52.2%2052.2%200%200%201%2014.552-6.397c23.101-6.006%2047.497%203.037%2061.102%2022.65a52.68%2052.68%200%200%201%209.003%2039.848a49.45%2049.45%200%200%201-22.34%2033.12l-71.664%2045.673a52.2%2052.2%200%200%201-14.563%206.398%22/%3E%3C/svg%3E" href="/frameworks/sveltekit">
    Quickstart
  </Card>

  <Card title="Astro" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20class=%22h-7%20w-7%22%20xmlns=%22http:/www.w3.org/2000/svg%22%20width=%2232%22%20height=%2232%22%20viewBox=%220%200%2032%2032%22%3E%3Cpath%20fill=%22url(%23vscodeIconsFileTypeAstro0)%22%20d=%22M11.025%2020.499c-.532%201.75-.154%204.184%201.105%205.331v-.042l.042-.112c.154-.741.756-1.203%201.526-1.175c.713.014%201.12.392%201.217%201.217c.042.308.042.616.056.938v.098c0%20.7.196%201.371.588%201.959c.35.56.84.993%201.497%201.287l-.028-.056l-.028-.112c-.49-1.469-.14-2.49%201.147-3.358l.392-.266l.868-.573a4.25%204.25%200%200%200%201.791-3.037c.07-.532%200-1.05-.154-1.553l-.21.14c-1.945%201.035-4.17%201.4-6.325.98c-1.301-.197-2.56-.56-3.498-1.652z%22/%3E%3Cpath%20fill=%22%23fff%22%20d=%22M4.925%2020.191s3.736-1.82%207.486-1.82l2.84-8.759c.098-.42.406-.7.756-.7s.644.28.756.714l2.826%208.746c4.45%200%207.487%201.82%207.487%201.82L20.709%202.84c-.168-.518-.49-.84-.896-.84h-7.612c-.406%200-.7.322-.896.84z%22/%3E%3Cdefs%3E%3ClinearGradient%20id=%22vscodeIconsFileTypeAstro0%22%20x1=%228.19%22%20x2=%2216.91%22%20y1=%2223%22%20y2=%2218.89%22%20gradientTransform=%22translate(-.673%20-2.198)scale(1.3993)%22%20gradientUnits=%22userSpaceOnUse%22%3E%3Cstop%20offset=%220%22%20stop-color=%22%23D83333%22/%3E%3Cstop%20offset=%221%22%20stop-color=%22%23F041FF%22/%3E%3C/linearGradient%3E%3C/defs%3E%3C/svg%3E" href="/frameworks/astro">
    Quickstart
  </Card>

  <Card title="Remix" icon="https://mintlify.s3.us-west-1.amazonaws.com/pinata/%3Csvg%20class=%22h-6%20w-6%22%20xmlns=%22http:/www.w3.org/2000/svg%22%20width=%2232%22%20height=%2232%22%20viewBox=%220%200%2024%2024%22%3E%3Cpath%20fill=%22%23888888%22%20d=%22M21.511%2018.508c.216%202.773.216%204.073.216%205.492H15.31c0-.309.006-.592.011-.878c.018-.892.036-1.821-.109-3.698c-.19-2.747-1.374-3.358-3.55-3.358H1.574v-5H11.97c2.748%200%204.122-.835%204.122-3.049c0-1.946-1.374-3.125-4.122-3.125H1.573V0h11.541c6.221%200%209.313%202.938%209.313%207.632c0%203.511-2.176%205.8-5.114%206.182c2.48.497%203.93%201.909%204.198%204.694M1.573%2024v-3.727h6.784c1.133%200%201.379.84%201.379%201.342V24Z%22/%3E%3C/svg%3E" href="/frameworks/remix">
    Quickstart
  </Card>
</CardGroup>

### 1. Get API key and Gateway URL

<img />

Inside the [Pinata App](https://app.pinata.cloud) select "API Keys" from the sidebar, then click "New Key" in the top right. We would recommend starting with Admin privileges and unlimited uses to start. You will receive a `pinata_api_key`, `pinata_api_secret`, and a `JWT`. The JWT is the most common authentication method and what we'll be using below.

Next you will want to grab your Gateway domain by clicking the Gateways tab in the sidebar. You should see it listed in the format `fun-llama-300.mypinata.cloud` and you will want to copy it exactly like that.

### 2. Install and Setup SDK

In the root of your project run the install command with your package manager of choice.

<CodeGroup>
  ```bash npm theme={null}
  npm i pinata
  ```

  ```bash pnpm theme={null}
  pnpm i pinata
  ```

  ```bash yarn theme={null}
  yarn add pinata
  ```

  ```bash bun theme={null}
  bun i pinata
  ```
</CodeGroup>

Import and initialize the SDK in your codebase with the API key and Gateway from the previous step

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: "PINATA_JWT",
  pinataGateway: "example-gateway.mypinata.cloud",
});
```

<Note>
  The `PINATA_JWT` is a secret key, be sure to initialize the SDK in a secure environment and practice basic variable security practices. If you need to upload from a client environment, consider using signed JWTs
</Note>

### 3. Upload a File

Use the `upload` method to upload a File object.

<CodeGroup>
  ```typescript SDK theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  async function main() {
    try {
      const file = new File(["hello world!"], "hello.txt", { type: "text/plain" });
      const upload = await pinata.upload.public.file(file);
      console.log(upload);
    } catch (error) {
      console.log(error);
    }
  }

  await main();
  ```

  ```typescript API theme={null}
  const JWT = "PINATA_JWT";

  async function uploadFile() {
    try {
      const text = "hello world!";
      const blob = new Blob([text], { type: "text/plain" });
      const file = new File([blob], "hello.txt");
      const data = new FormData();
      data.append("file", file);
      data.append("network", "public")

      const request = await fetch(
        "https://uploads.pinata.cloud/v3/files",
        {
          method: "POST",
          headers: {
            Authorization: `Bearer ${JWT}`,
          },
          body: data,
        }
      );
      const response = await request.json();
      console.log(response);
    } catch (error) {
      console.log(error);
    }
  }
  ```
</CodeGroup>

You should get a response object like the one below

<CodeGroup>
  ```typescript SDK theme={null}
  {
    id: "0195f815-5c5e-716d-9240-d3ae380e2002",
    group_id: null,
    name: "hello.txt",
    cid: "bafkreidvbhs33ighmljlvr7zbv2ywwzcmp5adtf4kqvlly67cy56bdtmve",
    created_at: "2025-04-02T19:58:24.616Z",
    size: 12,
    number_of_files: 1,
    mime_type: "text/plain",
    vectorized: false,
    network: "public",
  }
  ```

  ```typescript API theme={null}
  {
    data: {
      id: "0195f815-5c5e-716d-9240-d3ae380e2002",
      group_id: null,
      name: "hello.txt",
      cid: "bafkreidvbhs33ighmljlvr7zbv2ywwzcmp5adtf4kqvlly67cy56bdtmve",
      created_at: "2025-04-02T19:58:24.616Z",
      size: 12,
      number_of_files: 1,
      mime_type: "text/plain",
      vectorized: false,
      network: "public",
    }
  }
  ```
</CodeGroup>

### 4. Retrieve a File through a Gateway

Use the `cid` of a file to fetch it through a Gateway directly or create a URL

<CodeGroup>
  ```typescript SDK theme={null}
  import { PinataSDK } from "pinata";

  const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
  });

  async function main() {
    try {
      const data = await pinata.gateways.public.get("bafkreibm6jg3ux5qumhcn2b3flc3tyu6dmlb4xa7u5bf44yegnrjhc4yeq");
      console.log(data)

      const url = await pinata.gateways.convert(
        "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq"
      )
      console.log(url)
    } catch (error) {
      console.log(error);
    }
  }

  main();
  ```

  ```typescript API theme={null}
  const gatewayDomain = "example-llama-3000.mypinata.cloud"
  const cid = "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
  const url = `https://${gatewayDomain}/ipfs/${cid}`
  ```
</CodeGroup>

## What's Next?

Ready to see more of what Pinata has to offer? Here are some additional features and concepts to help you get the most out of our platform:

<CardGroup>
  <Card title="Groups" icon="cabinet-filing" href="https://docs.pinata.cloud/files/groups">
    With Groups, you can organize your files via the Pinata API or the web app. Create a Group, store your IPFS content, and fetch content quickly and easily.
  </Card>

  <Card title="Workspaces" icon="people-group" href="https://docs.pinata.cloud/account-management/workspaces">
    Workspaces allow you to add multiple team members to your Pinata account and collaborate seamlessly. Even if your team members don’t have a Pinata account, you can invite them easily. This feature is essential for efficient project collaboration and management.
  </Card>
</CardGroup>


# Config
Source: https://docs.pinata.cloud/sdk/config



Overview of the Private IPFS SDK Config

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});
```

## Parameters

### pinataJwt (Optional)

* Type: `string`

The Pinata API JWT key that authorizes the SDK. [Read more about API Keys](/account-management/api-keys).

### pinataGateway (Optional)

* Type: `string`

The domain of the Gateway included with your account. [Read more about Gateways](/gateways/retrieving-files).

### pinataGatewayKey (Optional)

* Type: `string`

Optional [Gateway Access Control](/gateways/gateway-access-controls) key to authorize requests outside your account.


# addSwap
Source: https://docs.pinata.cloud/sdk/files/private/add-swap

`org:files:write`

Swap a CID for another using the [Hot Swaps](/gateways/plugins/hot-swaps) gateway plugin

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const swap = await pinata.files.private.addSwap({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  swapCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu"
})
```

## Returns

```typescript theme={null}
export type SwapCidResponse = {
	mapped_cid: string;
	created_at: string;
};
```

## Parameters

Pass in the required parameters below to swap a CID

### cid

* Type: `string`

This would be the original CID that would be visted

```typescript {2} theme={null}
const swap = await pinata.files.private.addSwap({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  swapCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu"
})
```

### swapCid

* Type: `string`

This would be the CID you would want the old CID to point to

```typescript {3} theme={null}
const swap = await pinata.files.private.addSwap({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  swapCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu"
})
```


# delete
Source: https://docs.pinata.cloud/sdk/files/private/delete

`org:files:write`

Delte an array of files from your account

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const deletedFiles = await pinata.files.private.delete([
  "4ad9d3d1-4ab4-464c-a42a-3027fc39a546"
])
```

## Returns

```typescript theme={null}
type DeleteResponse[] = {
  id: string;
  status: string;
};
```

## Parameters

### files

* Type: `string[]`

An array of file IDs you want to delete

```typescript theme={null}
const unpin = await pinata.files.private
  .delete([
    "5e3011c0-f242-46b8-ad8d-2141bba23096",
    "e4cb100d-9065-4a08-80a3-f195f35de336"
  ])
```


# deleteSwap
Source: https://docs.pinata.cloud/sdk/files/private/delete-swap

`org:files:write`

Remove a CID swap for [Hot Swaps](/gateways/plugins/hot-swaps) plugin

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const deleteSwap = await pinata.files.private.deleteSwap(
  "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske"
)
```

## Returns

```typescript theme={null}
OK
```

## Parameters

Pass in the required parameters below to remove a CID swap

### cid

* Type: `string`

This would be the original CID that was swapped

```typescript theme={null}
const deleteSwap = await pinata.files.private.deleteSwap(
  "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske"
)
```


# deleteVectors
Source: https://docs.pinata.cloud/sdk/files/private/delete-vectors

`org:files:write`

<Warning>
  The file vectors feature is still in beta. Please contact the team at <a href="mailto:team@pinata.cloud">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

Delete vectors for a given `fileId`

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example.mypinata.cloud",
});

const update = await pinata.files.private
  .deleteVectors("52681e41-86f4-407b-8f79-33a7e7e5df68")
```

## Returns

```typescript theme={null}
type VectorizeFileResponse = {
	status: boolean;
};
```

## Parameters

### fileId

* Type: `string`

ID of the target file to delete vectors

```typescript {2} theme={null}
const update = await pinata.files.private
  .deleteVectors("52681e41-86f4-407b-8f79-33a7e7e5df68")
```


# getSwapHistory
Source: https://docs.pinata.cloud/sdk/files/private/get-swap-history

`org:files:read`

See the history of [Hot Swaps](/gateways/plugins/hot-swaps) on a Gateway domain for a specified CID.

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const history = await pinata.files.private.getSwapHistory({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  domain: "discordpinnie.mypinata.cloud"
})
```

## Returns

```typescript theme={null}
SwapCidResponse[]

export type SwapCidResponse = {
	mapped_cid: string;
	created_at: string;
};
```

## Parameters

Pass in the required parameters to get a swap history

### cid

* Type: `string`

The target CID for swap history

```typescript {2} theme={null}
const history = await pinata.files.private.getSwapHistory({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  domain: "discordpinnie.mypinata.cloud"
})
```

### domain

* Type: `string`

The Gateway domain that has the Hot Swaps plugin installed

```typescript {3} theme={null}
const history = await pinata.files.private.getSwapHistory({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  domain: "discordpinnie.mypinata.cloud"
})
```


# list
Source: https://docs.pinata.cloud/sdk/files/private/list

`org:files:read`

List and filter files pinned to your Pinata account

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const files = await pinata.files.pivate.list()
```

## Returns

```typescript theme={null}
type FileListResponse = {
  files: FileListItem[];
  next_page_token: string;
};

type FileListItem = {
	id: string;
	name: string | null;
	cid: "pending" | string;
	size: number;
	numberOfFiles: number;
	mimeType: string;
	groupId: string;
	updatedAt: string;
	createdAt: string;
};
```

## Parameters

Filter response with the following additional methods. All filters are optional.

### name

* Type: `string`

Filter results based on name

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .name("pinnie")
```

### group

* Type: `string`

Filter results based on group ID

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .group("5b56981c-7e5b-4dff-aeca-de784728dddb")
```

### noGroup

* Type: `boolean`

Filter results to only show files that are not part of a group

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .noGroup(true)
```

### cid

* Type: `string`

Filter results based on CID

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .cid("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
```

### keyvalues

* Type: `Record<string, string>`

Filter results based on keyvalue pairs in metadata

```typescript {3-5} theme={null}
const files = await pinata.files.private
  .list()
  .keyvalues({
    env: "prod"
  })
```

### mimeType

* Type: `string`

Filter results based on mime type

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .mimeType("image/png")
```

### order

* Type: `"ASC" | "DESC"`

Order results either ascending or descending by created date

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .order("ASC")
```

### limit

* Type: `number`

Limit the number of results

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .limit(10)
```

### cidPending

* Type: `boolean`

Filters results and only returns files where `cid` is still `pending`

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .cid(true)
```

### pageToken

* Type: `string`

Paginates through files based on a provided page token

```typescript {3} theme={null}
const files = await pinata.files.private
  .list()
  .pageToken("MDE5MWIzZWYtM2U0Zi03YTY5LWE3OTQtOTRhZDE5NjQxMTk0")
```

## Auto Paginate

The `list` method has an auto pagination feature that is triggered when used inside a `for await` iterator

```typescript theme={null}
for await (const item of pinata.files.private.list()) {
  console.log(item.id);
}
```

Works like magic ✨


# queryVectors
Source: https://docs.pinata.cloud/sdk/files/private/query-vectors

`org:files:write`

<Warning>
  The file vectors feature is still in beta. Please contact the team at <a href="mailto:team@pinata.cloud">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

Query file vectors for a given `groupId`

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example.mypinata.cloud",
});

const update = await pinata.files.private.queryVectors({
  groupId: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  query: "Hello World"
})
```

## Returns

```typescript theme={null}
type VectorizeQueryResponse = {
	count: number;
	matches: VectorQueryMatch[];
};

type VectorQueryMatch = {
	file_id: string;
	cid: string;
	score: number;
};

// If using returnFile

type GetCIDResponse = {
  data?: JSON | string | Blob | null;
  contentType: ContentType;
};
```

## Parameters

### groupId

* Type: `string`

ID of the target group to query vectors

```typescript {2} theme={null}
const results = await pinata.files.private.queryVectors({
  groupId: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  query: "Hello World"
})
```

### query

* Type: `string`

Query string

```typescript {3} theme={null}
const results = await pinata.files.private.queryVectors({
  groupId: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  query: "Hello World"
})
```

### returnFile (Optional)

* Type: `boolean`

Return the top matched file itself if set to true

```typescript {4} theme={null}
const { data, contentType }  = await pinata.files.private.queryVectors({
  groupId: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  query: "Hello World",
  returnFile: true
})
```


# update
Source: https://docs.pinata.cloud/sdk/files/private/update

`org:files:write`

Update information for an existing file

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example.mypinata.cloud",
});

const update = await pinata.files.private.update({
  id: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  name: "New File Name",
})
```

## Returns

```typescript theme={null}
type FileListItem = {
	id: string;
	name: string | null;
	cid: "pending" | string;
	size: number;
	numberOfFiles: number;
	mimeType: string;
	groupId: string;
	updatedAt: string;
	createdAt: string;
};
```

## Parameters

### id

* Type: `string`

ID of the target file to update

```typescript {2} theme={null}
const update = await pinata.files.private.update({
  id: "8809812b-cd36-499f-b9b3-a37258a9cd6a",
  name: "New File Name",
})
```

### name (Optional)

* Type: `string`

Update the name of a file

```typescript {3} theme={null}
const update = await pinata.files.private.update({
  id: "8809812b-cd36-499f-b9b3-a37258a9cd6a",
  name: "New File Name"
})
```

### keyvalues (Optional)

* Type: `string`

Update the name of a file

```typescript {3-5} theme={null}
const update = await pinata.files.private.update({
  id: "8809812b-cd36-499f-b9b3-a37258a9cd6a",
  keyvalues: {
    env: "prod"
  }
})
```


# vectorize
Source: https://docs.pinata.cloud/sdk/files/private/vectorize

`org:files:write`

<Warning>
  The file vectors feature is still in beta. Please contact the team at <a href="mailto:team@pinata.cloud">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

Vectorize an existing file (must be part of a group)

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example.mypinata.cloud",
});

const update = await pinata.files.private
  .vectorize("52681e41-86f4-407b-8f79-33a7e7e5df68")
```

## Returns

```typescript theme={null}
type VectorizeFileResponse = {
	status: boolean;
};
```

## Parameters

### fileId

* Type: `string`

ID of the target file to vectorize

```typescript {2} theme={null}
const update = await pinata.files.private
  .vectorize("52681e41-86f4-407b-8f79-33a7e7e5df68")
```


# addSwap
Source: https://docs.pinata.cloud/sdk/files/public/add-swap

`org:files:write`

Swap a CID for another using the [Hot Swaps](/gateways/plugins/hot-swaps) gateway plugin

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
	pinataJwt: process.env.PINATA_JWT!,
	pinataGateway: "example-gateway.mypinata.cloud",
});

const swap = await pinata.files.public.addSwap({
	cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
	swapCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu"
})
```

## Returns

```typescript theme={null}
export type SwapCidResponse = {
	mapped_cid: string;
	created_at: string;
};
```

## Parameters

Pass in the required parameters below to swap a CID

### cid

* Type: `string`

This would be the original CID that would be visted

```typescript {2} theme={null}
const swap = await pinata.files.public.addSwap({
	cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
	swapCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu"
})
```

### swapCid

* Type: `string`

This would be the CID you would want the old CID to point to

```typescript {3} theme={null}
const swap = await pinata.files.public.addSwap({
	cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
	swapCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu"
})
```


# delete
Source: https://docs.pinata.cloud/sdk/files/public/delete

`org:files:write`

Delte an array of files from your account

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const deletedFiles = await pinata.files.public.delete([
  "4ad9d3d1-4ab4-464c-a42a-3027fc39a546"
])
```

## Returns

```typescript theme={null}
type DeleteResponse[] = {
  id: string;
  status: string;
};
```

## Parameters

### files

* Type: `string[]`

An array of file IDs you want to delete

```typescript theme={null}
const unpin = await pinata.files.public
  .delete([
    "5e3011c0-f242-46b8-ad8d-2141bba23096",
    "e4cb100d-9065-4a08-80a3-f195f35de336"
  ])
```


# deleteSwap
Source: https://docs.pinata.cloud/sdk/files/public/delete-swap

`org:files:write`

Remove a CID swap for [Hot Swaps](/gateways/plugins/hot-swaps) plugin

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const deleteSwap = await pinata.files.public.deleteSwap(
  "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske"
)
```

## Returns

```typescript theme={null}
OK
```

## Parameters

Pass in the required parameters below to remove a CID swap

### cid

* Type: `string`

This would be the original CID that was swapped

```typescript theme={null}
const deleteSwap = await pinata.files.public.deleteSwap(
  "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske"
)
```


# getSwapHistory
Source: https://docs.pinata.cloud/sdk/files/public/get-swap-history

`org:files:read`

See the history of [Hot Swaps](/gateways/plugins/hot-swaps) on a Gateway domain for a specified CID.

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const history = await pinata.files.public.getSwapHistory({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  domain: "discordpinnie.mypinata.cloud"
})
```

## Returns

```typescript theme={null}
SwapCidResponse[]

export type SwapCidResponse = {
	mapped_cid: string;
	created_at: string;
};
```

## Parameters

Pass in the required parameters to get a swap history

### cid

* Type: `string`

The target CID for swap history

```typescript {2} theme={null}
const history = await pinata.files.public.getSwapHistory({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  domain: "discordpinnie.mypinata.cloud"
})
```

### domain

* Type: `string`

The Gateway domain that has the Hot Swaps plugin installed

```typescript {3} theme={null}
const history = await pinata.files.getSwapHistory({
  cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  domain: "discordpinnie.mypinata.cloud"
})
```


# list
Source: https://docs.pinata.cloud/sdk/files/public/list

`org:files:read`

List and filter files pinned to your Pinata account

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
	pinataJwt: process.env.PINATA_JWT!,
	pinataGateway: "example-gateway.mypinata.cloud",
});

const files = await pinata.files.public.list()
```

## Returns

```typescript theme={null}
type FileListResponse = {
		files: FileListItem[];
		next_page_token: string;
};

type FileListItem = {
	id: string;
	name: string | null;
	cid: "pending" | string;
	size: number;
	numberOfFiles: number;
	mimeType: string;
	groupId: string;
	updatedAt: string;
	createdAt: string;
};
```

## Parameters

Filter response with the following additional methods. All filters are optional.

### name

* Type: `string`

Filter results based on name

```typescript {3} theme={null}
const files = await pinata.files.public
		.list()
		.name("pinnie")
```

### group

* Type: `string`

Filter results based on group ID

```typescript {3} theme={null}
const files = await pinata.files.public
		.list()
		.group("5b56981c-7e5b-4dff-aeca-de784728dddb")
```

### noGroup

* Type: `boolean`

Filter results to only show files that are not part of a group

```typescript {3} theme={null}
const files = await pinata.files.public
		.list()
		.noGroup(true)
```

### cid

* Type: `string`

Filter results based on CID

```typescript {3} theme={null}
const files = await pinata.files.public
		.list()
		.cid("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
```

### keyvalues

* Type: `Record<string, string>`

Filter results based on keyvalue pairs in metadata

```typescript {3-5} theme={null}
const files = await pinata.files.public
		.list()
		.keyvalues({
			env: "prod"
		})
```

### mimeType

* Type: `string`

Filter results based on mime type

```typescript {3} theme={null}
const files = await pinata.files.public
		.list()
		.mimeType("image/png")
```

### order

* Type: `"ASC" | "DESC"`

Order results either ascending or descending by created date

```typescript {3} theme={null}
const files = await pinata.files.public
		.list()
		.order("ASC")
```

### limit

* Type: `number`

Limit the number of results

```typescript {3} theme={null}
const files = await pinata.files.public
		.list()
		.limit(10)
```

### cidPending

* Type: `boolean`

Filters results and only returns files where `cid` is still `pending`

```typescript {3} theme={null}
const files = await pinata.files.public
		.list()
		.cid(true)
```

### pageToken

* Type: `string`

Paginates through files based on a provided page token

```typescript {3} theme={null}
const files = await pinata.files.public
		.list()
		.pageToken("MDE5MWIzZWYtM2U0Zi03YTY5LWE3OTQtOTRhZDE5NjQxMTk0")
```

## Auto Paginate

The `list` method has an auto pagination feature that is triggered when used inside a `for await` iterator

```typescript theme={null}
for await (const item of pinata.files.public.list()) {
		console.log(item.id);
}
```

Works like magic ✨


# queue
Source: https://docs.pinata.cloud/sdk/files/public/queue

`org:files:read`

List pin by CID requests in queue

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const queue = await pinata.files.public.queue().status("prechecking")
```

## Returns

```typescript theme={null}
export type PinQueueResponse = {
	rows: PinQueueItem[];
	next_page_token: string;
};

export type PinQueueItem = {
	id: string;
	cid: string;
	date_queued: string;
	name: string;
	status: string;
	keyvalues: any;
	host_nodes: string[];
	pin_policy: {
		regions: {
			id: string;
			desiredReplicationCount: number;
		}[];
		version: number;
	};
};
```

## Parameters

Filter results with the following methods. All filters are optional.

### cid

* Type: `string`

Filter by `cid`

```typescript theme={null}
const jobs = await pinata.files.public
  .queue()
  .cid('bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4')
```

### status

* Type: ` "prechecking" | "retrieving" | "expired" | "backfilled" | "over_free_limit" | "over_max_size" | "invalid_object" | "bad_host_node"`

Filter by current status

```typescript theme={null}
const jobs = await pinata.files.public
  .queue()
  .status("prechecking")
```

### sort

* Type: `"ASC" | "DSC"`

Order results by either ascending or descending by submission

```typescript theme={null}
const jobs = await pinata.files.public
  .queue()
  .sort("ASC")
```

### pageLimit

* Type: `number`

Limit the number of results. Default is `10`, max is `250`

```typescript theme={null}
const jobs = await pinata.files.public
  .queue()
  .pageLimit(100)
```

### pageToken

* Type: `string`

Paginate through results

```typescript theme={null}
const jobs = await pinata.files.public
  .queue()
  .pageToken("TOKEN")
```

## Auto Paginate

The `pinJobs` method has an auto pagination feature that is triggered when used inside a `for await` iterator

```typescript theme={null}
for await (const job of pinata.files.public.queue().status("expired") {
  console.log(job.cid);
}
```


# update
Source: https://docs.pinata.cloud/sdk/files/public/update

`org:files:write`

Update information for an existing file

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example.mypinata.cloud",
});

const update = await pinata.files.public.update({
  id: "52681e41-86f4-407b-8f79-33a7e7e5df68",
  name: "New File Name",
})
```

## Returns

```typescript theme={null}
type FileListItem = {
	id: string;
	name: string | null;
	cid: "pending" | string;
	size: number;
	numberOfFiles: number;
	mimeType: string;
	groupId: string;
	updatedAt: string;
	createdAt: string;
};
```

## Parameters

### id

* Type: `string`

ID of the target file to update

```typescript {2} theme={null}
const update = await pinata.files.public.update({
  id: "8809812b-cd36-499f-b9b3-a37258a9cd6a",
  name: "New File Name",
})
```

### name (Optional)

* Type: `string`

Update the name of a file

```typescript {3} theme={null}
const update = await pinata.files.public.update({
  id: "8809812b-cd36-499f-b9b3-a37258a9cd6a",
  name: "New File Name"
})
```

### keyvalues (Optional)

* Type: `string`

Update the name of a file

```typescript {3-5} theme={null}
const update = await pinata.files.public.update({
  id: "8809812b-cd36-499f-b9b3-a37258a9cd6a",
  keyvalues: {
    env: "prod"
  }
})
```


# createAccessLink
Source: https://docs.pinata.cloud/sdk/gateways/private/create-signed-url

`org:files:write`

Creates a temporary access link for a file on private IPFS

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const url = await pinata.gateways.private.createAccessLink({
	cid: "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq",
	expires: 30,
});
```

## Returns

* Type: `string`

The full signed URL

```
https://example-gateway.mypinata.cloud/files/bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq?X-Algorithm=PINATA1&X-Date=1724943397&X-Expires=30&X-Method=GET&X-Signature=<SIGNATURE>
```

## Parameters

### cid

* Type: `string`

Accepts CID of the file you are trying to create an access link for

```typescript {2} theme={null}
const url = await pinata.gateways.private.createAccessLink({
  cid: "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq",
	expires: 30,
});
```

### expires

* Type: `number`

The number of seconds the access link should be valid for

```typescript {3} theme={null}
const url = await pinata.gateways.private.createAcceslink({
	cid: "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq",
	expires: 30,
});
```

### date (Optional)

* Type: `number`

A UNIX timestamp of the date the link is created

```typescript {1-2,7} theme={null}
const date = Math.floor(new Date().getTime() / 1000);
//date: 1724943711

const url = await pinata.gateways.private.createAccessLink({
	cid: "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq",
	expires: 30,
	date: date
});
```

### gateway (Optional)

* Type: `string`

Use a Gateway domain other than the default domain from the config

```typescript {4} theme={null}
const url = await pinata.gateways.private.createAccessLink({
	cid: "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq",
	expires: 30,
	gateway: "discordpinnie.mypinata.cloud"
});
```

### optimizeImage (Optional)

* Type: [OptimizeImageOptions](/sdk/types#optimizeimageoptions)

```typescript theme={null}
type OptimizeImageOptions = {
  width?: number;
  height?: number;
  dpr?: number;
  fit?: "scaleDown" | "contain" | "cover" | "crop" | "pad";
  gravity?: "auto" | "side" | string;
  quality?: number;
  format?: "auto" | "webp";
  animation?: boolean;
  sharpen?: number;
  onError?: boolean;
  metadata?: "keep" | "copyright" | "none";
};
```

If the content being fetched is an image you can apply image optimizations to the image.

```typescript {3-7} theme={null}
const data = await pinata.gateways.private
  .createAccessLink("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
  .optimizeImage({
    width: 500,
    height: 500,
    format: "webp"
  })
```


# get
Source: https://docs.pinata.cloud/sdk/gateways/private/get

`org:files:write`

Retrieve a file through the config's `pinataGateway`

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const file = await pinata.gateways.private.get("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
```

## Returns

Returns the data in the form of `JSON`, `string`, or `Blob` as well as the `ContentType`

```typescript theme={null}
type GetCIDResponse = {
  data?: JSON | string | Blob | null;
  contentType: ContentType;
};

type ContentType =
  | "application/json"
  | "application/xml"
  | "text/plain"
  | "text/html"
  | "text/css"
  | "text/javascript"
  | "application/javascript"
  | "image/jpeg"
  | "image/png"
  | "image/gif"
  | "image/svg+xml"
  | "audio/mpeg"
  | "audio/ogg"
  | "video/mp4"
  | "application/pdf"
  | "application/octet-stream"
  | string;
```

## Parameters

### cid

* Type: `string`

Accepts CID of the file you are trying to fetch

```typescript theme={null}
const data = await pinata.gateways.private.get(
	"bafybeibo5zcqeorhqxczodrx52rn7byyrwfvwthz5dspnjlbkd7zkugefi",
);
```

### optimizeImage (Optional)

* Type: [OptimizeImageOptions](/sdk/types#optimizeimageoptions)

```typescript theme={null}
type OptimizeImageOptions = {
  width?: number;
  height?: number;
  dpr?: number;
  fit?: "scaleDown" | "contain" | "cover" | "crop" | "pad";
  gravity?: "auto" | "side" | string;
  quality?: number;
  format?: "auto" | "webp";
  animation?: boolean;
  sharpen?: number;
  onError?: boolean;
  metadata?: "keep" | "copyright" | "none";
};
```

If the content being fetched is an image you can apply image optimizations to the image.

```typescript {3-7} theme={null}
const data = await pinata.gateways.private
  .get("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
  .optimizeImage({
    width: 500,
    height: 500,
    format: "webp"
  })
```


# convert
Source: https://docs.pinata.cloud/sdk/gateways/public/convert



Convert an IPFS link into one that uses your Dedicated Gateway

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const url = await pinata.gateways.convert(
  "ipfs://QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng"
);
```

## Returns

```typescript theme={null}
string
```

## Parameters

### url

* Type: `string`

Accepts CID or IPFS gateway link.

```typescript theme={null}
const url = await pinata.gateways.convert(
	"bafybeibo5zcqeorhqxczodrx52rn7byyrwfvwthz5dspnjlbkd7zkugefi/hello-1.txt",
);

const url = await pinata.gateways.convert(
	"https://ipfs.io/ipfs/bafybeibo5zcqeorhqxczodrx52rn7byyrwfvwthz5dspnjlbkd7zkugefi/hello-1.txt",
);

const url = await pinata.gateways.convert(
	"https://bafyreibroegmxohcbvvs3rziqsp3osyn7t5rzot34y6pn5xtewffhtsl4e.ipfs.nftstorage.link/metadata.json",
);
```

### prefix (Optional)

* Type: `string`

Use a different gateway prefix than the config default

```typescript theme={null}
const url = await pinata.gateways.convert(
	"QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng",
	"https://ipfs.io"
);
```


# get
Source: https://docs.pinata.cloud/sdk/gateways/public/get



Retrieve a file from IPFS through the config's `pinataGateway`

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const file = await pinata.gateways.public.get("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
```

## Returns

Returns the data from the CID in the form of `JSON`, `string`, or `Blob` as well as the `ContentType`

```typescript theme={null}
type GetCIDResponse = {
  data?: JSON | string | Blob | null;
  contentType: ContentType;
};

type ContentType =
  | "application/json"
  | "application/xml"
  | "text/plain"
  | "text/html"
  | "text/css"
  | "text/javascript"
  | "application/javascript"
  | "image/jpeg"
  | "image/png"
  | "image/gif"
  | "image/svg+xml"
  | "audio/mpeg"
  | "audio/ogg"
  | "video/mp4"
  | "application/pdf"
  | "application/octet-stream"
  | string;
```

## Parameters

### cid

* Type: `string`

Accepts CID or IPFS gateway link.

```typescript theme={null}
const data = await pinata.gateways.public.get(
	"bafybeibo5zcqeorhqxczodrx52rn7byyrwfvwthz5dspnjlbkd7zkugefi/hello-1.txt",
);

const data = await pinata.gateways.public.get(
	"https://ipfs.io/ipfs/bafybeibo5zcqeorhqxczodrx52rn7byyrwfvwthz5dspnjlbkd7zkugefi/hello-1.txt",
);

const data = await pinata.gateways.public.get(
	"https://bafyreibroegmxohcbvvs3rziqsp3osyn7t5rzot34y6pn5xtewffhtsl4e.ipfs.nftstorage.link/metadata.json",
);
```

## Methods

### optimizeImage (Optional)

* Type: [OptimizeImageOptions](/sdk/types#optimizeimageoptions)

```typescript theme={null}
type OptimizeImageOptions = {
  width?: number;
  height?: number;
  dpr?: number;
  fit?: "scaleDown" | "contain" | "cover" | "crop" | "pad";
  gravity?: "auto" | "side" | string;
  quality?: number;
  format?: "auto" | "webp";
  animation?: boolean;
  sharpen?: number;
  onError?: boolean;
  metadata?: "keep" | "copyright" | "none";
};
```

If the content being fetched is an image you can apply image optimizations to the image.

```typescript theme={null}
const data = await pinata.gateways.public
  .get("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
  .optimizeImage({
    width: 500,
    height: 500,
    format: "webp"
  })
```


# Getting Started
Source: https://docs.pinata.cloud/sdk/getting-started

Get up and running with the Pinata IPFS SDK

<img />

The IPFS SDK is an all-in-one tool for everything you might need, from uploading content, using Gateways, even user or group management!

## 1. Installation and Setup

Install with your package manager of choice

<CodeGroup>
  ```bash npm theme={null}
  npm i pinata
  ```

  ```bash pnpm theme={null}
  pnpm i pinata
  ```

  ```bash yarn theme={null}
  yarn add pinata
  ```

  ```bash bun theme={null}
  bun i pinata
  ```
</CodeGroup>

Import and initialize the SDK in your codebase with the following variables

* [Pinata API Key JWT](/account-management/api-keys)
* [Pinata Dedicated Gateway Domain](/gateways/retrieving-files)

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: "PINATA_JWT",
  pinataGateway: "example-gateway.mypinata.cloud",
});
```

<Note>The `PINATA_JWT` is a secret key, be sure to initialize the SDK in a secure environment and practice basic variable security practices. If you need to upload from a client environment, consider using signed JWTs</Note>

## 2. Upload a File

```typescript {11} theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

async function main() {
  try {
    const file = new File(["hello world!"], "hello.txt", { type: "text/plain" });
    const upload = await pinata.upload.public.file(file);
    console.log(upload);
  } catch (error) {
    console.log(error);
  }
}

await main();
```

This will return an object like the following

```typescript theme={null}
{
  id: "0195f815-5c5e-716d-9240-d3ae380e2002",
  group_id: null,
  name: "hello.txt",
  cid: "bafkreidvbhs33ighmljlvr7zbv2ywwzcmp5adtf4kqvlly67cy56bdtmve",
  created_at: "2025-04-02T19:58:24.616Z",
  size: 12,
  number_of_files: 1,
  mime_type: "text/plain",
  vectorized: false,
  network: "public",
}
```

## 3. Retrieve a File

Use the `cid` of a file to fetch it through a Gateway or create a URL to access it

```typescript {10,13} theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
    pinataJwt: process.env.PINATA_JWT!,
    pinataGateway: "example-gateway.mypinata.cloud",
});

async function main() {
  try {
    const data = await pinata.gateways.public.get("bafkreibm6jg3ux5qumhcn2b3flc3tyu6dmlb4xa7u5bf44yegnrjhc4yeq");
    console.log(data)

    const url = await pinata.gateways.public.convert("bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq")
    console.log(url)

  } catch (error) {
    console.log(error);
  }
}

main();
```


# addFiles
Source: https://docs.pinata.cloud/sdk/groups/private/add-files

`org:groups:write`

Add private files to a private group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const group = await pinata.groups.private.addFiles({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```

## Returns

```typescript theme={null}
type UpdateGroupFilesResponse[] = {
	id: string;
	status: string;
};
```

## Parameters

### groupId

* Type: `string`

ID of the target Group to add files to

```typescript {2} theme={null}
const group = await pinata.groups.private.addFiles({
  groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```

### files

* Type: `string[]`

An array of file IDs as strings that you want to add to the group

```typescript {3-6} theme={null}
const group = await pinata.groups.private.addFiles({
  groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```


# create
Source: https://docs.pinata.cloud/sdk/groups/private/create

`org:groups:write`

Create a private group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const group = await pinata.groups.private.create({
	name: "My New Group",
});
```

## Returns

```typescript theme={null}
type GroupResponseItem = {
    id: string;
    name: string;
    created_at: string;
};
```

## Parameters

### name

* Type: `string`

Requires a name for the group to be created

```typescript {2} theme={null}
const group = await pinata.groups.private.create({
	name: "My New Group",
});
```


# delete
Source: https://docs.pinata.cloud/sdk/groups/private/delete

`org:groups:write`

Delete a private group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const groups = await pinata.groups.private.delete({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
});
```

## Returns

```typescript theme={null}
OK
```

## Parameters

### groupId

* Type: `string`

ID for the target Group

```typescript {2} theme={null}
const groups = await pinata.groups.private.delete({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
});
```


# get
Source: https://docs.pinata.cloud/sdk/groups/private/get

`org:groups:read`

Get info for an existing private group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const groups = await pinata.groups.private.get({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
});
```

## Returns

```typescript theme={null}
type GroupResponseItem = {
    id: string;
    name: string;
    created_at: string;
};
```

## Parameters

### groupId

* Type: `string`

ID for the target Group

```typescript {2} theme={null}
const groups = await pinata.groups.private.get({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
});
```


# list
Source: https://docs.pinata.cloud/sdk/groups/private/list

`org:groups:read`

List and filter through all private groups

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const groups = await pinata.groups.private
  .list()
```

## Returns

```typescript theme={null}
type GroupListResponse = {
  groups: GroupResponseItem[];
  next_page_token: string;
};

type GroupResponseItem = {
    id: string;
    is_public: boolean;
    name: string;
    created_at: string;
};
```

## Parameters

Filter response with the following additional methods. All filters are optional.

### name

* Type: `string`

Filters groups based the group name

```typescript {3} theme={null}
const groups = await pinata.groups.private
    .list()
    .name("SDK")
```

### limit

* Type: `number`

Limits the number of results

```typescript {3} theme={null}
const groups = await pinata.groups.private
    .list()
    .limit(10)
```

### pageToken

* Type: `string`

Paginates through groups based on a provided page token

```typescript {3} theme={null}
const groups = await pinata.groups.private
  .list()
  .pageToken("MDE5MWIzZWYtM2U0Zi03YTY5LWE3OTQtOTRhZDE5NjQxMTk0")
```

## Auto Paginate

The `list` method has an auto pagination feature that is triggered when used inside a `for await` iterator

```typescript theme={null}
for await (const item of pinata.gateways.private.list()) {
  console.log(item.name);
}
```


# removeFiles
Source: https://docs.pinata.cloud/sdk/groups/private/remove-files

`org:groups:write`

Remove private files from a private group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const group = await pinata.groups.private.removeFiles({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```

## Returns

```typescript theme={null}
type UpdateGroupFilesResponse[] = {
	id: string;
	status: string;
};
```

## Parameters

### groupId

* Type: `string`

ID of the target Group to remove files from

```typescript {2} theme={null}
const group = await pinata.groups.private.removeFiles({
  groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```

### files

* Type: `string[]`

An array of file IDs as strings that you want to remove from the group

```typescript {3-6} theme={null}
const group = await pinata.groups.private.removeFiles({
  groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```


# update
Source: https://docs.pinata.cloud/sdk/groups/private/update

`org:groups:write`

Update the name of a private group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const groups = await pinata.groups.private.update({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	name: "My New Group 2",
});
```

## Returns

```typescript theme={null}
type GroupResponseItem = {
    id: string;
    name: string;
    created_at: string;
};
```

## Parameters

### groupId

* Type: `string`

ID for the target Group

```typescript {2} theme={null}
const groups = await pinata.groups.private.update({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	name: "My New Group 2",
});
```

### name (Optional)

* Type: `string`

Updated name for the target group

```typescript {2} theme={null}
const groups = await pinata.groups.private.update({
  groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	name: "My Group Again",
});
```


# addFiles
Source: https://docs.pinata.cloud/sdk/groups/public/add-files

`org:groups:write`

Add public files to a public group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const group = await pinata.groups.public.addFiles({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```

## Returns

```typescript theme={null}
type UpdateGroupFilesResponse[] = {
	id: string;
	status: string;
};
```

## Parameters

### groupId

* Type: `string`

ID of the target Group to add files to

```typescript {2} theme={null}
const group = await pinata.groups.public.addFiles({
  groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```

### files

* Type: `string[]`

An array of file IDs as strings that you want to add to the group

```typescript {3-6} theme={null}
const group = await pinata.groups.public.addFiles({
  groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```


# create
Source: https://docs.pinata.cloud/sdk/groups/public/create

`org:groups:write`

Create a public group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const group = await pinata.groups.public.create({
	name: "My New Group",
});
```

## Returns

```typescript theme={null}
type GroupResponseItem = {
    id: string;
    name: string;
    created_at: string;
};
```

## Parameters

### name

* Type: `string`

Requires a name for the group to be created

```typescript {2} theme={null}
const group = await pinata.groups.public.create({
	name: "My New Group",
});
```


# delete
Source: https://docs.pinata.cloud/sdk/groups/public/delete

`org:groups:write`

Delete a public group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const groups = await pinata.groups.public.delete({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
});
```

## Returns

```typescript theme={null}
OK
```

## Parameters

### groupId

* Type: `string`

ID for the target Group

```typescript {2} theme={null}
const groups = await pinata.groups.public.delete({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
});
```


# get
Source: https://docs.pinata.cloud/sdk/groups/public/get

`org:groups:read`

Get info for an existing public group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const groups = await pinata.groups.public.get({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
});
```

## Returns

```typescript theme={null}
type GroupResponseItem = {
    id: string;
    name: string;
    created_at: string;
};
```

## Parameters

### groupId

* Type: `string`

ID for the target Group

```typescript {2} theme={null}
const groups = await pinata.groups.public.get({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
});
```


# list
Source: https://docs.pinata.cloud/sdk/groups/public/list

`org:groups:read`

List and filter through all public groups

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const groups = await pinata.groups.public
  .list()
```

## Returns

```typescript theme={null}
type GroupListResponse = {
  groups: GroupResponseItem[];
  next_page_token: string;
};

type GroupResponseItem = {
    id: string;
    name: string;
    created_at: string;
};
```

## Parameters

Filter response with the following additional methods. All filters are optional.

### name

* Type: `string`

Filters groups based the group name

```typescript {3} theme={null}
const groups = await pinata.groups.public
    .list()
    .name("SDK")
```

### limit

* Type: `number`

Limits the number of results

```typescript {3} theme={null}
const groups = await pinata.groups.public
    .list()
    .limit(10)
```

### pageToken

* Type: `string`

Paginates through groups based on a provided page token

```typescript {3} theme={null}
const groups = await pinata.groups.public
  .list()
  .pageToken("MDE5MWIzZWYtM2U0Zi03YTY5LWE3OTQtOTRhZDE5NjQxMTk0")
```

## Auto Paginate

The `list` method has an auto pagination feature that is triggered when used inside a `for await` iterator

```typescript theme={null}
for await (const item of pinata.gateways.public.list()) {
  console.log(item.name);
}
```


# removeFiles
Source: https://docs.pinata.cloud/sdk/groups/public/remove-files

`org:groups:write`

Remove public files from a public group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const group = await pinata.groups.public.removeFiles({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```

## Returns

```typescript theme={null}
type UpdateGroupFilesResponse[] = {
	id: string;
	status: string;
};
```

## Parameters

### groupId

* Type: `string`

ID of the target Group to remove files from

```typescript {2} theme={null}
const group = await pinata.groups.public.removeFiles({
  groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```

### files

* Type: `string[]`

An array of file IDs as strings that you want to remove from the group

```typescript {3-6} theme={null}
const group = await pinata.groups.public.removeFiles({
  groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	files: [
	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
		"a606ef7e-70a0-40ad-9b8a-60563e009655"
	],
});
```


# update
Source: https://docs.pinata.cloud/sdk/groups/public/update

`org:groups:write`

Update the name of a public group

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const groups = await pinata.groups.public.update({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
	name: "My New Group 2",
});
```

## Returns

```typescript theme={null}
type GroupResponseItem = {
    id: string;
    name: string;
    created_at: string;
};
```

## Parameters

### groupId

* Type: `string`

ID for the target Group

```typescript {2} theme={null}
const groups = await pinata.groups.public.update({
	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
});
```

### name (Optional)

* Type: `string`

Updated name for the target group

```typescript {2} theme={null}
const groups = await pinata.groups.public.update({
	name: "My Group Again",
});
```


# React Hooks
Source: https://docs.pinata.cloud/sdk/react

A collection of React hooks to use with Pinata

Included with the Pinata SDK is the `pinata/react` package which comes with a hook you can use to upload files and a convert helper function for converting CIDs into IPFS Gateway URLs.

## Installation

Install the Pinata SDK

```bash theme={null}
npm i pinata
```

## Usage

Import at the top of your desired page or component

```typescript theme={null}
import { useUpload, convert } from "pinata/react";
```

Inside your page or component use the hook to extract methods and state

```typescript theme={null}
const {
	upload, // Method to upload a file using a presigned URL
	progress, // Progress state as integer
	loading, // Boolean uploading state
	uploadResponse, // Either full Upload Response or just a CID if you use Resumable Uploads
	error, // Error state
	pause, // Pause upload method
	resume, // Resume upload method
	cancel, // Cancel current upload method
} = useUpload();
```

<Note>
  Keep in mind that states like `pause`, `resume`, or `progress` are only available on files over 100MB that automatically engage resumable uploads through TUS.
</Note>

Return types for `useUpload`

```typescript theme={null}
export type UseUploadReturn = {
	progress: number;
	loading: boolean;
	error: Error | null;
	uploadResponse: UploadResult | null;
	upload: (
		file: File,
		network: "public" | "private",
		url: string,
		options?: UploadOptions,
	) => Promise<void>;
	pause: () => void;
	resume: () => void;
	cancel: () => void;
};
```

To upload a file you must already have a server setup that returns a [Presigned URL](/files/presigned-urls). Then you can pass it into the `upload` method like so.

```typescript theme={null}
await upload(file, "public", "presigned_URL", {
  metadata: {
  	name: file.name || "Upload from React",
  	keyvalues: {
  		app: "React",
  		timestamp: Date.now().toString(),
  	},
  }
});
```

<Tip>
  [Learn how to send Presigned URLs from your server](/frameworks/hono)
</Tip>

Below are the available `UploadOptions` that can be passed into `upload`

```typescript theme={null}
export type UploadOptions = {
	metadata?: PinataMetadata;
	groupId?: string;
	chunkSize?: number; // Defaults to 1014 * 256 * 20 * 10 (~52MB)
};
```

Once a file is uploaded the `uploadResponse` will contain either the full upload response or just the CID if your file was over 100MB and utilized TUS resumable uploads.

The `convert` helper can be used to turn a CID into a URL like so:

```typescript theme={null}
const ipfsLink = await convert(uploadResponse.cid, "https://gateway.pinata.cloud");
// https://gateway.pinata.cloud/ipfs/CID
```

Below is a full example of implementing the `useUpload` hook with progress and abilities to pause and resume the upload.

```typescript theme={null}
import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import pinataLogo from "/pinnie.png";
import "./App.css";
import { useUpload, convert } from "pinata/react";

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [link, setLink] = useState("");

  const { upload, uploadResponse, loading, error, progress, pause, resume, cancel } = useUpload();

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleUpload = async () => {
    if (!file) return;

    const urlRes = await fetch(`${import.meta.env.VITE_SERVER_URL}/presigned_url`);
    const urlData = await urlRes.json();

    try {
      // Use the upload function from useUpload hook
      await upload(file, "public", urlData.url, {
        metadata: {
          name: file.name || "Upload from Web",
          keyvalues: {
            app: "Pinata Web Demo",
            timestamp: Date.now().toString(),
          },
        },
      });
    } catch (uploadError) {
      console.error("Upload error:", uploadError);
    }
  };

  // Set the link when upload is successful
  if (uploadResponse && !link) {
    async function setIpfsLink() {
      let ipfsLink: string = "";
      if (typeof uploadResponse === "string") {
        ipfsLink = await convert(uploadResponse, "https://gateway.pinata.cloud");
      } else if (uploadResponse) {
        ipfsLink = await convert(uploadResponse.cid, "https://gateway.pinata.cloud");
      }
      setLink(ipfsLink);
    }
    setIpfsLink();
  }

  // Get upload status message
  const getStatusMessage = () => {
    if (loading) return `Uploading file to Pinata...`;
    if (error) return `Upload error: ${error?.message || "Unknown error"}`;
    return "";
  };

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
        <a href="https://pinata.cloud" target="_blank">
          <img src={pinataLogo} className="logo pinata" alt="Pinata logo" />
        </a>
      </div>
      <h1>Vite + React + Pinata</h1>
      <div className="card">
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleUpload} disabled={!file || loading}>
          {loading ? "Uploading..." : "Upload to Pinata"}
        </button>

        {loading && (
          <div className="upload-status-container">
            <p>{getStatusMessage()}</p>

            <div className="upload-controls-container">
              {progress < 100 && (
                <>
                  <button onClick={pause} className="control-button pause">
                    Pause
                  </button>
                  <button onClick={resume} className="control-button resume">
                    Resume
                  </button>
                  <button onClick={cancel} className="control-button cancel">
                    Cancel
                  </button>
                </>
              )}
            </div>
          </div>
        )}

        {!loading && getStatusMessage() && <p>{getStatusMessage()}</p>}

        {link && (
          <div className="success-container">
            <p className="success-title">Upload Complete!</p>
            <a href={link} target="_blank" className="view-link">
              View File
            </a>
          </div>
        )}
      </div>
      <p className="read-the-docs">Click on the Vite and React logos to learn more</p>
    </>
  );
}

export default App;
```

## Questions

Please [contact us](mailto:steve@pinata.cloud) if you have any issues!


# add
Source: https://docs.pinata.cloud/sdk/signatures/public/add

`org:files:write`

Add an EIP-712 signature to a CID

<Note>
  For more information about adding signatures to CIDs on IPFS please read the [Signatures Guide](/files/signatures).
</Note>

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signature = await pinata.signatures.public.add({
  cid: "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU",
  signature: "0x1b...911b",
  address: "0xB3899AA8E13172E48D44CE411b0c4c2f08730Dc6"
});
```

## Returns

```typescript theme={null}
type SignatureResponse = {
  cid: string;
  signature: string;
};
```

## Parameters

### cid

* Type: `string`

Target CID that you want to add a signature to.

```typescript {2} theme={null}
const signature = await pinata.signatures.public.add({
  cid: "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU",
  signature: "0x1b...911b",
  address: "0xB3899AA8E13172E48D44CE411b0c4c2f08730Dc6"
});
```

### signature

* Type: `0x${string}`

EIP-712 Signature to be assigned to target CID.

```typescript {3} theme={null}
const signature = await pinata.signatures.public.add({
  cid: "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU",
  signature: "0x1b...911b",
  address: "0xB3899AA8E13172E48D44CE411b0c4c2f08730Dc6"
});
```

### address

* Type: `0x${string}`

Wallet address that made the signature

```typescript {4} theme={null}
const signature = await pinata.signatures.public.add({
  cid: "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU",
  signature: "0x1b...911b",
  address: "0xB3899AA8E13172E48D44CE411b0c4c2f08730Dc6"
});
```


# delete
Source: https://docs.pinata.cloud/sdk/signatures/public/delete

`org:files:write`

Delete an EIP-712 signature from a CID

<Note>
  For more information about adding signatures to CIDs on IPFS please read the [Signatures Guide](/files/signatures).
</Note>

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signature = await pinata.signatures.delete(
  "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU"
);
```

## Returns

```typescript theme={null}
OK
```

## Parameters

### cid

* Type: `string`

Target CID that you want to add a signature to.

```typescript theme={null}
const signature = await pinata.signatures.delete(
  "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU"
);
```


# get
Source: https://docs.pinata.cloud/sdk/signatures/public/get

`org:files:read`

Get signature for CID

<Note>
  For more information about adding signatures to CIDs on IPFS please read the [Signatures Guide](/files/signatures).
</Note>

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signature = await pinata.signatures.get("QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU");
```

## Returns

```typescript theme={null}
type SignatureResponse = {
  cid: string;
  signature: string;
};
```

## Parameters

### cid

* Type: `string`

Target CID that you want to add a signature to.

```typescript theme={null}
const signature = await pinata.signatures.get("QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU");
```


# base64
Source: https://docs.pinata.cloud/sdk/upload/private/base64

`org:files:write`

Upload a base64 string to Private IPFS

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const upload = await pinata.upload.private.base64("SGVsbG8gV29ybGQh")
```

## Returns

```typescript theme={null}
type UploadResponse = {
	id: string;
	name: string;
	cid: string;
	size: number;
	created_at: string;
	number_of_files: number;
	mime_type: string;
	group_id: string | null;
	keyvalues: {
		[key: string]: string;
	};
	vectorized: boolean;
	network: string;
};
```

## Parameters

### base64

* Type: `string`

Accepts a string encoded in base64

```typescript theme={null}
const upload = await pinata.upload.private.base64("SGVsbG8gV29ybGQh")
```

### group (Optional)

* Type: `string`

Upload to a specific group by passing in the `groupId`

```typescript {3} theme={null}
const upload = await pinata.upload.private
  .base64("SGVsbG8gV29ybGQh")
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Add optional metadata to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.private
  .base64("SGVsbG8gV29ybGQh")
  .keyvalues({
    env: "prod"
  })
```

### name (Optional)

* Type: `string`

Add optional name to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.private
  .base64("SGVsbG8gV29ybGQh")
  .name("hello.txt")
```

### vectorize (Optional)

<Warning>
  The file vectors feature is still in beta. Please contact the team at <a href="mailto:team@pinata.cloud">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

* Type: `null`

Vectorize a file on upload, requires a group to be used as well.

```typescript {4} theme={null}
const upload = await pinata.upload.private
  .base64("SGVsbG8gV29ybGQh")
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
  .vectorize()
```

### url (Optional)

* Type: `string`

Pass in a presigned upload URL created with [createSignedURL](./create-signed-url)

```typescript {3} theme={null}
const upload = await pinata.upload.private
  .file(file)
  .url(url)
```

### key (Optional)

* Type: `string`

Upload a file using a secondary API key generated through `keys.create()`

```typescript {3} theme={null}
const upload = await pinata.upload.private
  .base64("SGVsbG8gV29ybGQh")
  .key("GENERATED_API_JWT")
```


# createSignedURL
Source: https://docs.pinata.cloud/sdk/upload/private/create-signed-url

`org:files:write`

Create a signed upload URL for a file upload. This method is ideal when you want to authorize server side but upload on the client; check out [this doc](/files/uploading-files#client-side-uploads) for more details.

<Note>
  All the information about the upload such as the name, group, keyvalues, etc. must be part of the signed URL in order for those values to go through. If you have a basic signed URL with no extra parameters and then try to add fields like name, group, etc. they will not go through.
</Note>

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signedURL = await pinata.upload.private.createSignedURL({
  expires: 30
});

const upload = await pinata.upload.private
  .file(file)
  .url(signedURL)
```

## Returns

* Type: `string`

The full signed URL

```
https://uploads.pinata.cloud/v3/files/209bb44c-e987-47c4-a9e3-a88e02d4d8e9?X-Algorithm=PINATA2&X-Date=1734379351&X-Expires=300&X-Method=%5B%22HEAD%22%2C%22PATCH%22%2C%22POST%22%5D&X-User-ID=eb73db21-10fa-4005-b97c-639e19e82d60&X-Signature=<SIGNATURE>
```

## Parameters

### expires

* Type: `number`

The number of seconds the signed URL should be valid for

```typescript {2} theme={null}
const url = await pinata.upload.private.createSignedURL({
	expires: 30,
});
```

### name (Optional)

* Type: `string`

Name for the file to be uploaded

```typescript {3} theme={null}
const url = await pinata.upload.private.createSignedURL({
	expires: 30,
	name: "My Cool File"
});
```

### mimeTypes (Optional)

* Type: `string[]`

Specify allowed file mime types and prevent uploads from files that do not match. Accepts wildcard mime types as well.

```typescript {3-6} theme={null}
const url = await pinata.upload.private.createSignedURL({
	expires: 30,
	mimeTypes: [
	  "image/*",
		"application/json"
	]
});
```

### maxFileSize (Optional)

* Type: `number`

Restrict upload to a specified file size in `bytes`

```typescript {3} theme={null}
const url = await pinata.upload.private.createSignedURL({
	expires: 30,
	maxFileSize: 50000 // 50kb
});
```

### groupId (Optional)

* Type: `string`

The target groupId the file would be uploaded to

```typescript {3} theme={null}
const url = await pinata.upload.private.createSignedURL({
	expires: 30,
	groupId: "ad4bc3bf-8794-49e7-94ff-fea1ce745779"
});
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Keyvalue pairs for the uploaded file

```typescript {3-5} theme={null}
const url = await pinata.upload.private.createSignedURL({
	expires: 30,
	keyvalues: {
	  env: "prod"
	}
});
```

### vectorize (Optional)

* Type: `boolean`

Vectorize the file on upload

```typescript {3} theme={null}
const url = await pinata.upload.private.createSignedURL({
	expires: 30,
	vectorize: true
});
```

### date (Optional)

* Type: `number`

A UNIX timestamp of the date a URL is signed

```typescript {1-2,6} theme={null}
const date = Math.floor(new Date().getTime() / 1000);
//date: 1724943711

const url = await pinata.upload.private.createSignedURL({
	expires: 30,
	date: date
});
```


# file
Source: https://docs.pinata.cloud/sdk/upload/private/file

`org:files:write`

Upload a single file to Private IPFS

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const file = new File(["hello world!"], "hello.txt", { type: "text/plain" })
const upload = await pinata.upload.private.file(file)
```

### Local Files

If you need to upload files from a local file source you can use `fs` to feed a file into a `blob`, then turn that `blob` into a `File`.

```typescript {10-12} theme={null}
const { PinataSDK } = require("pinata")
const fs = require("fs")
const { Blob } = require("buffer")

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud"
})

const blob = new Blob([fs.readFileSync("./hello-world.txt")]);
const file = new File([blob], "hello-world.txt", { type: "text/plain"})
const upload = await pinata.upload.private.file(file);
```

## Returns

```typescript theme={null}
type UploadResponse = {
	id: string;
	name: string;
	cid: string;
	size: number;
	created_at: string;
	number_of_files: number;
	mime_type: string;
	group_id: string | null;
	keyvalues: {
		[key: string]: string;
	};
	vectorized: boolean;
	network: string;
};
```

## Parameters

### file

* Type: `File` object

Accepts a File object in accordance with the [W3C File API](https://w3c.github.io/FileAPI/#file-section).

```typescript {3} theme={null}
const blob = new Blob(["hello world!"], { type: "text/plain" })
const file = new File([blob], "hello.txt", { type: "text/plain" })
const upload = await pinata.upload.private.file(file)
```

In most environments you can also pass a Blob here as well.

```typescript {2} theme={null}
const blob = new Blob(["hello world!"], { type: "text/plain" })
const upload = await pinata.upload.private.file(blob)
```

### group (Optional)

* Type: `string`

Upload to a specific group by passing in the `groupId`

```typescript {3} theme={null}
const upload = await pinata.upload.private
  .file(file)
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Add optional keyvalues to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.private
  .file(file)
  .keyvalues({
    env: "prod"
  })
```

### name (Optional)

* Type: `string`

Add optional name to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.private
  .file(file)
  .name("hello.txt")
```

### vectorize (Optional)

<Warning>
  The file vectors feature is still in beta. Please contact the team at <a href="mailto:team@pinata.cloud">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

* Type: `null`

Vectorize a file on upload, requires a group to be used as well.

```typescript {4} theme={null}
const upload = await pinata.upload.private
  .file(file)
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
  .vectorize()
```

### url (Optional)

* Type: `string`

Pass in a presigned upload URL created with [createSignedURL](./create-signed-url)

```typescript {3} theme={null}
const upload = await pinata.upload.private
  .file(file)
  .url(url)
```

### key (Optional)

* Type: `string`

Upload a file using a secondary API key generated through `keys.create()`

```typescript {3} theme={null}
const upload = await pinata.upload.private
  .file(file)
  .key("GENERATED_API_JWT")
```


# json
Source: https://docs.pinata.cloud/sdk/upload/private/json

`org:files:write`

Upload a JSON object to Private IPFS

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const upload = await pinata.upload.json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
})
```

## Returns

```typescript theme={null}
type UploadResponse = {
	id: string;
	name: string;
	cid: string;
	size: number;
	created_at: string;
	number_of_files: number;
	mime_type: string;
	group_id: string | null;
	keyvalues: {
		[key: string]: string;
	};
	vectorized: boolean;
	network: string;
};
```

## Parameters

### JSON

* Type: `Record<string, unknown>`

Accepts an object that is turned into JSON

```typescript theme={null}
const upload = await pinata.upload.private.json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
})
```

### group (Optional)

* Type: `string`

Upload to a specific group by passing in the `groupId`

```typescript {7} theme={null}
const upload = await pinata.upload.private
  .json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
  })
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Add optional keyvalues to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.private
  .json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
  })
  .keyvalues({
    env: "prod"
  })
```

### name (Optional)

* Type: `string`

Add optional name to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.private
  .json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
  })
  .name("metadata.json")
```

### vectorize (Optional)

<Warning>
  The file vectors feature is still in beta. Please contact the team at <a href="mailto:team@pinata.cloud">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

* Type: `null`

Vectorize a file on upload, requires a group to be used as well.

```typescript {8} theme={null}
const upload = await pinata.upload.private
  .json({
      content: "console.log('hello world!)",
      name: "helloworld.ts",
      lang: "ts"
  })
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
  .vectorize()
```

### url (Optional)

* Type: `string`

Pass in a presigned upload URL created with [createSignedURL](./create-signed-url)

```typescript {3} theme={null}
const upload = await pinata.upload.private
  .json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
  })
  .url(url)
```

### key (Optional)

* Type: `string`

Upload a file using a secondary API key generated through `keys.create()`

```typescript {7} theme={null}
const upload = await pinata.upload.private
    .json({
        content: "console.log('hello world!)",
        name: "helloworld.ts",
        lang: "ts"
    })
  .key("GENERATED_API_JWT")
```


# url
Source: https://docs.pinata.cloud/sdk/upload/private/url

`org:files:write`

Upload the contents of a URL to Private IPFS

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const upload = await pinata.upload.private.url("https://i.imgur.com/u4mGk5b.gif")
```

## Returns

```typescript theme={null}
type UploadResponse = {
	id: string;
	name: string;
	cid: string;
	size: number;
	created_at: string;
	number_of_files: number;
	mime_type: string;
	group_id: string | null;
	keyvalues: {
		[key: string]: string;
	};
	vectorized: boolean;
	network: string;
};
```

## Parameters

### url

* Type: `string`

Accepts a URL in the form of a string. The mimetype of the URL body provided in the headers typically determines the resulting file.

```typescript theme={null}
const upload = await pinata.upload.private.url("https://i.imgur.com/u4mGk5b.gif")
```

### group (Optional)

* Type: `string`

Upload to a specific group by passing in the `groupId`

```typescript {3} theme={null}
const upload = await pinata.upload.private
  .url("https://i.imgur.com/u4mGk5b.gif")
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Add optional keyvalues to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.private
  .url("https://i.imgur.com/u4mGk5b.gif")
  .keyvalues({
    env: "prod"
  })
```

### name (Optional)

* Type: `string`

Add optional name to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.private
  .url("https://i.imgur.com/u4mGk5b.gif")
  .name("pinnie.gif")
```

### vectorize (Optional)

<Warning>
  The file vectors feature is still in beta. Please contact the team at <a href="mailto:team@pinata.cloud">[team@pinata.cloud](mailto:team@pinata.cloud)</a> if you have any issues.
</Warning>

* Type: `null`

Vectorize a file on upload, requires a group to be used as well.

```typescript {4} theme={null}
const upload = await pinata.upload.private
  .url("https://i.imgur.com/u4mGk5b.gif")
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
  .vectorize()
```

### url (Optional)

* Type: `string`

Pass in a presigned upload URL created with [createSignedURL](./create-signed-url)

```typescript {3} theme={null}
const upload = await pinata.upload.private
  .url(url)
  .url(url)
```

### key (Optional)

* Type: `string`

Upload a file using a secondary API key generated through `keys.create()`

```typescript {3} theme={null}
const upload = await pinata.upload.private
  .url("https://i.imgur.com/u4mGk5b.gif")
  .key("GENERATED_API_JWT")
```


# base64
Source: https://docs.pinata.cloud/sdk/upload/public/base64

`org:files:write`

Upload a base64 string to Pinata

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const upload = await pinata.upload.public.base64("SGVsbG8gV29ybGQh")
```

## Returns

```typescript theme={null}
type UploadResponse = {
	id: string;
	name: string;
	cid: string;
	size: number;
	created_at: string;
	number_of_files: number;
	mime_type: string;
	group_id: string | null;
	keyvalues: {
		[key: string]: string;
	};
	vectorized: boolean;
	network: string;
};
```

## Parameters

### base64

* Type: `string`

Accepts a string encoded in base64

```typescript theme={null}
const upload = await pinata.upload.public.base64("SGVsbG8gV29ybGQh")
```

### group (Optional)

* Type: `string`

Upload to a specific group by passing in the `groupId`

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .base64("SGVsbG8gV29ybGQh")
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Add optional keyvalues to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .base64("SGVsbG8gV29ybGQh")
  .keyvalues({
    env: "prod"
  })
```

### name (Optional)

* Type: `string`

Add optional name to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .base64("SGVsbG8gV29ybGQh")
  .name("hello.txt")
```

### url (Optional)

* Type: `string`

Pass in a presigned upload URL created with [createSignedURL](./create-signed-url)

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .file(file)
  .url(url)
```

### key (Optional)

* Type: `string`

Upload a file using a secondary API key generated through `keys.create()`

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .base64("SGVsbG8gV29ybGQh")
  .key("GENERATED_API_JWT")
```


# cid
Source: https://docs.pinata.cloud/sdk/upload/public/cid

`org:files:write`

Pin an existing CID on IPFS to your Pinata account

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const pin = await pinata.upload.public.cid("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
```

## Returns

```typescript theme={null}
type PinByCIDResponse = {
	id: string;
	cid: string;
	status: "prechecking" | "retrieving";
	name: string;
};
```

## Parameters

### cid

* Type: `string`

Target CID already on IPFS

```typescript theme={null}
const pin = await pinata.upload.public.cid("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Add optional keyvalues to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .cid("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
  .keyvalues({
    env: "prod"
  })
```

### name (Optional)

* Type: `string`

Add optional name to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .cid("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
  .name("hello.txt")
```

### group (Optional)

* Type: `string`

Upload to a specific group by passing in the `groupId`

```typescript theme={null}
const pin = await pinata.upload.public
  .cid("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
```

### key (Optional)

* Type: `string`

Upload a file using a secondary API key generated through `keys.create()`

```typescript theme={null}
const pin = await pinata.upload.public
  .cid("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
  .key("GENERATED_API_JWT")
```

### peerAddress (Optional)

* Type: `string[]`

Accepts an array of host node IDs to peer with

```typescript theme={null}
const pin = await pinata.upload
  .cid("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng")
  .peerAddress([
    "/ip4/hostNode1ExternalIP/tcp/4001/ipfs/hostNode1PeerId",
    "/ip4/hostNode2ExternalIP/tcp/4001/ipfs/hostNode2PeerId"
  ])
```


# createSignedURL
Source: https://docs.pinata.cloud/sdk/upload/public/create-signed-url

`org:files:write`

Create a signed upload URL for a file upload. This method is ideal when you want to authorize server side but upload on the client; check out [this doc](/files/uploading-files#client-side-uploads) for more details.

<Note>
  All the information about the upload such as the name, group, keyvalues, etc. must be part of the signed URL in order for those values to go through. If you have a basic signed URL with no extra parameters and then try to add fields like name, group, etc. they will not go through.
</Note>

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signedURL = await pinata.upload.public
  .createSignedURL({
    expires: 30
  });

const upload = await pinata.upload.public
  .file(file)
  .url(signedURL)
```

## Returns

* Type: `string`

The full signed URL

```
https://uploads.pinata.cloud/v3/files/209bb44c-e987-47c4-a9e3-a88e02d4d8e9?X-Algorithm=PINATA2&X-Date=1734379351&X-Expires=300&X-Method=%5B%22HEAD%22%2C%22PATCH%22%2C%22POST%22%5D&X-User-ID=eb73db21-10fa-4005-b97c-639e19e82d60&X-Signature=<SIGNATURE>
```

## Parameters

### expires

* Type: `number`

The number of seconds the signed URL should be valid for

```typescript {2} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
});
```

### name (Optional)

* Type: `string`

Name for the file to be uploaded

```typescript {3} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	name: "My Cool File"
});
```

### mimeTypes (Optional)

* Type: `string[]`

Specify allowed file mime types and prevent uploads from files that do not match. Accepts wildcard mime types as well.

```typescript {3-6} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	mimeTypes: [
	  "image/*",
		"application/json"
	]
});
```

### maxFileSize (Optional)

* Type: `number`

Restrict upload to a specified file size in `bytes`

```typescript {3} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	maxFileSize: 50000 // 50kb
});
```

### groupId (Optional)

* Type: `string`

The target groupId the file would be uploaded to

```typescript {3} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	groupId: "ad4bc3bf-8794-49e7-94ff-fea1ce745779"
});
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Keyvalue pairs for the uploaded file

```typescript {3-5} theme={null}
const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	keyvalues: {
	  env: "prod"
	}
});
```

### date (Optional)

* Type: `number`

A UNIX timestamp of the date a URL is signed

```typescript {1-2,6} theme={null}
const date = Math.floor(new Date().getTime() / 1000);
//date: 1724943711

const url = await pinata.upload.public.createSignedURL({
	expires: 30,
	date: date
});
```


# file
Source: https://docs.pinata.cloud/sdk/upload/public/file

`org:files:write`

Upload a single file to Pinata

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const file = new File(["hello world!"], "hello.txt", { type: "text/plain" })
const upload = await pinata.upload.public.file(file)
```

### Local Files

If you need to upload files from a local file source you can use `fs` to feed a file into a `blob`, then turn that `blob` into a `File`.

```typescript {10-12} theme={null}
const { PinataSDK } = require("pinata")
const fs = require("fs")
const { Blob } = require("buffer")

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud"
})

const blob = new Blob([fs.readFileSync("./hello-world.txt")]);
const file = new File([blob], "hello-world.txt", { type: "text/plain"})
const upload = await pinata.upload.public.file(file);
```

## Returns

```typescript theme={null}
type UploadResponse = {
	id: string;
	name: string;
	cid: string;
	size: number;
	created_at: string;
	number_of_files: number;
	mime_type: string;
	group_id: string | null;
	keyvalues: {
		[key: string]: string;
	};
	vectorized: boolean;
	network: string;
};
```

## Parameters

### file

* Type: `File` object

Accepts a File object in accordance with the [W3C File API](https://w3c.github.io/FileAPI/#file-section).

```typescript {3} theme={null}
const blob = new Blob(["hello world!"], { type: "text/plain" })
const file = new File([blob], "hello.txt", { type: "text/plain" })
const upload = await pinata.upload.public.file(file)
```

In most environments you can also pass a Blob here as well.

```typescript {2} theme={null}
const blob = new Blob(["hello world!"], { type: "text/plain" })
const upload = await pinata.upload.public.file(blob)
```

### group (Optional)

* Type: `string`

Upload to a specific group by passing in the `groupId`

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .file(file)
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Add optional keyvalues to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .file(file)
  .keyvalues({
    env: "prod"
  })
```

### name (Optional)

* Type: `string`

Add optional name to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .file(file)
  .name("hello.txt")
```

### url (Optional)

* Type: `string`

Pass in a presigned upload URL created with [createSignedURL](./create-signed-url)

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .file(file)
  .url(url)
```

### key (Optional)

* Type: `string`

Upload a file using a secondary API key generated through `keys.create()`

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .file(file)
  .key("GENERATED_API_JWT")
```

### car (Optional)

* Type: `boolean`

Upload a file as a raw CAR file

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .file(file)
  .car()
```


# fileArray
Source: https://docs.pinata.cloud/sdk/upload/public/file-array

`org:files:write`

Upload an array of files to Pinata as a folder

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const file1 = new File(["hello world!"], "hello.txt", { type: "text/plain" })
const file2 = new File(["hello world again!"], "hello2.txt", { type: "text/plain" })
const upload = await pinata.upload.public.fileArray([file1, file2])
```

## Returns

```typescript theme={null}
type UploadResponse = {
	id: string;
	name: string;
	cid: string;
	size: number;
	created_at: string;
	number_of_files: number;
	mime_type: string;
	group_id: string | null;
	keyvalues: {
		[key: string]: string;
	};
	vectorized: boolean;
	network: string;
};
```

## Parameters

### file

* Type: `File[]` object

Accepts an array of File objects in accordance with the [W3C File API](https://w3c.github.io/FileAPI/#file-section).

```typescript theme={null}
const file1 = new File([blob1], "hello1.txt", { type: "text/plain" })
const file2 = new File([blob2], "hello2.txt", { type: "text/plain" })
const upload = await pinata.upload.public.fileArray([file1, file2])
```

### group (Optional)

* Type: `string`

Upload to a specific group by passing in the `groupId`

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .fileArray([file1, file2])
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Add optional keyvalues to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .fileArray([file1, file2])
  .keyvalues({
    env: "prod"
  })
```

### name (Optional)

* Type: `string`

Add optional name to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .fileArray([file1, file2])
  .name("folder")
```

### key (Optional)

* Type: `string`

Upload a file using a secondary API key generated through `keys.create()`

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .fileArray([file1, file2])
  .key("GENERATED_API_JWT")
```

### url (Optional)

* Type: `string`

Pass in a presigned upload URL created with [createSignedURL](./create-signed-url)

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .fileArray([file1, file2])
  .url(url)
```


# json
Source: https://docs.pinata.cloud/sdk/upload/public/json

`org:files:write`

Upload a JSON object to Pinata

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const upload = await pinata.upload.public.json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
})
```

## Returns

```typescript theme={null}
type UploadResponse = {
	id: string;
	name: string;
	cid: string;
	size: number;
	created_at: string;
	number_of_files: number;
	mime_type: string;
	group_id: string | null;
	keyvalues: {
		[key: string]: string;
	};
	vectorized: boolean;
	network: string;
};
```

## Parameters

### JSON

* Type: `Record<string, unknown>`

Accepts an object that is turned into JSON

```typescript theme={null}
const upload = await pinata.upload.public.json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
})
```

### group (Optional)

* Type: `string`

Upload to a specific group by passing in the `groupId`

```typescript {7} theme={null}
const upload = await pinata.upload.public
  .json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
  })
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Add optional keyvalues to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
  })
  .keyvalues({
    env: "prod"
  })
```

### name (Optional)

* Type: `string`

Add optional name to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
  })
  .name("metadata.json")
```

### url (Optional)

* Type: `string`

Pass in a presigned upload URL created with [createSignedURL](./create-signed-url)

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .json({
    content: "console.log('hello world!)",
    name: "helloworld.ts",
    lang: "ts"
  })
  .url(url)
```

### key (Optional)

* Type: `string`

Upload a file using a secondary API key generated through `keys.create()`

```typescript {7} theme={null}
const upload = await pinata.upload.public
    .json({
        content: "console.log('hello world!)",
        name: "helloworld.ts",
        lang: "ts"
    })
  .key("GENERATED_API_JWT")
```


# url
Source: https://docs.pinata.cloud/sdk/upload/public/url

`org:files:write`

Upload the contents of a URL to Pinata

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const upload = await pinata.upload.public.url("https://i.imgur.com/u4mGk5b.gif")
```

## Returns

```typescript theme={null}
type UploadResponse = {
	id: string;
	name: string;
	cid: string;
	size: number;
	created_at: string;
	number_of_files: number;
	mime_type: string;
	group_id: string | null;
	keyvalues: {
		[key: string]: string;
	};
	vectorized: boolean;
	network: string;
};
```

## Parameters

### url

* Type: `string`

Accepts a URL in the form of a string. The mimetype of the URL body provided in the headers typically determines the resulting file.

```typescript theme={null}
const upload = await pinata.upload.public.url("https://i.imgur.com/u4mGk5b.gif")
```

### group (Optional)

* Type: `string`

Upload to a specific group by passing in the `groupId`

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .url("https://i.imgur.com/u4mGk5b.gif")
  .group("b07da1ff-efa4-49af-bdea-9d95d8881103")
```

### keyvalues (Optional)

* Type: `Record<string, string>`

Add optional keyvalues to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .url("https://i.imgur.com/u4mGk5b.gif")
  .keyvalues({
    env: "prod"
  })
```

### name (Optional)

* Type: `string`

Add optional name to file

```typescript {3-8} theme={null}
const upload = await pinata.upload.public
  .url("https://i.imgur.com/u4mGk5b.gif")
  .name("pinnie.gif")
```

### url (Optional)

* Type: `string`

Pass in a presigned upload URL created with [createSignedURL](./create-signed-url)

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .url(url)
  .url(url)
```

### key (Optional)

* Type: `string`

Upload a file using a secondary API key generated through `keys.create()`

```typescript {3} theme={null}
const upload = await pinata.upload.public
  .url("https://i.imgur.com/u4mGk5b.gif")
  .key("GENERATED_API_JWT")
```


# V2 Migration Guide
Source: https://docs.pinata.cloud/sdk/v2-migration-guide



The `pinata@1.x` package became a Private IPFS only SDK and the Public IPFS SDK was moved to `pinata-web3`. This was also a result of our APIs being disconnected as well. Due to this problem we've unified our Public and Private IPFS APIs in our V3 API, and we have also unified them in our SDK in a new V2 release. This document will walk you through how to migrate from previous versions of either `pinata` or `pinata-web3`.

## `pinata@1.x`

The `pinata` package was originally just for Private IPFS but now supports both Public and Private IPFS in `pinata@2.x`.

### API Keys

If you happened to be using a scoped API key for [legacy endpoints](/api-reference/endpoint/ipfs/pin-file-to-ipfs) like `pinFileToIPFS` or `pinJSONToIPFS` then you will need to create a new API key for the V2 SDK which uses the new [V3 endpoints](/api-reference/introduction). If you want to scope your endpoint for the new API you can use the [API docs for key creation](/api-reference/endpoint/v3-create-api-key) to do so.

### Installation and Initialization

Install the latest version by running the following command:

```bash theme={null}
npm i pinata@latest
```

Initalizing the SDK works the exact same way in previous versions

```typescript theme={null}
const pinata = new PinataSDK({
  pinataJwt: "PINATA_JWT",
  pinataGateway: "example-gateway.mypinata.cloud",
});
```

### Public & Private Methods

In `pinata@1.x` all methods were direct. In V2 there are public and private methods for the following classes:

* `upload`
* `files`
* `groups`
* `gateways`
* `signatures`

This means you can simple pass in `public` or `private` after the main class to access those specific networks.

<CodeGroup>
  ```typescript Before theme={null}
  const upload = await pinata.upload.file(file)
  ```

  ```typescript After theme={null}
  // Public IPFS
  const upload = await pinata.upload.public.file(file)
  // Private IPFS
  const upload = await pinata.upload.private.file(file)
  ```
</CodeGroup>

### Accessing Private IPFS Files

The method `createSignedURL` for accessing files on Private IPFS has been renamed to `createAccessLink`

<CodeGroup>
  ```typescript Before theme={null}
  const url = await pinata.gateways.createSignedURL({
  	cid: "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq",
  	expires: 30,
  });
  ```

  ```typescript After theme={null}
  const url = await pinata.gateways.private.createAccessLink({
  	cid: "bafkreib4pqtikzdjlj4zigobmd63lig7u6oxlug24snlr6atjlmlza45dq",
  	expires: 30,
  });
  ```
</CodeGroup>

### Uploads with Metadata

When uploading files the `addMetadata()` method has been replaced with `name()` and `keyvalues()` to better match querying and listing files with those attributes.

<CodeGroup>
  ```typescript Before {4-7} theme={null}
  const upload = await pinata.upload
    .file(file)
    .addMetadata({
      name: "hello.txt",
      keyvalues: {
        env: "prod"
      }
    })
  ```

  ```typescript After {3-6} theme={null}
  const upload = await pinata.upload.public
    .file(file)
    .keyvalues({
      env: "prod"
    })
    .name("hello.txt")
  ```
</CodeGroup>

## `pinata-web3@0.x`

The `pinata-web3` package previously was only supporting Public IPFS, and lacked some of the more natural organization that the `pinata` package had. With `pinata@2.x` the SDK supprts both Public and Private IPFS and is recommended that you migrate to `pinata` instead of continuing to use `pinata-web3`. This guide will walk through the changes that will need to be made.

### API Keys

If you happened to be using a scoped API key for [legacy endpoints](/api-reference/endpoint/ipfs/pin-file-to-ipfs) like `pinFileToIPFS` or `pinJSONToIPFS` then you will need to create a new API key for the V2 SDK which uses the new [V3 endpoints](/api-reference/introduction). If you want to scope your endpoint for the new API you can use the [API docs for key creation](/api-reference/endpoint/v3-create-api-key) to do so.

### Installation and Initialization

Install the latest version by running the following command:

```bash theme={null}
npm i pinata@latest
```

Initalizing the SDK works the exact same way in previous versions, but you will need to change your imports from `pinata-web3` to `pinata`.

<CodeGroup>
  ```typescript Before theme={null}
  import { PinataSDK } from "pinata-web3"

  const pinata = new PinataSDK({
    pinataJwt: "PINATA_JWT",
    pinataGateway: "example-gateway.mypinata.cloud",
  });
  ```

  ```typescript After theme={null}
  import { PinataSDK } from "pinata" // Import changed

  const pinata = new PinataSDK({
    pinataJwt: "PINATA_JWT",
    pinataGateway: "example-gateway.mypinata.cloud",
  });
  ```
</CodeGroup>

### Public & Private Methods

In `pinata-web3@0.x` all methods were direct. In V2 there are public and private methods for the following classes:

* `upload`
* `files`
* `groups`
* `gateways`
* `signatures`

This means you can simple pass in `public` or `private` after the main class to access those specific networks.

<CodeGroup>
  ```typescript Before theme={null}
  const upload = await pinata.upload.file(file)
  ```

  ```typescript After theme={null}
  // Public IPFS
  const upload = await pinata.upload.public.file(file)
  // Private IPFS
  const upload = await pinata.upload.private.file(file)
  ```
</CodeGroup>

### File Management

In `pinata-web3` the methods to `listFiles()`, `updateMetadata()`, `unpin()` under the main PinataSDK class have been moved to a separate `files` class for better organization.

#### `listFiles()` -> `files.<network>.list()`

<CodeGroup>
  ```typescript Before theme={null}
  const files = await pinata.listFiles()
  ```

  ```typescript After theme={null}
  // Public IPFS
  const files = await pinata.files.public.list()
  // Private IPFS
  const files = await pinata.files.private.list()
  ```
</CodeGroup>

#### `updateMetadata()` -> `files.<network>.update()`

<CodeGroup>
  ```typescript Before theme={null}
  const update = await pinata.updateMedatadata({
    cid: "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4",
    name: "Pinnie V2",
    keyValues: {
      whimsey: 200
    }
  })
  ```

  ```typescript After theme={null}
  // Public IPFS
  const update = await pinata.files.public.update({
    id: "52681e41-86f4-407b-8f79-33a7e7e5df68",
    name: "New File Name",
    keyvalues: {
      env: "prod"
    }
  })
  // Private IPFS
  const update = await pinata.files.private.update({
    id: "52681e41-86f4-407b-8f79-33a7e7e5df68",
    name: "New File Name",
    keyvalues: {
      env: "prod"
    }
  })
  ```
</CodeGroup>

#### `unpin()` -> `files.<network>.delete()`

<CodeGroup>
  ```typescript Before theme={null}
  const unpin = await pinata.unpin([
    "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
  ])
  ```

  ```typescript After theme={null}
  // Public IPFS
  const deletedFiles = await pinata.files.public.delete([
    "4ad9d3d1-4ab4-464c-a42a-3027fc39a546"
  ])

  // Private IPFS
  const deletedFiles = await pinata.files.private.delete([
    "4ad9d3d1-4ab4-464c-a42a-3027fc39a546"
  ])
  ```
</CodeGroup>

#### `pinJobs()` -> `files.public.queue()`

To list you pending pin by CID queue you can use the `queue()` method.

<CodeGroup>
  ```typescript Before theme={null}
  const queue = await pinata.pinJobs().status("prechecking")
  ```

  ```typescript After theme={null}
  const queue = await pinata.files.public.queue().status("prechecking")
  ```
</CodeGroup>

### Swaps are now under Files

In `pinata-web3` the Hot Swap methods were under the `gateways` class. These have been moved to the `files` class instead. Some of the naming convention has been updated as well.

#### `swapCid()` -> `addSwap()`

<CodeGroup>
  ```typescript Before theme={null}
  const swap = await pinata.gateways.swapCid({
    cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
    swapCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu"
  })
  ```

  ```typescript After theme={null}
  const swap = await pinata.files.public.addSwap({
  	cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
  	swapCid: "bafkreihumyr3bgxulu45ghws33xokwjm5o7xnkkgakaz66ldtylwiecnhu"
  })
  ```
</CodeGroup>

#### `swapHistory()` -> `getSwapHistory()`

<CodeGroup>
  ```typescript Before theme={null}
  const history = await pinata.gateways.swapHistory({
    cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
    domain: "discordpinnie.mypinata.cloud"
  })
  ```

  ```typescript After theme={null}
  const history = await pinata.files.public.getSwapHistory({
    cid: "bafkreibbvdqf5ekc2crouowv7vtjbcmbjoiysegslmmqc6jrxbaa43xske",
    domain: "discordpinnie.mypinata.cloud"
  })
  ```
</CodeGroup>

### Groups

Groups have been updated to follow the file ID paradigm that is now part of the SDK, and so has the method names for adding or removing files

#### `addCids()` -> `addFiles()`

<CodeGroup>
  ```typescript Before theme={null}
  const group = await pinata.groups.addCids({
  	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
  	cids: ["QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng"],
  });
  ```

  ```typescript After theme={null}
  const group = await pinata.groups.public.addFiles({
  	groupId: "3778c10d-452e-4def-8299-ee6bc548bdb0",
  	files: [
  	  "7e18c4a4-9501-44de-8f81-403db7de0e39",
  		"a606ef7e-70a0-40ad-9b8a-60563e009655"
  	],
  });
  ```
</CodeGroup>

<Tip>
  [See full reference](/sdk/groups/public)
</Tip>

### Analytics

In `pinata-web3` analytics was grouped under the `gateways` class. In `pinata@2.x` it has been moved into it's own class. Additionally the methods inside have been completely rewired to fit needs better.

<CodeGroup>
  ```typescript Before theme={null}
  const analytics = await pinata.gateways.topUsageAnalytics({
    domain: "docs.mypinata.cloud",
    start: "2024-08-01",
    end: "2024-08-15",
    sortBy: "requests",
    attribute: "cid"
  })
  .cid("QmVLwvmGehsrNEvhcCnnsw5RQNseohgEkFNN1848zNzdng");

  const analytics = await pinata.gateways.dateIntervalAnalytics({
    domain: "docs.mypinata.cloud",
    start: "2024-08-01",
    end: "2024-08-15",
    interval: "day"
  })
  .sort("desc");
  ```

  ```typescript After theme={null}
  const clicks = await pinata.analytics.requests
    .days(30)
    .limit(10)
    .cid("<CID>")

  const bandwidth = await pinata.analytics.bandwidth
    .days(30)
    .limit(10)
    .cid("<CID>")
  ```
</CodeGroup>

<Tip>
  See [Analytics Reference](/sdk/analytics/requests) for more info
</Tip>

### Usage Class Removed

The `pinata.usage` class in the `pinata-web3` package has been removed in `pinata@2.x`.


# Community SDKs
Source: https://docs.pinata.cloud/tools/community-sdks



## IPFS Gateway Tools SDK

This is a convenience SDK that allows developers to take an IPFS URL of any kind and convert it to a Gateway URL of their choosing. This is especially useful when you want to load IPFS content through your own [Dedicated Gateway](/gateways/dedicated-ipfs-gateways).

[https://www.npmjs.com/package/@pinata/ipfs-gateway-tool](https://www.npmjs.com/package/@pinata/ipfs-gateway-tool)

## Community SDKs

These SDKs have been written by members of the Pinata community. They have not been audited by anyone at Pinata, nor can we vouch for their security or viability.

### Python

[https://github.com/Vourhey/pinatapy](https://github.com/Vourhey/pinatapy)

[https://github.com/edmondyu/pinata-python-util](https://github.com/edmondyu/pinata-python-util)

### Go

[https://gitlab.com/benoit74/pinata-cli](https://gitlab.com/benoit74/pinata-cli)

### Rust

[https://github.com/perfectmak/pinata-sdk](https://github.com/perfectmak/pinata-sdk)

### .NET

[https://www.nuget.org/packages/Pinata.Client/](https://www.nuget.org/packages/Pinata.Client/)

### Elixir

[https://github.com/m1ome/ex\_pinata](https://github.com/m1ome/ex_pinata)


# IPFS CLI
Source: https://docs.pinata.cloud/tools/ipfs-cli

The official CLI for Pinata written in Go

![cover](https://dweb.mypinata.cloud/ipfs/QmNcdx9t48z7RQUXUZZHmuc4zBfyBxKLjDfEgmfhiop7j7?img-format=webp)

The IPFS CLI is a tool you can use alongside your account to upload and manage files through your terminal. The source code can be found in the link below.

<Card icon="github" href="https://github.com/PinataCloud/ipfs-cli" title="Source Code" />

## Installation

<Note>
  If you are on Windows please use WSL when installing. If you get an error that it was not able to resolve the github host run `git config --global --unset http.proxy`
</Note>

### Install Script

The easiest way to install is to copy and paste this script into your terminal

```bash theme={null}
curl -fsSL https://cli.pinata.cloud/install | bash
```

### Homebrew

If you are on MacOS and have homebrew installed you can run the command below to install the CLI

```
brew install PinataCloud/ipfs-cli/ipfs-cli
```

### Building from Source

To build and install from source make sure you have [Go](https://go.dev/) installed on your computer and the following command returns a version:

```
go version
```

Then paste and run the following into your terminal:

```
git clone https://github.com/PinataCloud/ipfs-cli && cd ipfs-cli && go install .
```

### Linux Binary

As versions are released you can visit the [Releases](https://github.com/PinataCloud/ipfs-cli/releases) page and download the appropriate binary for your system, them move it into your bin folder.

For example, this is how I install the CLI for my Raspberry Pi

```
wget https://github.com/PinataCloud/ipfs-cli/releases/download/v0.1.0/ipfs-cli_Linux_arm64.tar.gz

tar -xzf ipfs-cli_Linux_arm64.tar.gz

sudo mv pinata /usr/bin
```

## Usage

The Pinata CLI is equipped with the majortiry of features on both the Public IPFS API and Private IPFS API.

### `auth`

With the CLI installed you will first need to authenticate it with your [Pinata JWT](https://docs.pinata.cloud/account-management/api-keys). Run this command and follow the steps to setup the CLI!

```
pinata auth
```

### `config`

Set a default IPFS network, can be either `public` or `private`. You can always change this at any time or override in individual commands. If none is set the default is `public`.

```
NAME:
   pinata config - Configure Pinata CLI settings

USAGE:
   pinata config command [command options] [arguments...]

COMMANDS:
   network, net  Set default network (public or private)
   help, h       Shows a list of commands or help for one command

OPTIONS:
   --help, -h  show help
```

### `upload`

```
NAME:
   pinata upload - Upload a file to Pinata

USAGE:
   pinata upload [command options] [path to file]

OPTIONS:
   --group value, -g value  Upload a file to a specific group by passing in the groupId
   --name value, -n value   Add a name for the file you are uploading. By default it will use the filename on your system. (default: "nil")
   --verbose                Show upload progress (default: false)
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h               show help
```

### `files`

```
NAME:
   pinata files - Interact with your files on Pinata

USAGE:
   pinata files command [command options] [arguments...]

COMMANDS:
   delete, d  Delete a file by ID
   get, g     Get file info by ID
   update, u  Update a file by ID
   list, l    List most recent files
   help, h    Shows a list of commands or help for one command

OPTIONS:
   --help, -h  show help
```

#### `get`

```
NAME:
   pinata files get - Get file info by ID

USAGE:
   pinata files get [command options] [ID of file]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

#### `list`

```
NAME:
   pinata files list - List most recent files

USAGE:
   pinata files list [command options] [arguments...]

OPTIONS:
   --name value, -n value                                           Filter by name of the target file
   --cid value, -c value                                            Filter results by CID
   --group value, -g value                                          Filter results by group ID
   --mime value, -m value                                           Filter results by file mime type
   --amount value, -a value                                         The number of files you would like to return
   --token value, -t value                                          Paginate through file results using the pageToken
   --cidPending                                                     Filter results based on whether or not the CID is pending (default: false)
   --keyvalues value, --kv value [ --keyvalues value, --kv value ]  Filter results by metadata keyvalues (format: key=value)
   --network value, --net value                                     Specify the network (public or private). Uses default if not specified
   --help, -h                                                       show help
```

#### `update`

```
NAME:
   pinata files update - Update a file by ID

USAGE:
   pinata files update [command options] [ID of file]

OPTIONS:
   --name value, -n value        Update the name of a file
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

#### `delete`

```
NAME:
   pinata files delete - Delete a file by ID

USAGE:
   pinata files delete [command options] [ID of file]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

### `groups`

```
NAME:
   pinata groups - Interact with file groups

USAGE:
   pinata groups command [command options] [arguments...]

COMMANDS:
   create, c  Create a new group
   list, l    List groups on your account
   update, u  Update a group
   delete, d  Delete a group by ID
   get, g     Get group info by ID
   add, a     Add a file to a group
   remove, r  Remove a file from a group
   help, h    Shows a list of commands or help for one command

OPTIONS:
   --help, -h  show help
```

#### `create`

```
NAME:
   pinata groups create - Create a new group

USAGE:
   pinata groups create [command options] [name of group]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

#### `get`

```
NAME:
   pinata groups get - Get group info by ID

USAGE:
   pinata groups get [command options] [ID of group]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

#### `list`

```
NAME:
   pinata groups list - List groups on your account

USAGE:
   pinata groups list [command options] [arguments...]

OPTIONS:
   --amount value, -a value      The number of groups you would like to return (default: "10")
   --name value, -n value        Filter groups by name
   --token value, -t value       Paginate through results using the pageToken
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

#### `add`

```
NAME:
   pinata groups add - Add a file to a group

USAGE:
   pinata groups add [command options] [group id] [file id]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

#### `remove`

```
NAME:
   pinata groups remove - Remove a file from a group

USAGE:
   pinata groups remove [command options] [group id] [file id]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

### `gateways`

```
NAME:
   pinata gateways - Interact with your gateways on Pinata

USAGE:
   pinata gateways command [command options] [arguments...]

COMMANDS:
   set, s   Set your default gateway to be used by the CLI
   open, o  Open a file in the browser
   link, l  Get either an IPFS link for a public file or a temporary access link for a Private IPFS file
   help, h  Shows a list of commands or help for one command

OPTIONS:
   --help, -h  show help
```

#### `set`

<Tip>
  Use the command with no arguments and get a list of your gateways to choose from!
</Tip>

```
NAME:
   pinata gateways set - Set your default gateway to be used by the CLI

USAGE:
   pinata gateways set [command options] [domain of the gateway]

OPTIONS:
   --help, -h  show help
```

#### `link`

```
NAME:
   pinata gateways link - Get either an IPFS link for a public file or a temporary access link for a Private IPFS file

USAGE:
   pinata gateways link [command options] [cid of the file, seconds the url is valid for]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

#### `open`

```
NAME:
   pinata gateways open - Open a file in the browser

USAGE:
   pinata gateways open [command options] [CID of the file]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

### `keys`

```
NAME:
   pinata keys - Create and manage generated API keys

USAGE:
   pinata keys command [command options] [arguments...]

COMMANDS:
   create, c  Create an API key with admin or scoped permissions
   list, l    List and filter API key
   revoke, r  Revoke an API key
   help, h    Shows a list of commands or help for one command

OPTIONS:
   --help, -h  show help
```

#### `create`

```
NAME:
   pinata keys create - Create an API key with admin or scoped permissions

USAGE:
   pinata keys create [command options] [arguments...]

OPTIONS:
   --name value, -n value                                       Name of the API key
   --admin, -a                                                  Set the key as Admin (default: false)
   --uses value, -u value                                       Max uses a key can use (default: 0)
   --endpoints value, -e value [ --endpoints value, -e value ]  Optional array of endpoints the key is allowed to use
   --help, -h                                                   show help
```

#### `list`

```
NAME:
   pinata keys list - List and filter API key

USAGE:
   pinata keys list [command options] [arguments...]

OPTIONS:
   --name value, -n value    Name of the API key
   --revoked, -r             Set the key as Admin (default: false)
   --exhausted, -e           Filter keys that are exhausted or not (default: false)
   --uses, -u                Filter keys that do or don't have limited uses (default: false)
   --offset value, -o value  Offset the number of results to paginate
   --help, -h                show help
```

#### `revoke`

```
NAME:
   pinata keys revoke - Revoke an API key

USAGE:
   pinata keys revoke [command options] [key]

OPTIONS:
   --help, -h  show help
```

### `swaps`

```
NAME:
   pinata swaps - Interact and manage hot swaps on Pinata

USAGE:
   pinata swaps command [command options] [arguments...]

COMMANDS:
   list, l    List swaps for a given gateway domain or for your config gateway domain
   add, a     Add a swap for a CID
   delete, d  Remeove a swap for a CID
   help, h    Shows a list of commands or help for one command

OPTIONS:
   --help, -h  show help
```

#### `list`

```
NAME:
   pinata swaps list - List swaps for a given gateway domain or for your config gateway domain

USAGE:
   pinata swaps list [command options] [cid] [optional gateway domain]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

#### `add`

```
NAME:
   pinata swaps add - Add a swap for a CID

USAGE:
   pinata swaps add [command options] [cid] [swap cid]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

#### `delete`

```
NAME:
   pinata swaps delete - Remeove a swap for a CID

USAGE:
   pinata swaps delete [command options] [cid]

OPTIONS:
   --network value, --net value  Specify the network (public or private). Uses default if not specified
   --help, -h                    show help
```

## Contact

If you have any questions please feel free to reach out to us!

[team@pinata.cloud](mailto:team@pinata.cloud)


# Pinata Expo Hooks
Source: https://docs.pinata.cloud/tools/pinata-expo-hooks

A collection of Expo compatible hooks to use with Pinata

<Warning>
  Pinata Expo Hooks are still under developement and will only work in iOS and Android at the moment. Please [reach out](mailto:steve@pinata.cloud) if you have any issues!
</Warning>

## Installation

Install with your package manager of choice

```bash theme={null}
pnpm i pinata-expo-hooks@latest
```

## Source Code

`pinata-expo-hooks` is MIT open sourced and can be accessed on GitHub with the link below

<Card title="PinataCloud/pinata-expo" icon="github" href="https://github.com/PinataCloud/pinata-expo" />

## Usage

Import at the top of your desired page or component

```typescript theme={null}
import { useUpload } from "pinata-expo-hooks";
```

Inside your page or component use the hook to extract methods and state

```typescript theme={null}
const {
	upload, // Method to upload a file using a presigned URL
	progress, // Progress state as integer
	loading, // Boolean uploading state
	uploadResponse, // File ID used to fetch the file info server side
	error, // Error state
	pause, // Pause upload method
	resume, // Resume upload method
	cancel, // Cancel current upload method
} = useUpload();
```

Return types for `useUpload`

```typescript theme={null}
export type UseUploadReturn = {
	progress: number;
	loading: boolean;
	error: Error | null;
	uploadResponse: string | null;
	upload: (
		fileUri: string,
		network: "public" | "private",
		url: string,
		options?: UploadOptions,
	) => Promise<void>;
	pause: () => void;
	resume: () => void;
	cancel: () => void;
};
```

To upload a file you must already have a server setup that returns a [Presigned URL](/files/presigned-urls). Then you can pass it into the `upload` method like so.

```typescript theme={null}
await upload(fileUri, "public", "presigned_URL", {
	name: fileName || "Upload from Expo",
	keyvalues: {
		app: "Pinata Expo Demo",
		timestamp: Date.now().toString(),
	},
});
```

<Tip>
  [Learn how to send Presigned URLs from your server](/frameworks/hono)
</Tip>

Below are the available `UploadOptions` that can be passed into `upload`

```typescript theme={null}
export type UploadOptions = {
	customHeaders?: Record<string, string>;
	name?: string;
	keyvalues?: Record<string, string>;
	groupId?: string;
	chunkSize?: number; // Defaults to 1014 * 256 * 20 * 10 (~52MB)
};
```

Once a file is uploaded the `uploadResponse` will contain the CID for the file.

Below is a full example of implementing the `useUpload` hook with progress and abilities to pause and resume the upload.

```typescript theme={null}
import { Image } from "expo-image";
import { View, Text, Button, StyleSheet } from "react-native";
import * as ImagePicker from "expo-image-picker";
import * as DocumentPicker from "expo-document-picker";
import { useState } from "react";
import ParallaxScrollView from "@/components/ParallaxScrollView";
import { useUpload } from "pinata-expo-hooks";

const SERVER_URL = "http://localhost:8787"; // Server that returns a presigned_url

export default function HomeScreen() {
	const {
		upload, // Method to upload a file using a presigned URL
		progress, // Progress state as integer
		loading, // Boolean uploading state
		uploadResponse, // CID for the uploaded file
		error, // Error state
		pause, // Pause upload method
		resume, // Resume upload method
		cancel, // Cancel current upload method
	} = useUpload();
	const [fileUri, setFileUri] = useState<string | null>(null);
	const [fileName, setFileName] = useState<string | null>(null);

	const pickImage = async () => {
		const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();

		if (status !== "granted") {
			alert("Sorry, we need camera roll permissions to make this work!");
			return;
		}

		const result = await ImagePicker.launchImageLibraryAsync({
			mediaTypes: ImagePicker.MediaTypeOptions.All,
			allowsEditing: false,
			quality: 1,
		});

		if (!result.canceled && result.assets && result.assets.length > 0) {
			setFileUri(result.assets[0].uri);
			setFileName(result.assets[0].uri.split("/").pop() || "image");
		}
	};

	// Pick document from device
	const pickDocument = async () => {
		try {
			const result = await DocumentPicker.getDocumentAsync();

			if (result.canceled === false) {
				setFileUri(result.assets[0].uri);
				setFileName(result.assets[0].name);
			}
		} catch (err) {
			console.error("Error picking document", err);
		}
	};

	// Start the upload process
	const startUpload = async () => {
		if (!fileUri) {
			alert("Please select a file first");
			return;
		}
		try {
			const urlRes = await fetch(`${SERVER_URL}/presigned_url`);
			if (!urlRes.ok) {
				console.log(urlRes.status);
			}
			const urlData = await urlRes.json();
			await upload(
				fileUri,
				"public", // or 'private' if you want a private upload
				urlData.url,
				{
					name: fileName || "Upload from Expo",
					keyvalues: {
						app: "Pinata Expo Demo",
						timestamp: Date.now().toString(),
					},
				},
			);
		} catch (err) {
			console.error("Failed to start upload:", err);
			alert("Failed to start upload");
		}
	};

	// Progress bar component
	const ProgressBar = ({ value }: { value: number }) => {
		return (
			<View style={styles.progressBarContainer}>
				<View style={[styles.progressBar, { width: `${value}%` }]} />
			</View>
		);
	};

	return (
		<ParallaxScrollView
			headerBackgroundColor={{ light: "#A1CEDC", dark: "#1D3D47" }}
			headerImage={
				<Image
					source={require("@/assets/images/partial-react-logo.png")}
					style={styles.reactLogo}
				/>
			}
		>
			<View style={styles.container}>
				<Text style={styles.title}>Pinata IPFS Upload</Text>

				<View style={styles.buttonContainer}>
					<Button title="Pick Image" onPress={pickImage} />
					<Button title="Pick Document" onPress={pickDocument} />
				</View>

				{fileUri && (
					<View style={styles.fileInfoContainer}>
						<Text style={styles.fileInfo}>Selected: {fileName}</Text>
						<Button
							title="Upload to IPFS"
							onPress={startUpload}
							disabled={loading}
							color="#FF6AC1" // Pinata pink
						/>
					</View>
				)}

				{loading && (
					<View style={styles.uploadStatusContainer}>
						<Text style={styles.uploadStatusText}>
							Uploading... {Math.round(progress)}%
						</Text>
						<ProgressBar value={progress} />

						<View style={styles.uploadControlsContainer}>
							{progress < 100 && (
								<>
									<Button title="Pause" onPress={pause} color="#FFA15C" />
									<Button title="Resume" onPress={resume} color="#5CB8FF" />
									<Button title="Cancel" onPress={cancel} color="#FF5C5C" />
								</>
							)}
						</View>
					</View>
				)}

				{error && (
					<View style={styles.errorContainer}>
						<Text style={styles.errorTitle}>Upload Error</Text>
						<Text style={styles.errorText}>{error.message}</Text>
					</View>
				)}

				{uploadResponse && (
					<View style={styles.successContainer}>
						<Text style={styles.successTitle}>Upload Complete!</Text>
						<Text style={styles.successText}>File CID: {uploadResponse}</Text>
					</View>
				)}
			</View>
		</ParallaxScrollView>
	);
}

const styles = StyleSheet.create({
	titleContainer: {
		flexDirection: "row",
		alignItems: "center",
		gap: 8,
	},
	stepContainer: {
		gap: 8,
		marginBottom: 8,
	},
	reactLogo: {
		height: 178,
		width: 290,
		bottom: 0,
		left: 0,
		position: "absolute",
	},
	container: {
		flex: 1,
		padding: 20,
		backgroundColor: "#f5f5f5",
	},
	title: {
		fontSize: 24,
		fontWeight: "bold",
		marginBottom: 20,
		textAlign: "center",
	},
	buttonContainer: {
		flexDirection: "row",
		justifyContent: "space-around",
		marginBottom: 20,
	},
	fileInfoContainer: {
		backgroundColor: "#fff",
		padding: 15,
		borderRadius: 8,
		marginBottom: 20,
		elevation: 2,
		shadowColor: "#000",
		shadowOffset: { width: 0, height: 1 },
		shadowOpacity: 0.2,
		shadowRadius: 2,
	},
	fileInfo: {
		marginBottom: 10,
	},
	uploadStatusContainer: {
		backgroundColor: "#fff",
		padding: 15,
		borderRadius: 8,
		marginBottom: 20,
		elevation: 2,
		shadowColor: "#000",
		shadowOffset: { width: 0, height: 1 },
		shadowOpacity: 0.2,
		shadowRadius: 2,
	},
	uploadStatusText: {
		marginBottom: 10,
		fontWeight: "bold",
	},
	progressBarContainer: {
		height: 10,
		backgroundColor: "#e0e0e0",
		borderRadius: 5,
		overflow: "hidden",
		marginBottom: 15,
	},
	progressBar: {
		height: "100%",
		backgroundColor: "#FF6AC1", // Pinata pink
	},
	uploadControlsContainer: {
		flexDirection: "row",
		justifyContent: "space-around",
	},
	errorContainer: {
		backgroundColor: "#FFEBEE",
		padding: 15,
		borderRadius: 8,
		marginBottom: 20,
		borderLeftWidth: 4,
		borderLeftColor: "#FF5C5C",
	},
	errorTitle: {
		fontWeight: "bold",
		color: "#D32F2F",
		marginBottom: 5,
	},
	errorText: {
		color: "#D32F2F",
	},
	successContainer: {
		backgroundColor: "#E8F5E9",
		padding: 15,
		borderRadius: 8,
		marginBottom: 20,
		borderLeftWidth: 4,
		borderLeftColor: "#4CAF50",
	},
	successTitle: {
		fontWeight: "bold",
		color: "#2E7D32",
		marginBottom: 10,
	},
	successText: {
		color: "#2E7D32",
		marginBottom: 5,
	},
	pinningContainer: {
		flexDirection: "row",
		alignItems: "center",
		marginBottom: 5,
	},
	pinningText: {
		color: "#FF6AC1",
		marginRight: 10,
	},
});
```

## Questions

Please [contact us](mailto:steve@pinata.cloud) if you have any issues!


# Add File To Group
Source: https://docs.pinata.cloud/api-reference/endpoint/add-file-to-group

put /groups/{network}/{id}/ids/{file_id}
`org:groups:write`




# Add Signature to CId
Source: https://docs.pinata.cloud/api-reference/endpoint/add-signature-to-cid

post /files/{network}/signature/{cid}
`org:files:write`




# Add Swap
Source: https://docs.pinata.cloud/api-reference/endpoint/add-swap

put /files/{network}/swap/{cid}
`org:files:write`




# Cancel Request
Source: https://docs.pinata.cloud/api-reference/endpoint/cancel-pin-by-cid

DELETE /files/public/pin_by_cid/{id}
`org:files:write`




# Create Group
Source: https://docs.pinata.cloud/api-reference/endpoint/create-group

post /groups/{network}
`org:groups:write`




# Create Signed Upload URL
Source: https://docs.pinata.cloud/api-reference/endpoint/create-signed-upload-url

pinata-api-v3-uploads.yaml post /files/sign
`org:files:write`




# Delete File by ID
Source: https://docs.pinata.cloud/api-reference/endpoint/delete-file-by-id

delete /files/{network}/{id}
`org:files:write`




# Delete File Vectors
Source: https://docs.pinata.cloud/api-reference/endpoint/delete-file-vectors

delete /vectorize/files/{file_id}
`org:write`




# Delete Group
Source: https://docs.pinata.cloud/api-reference/endpoint/delete-group

delete /groups/{network}/{id}
`org:groups:write`




# Get File by ID
Source: https://docs.pinata.cloud/api-reference/endpoint/get-file-by-id

get /files/{network}/{id}
`org:files:read`




# Get Group
Source: https://docs.pinata.cloud/api-reference/endpoint/get-group

get /groups/{network}/{id}
`org:groups:read`




# Get Signature for a CID
Source: https://docs.pinata.cloud/api-reference/endpoint/get-signature-for-a-cid

get /files/{network}/signature/{cid}
`org:files:read`




# Create Download Link
Source: https://docs.pinata.cloud/api-reference/endpoint/get-signed-url

pinata-api-v3.yaml post /files/private/download_link
`org:files:write`




# Get Swap History
Source: https://docs.pinata.cloud/api-reference/endpoint/get-swap-history

get /files/{network}/swap/{cid}
`org:files:read`




# Create Custom Domain for Gateway
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-custom-domain-for-gateway

post /gateways/{id}/custom_domain
`org:gateways:write`




# Create Gateway
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway

post /gateways
`org:gateways:write`




# Create Gateway Host Origin Restriction
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway-host-origin-restriction

post /gateways/{id}/hosts
`org:gateways:write`




# Create Gateway IP Address Restriction
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway-ip-address-restriction

post /gateways/{id}/ips
`org:gateways:write`




# Create Gateway Key Restriction
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/create-gateway-key-restriction

post /gateways/{id}/access_tokens
`org:gateways:write`




# Delete Gateway
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/delete-gateway

delete /gateways/{id}
`org:gateways:write`




# Delete Gateway Custom Domain
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/delete-gateway-custom-domain

delete /gateways/{id}/custom_domain/{custom_domain_id}
`org:gateways:write`




# Gateway Custom Domain Details
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/gateway-custom-domain-details

get /gateways/{id}/custom_domain/{custom_domain_id}
`org:gateways:read`




# Gateway Details
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/gateway-details

get /gateways/{id}
`org:gateways:read`




# Gateway Domain Available
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/gateway-domain-available

get /gateways/exists/{domain}
`org:gateways:read`




# Get Marketplace Plugin Details
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/get-marketplace-plugin-details

get /gateways/plugins/marketplace/{id}
`org:gateways:read`




# Install Gateway Plugin
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/install-gateway-plugin

post /gateways/plugins/{gateway_id}
`org:gateways:write`




# List Gateway Plugins
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/list-gateway-plugins

get /gateways/plugins
`org:gateways:read`




# List Gateways
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/list-gateways

get /gateways
`org:gateways:read`




# List Installed Plugins for Gateway
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/list-installed-plugins-for-gateway

get /ipfs/gateway_plugins/{gateway_id}
`org:gateways:read`




# List Marketplace Plugins
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/list-marketplace-plugins

get /gateways/plugins/marketplace
`org:gateways:read`




# Revoke Gateway Key
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/revoke-gateway-key

delete /gateways/{id}/access_tokens/{access_token_id}
`org:gateways:write`




# Revoke Host Origin Restriction
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/revoke-host-origin-restriction

delete /gateways/{id}/hosts/{host_id}
`org:gateways:write`




# Revoke IP Address Restricton
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/revoke-ip-address-restricton

delete /gateways/{id}/ips/{ip_id}
`org:gateways:write:




# Time Interval Gateway Analytics
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/time-interval-gateway-analytics

get /analytics/gateways/time_series
`org:analytics:read`




# Top Gateway Analytics
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/top-gateway-analytics

get /analytics/gateways/top
`org:analytics:read`




# Uninstall Gateway Plugin
Source: https://docs.pinata.cloud/api-reference/endpoint/ipfs/uninstall-gateway-plugin

delete /gateways/plugins/{gateway_id}/plugin/{plugin_id}
`org:gateways:write`




# List Files
Source: https://docs.pinata.cloud/api-reference/endpoint/list-files

get /files/{network}
`org:files:read`




# List Groups
Source: https://docs.pinata.cloud/api-reference/endpoint/list-groups

get /groups/{network}
`org:groups:read`




# Pin by CID
Source: https://docs.pinata.cloud/api-reference/endpoint/pin-by-cid

post /files/public/pin_by_cid
`org:files:write`




# Query File Vectors
Source: https://docs.pinata.cloud/api-reference/endpoint/query-file-vectors

post /vectorize/groups/{group_id}/query
`org:write`




# Query Pin Requests
Source: https://docs.pinata.cloud/api-reference/endpoint/query-pin-requests

get /files/public/pin_by_cid
`org:files:read`




# Remove File From Group
Source: https://docs.pinata.cloud/api-reference/endpoint/remove-file-from-group

delete /groups/{network}/{id}/ids/{file_id}
`org:groups:write`




# Remove Signature from CID
Source: https://docs.pinata.cloud/api-reference/endpoint/remove-signature-from-cid

delete /files/{network}/signature/{cid}
`org:files:write`




# Remove Swap
Source: https://docs.pinata.cloud/api-reference/endpoint/remove-swap

delete /files/{network}/swap/{cid}
`org:files:write`




# Update File
Source: https://docs.pinata.cloud/api-reference/endpoint/update-file

put /files/{network}/{id}
`org:files:write`




# Update Group
Source: https://docs.pinata.cloud/api-reference/endpoint/update-group

put /groups/{network}/{id}
`org:groups:write`




# Upload a File
Source: https://docs.pinata.cloud/api-reference/endpoint/upload-a-file

post /files
`org:files:write`


<Note>
  The V3 Upload endpoint currently does not support folder uploads. Please use the legacy [pinFileToIPFS endpoint](/api-reference/endpoint/ipfs/pin-file-to-ipfs)
</Note>


# Create API Key
Source: https://docs.pinata.cloud/api-reference/endpoint/v3-create-api-key

post /api_keys
`org:write`




# List API Keys
Source: https://docs.pinata.cloud/api-reference/endpoint/v3-list-api-keys

get /api_keys
`org:write`




# Revoke API Key
Source: https://docs.pinata.cloud/api-reference/endpoint/v3-revoke-api-key

delete /api_keys/{key}
`org:write`




# Vectorize a File
Source: https://docs.pinata.cloud/api-reference/endpoint/vectorize-file

post /vectorize/files/{file_id}
`org:write`




# Add CID to Payment Instruction
Source: https://docs.pinata.cloud/api-reference/endpoint/x402/cids-add

put /x402/payment_instructions/{id}/cids/{cid}
Associates a CID with a payment instruction



# List CIDs for Payment Instruction
Source: https://docs.pinata.cloud/api-reference/endpoint/x402/cids-list

get /x402/payment_instructions/{id}/cids
Returns a paginated list of CIDs associated with a payment instruction



# Remove CID from Payment Instruction
Source: https://docs.pinata.cloud/api-reference/endpoint/x402/cids-remove

delete /x402/payment_instructions/{id}/cids/{cid}
Removes a CID association from a payment instruction



# Create Payment Instruction
Source: https://docs.pinata.cloud/api-reference/endpoint/x402/payment-instructions-create

post /x402/payment_instructions
Creates a new payment instruction



# Delete Payment Instruction
Source: https://docs.pinata.cloud/api-reference/endpoint/x402/payment-instructions-delete

delete /x402/payment_instructions/{id}
Deletes a payment instruction (soft delete). All CID mappings must be deleted first.



# Get Payment Instruction
Source: https://docs.pinata.cloud/api-reference/endpoint/x402/payment-instructions-get

get /x402/payment_instructions/{id}
Retrieves a specific payment instruction by ID



# List Payment Instructions
Source: https://docs.pinata.cloud/api-reference/endpoint/x402/payment-instructions-list

get /x402/payment_instructions
Returns a paginated list of payment instructions



# Update Payment Instruction
Source: https://docs.pinata.cloud/api-reference/endpoint/x402/payment-instructions-update

patch /x402/payment_instructions/{id}
Updates an existing payment instruction



# Upload a File
Source: https://docs.pinata.cloud/api-reference/endpoint/x402/pin

pinata-x402-api-v1.yaml post /pin/{network}
Uploads a file to Pinata's public IPFS network

## Cost

| Price           | Duration           |
| --------------- | ------------------ |
| \$0.10/GB \* 12 | Pins for 12 months |

## Example Usage

In order to access these endpoints you will need to use either [`@x402/axios`](https://www.npmjs.com/package/@x402/axios) or [`@x402/fetch`](https://www.npmjs.com/package/@x402/fetch). Once installed you will also need either [Viem](https://viem.sh) or a Coinbase developer account. From there you can create an `account` locally or through the CDP Wallet API.

When you make a request to one of the Pinata x402 endpoints it will return a 402 error saying payment is required. Then the `fetchWithPayment` method from the fetch or axios library will make a second requst for the requested payment amount. After payment is settled then you can use the returned presigned URL to upload the file to Pinata.

```typescript theme={null}
import { wrapFetchWithPayment, decodeXPaymentResponse } from "@x402/fetch";
import { account } from "./viem";

const fetchWithPayment = wrapFetchWithPayment(fetch, account);

const url = "https://402.pinata.cloud/v1/pin/public";

fetchWithPayment(url, {
  method: "POST",
  body: JSON.stringify({
    fileSize: 5000000,
  }),
})
  .then(async (response) => {
    const body = (await response.json()) as { url: string };
    console.log(body);

    const uuid = crypto.randomUUID();

    const file = new File([`Paid and pinned by 402.pinata.cloud: ${uuid}`], "file.txt");

    const data = new FormData();
    data.append("network", "public");
    data.append("file", file);

    const uploadReq = await fetch(body.url, {
      method: "POST",
      body: data,
    });

    const uploadRes = await uploadReq.json();
    console.log(uploadRes);
  })
  .catch((error) => {
    console.error(error.response?.data?.error);
  });
```

Uploading files to Public IPFS means you can access them through a gateway like `https://ipfs.io/ipfs/:CID`. If you upload a file as `private` then it will not be accessible on public IPFS, so in order to access it you need to create a temporary access URL. This flow is similar to the previous one, except you would provide the CID that you uploded previously that you would like to access. After a successful payment the server will return a URL you can access the file with.

```typescript theme={null}
import { wrapFetchWithPayment, decodeXPaymentResponse } from "@x402/fetch";
import { account } from "./viem";

const fetchWithPayment = wrapFetchWithPayment(fetch, account);

const url =
  "https://402.pinata.cloud/v1/retrieve/private/bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4";

fetchWithPayment(url, {
  method: "GET",
})
  .then(async (response) => {
    const body = (await response.json()) as { url: string };
    console.log(body);
  })
  .catch((error) => {
    console.error(error.response?.data?.error);
  });
```


# Retrieve a Private File
Source: https://docs.pinata.cloud/api-reference/endpoint/x402/retrieve

pinata-x402-api-v1.yaml get /retrieve/private/{cid}
Retrieves a private file from IPFS by its CID

## Cost

| Price    | Duration    |
| -------- | ----------- |
| \$0.0001 | Per request |

## Example Usage

If you upload a file as `private` then it will not be accessible on public IPFS, so in order to access it you need to create a temporary access URL. This flow is similar to the previous one, except you would provide the CID that you uploded previously that you would like to access. After a successful payment the server will return a URL you can access the file with.

```typescript theme={null}
import { wrapFetchWithPayment, decodeXPaymentResponse } from "@x402/fetch";
import { account } from "./viem";

const fetchWithPayment = wrapFetchWithPayment(fetch, account);

const url =
	"https://402.pinata.cloud/v1/retrieve/private/bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4";

fetchWithPayment(url, {
	method: "GET",
})
	.then(async (response) => {

		const body = (await response.json()) as { url: string };
		console.log(body);

	})
	.catch((error) => {
		console.error(error.response?.data?.error);
	});
```


# Introduction
Source: https://docs.pinata.cloud/api-reference/introduction

Getting started with the Pinata API

Welcome to the Pinata API Reference! Before you can do anything in the API, you'll need some API Keys.

## API Keys

Visit the [Pinata API Keys](https://app.pinata.cloud/developers/api-keys) page to generate new keys.

<img />

In the 'New Key' modal, you can choose if you want the key to be an Admin key and have full access over every endpoint, or scope the keys by selecting which endpoints you want to use. You can also give it a limited number of uses, so be sure to give it a name to keep track of it. Once you have that filled out, click "Generate API Key" and it will show you the `pinata_api_key`, `pinata_api_secret_key`, and the `JWT`. It's best to click "Copy All" and keep the API key data safe and secure.

<Warning>
  Once API keys have been created, you will not be able to see the secret or JWT
  again
</Warning>

Once you have created your keys you can go ahead and try testing them! Try to paste this into your terminal with your `JWT`

```bash theme={null}
curl --request GET \
     --url https://api.pinata.cloud/data/testAuthentication \
     --header 'accept: application/json' \
     --header 'authorization: Bearer YOUR_PINATA_JWT'
```

If successful you should see this!

```shell bash theme={null}
{
  "message": "Congratulations! You are communicating with the Pinata API!"
}
```


# bandwidth
Source: https://docs.pinata.cloud/sdk/analytics/bandwidth

`org:analytics:read`

Get analytics on bandwidth for multiple properties

## Usage

The `analytics` class is unique in that it very flexible, but also can require more queries to be used well. Be sure to real the [Parameters](#parameters) in detail to understand how it can be used.

The `bandwidth` method will sort results by highest number of bandwidth, but will also include `requests` values.

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const clicks = await pinata.analytics.bandwidth
  .days(30)
  .limit(10)
  .cid("<CID>")
```

## Returns

What is returned in `value` will depend on they property or query used. For instance, using `cid()` will return CIDs, `country()` will return Countries, etc.

```typescript theme={null}
type TopAnalyticsResponse = {
	data: TopAnalyticsItem[];
};

type TopAnalyticsItem = {
	value: string;
	requests: number;
	bandwidth: number;
};
```

## Parameters

Filter response with the following additional methods. It does require at least one property, such as `cid`, `fileName`, `userAgent`, `country`, `region`, or `referrer`.

### cid

* Type: `string`

Returns bandwidth for all CIDs

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .cid()
```

Filter by passing an argument

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .cid("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
```

### fileName

* Type: `string`

Returns bandwidth for all file names

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .fileName()
```

Filter by passing an argument

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .fileName("pinnie.png")
```

### userAgent

* Type: `string`

Returns bandwidth for user agents

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .userAgent()
```

Filter by passing an argument

```typescript {3-5} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .userAgent(
    "Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0"
  )
```

### country

* Type: `string`

Returns bandwidth for countries

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .country()
```

Filter by passing an argument

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .country("us")
```

### region

* Type: `string`

Returns bandwidth for regions inside of countries

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .region()
```

Filter by passing an argument

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .region("us - VA")
```

### referer

* Type: `string`

Returns bandwidth for referers

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .referer()
```

Filter by passing an argument

```typescript {3} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .referer("https://docs.pinata.cloud/")
```

### days

* Type: `number`

Number of days to query. Starts with current date and then goes back by provided number.

```typescript {2} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .cid()
```

### sort

* Type: `"asc" | "desc"`

Order results either ascending or descending by created date

```typescript {4} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .cid()
  .sort("asc")
```

### limit

* Type: `number`

Limit the number of results

```typescript {4} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .cid()
  .limit(10)
```

### customDates

* Type: `string, string`

Custom dates to query using a start and end date with the format `YYYY-MM-DD`

```typescript {2} theme={null}
const files = await pinata.analytics.bandwidth
  .customDates("2024-11-01", "2024-11-20")
  .cid()
```

### from

* Type: `string`

Provide an alternate Gateway domain to query instead of the default one found in the Pinata SDK Config

```typescript {4} theme={null}
const files = await pinata.analytics.bandwidth
  .days(7)
  .cid()
  .from("example-2.mypinata.cloud")
```


# requests
Source: https://docs.pinata.cloud/sdk/analytics/requests

`org:analytics:read`

Get analytics on requests for multiple properties

## Usage

The `analytics` class is unique in that it very flexible, but also can require more queries to be used well. Be sure to real the [Parameters](#parameters) in detail to understand how it can be used.

The `requests` method will sort results by highest number of requests, but will also include `bandwidth` values.

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const clicks = await pinata.analytics.requests
  .days(30)
  .limit(10)
  .cid("<CID>")
```

## Returns

What is returned in `value` will depend on they property or query used. For instance, using `cid()` will return CIDs, `country()` will return Countries, etc.

```typescript theme={null}
type TopAnalyticsResponse = {
	data: TopAnalyticsItem[];
};

type TopAnalyticsItem = {
	value: string;
	requests: number;
	bandwidth: number;
};
```

## Parameters

Filter response with the following additional methods. It does require at least one property, such as `cid`, `fileName`, `userAgent`, `country`, `region`, or `referrer`.

### cid

* Type: `string`

Returns requests for all CIDs

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .cid()
```

Filter by passing an argument

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .cid("bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4")
```

### fileName

* Type: `string`

Returns requests for all file names

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .fileName()
```

Filter by passing an argument

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .fileName("pinnie.png")
```

### userAgent

* Type: `string`

Returns requests for user agents

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .userAgent()
```

Filter by passing an argument

```typescript {3-5} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .userAgent(
    "Mozilla/5.0 (X11; Linux x86_64; rv:132.0) Gecko/20100101 Firefox/132.0"
  )
```

### country

* Type: `string`

Returns requests for countries

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .country()
```

Filter by passing an argument

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .country("us")
```

### region

* Type: `string`

Returns requests for regions inside of countries

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .region()
```

Filter by passing an argument

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .region("us - VA")
```

### referer

* Type: `string`

Returns requests for referers

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .referer()
```

Filter by passing an argument

```typescript {3} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .referer("https://docs.pinata.cloud/")
```

### days

* Type: `number`

Number of days to query. Starts with current date and then goes back by provided number.

```typescript {2} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .cid()
```

### sort

* Type: `"asc" | "desc"`

Order results either ascending or descending by created date

```typescript {4} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .cid()
  .sort("asc")
```

### limit

* Type: `number`

Limit the number of results

```typescript {4} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .cid()
  .limit(10)
```

### customDates

* Type: `string, string`

Custom dates to query using a start and end date with the format `YYYY-MM-DD`

```typescript {2} theme={null}
const files = await pinata.analytics.requests
  .customDates("2024-11-01", "2024-11-20")
  .cid()
```

### from

* Type: `string`

Provide an alternate Gateway domain to query instead of the default one found in the Pinata SDK Config

```typescript {4} theme={null}
const files = await pinata.analytics.requests
  .days(7)
  .cid()
  .from("example-2.mypinata.cloud")
```


# create
Source: https://docs.pinata.cloud/sdk/keys/create

`org:write`

Create an API key

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const key = await pinata.keys.create({
  keyName: "user 1",
  permissions: {
    resources:  [
      "org:files:read",
      "org:groups:read"
    ]
  },
  maxUses: 1,
});
```

## Returns

```typescript theme={null}
type KeyResponse = {
  JWT: string;
  pinata_api_key: string;
  pinata_api_secret: string;
};
```

## Parameters

### keyName

* Type: `string`

Name for the API key

```typescript {2} theme={null}
const key = await pinata.keys.create({
  keyName: "user 1",
  permissions: {
    admin: true,
  },
  maxUses: 1,
});
```

### maxUses (Optional)

* Type: `number`

Limit the number of uses a key is valid for

```typescript {6} theme={null}
const key = await pinata.keys.create({
  keyName: "user 1",
  permissions: {
    admin: true,
  },
  maxUses: 1,
});
```

### permissions

* Type: [KeyPermissions](../types#keypermissions)

#### admin (Optional)

* Type: `boolean`

Grants the key admin access to all endpoints

```typescript {4} theme={null}
const key = await pinata.keys.create({
  keyName: "user 1",
  permissions: {
    admin: true,
  }
});
```

#### resources (Optional)

* Type: `ResourcePermission[]`

```typescript theme={null}
export type ResourcePermission =
	| "org:read"
	| "org:write"
	| "org:files:read"
	| "org:files:write"
	| "org:groups:read"
	| "org:groups:write"
	| "org:gateways:read"
	| "org:gateways:write"
	| "org:analytics:read"
	| "org:analytics:write";
```

Scope the API key by ResourcePermission

```typescript {4-7} theme={null}
const key = await pinata.keys.create({
  keyName: "user 1",
  permissions: {
    resources: [
      "org:files:read",
      "org:groups:read",
    ]
  }
});
```

#### endpoints (Optional)

* Type [Endpoints](../types#endpoints)

```typescript {3-20} theme={null}
const key = await pinata.keys.create({
  keyName: "user 1",
  permissions: {
    endpoints: {
      data: {
        pinList: true,
        userPinnedDataTotal: false
      },
      pinning: {
        hashMetadata: true,
        hashPinPolicy: false,
        pinByHash: true,
        pinFileToIPFS: true,
        pinJSONToIPFS: true,
        pinJobs: false,
        unpin: false,
        userPinPolicy: false
      }
    }
  }
});
```


# list
Source: https://docs.pinata.cloud/sdk/keys/list

`org:write`

List and filter through Keys

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const keys = await pinata.keys
  .list()
  .name("Admin")
  .revoked(false)
```

## Returns

```typescript theme={null}
type KeyListItem = {
  id: string;
  name: string;
  key: string;
  secret: string;
  max_uses: number;
  uses: number;
  user_id: string;
  scopes: KeyScopes;
  revoked: boolean;
  createdAt: string;
  updatedAt: string;
};
```

## Parameters

Filter response with the following additional methods. All filters are optional.

### name

* Type: `string`

Filter by name, uses "contains" matching

```typescript theme={null}
const keys = await pinata.keys
  .list()
  .name("Greetings");
```

### revoked

* Type: `boolean`

Filter keys by whether or not they have been revoked

```typescript theme={null}
const keys = await pinata.keys
  .list()
  .revoked(false);
```

### exhausted

* Type: `boolean`

Filter keys based on whether they had limited uses that were exhuasted

```typescript theme={null}
const keys = await pinata.keys
  .list()
  .exhausted(false);
```

### offset

* Type: `number`

Offset the number of keys returned to paginate

```typescript theme={null}
const keys = await pinata.keys
  .list()
  .offset(5);
```

## Auto Paginate

The `list` method has an auto pagination feature that is triggered when used inside a `for await` iterator

```typescript theme={null}
for await (const item of pinata.keys.list()) {
  console.log(item.name);
}
```


# revoke
Source: https://docs.pinata.cloud/sdk/keys/revoke

`org:write`

Revoke an API Key

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const revoke = await pinata.keys.revoke([
 "94566af5e63833e260be"
]);
```

## Returns

```typescript theme={null}
type RevokeKeyResponse[] = {
  key: string;
  status: string;
};
```

## Parameters

### keys

* Type: `string[]`

An array of API Keys to revoke. This is the `key` found in the response of `keys.list`

```typescript theme={null}
const revoke = await pinata.keys.revoke([
 "94566af5e63833e260be"
]);
```


# add
Source: https://docs.pinata.cloud/sdk/signatures/private/add

`org:files:write`

Add an EIP-712 signature to a CID

<Note>
  For more information about adding signatures to CIDs on IPFS please read the [Signatures Guide](/files/signatures).
</Note>

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signature = await pinata.signatures.private.add({
  cid: "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU",
  signature: "0x1b...911b",
  address: "0xB3899AA8E13172E48D44CE411b0c4c2f08730Dc6"
});
```

## Returns

```typescript theme={null}
type SignatureResponse = {
  cid: string;
  signature: string;
};
```

## Parameters

### cid

* Type: `string`

Target CID that you want to add a signature to.

```typescript {2} theme={null}
const signature = await pinata.signatures.private.add({
  cid: "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU",
  signature: "0x1b...911b",
  address: "0xB3899AA8E13172E48D44CE411b0c4c2f08730Dc6"
});
```

### signature

* Type: `0x${string}`

EIP-712 Signature to be assigned to target CID.

```typescript {3} theme={null}
const signature = await pinata.signatures.private.add({
  cid: "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU",
  signature: "0x1b...911b",
  address: "0xB3899AA8E13172E48D44CE411b0c4c2f08730Dc6"
});
```

### address

* Type: `0x${string}`

Wallet address that made the signature

```typescript {4} theme={null}
const signature = await pinata.signatures.private.add({
  cid: "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU",
  signature: "0x1b...911b",
  address: "0xB3899AA8E13172E48D44CE411b0c4c2f08730Dc6"
});
```


# delete
Source: https://docs.pinata.cloud/sdk/signatures/private/delete

`org:files:write`

Delete an EIP-712 signature from a CID

<Note>
  For more information about adding signatures to CIDs on IPFS please read the [Signatures Guide](/files/signatures).
</Note>

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signature = await pinata.signatures.delete(
  "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU"
);
```

## Returns

```typescript theme={null}
OK
```

## Parameters

### cid

* Type: `string`

Target CID that you want to add a signature to.

```typescript theme={null}
const signature = await pinata.signatures.delete(
  "QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU"
);
```


# get
Source: https://docs.pinata.cloud/sdk/signatures/private/get

`org:files:read`

Get signature for CID

<Note>
  For more information about adding signatures to CIDs on IPFS please read the [Signatures Guide](/files/signatures).
</Note>

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata-web3";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const signature = await pinata.signatures.get("QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU");
```

## Returns

```typescript theme={null}
type SignatureResponse = {
  cid: string;
  signature: string;
};
```

## Parameters

### cid

* Type: `string`

Target CID that you want to add a signature to.

```typescript theme={null}
const signature = await pinata.signatures.get("QmXGeVy9dVwfuFJmvbzz8y4dYK1TdxXbDGzwbNuyZ5xXSU");
```


# Analytics
Source: https://docs.pinata.cloud/sdk/types/analytics



### AnalyticsQuery

```typescript theme={null}
export type AnalyticsQuery = {
	gateway_domain: string;
	start_date: string;
	end_date: string;
	cid?: string;
	file_name?: string;
	user_agent?: string;
	country?: string;
	region?: string;
	referer?: string;
	limit?: number;
	sort_order?: "asc" | "desc";
};
```

### TopAnalyticsQuery

```typescript theme={null}
export type TopAnalyticsQuery = AnalyticsQuery & {
	sort_by: "requests" | "bandwidth";
	attribute:
		| "cid"
		| "country"
		| "region"
		| "user_agent"
		| "referer"
		| "file_name";
};
```

### TopAnalyticsResponse

```typescript theme={null}
export type TopAnalyticsResponse = {
	data: TopAnalyticsItem[];
};
```

### TopAnalyticsItem

```typescript theme={null}
export type TopAnalyticsItem = {
	value: string;
	requests: number;
	bandwidth: number;
};
```

### TimeIntervalAnalyticsQuery

```typescript theme={null}
export type TimeIntervalAnalyticsQuery = AnalyticsQuery & {
	sort_by?: "requests" | "bandwidth";
	date_interval: "day" | "week";
};
```

### TimePeriodItem

```typescript theme={null}
export type TimePeriodItem = {
	period_start_time: string;
	requests: number;
	bandwidth: number;
};
```

### TimeIntervalAnalyticsResponse

```typescript theme={null}
export type TimeIntervalAnalyticsResponse = {
	total_requests: number;
	total_bandwidth: number;
	time_periods: TimePeriodItem[];
};
```

### UserPinnedDataResponse

```typescript theme={null}
export type UserPinnedDataResponse = {
	pin_count: number;
	pin_size_total: number;
	pin_size_with_replications_total: number;
};
```


# Config
Source: https://docs.pinata.cloud/sdk/types/config



### PinataConfig

```typescript theme={null}
export type PinataConfig = {
	pinataJwt?: string;
	pinataGateway?: string;
	pinataGatewayKey?: string;
	customHeaders?: Record<string, string>;
	endpointUrl?: string;
	uploadUrl?: string;
};
```


# Files
Source: https://docs.pinata.cloud/sdk/types/files



### FileObject

```typescript theme={null}
export type FileObject = {
	name: string;
	size: number;
	type: string;
	lastModified: number;
	arrayBuffer: () => Promise<ArrayBuffer>;
};
```

### JsonBody

```typescript theme={null}
export type JsonBody = Record<string, unknown>;
```

### PinataMetadata

```typescript theme={null}
export type PinataMetadata = {
	name?: string;
	keyvalues?: Record<string, string>;
};
```

### UpdateFileOptions

```typescript theme={null}
export type UpdateFileOptions = {
	id: string;
	name?: string;
	keyvalues?: Record<string, string>;
};
```

### DeleteResponse

```typescript theme={null}
export type DeleteResponse = {
	id: string;
	status: string;
};
```

### FileListItem

```typescript theme={null}
export type FileListItem = {
	id: string;
	name: string | null;
	cid: "pending" | string;
	size: number;
	number_of_files: number;
	mime_type: string;
	keyvalues: Record<string, string>;
	group_id: string | null;
	created_at: string;
};
```

### FileListResponse

```typescript theme={null}
export type FileListResponse = {
	files: FileListItem[];
	next_page_token: string;
};
```

### FileListQuery

```typescript theme={null}
export type FileListQuery = {
	name?: string;
	group?: string;
	noGroup?: boolean;
	mimeType?: string;
	cid?: string;
	cidPending?: boolean;
	metadata?: Record<string, string>;
	order?: "ASC" | "DESC";
	limit?: number;
	pageToken?: string;
};
```

### PinQueueQuery

```typescript theme={null}
export type PinQueueQuery = {
	sort?: "ASC" | "DSC";
	status?:
		| "prechecking"
		| "retrieving"
		| "expired"
		| "backfilled
		| "over_free_limit"
		| "over_max_size"
		| "invalid_object"
		| "bad_host_node";
	ipfs_pin_hash?: string;
	limit?: number;
	pageToken?: string;
};
```

### PinQueueItem

```typescript theme={null}
export type PinQueueItem = {
	id: string;
	cid?: string;
	ipfs_pin_hash?: string;
	date_queued: string;
	name: string;
	status: string;
	keyvalues: any;
	host_nodes: string[];
	pin_policy: {
		regions: {
			id: string;
			desiredReplicationCount: number;
		}[];
		version: number;
	};
};
```

### PinQueueResponse

```typescript theme={null}
export type PinQueueResponse = {
	rows: PinQueueItem[];
	next_page_token: string;
};
```

### SwapCidOptions

```typescript theme={null}
export type SwapCidOptions = {
	cid: string;
	swapCid: string;
};
```

### SwapHistoryOptions

```typescript theme={null}
export type SwapHistoryOptions = {
	cid: string;
	domain: string;
};
```

### SwapCidResponse

```typescript theme={null}
export type SwapCidResponse = {
	mapped_cid: string;
	created_at: string;
};
```

### VectorizeFileResponse

```typescript theme={null}
export type VectorizeFileResponse = {
	status: boolean;
};
```

### VectorizeQuery

```typescript theme={null}
export type VectorizeQuery = {
	groupId: string;
	query: string;
	returnFile?: boolean;
};
```

### VectorQueryMatch

```typescript theme={null}
export type VectorQueryMatch = {
	file_id: string;
	cid: string;
	score: number;
};
```

### VectorizeQueryResponse

```typescript theme={null}
export type VectorizeQueryResponse = {
	count: number;
	matches: VectorQueryMatch[];
};
```

***


# Gateways
Source: https://docs.pinata.cloud/sdk/types/gateways



### ContentType

```typescript theme={null}
export type ContentType =
	| "application/json"
	| "application/xml"
	| "text/plain"
	| "text/html"
	| "text/css"
	| "text/javascript"
	| "application/javascript"
	| "image/jpeg"
	| "image/png"
	| "image/gif"
	| "image/svg+xml"
	| "audio/mpeg"
	| "audio/ogg"
	| "video/mp4"
	| "application/pdf"
	| "application/octet-stream"
	| string
	| null; // Allow for other MIME types
```

### GetCIDResponse

```typescript theme={null}
export type GetCIDResponse = {
	data?: JSON | string | Blob | null;
	contentType: ContentType;
};
```

### OptimizeImageOptions

```typescript theme={null}
export type OptimizeImageOptions = {
	width?: number;
	height?: number;
	dpr?: number;
	fit?: "scaleDown" | "contain" | "cover" | "crop" | "pad";
	gravity?: "auto" | "side" | string;
	quality?: number;
	format?: "auto" | "webp";
	animation?: boolean;
	sharpen?: number;
	onError?: boolean;
	metadata?: "keep" | "copyright" | "none";
};
```

### AccessLinkOptions

```typescript theme={null}
export type AccessLinkOptions = {
	cid: string;
	date?: number;
	expires: number;
	gateway?: string;
};
```

### ContainsCIDResponse

```typescript theme={null}
export type ContainsCIDResponse = {
	containsCid: boolean;
	cid: string | null;
};
```


# Groups
Source: https://docs.pinata.cloud/sdk/types/groups



### GroupOptions

```typescript theme={null}
export type GroupOptions = {
	name: string;
	isPublic?: boolean;
};
```

### UpdateGroupOptions

```typescript theme={null}
export type UpdateGroupOptions = {
	groupId: string;
	name?: string;
	isPublic?: boolean;
};
```

### GetGroupOptions

```typescript theme={null}
export type GetGroupOptions = {
	groupId: string;
};
```

### GroupListResponse

```typescript theme={null}
export type GroupListResponse = {
	groups: GroupResponseItem[];
	next_page_token: string;
};
```

### GroupResponseItem

```typescript theme={null}
export type GroupResponseItem = {
	id: string;
	is_public: boolean;
	name: string;
	createdAt: string;
};
```

### GroupQueryOptions

```typescript theme={null}
export type GroupQueryOptions = {
	name?: string;
	limit?: number;
	pageToken?: string;
	isPublic?: boolean;
};
```

### GroupCIDOptions

```typescript theme={null}
export type GroupCIDOptions = {
	groupId: string;
	files: string[];
};
```

### UpdateGroupFilesResponse

```typescript theme={null}
export type UpdateGroupFilesResponse = {
	id: string;
	status: string;
};
```


# Keys
Source: https://docs.pinata.cloud/sdk/types/keys



### KeyPermissions

```typescript theme={null}
export type KeyPermissions = {
	admin?: boolean;
	endpoints?: Endpoints;
};
```

### Endpoints

```typescript theme={null}
export type Endpoints = {
	data?: DataEndponts;
	pinning?: PinningEndpoints;
};
```

### DataEndponts

```typescript theme={null}
export type DataEndponts = {
	pinList?: boolean;
	userPinnedDataTotal?: boolean;
};
```

### PinningEndpoints

```typescript theme={null}
export type PinningEndpoints = {
	hashMetadata?: boolean;
	hashPinPolicy?: boolean;
	pinByHash?: boolean;
	pinFileToIPFS?: boolean;
	pinJSONToIPFS?: boolean;
	pinJobs?: boolean;
	unpin?: boolean;
	userPinPolicy?: boolean;
};
```

### KeyOptions

```typescript theme={null}
export type KeyOptions = {
	keyName: string;
	permissions: KeyPermissions;
	maxUses?: number;
};
```

### KeyResponse

```typescript theme={null}
export type KeyResponse = {
	JWT: string;
	pinata_api_key: string;
	pinata_api_secret: string;
};
```

### KeyListQuery

```typescript theme={null}
export type KeyListQuery = {
	revoked?: boolean;
	limitedUse?: boolean;
	exhausted?: boolean;
	name?: string;
	offset?: number;
};
```

### KeyListItem

```typescript theme={null}
export type KeyListItem = {
	id: string;
	name: string;
	key: string;
	secret: string;
	max_uses: number;
	uses: number;
	user_id: string;
	scopes: KeyScopes;
	revoked: boolean;
	createdAt: string;
	updatedAt: string;
};
```

### KeyScopes

```typescript theme={null}
type KeyScopes = {
	endpoints: {
		pinning: {
			pinFileToIPFS: boolean;
			pinJSONToIPFS: boolean;
		};
	};
	admin: boolean;
};
```

### KeyListResponse

```typescript theme={null}
export type KeyListResponse = {
	keys: KeyListItem[];
	count: number;
};
```

### RevokeKeyResponse

```typescript theme={null}
export type RevokeKeyResponse = {
	key: string;
	status: string;
};
```


# Signatures
Source: https://docs.pinata.cloud/sdk/types/signatures



### SignatureOptions

```typescript theme={null}
export type SignatureOptions = {
	cid: string;
	signature: string;
	address: string;
};
```

### SignatureResponse

```typescript theme={null}
export type SignatureResponse = {
	cid: string;
	signature: string;
};
```


# Uploads
Source: https://docs.pinata.cloud/sdk/types/uploads



### UploadResponse

```typescript theme={null}
export type UploadResponse = {
	id: string;
	name: string;
	cid: string;
	size: number;
	created_at: string;
	number_of_files: number;
	mime_type: string;
	user_id: string;
	keyvalues: {
		[key: string]: string;
	};
	vectorized: boolean;
	network: string;
};
```

### UploadOptions

```typescript theme={null}
export type UploadOptions = {
	metadata?: PinataMetadata;
	//pinType?: "async" | "sync" | "cidOnly";
	keys?: string;
	groupId?: string;
	vectorize?: boolean;
	url?: string;
};
```

### SignedUploadUrlOptions

```typescript theme={null}
export type SignedUploadUrlOptions = {
	date?: number;
	expires: number;
	groupId?: string;
	name?: string;
	keyvalues?: Record<string, string>;
	vectorize?: boolean;
};
```

### UploadCIDOptions

```typescript theme={null}
export type UploadCIDOptions = {
	metadata?: PinataMetadata;
	peerAddresses?: string[];
	keys?: string;
	groupId?: string;
};
```

### PinByCIDResponse

```typescript theme={null}
export type PinByCIDResponse = {
	id: string;
	cid: string;
	status: "prechecking" | "retrieving";
	name: string;
};
```


# x402
Source: https://docs.pinata.cloud/sdk/types/x402



Types for x402 monetization features

## PaymentRequirement

Defines a single payment requirement within a payment instruction.

```typescript theme={null}
type PaymentRequirement = {
  asset: string;
  pay_to: string;
  network: "base" | "base-sepolia" | "eip155:8453" | "eip155:84532";
  amount: string;
  description?: string;
};
```

| Property      | Type                                                                | Description                                                                                                   |
| ------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `asset`       | `string`                                                            | The USDC token contract address for the network (e.g., `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` for Base) |
| `pay_to`      | `string`                                                            | The wallet address to receive payments                                                                        |
| `network`     | `"base"` \| `"base-sepolia"` \| `"eip155:8453"` \| `"eip155:84532"` | The blockchain network for transactions. Accepts friendly names or EIP-155 chain IDs                          |
| `amount`      | `string`                                                            | The amount required in USDC smallest units (6 decimals). Example: `"10000"` = \$0.01                          |
| `description` | `string`                                                            | Optional description for this requirement                                                                     |

## PaymentInstruction

Represents a complete payment instruction with all its requirements.

```typescript theme={null}
type PaymentInstruction = {
  id: string;
  version: number;
  payment_requirements: PaymentRequirement[];
  name: string;
  description?: string;
  created_at: string;
};
```

| Property               | Type                   | Description                                   |
| ---------------------- | ---------------------- | --------------------------------------------- |
| `id`                   | `string`               | Unique identifier for the payment instruction |
| `version`              | `number`               | Version number of the instruction             |
| `payment_requirements` | `PaymentRequirement[]` | Array of payment requirements                 |
| `name`                 | `string`               | Name of the payment instruction               |
| `description`          | `string`               | Optional description                          |
| `created_at`           | `string`               | ISO timestamp of creation                     |

## CreatePaymentInstructionRequest

Request body for creating a new payment instruction.

```typescript theme={null}
type CreatePaymentInstructionRequest = {
  name: string;
  payment_requirements: PaymentRequirement[];
  description?: string;
};
```

## UpdatePaymentInstructionRequest

Request body for updating an existing payment instruction.

```typescript theme={null}
type UpdatePaymentInstructionRequest = {
  name?: string;
  payment_requirements?: PaymentRequirement[];
  description?: string;
};
```

## PaymentInstructionListQuery

Query parameters for listing payment instructions.

```typescript theme={null}
type PaymentInstructionListQuery = {
  limit?: number;
  pageToken?: string;
  cid?: string;
  name?: string;
  id?: string;
};
```

| Property    | Type     | Description                         |
| ----------- | -------- | ----------------------------------- |
| `limit`     | `number` | Maximum number of results to return |
| `pageToken` | `string` | Pagination token for next page      |
| `cid`       | `string` | Filter by associated CID            |
| `name`      | `string` | Filter by instruction name          |
| `id`        | `string` | Filter by instruction ID            |

## PaymentInstructionListResponse

Response structure for listing payment instructions.

```typescript theme={null}
type PaymentInstructionListResponse = {
  data: {
    payment_instructions: PaymentInstruction[];
    next_page_token?: string;
  };
};
```

## PaymentInstructionResponse

Response structure for single payment instruction operations.

```typescript theme={null}
type PaymentInstructionResponse = {
  data: PaymentInstruction;
};
```

## PaymentInstructionDeleteResponse

Response structure for delete operations.

```typescript theme={null}
type PaymentInstructionDeleteResponse = {
  data: {};
};
```

## CidListQuery

Query parameters for listing CIDs associated with a payment instruction.

```typescript theme={null}
type CidListQuery = {
  limit?: number;
  pageToken?: string;
};
```

## CidListResponse

Response structure for listing CIDs.

```typescript theme={null}
type CidListResponse = {
  data: {
    cids: string[];
    next_page_token?: string;
  };
};
```

## CidAssociation

Represents a CID associated with a payment instruction.

```typescript theme={null}
type CidAssociation = {
  payment_instruction_id: string;
  cid: string;
  created_at: string;
};
```

| Property                 | Type     | Description                                       |
| ------------------------ | -------- | ------------------------------------------------- |
| `payment_instruction_id` | `string` | ID of the associated payment instruction          |
| `cid`                    | `string` | The IPFS CID                                      |
| `created_at`             | `string` | ISO timestamp of when the association was created |

## CidAssociationResponse

Response structure for adding a CID to a payment instruction.

```typescript theme={null}
type CidAssociationResponse = {
  data: CidAssociation;
};
```

## CidRemoveResponse

Response structure for removing a CID from a payment instruction.

```typescript theme={null}
type CidRemoveResponse = {
  data: {};
};
```


# add
Source: https://docs.pinata.cloud/sdk/x402/cids/add



Associate a CID with a payment instruction for x402 monetization

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const association = await pinata.x402.addCid(
  "01234567-89ab-cdef-0123-456789abcdef",
  "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
);
```

## Returns

```typescript theme={null}
type CidAssociationResponse = {
  data: CidAssociation;
};

type CidAssociation = {
  payment_instruction_id: string;
  cid: string;
  created_at: string;
};
```

## Parameters

### paymentInstructionId (required)

* Type: `string`

The unique identifier of the payment instruction to associate the CID with

```typescript theme={null}
const association = await pinata.x402.addCid(
  "01234567-89ab-cdef-0123-456789abcdef",
  "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
);
```

### cid (required)

* Type: `string`

The IPFS CID to associate with the payment instruction. Once associated, accessing this content will require payment according to the payment instruction.

```typescript theme={null}
const association = await pinata.x402.addCid(
  "01234567-89ab-cdef-0123-456789abcdef",
  "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
);
```


# list
Source: https://docs.pinata.cloud/sdk/x402/cids/list



List all CIDs associated with a payment instruction

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const cids = await pinata.x402.listCids(
  "01234567-89ab-cdef-0123-456789abcdef"
);
```

## Returns

```typescript theme={null}
type CidListResponse = {
  data: {
    cids: string[];
    next_page_token?: string;
  };
};
```

## Parameters

### paymentInstructionId (required)

* Type: `string`

The unique identifier of the payment instruction

```typescript theme={null}
const cids = await pinata.x402.listCids(
  "01234567-89ab-cdef-0123-456789abcdef"
);
```

### options

Optional parameters for pagination.

#### limit

* Type: `number`

Limit the number of results returned

```typescript {3-5} theme={null}
const cids = await pinata.x402.listCids(
  "01234567-89ab-cdef-0123-456789abcdef",
  {
    limit: 10,
  }
);
```

#### pageToken

* Type: `string`

Paginate through results using a page token from a previous response

```typescript {3-5} theme={null}
const cids = await pinata.x402.listCids(
  "01234567-89ab-cdef-0123-456789abcdef",
  {
    pageToken: "MDE5MWIzZWYtM2U0Zi03YTY5LWE3OTQtOTRhZDE5NjQxMTk0",
  }
);
```


# remove
Source: https://docs.pinata.cloud/sdk/x402/cids/remove



Remove a CID association from a payment instruction

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const result = await pinata.x402.removeCid(
  "01234567-89ab-cdef-0123-456789abcdef",
  "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
);
```

## Returns

```typescript theme={null}
type CidRemoveResponse = {
  data: {};
};
```

## Parameters

### paymentInstructionId (required)

* Type: `string`

The unique identifier of the payment instruction

```typescript theme={null}
const result = await pinata.x402.removeCid(
  "01234567-89ab-cdef-0123-456789abcdef",
  "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
);
```

### cid (required)

* Type: `string`

The IPFS CID to remove from the payment instruction. Once removed, the content will no longer require payment for access through this instruction.

```typescript theme={null}
const result = await pinata.x402.removeCid(
  "01234567-89ab-cdef-0123-456789abcdef",
  "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4"
);
```


# x402 Monetization
Source: https://docs.pinata.cloud/sdk/x402/index



<Note>
  x402 is available on paid Pinata accounts. [Upgrade your account](https://app.pinata.cloud/billing) to access x402 monetization features.
</Note>

Monetize your private IPFS files by receiving USDC payments directly to your wallet using the x402 protocol.

For detailed concepts and workflows, see the [x402 Introduction](/files/x402/intro).

## Quick Example

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "your-gateway.mypinata.cloud",
});

// 1. Upload a private file
const file = new File(["premium content"], "content.pdf", { type: "application/pdf" });
const upload = await pinata.upload.private.file(file);

// 2. Create a payment instruction
const instruction = await pinata.x402.createPaymentInstruction({
  name: "Premium Content Access",
  payment_requirements: [
    {
      asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", // USDC on Base
      pay_to: "0xYourWalletAddress", // YOU receive payments here
      network: "base",
      amount: "10000", // $0.01 in USDC
    },
  ],
});

// 3. Attach CID to payment instruction
await pinata.x402.addCid(instruction.data.id, upload.cid);

// 4. Share the x402 gateway URL
// https://your-gateway.mypinata.cloud/x402/cid/{cid}
```

## Network Configuration

**USDC is currently the only supported token.**

| Network                | USDC Token Address                           | Use Case                |
| ---------------------- | -------------------------------------------- | ----------------------- |
| Base (Mainnet)         | `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913` | Production monetization |
| Base Sepolia (Testnet) | `0x036CbD53842c5426634e7929541eC2318f3dCF7e` | Testing payment flows   |

## Payment Amounts

USDC has 6 decimals. To convert USD to token amount, multiply by 1,000,000:

| USD    | `amount`    |
| ------ | ----------- |
| \$0.01 | `"10000"`   |
| \$0.10 | `"100000"`  |
| \$1.00 | `"1000000"` |

## Available Methods

### Payment Instructions

* [list](/sdk/x402/payment-instructions/list) - List all payment instructions
* [create](/sdk/x402/payment-instructions/create) - Create a new payment instruction
* [get](/sdk/x402/payment-instructions/get) - Get a payment instruction by ID
* [update](/sdk/x402/payment-instructions/update) - Update a payment instruction
* [delete](/sdk/x402/payment-instructions/delete) - Delete a payment instruction

### CID Management

* [list](/sdk/x402/cids/list) - List CIDs attached to a payment instruction
* [add](/sdk/x402/cids/add) - Attach a CID to a payment instruction
* [remove](/sdk/x402/cids/remove) - Remove a CID from a payment instruction

## Related Resources

* [x402 Introduction](/files/x402/intro) - Overview of x402 monetization
* [Quick Start Guide](/files/x402/x402-quick-start) - Step-by-step setup guide
* [Payment Instructions Guide](/files/x402/x402-payment-instructions) - Detailed workflow guide
* [Accessing Paid Content](/files/x402/x402-accessing-paid-content) - How requesters access paid content
* [x402 Types](/sdk/types/x402) - TypeScript type definitions


# create
Source: https://docs.pinata.cloud/sdk/x402/payment-instructions/create



Create a new payment instruction for x402 monetization

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const instruction = await pinata.x402.createPaymentInstruction({
  name: "Premium Content Access",
  payment_requirements: [
    {
      asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", // USDC on Base
      pay_to: "0x1234567890abcdef1234567890abcdef12345678",
      network: "base",
      amount: "10000", // $0.01 in USDC (6 decimals)
    },
  ],
});
```

## Returns

```typescript theme={null}
type PaymentInstructionResponse = {
  data: PaymentInstruction;
};

type PaymentInstruction = {
  id: string;
  version: number;
  payment_requirements: PaymentRequirement[];
  name: string;
  description?: string;
  created_at: string;
};

type PaymentRequirement = {
  asset: string;
  pay_to: string;
  network: "base" | "base-sepolia" | "eip155:8453" | "eip155:84532";
  amount: string;
  description?: string;
};
```

## Parameters

### name (required)

* Type: `string`

The name for the payment instruction

```typescript {2} theme={null}
const instruction = await pinata.x402.createPaymentInstruction({
  name: "Premium Content Access",
  payment_requirements: [
    {
      asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", // USDC on Base
      pay_to: "0x1234567890abcdef1234567890abcdef12345678",
      network: "base",
      amount: "10000", // $0.01 in USDC (6 decimals)
    },
  ],
});
```

### payment\_requirements (required)

* Type: `PaymentRequirement[]`

An array of payment requirements. Each requirement specifies the asset, recipient address, network, and amount required for access.

```typescript {3-9} theme={null}
const instruction = await pinata.x402.createPaymentInstruction({
  name: "Premium Content Access",
  payment_requirements: [
    {
      asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", // USDC on Base
      pay_to: "0x1234567890abcdef1234567890abcdef12345678",
      network: "base",
      amount: "10000", // $0.01 in USDC (6 decimals)
    },
  ],
});
```

#### PaymentRequirement Properties

| Property      | Type                                                                | Required | Description                                     |
| ------------- | ------------------------------------------------------------------- | -------- | ----------------------------------------------- |
| `asset`       | `string`                                                            | Yes      | The USDC token contract address for the network |
| `pay_to`      | `string`                                                            | Yes      | The wallet address to receive payments          |
| `network`     | `"base"` \| `"base-sepolia"` \| `"eip155:8453"` \| `"eip155:84532"` | Yes      | The blockchain network                          |
| `amount`      | `string`                                                            | Yes      | The maximum amount required for access          |
| `description` | `string`                                                            | No       | Optional description for this requirement       |

### description

* Type: `string`

An optional description for the payment instruction

```typescript {10} theme={null}
const instruction = await pinata.x402.createPaymentInstruction({
  name: "Premium Content Access",
  payment_requirements: [
    {
      asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", // USDC on Base
      pay_to: "0x1234567890abcdef1234567890abcdef12345678",
      network: "base",
      amount: "10000", // $0.01 in USDC (6 decimals)
    },
  ],
  description: "Access to exclusive premium content",
});
```


# delete
Source: https://docs.pinata.cloud/sdk/x402/payment-instructions/delete



Delete a payment instruction

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const result = await pinata.x402.deletePaymentInstruction(
  "01234567-89ab-cdef-0123-456789abcdef"
);
```

## Returns

```typescript theme={null}
type PaymentInstructionDeleteResponse = {
  data: {};
};
```

## Parameters

### id (required)

* Type: `string`

The unique identifier of the payment instruction to delete

```typescript theme={null}
const result = await pinata.x402.deletePaymentInstruction(
  "01234567-89ab-cdef-0123-456789abcdef"
);
```


# get
Source: https://docs.pinata.cloud/sdk/x402/payment-instructions/get



Retrieve a specific payment instruction by ID

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const instruction = await pinata.x402.getPaymentInstruction(
  "01234567-89ab-cdef-0123-456789abcdef"
);
```

## Returns

```typescript theme={null}
type PaymentInstructionResponse = {
  data: PaymentInstruction;
};

type PaymentInstruction = {
  id: string;
  version: number;
  payment_requirements: PaymentRequirement[];
  name: string;
  description?: string;
  created_at: string;
};

type PaymentRequirement = {
  asset: string;
  pay_to: string;
  network: "base" | "base-sepolia" | "eip155:8453" | "eip155:84532";
  amount: string;
  description?: string;
};
```

## Parameters

### id (required)

* Type: `string`

The unique identifier of the payment instruction to retrieve

```typescript theme={null}
const instruction = await pinata.x402.getPaymentInstruction(
  "01234567-89ab-cdef-0123-456789abcdef"
);
```


# list
Source: https://docs.pinata.cloud/sdk/x402/payment-instructions/list



List and filter payment instructions for x402 monetization

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const instructions = await pinata.x402.listPaymentInstructions();
```

## Returns

```typescript theme={null}
type PaymentInstructionListResponse = {
  data: {
    payment_instructions: PaymentInstruction[];
    next_page_token?: string;
  };
};

type PaymentInstruction = {
  id: string;
  version: number;
  payment_requirements: PaymentRequirement[];
  name: string;
  description?: string;
  created_at: string;
};

type PaymentRequirement = {
  asset: string;
  pay_to: string;
  network: "base" | "base-sepolia" | "eip155:8453" | "eip155:84532";
  amount: string;
  description?: string;
};
```

## Parameters

Filter response with the following optional parameters.

### limit

* Type: `number`

Limit the number of results returned

```typescript {2-4} theme={null}
const instructions = await pinata.x402.listPaymentInstructions({
  limit: 10,
});
```

### pageToken

* Type: `string`

Paginate through results using a page token from a previous response

```typescript {2-4} theme={null}
const instructions = await pinata.x402.listPaymentInstructions({
  pageToken: "MDE5MWIzZWYtM2U0Zi03YTY5LWE3OTQtOTRhZDE5NjQxMTk0",
});
```

### cid

* Type: `string`

Filter payment instructions by associated CID

```typescript {2-4} theme={null}
const instructions = await pinata.x402.listPaymentInstructions({
  cid: "bafkreih5aznjvttude6c3wbvqeebb6rlx5wkbzyppv7garjiubll2ceym4",
});
```

### name

* Type: `string`

Filter payment instructions by name

```typescript {2-4} theme={null}
const instructions = await pinata.x402.listPaymentInstructions({
  name: "Premium Content",
});
```

### id

* Type: `string`

Filter by specific payment instruction ID

```typescript {2-4} theme={null}
const instructions = await pinata.x402.listPaymentInstructions({
  id: "01234567-89ab-cdef-0123-456789abcdef",
});
```


# update
Source: https://docs.pinata.cloud/sdk/x402/payment-instructions/update



Update an existing payment instruction

## Usage

```typescript theme={null}
import { PinataSDK } from "pinata";

const pinata = new PinataSDK({
  pinataJwt: process.env.PINATA_JWT!,
  pinataGateway: "example-gateway.mypinata.cloud",
});

const instruction = await pinata.x402.updatePaymentInstruction(
  "01234567-89ab-cdef-0123-456789abcdef",
  {
    name: "Updated Premium Content",
  }
);
```

## Returns

```typescript theme={null}
type PaymentInstructionResponse = {
  data: PaymentInstruction;
};

type PaymentInstruction = {
  id: string;
  version: number;
  payment_requirements: PaymentRequirement[];
  name: string;
  description?: string;
  created_at: string;
};

type PaymentRequirement = {
  asset: string;
  pay_to: string;
  network: "base" | "base-sepolia" | "eip155:8453" | "eip155:84532";
  amount: string;
  description?: string;
};
```

## Parameters

### id (required)

* Type: `string`

The unique identifier of the payment instruction to update

```typescript theme={null}
const instruction = await pinata.x402.updatePaymentInstruction(
  "01234567-89ab-cdef-0123-456789abcdef",
  {
    name: "Updated Name",
  }
);
```

### name

* Type: `string`

Update the name of the payment instruction

```typescript {4} theme={null}
const instruction = await pinata.x402.updatePaymentInstruction(
  "01234567-89ab-cdef-0123-456789abcdef",
  {
    name: "Updated Premium Content",
  }
);
```

### payment\_requirements

* Type: `PaymentRequirement[]`

Update the payment requirements array

```typescript {4-11} theme={null}
const instruction = await pinata.x402.updatePaymentInstruction(
  "01234567-89ab-cdef-0123-456789abcdef",
  {
    payment_requirements: [
      {
        asset: "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913", // USDC on Base
        pay_to: "0xnewaddress1234567890abcdef12345678",
        network: "base",
        amount: "20000", // $0.02 in USDC (6 decimals)
      },
    ],
  }
);
```

#### PaymentRequirement Properties

| Property      | Type                                                                | Required | Description                                     |
| ------------- | ------------------------------------------------------------------- | -------- | ----------------------------------------------- |
| `asset`       | `string`                                                            | Yes      | The USDC token contract address for the network |
| `pay_to`      | `string`                                                            | Yes      | The wallet address to receive payments          |
| `network`     | `"base"` \| `"base-sepolia"` \| `"eip155:8453"` \| `"eip155:84532"` | Yes      | The blockchain network                          |
| `amount`      | `string`                                                            | Yes      | The amount required for access                  |
| `description` | `string`                                                            | No       | Optional description for this requirement       |

### description

* Type: `string`

Update the description of the payment instruction

```typescript {4} theme={null}
const instruction = await pinata.x402.updatePaymentInstruction(
  "01234567-89ab-cdef-0123-456789abcdef",
  {
    description: "Updated description for the payment instruction",
  }
);
```


