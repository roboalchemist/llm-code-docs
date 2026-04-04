# Source: https://www.aptible.com/docs/how-to-guides/app-guides/use-domain-apex-with-endpoints/domain-apex-redirect.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.aptible.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Domain Apex Redirect

The general idea behind setting up a redirection is to sidestep your domain apex entirely and redirect your users transparently to a subdomain, from which you will be able to create a CNAME to an Aptible [Endpoint Hostname](/core-concepts/apps/connecting-to-apps/app-endpoints/custom-domain#endpoint-hostname).

Most customers often choose to use a subdomain such as www or app for this purpose.

To set up a redirection from your domain apex to a subdomain, we strongly recommend using a combination of AWS S3, AWS CloudFront, and AWS Certificate Manager. Using these three services, you can set up a redirection that is easy to set up and requires absolutely no maintenance going forward.

To make things easier for you, Aptible provides detailed instructions to set this up, including a CloudFormation template that will automate all the heavy lifting for you.

To use this template, review the instructions here: [How do I set up an apex redirect using Amazon AWS](/how-to-guides/app-guides/use-domain-apex-with-endpoints/aws-domain-apex-redirect).
