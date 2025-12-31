# Source: https://firebase.google.com/docs/functions/rc-events.md.txt

<br />

You can trigger a function in response to[Firebase Remote Config](https://firebase.google.com/docs/remote-config)events, including the publication of a new config version or the rollback to an older version. This guide describes how to create aRemote Configbackground function that performs a diff of two template versions.

## Trigger aRemote Configfunction

To trigger aRemote Configfunction, first import the required modules:  

### Node.js

     // The Cloud Functions for Firebase SDK to set up triggers and logging.
    const {onConfigUpdated} = require("firebase-functions/remoteConfig");
    const logger = require("firebase-functions/logger");
    // The Firebase Admin SDK to obtain access tokens.
    const admin = require("firebase-admin");
    const app = admin.initializeApp();
    const jsonDiff = require("json-diff");  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/remote-config-diff/functions/index.js#L20-L26

### Python

     # The Cloud Functions for Firebase SDK to set up triggers and logging.
    from firebase_functions import remote_config_fn

    # The Firebase Admin SDK to obtain access tokens.
    import firebase_admin

    app = firebase_admin.initialize_app()

    import deepdiff
    import requests  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/remote-config-diff/functions/main.py#L17-L26

Then define a handler for the update event. The event object passed to this function contains metadata about a template update, such as the new version number and time of the update. You can also retrieve the email for the user who made the update, with name and an image if available.

Here's an example of aRemote Configfunction that logs a diff of each updated version and the version it replaced. The function examines the version number field of the template object and retrieves the current (newly updated) version together with the version one number lower:  

### Node.js

     exports.showconfigdiff = onConfigUpdated(async (event) => {
      try {
        // Obtain the access token from the Admin SDK
        const accessTokenObj = await admin.credential.applicationDefault()
            .getAccessToken();
        const accessToken = accessTokenObj.access_token;

        // Get the version number from the event object
        const remoteConfigApi = "https://firebaseremoteconfig.googleapis.com/v1/" +
            `projects/${app.options.projectId}/remoteConfig`;
        const currentVersion = event.data.versionNumber;
        const prevVersion = currentVersion - 1;
        const templatePromises = [];
        templatePromises.push(fetch(
            remoteConfigApi,
            {
              method: "POST",
              body: new URLSearchParams([["versionNumber", currentVersion + ""]]),
              headers: {Authorization: "Bearer " + accessToken},
            },
        ));
        templatePromises.push(fetch(
            remoteConfigApi,
            {
              method: "POST",
              body: new URLSearchParams([["versionNumber", prevVersion + ""]]),
              headers: {Authorization: "Bearer " + accessToken},
            },
        ));

        // Get the templates
        const responses = await Promise.all(templatePromises);
        const results = responses.map((r) => r.json());
        const currentTemplate = results[0];
        const previousTemplate = results[1];
        // Figure out the differences of the templates
        const diff = jsonDiff.diffString(previousTemplate, currentTemplate);
        // Log the difference
        logger.log(diff);
      } catch (error) {
        logger.error(error);
      }
    });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/remote-config-diff/functions/index.js#L30-L72

This sample uses the[`json-diff`](https://www.npmjs.com/package/json-diff)and[`request-promise`](https://www.npmjs.com/package/request-promise)modules to create the diff and build the request to get the template object.

### Python

     @remote_config_fn.on_config_updated()
    def showconfigdiff(event: remote_config_fn.CloudEvent[remote_config_fn.ConfigUpdateData]) -> None:
        """Log the diff of the most recent Remote Config template change."""

        # Obtain an access token from the Admin SDK
        access_token = app.credential.get_access_token().access_token

        # Get the version number from the event object
        current_version = int(event.data.version_number)

        # Figure out the differences between templates
        remote_config_api = ("https://firebaseremoteconfig.googleapis.com/v1/"
                             f"projects/{app.project_id}/remoteConfig")
        current_template = requests.get(remote_config_api,
                                        params={"versionNumber": current_version},
                                        headers={"Authorization": f"Bearer {access_token}"})
        previous_template = requests.get(remote_config_api,
                                         params={"versionNumber": current_version - 1},
                                         headers={"Authorization": f"Bearer {access_token}"})
        diff = deepdiff.DeepDiff(previous_template, current_template)

        # Log the difference
        print(diff.pretty())  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/remote-config-diff/functions/main.py#L31-L53

This sample uses[`deepdiff`](https://pypi.org/project/deepdiff/)to create the diff, and`requests`to build and send the request to get the template object.