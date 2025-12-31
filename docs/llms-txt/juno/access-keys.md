# Source: https://juno.build/docs/miscellaneous/access-keys.md

# Access Keys

Access keys play a crucial role in granting permissions to Mission Controls, Satellites or Analytics within Juno.

When you sign in to Juno's [Console](/docs/terminology.md#console) using [Internet Identity](https://internetcomputer.org/internet-identity), you â and no one else (including not Juno) â become the owner of your [mission control](/docs/terminology.md#mission-control). This information is then sent back to your browser, where you can manage your modules.

![Juno&#39;s console flow](/assets/images/console-d0903e4989f7c4db5f4e85567211d266.png)

When you create a [satellite](/docs/terminology.md#satellite), you and your mission control become its owners. Per extension, you â and no one else (including not Juno) â own your satellite.

**Note:**

*   What was previously referred to as _controllers_ in earlier versions of the documentation is now called _administrative access keys_. The concept remains the same â only the terminology has been updated for clarity and consistency.
*   One access key is identified by a [principal](/docs/terminology.md#principal).

---

## Roles

Each access key is assigned a **role** that defines what it can do:

| Role (Internal) | Display Name | Can Submit | Can Apply/Commit | Can Deploy Immediately | Can Upgrade Immediately |
| --- | --- | --- | --- | --- | --- |
| **Admin** | Administrator | â   | â   | â   | â   |
| **Write** | Editor | â   | â   | â   | â   |
| **Submit** | Submitter | â   | â   | â   | â   |

An **administrator** can perform tasks such as configuring or deploying an app, topping up a mission control or satellite, creating a new collection in the [datastore](/docs/build/datastore.md) or [storage](/docs/build/storage.md), or configuring a custom domain in the [hosting](/docs/build/hosting.md).

An **editor** can publish new serverless function versions to a Satelliteâs CDN, deploy your frontend application, and read data from a collection. However, it cannot directly upgrade a Satellite or start/stop a module.

A **submitter** can propose changesâsuch as publishing a new version of a serverless function or frontend appâbut those changes must be manually reviewed and applied using the Console UI or CLI.

---

## Generating Access Keys

You can generate additional access keys to allow other developers, services, or CI pipelines to interact with your modules. When doing so, you can assign a role based on the level of access required.

Access keys can be generated either through the Console UI or using the CLI.

**Note:**

You can generate a limited number of administrator access keys for a single module, in line with the limitation set by the [Internet Computer](https://internetcomputer.org/docs/current/references/ic-interface-spec#ic-create_canister).

To accomplish this, you have two main options.

**Tip:**

When creating a new Satellite, itâs very likely that youâll want to generate access keys for local development or to enable automated deployments from CI. Check out the guides:

*   [GitHub Actions](/docs/guides/github-actions.md)
*   [Manual Deployments](/docs/guides/manual-deployment.md)

---

## Generate an Access Key with the Console UI

You can generate and manage access keys through the Console:

1.  Go to [http://console.juno.build](http://console.juno.build) and select your module (Satellite, Analytics or Mission Control)
2.  Open the **Setup** tab
3.  Scroll to the **Access Keys** section and click **Add an access key**
4.  Choose **Generate a new access key**
5.  Select the desired role (e.g., **Administrator**)
6.  Click **Submit**

You can also manually enter an access key instead of generating one, if you wish to reuse an existing one.

---

## Generate an Access Key with the CLI

When using the CLI, you can either reuse an existing access key or generate a new one.

---

### Reuse an existing access key

When setting up an additional Satellite, you might want to reuse an existing access key already configured on your local machine. To do this, simply run:

```
juno login
```

and follow the instructions.

When you run the command, the CLI checks if an access key is already present on your machine. If found, it will give you the option to either reuse the existing key or generate a new one. If you choose to reuse it, the CLI will guide you through the process.

---

### Generate a new access key

To **generate a new access key** and attach it to your desired Mission Controls and Satellites, you can run:

```
juno login
```

The CLI will guide you through the process.

This method is useful if you want to generate a completely new key and apply it across all your modules.

**Note:**

This action will overwrite the previously saved key used to configure your local CLI environment.