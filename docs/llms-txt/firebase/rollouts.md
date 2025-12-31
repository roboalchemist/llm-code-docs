# Source: https://firebase.google.com/docs/app-hosting/rollouts.md.txt

# Source: https://firebase.google.com/docs/remote-config/rollouts.md.txt

# Source: https://firebase.google.com/docs/app-hosting/rollouts.md.txt

# Source: https://firebase.google.com/docs/remote-config/rollouts.md.txt

<br />

Remote Configrollouts give you the ability to safely and gradually release new features and updates to your app. Using a[Remote Configparameter](https://firebase.google.com/docs/remote-config/parameters), you can release new app features in a controlled manner to specific user groups. As your rollout proceeds, monitor its success usingFirebase CrashlyticsandGoogle Analytics. UseRemote Configrollouts to:

- **Minimize potential issues:**Identify and address any bugs or issues before they impact a large portion of your user base.
- **Gather valuable feedback:**Collect feedback from a limited audience and iterate on your implementation before rolling out to a wider audience.
- **Enable iterative development:**Make quick, iterative changes to widely-deployed apps while mitigating risk
- **Monitor metrics you care about:** Compare app stability between rollout and control groups withCrashlyticsand useGoogle Analyticsto monitor metrics like revenue and engagement.

For example, if you created an app that incorporates generative AI and stores prompts within aRemote ConfigJSON parameter, you might want to:

1. Create a rollout that updates the parameter that contains your LLM prompt(s) to a small percentage of your user base.
2. Monitor the resulting performance--have conversions increased or decreased? What about engagement? Are there more or fewer crashes?
3. Depending on the results of the rollout, you may decide to:
   - Roll back your change.
   - Update the prompt parameter value to adjust and refine your model's response.
   - Increase your rollout percentage to roll out to a larger audience, ultimately rolling out 100% of your users.

You can also[access the history](https://firebase.google.com/docs/remote-config/templates#firebase-console)of all of your changes using theFirebaseconsole.
| Monitoring forRemote Configrollouts is available for the following versions of Firebase SDKs:
|
| - Firebase iOS SDK v10.24.0+
| - Firebase SDK for Android SDK v21.6.0+ (Firebase BoM v32.6.0+)
|
| CrashlyticsandGoogle Analyticsare optional, but provide significant value by measuring app stability and reporting key metrics like revenue, conversions, and user engagement. Rollout metrics are available for the following versions:
|
| - CrashlyticsAndroid SDK v18.6.0+ (Firebase BoM v32.6.0+)
| - CrashlyticsiOS SDK v10.24.0
| - Firebase SDK forGoogle Analytics(any version)

## Key capabilities

|-------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| Target by user attributes     | Deliver features to specific user segments based on user properties, app behavior, or any other relevant criteria.                                  |
| Staged rollouts               | Gradually increase the percentage of users exposed to a new feature over time, reducing the risk of unexpected issues.                              |
| Monitor stability             | UseCrashlyticsto monitor potential issues (like crashes, non-fatal errors, and non-responsive apps) that may be introduced by your feature release. |
| Gain insight into key metrics | Ensure that your new release positively affects theGoogle Analyticsmetrics you care about, like conversions, revenue, and user engagement.          |
| Rollback functionality        | If rollout results show potential issues, roll back to a previous version of the feature for all or a specific segment of affected users.           |

## How does it work?

Remote Configrollouts rely on three key components:

1. [Remote Config](https://firebase.google.com/docs/remote-config)stores and manages your app's configuration data, including feature flags and configuration parameters.
2. [Crashlytics](https://firebase.google.com/docs/crashlytics)provides real-time crash reporting and performance monitoring so that you can track the impact of your rollout and quickly identify any trending issues.
3. [Google Analytics](https://firebase.google.com/docs/analytics)provides the ability to target rollouts based on user attributes*and*monitor how your launch affects key metrics like revenue, user engagement, and conversion events.

For more information, see[AboutRemote Configrollouts](https://firebase.google.com/docs/remote-config/rollouts/about).

## Implementation Path

|---|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | ConfigureRemote Config  | Define your feature flags and configuration parameters in theFirebaseconsole.                                                                                |
|   | Set upCrashlytics       | IntegrateCrashlyticsinto your app to monitor its performance and identify any issues.                                                                        |
|   | Set upGoogle Analytics  | IntegrateAnalyticsinto your app to view key metrics like revenue and user retention.                                                                         |
|   | Implement rollout logic | ConfigureRemote Configin theFirebaseconsole and in your app to access and apply feature flags and configuration parameters based on user targeting criteria. |
|   | Monitor and iterate     | MonitorCrashlyticsdata and user feedback to track the rollout's impact and make adjustments as needed.                                                       |

## Policies and limits

A/B Testingexperiments andRemote Configrollouts share the total experiment limit: 24. For example, if you are running 12 A/B Tests, you are limited to 12 running rollouts.

## Next steps

- Learn more[aboutRemote Configrollouts](https://firebase.google.com/docs/remote-config/rollouts/about).
- Get started with[Remote Configrollouts](https://firebase.google.com/docs/remote-config/rollouts/get-started).