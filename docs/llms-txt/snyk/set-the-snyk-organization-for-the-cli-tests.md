# Source: https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/snyk-cli-for-snyk-code/set-the-snyk-organization-for-the-cli-tests.md

# Set the Snyk Organization for CLI tests

If you have several Organizations in your Snyk account, before you test your code using the CLI, specify which Snyk Organization will be used for the test count.

You can find your available CLI test count on the Organization **Settings** page > **Plan and billing** > **Usage** tab > **Test Usage** section > **Snyk Code** field:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-75910f5314c411e200bff4bdca0ed754de7fb979%2Fplan_and_billing_test_usage.png?alt=media" alt=""><figcaption><p>Snyk Code test usage</p></figcaption></figure>

By default, the CLI runs tests under your **Preferred Organization**, as defined in your **Account settings:**

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-19063dcf7423e3ba30c843bb498ed9d8f8342576%2Fset_snyk_org_CLI_tests_account_settings.png?alt=media" alt=""><figcaption><p>Preferred Organization in Snyk Account settings</p></figcaption></figure>

You can [change your **Preferred Organization**](https://docs.snyk.io/snyk-platform-administration/groups-and-organizations/organizations/create-and-delete-organizations) or set another Organization for the CLI tests via the CLI.

When setting an Organization for the CLI tests, you have two options:

* [Set the default Organization globally for CLI tests](#set-the-default-organization-globally-for-cli-tests)
* [Set an Organization locally for a specific CLI test](#set-an-organization-locally-for-a-specific-cli-test)

## Find Snyk ID and internal name of an Organization

When setting an Organization for the CLI tests, you can use either the Organization ID or the Organization internal name. These Organization identification details are generated automatically by Snyk for each Organization when it is created. The value you select to enter in the command will be shown as the **Organization** name in the test results. You can find the Snyk ID and internal name on the **Settings** page of the Organization on the Web UI.

Follow these steps to find an Organization ID and internal name:

1\. On the Snyk Web UI, open the Organization whose details you want to find:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-54aa4ad6696bd6b9981074f9adb33cb255f15003%2Fsnyk-org-switcher.png?alt=media" alt="Open an Organization to find its details"><figcaption><p>Open an Organization to find its details</p></figcaption></figure>

2\. Once the selected Organization is open, click the **Org Settings.**

3\. On the **Settings** page of the Organization, select the **General** tab to find the following:

* **Internal name:** stated in the **Organization name** section.
  * You can change the display name of an Organization, but not the internal name.
  * The internal name also appears in the URL of the Organization.
  * When using the internal name for setting the Organization for the CLI tests, copy the name from the **Settings** page. The internal name is always written in lowercase letters.
* **ID:** appears in the **Organization ID** section. You can use the **Copy** button to copy the ID to the CLI.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-eb156ae9ff6c419149c74fc89679e997d953d78c%2Fsettings_general_org_name_id.png?alt=media" alt=""><figcaption><p>Organization name and ID</p></figcaption></figure>

## Set the default Organization globally for CLI tests

You can set a default Organization globally for all CLI tests via the CLI. This default Organization will override the Organization set as the [preferred Organization](https://docs.snyk.io/snyk-platform-administration/groups-and-organizations/organizations/create-and-delete-organizations). When entering this command, you can use either the [ID or internal name](#find-snyk-id-and-internal-name-of-an-organization) of the new default Organization.

Regardless of the Organization you set as a global default, you can [run specific CLI tests under a different Organization](#set-an-organization-locally-for-a-specific-cli-test).

To set a default Organization for all CLI tests, In the terminal, enter

```
snyk config set org=<ORG_ID_or_ORG_INTERNAL_NAME>
```

You receive the following confirmation:

```
org updated
```

From now on, all your CLI tests will run under the specified Organization.

For example, to set the Snyk Demo Org as the default Organization for the CLI tests, use the Organization ID and enter:

```
snyk config set org=a7708807-3881-xxxx-xxxx-xxxxxxxxxxxx
```

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-16c2dee152e7ae5482770bb648b734ee690b3ad1%2FSnyk%20Code%20-%20CLI%20-%20Org%20-%20Setting%20global%20default.png?alt=media&#x26;token=ea33a6c6-d703-4476-aaa5-b014f9f4783b" alt="Command to set Organization and confirmation"><figcaption><p>Command to set Organization and confirmation</p></figcaption></figure>

From now on, all the CLI tests will run by default under the Snyk Demo Org Organization, and the Snyk Demo Org ID will appear in the test results:

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-5f47aefdee7c4e67c085fe244f7e2a860ddb6055%2FSnyk%20Code%20-%20CLI%20-%20Organization%20-%20Global%20Settings%20-%20Results%20-%202.png?alt=media" alt="Snyk Demo Org ID in test results"><figcaption><p>Snyk Demo Org ID in test results</p></figcaption></figure>

## Set an Organization locally for a specific CLI test

You can run a specific CLI test under a different Organization from the default. When using this option, the specified Organization will override the default Organization in a specific CLI test. You can use either the [ID or internal name of the Organization](#find-snyk-id-and-internal-name-of-an-organization) to run a command.

To set an Organization for a specific CLI test in the terminal, after the `test` command enter:

```
--org=<ORG_ID_or_ORG_INTERNAL_NAME>
```

For example, to set the Snyk Test Org as the Organization for a specific CLI test, we use the Organization internal name and enter:

```
snyk code test --org=snyk-xxxx-xxx 
```

The internal name of the Snyk Test Org Organization appears in the results of this test:

![Organization internal name in test results](https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-1b4d0b3881de380d3cf44528c6ad2f55944627de%2FSnyk%20Code%20-%20CLI%20-%20Organization%20-%20Specific%20test%20Settings%20-%20Results%20-%202.png?alt=media)
