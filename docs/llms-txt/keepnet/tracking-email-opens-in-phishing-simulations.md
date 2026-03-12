# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/tracking-email-opens-in-phishing-simulations.md

# Tracking Email Opens in Phishing Simulations

Keepnet utilizes a tracking pixel to monitor when users open phishing simulation emails. This tracking pixel is embedded in all phishing simulation emails sent through the platform. When the email is opened, the pixel sends a response to Keepnet, logging the open event.

It is important to note that opening a phishing simulation email is **not** considered a failure and does **not** impact the user’s gamification score. However, phishing emails may be marked as "opened" automatically in the following scenarios:

* **Email Reported:** If a user reports the phishing email using the **Reporter Button**, the email is automatically logged as opened.
* **Phishing Failure:** If a user clicks on a phishing link or opens a malicious attachment within the simulation email, the system will mark the email as opened, even if the tracking pixel does not load.

This tracking mechanism ensures accurate monitoring of user interactions while maintaining fair evaluation criteria in phishing awareness programs.

## Email Opens Not Being Recorded

In some organizations, email client settings prevent images from being automatically downloaded. When this occurs, Keepnet's tracking pixel cannot load, and email opens will not be recorded in phishing simulation reports.

If your organization blocks automatic image downloads, you can enable email open tracking using one of the following methods:

#### Safe Senders List (not recommended) <a href="#h_01hhzbstr3357bgzfne1837nc5" id="h_01hhzbstr3357bgzfne1837nc5"></a>

You can add phishing email senders to a safe senders list to allow all email images to load. This method is not recommended for the following reasons:

* There is a limit to the number of safe senders you can add, and Keepnet sends simulations from many different email addresses. Our phishing simulation email addresses are also subject to change without notice.
* Your users may be able to identify phishing simulation emails due to all of the images loading, while other external, non-Keepnet emails would not load images.

#### Trusted Zone in Outlook (recommended) <a href="#h_01hhzbvxf62d5r1rnb2jmpyk5g" id="h_01hhzbvxf62d5r1rnb2jmpyk5g"></a>

You can create a Group Policy Object in Active Directory to update the Trusted Zone in Outlook to allow tracking pixels to load without allowing all other phishing simulation email images to load. The steps to complete this are detailed below:

1. Navigate to your **Local Group Policy Editor**.
2. You will find the correct Group Policy to edit by navigating to **User Configuration** > **Windows Settings** > **Administrative Templates** > **Windows Components** > **Internet Explorer** > **Internet Control Panel** > **Security Page**.
3. Double-click the **Site to Zone Assignment List** policy to modify the policy.
4. Enable the policy by selecting the **Enabled** option.
5. Under the **Options** area, click **Show**.
6. From the **Show Contents** window, enter the phish link domain used in your test in the **Value Name**. You can also use wildcards in your entry to indicate a phish link subdomain.
   * For a complete list of phish link domains, navigate to the **Phishing** > **Settings** > **Domains** tab in the Keepnet Platform.
7. For the **Value**, enter "2", which corresponds to "Trusted Zone".
8. Click **OK**.
9. Navigate to **Outlook**.
10. Select **Options** > **Trust Center** > **Trust Center Settings**. Click the check mark to **Allow downloads from Websites in this security zone: Trust Zone**.

We recommend sending a phishing test campaign to yourself once these settings are saved so you can ensure opens are being tracked successfully.
