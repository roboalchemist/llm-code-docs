# Source: https://firebase.google.com/docs/ml-kit/generate-smart-replies.md.txt

# Smart Reply

> [!CAUTION]
> This page describes an old version of the Smart Reply API, which was part
> of ML Kit for Firebase. Development of this API has been moved to the
> standalone ML Kit SDK, which you can use with or without Firebase.
> [Learn more](https://developers.google.com/ml-kit/migration).
>
> See
> [Smart Reply](https://developers.google.com/ml-kit/language/smart-reply)
> for the latest documentation.

![](https://firebase.google.com/static/docs/ml-kit/images/smart_reply@2x.png)

With ML Kit's Smart Reply API, you can automatically generate relevant
replies to messages. Smart Reply helps your users respond to messages quickly,
and makes it easier to reply to messages on devices with limited input
capabilities.

[iOS](https://firebase.google.com/docs/ml-kit/ios/generate-smart-replies)
[Android](https://firebase.google.com/docs/ml-kit/android/generate-smart-replies)
This is a beta release of ML Kit for Firebase. This API might be changed in backward-incompatible ways and is not subject to any SLA or deprecation policy.

## Key capabilities

|---|---|
| Generates contextually-relevant suggestions | The Smart Reply model generates reply suggestions based on the full context of a conversation, and not just a single message, resulting in suggestions that are more helpful to your users. |
| Runs on the device | The on-device model generates replies quickly, and doesn't require you to send users' messages to a remote server. |

## Limitations

- Smart Reply is intended for casual conversations in consumer apps. Reply suggestions might not be appropriate for other contexts or audiences.
- Currently, only English is supported. The model automatically detects if a different language is used and if so, will not provide suggestions.

## How the model works

- The model uses up to 10 of the most recent messages from a conversation history to generate reply suggestions.
- It detects the language of the conversation and only attempts to provide responses when the language is determined to be English.
- Next, the model compares the messages against a list of sensitive topics and won't provide suggestions when it detects a sensitive topic.
- If the language is determined to be English and no sensitive topics are detected, the model provides up to three suggested responses. The number of responses depends on how many meet a sufficient level of confidence based on the input to the model.

## Providing feedback

Due to the complexity of natural language processing, the suggestions provided
by the model might not be appropriate for all contexts or audiences. If you
encounter inappropriate reply suggestions, reach out to
[Firebase support](https://firebase.google.com/support). Your feedback
helps to continue to improve the model and sensitive topic filter.

## Example results

### Input

| Timestamp | User ID | Local User? | Message |
|---|---|---|---|
| Thu Feb 21 13:13:39 PST 2019 |   | true | are you on your way? |
| Thu Feb 21 13:15:03 PST 2019 | FRIEND0 | false | Running late, sorry! |

### Suggested replies

| Suggestion #1 | Suggestion #2 | Suggestion #3 |
|---|---|---|
| No worries | 😞 | No problem! |