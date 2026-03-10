# Source: https://docs.aws.amazon.com/agentworkspace/latest/devguide/llms.txt

# Agent Workspace Developer guide

- [Document history](https://docs.aws.amazon.com/agentworkspace/latest/devguide/doc-history.html)

## [What is the Amazon Connect agent workspace?](https://docs.aws.amazon.com/agentworkspace/latest/devguide/what-is-service.html)

- [Are you a first-time Amazon Connect agent workspace user?](https://docs.aws.amazon.com/agentworkspace/latest/devguide/first-time-user.html): If you are a first-time user of Amazon Connect agent workspace, we recommend that you begin by reading the following sections:
- [How applications are loaded in the agent workspace](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrating-with-agent-workspace-how-apps-load.html): How applications are loaded in the agent workspace.
- [Recommendations and best practices](https://docs.aws.amazon.com/agentworkspace/latest/devguide/recommendations-and-best-practices.html): Recommendations and best practices.


## [Working with 3P apps](https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started.html)

### [Prerequisites for 3P apps](https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-prerequisites.html)

Prerequisites to get started with third-party development in the agent workspace.

- [IAM role required](https://docs.aws.amazon.com/agentworkspace/latest/devguide/appendix-role-required.html): On top of the AmazonConnect_FullAccess IAM policy, users need the following IAM permissions for creating an app and associating it with an Amazon Connect instance.

### [Create your application](https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-create-application.html)

Create your third-party application in the agent workspace.

- [Install the Amazon Connect SDK](https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-install-sdk.html): Installing the Amazon Connect SDK.

### [Using Connect SDK without package manager](https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager.html)

Learn how to use the Amazon Connect SDK without npm, webpack, or other JavaScript package managers and bundlers.

- [Building the script file](https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager-building.html): Step-by-step instructions for creating a browser-consumable bundle from the SDK npm packages.
- [Using with StreamsJS](https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager-streamsjs.html): How to use the prebuilt bundle in a solution that uses Amazon Connect Streams.
- [Using in 3P app](https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager-3p-app.html): How to use the prebuilt bundle in a third-party application that runs within the Amazon Connect Agent Workspace.
- [Updating the bundle](https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager-updating.html): How to update the bundle when a new version of the SDK is released.
- [Troubleshooting](https://docs.aws.amazon.com/agentworkspace/latest/devguide/sdk-without-package-manager-troubleshooting.html): Common issues and resolutions when using the SDK without a package manager.
- [Initialize the Amazon Connect SDK in your application](https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-initialize-sdk.html): Initialize the Amazon Connect SDK in your application.
- [Events and requests](https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-events-and-requests.html): App developers can easily create applications that seamlessly integrate into the agent workspace experience with the event and request functionality natively supported by the Amazon Connect SDK.
- [Application authentication](https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-authentication.html): Apps in the Amazon Connect agent workspace must provide their own authentication to their users.
- [Integrate with agent data](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-with-agent-data.html): Integrate with agent data.
- [Integrate with contact data](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-with-contact-data.html): Integrate with contact data.

### [Lifecycle events](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrating-with-agent-workspace-lifecycle-events.html)

Lifecycle events.

- [Create event](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrating-with-agent-workspace-lifecycle-events-create.html): The create event in the Amazon Connect agent workspace results in the onCreate handler passed into the AmazonConnectApp.init() to be invoked.
- [Destroy event](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrating-with-agent-workspace-lifecycle-events-destroy.html): The destroy event in the Amazon Connect agent workspace will trigger the onDestroy callback configured during AmazonConnectApp.init().
- [Apply a theme](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrating-with-agent-workspace-theme.html): Apply a theme.
- [Test your application locally](https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-testing.html): Once you have a minimal version of the app that you want to use in the Amazon Connect agent workspace with the Amazon Connect SDK that you want to test in the agent workspace, run your app locally and create an application in the AWS console with an AccessUrl using the localhost endpoint, like http://localhost:3000 .
- [Test with a deployed version of your application](https://docs.aws.amazon.com/agentworkspace/latest/devguide/getting-started-test-with-deployed-app.html): Test with a deployed version of your application.
- [Error handling](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrating-with-agent-workspace-error-handling.html): Error handling.
- [Troubleshooting](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrating-with-agent-workspace-troubleshooting.html): Troubleshooting.


## [Building 3P services](https://docs.aws.amazon.com/agentworkspace/latest/devguide/building-3P-services.html)

- [Agent workspace startup process](https://docs.aws.amazon.com/agentworkspace/latest/devguide/building-3P-services-startup-process.html): Understanding the startup process for third-party services in the agent workspace.
- [Create a service](https://docs.aws.amazon.com/agentworkspace/latest/devguide/building-3P-services-creating.html): Learn how to create and set up a third-party service.
- [Implementation patterns](https://docs.aws.amazon.com/agentworkspace/latest/devguide/building-3P-services-implementation-patterns.html): Explore various implementation patterns for third-party services.
- [Best practices](https://docs.aws.amazon.com/agentworkspace/latest/devguide/building-3P-services-best-practices.html): Best practices and recommendations for building third-party services.


## [Integrating AWS-managed apps](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-aws-managed-apps-streams.html)

- [Implementation guide](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-aws-managed-apps-implementation.html): Implementation steps for integrating AWS-managed applications using Streams and AppManager.
- [Retrieve available applications](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-aws-managed-apps-catalog.html): Retrieve applications available to the authenticated user.
- [Application lifecycle management](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-aws-managed-apps-lifecycle.html): Managing application lifecycle throughout the page's life.
- [Advanced configuration](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-aws-managed-apps-advanced.html): Advanced configuration options for AWS-managed applications.
- [Dynamic application management](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-aws-managed-apps-react-example.html): Example implementation of dynamic application management with React.
- [Troubleshooting](https://docs.aws.amazon.com/agentworkspace/latest/devguide/integrate-aws-managed-apps-troubleshooting.html): Common issues and resolutions when integrating AWS-managed applications.


## [Connect SDK API reference](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-events-and-requests.html)

### [Activity](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-activity-client.html)

The Amazon Connect SDK provides a SessionExpirationWarningClient which serves as an interface that your app in the Amazon Connect agent workspace can use to subscribe to events related to session expiration due to inactivity and to signal the Amazon Connect that the agent is active.

- [onExpirationWarning()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-offexpirationwarning.html): Unsubscribes a callback function from the expiration warning event that is triggered when the agent is nearing expiration due to inactivity.
- [offExpirationWarningCleared()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-offexpirationwarningcleared.html): Unsubscribes a callback function from the expiration warning cleared event that is triggered when the expiration warning is dismissed due to the agent choosing to stay logged in.
- [offSessionExtensionError()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-offsessionextensionerror.html): Unsubscribes a callback function from the session extension error event that is triggered when the agent's session fails to update.
- [onExpirationWarning()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-onexpirationwarning.html): Subscribes a callback function to be invoked whenever the agent's session is about to expire due to inactivity.
- [onExpirationWarningCleared()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-onexpirationwarningcleared.html): Subscribes a callback function to be invoked when the agent has acknowledged the expiration warning and chooses to update their session.
- [onSessionExtensionError()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-onsessionextensionerror.html): Subscribes a callback function to be invoked when an attempt to extend the agent's session fails.
- [sendActivity()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-activity-sendactivity.html): Sends a signal to the Amazon Connect indicating that the agent is active and should not be logged out.

### [Agent](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-agent-client.html)

Third-party application agent APIs.

- [getARN()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getarn.html): Returns the Amazon Resource Name(ARN) of the user that's currently logged in to the Amazon Connect agent workspace.
- [getChannelConcurrency()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getchannelconcurrency.html): Returns a map of ChannelType-to-number indicating how many concurrent contacts can an Amazon Connect agent workspace agent have on a given channel. 0 represents a disabled channel.
- [getExtension()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getextension.html): Returns phone number of the agent currently logged in to the Amazon Connect agent workspace.
- [getName()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getname.html): Returns the name of the user that's currently logged in to the Amazon Connect agent workspace.
- [getRoutingProfile()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getroutingprofile.html): Returns the routing profile of the agent currently logged in to the Amazon Connect agent workspace.
- [getState()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-getstate.html): Returns the Amazon Connect agent workspace agent's current AgentState object indicating their availability state type.
- [listAvailabilityStates()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-listavailabilitystates.html): Get all the availability states configured for the current agent.
- [listQuickConnects()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-listquickconnects.html): Get the list of Quick Connect endpoints associated with the given queue(s).
- [offEnabledChannelListChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-off-enabledchannellistchanged.html): Unsubscribes from EnabledChannelListChanged event.
- [offRoutingProfileChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-off-routingprofilechanged.html): Unsubscribes from RoutingProfileChanged event.
- [onEnabledChannelListChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-on-enabledchannellistchanged.html): Creates a subscription for EnabledChannelListChanged event.
- [onRoutingProfileChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-on-routingprofile-changed.html): Creates a subscription for RoutingProfileChanged event.
- [setAvailabilityState()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-setavailabilitystate.html): Set the agent state with the given agent state ARN
- [setAvailabilityStateByName()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-setavailabilitystatebyname.html): Set the agent state with the given agent state name.
- [setOffline()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-requests-setoffline.html): Sets the agent state to Offline.
- [onStateChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-events-statechanged-sub.html): Subscribes a callback function to-be-invoked whenever an agent state changed event occurs in the Amazon Connect agent workspace.
- [offStateChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-agent-events-statechanged-unsub.html): Unsubscribes the callback function from the agent stated change event in the Amazon Connect agent workspace.

### [AppController](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller.html)

Third-party application controller APIs.

- [closeApp()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller-closeapp.html): Closes the application for the given application instance ID in the Amazon Connect agent workspace.
- [focusApp()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller-focusapp.html): Brings the application into focus in the Amazon Connect agent workspace for the given application instance ID.
- [getApp()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller-getapp.html): Returns the application information for the given application instance ID in the Amazon Connect agent workspace.
- [getAppCatalog()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller-getappcatalog.html): Returns all the applications that are available in the Amazon Connect agent workspace for the current logged-in user.
- [getAppConfig()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller-getappconfig.html): Returns the application configuration for the given application ARN in the Amazon Connect agent workspace.
- [getApps()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller-getapps.html): Returns the application information for all active application instances in the Amazon Connect agent workspace.
- [launchApp()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-app-controller-launchapp.html): Launch the application in the agent workspace for the given application ARN or name.

### [Contact](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-contact-client.html)

Third-party application contact APIs.

- [accept()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-accept.html): Accept the incoming contact for the given contactId.
- [addParticipant()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-addparticipant.html): Add another participant to the contact.
- [clear()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-clear.html): Clears the contact for the given contactId.
- [onCleared()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-clearedsubscribing.html): Creates a subscription whenever a contact cleared event occurs in Amazon Connect agent workspace
- [offCleared()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-clearedunsubscribing.html): Unsubscribes the callback function from the contact cleared event in the Amazon Connect agent workspace.
- [onConnected()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-connected-sub.html): Subscribes a callback function to-be-invoked whenever a contact Connected event occurs in the Amazon Connect agent workspace.
- [offConnected()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-connected-unsub.html): Unsubscribes the callback function from Connected event in the Amazon Connect agent workspace.
- [disconnectParticipant()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-disconnectparticipant.html): Disconnects a specific participant from the contact.
- [engagePreviewContact()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-engagepreviewcontact.html): Initiate the outbound dial for a preview contact being previewed by an agent.
- [getAttribute()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getattribute.html): Returns the requested attribute associated with the contact in the Amazon Connect agent workspace.
- [getAttributes()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getattributes.html): Returns a map of the attributes associated with the contact in the Amazon Connect Agent Workspace.
- [getChannelType()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getchanneltype.html): Get the type of the contact
- [getContact()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getcontact.html): Retrieves detailed information for a specific contact by its ID.
- [getInitialContactId()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getinitialcontactid.html): Returns the original (initial) contact id from which this contact was transferred in the Amazon Connect agent workspace, or none if this is not an internal Connect transfer.
- [getParticipant()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getparticipant.html): Retrieves information for a specific participant.
- [getParticipantState()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getparticipantstate.html): Retrieves the current state of a specific participant.
- [getPreviewConfiguration()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getpreviewconfiguration.html): Get configuration information related to the preview experience.
- [getQueue()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getqueue.html): Returns the queue associated with the contact in the Amazon Connect agent workspace.
- [getQueueTimestamp()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getqueuetimestamp.html): Returns a Date object with the timestamp associated with when the contact was placed in the queue in the Amazon Connect agent workspace.
- [getStateDuration()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-getstateduration.html): Returns the duration of the contact state in milliseconds relative to local time, in the Amazon Connect agent workspace.
- [isPreviewMode()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-ispreviewmode.html): Returns whether the contact is being previewed.
- [listContacts()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-listcontacts.html): Lists all contacts for the current agent.
- [listParticipants()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-listparticipants.html): Retrieves all participants associated with a specific contact.
- [onMissed()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-missed-sub.html): Subscribes a callback function to-be-invoked whenever a contact missed event occurs in the Amazon Connect agent workspace.
- [offMissed()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-missed-unsub.html): Unsubscribes the callback function from the contact missed event.
- [offIncoming()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-off-incoming.html): Unsubscribes the callback function from the contact incoming event in the Amazon Connect agent workspace.
- [onIncoming()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-on-incoming.html): Creates a subscription whenever a new incoming event occurs in Amazon Connect agent workspace.
- [onParticipantAdded()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-participantadded-sub.html): Subscribes to participant added events.
- [offParticipantAdded()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-participantadded-unsub.html): Unsubscribes from participant added events.
- [onParticipantDisconnected()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-participantdisconnected-sub.html): Subscribes to participant disconnected events.
- [offParticipantDisconnected()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-participantdisconnected-unsub.html): Unsubscribes from participant disconnected events.
- [onParticipantStateChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-participantstatechanged-sub.html): Subscribes to participant state change events.
- [onStartingAcw()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-startingacw-sub.html): Subscribes a callback function to-be-invoked whenever a contact StartingAcw event occurs in the Amazon Connect agent workspace.
- [offStartingAcw()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-events-startingacw-unsub.html): Unsubscribes the callback function from the contact StartingAcw event in the Amazon Connect agent workspace.
- [transfer()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-contact-requests-transfer.html): Transfer the given contact to another agent using a quick connect and disconnect from the contact.

### [Email](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-email-client.html)

Third-party application email APIs.

- [onAcceptedEmail()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-acceptedemail-subscribing.html): Subscribe a callback function when an inbound email contact has been accepted.
- [offAcceptedEmail()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-acceptedemail-unsubscribing.html): Unsubscribe a callback function when an inbound email contact has been accepted.
- [createDraftEmail()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-createdraftemail.html): Creates a draft outbound email contact; can either be an agent initiated outbound draft email or an agent reply draft email.
- [onDraftEmailCreated()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-draftemailcreated-subscribing.html): Subscribe a callback function when a draft email contact has been created.
- [offDraftEmailCreated()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-draftemailcreated-unsubscribing.html): Unsubscribe a callback function when a draft email contact has been created.
- [getEmailData()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-getemaildata.html): Get the metadata for an email contact while handling an active email contact.
- [getEmailThread()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-getemailthread.html): Returns an array of EmailThreadContact objects that represent that contact's email thread.
- [sendEmail()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-email-requests-sendemail.html): Sends both agent initiated and agent reply draft email contacts.

### [File](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-file-client.html)

Third-party application file APIs.

- [batchGetAttachedFileMetadata()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-file-requests-batchgetattachedfilemetadata.html): Get metadata about multiple attached files on an associated resource while handling an active contact.
- [completeAttachedFileUpload()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-file-requests-completeattachedfileupload.html): Allows you to confirm that the attachment has been uploaded using the pre-signed URL provided in the startAttachedFileUpload API.
- [deleteAttachedFile()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-file-requests-deleteattachedfile.html): Deletes an attached file along with the underlying S3 Object.
- [getAttachedFileUrl()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-file-requests-getattachedfileurl.html): Returns a pre-signed URL to download an approved attached file while handling an active contact.
- [startAttachedFileUpload()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-file-requests-startattachedfileupload.html): Provides a pre-signed Amazon S3 URL in response to upload a new attached file.

### [MessageTemplate](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-message-template-client.html)

Third-party application message template APIs.

- [getContent()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-message-template-requests-getcontent.html): Gets the content of a message template.
- [isEnabled()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-message-template-requests-isenabled.html): Determine if the Message Template feature is enabled for the Connect instance.
- [searchMessageTemplates()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-message-template-requests-searchmessagetemplates.html): Returns the SearchMessageTemplatesResponse object, which contains the matching message templates and a token to retrieve the next page of results.

### [QuickResponses](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-quick-responses-client.html)

Third-party application quick responses APIs.

- [isEnabled()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-quick-responses-requests-isenabled.html): Determine if the Quick Responses feature is enabled for the Connect instance.
- [searchQuickResponses()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-quick-responses-requests-searchquickresponses.html): Returns the SearchQuickResponsesResult object, which contains the matching quick response results and a token to retrieve the next page of results.

### [User](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-user.html)

Third-party application user APIs.

- [getLanguage()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-user-requests-getlanguage.html): Returns the language setting for the current user in the Amazon Connect Agent Workspace.
- [onLanguageChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-user-events-languagechanged-sub.html): Subscribes a callback function to-be-invoked whenever a user LanguageChanged event occurs in the Amazon Connect Agent Workspace.
- [offLanguageChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-user-events-languagechanged-unsub.html): Unsubscribes the callback function from LanguageChanged event in the Amazon Connect Agent Workspace.

### [Voice](https://docs.aws.amazon.com/agentworkspace/latest/devguide/api-reference-3P-apps-voice-client.html)

Third-party application voice APIs.

- [canResumeParticipant()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-canresumeparticipant.html): Checks whether a specific participant can be resumed from hold.
- [canResumeSelf()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-canresumeself.html): Checks whether the current user's participant can be resumed from hold for a specific contact.
- [conferenceParticipants()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-conferenceparticipants.html): Conferences all participants on a contact together, removing any hold states and enabling all participants to communicate with each other.
- [createOutboundCall()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-createoutboundcall.html): Creates an outbound call to the given phone number and returns the contactId if resolveBeforeConfirmation is set to false.
- [getInitialCustomerPhoneNumber()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-getinitialcustomerphonenumber.html): Gets the phone number of the initial customer connection.
- [getOutboundCallPermission()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-getoutboundcallpermission.html): Gets true if the agent has the security profile permission for making outbound calls, false otherwise.
- [holdParticipant()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-holdparticipant.html): Places a specific participant on hold.
- [getVoiceEnhancementMode()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-getvoiceenhancementmode.html): Gets the voice enhancement mode of the user that's currently logged in to the Amazon Connect agent workspace.
- [getVoiceEnhancementPaths()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-getvoiceenhancementpaths.html): Returns the voice enhancements models static assets URL paths.
- [isParticipantOnHold()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-isparticipantonhold.html): Checks whether a specific participant is currently on hold.
- [listDialableCountries()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-listdialablecountries.html): Get a list of dialable countries
- [offCanResumeParticipantChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-offcanresumeparticipantchanged.html): Unsubscribes from participant capability change events.
- [offCanResumeSelfChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-offcanresumeselfchanged.html): Unsubscribes from capability change events for the current user.
- [offParticipantHold()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-offparticipanthold.html): Unsubscribes from participant hold events.
- [offParticipantResume()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-offparticipantresume.html): Unsubscribes from participant resume events.
- [offSelfHold()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-offselfhold.html): Unsubscribes from self hold events.
- [offSelfResume()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-offselfresume.html): Unsubscribes from self resume events.
- [offVoiceEnhancementModeChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-offvoiceenhancementmodechanged.html): Unsubscribes a callback function registered for voice enhancements mode changed event.
- [onCanResumeParticipantChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-oncanresumeparticipantchanged.html): Subscribes to events when a participant's capability to be resumed from hold changes.
- [onCanResumeSelfChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-oncanresumeselfchanged.html): Subscribes to events when the current user's capability to be resumed from hold changes.
- [onParticipantHold()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-onparticipanthold.html): Subscribes to events when any participant is put on hold.
- [onParticipantResume()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-onparticipantresume.html): Subscribes to events when any participant is taken off hold.
- [onSelfHold()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-onselfhold.html): Subscribes to events when the current user's participant is put on hold.
- [onSelfResume()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-onselfresume.html): Subscribes to events when the current user's participant is taken off hold.
- [onVoiceEnhancementModeChanged()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-onvoiceenhancementmodechanged.html): Subscribes a callback function whenever voice enhancements mode is changed in user's profile.
- [resumeParticipant()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-resumeparticipant.html): Resumes a specific participant from hold.
- [setVoiceEnhancementMode()](https://docs.aws.amazon.com/agentworkspace/latest/devguide/3P-apps-voice-requests-setvoiceenhancementmode.html): Sets the voice enhancement mode of the user that's currently logged in to the Amazon Connect agent workspace.
