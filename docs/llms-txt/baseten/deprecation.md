# Source: https://docs.baseten.co/development/model-apis/deprecation.md

# Deprecation

> Overview of Baseten’s deprecation policy for Model APIs.

## Deprecation Process

As open source models advance rapidly, we prioritize serving the highest quality models and deprecate specific Model APIs when stronger alternatives are available. When a model is selected for deprecation we follow the below process:

1. **Announcement**
   * Deprecations are announced \~2 weeks prior to the deprecation date
   * Updated documentation identifying the model to be deprecated along with a recommended replacement
   * Affected users will be contacted via email
2. **Transition**
   * The deprecating model will remain fully functional until the final deprecation date. Following the initial deprecation announcement users have \~2 weeks to transition. There are two options:
     1. Migrate to a dedicated deployment with the deprecated model weights [contact us](https://www.baseten.co/talk-to-us/deprecation-inquiry/)
     2. Shift the Model API model ID to an active model (we provide a recommendation in the deprecation announcement)
3. **Deprecation date**
   * The model ID for the deprecated model will become inactive and return an error for all requests
   * Changelog notification of deprecation with a recommended replacement

## Planned Deprecations

There are no planned deprecations at this time.
