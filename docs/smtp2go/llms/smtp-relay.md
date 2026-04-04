# Source: https://developers.smtp2go.com/docs/smtp-relay.md

# SMTP Relay

A common way to integrate SMTP2GO into your software or application is by using Simple Mail Transfer Protocol (SMTP).

## The requirements to send using SMTP

In your SMTP2GO account, you will need to ensure you have [verified your senders](https://support.smtp2go.com/hc/en-gb/articles/9150216032537-Verified-Senders-Sender-Domain-vs-Single-Sender-Emails) on the "Sending > [Verified Senders](https://support.smtp2go.com/hc/en-gb/articles/115004408567-Verified-Senders)"  section and you've created an [SMTP User](https://support.smtp2go.com/hc/en-gb/articles/13645646122777-SMTP-Users) (username and password) for authentication to our servers on the "Sending > [SMTP Users](https://support.smtp2go.com/hc/en-gb/articles/13645646122777-SMTP-Users)" section. Verifying your senders and adding SMTP Users can alternatively be handled via the API.

Then, simply set our SMTP server details as the outgoing server in your sending software or application. Moving forward, SMTP2GO will handle the delivery and you'll have access to real-time reporting, statistics and further features/settings in the App or by utilizing the API.

## SMTP Settings

**Server:**\
mail.smtp2go.com

**Port:**\
TLS (*or no encryption*): available on 25, 2525, 8025, 587 and 80.\
SSL: available on ports 465, 8465 and 443.

**Username and Password:**\
Required by default. A combination from your account's "Sending > [SMTP Users](https://support.smtp2go.com/hc/en-gb/articles/13645646122777-SMTP-Users)" section.\
SMTP Users can be added and managed using the [API](https://developers.smtp2go.com/reference/add-an-smtp-user).

## Further specific settings:

* USA (mail-us.smtp2go.com), EU/UK (mail-eu.smtp2go.com), EU only (mail-eu2.smtp2go.com) and Australian (mail-au.smtp2go.com) customers may be interested in our [Location Specific Services](https://support.smtp2go.com/hc/en-gb/articles/4741818447129-Location-Specific-Services).
* If your software does not allow you to enter a username and password for authentication, view our [Alternatives to SMTP Authentication](https://support.smtp2go.com/hc/en-gb/articles/223087467-Alternatives-to-SMTP-Authentication) article covering IP Authentication and Address Authentication (available to paid plans).
* If your software requires an IP address to connect to instead of the hostnames we offer, please see our available IPs listed in the [Connecting to an IP Address](https://support.smtp2go.com/hc/en-gb/articles/223087667-Connecting-to-an-IP-Address) article.

## Setup Guides

We have a range of [common setup guides](https://www.smtp2go.com/setupguide/) available to help you get set up.\
If there's not a guide for your software or application and you need assistance, our [support team](https://www.smtp2go.com/contact/) can help to advise further.

Our [Common Sending Errors](https://support.smtp2go.com/hc/en-gb/articles/13990494697369-Common-Sending-Errors) article covers common errors encountered when trying to send and how to resolve them. If you encounter connection issues or timeouts, check our [troubleshooting](https://support.smtp2go.com/hc/en-gb/articles/12813014000921-Troubleshooting-Connection-Issues) article for options to try and help investigate.

## Points to note

* The [maximum email size](https://support.smtp2go.com/hc/en-gb/articles/223087547-Maximum-Attachment-Size) (including attachments) when sending via SMTP is 50 MB.
* The [maximum number of recipients per email](https://support.smtp2go.com/hc/en-gb/articles/223087587-Maximum-Number-of-Recipients-Per-Email) (To, CC & BCC) is 400. However, we recommend not exceeding 50-100.
* The default [maximum sending speed](https://support.smtp2go.com/hc/en-gb/articles/223087647-Maximum-Sending-Speed) is 200,000 emails per hour.
* We allow up to 40 simultaneous SMTP connections and up to 5,000 emails per connection.
* Email Templates are only supported when sending via our API.
* Inbound IPs can be found [here](https://support.smtp2go.com/hc/en-gb/articles/227835308-Worldwide-Server-Locations-IP-Addresses-and-Email-Routing) and outbound IPs [here](https://support.smtp2go.com/hc/en-gb/articles/223087327-Allow-List-IP-Addresses-With-Your-Incoming-MX-Server).

## Global Infrastructure

SMTP2GO uses special routing technology which means that wherever in the world you connect to us, you'll connect to the nearest server (geographically speaking) to your location.

For example, if you're in the USA, you'll connect with one of our servers based in the USA. If you're in Europe, you'll connect with one of our servers based in Europe, and if you're in Australia, you'll connect with our servers based in Australia. Customers wishing to only ever connect to USA, Europe or Australia can choose a [location-specific SMTP server name](https://support.smtp2go.com/hc/en-gb/articles/4741818447129).

Connecting to a geographically close server is important as it greatly reduces the overall time to send an email, and can really speed things up if you're sending a large number of emails. We currently have inbound servers in Los Angeles (CA), Fremont (CA), Seattle (WA), Newark (NJ), Frankfurt (Germany), London (UK), Singapore, and Sydney (Australia). We also have data centers in Chicago (IL), Reston (VA), and Amsterdam (the Netherlands), and Sydney (Australia) which securely send emails and store your account information.

If your company wishes to have everything located in the EU, you can request to be placed in our Amsterdam data center. If you sign up from Europe, then your account will automatically be placed there. Similarly, you can request to be placed in our Australian data center (new accounts from Oceania are placed there automatically) or US data centers. To verify that your account is properly configured to process, send, and store data solely in your preferred data center, view our [Verify Data Center and Server Location](https://support.smtp2go.com/hc/en-gb/articles/360005171574) article.

<Image align="center" src="https://files.readme.io/28e222b-Locations.png" />

If you have questions or need assistance getting set up and sending via SMTP, please [contact](https://www.smtp2go.com/contact/) our support team.