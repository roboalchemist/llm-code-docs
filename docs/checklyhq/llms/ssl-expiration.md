# Source: https://checklyhq.com/docs/communicate/alerts/ssl-expiration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# SSL Certificate Expiration Alerts

An expired SSL certificate can cause havoc to sites and APIs. Checkly performs an hourly check on your certificate and can
alert you up to 30 days before your certificate expires. All alert channels (e-mail, SMS, OpsGenie, Webhook etc.) can be used for this alert.

Simply create or pick an existing alert channel that your check subscribes to and enable *SSL certificate expiration* and
set the day threshold to your preference. If you don't have your alert channels set up yet, see [Alert Channels](/communicate/alerts/channels).

<Frame>
    <img src="https://mintcdn.com/checkly-422f444a/riTtJrRZAx73iREC/images/docs/images/alerting/ssl_check_example.png?fit=max&auto=format&n=riTtJrRZAx73iREC&q=85&s=d562053234659d68de432dd15d611e0d" alt="Example alert channel form" width="1308" height="646" data-path="images/docs/images/alerting/ssl_check_example.png" />
</Frame>

Some tips on using SSL alerts

* You can create specific alert channels for certificate expirations and subscribe all checks/groups to that channel.
* You can create multiple alert channels with different thresholds if you want to be alerted at multiple thresholds.

## API checks

The domain for the certificate is parsed from the `URL` in the HTTP request settings so it does not require any setup.

When you update your check's URL or your SSL cert, allow up to an hour for the SSL expiration date to update on Checkly’s end.

<Warning>
  When using [environment variables in the URL](/platform/variables#accessing-variables-in-api-checks), make sure that the domain is fully specified.
  SSL monitoring cannot parse the domain from a URL like `{{BASE_URL}}/test-endpoint`, but using environment variables in other parts of the URL like `https://checklyhq.com/{{TEST_PATH}}` works.
</Warning>

### Getting `Error: unable to verify the first certificate`

If prompted with this error, the usual cause is the certificate chain of the given website being incomplete. This will
not happen with a browser check, because the browser will complete the certificate chain on its own. When running an API check,
though, no browser is involved - therefore the error takes place. You can use an online SSL checker
(e.g.: [SSL Shopper](https://www.sslshopper.com/ssl-checker.html)) to help you diagnose issues with your certificate.

## Browser checks

Since browser checks can connect to multiple domains, you need to set the SSL certificate domain to receive certificate alerts for them.

When you change this setting or update your SSL cert, allow up to an hour for the SSL expiration date to update on Checkly’s end.

<img src="https://mintcdn.com/checkly-422f444a/riTtJrRZAx73iREC/images/docs/images/alerting/browser_ssl_check.png?fit=max&auto=format&n=riTtJrRZAx73iREC&q=85&s=10ee8a5bbe8f5226425ad79391c30a8f" alt="SSL checks for browser checks" width="2404" height="715" data-path="images/docs/images/alerting/browser_ssl_check.png" />


Built with [Mintlify](https://mintlify.com).