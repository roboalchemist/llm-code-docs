# Source: https://docs.curator.interworks.com/site_administration/user_notifications/third_party_cookies.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Third Party Cookies 

> Configure third-party cookie warnings and troubleshoot embedded visualization login issues in Safari browsers.

Embedding visualizations within Curator requires third party cookies to be enabled.  By default Chrome and
Firefox allow this but Safari does not.  When you encounter this issue,
**the embedded visualization (e.g.Tableau) login prompt might continue to appear inside of Curator even after
successfully logging in to Curator**.

## Warning Users About Third-Party Cookie Embedding Issues

Since your Curator users may not be aware this setting is preventing them from being able to use the embedded
view in Curator, you can enable an alert that tells them if this is preventing them from being able to
seamlessly log in to their embedded visualization.  To enable this warning follow the steps below:

1. Navigate to the backend of the system (e.g. `http://curatorexample.com/backend`) and log in if prompted.
2. Navigate to **Settings** > **Curator** > **Portal Settings**.
3. Click on the "Features" tab.
4. Scroll down to the "Usability" section and enable *3rd Party Cookies Enabled Check*.

## Information on How to Enable Third-Party Cookies

See the steps here to allow cookies on devices that use Safari:

* [Unblocking cookies on iOS](https://support.apple.com/en-us/HT201265)
* [Unblocking cookies on MacOS](https://support.apple.com/guide/safari/manage-cookies-and-website-data-sfri11471/mac)
