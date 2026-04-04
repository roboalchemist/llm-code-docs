# Source: https://firebase.google.com/docs/in-app-messaging/modify-message-behavior.md.txt

<br />

iOS+AndroidFlutter  

<br />

With little to no coding effort, Firebase In-App Messaging allows you to create, configure and target rich user interactions, leveraging the capabilities ofGoogle Analyticsout of the box to tie messaging events to actual user characteristics, activities, and choices. With some additionalFirebase In-App MessagingSDK integration, you can tailor the behavior of in-app messages even further, responding when users interact with messages, triggering message events outside theAnalyticsframework, and allowing users to control sharing of their personal data related to messaging interactions.

## Respond when users interact with in-app messages

With actions you can use your in-app messages to direct users to a website or a specific screen in your app.

Your code can respond to basic interactions (clicks and dismissals), to impressions (verified views of your messages), and to display errors logged and confirmed by the SDK. For example, when your message is composed as a Card modal, you might want to track and follow-up on which of two URLs the user clicked on the Card.

### Implement a DisplayDelegate to handle Card interactions

You can register an in-app messaging display delegate that will be called whenever there is any interaction with an in-app message. To do this, implement a class per the`InAppMessagingDisplayDelegate`protocol and set it as the delegate property on the`InAppMessaging`instance.

Assuming again that you want to track which link a user clicked on a Card-style message, define a class that implements the`messageClicked`method per the`DisplayDelegate`protocol, thereby providing you access to the link clicked by the user.  

### Swift

<br />

**Note:**This product is not available on macOS, Mac Catalyst, App Clip or watchOS targets.

Refer to the Swift[display delegate reference](https://firebase.google.com/docs/reference/swift/firebaseinappmessaging/api/reference/Protocols/InAppMessagingDisplayDelegate)for the set of callback methods that can be implemented and their parameters, including InAppMessagingAction.  


    // In CardActionFiamDelegate.swift
    class CardActionFiamDelegate : NSObject, InAppMessagingDisplayDelegate {

        func messageClicked(_ inAppMessage: InAppMessagingDisplayMessage) {
            // ...
        }

        func messageDismissed(_ inAppMessage: InAppMessagingDisplayMessage,
                              dismissType: InAppMessagingDismissType) {
            // ...
        }

        func impressionDetected(for inAppMessage: InAppMessagingDisplayMessage) {
            // ...
        }

        func displayError(for inAppMessage: InAppMessagingDisplayMessage, error: Error) {
            // ...
        }

    }  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/inappmessaging/FIAMReference/FIAMReferenceSwift/CardActionFiamDelegate.swift#L20-L39


    // In AppDelegate.swift
    // Register the delegate with the InAppMessaging instance
    let myFiamDelegate = CardActionFiamDelegate()
    InAppMessaging.inAppMessaging().delegate = myFiamDelegate;  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/inappmessaging/FIAMReference/FIAMReferenceSwift/AppDelegate.swift#L30-L32

### Objective-C

<br />

**Note:**This product is not available on macOS, Mac Catalyst, App Clip or watchOS targets.

Refer to the Objective-C[display delegate reference](https://firebase.google.com/docs/reference/ios/firebaseinappmessaging/api/reference/Protocols/FIRInAppMessagingDisplayDelegate)for the set of callback methods that can be implemented and their parameters, including FIRInAppMessagingDisplayMessage.  


    // In CardActionFiamDelegate.h
    @interface CardActionFiamDelegate : NSObject <FIRInAppMessagingDisplayDelegate>
    @end

    // In CardActionFiamDelegate.m
    @implementation CardActionFiamDelegate

    - (void)displayErrorForMessage:(nonnull FIRInAppMessagingDisplayMessage *)inAppMessage
                             error:(nonnull NSError *)error {
        // ...
    }

    - (void)impressionDetectedForMessage:(nonnull FIRInAppMessagingDisplayMessage *)inAppMessage {
        // ...
    }

    - (void)messageClicked:(nonnull FIRInAppMessagingDisplayMessage *)inAppMessage {
        // ...
    }

    - (void)messageDismissed:(nonnull FIRInAppMessagingDisplayMessage *)inAppMessage
                 dismissType:(FIRInAppMessagingDismissType)dismissType {
        // ...
    }

    @end  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/inappmessaging/FIAMReference/FIAMReference/CardActionFiamDelegate.m#L20-L40


    // In AppDelegate.m
    CardActionFiamDelegate *myFiamDelegate = [CardActionFiamDelegate new];
    [FIRInAppMessaging inAppMessaging].delegate = myFiamDelegate;  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/inappmessaging/FIAMReference/FIAMReference/AppDelegate.m#L35-L36

## Trigger in-app messages programmatically

Firebase In-App Messagingby default allows you to trigger in-app messages with Google Analytics for Firebase events, with no additional integration. You can also manually trigger events programmatically with theFirebase In-App MessagingSDK's programmatic triggers.

In the In-App Messaging campaign composer, create a new campaign or select an existing campaign, and in the Scheduling step of the composer workflow, note the event ID of a newly-created or existing messaging event. Once noted, instrument your app to trigger the event by its ID.  

### Swift

<br />

**Note:**This product is not available on macOS, Mac Catalyst, App Clip or watchOS targets.  

    ...
    // somewhere in the app's code
    InAppMessaging.inAppMessaging().triggerEvent("exampleTrigger");

### Objective-C

<br />

**Note:**This product is not available on macOS, Mac Catalyst, App Clip or watchOS targets.  

    ...
    // somewhere in the app's code
    [[FIRInAppMessaging inAppMessaging] triggerEvent:@"exampleTrigger"];

## Use campaign custom metadata

In your campaigns, you can specify custom data in a series of key/value pairs. When users interact with messages, this data is available for you to, for example, display a promo code.  

### Swift

<br />

**Note:**This product is not available on macOS, Mac Catalyst, App Clip or watchOS targets.  

    class CardActionDelegate : NSObject, InAppMessagingDisplayDelegate {

        func messageClicked(_ inAppMessage: InAppMessagingDisplayMessage) {
    	// Get data bundle from the inapp message
    	let appData = inAppMessage.appData
    	// ...
        }
    }  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/inappmessaging/FIAMReference/FIAMReferenceSwift/CardActionFiamDelegate.swift#L44-L51

### Objective-C

<br />

**Note:**This product is not available on macOS, Mac Catalyst, App Clip or watchOS targets.  

    @implementation ExampleCardActionDelegate

    - (void)messageClicked:(nonnull FIRInAppMessagingDisplayMessage *)inAppMessage {
        NSDictionary *appData = inAppMessage.appData;
        NSLog(@"Message data: %@", appData);
    	// ...
    }

    @end  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/inappmessaging/FIAMReference/FIAMReference/CardActionFiamDelegate.m#L48-L56

## Temporarily disable in-app messages

By default,Firebase In-App Messagingrenders messages whenever a triggering condition is satisfied, regardless of an app's current state. If you'd like to suppress message displays for any reason, for example to avoid interrupting a sequence of payment processing screens, use the SDK's`messageDisplaySuppressed`property as illustrated here in Objective-C:  

      [FIRInAppMessaging inAppMessaging].messageDisplaySuppressed = YES;  
    https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/inappmessaging/FIAMReference/FIAMReference/ViewController.m#L31-L31

Setting the property to`YES`preventsFirebase In-App Messagingfrom displaying messages, while`NO`reenables message display. The SDK resets the property to`NO`on app restart. Suppressed messages are ignored by the SDK. Their trigger conditions must be met again while suppression is off, beforeFirebase In-App Messagingcan display them.

## Enable opt-out message delivery

By default,Firebase In-App Messagingautomatically delivers messages to all app users you target in messaging campaigns. To deliver those messages, theFirebase In-App MessagingSDK usesFirebaseinstallation IDs to identify each user's app. This means thatIn-App Messaginghas to send client data, linked to the installation ID, to Firebase servers. If you'd like to give users more control over the data they send, disable automatic data collection and give them a chance to approve data sharing.

To do that, you have to disable automatic initialization forFirebase In-App Messaging, and initialize the service manually for opt-in users:

1. Turn off automatic initialization with a new key in your`Info.plist`file:

   - Key:`FirebaseInAppMessagingAutomaticDataCollectionEnabled`
   - Value:`NO`
2. InitializeFirebase In-App Messagingfor selected users manually:

       // Only needed if FirebaseInAppMessagingAutomaticDataCollectionEnabled is set to NO
       // in Info.plist
       [FIRInAppMessaging inAppMessaging].automaticDataCollectionEnabled = YES;  
       https://github.com/firebase/snippets-ios/blob/affc6b838d3dc3382ca741983dad489631d52b43/inappmessaging/FIAMReference/FIAMReference/ViewController.m#L37-L39

   Once you set`automaticDataCollectionEnabled`to`YES`, the value persists through app restarts, overriding the value in your`Info.plist`. If you'd like to disable initialization again, for example if a user opts out of collection later, set the property to`NO`.