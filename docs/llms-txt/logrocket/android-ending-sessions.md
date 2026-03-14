# Source: https://docs.logrocket.com/reference/android-ending-sessions.md

# Ending Sessions (Android)

End the current session with various levels of urgency for Android

Logrocket sessions will automatically end according to the logic outlined [here](https://docs.logrocket.com/docs/what-defines-a-session#logrocket-native-mobile-sdks). The following options can be used if you wish to stop the SDK outside of these conditions.

> 🚧 Avoid calling these in the main UI thread to prevent impacting user experience
>
> Due to the need for the shutdown process to wait on various actions to complete successfully , please ensure that if you call `shutdown()`, `endSession()` or `hardShutdown()` you are doing so off of the main UI thread so that rendering is not blocked.

### shutdown()

* This function will shutdown the SDK and end the current session gracefully, ensuring all data from the current session is successfully uploaded.
* If [init() ](https://docs.logrocket.com/reference/android#initializing-the-sdk) is called afterwards the previous session will be resumed.

### endSession()

* This function will shutdown the SDK gracefully and end the current session. Some session data just before session end may be lost.
* If [init() ](https://docs.logrocket.com/reference/android#initializing-the-sdk) is called afterwards a new session will be started.

### hardShutdown()

* This function will shutdown the SDK as abruptly as possible and end the current session imediately, purging any session data not yet uploaded, resulting in loss of data.
* If [init() ](https://docs.logrocket.com/reference/android#initializing-the-sdk) is called afterwards a new session will be started.

### startNewSession ()

* This function will both end the current session, and initialize a new session. The new session will have no connection to the previous one. This is best used for shared devices with multiple users, where you want to understand separate user behavior across different sessions.
* More information on using this option [here](https://docs.logrocket.com/reference/android-start-new-session)