# Source: https://firebase.google.com/docs/extensions/publishers/register.md.txt

<br />

Before you can share extensions you create with others, you must register as a publisher. When you register as an extensions publisher, you create a publisher ID that lets users quickly identify you as the author of your extensions. Users will install your extension by specifying an extensions name that looks like the following example:  

```
your-publisher-id/your-extension-id
```

<br />

Your publisher ID will generally be your company's name or your brand name. Take some time to choose a publisher ID because you won't be able to change it later without registering a new one and republishing your extensions.

Your publisher ID will be permanently linked to a Firebase project, which is dedicated for IAM activities, publishing extensions, and viewing metrics. You should use this project exclusively for managing published extensions (that is, don't add any apps to the project and don't enable any other Firebase services in it). By using a dedicated project, you keep your extensions publishing activities insulated from your other Firebase project management activities.

The publisher project will have a[project lien](https://cloud.google.com/resource-manager/docs/project-liens)placed on it to prevent accidental deletion. To request deletion of your publisher profile and project, contact`firebase-extensions-publisher-projects@google.com`.

<br />

| Firebase uses your publisher project**only** for managing who can publish extensions under your publisher ID (using IAM permissions) and for surfacing extension metrics.
|
| <br />
|
| - The project doesn't host your extensions code.
| - The project doesn't have access to any data collected or created by your extension.

To register, click the button below:

[Register as an extensions publisher](https://console.firebase.google.com/?createPublisherProfile)

This will create a new publisher project and profile. After you've registered, you can view your profile from the same page.

If your Google Cloud organization has[policy constraints](https://cloud.google.com/resource-manager/docs/organization-policy/overview)that make it difficult to register a publisher profile through the Firebase console, you can instead use the Firebase CLI to turn an existing project into a publisher project:  

    firebase ext:dev:register --project=<var translate="no">PROJECT_ID</var>

Make sure the project is a Firebase project. If you have a Google Cloud project,[convert it to a Firebase project](https://firebase.google.com/docs/cli#management-commands)first. Don't use existing projects in which you use other Firebase services, as publisher projects are treated differently, and you can't easily access those services in the Firebase console.
| **Note:** If you need to unregister a publisher ID---for example, to link the ID to a different project---contact[support](https://firebase.google.com/support/troubleshooter/contact).