# Source: https://docs.logrocket.com/docs/conditional-recording.md

# Conditional Recording

Available as a separate add on for Pro and Enterprise customers

Many of our clients capture hundreds of millions of monthly sessions, making it difficult to store all sessions without significant infrastructure cost. LogRocket solves this problem by allowing customers to control which sessions to keep for troubleshooting and analysis.

<Image align="center" border={true} src="https://files.readme.io/a3a1cbc-conditional_recording_lr_site.png" className="border" />

Ideas for leveraging our filters to control the sessions you capture:

### 1. Capture clicks

Capture sessions where a user clicks on your 'checkout' button, 'add to cart' button, Support tools, and more.

### 2. Capture page(s) visited

Control session capture based on visited url, such as "record 20% of users who visit our checkout page".

### 3. Capture based on session duration

Capture sessions that are greater than a specified duration.

It is also possible to capture only sessions with user activity after a specified duration with "Active Time In Session" filter.

### 4. Capture network failures

Capture sessions that include errors, to better understand the root cause of these issues as well as the user's experience. Use the Network Request filter to capture:

* Network errors
* Specific request and response bodies
* Slow network requests, using the 'duration' field

### 5. Capture error messages or visible elements

Capture sessions where a specific element is visible, such as Element Visible with text contains "Oops! Sorry an error occurred".

### 6. Capture log messages

Capture sessions with certain log messages. This can be filtered based on text in the log message, or the log level.

### 7. Capture custom events

Capture sessions based on a specific custom event you set in your code. See documentation on custom events here for [web](https://docs.logrocket.com/reference/track), [native android](https://docs.logrocket.com/reference/android-custom-events), [native iOS](https://docs.logrocket.com/reference/ios-custom-events), and [react native](https://docs.logrocket.com/reference/react-native-custom-events).

### 8. Capture platforms

Capture sessions from specific platforms, including web, iOS, or Android.

## Lookback Length

All recordings record up to 10MB of activity prior to the recording condition being met. For example, if you have a rule to see "Visited URL contains /checkout", the duration of the session you'll see prior to the user visiting the checkout URL will vary based on the amount and type of session events that occurred before the rule was triggered. Exact durations will vary significantly case by case, but in general we have seen this translate to several minutes or more of lookback.

## Adding Multiple Conditions

LogRocket allows you to set multiple conditions, so you can capture sessions flexibly to meet your needs. to use this, click to create a new Recording Condition from the Conditional Recording settings page, and set the sampling rate. These rules will be considered separately, not cumulatively, so a session needs to meet only one condition in order to be recorded.

<Image align="center" border={false} width="400px" src="https://files.readme.io/29ac3106a6026c36616c58277dc90a59cc396cddd897f64b44ab9f93476a7478-Screenshot_2024-11-08_at_12.01.45_PM.png" />

## Adding Multiple Rules to Single Condition

You can also set multiple rules in a single condition - this means a session must contain all events in order to be recorded. To use this, select "Add Filter" within a Conditional Recording rule details page.

Please note that recording will begin shortly before the last condition to be fulfilled is met. At this time, rules can be fulfilled in any order.  Note that for mobile sessions, rules with multiple filters are only supported for SDK versions 1.42.0 and up.

<Image align="center" border={false} width="1000px" src="https://files.readme.io/f432bbc25263d59b3064d94ebfa7df98a394b2c617ab82cb8d979755802a316c-Screenshot_2024-11-08_at_12.18.01_PM.png" />

<br />

***

If you have any questions about this functionality, please reach out to your Customer Success Manager or [support@logrocket.com](mailto:support@logrocket.com).