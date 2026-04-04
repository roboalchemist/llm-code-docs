# Source: https://firebase.google.com/docs/tutorials/welcome-back-screen.md.txt

Personalized content can delight your users and provide an experience from the very first interaction with your app based on their preferences, usage history, and locale. Firebase allows you to define audiences based onGoogle Analyticsmetrics and customize your application withFirebase Remote Configdirectly from theFirebaseconsole.

Using these two features together, you can customize your app's welcome back screen for a repeat user based on their preferences or activity in your app.

This guide walks you through the process to create your own personalized "welcome back" screen on Android.

To get started, you'll need an Android app connected to a Firebase project. If you don't already have one, see[Get started for Android](https://firebase.google.com/docs/android/setup)to connect your app.

## Implementation overview

Implementing your app's personalized welcome screen consists of 3 broad steps:

1. **Set upRemote Configto hold parameters for the elements to be personalized.**For example, you might store the welcome screen message as a parameter. This way you can update the message without republishing your app.
2. **Set upAnalyticsto define audiences and/or user properties forRemote Configto target your users.**Both features can be used for targeting; however, there are important differences between them. The relative advantages of each are discussed later in this guide.
3. **ConfigureRemote Configconditions to customize your parameter based on theAnalyticsaudiences or user properties you set up.**

## Set up parameters inRemote Config

Once you identify the elements of your app you want to customize, useRemote Configto store parameters. We'll explore personalizing the welcome screen message in the rest of this guide.

### What to do in the Firebase console

1. Go to the[Remote Configparameter](https://console.firebase.google.com/project/_/config)page in theFirebaseconsole. If you've never configuredRemote Configin your app, click**Add Your First Parameter**.
2. Fill out a parameter key and default value. For example,`welcome_message`and`Welcome to this sample app`.

   ![<span class=](https://firebase.google.com/static/docs/tutorials/images/remote-config-param.png)Remote Configparameter configuration."\>
3. Click**Publish Changes**.

### What to do in the Android app

1. Add code to read and display the parameter you just added to your app in theFirebaseconsole. For example:

       final FirebaseRemoteConfig config = FirebaseRemoteConfig.getInstance();
       config.getInstance.fetch(CACHE_EXPIRATION_MS)
         .addOnCompleteListener(this, new OnCompleteListener<Void>() {
           @Override
           public void onComplete(@NonNull Task<Void> task) {
               if (task.isSuccessful()) {
                   config.activateFetched();

                   String welcomeMessage = config.getString("welcome_message");
               }
           }
       });

   You can also follow the steps in[Use FirebaseRemote Configon Android](https://firebase.google.com/docs/remote-config/get-started?platform=android)to read and display the parameter that you created in the console. If you get stuck, the[Android walkthrough](https://firebase.google.com/docs/remote-config/android)guides you through the working sample app implementation.
2. Turn on[developer mode](https://firebase.google.com/docs/reference/android/com/google/firebase/remoteconfig/FirebaseRemoteConfigSettings.Builder#setDeveloperModeEnabled(boolean))to see config changes immediately while testing.

### Test that it works

1. Open your app and make sure that it shows the current value of the parameter in the[Remote ConfigUI](https://console.firebase.google.com/project/_/config).
2. Change the value in the console and click**Publish Changes**
3. Restart your app. The new parameter value should be shown.

## Set upAnalyticsaudiences or user properties

In this step you'll useAnalyticsto define the users who should see personalized content. In this walkthrough, we'll use a user property to do this but you could also define an[Audience](https://support.google.com/firebase/answer/6317509?hl=en&ref_topic=6317489). These approaches are similar, but you should be aware that once a user is added to an Audience, they cannot leave it or be removed. If the attribute you want to use for targeting could change, use a user property instead.

### What to do in the Firebase console

1. Go to the[Analyticsuser property](https://console.firebase.google.com/project/_/analytics/userproperty)page in theFirebaseconsole. Click**New User Property**.
2. Give the user property a name and description. For example, if you were customizing an app based on whether a user prefers dogs or cats, you might name it`animal_preference`.

   ![<span class=](https://firebase.google.com/static/docs/tutorials/images/analytics-user-property.png)Analyticsuser property configuration."\>
3. Click**Create**.

### What to do in the Android app

1. Follow the steps in[Set User Properties](https://firebase.google.com/docs/analytics/android/properties#set_user_properties)to learn to set your user property in your application. For example, you might ask a user if they prefer cats or dogs and set a string value accordingly. You can skip over the steps to register your property in the console as you've already done that in the previous section.
2. Follow the steps in[Debugging Events](https://firebase.google.com/docs/analytics/debugview)to enable debug mode for your app.

### Test that it works

1. Open your app and navigate to where your user property is set.
2. Open the[AnalyticsDebugView page](https://console.firebase.google.com/project/_/analytics/debugview)in theFirebaseconsole.
3. Look to see if any user properties have been set (there might be a few minutes of delay before anything shows up).

## ConfigureRemote Configconditions

Now that your app has parameters that can be configured, and user properties (or audiences) to use as variables, you can create conditions to personalize the values of your parameters.

### What to do in the Firebase console

1. Go to[Remote Config](https://console.firebase.google.com/project/_/config)in theFirebaseconsole.
2. Click your parameter to edit it.
3. Click**Add value for condition**.
4. Select**Define new condition**.
5. Give your condition a name. For example, "Prefers cats" to reflect the user preference from earlier.
6. Under**Applies if** , select**User property** (or**User in audience** if you created an Audience inAnalytics), and select your parameter, and define a conditional relationship with your parameter values.

   ![A new <span class=](https://firebase.google.com/static/docs/tutorials/images/new-condition.png)Remote Configcondition."\>
7. Click**Create condition**.

8. Enter a value to reflect the new condition. For example, the welcome message for "Prefers cats" could be "Meow!".

9. Click**Update**to save your changes.

10. Click**Publish Changes**to enable the new conditions and values in your app.

### Test that it works

1. Open your app and navigate to where your user property is set.
2. Open the[AnalyticsDebugView page](https://console.firebase.google.com/project/_/analytics/debugview)in theFirebaseconsole.
3. Look to see if any user properties have been set (there might be a few minutes of delay before anything shows up).
4. Restart your app and verify that your personalized elements have been set.