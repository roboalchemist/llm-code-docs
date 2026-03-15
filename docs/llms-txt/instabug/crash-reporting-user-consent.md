# Source: https://docs.instabug.com/ios/setup-luciq-for-ios/setup-crash-reporting/crash-reporting-user-consent.md

# Crash Reporting User Consent

Suppose you want your users' confirmation before sending a crash report to Luciq. In that case, the Luciq SDK exposes a callback awaiting each user's confirmation before sending any crash/error data to Luciq.

This callback function instructs Luciq to await user confirmation before sending crash reports. It is designed to enhance end-user privacy and control by allowing them to approve or decline the submission of crash reports, ensuring a more transparent and user-centric experience.

This callback applies to fatal errors (crashes) and out-of-memory (OOM) reports, force restarts, and excludes app hangs and non-fatal errors.

If no response is received within a 2-minute window, the callback triggers a timeout mechanism, preventing the automatic crash report sending.

**Example Usage**

{% tabs %}
{% tab title="Swift" %}
{% code overflow="wrap" %}

```swift
 CrashReporting.onWillSendCrashReportHandler = { crashType, completionHandler in

            let crashTypeAsString: String

            switch (crashType) {

            case .crash:

                    crashTypeAsString = "Fatal Crash"

            case .forceRestart:

                    crashTypeAsString = "User termination Crash"

            case .OOM:

                    crashTypeAsString = "OOM Crash"

            @unknown default:

                fatalError()

            }

            let message = "Are You Sure Want to send Crash! for crash type: \(crashTypeAsString)"

            let alert = UIAlertController(title: "Crash Consent", message: message, preferredStyle: .alert)

            let yesButton = UIAlertAction(title: "Yes", style: .default, handler: { _ in

                completionHandler?(.accept);

            })

            alert.addAction(yesButton)

            let noButton = UIAlertAction(title: "No", style: .default, handler: { _ in

                completionHandler?(.reject);

            })

            alert.addAction(noButton)

            let rootViewController = UIApplication.shared.keyWindow?.rootViewController

            rootViewController?.present(alert, animated: true)

        }
```

{% endcode %}
{% endtab %}

{% tab title="Objective-C" %}
{% code overflow="wrap" %}

```objectivec
LCQCrashReporting.onWillSendCrashReportHandler = ^(LCQCrashType crashType, LCQCrashReportConsentReplyHandler completionHandler) {

        NSString *crashTypeAsString;

        switch (crashType) {

            case LCQCrashTypeCrash:

                crashTypeAsString = @"Fatal Crash";

                break;

            case LCQCrashTypeForceRestart:

                crashTypeAsString = @"User termination Crash";

                break;

            case LCQCrashTypeOOM:

                crashTypeAsString = @"OOM Crash";

                break;

        }

        NSString *message = [NSString stringWithFormat:@"Are You Sure Want to send Crash! for crash type: %@", crashTypeAsString];

        UIAlertController * alert = [UIAlertController

                                     alertControllerWithTitle:@"Crash Consent"

                                     message:message

                                     preferredStyle:UIAlertControllerStyleAlert];

        UIAlertAction* yesButton = [UIAlertAction

                                    actionWithTitle:@"Yes"

                                    style:UIAlertActionStyleDefault

                                    handler:^(UIAlertAction * action) {

            completionHandler(LCQCrashReportConsentAccept);

        }];

        [alert addAction:yesButton];

        UIAlertAction* noButton = [UIAlertAction

                                   actionWithTitle:@"No"

                                   style:UIAlertActionStyleDefault

                                   handler:^(UIAlertAction * action) {

            completionHandler(LCQCrashReportConsentReject);

        }];

        [alert addAction:noButton];

        UIViewController *rootViewController = [UIApplication.sharedApplication.keyWindow rootViewController];

        [rootViewController presentViewController:alert animated:YES completion:nil];

    };
```

{% endcode %}
{% endtab %}
{% endtabs %}
