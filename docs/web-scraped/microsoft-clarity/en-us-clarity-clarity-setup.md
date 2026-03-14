# Source: https://learn.microsoft.com/en-us/clarity/clarity-setup

Title: How to setup Clarity manually

URL Source: https://learn.microsoft.com/en-us/clarity/clarity-setup

Markdown Content:
Tip

Want to check out what Clarity is? Try our live [Demo](https://clarity.microsoft.com/demo/projects/view/3t0wlogvdz/heatmaps?date_h=Last%203%20days&url_h=https%3A%2F%2Fclarity.microsoft.com%2F).

You need to install the tracking code to start using Clarity on your website. Each website you add to your Clarity account has its unique tracking code to install. You can add the same script to multiple subdomains of your website.

1.   Select a project and go to **Settings** ->**Setup**. Learn [how to add a project](https://learn.microsoft.com/en-us/clarity/setup-and-installation/getting-started#add-a-new-project).

2.   Choose an installation method with which you would like to proceed further.

![Image 1: Choose an installation method.](https://learn.microsoft.com/en-us/clarity/media/setup-1.png)

There are three ways to install Clarity:

*   [Install on a third-party platform](https://learn.microsoft.com/en-us/clarity/clarity-setup#install-on-a-third-party-platform)
*   [Install manually](https://learn.microsoft.com/en-us/clarity/clarity-setup#install-manually)
*   [Install using NPM](https://learn.microsoft.com/en-us/clarity/clarity-setup#install-using-npm)

You can also [share code with your team member](https://learn.microsoft.com/en-us/clarity/clarity-setup#share-code-with-your-team-member) who can help you with the installation.

Note

*   Clarity shouldn't be used on any websites/apps targeting users under the age of 18 globally.
*   You can instantly start viewing data in the project as soon as you add the code.
*   By default, Clarity masks all sensitive content on your site.

You can install Clarity tracking code on third-party platforms like Shopify, SquareSpace, Wix, WordPress, and more. Refer to the [list of supported third-party platforms](https://learn.microsoft.com/en-us/clarity/third-party-integrations/clarity-third-platform).

1.   Select **View all platforms** for a list of supported platforms.

![Image 2: Select view all platforms.](https://learn.microsoft.com/en-us/clarity/media/select-view-all-platforms.png)

2.   Setup Clarity using any of the listed platforms. Follow the setup instructions on each platform as you select one.

![Image 3: View supported platforms.](https://learn.microsoft.com/en-us/clarity/media/list-of-supported-platforms.png)

3.   If your platform isn't listed, select **I don't see my platform** to submit a request.

![Image 4: Select I don't see my platform.](https://learn.microsoft.com/en-us/clarity/media/select-no-platform.png)

4.   Enter the platform name and select **Submit**. While we'll try to support your platform in the future, you can [install the code manually](https://learn.microsoft.com/en-us/clarity/clarity-setup#install-manually) to start using Clarity immediately.

![Image 5: Submit platform request.](https://learn.microsoft.com/en-us/clarity/media/submit-platform-request.png)

Note

To set up Clarity, you need access to your website's `<head>` section.

1.   To manually install, select **Get tracking code**.

![Image 6: Select get tracking code.](https://learn.microsoft.com/en-us/clarity/media/select-get-tracking-code.png)

2.   Copy the code and paste it into the `<head>` section of your website or web app.

![Image 7: Copy tracking code.](https://learn.microsoft.com/en-us/clarity/media/copy-tracking-code.png)

The NPM integration enables you to seamlessly incorporate advanced analytics into your JavaScript projects, offering features like heatmaps, session recordings, and much more. To get started, use the Clarity package available on NPM and follow the provided instructions to add the initialization code to your site. Refer to the [NPM documentation](https://www.npmjs.com/package/@microsoft/clarity) to learn more.

![Image 8: View NPM installation instructions.](https://learn.microsoft.com/en-us/clarity/media/view-npm-installation-instructions.png)

Choose this method if you like to share the code with a team member who can help you set up Clarity.

1.   Select **Share code**.

![Image 9: Select share code.](https://learn.microsoft.com/en-us/clarity/media/select-share-code.png)

2.   Enter your team member's email ID and select **Submit**. An email with the tracking code and setup instructions is sent to your teammate.

![Image 10: Enter email ID and select submit.](https://learn.microsoft.com/en-us/clarity/media/enter-email-to-share-code.png)

There are two ways to verify if Clarity is installed correctly:

Once the script is added, find your project's Recordings and Dashboard data instantly. As soon you add the tracking code, you can view [real time](https://learn.microsoft.com/en-us/clarity/session-recordings/clarity-real-time) data with the number of current live users as shown:

![Image 11: View number of live recordings.](https://learn.microsoft.com/en-us/clarity/media/clarity-live-recordings-installation.png)

Select **Watch now** to start viewing the live users.

See POST requests to [https://www.clarity.ms/collect](https://www.clarity.ms/collect) while interacting with your site. Here are the steps to view the request:

1.   Right-click on your website and select **Inspect**.

![Image 12: Right click and select inspect.](https://learn.microsoft.com/en-us/clarity/media/setup-verification-1.png)

2.   Go to the **Network** tab and select **collect** file. You can view the POST request as shown.

![Image 13: Go to network and select collect.](https://learn.microsoft.com/en-us/clarity/media/setup-verification-2.png)

3.   Once you see the data on your project dashboard, explore [Heatmaps](https://learn.microsoft.com/en-us/clarity/heatmaps/heatmaps-overview) to see how users interact with your website.

Optionally, using this section, you can integrate and manage Google Analytics, and Google Tag Manager.

Google Analytics integration allows Clarity to link session playbacks with your Google Analytics dashboard.

Select **Getting started** if you wish to integrate and learn more about [Google Analytics integration](https://learn.microsoft.com/en-us/clarity/ga-integration/ga-integration).

![Image 14: Select getting started in GA integration.](https://learn.microsoft.com/en-us/clarity/media/ga-integration.png)

Google Tag Manager integration is automatically detected.

1.   Select **Finish setup** if you wish to integrate.

![Image 15: Select finish setup on GTM.](https://learn.microsoft.com/en-us/clarity/media/finish-setup-gtm.png)

2.   If you wish not to integrate, select **Sign in with a different account**.

3.   Select a **GTM account**, **GTM container** from the drop-down, and select **Create and publish**.

![Image 16: Select create and publish.](https://learn.microsoft.com/en-us/clarity/media/gtm-setup-publish.png)

Manage cookies and fraud detection through advanced settings.

Clarity uses cookies to gather session data. Toggle the button to turn on cookies.

![Image 17: Cookies in advanced settings.](https://learn.microsoft.com/en-us/clarity/media/cookie-setting.png)

If this setting is turned off, you need to pass the consent. Recordings aren't linked together into multi-page sessions. [Learn how to customize the usage of cookies](https://learn.microsoft.com/en-us/clarity/setup-and-installation/consent-mode).

![Image 18: Turn off cookies.](https://learn.microsoft.com/en-us/clarity/media/cookies-off.png)

By default, Clarity detects bot traffic and excludes it from total session count and analytics. You can view the number of excluded bot sessions at the top of your dashboard.

![Image 19: Bots excluded in dashboard.](https://learn.microsoft.com/en-us/clarity/media/bots-excluded.png)

Toggle the button to turn bot detection off or back on again. When bot detection is turned off, Clarity is unable to detect bot traffic and exclude this from your total session count.

![Image 20: Turn on bot detection.](https://learn.microsoft.com/en-us/clarity/media/bot-detection-on.png)

Clarity works on most sites with little code. It requires some modern browser APIs but should never throw exceptions on older browsers.

Though any site architecture is supported, Clarity can't capture what's inside your website's Canvas or third-party iFrame elements.

For answers to common questions, refer to [Setup FAQ](https://learn.microsoft.com/en-us/clarity/faq#setup).
