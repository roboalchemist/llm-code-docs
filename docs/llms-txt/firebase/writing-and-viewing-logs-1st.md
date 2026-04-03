# Source: https://firebase.google.com/docs/functions/1st-gen/writing-and-viewing-logs-1st.md.txt

<br />

| **Note:** The 1st-gen functionality described in this page is also supported inCloud Functions(2nd gen) with improved features and performance. For more information about 2nd gen, see the[version comparison](https://firebase.google.com/docs/functions/version-comparison). To go directly to the 2nd gen guide for this feature, see[Write and view logs](https://firebase.google.com/docs/functions/writing-and-viewing-logs).

Logging is an important tool for debugging and monitoring code.Cloud Functionsgives you the option of using its logger SDK, custom GoogleCloud Logging, or the`console`object standard for developing for the web.

## Writing logs

While theCloud Functions[logger](https://firebase.google.com/docs/reference/functions/firebase-functions.logger)SDK is recommended for most situations, you might choose one of the other options for these reasons:

- You have an existing code base and prefer not to refactor from`console.log`.
- You're familiar withCloud Logging(formerly StackDriver logging) and prefer to use it for custom logging.

### Using theCloud Functionslogger SDK

TheCloud Functionslogger SDK provides a standard interface that has a similar api to`console.log`statements and supports other log levels. You can use this SDK to log events with[structured data](https://cloud.google.com/logging/docs/structured-logging), enabling easier analysis and monitoring.

The logger SDK supports log entries as part of a wildcard import. For example:  

      const functions = require("firebase-functions/v1");

      functions.logger.log("Hello from info. Here's an object:", someObj);

Alternatively, you can use individual exports. This example demonstrates structured data attached to the log as the last argument:  

    const { warn } = require("firebase-functions/logger");


    // Attach structured data to the log as the last argument.
    warn("This is a 'WARNING' severity message with some metadata.", {
      key1: 'val1',
      key2: 'val2'
    });

- `logger.log()`commands have the**INFO**log level.
- `logger.info()`commands have the**INFO**log level.
- `logger.warn()`commands have the**WARNING**log level.
- `logger.error()`commands have the**ERROR**log level.
- Internal system messages have the**DEBUG**log level.

With`logger.write()`, you can write log entries addition log severity levels of`CRITICAL`,`ALERT`, and`EMERGENCY`. See[LogSeverity](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity).

### CustomCloud Logginglogs

Cloud Functionslogs with the logger SDK are backed by[Cloud Logging](https://cloud.google.com/logging/). You can use the[Cloud Logginglibrary for Node.js](https://github.com/googleapis/nodejs-logging#readme)to log events with structured data, enabling easier analysis and monitoring.  

    const { Logging } = require('@google-cloud/logging');

    // ...

    // Instantiate the logging SDK. The project ID will
    // be automatically inferred from the Cloud Functions environment.
    const logging = new Logging();
    const log = logging.log('my-custom-log-name');

    // This metadata is attached to each log entry. This specifies a fake
    // Cloud Function called 'Custom Metrics' in order to make your custom
    // log entries appear in the Cloud Functions logs viewer.
    const METADATA = {
      resource: {
        type: 'cloud_function',
        labels: {
          function_name: 'CustomMetrics',
          region: 'us-central1'
        }
      }
    };

    // ...

    // Data to write to the log. This can be a JSON object with any properties
    // of the event you want to record.
    const data = {
      event: 'my-event',
      value: 'foo-bar-baz',

      // Optional 'message' property will show up in the Firebase
      // console and other human-readable logging surfaces
      message: 'my-event: foo-bar-baz'
    };

    // Write to the log. The log.write() call returns a Promise if you want to
    // make sure that the log was written successfully.
    const entry = log.entry(METADATA, data);
    log.write(entry);  
    https://github.com/firebase/snippets-node/blob/4738eab0d52a393e4e3027e7a6992fd6c892faf2/functions/stackdriver-logging/index.js#L35-L49

| **Note:** Cloud Loggingis a chargeable service; you may be billed if you exceed the no-cost quota. For more information, see[Cloud Loggingpricing](https://cloud.google.com/stackdriver/pricing).

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