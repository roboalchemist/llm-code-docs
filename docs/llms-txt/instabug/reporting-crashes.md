# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-crash-reporting/reporting-crashes.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-crash-reporting/reporting-crashes.md

# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-crash-reporting/reporting-crashes.md

# Reporting Crashes

### Manual Crash Reporting

You can use the following method and API to manually report any error or exception that you handle in your code and assign it a severity level.

You can now choose between two modes for the stack trace when reporting manual exceptions and errors: Full stack trace and Current thread only.

#### Full Stack Trace

The default mode for stack trace reporting is Full stack trace, which provides a complete stack trace for the error, including information about all threads. This mode is useful when you need to identify the exact cause of the error, as it provides a detailed view of the code execution flow.

#### Current Thread Only

The new mode for stack trace reporting is the Current thread only, which provides a stack trace for the current thread only. This mode is useful when you need to optimize the performance of their application, as it provides a lighter-weight option for reporting errors.

#### Report Exception

To report exceptions manually, use the following methods:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let exception = NSException(name: NSExceptionName("some_exception"), reason: "Exception reason")
if let nonFatalException = CrashReporting.exception(exception) {
	nonFatalException.stackTraceMode = .full
    nonFatalException.report()
    
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSException *exception = [NSException exceptionWithName:@"some_exception" reason:@"Exception reason" userInfo:nil];
LCQNonFatalException *nonFatalException = [LCQCrashReporting exception:exception];
nonFatalException.stackTraceMode = LCQNonFatalStackTraceModeFull;
[nonFatalException report];
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Report Error

To report errors manually, use the following methods:

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
if let nonFatal = CrashReporting.error(error) {
    nonFatal.stackTraceMode = .full
    nonFatal.report()
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSError *error = [[NSError alloc] initWithDomain:@"Domain" code:0 userInfo:nil];
LCQNonFatalError *nonFatal = [LCQCrashReporting error:error];
nonFatal.stackTraceMode = LCQNonFatalStackTraceModeFull;
[nonFatal report];
```

{% endcode %}
{% endtab %}
{% endtabs %}

#### Adding Levels to Exception & Errors

You can set different levels for manually reported exceptions using the following API:

**Exceptions**

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let exception = NSException(name: NSExceptionName("some_exception"), reason: "Exception reason")
if let nonFatalException = CrashReporting.exception(exception) {
    nonFatalException.userAttributes = [
      "hello" : "world"
    ]
    nonFatalException.groupingString = "com.service.method.some_exception"
    nonFatalException.level = .critical
    nonFatalException.report()
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSException *exception = [NSException exceptionWithName:@"some_exception" reason:@"Exception reason" userInfo:nil];
LCQNonFatalException *nonFatalException = [LCQCrashReporting exception:exception];
nonFatalException.userAttributes = @{
    @"hello" : @"world"
};
nonFatalException.groupingString = @"com.service.method.some_exception";
nonFatalException.level = LCQNonFatalLevelWarning;
[nonFatalException report];
```

{% endcode %}
{% endtab %}
{% endtabs %}

**Errors**

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
let domain = "com.service.method"
let code = 0
let error = NSError(domain: domain, code: code, userInfo: nil)
if let nonfatal = CrashReporting.error(error) {
    // Set the level here
    nonfatal.level = .critical
    nonfatal.report()
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSError* error = [[NSError alloc] initWithDomain:@"Domain" code:0 userInfo:nil];
LCQNonFatalError* nonFatalError = [LCQCrashReporting error:error];
// Set the level here
nonFatalError.level = LCQNonFatalLevelCritical;
[nonFatalError report];
```

{% endcode %}
{% endtab %}
{% endtabs %}

**Severity Levels**

Here are the different severity levels available for exceptions and errors. In case no level is indicated, the default level would be error.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
warning
error
critical
info
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQNonFatalLevelWarning
LCQNonFatalLevelError
LCQNonFatalLevelCritical
LCQNonFatalLevelInfo
```

{% endcode %}
{% endtab %}
{% endtabs %}

{% hint style="info" %}

#### Performance Improvement

On average, it takes 5ms less to capture a stack trace while using `CallerThread`.
{% endhint %}

### Modifying Stacktraces for Handled Errors

If you use a wrapper function to send handled errors, you can trim the wrapper function from the event’s stack trace. This will help you in having a more readable stacktrace.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
if let nonFatal = CrashReporting.error(error) {
    nonFatal.stackFramesToTrim = 2
    nonFatal.report()
}
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
NSError *error = [[NSError alloc] initWithDomain:@"Domain" code:0 userInfo:nil];
LCQNonFatalError *nonFatal = [LCQCrashReporting error:error];
nonFatal.stackFramesToTrim = 2;
[nonFatal report];
```

{% endcode %}
{% endtab %}
{% endtabs %}

### Grouping

When an already existing crash occurs once more for any user, that crash is reported as an occurrence in the original entry. However, in order to calculate whether a crash already exists and needs to be grouped, Luciq generates a fingerprint based on attributes used in the grouping logic.

The default Luciq grouping algorithm uses a mix of the exception and stack trace information. In some cases, you might want to change how the issues are grouped together using custom grouping or fingerprints.

#### Crash-to-Screen Assignment Logic

When a crash occurs during a screen transition, Luciq assigns the crash to a specific screen based on the timing of the `viewDidAppear` and `viewDidDisappear` lifecycle events. The crash will be attributed to the screen name that was last set by the SDK before the crash occurred.

#### Custom Grouping

{% hint style="warning" %}

#### Required dSYM Files

Please note that in order for custom grouping to be applied, dSYM files are required to be uploaded first; otherwise, default grouping will be applied. For more information on uploading dSYM files, please visit the [symbolication page](https://docs.luciq.ai/ios/setup-luciq-for-ios/setup-crash-reporting/symbolication).
{% endhint %}

One way to customize how crashes are grouped together is by providing Luciq with packages that you would like us to ignore from our default grouping logic. If you define a package to be ignored, Luciq will skip the frame with that package and move on to find the next one that is not on your ignored list. This is done on an application level by going to your **Application → Settings → Custom Crash Grouping**.

**Expected Input:**

* Path
* Binary Image

Paths will be evaluated on a **starts with** basis, while Binary Images will be evaluated on an **equality** basis.

#### Examples:

* Path = `Luciq`\
  \-- Ignores = `Luciq`, `Luciq/CrashReporting`, `Luciq/APM`
* Path = `Luciq/APM`\
  \-- Ignores = `Luciq/APM`, `Luciq/APM/AppLaunch`\
  \-- Doesn't Ignore = `Luciq`, `Luciq/CrashReporting`
* Binary Image = `BinaryImage`\
  \-- Ignores = `BinaryImage`\
  \-- Doesn't Ignore = `BinaryImage2`, `Binaryimage`

*Sample Stack Trace:*

{% code overflow="wrap" %}

```undefined
libobic.A.dylib    foreach_realized_class(bool (objc_class*) block_pointer) + 123

CoreFoundation.    -__NSSingleObjectArraylenumerateObjectsWithOptions:usingBlock:] + 11

ThirdParty         -[LoggerManager LogArray:] + 80

Myapp              - ViewController tableView:didSelectRowAtindexPath:
UIKitCore          -[UIKBUndoStateHUD initWithKeyboardAppearance:] + 4171
Myapp              _main
```

{% endcode %}

* **Without** custom grouping, Luciq would group the crash based on `ThirdParty -[LoggerManager LogArray:] + 80` since it's the first non-system frame
* **With** custom grouping while ignoring **path** `home/files/ThirdParty/` and **binary image** `ThirdParty`, we will skip the first frame `ThirdParty -[LoggerManager LogArray:] + 80`, and the crash will be grouped based on `Myapp - ViewController tableView:didSelectRowAtindexPath:`.

### Custom Fingerprinting

{% hint style="warning" %}

#### Overriding the default grouping

Please note that using custom fingerprinting will override Luciq's default grouping by sending a fingerprint string.
{% endhint %}

In the event that you'd like to report the exception manually with a custom grouping fingerprint in mind, you can use the below APIs to do just that.

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
CrashReporting.reportError(error, withGroupingString: "grouping string")
CrashReporting.report(exception, withGroupingString: "grouping string")
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
[LCQCrashReporting reportException:exception groupingString:@"grouping string"];
[LCQCrashReporting reportError:error groupingString:@"grouping string"];
```

{% endcode %}
{% endtab %}
{% endtabs %}
