# Source: https://developers.smtp2go.com/docs/report-on-email-delivery.md

# Bounce Report & Statistics

Quickly retrieve statistics to help monitor your deliverability

One of the most important metrics used to rate the reputation of an SMTP2GO account is the Bounce Rate. Via the SMTP2GO API, you can quickly retrieve statistics to help monitor your deliverability, including bounce rate, and much more.

In this guide, we set up a simple request to retrieve a Bounce Rate report.

## Understanding Bounce Rate

The 'Bounce Rate' shown in the SMTP2GO App is the percentage of emails sent in the last 30 days that have bounced back; it includes both soft and hard bounces.

> 📘 Soft vs Hard Bounce
>
> A **soft bounce** could be due to an email being rejected by a recipient's mail server due to content it suspects is spam.
>
> A **hard bounce** is a permanent error, and could be due to a typo/mistake in the recipient's email address, or their email address no longer being valid.

Aim to have a bounce rate below 8%. Anything higher usually indicates a problem with your mailing list: it could be out-of-date, or you may be trying to use a mailing list that isn't in accordance with our [Terms of Service](https://www.smtp2go.com/terms/).

We rate a 0 to 8% rate as Good; a 8% to 12% rate as Fair (a little too high); and a rate above 12% as Poor (too high).

## Reporting Bounce Rates

Whilst the “Reports” section of your SMTP2GO Dashboard features one, streamlined activity report, the same data can be retrieved with the API.

Using the [/stats/email\_bounces](https://developers.smtp2go.com/reference/email-bounces) endpoint we can access statistics on your email bounces for the last 30 days. The API will return the following data:

* emails - Number of emails sent
* rejects - Number of emails rejected
* softbounces - Number of emails soft bounced by receiving mail servers
* hardbounces - Number of emails hard bounced by receiving mail servers
* bounce\_percent - Percentage of email bounces, compared to total emails sent

The /stats/email\_bounces endpoint does not make use of parameters, and requires only a POST with authentication and headers.

**Set up your headers.**

Be sure to include the content type and your API Key in your header, and all requests going forward.

**Examples use cURL language**

Though this guide uses cURL for examples, a wide number of options from *C++*, to *Javascript, Node* and more can be accessed throughout our API Reference Documentation.

```curl
curl --request POST \
     --url https://api.smtp2go.com/v3/stats/email_bounces \
     --header 'Content-Type: application/json' \
     --header 'X-Smtp2go-Api-Key: api-xxxxxxxxxxxx' \
     --header 'accept: application/json'
```

Responses will follow

> 👍 Success!
>
> Look out for a 200 OK response

Similar to the below:

```
{
  "request_id": "ee9b9484-63eb-11ed-8da7-f23c9216ce11",
  "data": {
    "emails": 1000,
    "rejects": 0,
    "softbounces": 5,
    "hardbounces": 5,
    "bounce_percent": "1.00"
  }
}
```

Any error responses will include an error code and explanatory string, similar to the below:

```curl
{
  "request_id": "22e5acba-43bf-11e6-ae42-408d5cce2644",
  "data": {
    "error": "You do not have permission to access this API endpoint",
    "error_code": "E_ApiResponseCodes.ENDPOINT_PERMISSION_DENIED"
  }
}
```

## A range of other reports

As well as the Bounce report, a number of other statistics can be retrieved through the API. These include:

**Email Cycle**
This report will give you statistics on the SMTP2GO account. Data includes the maximum number of emails you can send during this monthly email cycle, based on your plan's monthly allowance, and the number of emails you have sent during this monthly email cycle.

**Email History**
This report will give you a summary of emails sent during a specified date range, per sender email address or SMTP username. The API will return the number of emails sent from the specified email address, the last IP used to send an email from the specified address, and more.

**Email Spam**
This report will give you a summary of how receiving mail servers handled your emails. Data includes the number of emails marked as 'Spam' by receiving email servers, the number of emails rejected by receiving email servers and a percentage of emails marked as 'Spam' by receiving email servers, compared to the total emails sent.

**Email Unsubscribes**
This report will give you a summary of how many recipients unsubscribed from emails that you sent.

**Email Summary**
This report will give you a summary of all other reports. The API will return bounces, spam counts, unsubscribes and more.