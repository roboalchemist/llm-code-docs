# Source: https://documentation.mailgun.com/docs/inboxready/onboarding-ir.md

# Mailgun Optimize APIs Overview

Mailgun Optimize by Sinch is a suite of deliverability tools and services that help take the complexity out of email deliverability. Here you will find the API's for Mailgun Optimize.

Info
To learn more about Optimize, see our article: [Mailgun Optimize: Introducing the best way to improve email deliverability](https://www.mailgun.com/blog/product/introducing-inboxready/)

Below is a list of Mailgun Optimize APIs and an overview of each. Each of these represents a critical aspect of email deliverability and management, ensuring that your email campaigns achieve maximum reach and effectiveness. You will be able to see the various endpoints for each API by clicking on the dropdown for each API on the left sidebar.

The complete [OpenAPI](https://www.openapis.org/) spec is available here: [Download OAS 3.1 Specification](https://documentation.mailgun.com/babadd35a5313c37aed088feab80bdec/openapi-final.yaml)

## Domains

Manage domains to monitor reputation. Use these APIs to register domains for domain-based reputation monitoring tools such as Bounce Classification, Spam Trap Monitoring, Domain Blocklist Monitoring,and Google Postmaster tools.

## Domain Blocklist Monitoring

Similar to IP blocklist monitoring, this function focuses on keeping an eye on your domainâs presence in blocklists, providing an additional layer of security and reputation management for your email campaigns.

Some of the monitored blocklists include:

- Spamhaus DBL
- URIBL
- SURBL


## Spam Trap Monitoring

Mailgun Optimize identifies and helps you avoid spam traps within your email lists. This feature is essential for maintaining a healthy sender reputation and ensuring that your emails are not flagged as spam.

To learn more about spam traps, read our article,  What are Spam Traps.

## Google Postmaster Tools

Integration with Google Postmaster Tools allows you to gain insights into how your emails are performing within the Gmail ecosystem. This can include data on spam rates, domain reputation, and other metrics relevant to Gmail.

## Bounce Classification

Identify critical bounces sent from Mailgun to quickly and easily identify problems with your sending. Continuing to generate bounces like this will lower your reputation and cause other problems with your sending. Our API classifies these bounces by sending domain and mailbox provider/spam filter. You can pull the logs on an individual bounce to get more details on the specific messages causing these bounces.

## IP Blocklist Monitoring

This feature enables you to monitor IP blocklists, allowing you to take immediate action if your IP is listed. This is crucial for maintaining the integrity of your email campaigns and ensuring consistent deliverability.

Monitored blocklists include:

- SpamCop
- CBL
- Spamhaus SBL
- Spamhaus PBL
- Spamhaus XBL
- Barracuda
- Senderscore BL


## Microsoft SNDS (Smart Network Data Services)

This feature provides data and insights into how your emails are being handled by Microsoftâs email services, like Outlook. This includes information on spam filtering and IP status, helping you optimize for one of the worldâs largest email service providers.

## Inbox Placement

This feature ensures that your emails land in the inbox and not the spam folder. By seed testing your emails, Mailgun Optimize can predict and improve where your emails will appear in various email services, like Gmail, with its tab organization.

### Creating Tests

When creating a test, all requests must contain a `subject` property and one source property (`html` or `url`). All other properties are optional.

### Getting Test Info

When getting test info, the call will return the subject and submission in UNIX timestamp format. It will also contain one to three properties containing any array of clients. The `completed` property shows clients that have completed screenshots uploaded. The `processing` property contains clients which are still processd by our system. The `bounced` property contains clients that were bounced by the destination and cannot be retried.

### Getting Test Results

This returns detailed results for screenshots which include their upload locations, send times, completion times, and information about bounces,if any. The URLS in this call are static and will not change for the duration of your active test (90 days from test creation). Any reprocessing that is done will replace the images in these locations. The image locations are generated progammatically before the screenshots are complete. This means that the presence of the URL in the call is not a guarantee that the file will be present. Use the `status` property to determine whenther or not the file is present in the location, ot ou can manually test the URL provided. If the file is not present, you will receieve a 403 Forbidden response from the endpoint.

### Reprocess Screenshots

Sometimes strange things happen on the internet. If a strange result has come back in your screenshot, use this function to tell us to retake screenshots free of charge.

The request should contain and object with a property of `clients` that contains a list of clients in the `TEST_ID` provided. The object returned will have a `success` value indicating if the attemp was successful. If it is false, there will be a `reason` value describing the failure.

For more on Blocklist Monitoring, see the article, How to Setup Blocklist Monitoring.

## Alerts

Mailgun Optimize provides alerts that notify you of critical issues with your email program, such as blocklistings or other factors that could impact your email deliverability. This enables you to act swiftly to resolve issues.

## Email Health Score

The Email Health Score API provides health scores for the overall account, as well as by domain, IP, and subaccount.
Think of your email health score as the email equivalent of a credit score, assessing your email program's health and IP reputation. Ranging from 0 to 100, it indicates the quality of your sender reputation and reflects how mailbox providers perceive you IP address and domain.