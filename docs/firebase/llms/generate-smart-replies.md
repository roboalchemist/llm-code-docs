# Source: https://firebase.google.com/docs/ml-kit/ios/generate-smart-replies.md.txt

# Source: https://firebase.google.com/docs/ml-kit/generate-smart-replies.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/generate-smart-replies.md.txt

| This page describes an old version of the Smart Reply API, which was part of ML Kit for Firebase. Development of this API has been moved to the standalone ML Kit SDK, which you can use with or without Firebase.[Learn more](https://developers.google.com/ml-kit/migration).
|
| See[Generate smart replies with ML Kit on Android](https://developers.google.com/ml-kit/language/smart-reply/android)for the latest documentation.

<br />

You can use ML Kit to generate message replies using an on-device model.

To generate smart replies, you pass ML Kit a log of recent messages in a conversation. If ML Kit determines the conversation is in English, and that the conversation doesn't have potentially sensitive subject matter, ML Kit generates up to three replies, which you can suggest to your user.

<br />

## Before you begin

1. If you haven't already,[add Firebase to your Android project](https://firebase.google.com/docs/android/setup).
2. Add the dependencies for the ML Kit Android libraries to your module (app-level) Gradle file (usually`app/build.gradle`):  

   ```carbon
   apply plugin: 'com.android.application'
   apply plugin: 'com.google.gms.google-services'

   dependencies {
     // ...
     implementation 'com.google.firebase:firebase-ml-natural-language:22.0.0'
     implementation 'com.google.firebase:firebase-ml-natural-language-smart-reply-model:20.0.7'
   }
   ```
3. Also in your app-level`build.gradle`file, disable compression of`tflite`files:  

   ```text
   android {
       // ...
       aaptOptions {
           noCompress "tflite"
       }
   }
   ```

## 1. Create a conversation history object

To generate smart replies, you pass ML Kit a chronologically-ordered`List`of`FirebaseTextMessage`objects, with the earliest timestamp first.

Whenever the user sends a message, add the message and its timestamp to the conversation history:  

### Java

    conversation.add(FirebaseTextMessage.createForLocalUser(
            "heading out now", System.currentTimeMillis()));

### Kotlin

    conversation.add(FirebaseTextMessage.createForLocalUser(
            "heading out now", System.currentTimeMillis()))

Whenever the user receives a message, add the message, its timestamp, and the sender's user ID to the conversation history. The user ID can be any string that uniquely identifies the sender within the conversation. The user ID doesn't need to correspond to any user data, and the user ID doesn't need to be consistent between conversation or invocations of the smart reply generator.  

### Java

    conversation.add(FirebaseTextMessage.createForRemoteUser(
            "Are you coming back soon?", System.currentTimeMillis(), userId));

### Kotlin

    conversation.add(FirebaseTextMessage.createForRemoteUser(
            "Are you coming back soon?", System.currentTimeMillis(), userId))

A conversation history object looks like the following example:

|          Timestamp           | User ID | Local User? |       Message        |
|------------------------------|---------|-------------|----------------------|
| Thu Feb 21 13:13:39 PST 2019 |         | true        | are you on your way? |
| Thu Feb 21 13:15:03 PST 2019 | FRIEND0 | false       | Running late, sorry! |

Note that the most recent message in the example above is from a non-local user. This is important because ML Kit suggests replies intended to be sent by the user of your app: the local user. You should be sure you're passing ML Kit a conversation log that ends with a message to which your user might want to reply.

## 2. Get message replies

To generate smart replies to a message, get an instance of`FirebaseSmartReply`and pass the conversation history to its`suggestReplies()`method:  

### Java

    FirebaseSmartReply smartReply = FirebaseNaturalLanguage.getInstance().getSmartReply();
    smartReply.suggestReplies(conversation)
            .addOnSuccessListener(new OnSuccessListener<SmartReplySuggestionResult>() {
                @Override
                public void onSuccess(SmartReplySuggestionResult result) {
                    if (result.getStatus() == SmartReplySuggestionResult.STATUS_NOT_SUPPORTED_LANGUAGE) {
                        // The conversation's language isn't supported, so the
                        // the result doesn't contain any suggestions.
                    } else if (result.getStatus() == SmartReplySuggestionResult.STATUS_SUCCESS) {
                        // Task completed successfully
                        // ...
                    }
                }
            })
            .addOnFailureListener(new OnFailureListener() {
                @Override
                public void onFailure(@NonNull Exception e) {
                    // Task failed with an exception
                    // ...
                }
            });

### Kotlin

    val smartReply = FirebaseNaturalLanguage.getInstance().smartReply
    smartReply.suggestReplies(conversation)
            .addOnSuccessListener { result ->
                if (result.getStatus() == SmartReplySuggestionResult.STATUS_NOT_SUPPORTED_LANGUAGE) {
                    // The conversation's language isn't supported, so the
                    // the result doesn't contain any suggestions.
                } else if (result.getStatus() == SmartReplySuggestionResult.STATUS_SUCCESS) {
                    // Task completed successfully
                    // ...
                }
            }
            .addOnFailureListener {
                // Task failed with an exception
                // ...
            }

If the operation succeeds, a`SmartReplySuggestionResult`object is passed to the success handler. This object contains a list of up to 3 suggested replies, which you can present to your user:  

### Java

    for (SmartReplySuggestion suggestion : result.getSuggestions()) {
        String replyText = suggestion.getText();
    }

### Kotlin

    for (suggestion in result.suggestions) {
        val replyText = suggestion.text
    }

Note that ML Kit might not return results if the model isn't confident in the relevance of the suggested replies, the input conversation isn't in English, or if the model detects sensitive subject matter.