# Source: https://firebase.google.com/docs/reference/unity/namespace/firebase/remote-config.md.txt

# Source: https://firebase.google.com/docs/reference/js/remote-config.md.txt

# Source: https://firebase.google.com/docs/reference/cpp/class/firebase/remote-config/remote-config.md.txt

# Source: https://firebase.google.com/docs/ai-logic/solutions/remote-config.md.txt

# Source: https://firebase.google.com/docs/remote-config.md.txt

# Source: https://firebase.google.com/docs/ai-logic/solutions/remote-config.md.txt

# Source: https://firebase.google.com/docs/remote-config.md.txt

# Firebase Remote Config

plat_iosplat_androidplat_webplat_flutterplat_cppplat_unity  
Change the behavior and appearance of your web client or server without publishing an app update, at no cost, for unlimited daily active users.  
FirebaseRemote Configis a cloud service that lets you change the behavior and appearance of your client app or server without requiring users to download an app update. When usingRemote Config, you create in-app default values that control the behavior and appearance of your application. Then, you can later use theFirebaseconsole or theRemote Configbackend APIs to override in-app default values for allRemote ConfigAPI consumers or for segments of your user base. Your app or server implementation controls when updates are applied, and it can frequently check for updates and apply them with a negligible impact on performance.

<br />

<br />

Ready to get started? Choose your platform:

[iOS+](https://firebase.google.com/docs/remote-config/ios/get-started)[Android](https://firebase.google.com/docs/remote-config/android/get-started)[Web](https://firebase.google.com/docs/remote-config/web/get-started)[Flutter](https://firebase.google.com/docs/remote-config/flutter/get-started)

[Unity](https://firebase.google.com/docs/remote-config/unity/get-started)[C++](https://firebase.google.com/docs/remote-config/cpp/get-started)[Backend APIs](https://firebase.google.com/docs/remote-config/automate-rc)

## Key capabilities

|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Quickly release changes to your app's user base                                                                                            | You can make changes to your app's default behavior and appearance by changing parameter values remotely. For example, you could use aRemote Configparameter as a feature flag to change your app's layout or color theme to support a seasonal promotion, with no need to publish an app update. | Server implementations can now fetch parameters and values. See[UseRemote Configin server environments](https://firebase.google.com/docs/remote-config/server)for more information.                                                |
| Customize your app for segments of your user base                                                                                          | You can useRemote Configto provide variations on your app's user experience to different segments of your user base by app version, language,[Google Analyticsaudience](https://support.google.com/analytics/answer/9267572), and[imported segment](https://firebase.google.com/docs/projects/import-segments). You can also useRemote Config[custom signal conditions](https://firebase.google.com/docs/remote-config/parameters?template_type=client#custom_signal_conditions)to match custom parameters you configure for your app. |
| UseRemote Configpersonalization to automatically and continuously customize your app for individual users and optimize for strategic goals | Use machine learning to continuously tailor individual user experience to optimize for goals like user engagement, ad clicks, and revenue---or any custom event you can measure withGoogle Analytics---with[Remote Configpersonalization](https://firebase.google.com/docs/remote-config/personalization).                                                                                                                                                                                                                             |
| Iteratively roll out new features to targeted segments of your user base and compare against an automatically-provisioned control group    | UseRemote Configrollouts to release targeted updates using parameter values as feature flags, gradually releasing new functionality to your users. Determine release stability and success by comparingCrashlyticsandGoogle Analyticsresults between the group receiving your rollout value and an equal-sized control group.                                                                                                                                                                                                          |
| Run A/B tests to improve your app                                                                                                          | You can use[A/B Testing](https://firebase.google.com/docs/ab-testing/abtest-config)and[random percentage targeting withGoogle Analytics](https://firebase.google.com/docs/remote-config/parameters#random_percentage)to A/B test improvements to your app across different segments of your user base to validate improvements before rolling them out to your entire user base.                                                                                                                                                       |

## How does it work?

Remote Configincludes a client library that handles important tasks like fetching parameter values and caching them, while still giving you control over when new values are*activated*so that they affect your app's user experience. This lets you safeguard your app experience by controlling the timing of any changes.

We recommend adding[real-timeRemote Config](https://firebase.google.com/docs/remote-config/real-time)functionality to your fetch logic to automatically fetch the latestRemote Configparameter values as soon as they're published.

TheRemote Configclient library`get`methods provide a single access point for parameter values. Your app fetches values fromRemote Configusing the same logic it uses to get in-app default values, so you can add the capabilities ofRemote Configto your app without writing a lot of code.

To override in-app default values, you use theFirebaseconsole or theRemote Configbackend APIs to create parameters with the same names as the parameters used in your app. For each parameter, you can set a default value inRemote Configto override the in-app default value, and you can also create conditional values to override the in-app default value for app instances that meet certain conditions.

Remote Configalso provides a server client library in the Firebase Admin Node.js SDK v12.1.0+. Your server implementations can use this to fetch values from server-specific templates stored byRemote Config. Learn more at[UseRemote Configin server environments](https://firebase.google.com/docs/remote-config/server).

To learn more about parameters, conditions, and howRemote Configresolves conflicts between conditional values, see[Remote ConfigParameters and Conditions](https://firebase.google.com/docs/remote-config/parameters).

## Implementation path

|---|-------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | Instrument your app withRemote Config                                                                                                     | Define which aspects of your app's behavior and appearance you want to be able to change usingRemote Config, and translate these into the parameters that you will use in your app.                                                                                                                                                                                                                                                                                                                                                                                   |
|   | Set default parameter values                                                                                                              | Set the in-app default values forRemote Configparameters using`setDefaults()`and, optionally,[download yourRemote Configtemplate defaults](https://firebase.google.com/docs/remote-config/templates#download_template_defaults).                                                                                                                                                                                                                                                                                                                                      |
|   | Add logic to fetch, activate, and get parameter values                                                                                    | Your app can safely and efficiently fetch parameter values from theRemote Configbackend periodically and activate those fetched values. Real-timeRemote Configlets your apps fetch updated values as soon as a newRemote Configversion is published without the need for polling. You can write your app without worrying about the best time to fetch values, or even whether any server-side values exist. Your app uses`get`methods to get the value of a parameter, similar to reading the value of a local variable defined in your app.                         |
|   | (As needed) Update default and conditional parameter values inRemote Config                                                               | You can define values in theFirebaseconsole or theRemote Configbackend APIs to override in-app default values. You can do this before or after you launch your app, because the same`get`methods access in-app default values and values fetched from theRemote Configbackend. See[Remote Configtemplates and versioning](https://firebase.google.com/docs/remote-config/templates)to learn more about managing and updatingRemote Configparameters and values. | Creating and editing server-specificRemote Configtemplates is only supported on theFirebaseconsole. |
|   | (As needed) Update default parameter values in your app                                                                                   | Whenever you update your app, you should synchronize its default parameter values with theRemote Configbackend. You can quickly download a file of default values in XML, property list (plist), or JSON format to update your app using the REST API andFirebaseconsole. For more information, see[DownloadRemote Configtemplate defaults](https://firebase.google.com/docs/remote-config/templates#download_template_defaults).                                                                                                                                     |
|   | UseA/B TestingandRemote Configpersonalization to customize user experience and determine the best parameter values to achieve your goals. | After you implementRemote Configin your app, you can use it to experiment, extend, and update your app with enhanced features like[A/B Testing](https://firebase.google.com/docs/ab-testing)and[Remote Configpersonalization](https://firebase.google.com/docs/remote-config/personalization).                                                                                                                                                                                                                                                                        |

## Policies and limits

Note the following policies:

- Don't useRemote Configto make app updates that should require a user's authorization. This could cause your app to be perceived as untrustworthy.
- Don't store confidential data inRemote Configparameter keys or parameter values.Remote Configdata is encrypted in transit, but end users can access any default or fetchedRemote Configparameter that is available to their app instance.
- Don't attempt to circumvent the requirements of your app's target platform usingRemote Config.

Remote Configparameters and conditions are subject to certain limits. To learn more, see[Limits on parameters and conditions](https://firebase.google.com/docs/remote-config/parameters#limits_on_parameters_and_conditions).

Note the following limits:

- A Firebase project can have 3000Remote Configparameters per template type (client or server), which are subject to length and content limits detailed in[Limits on parameters and conditions](https://firebase.google.com/docs/remote-config/parameters#limits_on_parameters_and_conditions).

- Firebase stores up to 300 lifetime versions of yourRemote Configtemplates per template type (client or server). This 300 version lifetime limit includes stored version numbers for deleted templates. See[Templates and versioning](https://firebase.google.com/docs/remote-config/templates)for details.

- You can have up to 24 running[A/B experiments](https://firebase.google.com/docs/ab-testing/ab-concepts#limits)and[Remote Configrollouts](https://firebase.google.com/docs/remote-config/rollouts#limits)combined.

## Looking to store other types of data?

- [Cloud Firestore](https://firebase.google.com/docs/firestore)is a flexible, scalable database for mobile, web, and server development from Firebase andGoogle Cloud.
- [Firebase Realtime Database](https://firebase.google.com/docs/database)stores JSON application data, like game state or chat messages, and synchronizes changes instantly across all connected devices. To learn more about the differences between database options, see[Choose a database:Cloud FirestoreorRealtime Database](https://firebase.google.com/docs/firestore/rtdb-vs-firestore).
- [Firebase Hosting](https://firebase.google.com/docs/hosting)hosts global assets, including the HTML, CSS, and JavaScript for your website as well as other developer-provided assets like graphics, fonts, and icons.
- [Cloud Storage](https://firebase.google.com/docs/storage)stores files such as images, videos, and audio as well as other user-generated content.

## Next steps

- See what you can do withRemote Configby reviewing typical[use cases](https://firebase.google.com/docs/remote-config/use-cases).
- Start your design. Review the key concepts and strategies such as[Remote Configparameters and conditions](https://firebase.google.com/docs/remote-config/parameters)and[loading strategies](https://firebase.google.com/docs/remote-config/loading).
- Get started integratingRemote Configwith your app. See the setup guides for[Android](https://firebase.google.com/docs/remote-config/android/get-started),[iOS+](https://firebase.google.com/docs/remote-config/ios/get-started), and[Web](https://firebase.google.com/docs/remote-config/web/get-started).
- Learn how to read and[modifyRemote Configparameter values programmatically](https://firebase.google.com/docs/remote-config/automate-rc).
- Learn how to create[Remote Configexperiments with A/B testing](https://firebase.google.com/docs/ab-testing/abtest-config).
- Learn how to use[Remote Configpersonalization](https://firebase.google.com/docs/remote-config/personalization)to automatically optimize individual user experience to achieve your goals.
- Learn how to use[Remote Configrollouts](https://firebase.google.com/docs/remote-config/rollouts)to gradually and iteratively release new features to your user base, verifying success and stability with side-by-sideCrashlyticsandGoogle Analyticsresults.
- Learn how to use[Remote Configin server environments](https://firebase.google.com/docs/remote-config/server).