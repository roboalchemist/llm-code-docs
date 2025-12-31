# Source: https://firebase.google.com/docs/perf-mon/attributes.md.txt

<br />

iOS+AndroidWeb  

<br />

WithPerformance Monitoring, you can use attributes to segment performance data and focus on your app's performance in different real-world scenarios.

After you click a trace name in the traces table (located at the bottom of the[*Performance*dashboard](https://console.firebase.google.com/project/_/performance)), you can drill down into metrics of interest. Use the**Filteradd**button (top-left of the screen) to filter the data by attribute, for example:

![an image of <span class=](https://firebase.google.com/static/docs/perf-mon/images/perf-mon-filter-by-attribute_native-1.png)Firebase Performance Monitoringdata being filtered by attribute" /\>

- Filter by*App version*to view data about a past release or your latest release
- Filter by*Device*to learn how older devices handle your app
- Filter by*Country*to make sure your database location isn't affecting a specific region

For even more powerful analysis based on attributes,[export your performance data to BigQuery](https://firebase.google.com/docs/perf-mon/bigquery-export).

## Default attributes

Performance Monitoringautomatically collects a variety of default attributes depending on the type of trace.

In addition to these default attributes, you can also[create custom attributes](https://firebase.google.com/docs/perf-mon/attributes#create-custom-attributes)on your[custom code traces](https://firebase.google.com/docs/perf-mon/custom-code-traces)to segment data by categories specific to your app. For example, in a game, you can segment data by game level.

### Default attributes for Apple and Android apps

All traces for Apple and Android apps collect the following attributes by default:

- App version
- Country
- OS level
- Device
- Radio
- Carrier

In addition, network request traces also collect the following attribute:

- MIME type

## Collecting user data

| **Collecting user data:** Performance Monitoringdoes not itself collect any personally identifiable information (PII), such as names, email addresses, or phone numbers. Developers can collect additional data usingPerformance Monitoringby creating custom attributes on custom code traces. Such data collected throughPerformance Monitoringshould not contain information that personally identifies an individual to Google.
|
| Here's an example of a log message that*does not*contain personally identifiable information:  
|
| ```java
| trace.putAttribute("experiment", "A");
| ```
|
| Here's an example that*does* contain personally identifiable information (***do not use***this type of custom attribute in your app):  
|
| ```java
| trace.putAttribute("email", user.getEmailAddress());
| ```
|
| Data that exposes any personally identifiable information is subject to deletion without notice.

## Create custom attributes

You can create custom attributes on any of your instrumented[custom code traces](https://firebase.google.com/docs/perf-mon/custom-code-traces).

Use thePerformance MonitoringTrace API ([Swift](https://firebase.google.com/docs/reference/swift/firebaseperformance/api/reference/Classes/Trace)\|[Obj-C](https://firebase.google.com/docs/reference/ios/firebaseperformance/api/reference/Classes/FIRTrace)) to add custom attributes to custom code traces.

To use custom attributes, add code to your app that defines the attribute and associates it with a specific custom code trace. You can set the custom attribute anytime between when the trace starts and when the trace stops.

Note the following:

- Names for custom attributes must meet the following requirements:

  - No leading or trailing whitespace, no leading underscore (`_`) character
  - No spaces
  - Max length is 32 characters
  - Allowed characters for the name are`A-Z`,`a-z`, and`_`.
- Each custom code trace can record up to 5 custom attributes.

- Please ensure that custom attributes do not contain any information that personally identifies an individual to Google.

  Learn more about this guideline
  | **Collecting user data:** Performance Monitoringdoes not itself collect any personally identifiable information (PII), such as names, email addresses, or phone numbers. Developers can collect additional data usingPerformance Monitoringby creating custom attributes on custom code traces. Such data collected throughPerformance Monitoringshould not contain information that personally identifies an individual to Google.
  |
  | Here's an example of a log message that*does not*contain personally identifiable information:  
  |
  | ```java
  | trace.putAttribute("experiment", "A");
  | ```
  |
  | Here's an example that*does* contain personally identifiable information (***do not use***this type of custom attribute in your app):  
  |
  | ```java
  | trace.putAttribute("email", user.getEmailAddress());
  | ```
  |
  | Data that exposes any personally identifiable information is subject to deletion without notice.

### Swift

<br />

**Note:**This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.  

```swift
let trace = Performance.startTrace(name: "<var class="readonly" translate="no">CUSTOM_TRACE_NAME</var>")

trace.setValue("A", forAttribute: "experiment")

// Update scenario.
trace.setValue("B", forAttribute: "experiment")

// Reading scenario.
let experimentValue:String? = trace.valueForAttribute("experiment")

// Delete scenario.
trace.removeAttribute("experiment")

// Read attributes.
let attributes:[String, String] = trace.attributes;
```

### Objective-C

<br />

**Note:**This Firebase product is not available on macOS, Mac Catalyst, watchOS targets.  

```objective-c
FIRTrace *trace = [FIRPerformance startTraceWithName:@"<var class="readonly" translate="no">CUSTOM_TRACE_NAME</var>"];

[trace setValue:@"A" forAttribute:@"experiment"];

// Update scenario.
[trace setValue:@"B" forAttribute:@"experiment"];

// Reading scenario.
NSString *experimentValue = [trace valueForAttribute:@"experiment"];

// Delete scenario.
[trace removeAttribute:@"experiment"];

// Read attributes.
NSDictionary <NSString *, NSString *> *attributes = [trace attributes];
```