Source: https://docs.slack.dev/changelog/2017-02-minor-field-changes

# Minor field changes

February 1, 2017

It's almost spring and we're doing a little cleaning early this year.

Ever notice how the `username` field of a file object in `channels.history` or \[`file_shared`\](/reference/events/file\_shared event isn't like typical username fields and contains a bunch of markup usually reserved only for message text?

And why is there a top-level `skype` field in user profile objects when _really_, shouldn't that be a custom field?

Well, _we've_ noticed. And so...

## What's changing? {#whats-changing}

On March 20, 2017:

1. Instead of seeing funky strings like `<U123456:tomatotude>` in the `username` field of file-related messages in `channels.history` and file-related events in the [Events](/apis/events-api/) & [RTM API](/legacy/legacy-rtm-api) APIs, you'll instead encounter just plain old `tomatotude` — because that's the username. If you want the user ID, you can fetch it from the `user` field just like any other message.

2. The `skype` field in [user](/reference/objects/user-object) profile data will begin appearing as a blank string: `""`. For teams with this profile field set today, you'll find that value in the custom profile fields configured for that team. If you attempt to set the `skype` field via [`users.profile.set`](/reference/methods/users.profile.set), your request will technically succeed but the provided value will be stubbornly ignored.

## What isn't changing? {#what-isnt-changing}

* No other types of message objects or events _besides_ file uploads will change in this correction to the `username` field.
* The `skype` field will not be removed from API responses.

## How do I prepare? {#how-do-i-prepare}

It is unlikely that you need to do anything at all.

In the rare case that you've customized behavior to deal with this `username` anomaly, you may need to adjust your behavior to treat it like a typical `username` field again.

If your app relies on a team's populated `skype` field, you'll need to look for it as part of the user's profile available in expanded user objects and with [`users.profile.get`](/reference/methods/users.profile.get).

## When is this happening? {#when-is-this-happening}

We'd like to enable these changes on **March 20, 2017**.

Please review how you handle these fields and, if necessary, make any needed modifications. Have questions or concerns? We're happy to help! Feel free to contact us [here](https://slack.com/help/requests/new).

**Tags:**

* [Announcement](/changelog/tags/announcement)
