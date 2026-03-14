# Source: https://docs.logrocket.com/reference/ending-sessions-react-native.md

# Ending Sessions (React Native)

End the current session with various levels of urgency for React Native

Logrocket sessions will automatically end according to the logic outlined [here](https://docs.logrocket.com/docs/what-defines-a-session#logrocket-native-mobile-sdks). The following options can be used if you wish to stop the SDK outside of these conditions.

> 🚧 Avoid calling these in the main UI thread to prevent impacting user experience
>
> Due to the need for the shutdown process to wait on various actions to complete successfully , please ensure that if you call `shutdown()`,  or `startNewSession()` you are doing so off of the main UI thread so that rendering is not blocked.

### shutdown()

* This function will shutdown the SDK and end the current session gracefully, ensuring all data from the current session is successfully uploaded.
* If [init() ](https://docs.logrocket.com/reference/android#initializing-the-sdk) is called afterwards the previous session will be resumed.

### startNewSession ()

* This function will both end the current session, and initialize a new session. The new session will have no connection to the previous one. This is best used for shared devices with multiple users, where you want to understand separate user behavior across different sessions.
* More information on using this option [here](https://docs.logrocket.com/reference/starting-a-new-clean-session-react-native)\*\*