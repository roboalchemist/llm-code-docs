# Source: https://docs.snyk.io/snyk-api/using-specific-snyk-apis/webhooks-apis/guides-to-webhooks/how-to-use-snyk-webhooks-to-integrate-new-relic-with-snyk/new-relic-curated-ui-and-snyk-custom-dashboard.md

# New Relic Curated UI and Snyk Custom Dashboard

Once the Azure Function and the Snyk Webhook are created, you see data coming in for Snyk projects with the configured retest frequency, or projects that you scan manually and where Snyk identifies new issues.

## Vulnerability event type

You can look into the Vulnerability event type to validate that data flows into New Relic.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-c7d3fdfa65041b26fadc3d6abd727ad2a3b7b14e%2Fnew-relic-vulnerability-event.png?alt=media" alt="Vulnerability event type"><figcaption><p>Vulnerability event type</p></figcaption></figure>

## New Relic Vulnerability Management

In addition New Relic provides a curated UI, a New Relic app named Vulnerability Management, that you can use to visualize all the issues being sent.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-bdbb2e8f94a0d1fc7b57257f268bcd30463f232a%2Fnew-relic-vulnerability-management-app.png?alt=media" alt="Vulnerability management app"><figcaption><p>Vulnerability management app</p></figcaption></figure>

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-83eb839cb784d30d10356f879c94bdc7acac06fc%2Fnew-relic-vulnerability-management-app-details.png?alt=media" alt="Vulnerability app management details"><figcaption><p>Vulnerability app management details</p></figcaption></figure>

## Snyk quickstart template

The Snyk team has also built a quickstart template that includes a sample custom dashboard to make sure all the data is presented in a Snyk-focused way.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-d3db14dab57153ed725db077605aacca58ddb0a1%2Fnew-relic-snyk-dashboard.png?alt=media" alt="New Relic Snyk dashboard"><figcaption><p>New Relic Snyk dashboard</p></figcaption></figure>
