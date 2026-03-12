# Source: https://developers.make.com/custom-apps-documentation/create-your-first-app/app-visibility.md

# App visibility

## Private app

A private app **can only be used by the author** of the app until the app is installed in an organization to which the author and other users have access.

{% hint style="info" %}
If you want to make your app available to everyone in your organization, create a new scenario with your app and save the scenario there.

In the dialog box, confirm the installation.
{% endhint %}

A private tag is displayed after your app's name on the app's page.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-123413ee13203306b7c10614630e09f5791e1aaa%2Fappvisibility_private.png?alt=media" alt="" width="236"></div>

### Deletion of a private app

If your private app is not used in any of your scenarios, you can delete the private app.

### Deletion of a module

You can delete a module for a private app only if it is not used in any scenario. If you try to delete a module used in a scenario, you will see a warning dialog with a request to remove the module from the scenario first.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-29150027ffcbc8727d359297281074e655a533b3%2Fdelete_module_warning.png?alt=media" alt="" width="365"></div>

### Deletion of a webhook, connection, RPC, or custom IML function

You can delete a webhook, connection, RPC, or custom IML function only if it is not used in any module. If you try to do so, you will see a warning dialog in the lower-right corner.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-8a1200ca01c7a66d40be948c90775ec355276d1e%2FScreen%20Shot%202022-08-22%20at%2017.59.44.png?alt=media" alt="" width="254"></div>

## Public app

If you want to share your app outside of your organization, you need to publish your app to generate an invite link.

Go to your app and open your app's page. Click **Publish** in the right upper corner.

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-d2e57a05e6b91d4b54f8382e5c499478e3701f17%2Fpublish_app.png?alt=media" alt="" width="563"></div>

Once you publish the app, the invite link is generated. You can share it with any other Maker who will then install it in their organization. It doesn't matter where the organization is located (EU1 or US1).

<div align="left"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-aad9f313702abe0511be230c192654a8c460964b%2Finvite_users.png?alt=media" alt="" width="563"></div>

### Deletion of a public app

{% hint style="warning" %}
Once the app is published, it is not possible to delete the app or make it private again.
{% endhint %}

If you wish to have your public app deleted, [contact our support team](https://www.make.com/en/login?source=ticket) and we will remove the app from your account.

### Deletion of a module, webhook, connection, RPC, or custom IML function

{% hint style="warning" %}
Once the app is published, it is not possible to delete any module or component.
{% endhint %}

We recommend you change the component's label to indicate that the component should not be used, e.g. `[DO NOT USE] My unwanted module`. Make sure the module is hidden.

### Distribution control of modules

If you actively share your public app via an invite link, you can control the distribution of modules that you have in your public app by making them hidden/visible.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-87f83f2db68b1a1c0d30835e4407f34c33f52561%2Fhidden_visible.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

If you hide an already visible module that is currently in use in a scenario, the module will continue working in the scenario. However, the hidden module will not be available in the app selector in a new scenario.

## Approved app

Approved apps are available to any user in Make. If you want to have your app available to all Makers, review the [app review procedure](https://developers.make.com/custom-apps-documentation/app-review/overview) to ensure that your app follows best practices.

Once you make sure your app follows our conditions and best practices, you can [request an app review](https://developers.make.com/custom-apps-documentation/app-review/request-app-review).

If the app [passes our review process](https://developers.make.com/custom-apps-documentation/app-review/approved-app), it becomes available for everyone to use. That mean's that any user on Make can add your app to his/her scenario and use it.
