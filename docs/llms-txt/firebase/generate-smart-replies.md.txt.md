# Source: https://firebase.google.com/docs/ml-kit/ios/generate-smart-replies.md.txt

> [!CAUTION]
> This page describes an old version of the Smart Reply API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Generate smart replies with ML Kit on iOS](https://developers.google.com/ml-kit/language/smart-reply/ios)
> for the latest documentation.


You can use ML Kit to generate message replies using an on-device
model.

To generate smart replies, you pass ML Kit a log of recent messages in a
conversation. If ML Kit determines the conversation is in English, and that
the conversation doesn't have potentially sensitive subject matter, ML Kit
generates up to three replies, which you can suggest to your user.

<br />

## Before you begin

1. If you have not already added Firebase to your app, do so by following the steps in the [getting started guide](https://firebase.google.com/docs/ios/setup).
2. Include the ML Kit libraries in your Podfile:

   ```
   pod 'Firebase/MLCommon', '6.25.0'
   pod 'Firebase/MLNLSmartReply', '6.25.0'
   ```
   After you install or update your project's Pods, be sure to open your Xcode project using its `.xcworkspace`.
3. In your app, import Firebase:

   #### Swift

   ```swift
   import Firebase
   ```

   #### Objective-C

   ```objective-c
   @import Firebase;
   ```

## 1. Create a conversation history object

To generate smart replies, you pass ML Kit a chronologically-ordered array of
`TextMessage` objects, with the earliest timestamp first. Whenever the user
sends or receives a message, add the message, its timestamp, and the message
sender's user ID to the conversation history.

The user ID can be any string that uniquely identifies the sender within the
conversation. The user ID doesn't need to correspond to any user data,
and the user ID doesn't need to be consistent between conversations or
invocations of the smart reply generator.

If the message was sent by the user you want to suggest replies to, set
`isLocalUser` to true.

### Swift

    var conversation: [TextMessage] = []

    // Then, for each message sent and received:
    let message = TextMessage(
        text: "How are you?",
        timestamp: Date().timeIntervalSince1970,
        userID: "userId",
        isLocalUser: false)
    conversation.append(message)

### Objective-C

    NSMutableArray *conversation = [NSMutableArray array];

    // Then, for each message sent and received:
    FIRTextMessage *message = [[FIRTextMessage alloc]
            initWithText:@"How are you?"
            timestamp:[NSDate date].timeIntervalSince1970
            userID:userId
            isLocalUser:NO];
    [conversation addObject:message];

A conversation history object looks like the following example:

| Timestamp | User ID | Local User? | Message |
|---|---|---|---|
| Thu Feb 21 13:13:39 PST 2019 |   | true | are you on your way? |
| Thu Feb 21 13:15:03 PST 2019 | FRIEND0 | false | Running late, sorry! |

Note that the most recent message in the example above is from a non-local
user. This is important because ML Kit suggests replies intended to be sent
by the user of your app: the local user. You should be sure you're passing
ML Kit a conversation log that ends with a message to which your user might
want to reply.

## 2. Get message replies

To generate smart replies to a message, get an instance of `SmartReply` and pass
the conversation history to its `suggestReplies(for:completion:)` method:

### Swift

    let naturalLanguage = NaturalLanguage.naturalLanguage()
    naturalLanguage.smartReply().suggestReplies(for: conversation) { result, error in
        guard error == nil, let result = result else {
            return
        }
        if (result.status == .notSupportedLanguage) {
            // The conversation's language isn't supported, so the
            // the result doesn't contain any suggestions.
        } else if (result.status == .success) {
            // Successfully suggested smart replies.
            // ...
        }
    }

### Objective-C

    FIRNaturalLanguage *naturalLanguage = [FIRNaturalLanguage naturalLanguage];
    FIRSmartReply *smartReply = [naturalLanguage smartReply];
    [smartReply suggestRepliesForMessages:inputText
                               completion:^(FIRSmartReplySuggestionResult * _Nullable result,
                                            NSError * _Nullable error) {
      if (error || !result) {
        return;
      }
      if (result.status == FIRSmartReplyResultStatusNotSupportedLanguage) {
          // The conversation's language isn't supported, so the
          // the result doesn't contain any suggestions.
      } else if (result.status == FIRSmartReplyResultStatusSuccess) {
          // Successfully suggested smart replies.
          // ...
      }
    }];
    ]

If the operation succeeds, a `SmartReplySuggestionResult` object is passed to
the completion handler. This object contains a list of up to 3 suggested
replies, which you can present to your user:

### Swift

    for suggestion in result.suggestions {
      print("Suggested reply: \(suggestion.text)")
    }

### Objective-C

    for (FIRSmartReplySuggestion *suggestion in result.suggestions) {
      NSLog(@"Suggested reply: %@", suggestion.text);
    }

Note that ML Kit might not return results if the model isn't confident in
the relevance of the suggested replies, the input conversation isn't in
English, or if the model detects sensitive subject matter.
**Known issue**: Currently, on 32-bit iOS devices, ML Kit doesn't return suggestions for any input.