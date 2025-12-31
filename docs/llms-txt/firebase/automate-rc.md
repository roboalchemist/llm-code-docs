# Source: https://firebase.google.com/docs/remote-config/automate-rc.md.txt

<br />

This document describes how you can programmatically read and modify the set of JSON-formatted parameters and conditions known as the[Remote Configtemplate](https://firebase.google.com/docs/remote-config/templates). This allows you to make template changes on the backend that the client app can fetch using the client library.

Using the[Remote ConfigREST API](https://firebase.google.com/docs/reference/remote-config/rest)or the[Admin SDKs](https://firebase.google.com/docs/admin/setup)described in this guide, you can bypass managing the template in theFirebaseconsole to directly integrateRemote Configchanges into your own processes. For example, withRemote Configbackend APIs, you could:

- **SchedulingRemote Configupdates** . By using API calls in conjunction with a cron job, you can changeRemote Configvalues on a regular schedule.
- **Batch import config values** in order to transition efficiently from your own proprietary system toFirebase Remote Config.
- **UseRemote ConfigwithCloud Functions for Firebase** , changing values in your app based on events that happen server-side. For example, you can useRemote Configto promote a new feature in your app, and then turn off that promotion automatically once you detect enough people have interacted with the new feature.

  ![Diagram showing the Remote Config backend interacting with custom tools and servers](https://firebase.google.com/static/docs/remote-config/images/Diagram-RC-REST-v3-580px.png)

The following sections of this guide describe operations you can do with theRemote Configbackend APIs. To review some code that performs these tasks via the REST API, see one of these sample apps:

- [Firebase Remote Config REST API Java Quickstart](https://github.com/firebase/quickstart-java/blob/master/config)
- [Firebase Remote Config REST API Node.js Quickstart](https://github.com/firebase/quickstart-nodejs/blob/master/config)
- [Firebase Remote Config REST API Python Quickstart](https://github.com/firebase/quickstart-python/blob/master/config)

## Modify Remote Config using the Firebase Admin SDK

TheAdmin SDKis a set of server libraries that let you interact with Firebase from privileged environments. In addition to performing updates toRemote Config, theAdmin SDKenables generation and verification of Firebase auth tokens, reading and writing fromRealtime Database, and so on. To learn more aboutAdmin SDKprerequisites and setup, see[Add the Firebase Admin SDK to your server](https://firebase.google.com/docs/admin/setup).

In a typicalRemote Configflow, you might get the current template, modify some of the parameters or parameter groups and conditions, validate the template, and then publish it. Before making those API calls, you must authorize requests from the SDK.

### Initialize the SDK and authorize API requests

When you initialize theAdmin SDKwith no parameters, the SDK uses[Google Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials)and reads options from the`FIREBASE_CONFIG`environment variable. If the content of the`FIREBASE_CONFIG`variable begins with a`{`it will be parsed as a JSON object. Otherwise the SDK assumes that the string is the name of a JSON file containing the options.

For example:  

### Node.js

```javascript
const admin = require('firebase-admin');
admin.initializeApp();
```

### Java

```java
FileInputStream serviceAccount = new FileInputStream("service-account.json");
FirebaseOptions options = FirebaseOptions.builder()
        .setCredentials(GoogleCredentials.fromStream(serviceAccount))
        .build();
FirebaseApp.initializeApp(options);
```

### Get the current Remote Config Template

When working withRemote Configtemplates, keep in mind that they are versioned, and that each version has a limited lifetime from its time of creation to the time you replace it with an update: 90 days, with a total limit of 300 stored versions. See[Templates and Versioning](https://firebase.google.com/docs/remote-config/templates)for more information.

You can use the backend APIs to get the current active version of theRemote Configtemplate in JSON format.

Parameters and parameter values created specifically as variants in anA/B Testingexperiment are not included in exported templates.

To get the template:  

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
| **Tip:** You can also download the currentRemote Configtemplate directly from theFirebaseconsole. Learn more at[Download and publish Remote Config templates](https://firebase.google.com/docs/remote-config/templates#download_and_publish_templates).

### Modify Remote Config parameters

You can programmatically modify and addRemote Configparameters and parameter groups. For example, to an existing parameter group named "new_menu" you could add a parameter to control the display of seasonal information:  

### Node.js

```javascript
function addParameterToGroup(template) {
  template.parameterGroups['new_menu'].parameters['spring_season'] = {
    defaultValue: {
      useInAppDefault: true
    },
    description: 'spring season menu visibility.',
  };
}
```

### Java

```java
template.getParameterGroups().get("new_menu").getParameters()
        .put("spring_season", new Parameter()
                .setDefaultValue(ParameterValue.inAppDefault())
                .setDescription("spring season menu visibility.")
        );
```

The API allows you to create new parameters and parameter groups, or modify default values, conditional values, and descriptions. In all cases, you must explicitly publish the template after making modifications.

### Modify Remote Config conditions

You can programmatically modify and addRemote Configconditions and conditional values. For example, to add a new condition:  

### Node.js

```javascript
function addNewCondition(template) {
  template.conditions.push({
    name: 'android_en',
    expression: 'device.os == \'android\' && device.country in [\'us\', \'uk\']',
    tagColor: 'BLUE',
  });
}
```

### Java

```java
template.getConditions().add(new Condition("android_en",
        "device.os == 'android' && device.country in ['us', 'uk']", TagColor.BLUE));
```

In all cases, you must explicitly publish the template after making modifications.
| **Note:** Because every value is inherently a string forFirebase Remote Config, booleans are input as "true" and "false". They are correctly type casted as a boolean when using`getBoolean`methods. "True" or "False" or "1" or "0" are not correct representations of booleans forFirebase Remote Config.

TheRemote Configbackend APIs provide several conditions and comparison operators that you can use to change the behavior and appearance of your app. To learn more about conditions and the operators supported for these conditions, see the[conditional expression reference](https://firebase.google.com/docs/remote-config/condition-reference).

### Validate the Remote Config template

Optionally, you can validate your updates before publishing them, as shown:  

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

This validation process checks for errors such as duplicate keys for parameters and conditions, invalid condition names or nonexistent conditions, or misformatted etags. For example, a request containing more than the allowed number of keys---2000---would return the error message,`Param count too large`.

### Publish the Remote Config template

Having retrieved a template and revised it with your desired updates, you can then publish it. Publishing a template as described in this section replaces the entire existing config template with the updated file, and the new active template is assigned a version number one number greater than the template it replaced.

If necessary, you can use the REST API to[roll back to the previous version](https://firebase.google.com/docs/remote-config/templates#roll_back_to_a_specific_stored_version_of_the_template). To mitigate the risk of errors in an update, you can[validate before publishing](https://firebase.google.com/docs/remote-config/automate-rc#validate_the_remote_config_template).

Remote Configpersonalizations and conditions are included in downloaded templates, so it's important to be aware of the following limitations when attempting to publish to a different project:

- Personalizations cannot be imported from project to project.

  For example, if you have personalizations enabled in your project and download and edit a template, you can publish it to the same project, but you can't publish it to a different project unless you delete the personalizations from the template.
- Conditions can be imported from project to project, but note that any specific conditional values (like app IDs or audiences), should exist in the target project before publishing.

  For example, if you have aRemote Configparameter that uses a condition that specifies a platform value of`iOS`, the template can be published to another project, because platform values are the same for any project. However, if it contains a condition that relies on a specific app ID or user audience that doesn't exist in the target project, validation will fail.
- If the template you plan to publish contains conditions that rely onGoogle Analytics,Analyticsmust be enabled in the target project.

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
| **Tip:** You can also publish aRemote Configtemplate directly from theFirebaseconsole. Learn more at[Download and publish Remote Config templates](https://firebase.google.com/docs/remote-config/templates#download_and_publish_templates).

## Modify Remote Config using the REST API

This section describes the main capabilities of theRemote ConfigREST API at`https://firebaseremoteconfig.googleapis.com`. For full detail, see the[API reference](https://firebase.google.com/docs/reference/remote-config/rest).

### Get an access token to authenticate and authorize API requests

Firebase projects support Google[service accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk), which you can use to call Firebase server APIs from your app server or trusted environment. If you're developing code locally or deploying your application on-premises, you can use credentials obtained via this service account to authorize server requests.

To authenticate a service account and authorize it to access Firebase services, you must generate a private key file in JSON format.

**To generate a private key file for your service account:**

1. In theFirebaseconsole, open**Settings \>[Service Accounts](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk)**.

2. Click**Generate New Private Key** , then confirm by clicking**Generate Key**.

3. Securely store the JSON file containing the key.

| **Note:** The service account you use to generate credentials must have the permissions included in the[Firebase Remote Config Admin role](https://firebase.google.com/docs/projects/iam/roles-predefined-product#remote-config). If you follow the steps above and use the default FirebaseAdmin SDKservice account, the requiredRemote Configpermissions are included. If you want to update audience or user property conditions with the REST API, you'll need to add the`firebaseanalytics.resources.googleAnalyticsReadAndAnalyze`permission to a[custom role](https://cloud.google.com/iam/docs/creating-custom-roles).

When authorizing via a service account, you have two choices for providing the credentials to your application. You can either set the<var translate="no">GOOGLE_APPLICATION_CREDENTIALS</var>environment variable, or you can explicitly pass the path to the service account key in code. The first option is more secure and is strongly recommended.

**To set the environment variable:**

Set the environment variable<var translate="no">GOOGLE_APPLICATION_CREDENTIALS</var>to the file path of the JSON file that contains your service account key. This variable only applies to your current shell session, so if you open a new session, set the variable again.  

### Linux or macOS

    export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

### Windows

With PowerShell:  

    $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

After you've completed the above steps, Application Default Credentials (ADC) is able to implicitly determine your credentials, allowing you to use service account credentials when testing or running in non-Google environments.

Use your Firebase credentials together with the[Google Auth Library](https://github.com/googleapis?q=auth)for your preferred language to retrieve a short-lived OAuth 2.0 access token:  

### node.js

     function getAccessToken() {
      return admin.credential.applicationDefault().getAccessToken()
          .then(accessToken => {
            return accessToken.access_token;
          })
          .catch(err => {
            console.error('Unable to get access token');
            console.error(err);
          });
    }  
    https://github.com/firebase/quickstart-nodejs/blob/55f2ff5c17c730f7fc352f51a5264011de92fed0/config/index.js#L9-L18

In this example, the Google API client library authenticates the request with a JSON web token, or JWT. For more information, see[JSON web tokens](https://github.com/googleapis/google-auth-library-nodejs/blob/d8c70b9d858e1ef07cb8ef2b5d5d560ac2b2600a/README.md#json-web-tokens).

### Python

    def _get_access_token():
      """Retrieve a valid access token that can be used to authorize requests.

      :return: Access token.
      """
      credentials = ServiceAccountCredentials.from_json_keyfile_name(
          'service-account.json', SCOPES)
      access_token_info = credentials.get_access_token()
      return access_token_info.access_token  
    https://github.com/firebase/quickstart-python/blob/2c68e7c5020f4dbb072cca4da03dba389fbbe4ec/config/configure.py#L15-L23

### Java

    public static String getAccessToken() throws IOException {
      GoogleCredentials googleCredentials = GoogleCredentials
              .fromStream(new FileInputStream("service-account.json"))
              .createScoped(Arrays.asList(SCOPES));
      googleCredentials.refreshAccessToken();
      return googleCredentials.getAccessToken().getTokenValue();
    }  
    https://github.com/firebase/snippets-java/blob/7051da2745f8f95b176c9c6347e0bb0db3de1112/admin/src/main/java/com/google/firebase/example/FirebaseRemoteConfigSnippets.java#L178-L184

After your access token expires, the token refresh method is called automatically to retrieve an updated access token.

To authorize access toRemote Config, request the scope`https://www.googleapis.com/auth/firebase.remoteconfig`.

### Modify the Remote Config template

When working withRemote Configtemplates, keep in mind that they are versioned, and that each version has a limited lifetime from its time of creation to the time you replace it with an update: 90 days, with a total limit of 300 stored versions. See[Templates and Versioning](https://firebase.google.com/docs/remote-config/templates)for more information.

#### Get the current Remote Config Template

You can use the backend APIs to get the current active version of theRemote Configtemplate in JSON format.

Parameters and parameter values created specifically as variants in anA/B Testingexperiment are not included in exported templates.

Use the following commands:  

### cURL

```console
curl --compressed -D headers -H "Authorization: Bearer <var translate="no">token</var>" -X GET https://firebaseremoteconfig.googleapis.com/v1/projects/<var translate="no">my-project-id</var>/remoteConfig -o <var translate="no">filename</var>
```

This command outputs the JSON payload to one file, and the headers (including the Etag) to a separate file.

### Raw HTTP request

```actionscript-3
Host: firebaseremoteconfig.googleapis.com

GET /v1/projects/<var translate="no">my-project-id</var>/remoteConfig HTTP/1.1
Authorization: Bearer token
Accept-Encoding: gzip
```
| **Note:** Because this is a read request, the ETag is returned, but not modified, by this command.

This API call returns the following JSON, along with a separate header which includes an[ETag](https://firebase.google.com/docs/remote-config/automate-rc#etag_usage_and_forced_updates)that you use for the subsequent request.

#### Validate the Remote Config template

Optionally, you can validate your updates before publishing them. Validate template updates by appending to your publish request the URL parameter`?validate_only=true`. In the response, a status code 200 and an updated etag with the suffix`-0`means that your update was successfully validated. Any non-200 response indicates that the JSON data contains errors that you must correct before publishing.

#### Update the Remote Config template

Having retrieved a template and revised the JSON content with your desired updates, you can then publish it. Publishing a template as described in this section replaces the entire existing config template with the updated file, and the new active template is assigned a version number one number greater than the template it replaced.

If necessary, you can use the REST API to[roll back to the previous version](https://firebase.google.com/docs/remote-config/templates#roll_back_to_a_specific_stored_version_of_the_template). To mitigate the risk of errors in an update, you can[validate before publishing](https://firebase.google.com/docs/remote-config/automate-rc#validate_the_remote_config_template).

Remote Configpersonalizations and conditions are included in downloaded templates, so it's important to be aware of the following limitations when attempting to publish to a different project:

- Personalizations cannot be imported from project to project.

  For example, if you have personalizations enabled in your project and download and edit a template, you can publish it to the same project, but you can't publish it to a different project unless you delete the personalizations from the template.
- Conditions can be imported from project to project, but note that any specific conditional values (like app IDs or audiences), should exist in the target project before publishing.

  For example, if you have aRemote Configparameter that uses a condition that specifies a platform value of`iOS`, the template can be published to another project, because platform values are the same for any project. However, if it contains a condition that relies on a specific app ID or user audience that doesn't exist in the target project, validation will fail.
- If the template you plan to publish contains conditions that rely onGoogle Analytics,Analyticsmust be enabled in the target project.

### cURL

```console
curl --compressed -H "Content-Type: application/json; UTF8" -H "If-Match: <var translate="no">last-returned-etag</var>" -H "Authorization: Bearer <var translate="no">token</var>" -X PUT https://firebaseremoteconfig.googleapis.com/v1/projects/<var translate="no">my-project-id</var>/remoteConfig -d @<var translate="no">filename</var>
```

For this`curl`command, you can specify the content by using the "@" character, followed by the filename.

### Raw HTTP request

```actionscript-3
Host: firebaseremoteconfig.googleapis.com
PUT /v1/projects/<var translate="no">my-project-id</var>/remoteConfig HTTP/1.1
Content-Length: size
Content-Type: application/json; UTF8
Authorization: Bearer token
If-Match: expected ETag
Accept-Encoding: gzip
JSON_HERE
```

Because this is a write request, the[ETag](https://firebase.google.com/docs/remote-config/automate-rc#etag_usage_and_forced_updates)is modified by this command and an updated ETag is provided in the response headers of the next`PUT`command.

### Modify Remote Config conditions

You can programmatically modifyRemote Configconditions and conditional values. With the REST API, you must edit the template directly to modify conditions before publishing the template.  

```scdoc
{
  "conditions": [{
    "name": "android_english",
    "expression": "device.os == 'android' && device.country in ['us', 'uk']",
    "tagColor": "BLUE"
  }, {
    "name": "tenPercent",
    "expression": "percent <= 10",
    "tagColor": "BROWN"
  }],
  "parameters": {
    "welcome_message": {
      "defaultValue": {
        "value": "Welcome to this sample app"
      },
      "conditionalValues": {
        "tenPercent": {
          "value": "Welcome to this new sample app"
        }
      },
      "description": "The sample app's welcome message"
    },
    "welcome_message_caps": {
      "defaultValue": {
        "value": "false"
      },
      "conditionalValues": {
        "android_english": {
          "value": "true"
        }
      },
      "description": "Whether the welcome message should be displayed in all capital letters."
    }
  }
}
```

The modifications above first define a set of conditions, and then defines default values and condition-based parameter (*conditional values* ) values for each parameter. It also adds an optional description for each element; like code comments, these are for developer use and are not displayed in the app. An[ETag](https://firebase.google.com/docs/remote-config/automate-rc#etag_usage_and_forced_updates)is also provided for version control purposes.
| **Note:** Because every value is inherently a string forFirebase Remote Config, booleans are input as "true" and "false". They are correctly type casted as a boolean when using`getBoolean`methods. "True" or "False" or "1" or "0" are not correct representations of booleans forFirebase Remote Config.

TheRemote Configbackend APIs provide several conditions and comparison operators that you can use to change the behavior and appearance of your app. To learn more about conditions and the operators supported for these conditions, see the[conditional expression reference](https://firebase.google.com/docs/remote-config/condition-reference).

#### HTTP Error codes

| Status Code |                                                                                                                                                                                                                                                                                                                                      Meaning                                                                                                                                                                                                                                                                                                                                      |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200         | Successfully Updated                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 400         | A validation error occurred. For example, a request containing more than the allowed number of keys---2000---would return 400 (Bad Request) with the error message,`Param count too large`. Also, this HTTPS Status Code can occur in these two situations: - A version mismatch error occurred because the set of values and conditions have been updated since you last retrieved an ETag value. To resolve this, you should use a`GET`command to get a fresh template and ETag value, update the template, and then submit using that template and the fresh ETag value. - A`PUT`command (UpdateRemote Configtemplate request) was made without specifying an`If-Match`header. |
| 401         | An authorization error occurred (no access token was provided or the FirebaseRemote ConfigREST API has not been added to your project in the Cloud Developer Console)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 403         | An authentication error occurred (the wrong access token was provided)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 500         | An internal error occurred. If this error occurs,[file a Firebase support ticket](https://firebase.google.com/support/contact/troubleshooting/)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

A status code of 200 means that theRemote Configtemplate (parameters, values and conditions for the project) has been updated and is now available to apps that use this project. Other status codes indicate that theRemote Configtemplate that existed previously is still in effect.

After you submit updates to your template, go to theFirebaseconsole to verify that your changes appear as expected. This is critical because the ordering of conditions affects how they are evaluated (the first condition that evaluates`true`takes effect).

## ETag usage and forced updates

TheRemote ConfigREST API uses an entity tag (ETag) to prevent race conditions and overlapping updates to resources. To learn more about ETags, see[ETag - HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/ETag).

For the REST API, Google recommends that you cache the ETag provided by the most recent`GET`command, and use that ETag value in the`If-Match`request header when issuing`PUT`commands. If your`PUT`command results in an HTTPS Status Code 409, you should issue a fresh`GET`command to acquire a new ETag and template to use with your next`PUT`command.
| **Note:** We're aware of an issue in which the ETag is not properly returned in cases where the request does not specify a compression type. Currently, it is required to include the header`Accept-Encoding: gzip`or equivalent in all requests.

You can circumvent the ETag, and the protection from that it provides, by forcing theRemote Configtemplate to be updated as follows:`If-Match: *`However, this approach is not recommended because it risks causing the loss of updates to yourRemote Configtemplate if multiple clients are updating theRemote Configtemplate. This kind of conflict could occur with multiple clients using the API, or with conflicting updates from API clients andFirebaseconsole users.

For guidance on managingRemote Configtemplate versions, see[Remote Config templates and versioning](https://firebase.google.com/docs/remote-config/templates).