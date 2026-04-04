# Source: https://firebase.google.com/docs/remote-config/loading.md.txt

<br />

Firebase Remote Configprovides lots of flexibility for how and when to fetch new values from the server and activate them in your app, allowing you to ensure a quality end user experience by controlling the timing of any visible configuration changes. You can fetch new values on application launch using`fetchAndActivate()`, and use[real-timeRemote Config](https://firebase.google.com/docs/remote-config#how_it_works)as a complementary method to automatically fetch the latest parameter values after a new version of yourRemote Configis published.

This guide looks at a few loading strategies and discusses key considerations for picking the best option for your app.

## Strategy 1: Fetch and activate on load

In this strategy, your app would call`fetchAndActivate()`when your app first starts up to fetch new values fromRemote Configand activate them as soon as they are done loading. This simple approach works well for configuration changes that don't cause any dramatic visual changes in your UI. It should be avoided in any situation where your UI could change noticeably while users are in the middle of using it.

After your app calls`fetchAndActivate()`, it can start listening for parameter value updates in real time by calling`addOnConfigUpdateListener`. This method starts listening for any server-side updates to parameter values, fetches them automatically, then calls the listener. A simple strategy is to activate the new values in the listener. However, as mentioned for`fetchAndActivate()`, activating immediately should be avoided for sensitive UIs.

## Strategy 2: Activate behind loading screen

As a remedy to the potential UI issue encountered in strategy 1, you could rely on a loading screen. Instead of starting up your app right away, show a loading screen and call`fetchAndActivate`in your completion handler. Then right after that --- again using a callback or a notification --- dismiss the loading screen and allow the user to start interacting with your app.

If you use this strategy, it's recommended to add a timeout to the loading screen. Remote Config's one-minute timeout may be too long for a quality app startup experience for users.

Listening for real-timeRemote Configupdates by calling`addOnConfigUpdateListener`works well with this strategy. Add the listener when the loading screen is displayed, then use`activate()`at one or more points in your app whereRemote Configvalues won't cause dramatic visual changes.
| **Note:** If you are loading values for an[A/B Testing](https://firebase.google.com/docs/ab-testing/abtest-config)experiment, this strategy is very strongly recommended. WithA/B Testing, additional time is required as the user is placed into an experiment and the experimental values are applied.

## Strategy 3: Load new values for next startup

An effective strategy is to load new configuration values to activate on your app's*next*startup. In this strategy, your app activates fetched values on startup before attempting to fetch new ones, operating on the assumption that it may have already fetched --- but not yet activated --- new configuration values. The order of operations for this strategy is:

1. On startup, immediately activate previously fetched values. This applies any values you've downloaded from the server in a previous session, and is nearly instantaneous.
2. While the user interacts with your app, kick off an asynchronous call to fetch new values according to the default minimum fetch interval and add a real-time config update listener. The real-time listener will automatically fetch any values that are published on the server while your app is running. Real-time updates bypass the minimum fetch interval setting.
3. In the completion handler or callback for the fetch call, do nothing. Your app will keep the downloaded values until you activate them the next time the app starts.

With this strategy, user wait time is greatly minimized. Combining the fetch and real-time listener strategies with`activate()`calls as needed in the app lifecycle makes sure users have the latest values fromRemote Configas they interact with your app.
| **Tip:** Use`fetch()`and`addOnConfigUpdateListener()`as complementary methods. It's recommended to call fetch once per app launch, then start listening for updates in real time and activate them as needed. Listening for real-time updates makes it possible to get the latest parameter values without calling fetch frequently.

## Loading anti-strategies

As you may have understood from the above discussion of loading pros and cons, there are a couple of usage patterns to avoid.

- **Don't** update or switch aspects of the UI while the user is viewing or interacting with it ---*unless*you have strong app or business reasons for doing so, like removing options related to a promotion that has just ended.
- **Don't** send mass numbers of simultaneous fetch requests, which could result in the server throttling your app. If you need to fetch updates frequently, use[real-timeRemote Config](https://firebase.google.com/docs/remote-config#how_does_it_work). While the risk of throttling is low in most production scenarios, it can be an issue during active development---and real-timeRemote Configis designed for this use case. Check out the[throttling guidance](https://firebase.google.com/docs/remote-config/get-started#throttling).
- **Don't** rely on network connectivity to obtainRemote Configvalues.**Do** set in-app default parameter values so that your app always behaves as expected. You can periodically keep app andRemote Configbackend default values in sync using[downloaded template defaults](https://firebase.google.com/docs/remote-config/templates#download_template_defaults).

## Next steps

These three basic strategies do not by any means comprise a complete list of the ways to load configuration values. Depending on your needs, you could devise much more sophisticated strategies.

Check out the API reference for your platform to learn more about the specific calls for fetching and activating configuration values.