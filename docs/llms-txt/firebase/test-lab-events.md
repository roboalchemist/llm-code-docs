# Source: https://firebase.google.com/docs/functions/test-lab-events.md.txt

<br />

## Import the required modules

To get started, import the modules required for handlingFirebase Test Labevents:  

### Node.js

     // The Cloud Functions for Firebase SDK to set up triggers and logging.
    const {onTestMatrixCompleted} = require("firebase-functions/testLab");
    const {logger} = require("firebase-functions");  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/testlab-matrix-completed/functions/index.js#L20-L22

### Python

     # The Cloud Functions for Firebase SDK to set up triggers and logging.
    from firebase_functions import test_lab_fn, params

    # The requests library to send web requests to Slack.
    import requests  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/testlab-to-slack/functions/main.py#L17-L21

## Trigger a function on TestMatrix completion

To trigger aFirebase Test Labfunction, define a handler for the test matrix completion event. In this example, the function triggers on test completion, retrieves the test matrix data from the CloudEvent object, and sends the corresponding test results to a Slack channel:  

### Node.js

    exports.posttestresultstoslack = onTestMatrixCompleted(
        {secrets: ["SLACK_WEBHOOK_URL"]},
        async (event) => {
        // Obtain Test Matrix properties from the CloudEvent
          const {testMatrixId, state, outcomeSummary} = event.data;

          // Create the title of the message
          const title = `${getSlackmoji(state)} ${getSlackmoji(
              outcomeSummary,
          )} ${testMatrixId}`;

          // Create the details of the message
          const details = `Status: *${state}* ${getSlackmoji(
              state,
          )}\nOutcome: *${outcomeSummary}* ${getSlackmoji(outcomeSummary)}
        `;

          // Post the message to slack
          const slackResponse = await postToSlack(title, details);

          // Log the response
          logger.log(slackResponse);
        });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/testlab-to-slack/functions/index.js#L95-L117

### Python

    @test_lab_fn.on_test_matrix_completed(secrets=["SLACK_WEBHOOK_URL"])
    def posttestresultstoslack(
            event: test_lab_fn.CloudEvent[test_lab_fn.TestMatrixCompletedData]) -> None:
        """Posts a test matrix result to Slack."""

        # Obtain Test Matrix properties from the CloudEvent
        test_matrix_id = event.data.test_matrix_id
        state = event.data.state
        outcome_summary = event.data.outcome_summary

        # Create the title of the message
        title = f"{slackmoji(state)} {slackmoji(outcome_summary)} {test_matrix_id}"

        # Create the details of the message
        details = (f"Status: *{state}* {slackmoji(state)}\n"
                   f"Outcome: *{outcome_summary}* {slackmoji(outcome_summary)}")

        # Post the message to Slack
        response = post_to_slack(title, details)

        # Log the response
        print(response.status_code, response.text)  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/testlab-to-slack/functions/main.py#L70-L91

## Access client details

Test matrices may be created from different sources or workflows. It is therefore often desirable to create functions that perform different actions based on the source or other important context of the test. To help with this,`gcloud`allows you to pass arbitrary information when starting a test that can be accessed later in your function. For example:  

    gcloud beta firebase test android run \
        --app=path/to/app.apk \
        --client-details testType=pr,link=<path/to/pull-request>

And then to access the information in your function:  

### Node.js

    const testType = event.data.clientInfo.details.testType;
    const link = event.data.clientInfo.details.link;

### Python

    test_type: str | None = event.data.client_info.details.get("testType")
    link: str | None = event.data.client_info.details.get("link")