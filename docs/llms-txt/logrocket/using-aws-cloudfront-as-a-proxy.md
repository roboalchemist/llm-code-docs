# Source: https://docs.logrocket.com/docs/using-aws-cloudfront-as-a-proxy.md

# Using AWS CloudFront as a proxy for LogRocket

AWS CloudFront is a LogRocket tested and supported proxy solution if you want to route data through an endpoint where you control the Domain Names and Certificates and expose LogRocket through the same domains your application already uses.

This documentation covers setting up a proxy in front of our SaaS installation using our provided Terraform.

## Setting up CloudFront

We require a custom CloudFront Policy and multiple Behaviors to route so we provide terraform to stand up your CloudFront.  If you want to do this manually, you will need to follow the multiple behaviors defined in the Terraform.  Our Terraform is considered the source of truth for configuration.

### Downloading Terraform

Our terraform is [available for download](https://storage.googleapis.com/logrocket-terraform/terraform-cloudfront-saas-proxy.zip) and will create the needed resources.

```
terraform init
terraform plan
terraform apply
```

### Testing your CloudFront Distribution

If you visit the URL of your CloudFront distribution with a trailing `/i` on the URL (So `https://yourdistribution.cloudfront.net/i` you should get an error message  "Invalid AppID"

If you need support configuring this, please include configuration data about your CloudFront Distribution - you can grab it as a YAML file with `aws cloudfront get-distribution --id <your distribution's ID>`

### Using your Custom Domain Name

AWS has thorough documentation for [Alternate Domains](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-procedures.html) which allows you to configure your desired hostname and TLS.  This can be done manually after you create the CloudFront distribution.  We do not provide terraform for configuring the ACM because there are many ways to do that and AWS provides a smoother option.

You do not need to do this, you can use a cloudfront endpoint for both ingestion and loading the SDK, but for the smoothest setup, you should make the proxy available on the same domain as your application.

If you use an Alternate Domain, follow the directions below but replace "your.cloudfront.net" with the Alternate Domain you have chosen.

## Configuring your web SDK to use CloudFront

### Script Tag

If you look at Project Setup under Settings in your LogRocket dashboard, you will set this up very similarly, but need to specify the CloudFront URL in one extra place.

Update your app to point fully at CloudFront - this changes where you download `LogRocket.min.js` from and updates the `ingestServer`.  If you copy the example below, you'll need to update all three of the CloudFront URLs and the appid to match your setup.

```
<script>window._lrAsyncScript = "https://your.cloudfront.net/logger.min.js"</script>
<script src="https://your.cloudfront.net/LogRocket.min.js" crossorigin="anonymous"></script>
<script>window.LogRocket && window.LogRocket.init('your/appid', { ingestServer: 'https://yourcloudfront.cloudfront.net'});</script>
```

### NPM

You must require and call logrocket's setup function before calling LogRocket.init - if you do not do this, LogRocket will default to the standard SaaS SDK and Ingestion servers.

Make sure you update to point to your CloudFront URL and AppID.

```
import setup from 'logrocket/setup';
const LogRocket = setup({
  sdkServer: 'https://your.cloudfront.net',
  ingestServer: 'https://your.cloudfront.net'
});
LogRocket.init('your/appid');
```

### Content Security Policy (CSP)

If you use a CSP you will need to allow your CloudFront domain or Custom Domain Name

```
Content-Security-Policy: child-src 'self' blob:; worker-src 'self' blob:; script-src 'self' https://your.cloudfront.net; connect-src https://your.cloudfront.net
```

Note that the [worker-src](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/worker-src) CSP directive wasn't supported in Safari or mobile Safari [before 15.5](https://developer.apple.com/documentation/safari-release-notes/safari-15_5-release-notes#Content-Security-Policy) and shouldn't be used in those older browsers. Using it anyway might prevent LogRocket from running and may prevent you from recording sessions in those browsers.