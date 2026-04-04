# Source: https://firebase.google.com/docs/functions/use-cases.md.txt

# Source: https://firebase.google.com/docs/remote-config/personalization/use-cases.md.txt

# Source: https://firebase.google.com/docs/hosting/use-cases.md.txt

# Source: https://firebase.google.com/docs/remote-config/use-cases.md.txt

<br />

App developers useRemote Configin many different ways to suit their unique requirements, and we encourage that. To give you an idea of the kinds of things you can do withRemote Config, this page describes some use cases with broad applicability to mobile developers.

## Launch new features with the percentage rollout mechanism

You can useRemote Configto perform a percentage rollout to slowly expose your users to new functionality. For this use case, let's say you have a new search function that is enabled and disabled using aRemote Configparameter named`new_search_feature_flag`, and you want to begin by rolling it out to 10% of your installed user base.

To achieve this, edit your`new_search_feature_flag`parameter, add a new condition, and select**User in random percentage**. Use the slider to set the random percentage between 0 and 10.
| **Tip:** You can use the**Seed** value to create multiple conditions that target specific ranges of the same randomized group of users. See[User in random percentage](https://firebase.google.com/docs/remote-config/parameters#random_percentage)for more information.
![Image moving through the Firebase console GUI steps to perform a percentage rollout on an existing parameter](https://firebase.google.com/static/docs/remote-config/images/RCUC_1_New_Feature_Rollout_1_1.png)Adding parameter for percentage feature rollout

Now, when the`new_search_feature_flag`value is fetched fromRemote Config, 10% of randomly selected users receive the value`true`, while the other 90% receive the value`false`.

When you are satisfied with the stability of the feature in 10% of the user population, you can increase it to 30%, to 50%, and eventually to 100% once you have full confidence in the feature.
| **Tip:** Be sure to add a[real-timeRemote Configlistener](https://firebase.google.com/docs/remote-config/real-time)to your app to ensure that your feature flag is rolled out (or rolled back) as soon as you modify your template.

## Define platform and locale-specific promo banners for your app

Imagine you have an e-commerce sale coming up and you want to enable a promotional splash page in your app. Further, imagine you want to customize this splash page to the same locale that your user has set on their device. You can define a parameter`promo_splash_graphic`and set its value to static URLs (hosted on[Firebase Storage](https://firebase.google.com/docs/storage/)or elsewhere) and then reference them dynamically in your app.

You could then assign different values to Android and Apple for locales that are most important to your promotional marketing campaign.If you need to trigger promotions at a specific time, you can useRemote Config's time conditions, and you can also use[real-timeRemote Config](https://firebase.google.com/docs/remote-config/real-time)to ensure that the changes are pulled soon after the template is published, and then you can activate them as-needed within your app.
![Animated image moving through the Firebase console GUI steps to define platform and locale-specific promo banners](https://firebase.google.com/static/docs/remote-config/images/RCUC_2_Promo_Banners_1_1.gif)Adding parameter for localized promo banners

You can also use the[Remote Configbackend APIs](https://firebase.google.com/docs/remote-config/automate-rc)to update the parameter values programmatically and then trigger the functionality from a cron job.

## Provide custom experiences for your users based on first-time app use

You can useRemote Configto provide custom experiences for users based on the date and time they first open your app, including the following use cases:

- Provide different onboarding flows as users join your app.
- Expose incentives or features hidden behind feature flags or toggles to new users after a certain date.
- Provide custom experiences to users who joined during a specific time period.

Let's say that you want to provide an in-game gift to new users to encourage initial engagement and retention,*and* you want to provide a different reward to a group of longtime users. You can create a parameter named`extra_coin_splash`that controls a pop-up that offers free in-game currency with a customizable message, number of bonus coins, and maximum number of times to re-display the offer if the user hasn't accepted the offer. You can use the in-app default value as the parameter default, and then create two conditions.

First, add a**Conditional value** to your`extra_coins_splash`Remote Configparameter that targets a specific Android or iOS app, set**First open**to a date and time in the future, and then set the parameter value to:  

    {"banner_text": "Welcome! Enjoy some extra coins!", "bonus_coins": 15, "max_display_retries": 2}

Next, add a condition for an existing user group that you want to reward, for example, all users who joined in July and are still using your game in October. To do this, add another**Conditional value** to the`extra_coins_splash`parameter with**First open**set between July 1 and August 1, and set the parameter value to:  

    {"banner_text": "Thanks for being a loyal user!", "bonus_coins": 30, "max_display_retries": 2}:

Your final`extra_coins_splash`parameter will look like the following:

![Remote Config parameter with conditional values](https://firebase.google.com/static/docs/remote-config/images/RCUC_5_NewUserTargeting_1.png "Remote Config parameter with conditional values")

After you publish your config with this parameter, both groups of users will receive the extra coin parameter values you configured after their next fetch.

As a next step, try an[A/B Testingexperiment](https://firebase.google.com/docs/ab-testing)or[personalization](https://firebase.google.com/docs/remote-config/personalization)with your parameters and targeting conditions, using different banner messages and bonus coin amounts.

## Test new functionality on a limited testing group

Normally for testing new functionality within a limited testing group, you would use an Alpha channel on Google Play or Test Flight for an Apple app. These tools are perfect when you want to test new functionality in the same cadence as your regular development cycle.

However, sometimes you might have a feature that you would like to test more quickly, and easily enable or disable regardless of the timing of the next release in your regular development cycle. For such cases,Remote Configcan be a very helpful tool.

Let's say you wanted to test new graphics among employees in your company. How could that be enabled withRemote Config?

When users log in to your app, check for their email ID and set up the user property`is_mydomain_employee=true`that applies only when the email belongs to your domain. Then create a condition that tracks that user property. You can target this user property inRemote Configand enable the new functionality only for these users.
![Animated image moving through the Firebase console GUI steps to test new functionality on a limited testing group](https://firebase.google.com/static/docs/remote-config/images/RCUC_3_Internal_Testing_1_1.gif)Targeting testing groups with a condition

## Use JSON to configure complex entities in your app or game

As your app grows in complexity, you need better ways of supplying configuration to your app. For example, if you want to configure a new login system, you might create oneRemote Configparameter for each dynamic value you want to control. However, configuring your login system this way is tedious, and very hard to understand and maintain.

A better way to provide configuration for such a login system would be to use JSON and group all of those parameters into one single parameter. This helps in editing and maintaining the`login`parameter much more easily over time.

TheFirebaseconsole provides a JSON validator and pretty-printer that you can use when editingRemote Configparameters. When working in the console, click the**{}**icon to open the editor.
![Animated image moving through the Firebase console GUI steps to configure complex entities with JSON](https://firebase.google.com/static/docs/remote-config/images/RCUC_4_JSON_Configurations_1_1.gif)Using the JSON editor to group parameters

## Send Slack / Email message when aRemote Configupdate is published

If you are part of a large team which usesRemote Config, it's often hard to keep track of who's publishingRemote Configin your team and when.

To simplify collaborative workflows, you can be alerted via your favorite mechanism (Slack or Email) in near real time. TheRemote ConfigREST API together with aRemote Configbackground trigger inCloud Functions for Firebasecan let you send a notification whenever yourRemote Configtemplate changes.

eBay recently[open sourced their implementation](https://github.com/eBay/firebase-remote-config-monitor/tree/master/functions)for how they useCloud FunctionswithRemote Configto publish a diff of previous vs newRemote Configtemplates into a Slack channel.