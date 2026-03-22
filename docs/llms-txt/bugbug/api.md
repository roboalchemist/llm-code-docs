# Source: https://docs.bugbug.io/integrations/api.md

# CLI

## Integrate with CI/CD using BugBug Command Line Interface

You can operate BugBug via the Command Line Interface (CLI). This empowers you to integrate with any continuous integration (CI) or continuous deployment (CD) pipelines or build system hooks.

{% embed url="<https://www.npmjs.com/package/@testrevolution/bugbug-cli>" %}

## Install via NPM

Open your terminal. First of all, you need  [Node.js](https://nodejs.org/en/download/) installed on your machine and [npm](https://www.npmjs.com/get-npm) installed.&#x20;

{% hint style="info" %}
You need Node.js **version 20** **or newer**
{% endhint %}

After you have **NodeJS** and **npm** installed simply run:

```
npm install -g @testrevolution/bugbug-cli
```

Remember that you need to have admin user permissions on NodeJS execution.

## Get your API token

You need to take **the API token** of the project you want to run with CLI. You will find that in the BugBug web app in the Integrations tab from the side menu:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FTLFXZqhMmHCNmsoKoVyt%2FZrzut%20ekranu%202023-03-16%20105458.png?alt=media&#x26;token=3f55bec1-c35d-488d-8025-bc60533db619" alt=""><figcaption><p>The API token for the project</p></figcaption></figure>

Then configure CLI with the project's API token:

```
bugbug config set-token <api-token-from-project-settings>
```

## Run tests from terminal

On BugBug npm's page, you find the available commands. You can also just strike `bugbug help` to see what you can do and how.

Example: list suites within the connected project:

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MKixgeBPbLvnD0l1eiV%2F-MOTTs00Id1fYue98q_t%2F-MOTX5rk6pQWIegiDMU3%2FScreenshot%202020-12-14%20at%2000.55.58.png?alt=media\&token=f4e7b5e3-def1-4f36-b57f-85c6ba7e603a)

To run a particular test via CLI you need to find the ID of the test. It's easy, just go to your test, expand `3 dots`, and select `Run via CLI`. Just simply copy the command for running, open the terminal, and paste and run. The command looks as below:

```
bugbug remote run test <test-id>
```

## Find your suite ID

You can run the whole suite as well by going to `Suites` the tab, expanding the details, and selecting `Run via CLI`. The command is the same but SUITE\_ID is different. That's how we recognize you want to run the whole suite!

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FFzJQlRDUfr2yEyxINkra%2FCLI_1.png?alt=media&#x26;token=d75399bb-8d42-4661-9776-70b7989de2f4" alt=""><figcaption><p>Run in CLI option in the more drop-down menu</p></figcaption></figure>

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FOIMY5rs0NvZWZdeLMc0H%2FCLI_2.png?alt=media&#x26;token=5e3dee99-10a6-4185-9c89-b3ee8a361c3e" alt=""><figcaption><p>Run this suite via CLI modal</p></figcaption></figure>

## Run tests from your build pipeline

Update your CI/CD build scripts to see test results directly in your build management tool *(for example in Bitbucket)*

Here's an example of what you can add to your build script:&#x20;

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FGztFcxAwzJBUTbYVthpv%2Fapi-example-script-safe.png?alt=media\&token=3d51c755-6f68-45d5-b0b3-0377ac78b409)

You can also override individual [variables](https://docs.bugbug.io/editing-tests/variables#intro-to-variables) from the command line with `--variable variableName="customVariableValue"`. This allows you to run different combinations of test data in different environments, for example, you can insert a different user password on prod and a different one on staging.&#x20;

{% hint style="info" %}
**If you're ambitious**&#x20;

Command line variables override allows you to test various combinations of test data. You could create a `for each` type of script and execute a suite with all the combinations.&#x20;
{% endhint %}

When you run your pipeline, BugBug tests would be triggered and your build will only be successful if all tests passed.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0Kxb7lJq47YCFbQKlBPv%2Fpipeline-example-safe.png?alt=media\&token=de42ab99-42b4-4052-8a7a-c3267bf9ea57)

Also read: [our advanced guide to automation testing for startups](https://bugbug.io/blog/software-testing/automation-testing-guide-for-startups-level-3/)

## Available commands list

Here is a list of the commands that may be in use with different options and/or flags:

### **`bugbug help <option>`**

| Options                                                                                        | Flags | Description                            |
| ---------------------------------------------------------------------------------------------- | ----- | -------------------------------------- |
| <ul><li><code>config</code></li><li><code>remote</code></li><li><code>version</code></li></ul> | N/A   | Show help menu for a specific command. |

### **`bugbug config <option>`**

| Options             | Flags | Description                                                                                                   |
| ------------------- | ----- | ------------------------------------------------------------------------------------------------------------- |
| `set-token <token>` | N/A   | <p></p><p>You can use this option for the command to set a valid token from your web app project settings</p> |

### **`bugbug remote <option>`**

| Options                       | Flags                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description                                       |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| `list test`                   | <ul><li><code>--no-wait</code> <br><em>Exit immediately without waiting for the result</em></li><li><code>--no-progress</code><br><em>Don't show progress spinner</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Returns a list of all existing tests              |
| `list suite`                  | <ul><li><code>--no-wait</code> <br><em>Exit immediately without waiting for the result</em></li><li><code>--no-progress</code><br><em>Don't show progress spinner</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Returns a list of all existing test suites        |
| `list profile`                | <ul><li><code>--no-wait</code> <br><em>Exit immediately without waiting for the result</em></li><li><code>--no-progress</code><br><em>Don't show progress spinner</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Returns a list of all existing test profiles      |
| `run test <test-id>`          | <ul><li><code>--no-wait</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--with-details</code><br> <em>Show result with details</em></li><li><code>--profile</code> <br><code>"\<profile-name>"</code><br> <em>Run with a specific, existing profile</em><br></li><li><code>--variable</code> <br><code>"\<variable-name>"</code><br> <em>Override default variable during a single run</em><br></li><li><code>--reporter</code><br> <em>The name of the reporter to use (default: "inline"). Instead of "inline" you can also set "junit" for the report to be exported to an XML file</em><br></li><li><code>--output-path</code><br> <em>The path to save the test report. Relative to the current working directory</em></li></ul> | Runs a specific test based on its ID              |
| `stop test <test-run-id>`     | <ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code><br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--result-timeout \<int></code><br><em>Modify the default result waiting time (minutes, default: 60)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Stop the test run based on its ID                 |
| `run suite <suite-id>`        | <ul><li><code>--no-wait</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--with-details</code><br><em>Show result with details</em></li><li><code>--profile</code> <br><code>"\<profile-name>"</code><br><em>Run with a specific, existing profile</em></li><li><code>--variable</code> <br><code>"\<variable-name>"</code><br><em>Override default variable during a single run</em></li><li><code>--reporter</code><br><em>The name of the reporter to use (default: "inline"). Instead of "inline" you can also set "<strong>junit</strong>" for the report to be exported to an XML file</em></li><li><code>--output-path</code><br><em>The path to save the test report. Relative to the current working directory</em></li></ul> | Runs a specific test suite based on its ID        |
| `stop suite <suite-run-id>`   | <p></p><ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code><br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--result-timeout \<int></code><br><em>Modify the default result waiting time (minutes, default: 60)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Stop the test suite run based on its ID           |
| `status test <test-id>`       | <ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Display the test's status based on a run ID       |
| `status suite <suite-run-id>` | <ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Display the test suite's status based on a run ID |
| `result test <test-run-id>`   | <ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--with-details</code><br><em>Show results with details</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Display the test result based on a run ID         |
| `result suite <test-run-id>`  | <ul><li><code>--no-progress</code><br><em>Exit immediately without waiting for the result</em></li><li><code>--debug</code> <br><em>Show more data</em> <em>(like raw API response)</em></li><li><code>--with-details</code><br><em>Show results with details</em></li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Display the test suite's result based on a run ID |

## Examples of usage

### Check the status of a test run by its ID:

```
bugbug remote status test <test-run-id>
```

**Output:**

```
ℹ Test name: [REG] Popup handling #2 (testRunId: 10a696b2-3ce6-4b45-8b9f-0a0a0abc00000)
✔ Status: passed
```

### Generate a report of a test run by its ID:

{% hint style="info" %}
By default "reporter" option is set to "inline".
{% endhint %}

```
bugbug remote status test <test-run-id> --reporter
```

**Output:**

```
ℹ Test name: Test number 71 (testRunId: ba5e19d8-609d-4529-95f6-0c6179e59614)
✔ Status: passed
```

### Generate a report of a test run by its ID that's exported to a junit format (XML file):

<pre><code><strong>bugbug remote status test &#x3C;test-run-id> --reporter junit
</strong></code></pre>

**Output:**

```
bugbug remote status test <test-run-id> --reporter junit
⠹ Waiting for result...
```

The XML file is automatically exported to your project's main directory:

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FtSdkYPHlyvsjBAec1MTZ%2Fxml-report.png?alt=media&#x26;token=9e8915f3-bfb8-460c-87dd-c5db4951f52d" alt=""><figcaption><p>Preview of a test report exported to an XML file</p></figcaption></figure>

### Execute a test suite by its ID:

<pre><code><strong>bugbug remote run suite &#x3C;test-suite-id>
</strong></code></pre>

**Output:**

```
bugbug remote status suite bceb9701-23d3-4b67-bfb7-a000a000a00
✔ Status: passed
```

### Check test suite run's status:

<pre><code><strong>bugbug remote status suite &#x3C;suite-run-id>
</strong></code></pre>

**Output:**

```
bugbug remote status suite 8de73c22-c8a3-4141-c111-0a0a0a0a0a
✔ Status: passed
```
