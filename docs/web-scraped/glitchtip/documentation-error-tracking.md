# Source: https://glitchtip.com/documentation/error-tracking

Title: GlitchTip

URL Source: https://glitchtip.com/documentation/error-tracking

Markdown Content:
[Setting up Error Tracking](https://glitchtip.com/documentation/error-tracking#setting-up-error-tracking)
---------------------------------------------------------------------------------------------------------

Your web app can send any errors it encounters to GlitchTip, which will notify you and record the error as an issue so you can see the details.

[Configuring your app](https://glitchtip.com/documentation/error-tracking#configuring-your-app)
-----------------------------------------------------------------------------------------------

Once you have created your GlitchTip project, the next step is to set up your web app so it can send error notifications to GlitchTip. If you previously selected a platform for your project and visit the Issues page, you will see detailed instructions for installing an SDK and configuring it to work with GlitchTip. If you did not select a platform, you can do that now on the project settings page, or you can read our SDK documentation [here](https://glitchtip.com/sdkdocs). When you first visit the issues page you will also see the DSN for your project. If you need to view your DSN later, you will be able to find it on the project settings page. Follow the SDK instructions to get your app set up and give it your DSN.

![Image 1: Screenshot of GlitchTip configuration instructions on issues page.](https://glitchtip.com/assets/screenshots/start-project@1x.png)

[Try it out](https://glitchtip.com/documentation/error-tracking#try-it-out)
---------------------------------------------------------------------------

Next, add some code to your project that will generate an error, such as dividing by zero. Once the error has been generated, navigate back to the issues page and verify that GlitchTip is now keeping a watchful eye on your app. Make sure to remove your test error once you’ve confirmed everything is working.

![Image 2: Screenshot of GlitchTip's issues page with a new issue displayed.](https://glitchtip.com/assets/screenshots/one-issue@1x.png)

[Turn on alerts](https://glitchtip.com/documentation/error-tracking#turn-on-alerts)
-----------------------------------------------------------------------------------

Now that GlitchTip is receiving your project’s errors, you will probably want to activate project alerts. Navigate to your organization’s Projects page and click the settings button on your project. Then scroll down to the Project Alerts section and click “Create New Alert”.

![Image 3: Screenshot of GlitchTip's project alert form.](https://glitchtip.com/assets/screenshots/new-project-alert@1x.png)

Here you can specify when you want to receive alerts based on the frequency of errors. By default, new project alerts send emails to a project’s team members, but you can also add a webhook URL by clicking “Add An Alert Recipient.”
