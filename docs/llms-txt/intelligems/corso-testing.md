# Source: https://docs.intelligems.io/integrations/corso-testing.md

# Corso Testing

## Introduction

Intelligems' [Corso](https://corso.com/corso-shipping-plus/) integration allows merchants to test Corso shipping rate configurations via an Intelligems content test. You can test:

* Shipping Rates - Test the impact of shipping rate modifications on conversion
  * Add additional fees
  * Apply shipping discount
  * Modify which rates are offered
* Test Rate settings - A/B test rate type, price, name, and description combinations

## How It Works

### One time - prepare Corso and Intelligems applications for integration

1. Reach out to Intelligems support [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request) for help enabling the setting that allows Intelligems to add the test group ID.
2. Enable the Intelligems Integration in Corso. Toggling on this integration allows you to select an Intelligems test group id as an automation value. If this setting is not available to you, reach out to Corso to enable it

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-5530f1c451850c4c7102833bfd1e2d90d5da5068%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

### To set up a Corso test:

1. Set up a `Content Test` within the Intelligems app, with the `On-site edits` type (you don’t need to do any modifications and can leave that section blank).
2. Copy the Intelligems test group ids for the test to use within Corso
   1. From the tests page, click the `...` menu of the test, and then click `Show Info`
   2. Copy the Intelligems test group id when settng up a modification in the next step
3. Create rules within Corso to assign Shipping Rate Modification rules per each Intelligems test group ID. If needed, reach out to Corso for further assistance
   1. Set a rule condition using `Intelligems Test Group ID` copied from the Intelligems app in the previous step
   2. Add whichever rate modifications you’d like to use for that test group

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-0907668b2220cde7ccb4cfae96bd20b23fe6ec30%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>
