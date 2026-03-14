# Source: https://docs.snowflake.com/en/user-guide/data-integration/openflow/processors/consumetwitter.md

# ConsumeTwitter 2025.10.9.21

## Bundle

org.apache.nifi | nifi-social-media-nar

## Description

Streams tweets from Twitter’s streaming API v2. The stream provides a sample stream or a search stream based on previously uploaded rules. This processor also provides a pass through for certain fields of the tweet to be returned as part of the response. See <https://developer.twitter.com/en/docs/twitter-api/data-dictionary/introduction> for more information regarding the Tweet object model.

## Tags

json, social media, status, tweets, twitter

## Input Requirement

FORBIDDEN

## Supports Sensitive Dynamic Properties

false

## Properties

| Property | Description |
| --- | --- |
| backfill-minutes | The number of minutes (up to 5 minutes) of streaming data to be requested after a disconnect. Only available for project with academic research access. See <https://developer.twitter.com/en/docs/twitter-api/tweets/filtered-stream/integrate/recovery-and-redundancy-features> |
| backoff-attempts | The number of reconnection tries the processor will attempt in the event of a disconnection of the stream for any reason, before throwing an exception. To start a stream after this exception occur and the connection is fixed, please stop and restart the processor. If the valueof this property is 0, then backoff will never occur and the processor will always need to be restartedif the stream fails. |
| backoff-time | The duration to backoff before requesting a new stream ifthe current one fails for any reason. Will increase by factor of 2 every time a restart fails |
| base-path | The base path that the processor will use for making HTTP requests. The default value should be sufficient for most use cases. |
| batch-size | The maximum size of the number of Tweets to be written to a single FlowFile. Will write fewer Tweets based on the number available in the queue at the time of processor invocation. |
| bearer-token | The Bearer Token provided by Twitter. |
| connect-timeout | The maximum time in which client should establish a connection with the Twitter API before a time out. Setting the value to 0 disables connection timeouts. |
| expansions | A comma-separated list of expansions for objects in the returned tweet. See <https://developer.twitter.com/en/docs/twitter-api/expansions> for proper usage. Possible field values include: author_id, referenced_tweets.id, referenced_tweets.id.author_id, entities.mentions.username, attachments.poll_ids, attachments.media_keys ,in_reply_to_user_id, geo.place_id |
| maximum-backoff-time | The maximum duration to backoff to start attempting a new stream. It is recommended that this number be much higher than the ‘Backoff Time’ property |
| media-fields | A comma-separated list of media fields to be returned as part of the tweet. Refer to <https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/media> for proper usage. Possible field values include: alt_text, duration_ms, height, media_key, non_public_metrics, organic_metrics, preview_image_url, promoted_metrics, public_metrics, type, url, width |
| place-fields | A comma-separated list of place fields to be returned as part of the tweet. Refer to <https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/place> for proper usage. Possible field values include: contained_within, country, country_code, full_name, geo, id, name, place_type |
| poll-fields | A comma-separated list of poll fields to be returned as part of the tweet. Refer to <https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/poll> for proper usage. Possible field values include: duration_minutes, end_datetime, id, options, voting_status |
| queue-size | Maximum size of internal queue for streamed messages |
| read-timeout | The maximum time of inactivity between receiving tweets from Twitter through the API before a timeout. Setting the value to 0 disables read timeouts. |
| stream-endpoint | The source from which the processor will consume Tweets. |
| tweet-fields | A comma-separated list of tweet fields to be returned as part of the tweet. Refer to <https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet> for proper usage. Possible field values include: attachments, author_id, context_annotations, conversation_id, created_at, entities, geo, id, in_reply_to_user_id, lang, non_public_metrics, organic_metrics, possibly_sensitive, promoted_metrics, public_metrics, referenced_tweets, reply_settings, source, text, withheld |
| user-fields | A comma-separated list of user fields to be returned as part of the tweet. Refer to <https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/user> for proper usage. Possible field values include: created_at, description, entities, id, location, name, pinned_tweet_id, profile_image_url, protected, public_metrics, url, username, verified, withheld |

## Relationships

| Name | Description |
| --- | --- |
| success | FlowFiles containing an array of one or more Tweets |

## Writes attributes

| Name | Description |
| --- | --- |
| mime.type | The MIME Type set to application/json |
| tweets | The number of Tweets in the FlowFile |
