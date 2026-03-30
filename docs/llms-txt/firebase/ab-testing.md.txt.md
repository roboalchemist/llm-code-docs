# Source: https://firebase.google.com/docs/ab-testing.md.txt

# Firebase A/B Testing

[Video](https://www.youtube.com/watch?v=OxMQORNh2E4)

Firebase A/B Testing helps you optimize your app experience by
streamlining the way you run, analyze, and scale product and marketing
experiments. It gives you the power to test changes to your app's UI, features,
or engagement campaigns to see how they impact your key
metrics (like revenue and retention) before you roll them out widely.

A/B Testing works with FCM so you can test different marketing
messages, and with Remote Config so you can test changes within your app.

<br />

Ready to get started? Choose a product:

[Create Remote Config experiments](https://firebase.google.com/docs/ab-testing/abtest-config)
[Create messaging experiments](https://firebase.google.com/docs/ab-testing/abtest-with-console)

## Key capabilities

|---|---|
| Test and improve your product experience | Create experiments with Remote Config to make changes to the behavior and appearance of your app across the variants in your experiment, and test which product experience is most effective at driving the results you most care about. |
| Find ways to re-engage your users by using the Notifications composer | Use A/B Testing to help you find the most effective wording and messaging settings for bringing users into your app. |
| Safely roll out new features | Don't roll a new feature out without making sure it meets your goals with a smaller subset of users first. Once you have confidence in your A/B Testing results, roll the feature out to all your users. |
| Target user groups | Run targeted A/B tests using data about your app users. For example, you could target a subset of users running a specific app version, platform, language, or select users that match a Google Analytics [user property](https://firebase.google.com/docs/analytics/user-properties) value. |

## How does it work?

When you create an experiment, create multiple variants of a user experience
and measure how well the variants perform toward a goal that you want to achieve
(such as boosting in-app purchases). Your targeted
user group can be defined by multiple criteria chained with "AND" logic; for
example, you could limit the group to users of a particular app version
who belong to both an Analytics
audience such as "crashing users" that match a custom Google Analytics
user property set by the client.

![AB Testing experiments test Remote Config and messaging actions
using Google Analytics to target users and measure outcomes.](https://firebase.google.com/static/docs/ab-testing/images/Diagram-AB-Testing-IO-v3.svg)

With Remote Config, you can experiment with changes to one or more
parameters to alter the behavior and appearance of your app. You could use this
for subtle changes like tinkering with the best color scheme and positioning of
menu options, or for more significant changes like testing a completely new
feature or UI design. With the Notifications composer, you can experiment to
find the right wording for a notification message.

Whether your experiment uses Remote Config or the Notifications composer, you can
monitor your experiment until you identify a *leader*, the variant that best
accomplishes your goal. You can start your experiment with a small percentage of
your user base, and increase that percentage over time. If your first
experiment does not reveal a variant that accomplishes your goal better than the
baseline, you can start a new round of experimentation to find the best way to
improve your app.

You can
also track other metrics (app crashes, retention, and revenue) along with
your goal so that you can have a better understanding of the outcome of your
experiment and how it impacts the experience of using your app.

## Implementation path

|---|---|---|
|   | Add Remote Config or Firebase Cloud Messaging to your app | If your app already uses Remote Config or Cloud Messaging (or both), you can skip to the next step. |
|   | Define the variants that you want to evaluate with an A/B test. | Whether your change is subtle or the addition of a new UI or feature, if you can control that change using Remote Config, you can test multiple variants on that change with A/B Testing. You can also use A/B Testing with the Notifications composer to test multiple variants on your re-engagement campaign before you roll it out to all users. |
|   | Define how you will measure success | With an experiment that uses the Notifications composer, you can use an Analytics event to define the goal of your experiment and compare experiment variants. With a Remote Config experiment, you can use either an Analytics event or a conversion funnel to define the goal of your experiment. |
|   | Monitor your experiment to find the winning variant | You can start your experiment with just a few users, and then roll it out to more users if early results look good. As you monitor your experiment, you will see whether some variants cause more app crashes or other impacts on the app experience, and you can also see which variant makes the most progress toward your goal. |

## Next steps

- Learn more about experiment concepts and best practices in [About Firebase A/B Testing](https://firebase.google.com/docs/ab-testing/ab-concepts).
- Get started creating experiments for [Remote Config](https://firebase.google.com/docs/ab-testing/abtest-config), [the Notifications composer](https://firebase.google.com/docs/ab-testing/abtest-with-console), or [In-App Messaging](https://firebase.google.com/docs/ab-testing/abtest-inappmessaging).
- Learn more about the Firebase features that interact with A/B Testing: [Google Analytics](https://firebase.google.com/docs/analytics), [Firebase Remote Config](https://firebase.google.com/docs/remote-config), [Cloud Messaging notifications](https://firebase.google.com/docs/cloud-messaging/concept-options#notifications), [In-App Messaging](https://firebase.google.com/docs/in-app-messaging), [AdMob](https://firebase.google.com/docs/admob), and [Remote Config personalization](https://firebase.google.com/docs/remote-config/personalization).