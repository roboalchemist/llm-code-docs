# Source: https://doc.keepnetlabs.com/next-generation-product/miscellaneous/allow-listing/allow-listing-the-pictures-on-microsoft-outlook-apps.md

# Allow Listing the Pictures on Microsoft Outlook Apps

This document provides information about images to be loaded automatically when a user opens the email sent by the platform in **Outlook Application**. This setting will remove the (X) looks on images in **Outlook App** and load the image automatically after the user opens the email.

## **Why does "X" appear on** Microsoft Emails?

When you send an email to your users, the platform places a user-invisible image with a height and width of 1px at the bottom of the email to see if the email is read by the target user (sometimes called a tracking pixel). This is a very common practice for modern digital marketing campaigns. However, many email services automatically block images, therefore resulting in the "Red X". If the user downloads the image, a request is sent to the address where the picture was is originated from. Thus, our portal can report whether the email has been read or not, provided the user 'downloads' or 'opens' the picture.

[Mailchimp](https://mailchimp.com/help/about-open-tracking/), [Sendgrid](https://docs.sendgrid.com/ui/account-and-settings/tracking), and other big email marketing products also send emails using this method, use these tracking pixels to confirm that the email is opened/read by the recipient. No other method has yet been developed technologically to understand whether or not the user has read the email.

Microsoft prevents the images in the email from being displayed directly to the users on its email products and applications (Outlook Desktop only). Because in real life, cyber attackers can use this same method to find out whether or not the target users are active email users and get their user-agent and IP information.

On Google GSuite products though, images are displayed directly, but while they are displayed, Google executes these processes through a proxy server for images. In this way, the real IP and user-agent information of the user are not disclosed.

## How to Prevent "X" from Appearing on Emails in Outlook App?

You can use the "Safe Sender List" feature of the Outlook App to trust the sender and let the Outlook App load images automatically on emails that are delivered from the sender.

Please click [here](https://support.microsoft.com/en-us/office/add-recipients-of-my-email-messages-to-the-safe-senders-list-be1baea0-beab-4a30-b968-9004332336ce) to go Microsoft document that explains this feature. This setting also must be made available to all users via [group policy](https://support.microsoft.com/en-us/topic/how-to-deploy-junk-email-settings-such-as-the-safe-senders-list-by-using-group-policy-d17e49fb-af72-c796-6295-4da6d89ef5fa). Applying this policy before sending [phishing simulations](https://keepnetlabs.com/products/phishing-simulator) or training campaigns loads the images automatically in the emails.

## FAQ

### Q: Is it possible to load images automatically when a user opens the email sent by the platform in Outlook App?

A: Outlook Application [by default](https://support.microsoft.com/en-us/office/block-or-unblock-automatic-picture-downloads-in-email-messages-15e08854-6808-49b1-9a0a-50b81f2d617a) blocks the images in the email that is delivered from outside of your network to be loaded automatically for privacy and security reasons. The Safe Sender List is the only option that let you trust the email sender to load images automatically after you click on the email to read.
