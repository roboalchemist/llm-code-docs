# Source: https://firebase.google.com/docs/functions/writing-and-viewing-logs.md.txt

<br />

Logging is an important tool for debugging and monitoring code.Cloud Functionsgives you the option of using the logger SDK for[Node.js](https://firebase.google.com/docs/reference/functions/2nd-gen/node/firebase-functions.logger)or[Python](https://firebase.google.com/docs/reference/functions/2nd-gen/python/firebase_functions.logger), or the`console`object standard for developing for the web.

Cloud Logging is a chargeable service; you may be billed if you exceed the no-cost quota. For more information, see[Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing).

## Writing logs

### Using theCloud Functionslogger SDK

TheCloud Functionslogger SDK provides a standard interface to report status from functions to Cloud Logging. You can use this SDK to log events with[structured data](https://cloud.google.com/logging/docs/structured-logging), enabling easier analysis and monitoring.

Import from the`logger`subpackage:  

### Node.js

    // All available logging functions
    const {
      log,
      info,
      debug,
      warn,
      error,
      write,
    } = require("firebase-functions/logger");  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/monitor-cloud-logging/functions/index.js#L23-L31

### Python

    from firebase_functions import logger  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/monitor-cloud-logging/functions/main.py#L8-L8

- `logger.log()`commands have the**INFO**log level.

- `logger.info()`commands have the**INFO**log level.

- `logger.warn()`commands have the**WARNING**log level.

- `logger.error()`commands have the**ERROR**log level.

- `logger.debug()`commands have the**DEBUG**log level.

- Internal system messages have the**DEBUG**log level.

This example demonstrates a function writing a basic log:  

### Node.js

    exports.helloWorld = onRequest((request, response) => {
      // sends a log to Cloud Logging
      log("Hello logs!");

      response.send("Hello from Firebase!");
    });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/monitor-cloud-logging/functions/index.js#L40-L45

### Python

    @https_fn.on_request()
    def hello_world(req: https_fn.Request) -> https_fn.Response:
        # sends a log to Cloud Logging
        logger.log("Hello logs!")

        return https_fn.Response("Hello from Firebase!")  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/monitor-cloud-logging/functions/main.py#L15-L20

Use different log levels for different types of log in your function code. Structured data can be attached to a log as the last argument. Here is an example of how a function can use each log type:  

### Node.js

    exports.getInspirationalQuote = onRequest(async (request, response) => {
      const db = getFirestore();
      const today = new Date();
      const quoteOfTheMonthRef = db
          .collection("quotes")
          .doc(`${today.getFullYear()}`)
          .collection("months")
          .doc(`${today.getMonth()}`);

      const DEFAULT_QUOTE =
          "You miss 100% of the shots you don't take. -Wayne Gretzky";
      let quote;
      try {
        const quoteOfTheMonthDocSnap = await quoteOfTheMonthRef.get();

        // Attach relevant debugging information with debug()
        debug("Monthly quote fetch result", {
          docRef: quoteOfTheMonthRef.path,
          exists: quoteOfTheMonthDocSnap.exists,
          createTime: quoteOfTheMonthDocSnap.createTime,
        });

        if (quoteOfTheMonthDocSnap.exists) {
          quote = quoteOfTheMonthDocSnap.data().text;
        } else {
          // Use warn() for lower-severity issues than error()
          warn("Quote not found for month, sending default instead", {
            docRef: quoteOfTheMonthRef.path,
            dateRequested: today.toLocaleDateString("en-US"),
          });

          quote = DEFAULT_QUOTE;
        }
      } catch (err) {
        // Attach an error object as the second argument
        error("Unable to read quote from Firestore, sending default instead",
            err);

        quote = DEFAULT_QUOTE;
      }

      // Attach relevant structured data to any log
      info("Sending a quote!", {quote: quote});
      response.json({inspirationalQuote: quote});
    });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/monitor-cloud-logging/functions/index.js#L49-L95

### Python

    @https_fn.on_request()
    def get_inspirational_quote(req: https_fn.Request) -> https_fn.Response:
        firestore_client = firestore.client()
        today = datetime.date.today()
        quote_of_the_month_ref = (firestore_client.collection("quotes").doc(str(
            today.year)).collection("months").doc(str(today.month)))

        default_quote = "Python has been an important part of Google since the beginning, and remains so as the system grows and evolves."

        quote = None
        try:
            quote_of_the_month = quote_of_the_month_ref.get()

            # Attach relevant debugging information with debug()
            logger.debug(
                "Monthly quote fetch result",
                docRef=quote_of_the_month.path,
                exists=quote_of_the_month.exists,
                createTime=quote_of_the_month.createTime,
            )

            if quote_of_the_month.exists:
                quote = quote_of_the_month.to_dict()["text"]
            else:
                # Use warn() for lower-severity issues than error()
                logger.warn(
                    "Quote not found for month, sending default instead",
                    doc_reference=quote_of_the_month.path,
                    date_requested=today.strftime("%Y-%m-%d"),
                )
                quote = default_quote
        except:
            e = sys.exc_info()[0]
            # Attach an error object as the second argument
            logger.error("Unable to read quote from Firestore, sending default instead", error=e)
            quote = default_quote

        # Attach relevant structured data to any log
        logger.info("Sending a quote!", quote=quote)
        return https_fn.Response("Hello from Firebase!")  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/monitor-cloud-logging/functions/main.py#L25-L66

With`logger.write()`, you can write log entries with additional log severity levels of`CRITICAL`,`ALERT`, and`EMERGENCY`. See[LogSeverity](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity).  

### Node.js

    exports.appHasARegression = onRegressionAlertPublished((event) => {
      write({
        // write() lets you set additional severity levels
        // beyond the built-in logger functions
        severity: "EMERGENCY",
        message: "Regression in production app",
        issue: event.data.payload.issue,
        lastOccurred: event.data.payload.resolveTime,
      });
    });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/quickstarts/monitor-cloud-logging/functions/index.js#L99-L108

### Python

    @crashlytics_fn.on_regression_alert_published()
    def app_has_regression(alert: crashlytics_fn.CrashlyticsRegressionAlertEvent) -> None:
        logger.write(
            severity="EMERGENCY",
            message="Regression in production app",
            issue=alert.data.payload.issue,
            last_occurred=alert.data.payload.resolve_time,
        )
        print(alert)  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/quickstarts/monitor-cloud-logging/functions/main.py#L71-L79

### Using`console.log`

The recommended solution for logging from a function is to use the logger SDK for your platform. With Node.js, you can instead use standard JavaScript logging calls such as`console.log`and`console.error`, but you first need to require a special module to patch the standard methods to work correctly:  

    require("firebase-functions/logger/compat");

Once you have required the logger compatibility module, you can use`console.log()`methods as normal in your code:  

    exports.helloError = functions.https.onRequest((request, response) => {
      console.log('I am a log entry!');
      response.send('Hello World...');
    });  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/functions/stackdriver-logging/index.js#L7-L10

- `console.log()`commands have the**INFO**log level.
- `console.info()`commands have the**INFO**log level.
- `console.warn()`commands have the**ERROR**log level.
- `console.error()`commands have the**ERROR**log level.
- Internal system messages have the**DEBUG**log level.

## Viewing logs

Logs forCloud Functionsare viewable either in the[Google Cloudconsole](https://console.cloud.google.com/functions/list),Cloud LoggingUI, or via the`firebase`command-line tool.

### Using the Firebase CLI

To view logs with the`firebase`tool, use the`functions:log`command:  

    firebase functions:log

To view logs for a specific function, provide the function name as an argument:  

    firebase functions:log --only <FUNCTION_NAME>

For the full range of log viewing options, view the help for`functions:log`:  

    firebase help functions:log

### Using theGoogle Cloudconsole

You can view logs for functions in the[Google Cloudconsole](https://console.cloud.google.com/functions/list).

### Using theCloud LoggingUI

You can[view logs forCloud Functions](https://console.cloud.google.com/project/_/logs?service=cloudfunctions.googleapis.com&&advancedFilter=resource.type%3D%22cloud_function%22%0A)in theCloud LoggingUI.

## Analyzing logs

Cloud Loggingoffers a powerful suite of logs analysis tools that you can use to monitor yourCloud Functions.

### Charts and alerts

Once you have created logs-based metrics to monitor your functions, you can create charts and alerts based on these metrics. For example, you could create a chart to visualize latency over time, or create an alert to let you know if a certain error occurs too often.

See[Creating Charts and Alerts](https://cloud.google.com/logging/docs/logs-based-metrics/charts-and-alerts)for detailed information on how to use logs-based metrics in charts and alerting policies.

## Understand and use execution IDs

By default, Cloud Run functions (2nd gen) supports concurrent execution of multiple requests within a single function instance. This means logs from different requests can be interleaved, making it harder to follow the flow of a single execution.

To help with this, functions deployed using Firebase CLI version 13.33.0 and later automatically deploy with an option to associate an execution ID with each log entry emitted during handling of that execution.

The execution ID uniquely identifies all logs associated with a single request handled by your function. No code changes are required; the execution ID will be automatically added to your logs.

To disable logging execution ID in your log entries, set the[environment variable](https://firebase.google.com/docs/functions/config-env?gen=2nd#env-variables)`LOG_EXECUTION_ID`to false in your dotenv file.

### Find and correlate logs by execution ID

You can inspect and correlate logs by execution ID in Cloud Logs Explorer.

1. Expand the log entry from your function. The execution ID is located within the structured log data, nested under labels as`labels.execution_id`.

2. Click the value of the`execution_id`and select "Show matching entries" from the drop-down menu to see all other logs associated with that same function execution.

By using the execution ID, you can group together all log messages related to a single request, even if your function is handling multiple requests concurrently.

### Enhance log visibility with custom summary fields

To make the execution ID more readily visible in the Logs Explorer, you can add it as a \[custom summary field\]\[cloud-logging-preference\]. After you add execution ID as a summary field, every log entry will show execution ID as a chip at the beginning of the log line. similar to the way 1st Gen functions surfaced execution ID for all log entries.

To add execution ID to summary field:

1. Click the value of the execution ID in the structured log entry under`labels.execution_id`.

2. Select "Add field to summary line" from the drop-down menu.

Each log entry now displays the`executionId`prominently in the summary field, making it easier to identify and group logs associated with a specific execution ID.