# Source: https://firebase.google.com/docs/functions/1st-gen/rc-events-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Remote Configtriggers](https://firebase.google.com/docs/functions/rc-events).

You can trigger a function in response to[Firebase Remote Config](https://firebase.google.com/docs/remote-config)events, including the publication of a new config version or the rollback to an older version. This guide describes how to create aRemote Configbackground function that performs a diff of two template versions.

## Trigger a Remote Config function

To define a handler forRemote Configevents, use the[`functions.remoteConfig`](https://firebase.google.com/docs/reference/functions/firebase-functions.remoteconfig)module's`onUpdate()`function. The`TemplateVersion`object returned by`onUpdate`contains the key metadata fields for a template update such as the version number and time of the update. You can also retrieve the email for the user who made the update, with name and an image if available.

Here's an example of aRemote Configfunction that returns a diff of each updated version and the version it replaced. The function examines the`versionNumber`field of the template object and retrieves the current (newly updated) version together with the version one number lower:  

```gdscript
exports.showConfigDiff = functions.remoteConfig.onUpdate(versionMetadata => {
  return admin.credential.applicationDefault().getAccessToken()
    .then(accessTokenObj => {
      return accessTokenObj.access_token;
    })
    .then(accessToken => {
      const currentVersion = versionMetadata.versionNumber;
      const templatePromises = [];
      templatePromises.push(getTemplate(currentVersion, accessToken));
      templatePromises.push(getTemplate(currentVersion - 1, accessToken));

      return Promise.all(templatePromises);
    })
    .then(results => {
      const currentTemplate = results[0];
      const previousTemplate = results[1];

      const diff = jsonDiff.diffString(previousTemplate, currentTemplate);

      functions.logger.log(diff);

      return null;
    }).catch(error => {
      functions.logger.error(error);
      return null;
    });
});https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node-1st-gen/remote-config-diff/functions/index.js#L24-L50
```

This sample uses the[`json-diff`](https://www.npmjs.com/package/json-diff)and[`request-promise`](https://www.npmjs.com/package/request-promise)modules to create the diff and build the request to get the template object. For a sample that incorporatesRemote Configclient logic as well asFirebase Cloud Messaging, see[Propagate Remote Config updates in real time](https://firebase.google.com/docs/remote-config/propagate-updates-realtime).