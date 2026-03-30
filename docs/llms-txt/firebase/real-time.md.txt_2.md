# Source: https://firebase.google.com/docs/remote-config/ios/real-time.md.txt

# Understand real-time Remote Config

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/remote-config/ios/real-time) [Android](https://firebase.google.com/docs/remote-config/android/real-time) [Web](https://firebase.google.com/docs/remote-config/web/real-time) [Flutter](https://firebase.google.com/docs/remote-config/flutter/real-time) [Unity](https://firebase.google.com/docs/remote-config/unity/real-time) [C++](https://firebase.google.com/docs/remote-config/cpp/real-time) |

Real-time Remote Config lets you receive updated [parameter keys and
values](https://firebase.google.com/docs/remote-config/parameters) as soon as
they're published on the server. This lets you quickly update any type of
app attribute controlled using a Remote Config parameter value. With
real-time Remote Config updates, you can:

- Reduce risk by rolling out features incrementally to targeted users, and performing an emergency rollback if needed.
- Increase user engagement by quickly customizing user experiences as they use the app. For example, you could update banners and offer incentives for users who match specific Google Analytics user properties or dynamically adjust game difficulty for cohorts of players.
- Reduce build dependencies and increase developer productivity: Use Remote Config parameters as feature flags to expose functionality for your development and test teams, while keeping it hidden to users in production.

To learn more about ways you can use Remote Config, see [What can you do
with
Remote Config?](https://firebase.google.com/docs/remote-config/use-cases)

In this guide, you'll:

- Learn more about the client-server relationship that supports real-time updates.
- Understand how the real-time functionality in the SDK works.
- Learn how to use real-time updates to keep your app configuration up-to-date.

> [!NOTE]
>
> Real-time updates are available for the Firebase SDK for Apple platforms v10.7.0+.

## The real-time client-server connection

When you implement real-time Remote Config in your app, you create a
real-time listener that opens an HTTP connection to the Remote Config
backend. The request includes the config version that's cached on the
device. The real-time Remote Config server uses an *invalidation message* to
signal to the app when a newer version of a server-side config should be
fetched.

If the server has a newer version, it sends the invalidation signal immediately.
If it doesn't have a newer version, it keeps the connection open and waits until
one is published on the server. When the client SDK receives an invalidation
signal, it automatically fetches it, then calls the listener callback registered
when you opened the listener connection. This fetch is similar to the fetch call
you can make with the SDK, but bypasses any caching or `minimumFetchInterval`
setting. The client-server connection is maintained while the app is in the
foreground.
![Real-time Remote Config client-server workflow](https://firebase.google.com/static/docs/remote-config/images/real-time-client-server.png) Real-time Remote Config client-server workflow

Since the client-server connection is made over HTTP, it doesn't require any
dependencies on other libraries.

## Listen for updates

Real-time updates complement Remote Config `fetch` calls. We recommend
calling fetch when your app starts (or sometime during your app's lifecycle) and
listening for real-time Remote Config updates during the user session to
ensure that you have the latest values as soon as they're published on the
server.

To listen for updates, call
[`addOnConfigUpdateListener`](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration),
implementing a callback that is invoked whenever a Remote Config update is
available in the app. Behind the scenes, this call starts listening for updates
from the Remote Config server. To learn more about the client-server
relationship, see [the previous section](https://firebase.google.com/docs/remote-config/ios/real-time#real-time-client-server-connection).

The callback is often a good place to use `activate` to make the updated config
parameters available to your app. See [Firebase Remote Config Loading
Strategies](https://firebase.google.com/docs/remote-config/loading) for
additional strategies to activate parameter values when you're using real-time
Remote Config.

## Selectively activate parameter values

When you call
[`addOnConfigUpdateListener`](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration),
you can await the change and activate it.

The `onUpdate` callback is called when both a new version of the template has
been automatically fetched and when that new version has changes to the
active parameter values in the app.

These callbacks are invoked with a parameter `configUpdate`.
`configUpdate` contains `updatedKeys`,
which is the set of changed parameter keys that initiated the real-time update
and includes the following:

- Parameter keys that were added or removed
- Parameter keys whose values have changed
- Parameter keys whose metadata has changed (for example, Remote Config personalization information)
- Parameter keys whose value source has changed (for example, an in-app default value updating to a server-side value)

If you're using a real-time listener in a particular view within your app, you
can check if the parameters relevant to that view have changed before
activating.

Occasionally, a fetch (either initiated when you call the `fetch` method, or by
real-time Remote Config) does not result in an update for the client. In
these cases, the
`onUpdate`
method or completion won't be called.

## Add and remove listeners

[`addOnConfigUpdateListener`](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration)
is the main entrypoint for real-time Remote Config. Calling this listener
for the first time in your app's lifecycle opens the connection to the backend.
Subsequent calls reuse the same connection, multiplexing the invalidation
message described in [the real-time client-server connection](https://firebase.google.com/docs/remote-config/ios/real-time#real-time-client-server-connection).

The call returns a "listener registration," which has a method called
[`remove`](https://firebase.google.com/docs/reference/swift/firebaseremoteconfig/api/reference/Classes/ConfigUpdateListenerRegistration).
To stop listening, store the reference to the listener registration. Call
`remove` to stop listening at this registration. If it's the only registered
listener, calling `remove` closes the real-time connection to the server.

Although you *can* manually stop listening for updates, it's often not
necessary. Real-time Remote Config automatically stops listening for updates
when the app enters the background and restarts when the app is foregrounded.

> [!NOTE]
> Real-time Remote Config limits projects to 20 million concurrent open connections. If a project exceeds this limit, incremental real-time connection requests may be rejected, and the client SDK will automatically fall back to the standard fetch mechanism. To ensure all clients receive configuration updates when published, this 20 million connection limit is temporarily suspended for the project while the newly-published template is propagating.

## Next steps

Check out [Get started with Firebase
Remote Config](https://firebase.google.com/docs/remote-config/get-started/ios) to configure
Remote Config and start [listening for updates in
real-time](https://firebase.google.com/docs/remote-config/ios/get-started#add-real-time-listener).