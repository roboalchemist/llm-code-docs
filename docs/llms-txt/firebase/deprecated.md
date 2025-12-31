# Source: https://firebase.google.com/docs/reference/unity/deprecated/deprecated.md.txt

# Deprecated List

## Summary


- Member [Firebase.AI.CountTokensResponse.TotalBillableCharacters](https://firebase.google.com/docs/reference/unity/struct/firebase/a-i/count-tokens-response#struct_firebase_1_1_a_i_1_1_count_tokens_response_1a6eb175efeeae649f94f3d6e83e497bec)
Use TotalTokens instead; Gemini 2.0 series models and newer are always billed by token count.
- Member [Firebase.AI.LiveSession.SendMediaChunksAsync](https://firebase.google.com/docs/reference/unity/class/firebase/a-i/live-session#class_firebase_1_1_a_i_1_1_live_session_1afd03a3dfb47b89b0e802d0e6c5430183) (List\< ModelContent.InlineDataPart \> mediaChunks, CancellationToken cancellationToken=default)
Use SendAudioRealtimeAsync, SendVideoRealtimeAsync, or SendTextRealtimeAsync instead.

<br />