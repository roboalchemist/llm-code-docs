# Source: https://plausible.io/docs/troubleshoot-integration

Title: Check if Plausible is installed correctly | Plausible docs

URL Source: https://plausible.io/docs/troubleshoot-integration

Markdown Content:
After you've [added the Plausible snippet to your site](https://plausible.io/docs/plausible-script), the dashboard will start displaying the stats in real-time as soon as the first visit is counted. There are no delays with data in Plausible.

If you see the dashboard with graphs and numbers, it means everything is working and we've counted your first visitor. Congrats! Plausible is now tracking your website statistics while preserving the privacy of your visitors.

Do you keep seeing a blinking green dot screen instead of the dashboard? The blinking green dot indicates that we’re listening for incoming visits in real-time but haven't recorded any yet.

Our testing tool will launch automatically from the blinking green dot screen to send test traffic to your site. This test traffic won't be recorded in the dashboard but you'll see a status message indicating whether Plausible Analytics has been installed correctly.

![Image 1: Integration verification tool](https://plausible.io/docs/img/v2/integration-verification-tool.webp)

### Launch the Plausible testing tool from your site settings[​](https://plausible.io/docs/troubleshoot-integration#launch-the-plausible-testing-tool-from-your-site-settings "Direct link to Launch the Plausible testing tool from your site settings")

Have you made any changes to your integration? You can launch our testing tool at any time from your [site settings](https://plausible.io/docs/website-settings) to verify whether the changes you made has worked.

Did our testing tool detect an issue with your integration? Or is there something unusual about the data you're seeing? See how to troubleshoot the most common issues below.

Did you block a specific segment of traffic using Shields?[​](https://plausible.io/docs/troubleshoot-integration#did-you-block-a-specific-segment-of-traffic-using-shields "Direct link to Did you block a specific segment of traffic using Shields?")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The **Shields** feature lets you block visits from being recorded based on IP addresses, hostnames, countries or specific pages.

If your own visits are missing, check whether you have added any [Shields rules](https://plausible.io/docs/excluding) that might be excluding them. Review the list of active rules for this site and make sure none of them apply to your current location or setup.

Have you added the Plausible snippet into your site?[​](https://plausible.io/docs/troubleshoot-integration#have-you-added-the-plausible-snippet-into-your-site "Direct link to Have you added the Plausible snippet into your site?")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We've put together [many integration guides](https://plausible.io/docs/integration-guides) that cover popular website builders and content management systems (CMS) such as WordPress and Ghost. Thanks to the members of our community, there are also community integrations and plugins for several frameworks such as Hugo and GatsbyJS. These can help you set up and start counting your site visitors in no time.

Have you cleared the cache of your site?[​](https://plausible.io/docs/troubleshoot-integration#have-you-cleared-the-cache-of-your-site "Direct link to Have you cleared the cache of your site?")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you are using caching on your site, the latest version of your site where our snippet is integrated may not be showing to all your visitors yet. Do purge the cache to ensure that you're presenting the latest version of your site to all your visitors.

Have you implemented Plausible using Google Tag Manager?[​](https://plausible.io/docs/troubleshoot-integration#have-you-implemented-plausible-using-google-tag-manager "Direct link to Have you implemented Plausible using Google Tag Manager?")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Please follow [our GTM guide](https://plausible.io/gtm-template) for instructions on how to integrate Plausible with our Google Tag Manager template.

Does your site use a Content Security Policy (CSP)?[​](https://plausible.io/docs/troubleshoot-integration#does-your-site-use-a-content-security-policy-csp "Direct link to Does your site use a Content Security Policy (CSP)?")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If it does, you would need to add our domain name (plausible.io) specifically to the allowed domains list in order for the script to work. [More info here](https://github.com/plausible/docs/issues/20).

Are you running on localhost?[​](https://plausible.io/docs/troubleshoot-integration#are-you-running-on-localhost "Direct link to Are you running on localhost?")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Our script automatically disables itself when running on localhost as most people don't want those stats to be counted. If you do want to track stats on localhost, [see our configuration guide](https://plausible.io/docs/script-extensions).

Are you running a Google AMP page?[​](https://plausible.io/docs/troubleshoot-integration#are-you-running-a-google-amp-page "Direct link to Are you running a Google AMP page?")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To track Google AMP pages with Plausible, you need to declare an AMP-analytics object on your AMP pages. [See the instructions here](https://github.com/plausible/analytics/discussions/220#discussioncomment-904022).

Did you insert multiple Plausible snippets into your site?[​](https://plausible.io/docs/troubleshoot-integration#did-you-insert-multiple-plausible-snippets-into-your-site "Direct link to Did you insert multiple Plausible snippets into your site?")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This may affect the accuracy of the tracking and can result in the stats being counted twice. Please make sure to only insert one snippet.

Are you using an older version of our script?[​](https://plausible.io/docs/troubleshoot-integration#are-you-using-an-older-version-of-our-script "Direct link to Are you using an older version of our script?")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In some cases when you’re using a custom proxy implementation, you may not be using the latest version of our tracking script. This doesn’t necessarily mean that the tracking won’t work but our automated verification tool won’t be able to confirm whether your integration is working correctly. Please update the script you're proxying to the latest version of our script.

If you're using [our WordPress plugin](https://plausible.io/wordpress-analytics-plugin) with the built-in proxy enabled, you'll need to:

1.   Disable the proxy
2.   Clear your cache
3.   Re-enable the proxy
4.   Clear your cache again

This ensures the changes are fully applied and the latest version of our script is properly loaded.

Has some other plugin altered our snippet?[​](https://plausible.io/docs/troubleshoot-integration#has-some-other-plugin-altered-our-snippet "Direct link to Has some other plugin altered our snippet?")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Are you using WP Rocket, SiteGround Optimizer or other performance optimization plugins? Or some type of consent banner plugin that determines which scripts can run when? These plugins may affect our tracking as they try to optimize our script. If you're on WordPress, we recommend you use [our official WordPress plugin](https://plausible.io/wordpress-analytics-plugin) to avoid these issues as we've built-in resolutions to the most common plugin conflicts.

Do you experience an issue even when using our plugin? Do check your integration manually using the steps below to identify which plugin is in question. Then please whitelist our script location and our domain name in the settings of the individual plugin to stop it from altering our snippet.

Are you using Cookiebot or a similar consent management platform? Have you set the Plausible script to load only after the user gives the consent? Our testing tool cannot verify the integration in that case so please do use [our manual verification process instead](https://plausible.io/docs/troubleshoot-integration#how-to-manually-check-your-integration).

Plausible is built to be privacy-first and compliant with various privacy regulations so do raise this with your legal team as they could provide the green light to not require user consent. See more details in [our data policy](https://plausible.io/data-policy) and in [this legal assessment written by a data protection lawyer](https://plausible.io/blog/legal-assessment-gdpr-eprivacy).

Is your website on a different URL than the one you added?[​](https://plausible.io/docs/troubleshoot-integration#is-your-website-on-a-different-url-than-the-one-you-added "Direct link to Is your website on a different URL than the one you added?")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Our testing tool visits the exact URL that you added to your Plausible account. For example, if you added `yourdomain.com` as your site, the tool will try to visit `yourdomain.com` directly.

If your website is at a different address, the verification tool will let you enter another URL manually. If the URL you added doesn’t work or doesn’t point to your actual site, the tool won’t be able to reach it or verify your integration. In that case, please use [our manual verification process instead](https://plausible.io/docs/troubleshoot-integration#how-to-manually-check-your-integration).

Are you blocking our script or using a VPN that blocks us?[​](https://plausible.io/docs/troubleshoot-integration#are-you-blocking-our-script-or-using-a-vpn-that-blocks-us "Direct link to Are you blocking our script or using a VPN that blocks us?")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Are you blocking our script from your own device? Or perhaps using a VPN that is blocking scripts? If you are running a browser extension or another service that may be blocking our script, your own visits may not be recorded. Do disable extensions such as adblockers or whitelist our script within the settings of the extension you are using to start counting your own visits too.

Using WordPress and integrated Plausible using our official WordPress plugin? Our plugin excludes logged-in admin visits by default which is why you may not see your own visits being recorded in the dashboard.

If the verification tool has confirmed that the tracking is working fine, then you have nothing to worry about. If you'd like to track those who use adblockers too, take a look at [our proxy solution](https://plausible.io/docs/proxy/introduction).

I don't see my own referral source[​](https://plausible.io/docs/troubleshoot-integration#i-dont-see-my-own-referral-source "Direct link to I don't see my own referral source")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

All referral sources are counted only when they start a new session on your site. This is why you don't see all your own referral sources if you for instance click to test several different UTM tagged links at the same time. Only the first one appears in the "**Top Sources**" report. You would need to start a new session (such as by waiting 30 minutes or using a different device, browser or IP address) to have the subsequent sources counted too.

This same mechanism is what keeps payment gateways and other external domains out of your referral sources. [Learn more about how referral attribution works](https://plausible.io/docs/top-referrers).

How to manually check your integration[​](https://plausible.io/docs/troubleshoot-integration#how-to-manually-check-your-integration "Direct link to How to manually check your integration")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
