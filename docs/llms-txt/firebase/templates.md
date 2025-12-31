# Source: https://firebase.google.com/docs/extensions/official/firestore-send-email/templates.md.txt

# Source: https://firebase.google.com/docs/remote-config/templates.md.txt

<br />

Client templatesServer templates  

<br />

Remote Configtemplates are sets of JSON-formatted parameters and conditions that you have created for your Firebase project. You can create*client* templates, from which your app fetches values, and*server*templates, from which server clients can fetch values.
This section discusses client templates. To learn about server-specific templates, click[**Server templates**](https://firebase.google.com/docs/remote-config/templates?template_type=server).

You modify and manage the template using theFirebaseconsole, which displays the contents of the template in graphical format in the[Parameters](https://console.firebase.google.com/project/_/config)and[Conditions](https://console.firebase.google.com/project/_/config/conditions)tabs.

You can also use the[theRemote ConfigREST API and Admin SDK](https://firebase.google.com/docs/remote-config/automate-rc)or the[FirebaseCLI](https://firebase.google.com/docs/cli#config-commands)to modify and manage your client template.

Here's an example of a server template file:  

    {
      "parameters": {
        "preamble_prompt": {
          "defaultValue": {
            "value": "You are a helpful assistant who knows everything there is to know about Firebase! "
          },
          "description": "Add this prompt to the user's prompt",
          "valueType": "STRING"
        },
        "model_name": {
          "defaultValue": {
            "value": "gemini-pro-test"
          },
          "valueType": "STRING"
        },
        "generation_config": {
          "defaultValue": {
            "value": "{\"temperature\": 0.9, \"maxOutputTokens\": 2048, \"topP\": 0.9, \"topK\": 20}"
          },
          "valueType": "JSON"
        },
      },
      "version": {
        "versionNumber": "19",
        "isLegacy": true
      }
    }

You can perform these version management tasks with theFirebaseconsole:

- List all stored template versions
- Retrieve a specific version
- Roll back to a specific client version
- DeleteRemote Configtemplates from the[Change history](https://console.firebase.google.com/project/_/config/history)page

There is a total limit of 300 lifetime stored versions per template type (300 client templates and 300 server templates), which includes stored version numbers for deleted templates. If you publish more than 300 template versions per template type during the lifetime of a project, the earliest versions are deleted, maintaining a maximum of 300 versions of that type.

Each time you update parameters,Remote Configcreates a new versionedRemote Configtemplate and stores the previous template as a version that you can retrieve or roll back to as needed. Version numbers are incremented sequentially from the initial value stored byRemote Config. All templates include a`version`field as shown, containing metadata about that specific version.

You can deleteRemote Configtemplates as-needed from the[Change history](https:////console.firebase.google.com/project/_/config/history)page on theRemote Configconsole.

## ManageRemote Configtemplate versions

This section describes how to manage versions of yourRemote Configtemplate.

### List all stored versions of theRemote Configtemplate

You can retrieve a list of all stored versions of theRemote Configtemplate. To do this:  

### Firebaseconsole

In the[Parameters](https://console.firebase.google.com/project/_/config)tab, select the "clock" icon displayed at top right. This opens the[Change history](https://console.firebase.google.com/project/_/config/history)page listing all stored template versions in a list menu at the right.

Details displayed for each stored version include information on whether the changes originated with the Console, with the REST API, from a rollback, or whether they were incremental changes from a forced save of the template.

### FirebaseCLI

```
firebase remoteconfig:versions:list
```

Use the`--limit`option to limit the number of versions being returned. Pass '0' to fetch all versions.

### Node.js

    function listAllVersions() {
      admin.remoteConfig().listVersions()
        .then((listVersionsResult) => {
          console.log("Successfully fetched the list of versions");
          listVersionsResult.versions.forEach((version) => {
            console.log('version', JSON.stringify(version));
          });
        })
        .catch((error) => {
          console.log(error);
        });
    }

### Java

```java
ListVersionsPage page = FirebaseRemoteConfig.getInstance().listVersionsAsync().get();
while (page != null) {
  for (Version version : page.getValues()) {
    System.out.println("Version: " + version.getVersionNumber());
  }
  page = page.getNextPage();
}

// Iterate through all versions. This will still retrieve versions in batches.
page = FirebaseRemoteConfig.getInstance().listVersionsAsync().get();
for (Version version : page.iterateAll()) {
  System.out.println("Version: " + version.getVersionNumber());
}
```

### REST

    curl --compressed -D headers -H "Authorization: Bearer <var>token</var>" -X GET https://firebaseremoteconfig.googleapis.com/v1/projects/<var>my-project-id</var>/remoteConfig:listVersions

The list of templates includes metadata for all stored versions, including the time of the update, the user who made it, and how it was made. Here is an example of a version element:  

    ```json
    {
      "versions": [{
        "version_number": "6",
        "update_time": "2022-05-12T02:38:54Z",
        "update_user": {
          "name": "Jane Smith",
          "email": "jane@developer.org",
          "imageUrl": "https://lh3.googleusercontent.com/a-/..."
        },
        "description": "One small change on the console",
        "origin": "CONSOLE",
        "update_type": "INCREMENTAL_UPDATE"
      }]
    }
    ```

### Retrieve a specific version of theRemote Configtemplate

You can retrieve any specific stored version of theRemote Configtemplate. To retrieve a stored template version:  

### Firebaseconsole

By default, the details pane in the[Change history](https://console.firebase.google.com/project/_/config/history)tab displays the current active template. To view details for another version in the list, select it from the right menu.

You can view a detailed diff of the currently selected version and any other stored version by hovering over the context menu for any non-selected version and selecting**Compare with selected version.**

### FirebaseCLI

```
firebase remoteconfig:get -v VERSION_NUMBER
```

Optionally, you can write the output to a specified file with`-o, `<var translate="no">FILENAME</var>.

### Node.js

Pass`getTemplate()`without any arguments to retrieve the latest version of the template, or to retrieve a specific version, use`getTemplateAtVersion()`.  

    // Get template version: 6
    admin.remoteConfig().getTemplateAtVersion('6')
      .then((template) => {
        console.log("Successfully fetched the template with ETag: " + template.etag);
      })
      .catch((error) => {
        console.log(error);
      });

### Java

```java
Template template = FirebaseRemoteConfig.getInstance().getTemplateAtVersionAsync(versionNumber).get();
// See the ETag of the fetched template.
System.out.println("Successfully fetched the template with ETag: " + template.getETag());
```

### REST

    curl --compressed -D headers -H "Authorization: Bearer <var>token</var>" -X GET https://firebaseremoteconfig.googleapis.com/v1/projects/<var>my-project-id</var>/remoteConfig?version_number=6

The URL parameter`?version_number`is valid only for`GET`operations; you cannot use it to specify version numbers for updates. A similar get request without the`?version_number`parameter would retrieve the current active template.

### Roll back to a specific stored version of theRemote Configtemplate

You can roll back to any stored version of the template. To roll back a template:  

### Firebaseconsole

For previous template versions eligible for rollback, an option button to roll back to that version is displayed at top right of the[Change history](https://console.firebase.google.com/project/_/config/history)page. Click and confirm this only if you are sure you want to roll back to that version and use those values*immediately*for all apps and users.

### FirebaseCLI

```
firebase remoteconfig:rollback -v VERSION_NUMBER
```

### Node.js

    // Roll back to template version: 6
    admin.remoteConfig().rollback('6')
      .then((template) => {
        console.log("Successfully rolled back to template version 6.");
        console.log("New ETag: " + template.etag);
      })
      .catch((error) => {
        console.log('Error trying to rollback:', e);
      })

### Java

```java
try {
  Template template = FirebaseRemoteConfig.getInstance().rollbackAsync(versionNumber).get();
  System.out.println("Successfully rolled back to template version: " + versionNumber);
  System.out.println("New ETag: " + template.getETag());
} catch (ExecutionException e) {
  if (e.getCause() instanceof FirebaseRemoteConfigException) {
    FirebaseRemoteConfigException rcError = (FirebaseRemoteConfigException) e.getCause();
    System.out.println("Error trying to rollback template.");
    System.out.println(rcError.getMessage());
  }
}
```

### REST

To roll back to a storedRemote Configtemplate, issue an HTTP POST with the custom method`:rollback`and, in the request body, the specific version to apply. For example:  

    curl --compressed -D headers -H "Authorization: Bearer <var>token</var>" -H "Content-Type: application/json" -X POST https://firebaseremoteconfig.googleapis.com/v1/projects/<var>my-project-id</var>/remoteConfig:rollback -d '{"version_number": 6}'

The response contains the contents of the now-active stored template, with its new version metadata.

Note that this rollback operation effectively creates a new numbered version. For example, rolling back from version 10 to version 6 effectively creates a new copy of version 6, differing from the original only in that its version number is 11. The original version 6 is still stored, assuming it has not reached its expiration, and version 11 becomes the active template.

### Delete aRemote Configtemplate

You can deleteRemote Configtemplates from theFirebaseconsole. To delete aRemote Configtemplate:
1. From theRemote Config[Parameters](https:////console.firebase.google.com/project/_/config)page, clickhistory[**Change history**](https:////console.firebase.google.com/project/_/config/history).

1. Toggle to the template you want to delete, clickmore_vert**More** , then select**Delete**.

2. When prompted to confirm the deletion, click**Delete**.

### Download and publishRemote Configtemplates

Download and publishRemote Configtemplates to integrate them into your source control and build systems, automate config updates, and keep parameters and values in sync across multiple projects.

You can download the currently activeRemote Configtemplate from theFirebaseconsole. You can then update the exported JSON file and publish it to the same project, or publish it to a new or existing project.

Let's say you have multiple projects that represent different stages of your software development lifecycle, like development, test, staging, and production environments. In this case, you could promote a fully-tested template from your staging environment to your production environment by downloading it from your staging project and publishing it to your production project.

You can also use this method to migrate configurations from one project to another, or populate a new project with parameters and values from an established project.

Parameters and parameter values created specifically as variants in anA/B Testingexperiment are not included in exported templates.

To export and importRemote Configtemplates:

1. [Download the currentRemote ConfigConfig template](https://firebase.google.com/docs/remote-config/templates#download_current_template).
2. [Validate theRemote Configtemplate](https://firebase.google.com/docs/remote-config/templates#validate_template).
3. [Publish theRemote Configtemplate](https://firebase.google.com/docs/remote-config/templates#publish_template).

#### Download the current Remote Config Template

Use the following to download the activeRemote Configtemplate in JSON format:  

### Firebaseconsole

1. From the[Remote ConfigParameters or Conditions](https://console.firebase.google.com/project/_/config)tab, open themore_vert**Menu** , and select**Download current config file**.
2. When prompted, click**Download config file** , choose the location where you want to save the file, then click**Save**.

### FirebaseCLI

```
firebase remoteconfig:get -o filename
```

### Node.js

```javascript
function getTemplate() {
  var config = admin.remoteConfig();
  config.getTemplate()
      .then(function (template) {
        console.log('ETag from server: ' + template.etag);
        var templateStr = JSON.stringify(template);
        fs.writeFileSync('config.json', templateStr);
      })
      .catch(function (err) {
        console.error('Unable to get template');
        console.error(err);
      });
}
```

### Java

```java
Template template = FirebaseRemoteConfig.getInstance().getTemplateAsync().get();
// See the ETag of the fetched template.
System.out.println("ETag from server: " + template.getETag());
```

### REST

```restructuredtext
curl --compressed -D headers -H "Authorization: Bearer token" -X GET https://firebaseremoteconfig.googleapis.com/v1/projects/my-project-id/remoteConfig -o filename
```

This command outputs the JSON payload to one file, and the headers (including the ETag) to a separate`headers`file.

#### Validate the Remote Config template

You can validate your template updates before publishing them using theFirebaseAdmin SDKor the REST API. Templates are also validated when you attempt to publish from theFirebaseCLI orFirebaseconsole.

<br />

The template validation process checks for errors such as duplicate keys for parameters and conditions, invalid condition names or nonexistent conditions, or misformatted ETags. For example, a request containing more than the allowed number of keys---2000---would return the error message,`Param count too
large`.  

### Node.js

```javascript
function validateTemplate(template) {
  admin.remoteConfig().validateTemplate(template)
      .then(function (validatedTemplate) {
        // The template is valid and safe to use.
        console.log('Template was valid and safe to use');
      })
      .catch(function (err) {
        console.error('Template is invalid and cannot be published');
        console.error(err);
      });
}
```

### Java

```java
try {
  Template validatedTemplate = FirebaseRemoteConfig.getInstance()
          .validateTemplateAsync(template).get();
  System.out.println("Template was valid and safe to use");
} catch (ExecutionException e) {
  if (e.getCause() instanceof FirebaseRemoteConfigException) {
    FirebaseRemoteConfigException rcError = (FirebaseRemoteConfigException) e.getCause();
    System.out.println("Template is invalid and cannot be published");
    System.out.println(rcError.getMessage());
  }
}
```

### REST

Validate template updates by appending URL parameter`?validate_only=true`to your publish request:

<br />

```restructuredtext
curl --compressed -H "Content-Type: application/json; UTF8" -H "If-Match: last-returned-etag" -H "Authorization: Bearer token" -X PUT https://firebaseremoteconfig.googleapis.com/v1/projects/my-project-id/remoteConfig?validate_only=true -d @filename
```

<br />

If your template was successfully validated, the curl command returns the JSON template you submitted and, in the saved`headers`file, you'll find an HTTP/2 status 200 and an updated ETag with the suffix`-0`. If your template was not validated, you'll receive the validation error in the JSON response and your`headers`file will contain a non-200 response (and no ETag).

#### Publish theRemote Configtemplate

After downloading a template, making any needed changes to the JSON content, and validating it, you can publish it to a project.

Publishing a template replaces the entire existing config template with the updated file and increments the template version by one. Because the entire configuration is replaced, if you delete a parameter from the JSON file and publish it, the parameter is deleted from the server and is no longer available to clients.

After publishing, changes to parameters and values are*immediately* available to your apps and users. If necessary, you can[roll back to a previous version](https://firebase.google.com/docs/remote-config/templates#rollback).

Use the following commands to publish your template:  

### Firebaseconsole

1. From the[Remote ConfigParameters or Conditions](https://console.firebase.google.com/project/_/config)tab, open themore_vert**Menu** , and select**Publish from a file**.
2. When prompted, click**Browse** , navigate to and select theRemote Configfile you want to publish, then click**Select**.
3. The file will be validated and, if successful, you can click**Publish**to make the configuration immediately available to your apps and users.

### Node.js

```javascript
function publishTemplate() {
  var config = admin.remoteConfig();
  var template = config.createTemplateFromJSON(
      fs.readFileSync('config.json', 'UTF8'));
  config.publishTemplate(template)
      .then(function (updatedTemplate) {
        console.log('Template has been published');
        console.log('ETag from server: ' + updatedTemplate.etag);
      })
      .catch(function (err) {
        console.error('Unable to publish template.');
        console.error(err);
      });
}
```

### Java

```java
try {
  Template publishedTemplate = FirebaseRemoteConfig.getInstance()
          .publishTemplateAsync(template).get();
  System.out.println("Template has been published");
  // See the ETag of the published template.
  System.out.println("ETag from server: " + publishedTemplate.getETag());
} catch (ExecutionException e) {
  if (e.getCause() instanceof FirebaseRemoteConfigException) {
    FirebaseRemoteConfigException rcError = (FirebaseRemoteConfigException) e.getCause();
    System.out.println("Unable to publish template.");
    System.out.println(rcError.getMessage());
  }
}
```

### REST

```restructuredtext
curl --compressed -H "Content-Type: application/json; UTF8" -H "If-Match: last-returned-etag" -H "Authorization: Bearer token" -X PUT https://firebaseremoteconfig.googleapis.com/v1/projects/my-project-id/remoteConfig -d @filename
```

For this`curl`command, you can specify the content by using the "@" character, followed by the filename.

Remote Configpersonalizations and conditions are included in downloaded templates, so it's important to be aware of the following limitations when attempting to publish to a different project:

- Personalizations cannot be imported from project to project.

  For example, if you have personalizations enabled in your project and download and edit a template, you can publish it to the same project, but you can't publish it to a different project unless you delete the personalizations from the template.
- Conditions can be imported from project to project, but note that any specific conditional values (like app IDs or audiences), should exist in the target project before publishing.

  For example, if you have aRemote Configparameter that uses a condition that specifies a platform value of`iOS`, the template can be published to another project, because platform values are the same for any project. However, if it contains a condition that relies on a specific app ID or user audience that doesn't exist in the target project, validation will fail.
- If the template you plan to publish contains conditions that rely onGoogle Analytics,Analyticsmust be enabled in the target project.

### DownloadRemote Configtemplate defaults

Because your app may not always be connected to the Internet, you should configure client-side app default values for allRemote Configparameters. You should also periodically synchronize your app client default values andRemote Configbackend default parameter values, because they may change over time.

As described in the platform-specific links at the end of this section, you can manually set these defaults in your app or you can streamline this process by downloading files that contain*only* the key-value pairs for all parameters and their default values in the activeRemote Configtemplate. You can then include this file in your project and configure your app to import these values.

You can download these files in XML format for Android apps, property list (plist) format for iOS apps, and JSON for web apps.

We recommend periodically downloadingRemote Configdefaults before any new app release to ensure that your app and theRemote Configbackend stay in sync.
| **Warning:** If**(in-app default)** is enabled forRemote Configparameters, the downloaded default values will be empty. When using this feature, we recommend configuring default values for all parameters in theFirebaseconsole.

To download a file that contains template defaults:  

### REST

```
curl --compressed -D headers -H "Authorization: Bearer token -X GET https://firebaseremoteconfig.googleapis.com/v1/projects/my-project-id/remoteConfig:downloadDefaults?format=file_format'
```

Use`XML`,`PLIST`, or`JSON`as the`format`value, depending on which file format you want to download.

### Firebaseconsole

1. In the[Parameters](https://console.firebase.google.com/project/_/config)tab, open themore_vert**Menu** , and select**Download default values**.
2. When prompted, click the radio button that corresponds to the file format you want to download, and then click**Download file**.

For more information about importingRemote Configdefault values into your app, see:

- [Set in-app default parameter values for Android](https://firebase.google.com/docs/remote-config/get-started?&platform=android#set_in_app_default_parameter_values)

- [Set in-app default parameter values for iOS](https://firebase.google.com/docs/remote-config/get-started?&platform=ios#set_in_app_default_parameter_values)

- [Set in-app default parameter values for Web](https://firebase.google.com/docs/remote-config/get-started?&platform=web#set_in_app_default_parameter_values)

- [Set in-app default parameter values for Unity](https://firebase.google.com/docs/remote-config/get-started?&platform=unity#set_in_app_default_parameter_values)

- [Set in-app default parameter values for C++](https://firebase.google.com/docs/remote-config/get-started?&platform=cpp#set_in_app_default_parameter_values)