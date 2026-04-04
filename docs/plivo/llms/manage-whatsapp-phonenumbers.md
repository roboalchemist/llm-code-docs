# Source: https://plivo.com/docs/messaging/concepts/whatsapp/manage-whatsapp-phonenumbers.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Business Phone Numbers

> Add, configure, and manage WhatsApp Business phone numbers via console

You can configure your phone numbers by clicking on Whatsapp > Whatsapp business account > Click on the account you have already linked > Configurations > Right below account details you would see ‘+Add Phone Number’ button >once added, you may see the ‘Unlink Number’ option below the ‘+Add Phone Number’ Button as shown in below image on the [Plivo console](https://cx.plivo.com/whatsapp/numbers) and from [Meta’s WhatsApp Manager](https://business.facebook.com/wa/manage/phone-numbers/?).

## Via the console

On the console, navigate to whatsapp > whatsapp\_business\_account. The first tab, Configuration, lets you view all the phone numbers that are linked to your WABA along with their status, name status, and quality rating.

<Frame>
    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/phone1.jpg?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=d354bd8d042b917f9f92a70232cc9060" alt="" width="1021" height="600" data-path="images/phone1.jpg" />
</Frame>

Status may be *connected*, *pending*, or *disconnected*. You can send messages from a phone number only if it is in *connected* status.

Name status provides the latest feedback from Meta on the display name’s verification status against this phone number. You can manage name status from [Meta WhatsApp Manager](https://business.facebook.com/wa/manage/phone-numbers/?).

Quality rating indicates the [quality feedback](https://developers.facebook.com/docs/whatsapp/messaging-limits) for your phone number depending on feedback provided by the recipients. The possible quality rating values are Green (High Quality), Yellow (Medium Quality), and Red (Low Quality). You can also request a review of your phone number for a WhatsApp Official Business Account (OBA). For more information about this process and the qualification criteria, please refer [here](https://developers.facebook.com/docs/whatsapp/overview/business-accounts#official)

### Unlinking a number

You can unlink a number from the [Plivo console](https://cx.plivo.com/whatsapp/numbers) to deregister the number with Plivo. Go to the console and select WhatsApp -> WhatsApp Business Accounts -> 'Select a WABA and view configuration is done here’. When you deregister a number, its status is listed as

`Disconnected`

and you will not be able to send messages with the number going forward.

## Via Meta WhatsApp Manager

You can also manage your numbers from [Meta WhatsApp Manager](https://business.facebook.com/wa/manage/phone-numbers/?).

<Frame>
    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/phone2.jpg?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=a41e79238e833bc0dde945ea7138d377" alt="" width="1649" height="600" data-path="images/phone2.jpg" />
</Frame>

From here, you can view [messaging limits](https://developers.facebook.com/docs/whatsapp/messaging-limits) provisioned for your phone numbers — that is, the maximum number of customers you can reach out to in a day. Meta will automatically increase the limits as your usage increases and if you get consistently good feedback from your customers.

You can configure how your message appears to WhatsApp-enabled recipients by clicking on the gear icon in the *Settings* column for any number.

<Frame>
    <img src="https://mintcdn.com/plivo/-VVFcM3g7XHd8wTl/images/phone3.jpg?fit=max&auto=format&n=-VVFcM3g7XHd8wTl&q=85&s=3d2d119766de67903f263e76e8862c65" alt="" width="1334" height="600" data-path="images/phone3.jpg" />
</Frame>

On this screen, you can configure your business profile picture and request an [official business account](https://developers.facebook.com/docs/whatsapp/overview/business-accounts#official-business-account), which displays with a green checkmark.
