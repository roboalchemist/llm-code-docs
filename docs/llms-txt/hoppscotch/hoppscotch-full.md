# Hoppscotch Documentation

Source: https://docs.hoppscotch.io/llms-full.txt

---

# Changelog
Source: https://docs.hoppscotch.io/documentation/changelog

New updates and improvements to Hoppscotch.

* Section moved to [GitHub Releases page](https://github.com/hoppscotch/hoppscotch/releases).


# Hoppscotch CLI
Source: https://docs.hoppscotch.io/documentation/clients/cli/overview

Run tests, manage automated API monitoring, and more.

Hoppscotch gives you multiple ways to interact with and configure your APIs. With the command-line interface (CLI) you can interact with the Hoppscotch platform using a terminal, or through an automated system. This enables you to run API tests, manage automated API monitoring, and more.

This section contains a complete list of all Hoppscotch CLI commands available, alongside their optional parameters for additional behavior. You can also find a complete list of configuration options to configure your APIs through Hoppscotch.

<Info>Hoppscotch CLI is currently in alpha stage. Report a bug by [opening a new issue](https://github.com/hoppscotch/hoppscotch/issues/new/choose).</Info>

## Pre-requisites

Before installing the Hoppscotch CLI, ensure your system meets the following requirements.

<AccordionGroup>
  <Accordion title="Windows & macOS">
    You will need `node-gyp` installed. Thus, follow the instructions from [node-gyp](https://github.com/nodejs/node-gyp).
  </Accordion>

  <Accordion title="Debian / Ubuntu derivatives">
    Execute the following command:

    ```
    sudo apt-get install python g++ build-essential
    ```
  </Accordion>

  <Accordion title="Alpine Linux">
    Execute the following command:

    ```
    sudo apk add python3 make g++
    ```
  </Accordion>

  <Accordion title="Amazon Linux (AMI)">
    Execute the following command:

    ```
    sudo yum install gcc72 gcc72-c++
    ```
  </Accordion>

  <Accordion title="Arch Linux">
    Execute the following command:

    ```
    sudo pacman -S make gcc python
    ```
  </Accordion>

  <Accordion title="RHEL / Fedora derivatives">
    Execute the following command:

    ```
    sudo dnf install python3 make gcc gcc-c++ zlib-devel brotli-devel openssl-devel libuv-devel
    ```
  </Accordion>
</AccordionGroup>

## Installing Hoppscotch CLI

Once the dependencies are installed, install @hoppscotch/cli from npm by running:

```bash theme={null}
npm i -g @hoppscotch/cli
```

<Warning> The **minimum supported Node.js version** for the CLI is now **v22**. If you're on Node.js v20 (EOL in April, 2026), you can continue using CLI `v0.26.0` alongside `v2025.10.1` of the Hoppscotch app. Future CLI versions will require Node.js v22 or higher. </Warning>

## Commands

### `hopp test`

The `hopp test` command allows you to run tests against a Hoppscotch collection file.

* The hopp test command recursively goes through each request in the collection and runs them, validating the responses with the test script provided in each request. Hence, the order of execution is the same as the order specified in the collection structure.
* If upon executing the command, a failed assertion (a failing test case) has occurred, the command will give a non-zero exit code and 0 exit code if all tests have passed.
* Unless there was a network error (for example, DNS resolution errors or network Connectivity Issues), the test script will be running and it is up to the test script to define what happens to error status codes. Non-200 status codes are still considered valid responses for test script execution.

```bash theme={null}
hopp test [-e <environment file>] [-d <delay_in_ms> ] <hoppscotch collection file>
```

### Running Collections present on the API client

The `hopp test` command can also be used to run collections present in your API client on Hoppscotch cloud or self-hosted platforms.
Do note that you need to create a personal access token for your CLI to connect to your API client, and you can not run collections present in your personal workspace.

```bash theme={null}
hopp test  [-e <environment id>] [-d <delay_i_ms>] <hoppscotch collection id> [--token <access_token>] [--server <server url>]
```

<Tip> You can directly copy the command with the auto-populated **Collection ID** and **Environment ID** by navigating to the **“CLI"** tab within the **“Run Collection”** action found in the context menu. </Tip>

### Generate JUnit Report for Collection Runs

The `hopp test` command now has the ability to generate a JUnit Report for collection runs in the CLI. The report is generated as an XML file at the specified path provided in the command. If no path is specified, the report will be saved in the working directory with the default name `hopp-junit-report.xml`.

```bash theme={null}
hopp test <file_path_or_id> --env <file_path_or_id> --reporter-junit [path]
```

#### JUnit Report Format Overview

The JUnit report generated for collection runs provides a structured summary of the test results. The table below provides a detailed breakdown of the JUnit report format, explaining the significance of each XML element:

| Element                       | Description                                                                                                                                                                                                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `<testsuites>`                | Root element representing the entire set of test suites.                                                                                                                                                                                                                                                                 |
| `<testsuite>`                 | Represents a collection of test cases for a specific request.                                                                                                                                                                                                                                                            |
| `<testcase>`                  | Represents an individual test case. It corresponds to `pw.expect()` assertions with the description prefixed by that of the test suite `pw.test()`.  It appears as a direct child of `<testsuite>`.                                                                                                                      |
| `name`                        | Attribute for `<testsuite>` and `<testcase>` elements. For `<testsuite>`, it indicates the hierarchy of collections up to the request. Organized at the request level using the naming convention: `<parent-collection-name>/<child-collection-name>/<request-name>`. While, for `<testcase>`, it'll be the description. |
| `classname`                   | Attribute of `<testcase>` that mirrors the `name` attribute of the parent `<testsuite>`.                                                                                                                                                                                                                                 |
| `<failure>`                   | Indicates an assertion failure within a `<testcase>`. Includes `type` and `message` attributes describing the failure.                                                                                                                                                                                                   |
| `<error>`                     | Indicates an error during assertion within a `<testcase>`. Includes `message` attribute describing the error.                                                                                                                                                                                                            |
| `<system-err>`                | Represents errors reported at the request level (e.g., invalid URL, reference error in the test script).  These errors are detailed within a `CDATA` section, with each error separated by newlines to ensure each issue is clearly identified.                                                                          |
| `time`                        | Attribute of `<testsuite>` that shows the execution time for the test cases (excluding request execution time). The total time is at the root `<testsuites>`.                                                                                                                                                            |
| `timestamp`                   | Attribute of `<testsuite>` that records the execution date and time in ISO string format.                                                                                                                                                                                                                                |
| `tests`, `failures`, `errors` | Attributes of `<testsuite>` and `<testsuites>` that track the number of test cases, failed cases, and errors, at the request level and effective count at the root level test suite respectively. Set to `0` at a request level test suite, if errors halt further execution.                                            |

### Arguments

* `hoppscotch collection id` : Each collection created in a Hoppscotch workspace is given a unique identifier known as the Collection ID. Collection IDs for each collection can be found under **“Details”** tab inside Collection **“Properties”**.

* `environment id` : Similar to Collection IDs, each environment created in a Hoppscotch workspace is assigned a unique identifier known as the Environment ID.

* `delay_i_ms` : Represents a time interval (in milliseconds) to pause execution of API requests before within a collection.

* `access token` : It is a secure, unique identifier used to authenticate a user's access to their Hoppscotch account and its resources like collections, environments data. [Learn more about personal access tokens](/documentation/features/pat)

* `server url` : This optional and is the URL of your self-hosted instance when you're self-hosting your API client

* `path` : Accounts for a file path where the JUnit report will be saved as an XML file in your file system.

* `no_of_iterations`: Indicates the number of iterations to run the collection. Each iteration will run the entire collection once, replacing any iteration-specific data defined by the `--iteration-data` flag (if provided).

  ```bash theme={null}
  hopp test <hoppscotch_collection_file_or_id> [--iteration-count <no_of_iterations>] [--iteration-data <file_path>]
  ```

* `file_path`: The path to the CSV file for iteration data. This file should follow the format:

  ```
  key1,key2,key3
  value1,value2,value3
  value4,value5,value6
  ```

  Each row in the CSV corresponds to an iteration, and the values from that row will replace the respective environment variables during the iteration. For example:

  * **Iteration 1:** The values value1, value2, and value3 will be used.
  * **Iteration 2:** The values value4, value5, and value6 will be used.

### Example

```bash theme={null}
hopp test kitchen-sink-hoppscotch-collection.json
hopp test -e environment.json kitchen-sink-hoppscotch-collection.json
hopp test -e environment.json -d 1000 kitchen-sink-hoppscotch-collection.json
hopp test clxsntdgh0000lcx9fnits2h8 --token <access token> 
hopp test -e clxspay2r0006lcx99aqgjbay -d 1000 clxsntdgh0000lcx9fnits2h8 --token <access token> --server http://localhost:3170
hopp test -e environment.json kitchen-sink-hoppscotch-collection.json --reporter-junit kitchen-sink-junit.xml
hopp test kitchen-sink-hoppscotch-collection.json --iteration-count 3 --iteration-data /path/to/iteration-data.csv
```

## Environment

Hoppscotch allows templates in several places. For example, you could specify your endpoint URL as `<<baseurl>>/post` and specify baseurl as [`https://echo.hoppscotch.io`](https://echo.hoppscotch.io) in an environment file.

Hoppscotch CLI supports environment files in two specific formats:

### 1. Single Environment Entry Export Format

This format is generated by Hoppscotch App when you export any of your environment. It includes a named environment (name) with key-value pairs, allowing you to define various variables within a single file.

```json theme={null}
{
  "name": "my_env",
  "variables": [
    {
      "key": "base_url",
      "value": "https://echo.hoppscotch.io"
    },
    {
      "key": "auth_token",
      "value": "xxxxxxxxxxxx"
    }
  ]
}
```

### 2. Legacy Export Format

Hoppscotch CLI continues to support the legacy format which was previously the only accepted format used by CLI.

```json theme={null}
{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}
```

### 3. Environment ID

To use an environment on your API client using its ID, click on the `Properties` action present in the **menu icon** next to each environment. Within the Details section, you'll find the **Environment ID**. Copy this ID and use it in the Hoppscotch CLI for execution.

<Note>Please note that the Hoppscotch CLI exclusively supports the above three formats for importing environment variables. It **does not** offer compatibility with **Bulk Environment** exports or **any other export** format.</Note>

## Secrets

If requests in a collection consists of secret variables we recommend either of the two approaches.

1. Inject the secret values as variables into the OS environment
2. Edit the environment export file and add the secret values manually

## Options

| Option              | Description                                                                                                       |
| ------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `-h`                | Gives a list of associated commands and their descriptions                                                        |
| `-v`                | Displays the current version of the CLI                                                                           |
| `--env or -e`       | Accepts environments in all the formats present in [Environment section](/documentation/clients/cli#environment). |
| `--delay` or `-d`   | Used to defer the execution of requests in a collection.                                                          |
| `--token`           | Expects a personal access token to be passed for establishing connection with your Hoppscotch account.            |
| `--server`          | URL of your self-hosted instance, if your collections are on a self-hosted instance.                              |
| `--reporter-junit`  | Expects a file path to store the JUnit Report.                                                                    |
| `--iteration-count` | Defines the number of iterations to run the collection.                                                           |
| `--iteration-data`  | Accepts the path to a CSV file that contains iteration data.                                                      |
| `--legacy-sandbox`  | Opt-out from the latest experimental scripting sandbox.                                                           |

## Test Report Components

Upon executing the commands, a comprehensive test report is generated, offering detailed insights into the performance of each request. Below, you'll find a breakdown of the components outlined in the test summary for the exported API Collection:

<CardGroup>
  <Card title="Test Cases" icon="square-1">
    Each instance of `pw.expect()` within the testScript of a request is considered a test case.
  </Card>

  <Card title="Test Suites" icon="square-2">
    Each invocation of `pw.test()` within the testScript of a request is regarded as a test suite.
  </Card>

  <Card title="Test Scripts" icon="square-3">
    The total number of `testScript` fields across all requests in the provided collection export file, representing the overall number of test scripts executed.
  </Card>

  <Card title="Test Duration" icon="square-4">
    The total time taken to execute all test cases within the collection.
  </Card>

  <Card title="Requests" icon="square-5">
    The total number of requests executed within the collection.
  </Card>

  <Card title="Requests Duration" icon="square-6">
    The cumulative time taken to execute all requests within the collection.
  </Card>

  <Card title="Pre-request Scripts" icon="square-7">
    The scripts executed prior to each request. The count matches the number of requests in the provided collection export file.
  </Card>
</CardGroup>


# Hoppscotch CLI Troubleshooting
Source: https://docs.hoppscotch.io/documentation/clients/cli/troubleshooting

Troubleshoot the CLI errors by understanding their meanings and possible causes.

Below is a set of error codes and the corresponding messages that will be displayed in the CLI under various scenarios associated with workspace access. Understanding the reasons behind these errors will help you troubleshoot them on your end.

## `TOKEN_EXPIRED`

> **The specified access token is expired. Please provide a valid token.**

**Reason:** The supplied access token via the `--token` flag has been expired.

```bash theme={null}
hopp test  [-e <environment-id>] <collection-id> [--token <access_token>] [--server <server_url>]
```

## `TOKEN_INVALID`

> **The specified access token is invalid. Please provide a valid token.**

**Reason:** The specified access token via the `--token` flag is invalid or might have been deleted.

```bash theme={null}
hopp test  [-e <environment-id>] <collection-id> [--token <access_token>] [--server <server_url>]
```

## `INVALID_ID`

> **The specified collection/environment (ID or file path) is invalid or inaccessible. Please ensure the supplied ID or file path is correct.**

### Case I

**Reason:** Either an invalid ID is supplied or the resource is inaccessible to the user because the user isn't part of the team to which the resource belongs.

```bash theme={null}
hopp test  [-e <invalid-env-id>] <invalid-collection-id> [--token <access_token>] [--server <server_url>]
```

### Case II

**Reason:** Supplied file path of the collection or environment doesn't exist.

```bash theme={null}
hopp test  [-e <non-existent-env-file-path>] <non-existent-collection-file-path> 
```

## `INVALID_SERVER_URL`

> **Please provide a valid SH instance server URL.**

**Reason:** There are multiple cases in which this error can occur:

* If the supplied server URL doesn't have a valid path under `/v1/access-tokens/{collection/environment}/{path/id}`, resulting in a `404` network call error.
* If the received content type from the response is not `application/json`, safeguarding against cases where the network call doesn't fail, such as when the route is invalid as above, and checking against the content type (e.g., supplying the FE instance URL).
* The supplied server URL doesn't conform to URL semantics (received `ERR_INVALID_URL` as the error code from the network call). For instance, missing a protocol (e.g., `http://` or `https://`), having an invalid structure, or containing illegal characters.
* Couldn't find the server because the domain name couldn't be resolved (received `ENOTFOUND` as the error code from the network call). For instance, a typo in the domain name.

```bash theme={null}
hopp test  [-e <environment-id>] <collection-id> [--token <access_token>] [--server <invalid-server-url>]
```

## `SERVER_CONNECTION_REFUSED`

> **Unable to connect to the server. Please check your network connection or server instance URL and try again.**

**Reason:** Found the server, but the server refused to connect (received `ECONNREFUSED` as the error code from the network call).

```bash theme={null}
hopp test  [-e <environment-id>] <collection-id> [--token <access_token>] [--server <invalid-server-url>]
```


# Hoppscotch Desktop App
Source: https://docs.hoppscotch.io/documentation/clients/desktop

Cross-platform desktop application that runs on macOS, Windows, and Linux.

Hoppscotch Desktop App is a cross-platform desktop application that helps you create and manage API requests. It is built on top of the [Hoppscotch Web Client](/documentation/clients/web) and is powered by [Tauri](https://tauri.app).

<Frame>
  <img />

  <img />
</Frame>

## Download Hoppscotch Desktop App

Download the latest version of Hoppscotch Desktop App for your operating system:

<AccordionGroup>
  <Accordion title="Mac" icon="apple">
    <Card title="Apple Silicon (.dmg)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_mac_aarch64.dmg">
      Download for Apple Silicon-based Mac.
    </Card>

    <Card title="Intel (.dmg)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_mac_x64.dmg">
      Download for Intel-based Mac.
    </Card>
  </Accordion>

  <Accordion title="Windows" icon="windows">
    <Card title="Windows Installer (.msi)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_win_x64.msi">
      Download the installer for Windows (64-bit).
    </Card>

    <Card title="Windows Portable (.exe)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_Cloud_win_x64_portable.zip">
      Download the portable version for Windows (64-bit).
    </Card>
  </Accordion>

  <Accordion title="Linux" icon="linux">
    <Card title="Debian (.deb)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_linux_x64.deb">
      Download the Debian package for Debian-based Linux distributions.
    </Card>

    <Card title="App Image (.AppImage)" href="https://github.com/hoppscotch/releases/releases/latest/download/Hoppscotch_linux_x64.AppImage">
      Download the AppImage for Linux.
    </Card>
  </Accordion>
</AccordionGroup>

## Install Hoppscotch Desktop App

1. Download the latest version of Hoppscotch Desktop App from the links above or from [official website](https://hoppscotch.com/download).
2. Open the downloaded file.
3. Follow the on-screen instructions to install Hoppscotch Desktop App.
4. Open Hoppscotch Desktop App.
5. If you see a warning message, click "**Open**".

## Access Hoppscotch

### Hoppscotch Cloud Edition for Individuals

Seamlessly access Hoppscotch Cloud Edition from Hoppscotch Desktop App:

1. Open Hoppscotch Desktop App.
2. Click the Hoppscotch logo in the top-left corner.
3. Click "**HOPPSCOTCH CLOUD**".
4. Sign in with your Hoppscotch Cloud account to access your workspaces and collections.

### Hoppscotch Cloud Edition for Organizations

<Note>
  This feature is coming soon.
</Note>

### Hoppscotch Self-Hosted Edition for Community

<Warning>
  To enable desktop app support for your self-hosted Hoppscotch instance, make sure to update the `WHITELISTED_ORIGINS` environment variable in your `.env` file with your deployment URL.
</Warning>

<Note>
  e.g. to allow connection to `https://hoppscotch.my-domain.com` you need to add `app://hoppscotch_my_domain_com` and `http://app.hoppscotch_my_domain_com` to the `WHITELISTED_ORIGINS` environment variable.

  ```bash theme={null}
  WHITELISTED_ORIGINS=...existing_origins,app://hoppscotch_my_domain_com,http://app.hoppscotch_my_domain_com
  ```

  <Tip>
    *app\://hoppscotch\_my\_domain\_com*   for Linux and macOS machines.
  </Tip>

  <Tip>
    *http\://app.hoppscotch\_my\_domain\_com*   for Windows machine.
  </Tip>
</Note>

Add your self-hosted Hoppscotch Community Edition instance to Hoppscotch Desktop App:

1. Open Hoppscotch Desktop App.
2. Click the Hoppscotch logo in the top-left corner.
3. Click "**Add an instance**".
4. Enter the URL of your self-hosted Hoppscotch instance.
5. Click "**Connect**".

<Tip>You can also self-host Hoppscotch Desktop App. Follow the instructions in the [Hoppscotch GitHub repository](https://github.com/hoppscotch/hoppscotch/tree/main/packages/hoppscotch-desktop).</Tip>

### Hoppscotch Self-Hosted Edition for Enterprise

<Warning>
  To enable desktop app support for your self-hosted Hoppscotch instance, make sure to update the `WHITELISTED_ORIGINS` environment variable in your `.env` file with your deployment URL.
</Warning>

<Note>
  e.g. to allow connection to `https://hoppscotch.my-domain.com` you need to add `app://hoppscotch_my_domain_com` and `http://app.hoppscotch_my_domain_com` to the `WHITELISTED_ORIGINS` environment variable.

  ```bash theme={null}
  WHITELISTED_ORIGINS=...existing_origins,app://hoppscotch_my_domain_com,http://app.hoppscotch_my_domain_com
  ```

  <Tip>
    *app\://hoppscotch\_my\_domain\_com*   for Linux and macOS machines.
  </Tip>

  <Tip>
    *http\://app.hoppscotch\_my\_domain\_com*   for Windows machine.
  </Tip>
</Note>

Add your self-hosted Hoppscotch Enterprise Edition instance to Hoppscotch Desktop App:

1. Open Hoppscotch Desktop App.
2. Click the Hoppscotch logo in the top-left corner.
3. Click "**Add an instance**".
4. Enter the URL of your self-hosted Hoppscotch instance.
5. Click "**Connect**".

<Tip>You can also self-host Hoppscotch Desktop App. Follow the instructions in the [Hoppscotch GitHub repository](https://github.com/hoppscotch/hoppscotch/tree/main/packages/hoppscotch-desktop).</Tip>


# Hoppscotch Web App
Source: https://docs.hoppscotch.io/documentation/clients/web

Build, test, and share your APIs directly in your browser.

Hoppscotch web client provides you with a really easy interface to develop and test your APIs. You can start using the web client by opening [hoppscotch.io](https://hoppscotch.io) in your browser.

<Frame>
  <img />

  <img />
</Frame>

## Progressive Web App

Hoppscotch is also available as a PWA (Progressive Web App).

<Tip>Progressive Web Apps (PWAs) are web apps that are fast, reliable, and engaging. They are installable and live on the user's home screen, without the need for an app store. They offer an immersive full-screen experience and re-engage users with web push notifications.</Tip>

## Why PWA

* **Fast** - Load instantly to get started with Hoppscotch in seconds.
* **Installable** - Install Hoppscotch on your device's home screen, just like a native app.
* **Reliable** - Never shows the downasaur, even in uncertain network conditions.
* **Engaging** - Feel like a natural app on the device, with an immersive user experience.

## Install Hoppscotch PWA

1. On your computer, open Chrome or any Chromium-based browser.
2. Go to [hoppscotch.io](https://hoppscotch.io).
3. At the top right of the address bar, click "**Install +**".
4. Follow the on-screen instructions to install the PWA.

<Tip>Read more about [Progressive Web Apps](https://web.dev/progressive-web-apps).</Tip>


# Community
Source: https://docs.hoppscotch.io/documentation/community

Join our open communities and forums.

At Hoppscotch, we believe that the community is the most important part of our product. We want to make sure that our users have a great experience using our products and that they can contribute to the development of our products with their ideas, feedback, and suggestions.

Join our open communities and forums to stay up to date with the latest happenings in the product.

<CardGroup>
  <Card title="X" icon="x-twitter" href="https://hoppscotch.io/twitter">
    Follow us on X for news, updates and more.
  </Card>

  <Card title="Discord" icon="discord" href="https://hoppscotch.io/discord">
    Join our Discord server to chat with the community.
  </Card>

  <Card title="GitHub" icon="github" href="https://hoppscotch.io/github">
    Contribute to the development of Hoppscotch.
  </Card>
</CardGroup>


# Contributors
Source: https://docs.hoppscotch.io/documentation/contributors

Hoppscotch exists thanks to the awesome people who contribute to it.

Hoppscotch is a community-driven project. We are thankful to all the contributors who have helped us in making Hoppscotch a better tool for developers.

Here are some of our top contributors who helped us to make Hoppscotch a better tool for developers.

![Contributors](https://contrib.rocks/image?repo=hoppscotch/hoppscotch)

* [View the full list of contributors here →](https://github.com/hoppscotch/hoppscotch/graphs/contributors)


# Develop
Source: https://docs.hoppscotch.io/documentation/develop

Learn how to contribute to Hoppscotch.

We love your input! We want to make contributing to Hoppscotch as easy and transparent as possible, whether it's:

* Reporting a bug
* Discussing the current state of the code
* Submitting a fix
* Proposing new features

## We develop with GitHub

We use GitHub to host code, track issues, and feature requests, as well as accept pull requests.

**We use [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow), So all code changes happen through pull requests.**

Pull requests are the best way to propose changes to the codebase (we use [GitHub Flow](https://guides.github.com/introduction/flow/index.html)). We actively welcome your pull requests.

## Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Please note we have a [code of conduct](/support/code-of-conduct), please follow it in all your interactions with the project.

## Pull Request Process

1. Ensure any install or build dependencies are removed before the end of the layer when doing a
   build.
2. Update the README.md with details of changes to the interface, this includes new environment
   variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this
   Pull Request would represent. The versioning scheme we use is [SemVer](https://semver.org).
4. You may merge the Pull Request once you have the sign-off of two other developers, or if you
   do not have permission to do that, you may request the second reviewer merge it for you.

## **Developing**

* Section moved to [Self-Hosting](/documentation/self-host/getting-started).

### Browser-based development environment

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/hoppscotch/hoppscotch)

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/hoppscotch/hoppscotch)

### Local development environment

* Section moved to [Self-Hosting](/documentation/self-host/getting-started).

### Docker compose

* Section moved to [Self-Hosting](/documentation/self-host/getting-started).

## **Docker**

* Section moved to [Self-Hosting](/documentation/self-host/getting-started).

## **Releasing**

* Section moved to [Self-Hosting](/documentation/self-host/getting-started).

#### Any contributions you make will be under the MIT License.

In short, when you submit code changes, your submissions are understood to be under the same [MIT License](https://choosealicense.com/licenses/mit) that covers the project. Feel free to contact the maintainers if that's a concern.

#### Report bugs using GitHub's Issues

We use GitHub issues to track public bugs. Report a bug by [opening a new issue](https://github.com/hoppscotch/hoppscotch/issues); it's that easy!

#### Write bug reports with detail, background, and sample code

[This is an example](https://stackoverflow.com/q/12088905/180626) of a bug report I wrote, and I think it's not a bad model. Here's [another example](https://www.openradar.me/11905408).

**Great Bug Reports** tend to have:

* A quick summary and/or background
* Steps to reproduce
  * Be specific!
  * Give a sample code if you can.
* What you expected would happen
* What happens
* Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)

People love thorough bug reports. I'm not even kidding.

#### Use a consistent coding style

I'm again borrowing these from [Facebook's Guidelines](https://reactjs.org/docs/how-to-contribute.html)

* 2 spaces for indentation rather than tabs
* You can try using Eslint code extensions in vs code or something similar.

## Recommended VS Code extensions

* WindiCSS IntelliSense

  [Install](https://marketplace.visualstudio.com/items?itemName=voorjaar.windicss-intellisense) • [Repository](https://github.com/windicss/windicss-intellisense)

* Vue Language Features (Volar)

  [Install](https://marketplace.visualstudio.com/items?itemName=vue.volar) • [Repository](https://github.com/johnsoncodehk/volar)

* Stylelint

  [Install](https://marketplace.visualstudio.com/items?itemName=stylelint.vscode-stylelint) • [Repository](https://github.com/stylelint/vscode-stylelint)

* SCSS IntelliSense

  [Install](https://marketplace.visualstudio.com/items?itemName=mrmlnc.vscode-scss) • [Repository](https://github.com/mrmlnc/vscode-scss)

* SCSS Formatter

  [Install](https://marketplace.visualstudio.com/items?itemName=sibiraj-s.vscode-scss-formatter) • [Repository](https://github.com/sibiraj-s/vscode-scss-formatter)

* PostCSS Language Support

  [Install](https://marketplace.visualstudio.com/items?itemName=csstools.postcss) • [Repository](https://github.com/csstools/postcss-language)

* npm Intellisense

  [Install](https://marketplace.visualstudio.com/items?itemName=christian-kohler.npm-intellisense) • [Repository](https://github.com/ChristianKohler/NpmIntellisense)

* JavaScript and TypeScript Nightly

  [Install](https://marketplace.visualstudio.com/items?itemName=ms-vscode.vscode-typescript-next) • [Repository](https://github.com/microsoft/vscode-typescript-next)

* GraphQL

  [Install](https://marketplace.visualstudio.com/items?itemName=GraphQL.vscode-graphql) • [Repository](https://github.com/graphql/vscode-graphql)

* ESLint

  [Install](https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint) • [Repository](https://github.com/Microsoft/vscode-eslint)

* EditorConfig for VS Code

  [Install](https://marketplace.visualstudio.com/items?itemName=EditorConfig.EditorConfig) • [Repository](https://github.com/editorconfig/editorconfig-vscode)

* npm

  [Install](https://marketplace.visualstudio.com/items?itemName=eg2.vscode-npm-script) • [Repository](https://github.com/Microsoft/vscode-npm-scripts)

## License

By contributing, you agree that your contributions will be licensed under [MIT License](https://github.com/hoppscotch/hoppscotch/blob/main/LICENSE).


# AI Features
Source: https://docs.hoppscotch.io/documentation/features/ai-features

Optimize API Development and Testing Workflows with Hoppscotch using AI.

<span>Experimental</span>

Hoppscotch now offers a set of AI-powered features designed to simplify core stages of the API development lifecycle. These include renaming of API requests, generation of structured request payloads, and scripting capabilities for pre-request logic and test cases.

<Warning> These AI features are currently in the `alpha` stage and are exclusively available on [Hoppscotch Cloud](https://hoppscotch.io) and our [Desktop app](https://hoppscotch.com/download). They are **NOT** supported in the Self-Hosted Edition at this time. </Warning>

### Enable AI-powered features

To activate AI-powered features, follow these steps:

1. Open the **Settings** page within the Hoppscotch application.
2. Scroll to the **Experiments** section.
3. Toggle the **AI Experiments** option to enable the features.

### Rename API Requests

When saving an API request to a collection, click the **Modify with AI** icon **( .⟡⁺ )** next to the request name field to have the system automatically assign a name based on the request's context and properties. Alternatively, you can use this feature to rename the pre-saved requests.

You can even customize the naming convention (e.g., CamelCase, PascalCase) through the **Request Naming Style** dropdown located in the **Experiments** section of the **Settings** page.

### Generate Request Body

Dynamically generate structured request payloads:

1. Click the **Modify with AI** icon **( .⟡⁺ )** in the **Request Body** section.
2. Define constraints or provide input for the desired structure.
3. Validate the generated body and select **Accept Change** to populate the request body field.

### Generate Pre-request Scripts

Generate pre-request scripts to handle necessary setup operations before sending the request:

1. Click the **Modify with AI** icon **( .⟡⁺ )** within the **Pre-request Script** section.
2. Enter specific logic or conditions required for the pre-request phase.
3. After reviewing the generated script, click **Accept Change** to apply it to the pre-request script section of your API request.

### Generate Test Scripts

Develop test cases for your API workflow:

1. Click the **Modify with AI** icon **( .⟡⁺ )** in the **Tests** section.
2. Specify the test parameters or expected outcomes.
3. Select **Accept Change** to integrate it into the test script editor for execution.


# Authorization
Source: https://docs.hoppscotch.io/documentation/features/authorization

Authorization is the process of verifying that a client has permission to access a resource.

REST APIs use authorization to ensure that a client has secure access only to the resources permitted by their roles. If you are building or integrating with a 3rd party API, you can choose between Basic Auth, Bearer Tokens, and OAuth2.0.

Auth details can be added to a header, body, or as parameters to a request. However, if you enter your auth details in the Authorization Tab, Hoppscotch will automatically modify the relevant parts of the request based on your chosen `Auth` type. Storing Auth Credentials or Bearer Tokens as environment variables, lets you re-use these more safely and efficiently.

## Inherit

Inherit Authorization allows requests to automatically adopt the authorization settings defined at the parent collection or subfolder level. This means you only need to configure the authorization once, and all nested requests will inherit these settings, ensuring consistency and saving time during setup.

## Basic Auth

Basic Authentication is one of the simplest methods to secure your API requests in Hoppscotch. It works by requiring a username and password to be sent along with each request. To get started, head to the **Authorization** tab and select `Basic Auth` as your authentication type. You'll then input your verified **username** and **password**. When you send the request, Hoppscotch will automatically encode your credentials in the format:

```
Basic <Base64-encoded-credentials>
```

<Tip> Basic Auth transmits your credentials in a way that can be easily decoded, so it's best suited for secure channels like HTTPS to prevent exposure.</Tip>

## Bearer Tokens

Bearer Tokens are used to authenticate requests using an access token, which can be a simple string or a JWT (JSON Web Token). To set it up, choose `Bearer` from the **Authorization** tab and enter your **access token**. Hoppscotch will include the token in the request header as:

```
Bearer <your-access-token>
```

<Info>Be aware that if your token expires, you'll need to refresh it manually and update it in Hoppscotch. For better security, consider storing your token as an environment variable so that you can easily reference it in your requests.</Info>

## API Key

API Keys are unique identifiers that help authenticate your requests to an API. In Hoppscotch, you can set up `API Key` authentication by selecting it from the **Authorization** tab. Here, you'll need to fill in two fields: the **Key**, which is the name the API expects (like `api_key` or `Authorization`), and the **Value**, which is your actual API Key. You can also choose whether to pass this API Key as a **Header** or as a **Query Parameter**.

<Tip>When using API Keys, keep an eye on the rate limits set by the API provider to avoid any issues. For improved security practices, store your API Key as an environment variable to facilitate easy management across different environments.</Tip>

## OAuth 2.0

OAuth 2.0 provides a secure way to let third-party applications access your resources without needing to share your passwords. Instead of directly passing credentials, you authenticate through a trusted service, which then issues an access token. This **token** allows your app to make API requests on your behalf.

<Warning> OAuth 2.0 workflows are not fully supported in the Hoppscotch Desktop application and are currently a work in progress. We're actively working on it, and it will function as intended soon!</Warning>

### Steps for OAuth 2.0 Setup

1. In the "**Authorization Tab**" for a request, select `OAuth 2.0` from the Authorization Type drop-down.
2. Select the [Grant Type](/documentation/features/authorization#grant-types) from Authorization Code (with or without PKCE), Client Credentials, Password Credentials, and Implicit.
3. Fill out the fields in the section below and click on "**Generate Token**" to generate a new access token.
4. You can save the token to be re-used later.

### Grant types

When using OAuth 2.0 authorization with Hoppscotch, you can utilize the following grant types:

#### 1. Authorization Code

The Authorization Code grant is used when your application needs to access a user's account. The user logs in to the OAuth provider and gives permission, allowing your app to receive a special code. You then use this code to request an access token that lets you access the user's data.

To use the `Authorization Code` grant type, ensure the [Callback URL](#oauth-callback-url-configuration) is correctly configured (either `https://hoppscotch.io/oauth` for Hoppscotch Cloud or `<your-domain>/oauth` for self-hosted editions). Next, provide the **Authorization Endpoint** and **Access Token Endpoint** from the API provider, along with the **Client ID** (and the Client Secret if you choose to use it). You can also specify the desired permissions in the **Scope** field and pass the token as a **Header** or as a **Query Parameter**. Once you've filled in these fields, click Generate Token to get your access token.

<Tip> If your API provider supports token refreshing, you can use the **"Refresh Token"** button in Hoppscotch to obtain a new access token without requiring the user to log in again.</Tip>

> #### Using PKCE
>
> Opting for OAuth 2.0 with PKCE (Proof Key for Code Exchange), you gain the option to enhance security. Upon selecting PKCE, you can choose between **SHA-256** or **Plain** algorithms.

#### 2. Client Credentials

The Client Credentials grant is suitable for server-to-server interactions, where your application needs to access its own resources rather than user-specific data. This method relies on your app's credentials to obtain an access token directly.

To obtain a token using `Client Credentials` grant type, input the **Authorization Endpoint** from the API provider, and fill in your **Client ID**. Including a Client Secret is optional.

<Note>
  You can now choose how the **client credentials** (Client ID and Client Secret) are sent to the server. Hoppscotch supports both:

  * Sending them in the **body of the request** (default behavior).
  * Sending them via **Basic Authentication headers**.

  Just select your preferred method in the `Client Authentication` field to suit your security requirements.
</Note>

#### 3. Password Credentials

The Password Credentials grant allows you to authenticate users by sending their username and password directly to the API. This method is less secure and is generally discouraged for third-party applications.

To implement the `Password` credentials grant type in Hoppscotch, provide your API provider's **Authorization Endpoint**, along with the **Username** and **Password**. Occasionally, you may also be required to supply a Client ID and Secret.

#### 4. Implicit

The Implicit grant is intended for client-side applications, where the access token is returned immediately without the need for an authorization code. While this method simplifies the process, it does come with security risks.

To configure the `Implicit` grant type in Hoppscotch, make sure the [Callback URL](#oauth-callback-url-configuration) is set as required (either `https://hoppscotch.io/oauth` or `<your-domain>/oauth`).  You will need to further provide the **Authorization Endpoint** and **Client ID** to generate the token.

### <Icon icon="check" /> OAuth Callback URL Configuration

When using OAuth 2.0 with Hoppscotch Cloud, the **callback URL** is fixed to `https://hoppscotch.io/oauth` while for self-hosted editions of Hoppscotch, the callback URL should be set to `<your-domain>/oauth` . You must configure this URL as a valid **redirect URI** in your OAuth provider's settings. This is important because Hoppscotch handles all OAuth requests on the client side. When your OAuth provider redirects you to this URL, we process the response to obtain the token or authorization code. Any mismatch between the registered callback URL and what Hoppscotch uses will result in errors like `INVALID_REDIRECT_URI` during the authorization process.

<Note> The Callback URL is required only for **Authorization Code** and **Implicit** grant types. Other grant types do not need this configuration. </Note>

## Digest

Digest Auth is a way to verify your identity without transmitting plain text passwords. Instead of sending your credentials directly as plain-text, it uses a challenge-response system to keep your information safe. When you attempt to access a restricted resource, the server responds with a `401 Unauthorized` status and a `WWW-Authenticate` header. This header contains essential information, including a unique challenge that you will use to generate a valid response.

To configure Digest Auth in Hoppscotch, start by entering your **Username** and **Password**. For added security, you can also provide optional parameters like Realm and Nonce from the `WWW-Authenticate` header. Choose the appropriate **Algorithm** for hashing and define the **Quality of Protection (QoP)** to further secure your requests. You can also specify parameters such as **Nonce Count**, **Client Nonce**, and **Opaque** to further bolster the authentication process.

<Note> **Digest Auth** is supported exclusively when using the [Hoppscotch Agent interceptor](/documentation/features/interceptor#hoppscotch-agent). </Note>

## AWS Signature

AWS Signature is a method used to authenticate API requests made to AWS services. When you send a request, this configuration ensures that your request is genuine and has not been tampered with. It does this by using a process called HMAC (Hash-based Message Authentication Code), which creates a unique signature based on your request details.

To set up `AWS Signature` in Hoppscotch, enter your AWS **Access Key** and **Secret Key** to sign your requests. For advanced configuration, you can also provide details like the **AWS Region** where your service is hosted (like *us-east-1*), the **Service Name** of the specific AWS service you're accessing (such as *s3 or dynamodb*), and a **Service Token** if you're using temporary security credentials.

## JWT

JWT (JSON Web Token) is a compact and secure way to transmit information between parties as a JSON object. It is commonly used for authentication and information exchange in web applications. In Hoppscotch, you can easily configure JWT authentication by selecting `JWT` from the **Authorization** tab.
You can then enter your **JWT Token** directly, or if you have a JWT secret, you can use it to generate the token. This token will be included in the request header as:

```
Authorization: Bearer <your_jwt_token>
```

***

# Managing Authorization at the Collection Level

When managing multiple requests within a collection, setting identical authorization configurations for each request individually can be tedious. It is now possible to set authorization at the collection level, ensuring it applies to all the requests stored within that collection.

**To set collection-level authorization:**

* Right-click on a collection or a subfolder within a collection to open its **properties**.
* Specify the authorization that all nested requests or folders should adhere to.
* If a subfolder should inherit the properties of a parent collection, specify the authorization as `inherit`.


# Client Certificate
Source: https://docs.hoppscotch.io/documentation/features/client-certificate

Configure client certificates for SSL authentication in Hoppscotch.

Add and manage client certificates in [Hoppscotch Desktop App](https://hoppscotch.com/download) or in Hoppscotch Web App using the [Hoppscotch Agent](/documentation/features/interceptor#hoppscotch-agent) as an interceptor to authenticate your identity when connecting to secure APIs.

### Prerequisites

Before you begin, ensure you have the following:

* Either the **Hoppscotch Desktop App** installed on your system, or if you are using the Hoppscotch Web App, make sure the **Hoppscotch Agent** is installed and configured.
* A valid Client Certificate in one of the following formats:
  * **.pem Certificate**
  * **.pfx/.pkcs12 Certificate**
* The corresponding private key file, if the certificate is in .pem format.

### Adding Client Certificate

1. Open Hoppscotch's settings page from the side bar.
2. Within Interceptors section, locate the `Client Certificates` action:
   * Under Native settings if using the Desktop App.
   * Under Agent if using the Web App.
3. Click on the option to add a new client certificate and select the type of certificate you want to add: **.pem** or **.pfx/.pkcs12**.
4. **Upload Certificate Files**
   * **.pem Certificate**: Choose the **certificate file** (.crt/.cer/.pem) and upload the **private key file** (.key/.pem) in the designated field.
   * **.pfx/.pkcs12 Certificate**: Choose the **.pfx/.pkcs12** file. You may need to enter the password associated with the certificate file.
5. After uploading the certificate files, click on the save button to store the settings.

<Warning> **You cannot edit a certificate after adding it.** </Warning>

### Using Client Certificate

Once you add the certificate, it will automatically be applied to the configured domain whenever you make an HTTP request. If you wish to disable the certificate for a domain, simply uncheck the corresponding checkbox.

### Removing a certificate

Remove a certificate when no longer needed for sending requests by selecting the **delete icon** located next to the certificate associated with a specific domain.


# Collections
Source: https://docs.hoppscotch.io/documentation/features/collections

Save, organize, and share your API requests with collections.

Hoppscotch helps you to organize your API requests with collections. You can create collections and add requests to them to share with your team or to use later. You can also import and export collections from Hoppscotch, OpenAPI, and Postman.

You can access the collections by clicking the "**Collections**" icon on the side panel.

## Creating a new collection

To create a new collection, click on the "**Add new**" button on the collections section and enter the name of the collection. You can also create a sub-collection by clicking on the "**Add new**" button on the desired collection and entering the name of the sub-collection.

## Save requests to collections

To add a new request to your collection, you can click on the "**Save**" button on the request page and select the collection you want to add it to. Click on the drop-down menu next to the save button and click on "**Save as**" to save the request to a new location.

<Tip>You can also use the keyboard shortcut <kbd>`Ctrl/Cmd`</kbd> + <kbd>`S`</kbd> to save the request to a collection.</Tip>

## Organizing collections

You can organize your collections by dragging and dropping them to the desired location. You can also create sub-collections by dragging and dropping a collection into another collection.

### Editing collections

To edit a collection, click on the "**Edit**" button on the collection's options.

### Adding requests to collections

To add a request to a collection, click on the "**New request**" button on the collection's options to save the current request to the collection.

## Duplicating collections

To duplicate a collection, click on the **"Duplicate"** button on the collection's options.

## Deleting collections

To delete a collection, click on the "**Delete**" button on the collection's options.

## Importing and exporting collections

You can import and export collections from Hoppscotch, OpenAPI, and Postman.

### Importing collections

To import a collection, click on the "**Import**" button in the collections section and select the collection type you want to import.

### Exporting collections

To export a collection, click on the "**Export**" button on the collection's options and select the collection type you want to export.

## Collection Properties

Collection properties enable you to define settings that universally apply to all requests within the collection.

At the collection level, you can configure:

* Authorization
* Headers
* Variables

Subfolders and individual requests within the collection inherit these properties by default and can override them when needed.

To set collection properties:

1. Right-click on a collection or a subfolder within a collection to open its properties.
2. Specify the authorization, headers, and variables that all nested requests or folders should adhere to.
3. If a subfolder should inherit the properties of a parent collection, specify the authorization as "inherit" and leave headers unchanged. Variables inherit automatically—override by redefining the same variable in the child.


# Context Menu
Source: https://docs.hoppscotch.io/documentation/features/context-menu

Use context-aware menus to assist with your actions and improve your workflow.

Context-aware menus enable quick actions like creating variables or adding query
parameters by selecting text or elements. The context menu offers three options:
**Set as Variable**, **Add to Parameters**, and **Open Request in New Tab**.

<Info>
  The "Add to Parameters" option is available only when using query parameters.
</Info>

## Set as Variable

You can use the **Set as Variable** option from the context menu to assign a
selected value to an environment variable.

Hoppscotch supports various variable scopes, including global, environment, and
request-specific variables. For more details on these scopes
[click here](/documentation/features/variables).

### How to use "Set as Variable"

After setting an [environment variable](/documentation/features/environments),
you can reference it using the format `<<variable name>>`. This allows you to
store For example, `<<baseURL>>` can be used to dynamically insert the base URL
across your requests.

## Add to Parameters

The **Add to Parameters** option allows you to quickly add parameters along with
their values.

When you select **Add to Parameters**, it automatically captures the parameter
and its value. For example, if the `baseURL` is
`https://jsonplaceholder.typicode.com/?user=1`, now the `user` with ID `1` will
be included in the parameter placeholder.

## Open Request in New Tab

The **Open Request in New Tab** option allows you to open any **selected URL or
text** as a new request in a separate tab..

By opening the selected URL in a new tab, you can continue working on your
original request in its own tab without any interruptions.


# Cookies
Source: https://docs.hoppscotch.io/documentation/features/cookies

Create and modify cookies associated with a domain and send cookies with requests.

<Info>Cookies support is only available in the [Hoppscotch Desktop App](/documentation/clients/desktop).</Info>

Hoppscotch Cookie Manager enables you to add, edit, and remove cookies for a domain. You can also send a cookie with a request.

To open the Cookie Manager, click on the "**Cookies**" button in the bottom bar.

### Adding a domain

The Cookie Manager allows you to specify a domain and add the cookies associated with that domain. You can remove all the domains using the "**Clear All**" button.

1. Add domain URL in the input field.
2. Click on the "**Add**" button.
3. Click on the "**Save**" button.

Once you've specified a domain, you can add a cookie by clicking the **+** icon and entering a cookie string.

### Removing a domain

You can remove a domain by clicking on the "**Delete**" icon from the Cookie Manager.

### Adding a cookie

You can add a cookie by clicking on the "**+**" icon from the Cookie Manager.

1. Click on the "**+**" icon.
2. Enter the cookie string in the input field.
3. Click on the "**Save**" button.

### Editing a cookie

You can edit a cookie by clicking on the "**Edit**" icon from the Cookie Manager.

1. Click on the "**Edit**" icon.
2. Edit the cookie string in the input field.
3. Click on the "**Save**" button.

### Removing a cookie

You can remove a cookie by clicking on the "**Delete**" icon from the Cookie Manager.

### Sending a cookie with requests

When you send a request to a domain for which you've specified a cookie, Hoppscotch will automatically include it as part of the request.


# Customization
Source: https://docs.hoppscotch.io/documentation/features/customization

Customize your Hoppscotch experience.

You can access the customization settings by clicking on the "[**Settings**](https://hoppscotch.io/settings)" icon on the side panel.

## Background color

You can choose from a range of colors to set as your background.

* System (Default)
* Light
* Dark
* Black

## Accent color

You can choose from a range of colors to set as your accent color.

* Green
* Teal
* Blue
* Indigo (Default)
* Purple
* Yellow
* Orange
* Red
* Pink

## Language

Hoppocotch supports multiple languages. You can choose your preferred language from the list of available languages.

## Expand navigation

You can choose to expand the side panel to view the navigation menu with labels.

## Sidebar position

You can choose to position the side panel on the left or right side of the screen.


# API Documentation
Source: https://docs.hoppscotch.io/documentation/features/documentation

Create, edit, and publish beautiful API documentation collaboratively with your team.

When you build a collection in Hoppscotch, documentation is generated for you out of the box. It covers every endpoint with ready-to-use code samples across popular languages. Request information like HTTP method, URL, headers, auth configuration, payload format, and response examples are all captured automatically.

Want to provide more context? Use Markdown to write descriptions for collections, folders, or requests, they'll appear directly in your published docs, helping developers get up to speed faster.

## What you can do

* Generate API documentation from your Collections
* Collaborate with your team to edit and refine content
* Support for Markdown descriptions
* Share documentation with your team or the world
* Publish documentation to a public URL
* Organize endpoints with folders and subfolders
* Include example requests and responses
* Code snippets for various languages and frameworks
* Version your documentation to maintain multiple releases
* Allow users to switch environments dynamically

## Create documentation

Descriptions make your documentation more useful by providing context beyond the raw request details. You can add descriptions at multiple levels collections, folders, and individual requests using Markdown syntax for formatting, links, images, and code blocks.

1. **Select a Collection**: Choose the collection you want to document.
2. **Write Documentation**: Navigate to Menu > Documentation.
3. **Publish**: Get a shareable link to your documentation by publishing it.

### Adding a description to a request

1. Select the request you want to document.
2. Navigate to the request's description field.
3. Add details about the endpoint's purpose, expected parameters, or usage notes.
4. Save to include it in the generated documentation.

## Collaborative Editing

Invite team members to your workspace to collaborate on documentation. Changes made to the collection are reflected in the documentation, keeping everything in sync.

## Features

### Real-time Updates

Documentation updates automatically as you modify your collection. You need to publish changes to redeploy the documentation.

### Code Snippets

Automatically generated code snippets for various languages and frameworks help developers integrate with your API quickly.

### Example Responses

Display example responses to help users understand what to expect from your API endpoints. You can add multiple examples for different scenarios (e.g., success, error).

### Markdown Support

Use Markdown to add rich text descriptions, images, and links to your documentation, making it easy to read and understand.

### Versioning

Maintain multiple versions of your API documentation to support different releases and API iterations.

1. **Create a Version**: When publishing your documentation, you can create a new version with a label (e.g., `v1.0`, `v2.0`).
2. **Switch Versions**: Users viewing your documentation can switch between available versions using the version selector dropdown.

Versioning helps you maintain backward compatibility documentation while showcasing new features in the latest release.

### Environment Selector

Each documentation version can be associated with a specific environment (e.g., Production, Staging, Development), allowing you to provide accurate base URLs and variables for that release.

1. **Configure Environments**: Set up environments with their respective base URLs and variables in your workspace.
2. **Select Environment per Version**: When publishing a documentation version, choose the environment to associate with it. Each version supports one environment.
3. **Dynamic Base URLs**: The documentation automatically displays the correct base URLs and code snippets based on the environment linked to the selected version.

This feature is particularly useful when your API is deployed across multiple environments, allowing you to publish separate documentation versions for each environment (e.g., `v1.0-prod`, `v1.0-staging`).

<Warning>
  Selecting an environment will expose its variables to users viewing the
  documentation. Avoid using environments that contain sensitive information
  such as API keys, tokens, or other secrets. Consider creating a dedicated
  environment for documentation purposes with only non-sensitive variables.
</Warning>

## Publishing

Publishing your documentation makes it accessible to anyone with the link, enabling developers worldwide to understand and integrate with your API. Once published, your documentation serves as a comprehensive guide for your collection, helping users explore endpoints and learn how to interact with your API.

Published documentation automatically includes details for each request in your collection, complete with sample code snippets in multiple programming languages. When auto-sync is enabled, any updates you make to your collection are reflected in the documentation instantly, no need to republish after every change.

<Frame>
  <img alt="Publishing Options" />

  <img alt="Publishing Option" />
</Frame>

### First-time Publishing

When you publish a collection for the first time, Hoppscotch automatically creates the initial version for you. The documentation will be auto-synced with your collection, meaning any changes you make to the collection will automatically update the published documentation.

1. **Open Documentation Panel**: Navigate to your collection and click on the Documentation option from the menu.
2. **Click Publish**: The initial version is created automatically and synced with your collection.

### Creating New Versions

After your first publish, you can create additional versions to maintain different releases of your API documentation. Click on "Create Version" to open the publishing options.

<Frame>
  <img alt="Publishing versions" />

  <img alt="Publishing versions" />
</Frame>

The publishing dialog includes the following options:

* **Title**: The name of your documentation (e.g., "Swagger Petstore").
* **Version**: A label for this version of your documentation (e.g., `v1.0`, `v2.0`).
* **Auto-sync with collection**: Enable this option to automatically update the published documentation when the collection changes. Disable it if you want to freeze this version.
* **Environment**: Attach an environment to resolve variables in the published documentation. The environment's base URL and variables will be displayed in the documentation.

Click **Publish** to deploy the new version.

### Published Documentation Snapshot

After creating a version, a snapshot view of the published documentation opens up. This provides a preview of what your users will see.

The snapshot view displays:

* **Title and Version**: The documentation name and version label (e.g., "Swagger Petstore v2.0.0").
* **Published URL**: The shareable link to your documentation with options to copy or open in a new tab.
* **Collection Structure**: A preview of your API endpoints organized by folders.
* **Documentation Content**: The description, contact information, and variables (such as `baseUrl`) from the attached environment.

<Note>
  Published versions are read-only snapshots. To make changes, create a new
  version or enable auto-sync with the collection.
</Note>

### Managing Published Documentation

* **Update**: Republish to reflect collection changes.
* **Unpublish**: Remove public access at any time.
* **Share**: Copy the documentation URL to distribute.

### Viewing Published Documentation

<Frame>
  <img alt="Published Documentation View" />

  <img alt="Published Documentation View" />
</Frame>

The published view includes a sidebar for navigating endpoints, a version selector, and the environment indicator showing the associated base URL and variables.


# Environments
Source: https://docs.hoppscotch.io/documentation/features/environments

Environments help you create variables that you can reuse in requests and scripts.

An environment allows you to group together a set of variable data. You can reference the variable data you define in an environment throughout Hoppscotch when sending requests or using scripts.

Environments are also useful when you need to manage shared variables with a team. You can create environments and share them with your workspace members.

## Types of Environments

1. Global Environment - Variables defined in a global environment can be accessed from any workspace anytime. However the variables defined in a personal or shared workspace environment if used will have higher precedence over a global variables
2. Personal Environment - Are personal to the user and is not associated with a shared workspace, however a user can use a personal environment in a shared workspace without sharing it with the workspace members
3. Shared Environments -  Are unique to each shared workspace, all the shared environments created in a shared workspace are accessible to every member of the shared workspace

## Types of Variables in an Environment

Hoppscotch environment provides support for two types of variables

1. A Regular environment variable allows users to reference the variable throughout Hoppscotch, and anyone can see the value associated with the variable. In a shared workspace, regular environment variable-value pairs will be synced to the server, making them available to all workspace members. However, you have the option to choose whether to sync a personal or global environment.

2. A secret environment variable enables users to specify secrets and reference the values as variables. The values of secret variables in any workspace will never be synced to the server or shared with any workspace members. It is expected that the user will populate the value of the variable at runtime. All secret variable values in Hoppscotch will be masked using asterisks (\*\*\*).

<Tip>Secret variables values will not be exported when an environment is exported.</Tip>

## Types of Values in an Environment

An environment variable can have two types of values:

1. **Initial Value** - The initial value of the variable when it is created. This value is used when the environment is first loaded.
2. **Current Value** - The current value of the variable, which can be modified at any time. This value is used when the environment is active.

## Shared Environment Access

|                  | Environment Variable                         | Secret Variable                                     |
| ---------------- | -------------------------------------------- | --------------------------------------------------- |
| Workspace Owner  | create / delete variable, edit value and use | create / delete secret variable, add values and use |
| Workspace Editor | create / delete variable, edit value and use | create / delete secret variable, add value and use  |
| Workspace Viewer | use                                          | add value and use                                   |

## Creating an environment

Click on the ”Environments” icon on the sidebar to create environments.

A variable created in an environment can be used by typing the variable name enclosed in double angle brackets `<<variable>>`

## Using scripts

You can also create and delete environment variables using scripts by using the `pw` object..

```javascript theme={null}
pw.env.set("variable", "value"); // Creates an environment variable 
pw.env.unset("variable"); // Deletes the environment variable
```

## Duplicating an environment

Create a copy of an existing environment to modify or test different configurations without affecting the original:

1. Click the "Environments" icon in the sidebar to view all existing environments under Global Environments.
2. Next to the environment you want to duplicate, click the **More** icon.
3. From the dropdown menu, select **Duplicate**. A new environment with the suffix `- Duplicate` will be created.

<Note> Secret variable values will not be copied to the duplicated environment. </Note>

<CardGroup>
  <Card title="Creating environment variables from client" icon="circle-arrow-right" href="/documentation/getting-started/rest/environment-variables">
    Learn how you can create environment variables from the client.
  </Card>

  <Card title="Creating environment variables using scripts" icon="circle-arrow-right" href="/documentation/getting-started/rest/pre-request-scripts#setting-environment-variables">
    Learn how you can create environment variables using pre-request scripts.
  </Card>

  <Card title="Read more pre-request script examples" icon="circle-arrow-right" href="/documentation/getting-started/rest/pre-request-scripts#examples">
    Learn more pre-request script examples.
  </Card>
</CardGroup>


# GraphQL API Testing
Source: https://docs.hoppscotch.io/documentation/features/graphql-api-testing

Test and play around with GraphQL APIs.

Hoppscotch's GraphQL API platform provides you with the best experience to test and play around with GraphQL.

It's primarily divided into two sections along with other features to help you build and test queries.

## Request

The request section houses the feature to enter your server endpoint and initiate a connection.

Once the connection is made, the `query` builder assists you in designing queries to fetch the data that you require and run it.

You can also add dynamic behavior to your queries by defining `variables`, `headers`, and `authorization`.

## Response

This is where you see the responses to your API endpoints. You can download and copy the returned responses for further use.

## Other features

### Documentation

GraphQL documentation is where you can view the documentation provided by the developer.

### Schema

GraphQL uses a schema to define the structure of the data, the schema explorer helps you to understand how your data is structured.

The GraphQL platform also houses other features like:

* [Environments](/documentation/features/environments)
* [Collections](/documentation/features/collections)
* [History](/documentation/features/history)


# History
Source: https://docs.hoppscotch.io/documentation/features/history

Store and access your previous requests and responses.

Hoppscotch helps you to keep track of your requests and responses. You can access the history of your requests by clicking on the "**History**" icon on the side panel.

## Save requests to history

To save a request to your history, you can click on the "Send" button on the request page. Hoppscotch will automatically save the request to your history.

## Accessing requests from history

To access a request from your history, click on the desired request in the history section. You can also access a request from your history by clicking on the "**History**" icon on the side panel.

## Favorite requests

You can favorite a request by clicking on the "**Favorite**" button on the history entry's options. Click on the "**Favorite**" button again to unfavorite the request. Favorite requests can be filtered by clicking on the "**Filter**" button in the history section and selecting the "**Favorites**" filter.

## Filter history

You can filter your history by clicking on the "**Filter**" button in the history section and selecting the desired filter.

## Deleting requests from history

To delete a request from your history, click on the "**Delete**" button on the history entry's options. You can also delete all requests from your history by clicking on the "**Clear history**" button in the history section.


# Importer
Source: https://docs.hoppscotch.io/documentation/features/importer

Migrate your data from other tools into Hoppscotch.

Import data from other tools into Hoppscotch. You can import data from the following tools:

| Service            | Collections                                         | Environments |
| ------------------ | --------------------------------------------------- | ------------ |
| **Hoppscotch**     | ✓                                                   | ✓            |
| **Postman**        | ✓                                                   | ✓            |
| **Insomnia**       | ✓                                                   | ✓            |
| **OpenAPI**        | ✓                                                   |              |
| **HTTP Archive**   | ✓                                                   |              |
| **Other services** | [Contact support](/support/getting-started/contact) |              |

<Note> The size limit for importing collections varies by Hoppscotch edition. In **Hoppscotch Cloud**, you can import collections up to **10 MB**, while **Self-Hosted editions** allow imports of up to **50 MB**. </Note>

## Import from Hoppscotch

1. Export your Hoppscotch collection/environment to a JSON file.
2. Open Hoppscotch and click on the "**Import**" button on the collection/environment section.
3. Click on the "**Import from Hoppscotch**" tab.
4. Click on the "**Choose file**" button and select the JSON file you exported in step 1.
5. Click on the "**Import**" button.

## Import from Personal and other workspaces

1. Open Hoppscotch and click on the "**Import**" button on the collection section.
2. Click on the "**Import from another workspace**" tab.
3. Select the desired **workspace** from the drop-down menu.
4. Choose the "**collection**" from the list.
5. Click on the "**Import**" button.

### <Icon icon="download" />  What's Imported in the above 2 cases

* **Collections:** Complete set of request details, including parameters, request bodies, headers, authorization settings, pre-request scripts, test cases, request variables, response examples and collection-level properties are retained.
* **Environments:** Regular environment variables are imported.

<Info> **Secret variables' values** need to be manually entered as they aren't stored server-side for security reasons. </Info>

## Import from Postman

1. Export your Postman collection/environment to a JSON file.
2. Open Hoppscotch and click on the "**Import**" button on the collection/environment section.
3. Click on the "**Import from Postman**" tab.
4. Click on the "**Choose file**" button and select the JSON file you exported in step 1.
5. Click on the "**Import**" button.

<Info>
  **Experimental Script Import:** When importing Postman collections (v2.0/v2.1), Hoppscotch can now import pre-request scripts and test scripts as an experimental feature. You'll be prompted to consent to this import during the process. This enables seamless migration of your existing Postman workflows including their scripting logic with Chai.js-powered assertions through the `pm` namespace compatibility layer.
</Info>

### <Icon icon="download" />  What's Imported

* **Collections:** Query parameters from Postman are imported as request parameters and path parameters are imported as request variables. Request bodies, headers, and basic authorization are also imported. **Pre-request scripts and test cases** can now be imported (experimental, requires consent). Advanced authorization setups and collection-level settings aren't imported.
* **Environments:** Imports both regular and secret environment variables directly.

## Import from Insomnia

1. Export your Insomnia collection/environment to a JSON file.
2. Open Hoppscotch and click on the "**Import**" button on the collection/environment section.
3. Click on the "**Import from Insomnia**" tab.
4. Click on the "**Choose file**" button and select the JSON file you exported in step 1.
5. Click on the "**Import**" button.

### <Icon icon="download" />  What's Imported

* **Collections:** Request details like query parameters are imported as request parameters, and path parameters are imported as request variables. Request bodies, headers, and basic authorization settings are also imported. However, other sections like scripts, tests, and advanced authorization methods aren't synced.
* **Environments:** Regular environment variables are imported.

## Import from OpenAPI

There are two ways to import OpenAPI collections into Hoppscotch:

### 1. Import from File

1. Export your OpenAPI specification to a JSON file.
2. Open Hoppscotch and click on the "**Import**" button on the collection section.
3. Click on the "**Import from OpenAPI**" tab.
4. Select **Import from File** option.
5. Click on the "**Choose file**" button and select the JSON file you exported in step 1.
6. Click on the "**Import**" button.

### 2. Import from URL

1. Copy the URL of your OpenAPI specification.
2. Open Hoppscotch and click on the "**Import**" button on the collection section.
3. Click on the "**Import from OpenAPI**" tab.
4. Select **Import from URL** option
5. Click on the "**Import from URL**" field and paste the URL that you copied in step 1.
6. Click on the "**Import**" button.

### <Icon icon="download" />  What's Imported

* **Collections:** Query parameters are imported as request parameters, and path parameters are imported as request variables. Authorization methods, headers, and response examples are also included. However, details like request bodies, scripts, and tests aren't imported.

## Import from HAR

1. Export the HTTP Archive (HAR) file from your browser or network monitoring tool.
2. Open Hoppscotch and click on the "**Import**" button on the collection section.
3. Click on the "**Import from HAR**" tab.
4. Click on the "**Choose file**" button and select the HAR file you exported in step 1.
5. Click on the "**Import**" button.

### <Icon icon="download" />  What's Imported

* **Collections:** Imports request headers and body content. Additional metadata or settings aren't included in this format.

## Import from other services

* If you want to import data from other services, please [contact support](/support/getting-started/contact) and we will help you out.

### Import from cURL

You can import cURL commands into Hoppscotch in the following ways:

* **Copy and paste**: Copy and paste the cURL command into the Hoppscotch URL bar.
* **Send drop-down menu**: Click on the send drop-down menu and select "**Import cURL**". Paste the cURL command into the text area and click on the "**Import**" button.


# Inspections
Source: https://docs.hoppscotch.io/documentation/features/inspections

Detect and resolve configuration errors in your API requests.

Hoppscotch inspections offer a powerful solution for debugging API requests, assisting in reducing errors due to misconfigured user inputs.

Hoppscotch inspections are designed to streamline the process of identifying and rectifying errors stemming from improperly configured API request inputs. When an input section within the application is not properly configured, Inspections will visually alert users by displaying an alert icon. This icon serves as an indicator that potential issues are present in the configuration.

## Inspecting Configuration Errors

Upon clicking the alert icon, the Inspections panel will provide an overview of possible configuration errors that might be hindering the accomplishment of your intended goal and ways to resolve the errors.


# Interceptor
Source: https://docs.hoppscotch.io/documentation/features/interceptor

Intercept and modify requests and responses.

You can access APIs blocked by `Cross-Origin Resource Sharing (CORS)` restriction by using either Hoppscotch Agent, Proxyscotch or custom middleware. You can also use the Hoppscotch web extension to intercept requests and responses.

<Tabs>
  <Tab title="Hoppscotch Agent">
    ## Hoppscotch Agent

    The Hoppscotch Agent is a micro application designed to mitigate the challenges posed by `CORS` in modern web browsers. Acting as a local intermediary, it intercepts API requests made through the Hoppscotch web app and reroutes them through your local machine. This means that the Hoppscotch Agent handles requests using your local network configuration.

    1. Download the Hoppscotch Agent for your operating system:

    <AccordionGroup>
      <Accordion title="Mac" icon="apple">
        <Card title="Apple Silicon (.dmg)" href="https://github.com/hoppscotch/agent-releases/releases/latest/download/Hoppscotch_Agent_mac_aarch64.dmg">
          Download for Apple Silicon-based Mac.
        </Card>

        <Card title="Intel (.dmg)" href="https://github.com/hoppscotch/agent-releases/releases/latest/download/Hoppscotch_Agent_mac_x64.dmg">
          Download for Intel-based Mac.
        </Card>
      </Accordion>

      <Accordion title="Windows" icon="windows">
        <Card title="Windows Installer (.msi)" href="https://github.com/hoppscotch/agent-releases/releases/latest/download/Hoppscotch_Agent_win_x64.msi">
          Download the installer for Windows (64-bit).
        </Card>

        <Card title="Windows Portable (.exe)" href="https://github.com/hoppscotch/agent-releases/releases/latest/download/Hoppscotch_Agent_win_x64_portable.zip">
          Download the portable version for Windows (64-bit).
        </Card>
      </Accordion>

      <Accordion title="Linux" icon="linux">
        <Card title="Debian (.deb)" href="https://github.com/hoppscotch/agent-releases/releases/latest/download/Hoppscotch_Agent_linux_x64.deb">
          Download the Debian package for Debian-based Linux distributions.
        </Card>

        <Card title="App Image (.AppImage)" href="https://github.com/hoppscotch/agent-releases/releases/latest/download/Hoppscotch_Agent_linux_x64.AppImage">
          Download the AppImage for Linux.
        </Card>
      </Accordion>
    </AccordionGroup>

    2. Open [Hoppscotch](https://hoppscotch.io) app and navigate to the "**Interceptors**" section in the **"Settings"** page.
    3. Locate the "**Agent**" option within the Interceptors section to initiate a connection to your local agent.
    4. The application will prompt you for a "**One-Time Verification Code**". This verification code will be generated within the Hoppscotch Agent.
    5. Enter the verification code into the application to establish a secure connection.

    Once connected, all API requests made through the Hoppscotch web app will be routed through Hoppscotch agent, effectively eliminating CORS-related issues.

    <Tip>Recommended interceptor for most users as it is compaitble with all platforms.</Tip>
  </Tab>

  <Tab title="Proxy">
    ## Proxy

    A proxy server acts as an intermediary between your device and the internet, forwarding requests and responses to and from the desired API. By routing requests through a proxy, you can bypass CORS restrictions and access APIs that would otherwise be blocked by the browser.

    * Enable proxy interceptor from "[**Settings page**](https://hoppscotch.io/settings)" under the **Interceptors** section.
    * You can replace the default Proxy URL with your own proxy middleware if you wish or use [Proxyscotch](https://github.com/hoppscotch/proxyscotch), which acts as a remote proxy server for routing API requests.

    ## Proxyscotch

    [Proxyscotch](https://github.com/hoppscotch/proxyscotch) is our official proxy server. It is an MIT licensed open-source project that can bypass Cross-Origin Resource Sharing (CORS) restrictions by routing API requests through a remotely hosted proxy, ensuring that requests originate from a trusted environment.

    #### Self-Hosted Proxyscotch

    To use Proxyscotch with a minimal setup, you can pull and run the official pre-built Docker image. This provides an instant proxy environment without requiring manual compilation or installation.
    You can host Proxyscotch on your own server by following the instructions below:

    ```bash theme={null}
    # Pull the latest Proxyscotch image from Docker Hub
    docker pull hoppscotch/proxyscotch

    # Run the container in detached mode, exposing port 9159
    docker run -d -p 9159:9159 --name proxyscotch hoppscotch/proxyscotch
    ```

    #### Proxyscotch Installer

    If you prefer a native installation, download and install both the Desktop and Server binaries for your operating system.

    <AccordionGroup>
      <Accordion title="Mac" icon="apple">
        <Card title="Tray application (macOS)" href="https://github.com/hoppscotch/proxyscotch/releases/latest/download/Proxyscotch-Desktop-macOS-v0.1.1.zip">
          Download proxyscotch for macOS desktops. This will install the tray application for seamless proxy management.
        </Card>

        <Card title="Proxy Server Binary (Intel-based macOS)" href="https://github.com/hoppscotch/proxyscotch/releases/latest/download/proxyscotch-server-darwin-amd64-v0.1.1">
          Download the proxy server binary for Intel-based (x86-64) Macs.
        </Card>

        <Card title="Proxy Server Binary (Apple Silicon macOS)" href="https://github.com/hoppscotch/proxyscotch/releases/latest/download/proxyscotch-server-darwin-arm64-v0.1.1">
          Download the proxy server binary for Apple Silicon-based (ARM64) Macs.
        </Card>
      </Accordion>

      <Accordion title="Windows" icon="windows">
        <Card title="Tray application (Windows - AMD)" href="https://github.com/hoppscotch/proxyscotch/releases/latest/download/Proxyscotch-Desktop-Windows-amd64-v0.1.1.exe">
          Download proxyscotch for AMD-based Windows desktops. This will install the tray application for easy proxy management.
        </Card>

        <Card title="Proxy Server Binary (Windows - AMD)" href="https://github.com/hoppscotch/proxyscotch/releases/latest/download/proxyscotch-server-windows-amd64-v0.1.1.exe">
          Download the proxy server binary for AMD-based Windows machines.
        </Card>

        <Card title="Tray application (Windows - ARM)" href="https://github.com/hoppscotch/proxyscotch/releases/latest/download/proxyscotch-arm64.exe">
          Download proxyscotch for ARM-based Windows desktops. This will install the tray application for easy proxy management.
        </Card>

        <Card title="Proxy Server Binary (Windows - ARM)" href="https://github.com/hoppscotch/proxyscotch/releases/latest/download/proxyscotch-server-windows-arm64-v0.1.1.exe">
          Download the proxy server binary for ARM-based Windows machines.
        </Card>
      </Accordion>

      <Accordion title="Linux" icon="linux">
        <Card title="Tray application (Linux - AMD)" href="https://github.com/hoppscotch/proxyscotch/releases/latest/download/Proxyscotch-Desktop-Linux-amd64-v0.1.1">
          Download proxyscotch for AMD-based Linux desktops. This will install the tray application for seamless proxy management.
        </Card>

        <Card title="Proxy Server Binary (Linux - AMD)" href="https://github.com/hoppscotch/proxyscotch/releases/latest/download/proxyscotch-server-linux-amd64-v0.1.1">
          Download the proxy server binary for AMD-based Linux machines.
        </Card>
      </Accordion>
    </AccordionGroup>

    <Note>
      The proxy will add a **desktop application to your system tray**, providing quick access to various proxy settings such as setting the access token. After launching the application, a dialog will prompt you to complete the **certificate installation** process. For more details on how to install the certificate, [visit this wiki](https://github.com/hoppscotch/proxyscotch/wiki/Certificate-Installation).

      Upon activation, the **server** will run in the background and interact with the proxy to route and manage requests.
    </Note>

    ### Building Proxyscotch from Source

    If you prefer to build and run Proxyscotch manually from source, you can clone the repository and compile the binaries for your platform.

    ```bash theme={null}
    git clone https://github.com/hoppscotch/proxyscotch.git 
    ```

    Follow the platform-specific instructions below to build the proxy and server from source for your operating system:

    <AccordionGroup>
      <Accordion title="Building on macOS" icon="apple">
        ```bash theme={null}
        # Build the desktop tray application
        ./build.sh darwin

        # Build the standalone server application
        ./build.sh darwin server
        ```
      </Accordion>

      <Accordion title="Building on Windows" icon="windows">
        You can use Git Bash to run the following commands:

        ```bash theme={null}
        # Build the desktop tray application
        ./build.sh windows

        # Build the standalone server application
        ./build.sh windows server
        ```
      </Accordion>

      <Accordion title="Building on Linux" icon="linux">
        ```bash theme={null}
        # Build the desktop tray application
        ./build.sh linux

        # Build the standalone server application
        ./build.sh linux server
        ```
      </Accordion>
    </AccordionGroup>

    <Tip> After building, the compiled binaries will be available in the `out/` directory. </Tip>

    #### Running the Proxyscotch Server

    After building the server, use the following command to start the proxy server:

    ```bash theme={null}
    $ ./out/<platform>-server/server --host="<hostname>:<port>" --token="<token_or_blank>"

    # e.g. on Linux
    $ ./out/linux-server/server --host="localhost:9159" --token=""

    # or on Windows
    $ ./out/windows-server/server.exe --host="localhost:9159" --token=""
    ```

    <Warning> When the **token is left blank**, it grants unrestricted access to your proxy server. While this might be convenient, please be aware of the potential security risks and consider whether this level of open access is appropriate for your use case. </Warning>

    #### Available Server Options

    After running the Proxyscotch server, you can customize its behavior using various command-line options.

    | **Option**                    | **Description**                                                            |
    | ----------------------------- | -------------------------------------------------------------------------- |
    | `--host="<hostname>:<port>"`  | Define the host and port (default: `localhost:9159`).                      |
    | `--token="<token>"`           | Set an access token to restrict proxy usage (leave blank for open access). |
    | `--allowed-origins="*"`       | Comma-separated list of allowed origins for CORS.                          |
    | `--banned-outputs="<values>"` | Comma-separated list of response values to redact.                         |
    | `--banned-dests="<hosts>"`    | Comma-separated list of blocked destination hosts.                         |

    ### Configure Proxyscotch in Hoppscotch

    Once the container is running or the server is active, configure Hoppscotch to use `http://localhost:9159` as the Proxy URL in the "**Settings**" page.

    This setup will route all API requests through Proxyscotch, facilitating communication with APIs that enforce strict CORS policies.
  </Tab>

  <Tab title="Browser Extension">
    ## Browser Extension

    Since `CORS` is as simple as adding some HTTP headers, it's only blocked by the browser. You can build some proxy-like component that will make a call for you and get the response from the desired API. You add it to the headers and then send it back to Hoppscotch.

    ### How to use the Browser Extension

    1. Install the browser extension from the below links:

       * [<Icon icon="chrome" />  Chrome](https://chrome.google.com/webstore/detail/hoppscotch-browser-extens/amknoiejhlmhancpahfcfcfhllgkpbld?hl=en)
       * [<Icon icon="firefox" />  Firefox](https://addons.mozilla.org/en-US/firefox/addon/hoppscotch)

    2. Click on the Hoppscotch Browser Extension icon from the browser toolbar and ensure that `hoppscotch.io` is in your active origins. If you are using Hoppscotch Self-Host, add your own domain as a new origin

       <Frame>
         <img />

         <img />
       </Frame>

    3. Refresh the Hoppscotch web app.

    4. Open the interceptor and change the middleware to the browser extension

       You can either go to the settings and enable the use of the browser extension as shown below:

       <Frame>
         <img />

         <img />
       </Frame>

       Or you can open the interceptor menu and change the middleware as shown below:

       <Frame>
         <img />

         <img />
       </Frame>

       ### Origins

       The origin list defines the URLs that the extension can connect to. If you're using hoppscotch.io, then you do not need to add any other origins. However, if you are using a self-hosted instance, you should add the domain of your self-hosted instance as an active origin.
  </Tab>
</Tabs>


# API Mocking
Source: https://docs.hoppscotch.io/documentation/features/mock

Create mock servers to simulate API endpoints and iterate on your API design without touching a backend.

Hoppscotch API Mocking lets you stand up mock servers that return predictable responses to HTTP requests. It's ideal for prototyping, front‑end development, contract-first API design, demos, and testing failure/latency scenarios, now built right into Hoppscotch.

## What you can do

* Spin up mock servers without writing code
* Define routes by method and path (with path params and queries)
* Return custom status codes, headers, and bodies
* Choose between static and dynamic responses (with [Variables](/documentation/features/variables))
* Simulate latency and flaky behaviors for realism
* Organize and reuse mocks with [Collections](/documentation/features/collections) and [Environments](/documentation/features/environments)
* Collaborate via [Workspaces](/documentation/features/workspaces)

## Create a mock server

You can create a mock server from scratch or from an existing Collection.

1. New mock server
   * Click "New"
   * Select source collection
   * Provide a mock server name
   * Choose a response delay

2. From a Collection
   * Select a Collection menu, then click "Configure Mock Server"
   * Provide a mock server name
   * Choose a response delay
   * Each request/example becomes an initial mock route you can refine

Once created, you'll get a mock server URL you can call from your app or your Hoppscotch requests.

<Tip>Keep the mock server URL in an Environment variable, for example `{{MOCK_BASE_URL}}`, so you can swap between mock and real servers easily.</Tip>

## Define routes and responses

A mock server is made of one or more routes. Each route matches an incoming request and returns a configured response.

Route fields:

* Method: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`
* Path: Supports path params and query strings
* Matching: Optional header and query matchers to choose the correct example
* Response: Status code, headers, body, and artificial latency

### Example route

Request

```
GET /users/42
```

Response

```json theme={null}
{
	"id": 42,
	"name": "Jane Doe",
	"role": "admin"
}
```

### Dynamic responses with variables

Use Hoppscotch variables to make responses dynamic and realistic.

* Timestamps: `{{timestamp}}`
* UUIDs: `{{uuid}}`
* Environment values: `{{ENV_NAME}}`

Example dynamic body:

```json theme={null}
{
	"requestId": "{{uuid}}",
	"generatedAt": "{{timestamp}}",
	"region": "{{REGION}}"
}
```

You can also reference variables in headers, for example `X-Request-ID: {{uuid}}`.

## Save a response as an Example

In Hoppscotch, you can save responses as examples to quickly populate mock routes with realistic data. Examples capture both the request configuration and its actual response, making it easy to convert real API behavior into mock endpoints.

**To save a response as an example:**

1. Navigate to the right-sidebar and select the collection with your request
2. Choose the request and click **"Send"**
3. In the response section, click the **"Save as Example"** icon
4. The example will be stored in the request's history within the collection

**Using examples in mock servers:**

* When creating a mock server from a Collection, each saved example automatically becomes a mock route
* Examples preserve the exact response status, headers, and body you received
* You can edit examples to adjust the mock response (modify status codes, add headers, introduce delays)
* Multiple examples for the same request let you simulate different scenarios (success, errors, edge cases)

**Example workflow:**

1. Call your API endpoint and receive a response
2. Save that response as an example
3. Create a mock server from the collection
4. The mock route now returns the exact response you captured
5. Edit the example to add delays or modify data for testing

<Tip>Use examples to quickly bootstrap realistic mock data from your actual API, then refine them to test edge cases and failure scenarios.</Tip>

## Latency, errors, and headers

Control the realism of your mocks by tuning:

* Status: 2xx, 3xx, 4xx, 5xx
* Headers: `Content-Type`, `Cache-Control`, custom headers
* Delay: Add fixed or ranged latency (for example, 250–1500 ms)

<Tip>Simulate network timeouts by setting a delay higher than your client's timeout to test retry logic.</Tip>

## Using mocks with Collections and Environments

* Save your mock routes alongside requests in a Collection for easy reuse
* Store the mock server base URL in an Environment, for example `{{MOCK_BASE_URL}}`
* Switch between mock and real backends by toggling the Environment variable

Example request target:

```
{{MOCK_BASE_URL}}/orders?limit=10
```

## Collaboration and sharing

Mocks live in your workspace, so teammates can:

* View and edit routes and examples
* Fork Collections and iterate on contracts
* Use the same Environments to keep URLs and tokens in sync

## Best practices

* Keep contracts first: define mocks before building the backend
* Add negative cases early (400/401/403/409/429/500) to harden clients
* Use example names that describe intent (for example, “empty list”, “invalid token”)
* Centralize variables (for example, `{{MOCK_BASE_URL}}`, `{{REGION}}`) in Environments
* Review and version mocks with your Collection changes

## Troubleshooting

* 404 from mock: Ensure the method and path match exactly (including base path), and check example matching rules
* Wrong example returned: Inspect header/query matchers and example priorities
* CORS errors in the browser: Add `Access-Control-Allow-Origin: *` (or your origin) to the response headers
* Timeouts: Reduce mock delay or increase your client timeout

## FAQs

### How do mocks differ from live endpoints?

Mocks return predefined responses based on your rules. They don't execute business logic or touch data stores.

### Can I generate mocks from my existing requests?

Yes. You can bootstrap routes from saved requests or examples in a Collection and refine them.

### Can I parametrize responses without code?

Yes. Use Hoppscotch variables (UUID, timestamp, and Environment values) directly in response bodies and headers.

### Can I self‑host mock servers?

Yes. See [Self‑host](/documentation/self-host/getting-started) for details on deploying Hoppscotch in your own infrastructure.

## Related

* [Collections](/documentation/features/collections)
* [Environments](/documentation/features/environments)
* [Variables](/documentation/features/variables)
* [Tests](/documentation/features/tests)
* [Workspaces](/documentation/features/workspaces)


# Personal Access Token
Source: https://docs.hoppscotch.io/documentation/features/pat

Securely connect your Hoppscotch account with other services within Hoppscotch ecosystem.

A Personal Access Token (PAT) in Hoppscotch acts as a secure authentication method,
allowing you to smoothly link your Hoppscotch API client, on Hoppscotch cloud or self-host, with the Hoppscotch CLI.

## Generating Personal Access Token

Follow these steps to create a new token, manage its settings. Personal access tokens cannot be used to access data in your personal workspace.

1. Login into the Hoppscotch API client using your credentials.

2. Once logged in, navigate to your profile settings by clicking on your profile icon, located in the top right corner of the screen.

3. In the profile settings menu, locate and click on `Personal Access Tokens`.

4. Within the Personal Access Tokens section, find the option to "Generate New Token" and click on it.

5. Provide a brief description under **Label** to remind yourself of the token's purpose and select an expiration date for the token. Options typically include 7 days, 30 days, 60 days, 90 days, or set it to never expire.

<Note> Once a Personal Access Token (PAT) is generated with **read-only access** permissions, it cannot be modified. Please review the token settings carefully before generating it to ensure it meets your access requirements.</Note>

6. After generating the token, it will be securely displayed. Use the **copy icon** to copy the token to your clipboard for immediate use.

7. If you decide that you no longer need the token, you can delete it by navigating back to your profile page.

<Warning> Remember, deleted tokens cannot be recovered.</Warning>

8. Once you've copied or saved your PAT, you can use it to authenticate API requests across different Hoppscotch services.

## Enterprise Token Management

In Self-Hosted Enterprise settings, users with Admin privileges have additional capabilities for managing Personal Access Tokens (PATs).

1. Admin can **oversee and manage** tokens generated by all users within the enterprise environment.
2. An Admin also possesses the **authority to delete** tokens under their purview. This capability ensures compliance with security protocols and allows for the removal of tokens that are no longer necessary or have expired.


# Realtime API Testing
Source: https://docs.hoppscotch.io/documentation/features/realtime-api-testing

Welcome to the home of your new documentation

Hoppscotch's Realtime API platform helps you test your real-time APIs easily.

It's primarily divided into two sections the request section and the response section.

## Request

The request section houses the feature to enter your server endpoint and initiate a connection. You also get the option to choose from four different protocols `WebSocket`, `SSE`, `Socket.IO`, and `MQTT`.

## Response

Once the connection is established, you can view the responses and logs in the response section.

<Card title="Getting started with Realtime" icon="circle-arrow-right" href="/documentation/getting-started/realtime/websocket">
  Read out step by step tutorial on working with Realtime protocols.
</Card>


# RESTful API Testing
Source: https://docs.hoppscotch.io/documentation/features/rest-api-testing

Test and play around with your RESTful API endpoints.

Hoppscotch's REST API platform provides you with a fast and seamless experience to test and debug your API endpoints.

It's primarily divided into two sections along with other features to help you build better APIs.

## Request

The request section provides you the capability to define your API endpoint and initiate the communication.

You can select from a range of HTTP methods such as `GET`, `POST`, `PUT` etc. You can read more about HTTP methods in [RESTful protocol](/documentation/protocols/rest).

You can also add dynamic behaviors to your requests by specifying `Headers`, `Request Body`, `Authorization Headers`, `Parameters`, and `Pre-request scripts`.

Hoppscotch also provides the capability to run `Tests` on the responses you receive.

## Response

This is where you see the responses to your API endpoints. You can download and copy the returned responses for further use.

## Other features

The REST API platform also houses other features like:

* [Environments](/documentation/features/environments)
* [Collections](/documentation/features/collections)
* [History](/documentation/features/history)


# Runner
Source: https://docs.hoppscotch.io/documentation/features/runner

Iterate and execute your requests in a collection.

The Runner is a powerful tool that allows you to run a collection of requests sequentially. You can also configure the run settings to suit your needs.

## Running a Collection

To run a collection:

* Right-click on the collection and select the "**Run Collection**" option.
* Alternatively, hover over the collection name and click on the "**Run Collection**" icon.

You can choose to run the collection from the CLI or through the web interface based on your preference. A new tab will open where you can configure the run settings as described below.

## Run Settings

1. **Delay**: Set an interval delay (in milliseconds) between running each request.
2. **Stop Run if Error Occurs**: The collection run stops if an error is encountered within a script or if there's a problem sending a request.
3. **Persist Responses**: Log response headers and bodies for review after running the collection. Note that persisting responses may impact performance for large collections.
4. **Keep Variable Values**: Persist the variables used in the run, so any updates made to the variables during the run will retain their changes after completion.

## Executing the Run

After setting up your preferences, start the collection runner. A new tab will display, showing real-time execution details, including:

* **Collection**: The name of the collection being executed.
* **Environment**: The active environment at runtime.
* **Duration**: Total time taken to complete the run.
* **Average Response Time**: The mean response time across all requests.

### Running and Post-Run Actions

* **Stop**: Stop the current run at any time.
* **Run Again**: When a run completes, you can restart with the same configurations as needed.
* **New Run**: Stop the current run and restart with new settings.

## Runner Results

The results view provides a comprehensive summary of your collection run, including:

* **Request Status**: Success or failure of each request, along with HTTP status codes.
* **Tests**: Detailed views of tests that passed or failed.
* **Persisted Responses**: If enabled, view headers and bodies by selecting each request; otherwise, this section remains hidden.


# Scripts
Source: https://docs.hoppscotch.io/documentation/features/scripts

Write pre-request scripts and build tests.

<Tabs>
  <Tab title="hopp [Experimental]">
    <Danger>
      It is not recommended to migrate or reformat your existing scripts to the new scripting APIs at this time. Upcoming updates are expected to introduce breaking changes as we continue to refine and improve the scripting experience.

      The current rollout is intentionally gradual, allowing us to gather user feedback and iterate based on real-world usage.

      All further updates to scripting will be scoped to the experimental scripting sandbox, which is the default, and the preference can be updated from `Settings → Experiments`.

      [Your feedback will be invaluable as we shape the next generation of Hoppscotch scripting.](https://github.com/hoppscotch/hoppscotch/discussions/5221)
    </Danger>

    <Note>
      This new experimental implementation provides a robust foundation for API scripting with enhanced capabilities for environment management, request manipulation, response processing, cookie handling, and comprehensive testing. The new system maintains backwards compatibility while introducing powerful new features for modern API testing workflows.
    </Note>

    ## `hopp.env` Namespace

    Environment variable management with scope-specific operations and enhanced functionality.

    ### `hopp.env.get(key: string)`

    Retrieves the value of the selected environment's variable. Accepts an environment variable as an argument.

    ```javascript theme={null}
    hopp.env.get("variable");
    hopp.env.get("baseURL");
    ```

    ### `hopp.env.getRaw(key: string)`

    Retrieves the raw value of the selected environment's variable without variable resolution.

    ```javascript theme={null}
    hopp.env.getRaw("variable");
    ```

    ### `hopp.env.set(key: string, value: string)`

    Sets the value of an environment variable in the selected environment.

    ```javascript theme={null}
    hopp.env.set("baseURL", "https://httpbin.org");
    ```

    ### `hopp.env.delete(key: string)`

    Deletes an environment variable from the selected environment.

    ```javascript theme={null}
    hopp.env.delete("baseURL");
    ```

    ### `hopp.env.reset(key: string)`

    Resets an environment variable to its initial value in the selected environment.

    ```javascript theme={null}
    hopp.env.reset("baseURL");
    ```

    ### `hopp.env.getInitialRaw(key: string)`

    Retrieves the initial raw value of an environment variable.

    ```javascript theme={null}
    hopp.env.getInitialRaw("baseURL");
    ```

    ### `hopp.env.setInitial(key: string, value: string)`

    Sets the initial value of an environment variable.

    ```javascript theme={null}
    hopp.env.setInitial("baseURL", "https://httpbin.org");
    ```

    #### Active Environment Scope

    Operations specific to the currently active environment.

    ### `hopp.env.active.get(key: string)`

    Retrieves the value of the active environment's variable.

    ```javascript theme={null}
    hopp.env.active.get("variable");
    ```

    ### `hopp.env.active.getRaw(key: string)`

    Retrieves the raw value of the active environment's variable.

    ```javascript theme={null}
    hopp.env.active.getRaw("variable");
    ```

    ### `hopp.env.active.set(key: string, value: string)`

    Sets the value of an active environment variable.

    ```javascript theme={null}
    hopp.env.active.set("baseURL", "https://httpbin.org");
    ```

    ### `hopp.env.active.delete(key: string)`

    Deletes a variable from the active environment.

    ```javascript theme={null}
    hopp.env.active.delete("baseURL");
    ```

    ### `hopp.env.active.reset(key: string)`

    Resets a variable in the active environment to its initial value.

    ```javascript theme={null}
    hopp.env.active.reset("baseURL");
    ```

    ### `hopp.env.active.getInitialRaw(key: string)`

    Retrieves the initial raw value of an active environment variable.

    ```javascript theme={null}
    hopp.env.active.getInitialRaw("baseURL");
    ```

    ### `hopp.env.active.setInitial(key: string, value: string)`

    Sets the initial value of an active environment variable.

    ```javascript theme={null}
    hopp.env.active.setInitial("baseURL", "https://httpbin.org");
    ```

    #### Global Environment Scope

    Operations specific to the global environment.

    ### `hopp.env.global.get(key: string)`

    Retrieves the value of the global environment's variable.

    ```javascript theme={null}
    hopp.env.global.get("variable");
    ```

    ### `hopp.env.global.getRaw(key: string)`

    Retrieves the raw value of the global environment's variable.

    ```javascript theme={null}
    hopp.env.global.getRaw("variable");
    ```

    ### `hopp.env.global.set(key: string, value: string)`

    Sets the value of a global environment variable.

    ```javascript theme={null}
    hopp.env.global.set("baseURL", "https://httpbin.org");
    ```

    ### `hopp.env.global.delete(key: string)`

    Deletes a variable from the global environment.

    ```javascript theme={null}
    hopp.env.global.delete("baseURL");
    ```

    ### `hopp.env.global.reset(key: string)`

    Resets a variable in the global environment to its initial value.

    ```javascript theme={null}
    hopp.env.global.reset("baseURL");
    ```

    ### `hopp.env.global.getInitialRaw(key: string)`

    Retrieves the initial raw value of a global environment variable.

    ```javascript theme={null}
    hopp.env.global.getInitialRaw("baseURL");
    ```

    ### `hopp.env.global.setInitial(key: string, value: string)`

    Sets the initial value of a global environment variable.

    ```javascript theme={null}
    hopp.env.global.setInitial("baseURL", "https://httpbin.org");
    ```

    ## `hopp.request` Namespace

    Request manipulation with immutable properties and dedicated mutation functions.

    #### Read-only Properties

    ### `hopp.request.url`

    The request URL as a string.

    ```javascript theme={null}
    const url = hopp.request.url;
    ```

    ### `hopp.request.method`

    The HTTP method of the request.

    ```javascript theme={null}
    const method = hopp.request.method;
    ```

    ### `hopp.request.params`

    The query parameters of the request.

    ```javascript theme={null}
    const params = hopp.request.params;
    ```

    ### `hopp.request.headers`

    The headers of the request.

    ```javascript theme={null}
    const headers = hopp.request.headers;
    ```

    ### `hopp.request.body`

    The body of the request.

    ```javascript theme={null}
    const body = hopp.request.body;
    ```

    ### `hopp.request.auth`

    The authentication configuration of the request.

    ```javascript theme={null}
    const auth = hopp.request.auth;
    ```

    #### Mutation Functions (Pre-request Phase Only)

    ### `hopp.request.setUrl(url: string)`

    Sets the request URL.

    ```javascript theme={null}
    hopp.request.setUrl("https://api.example.com/users");
    ```

    ### `hopp.request.setMethod(method: string)`

    Sets the HTTP method of the request.

    ```javascript theme={null}
    hopp.request.setMethod("POST");
    ```

    ### `hopp.request.setHeader(name: string, value: string)`

    Sets a header on the request.

    ```javascript theme={null}
    hopp.request.setHeader("Authorization", "Bearer token");
    ```

    ### `hopp.request.setHeaders(headers: HoppRESTHeader[])`

    Sets multiple headers on the request.

    ```javascript theme={null}
    hopp.request.setHeaders([{ key: "Content-Type", value: "application/json" }]);
    ```

    ### `hopp.request.removeHeader(name: string)`

    Removes a header from the request.

    ```javascript theme={null}
    hopp.request.removeHeader("Authorization");
    ```

    ### `hopp.request.setParam(name: string, value: string)`

    Sets a query parameter on the request.

    ```javascript theme={null}
    hopp.request.setParam("userId", "123");
    ```

    ### `hopp.request.setParams(params: HoppRESTParam[])`

    Sets multiple query parameters on the request.

    ```javascript theme={null}
    hopp.request.setParams([{ key: "userId", value: "123" }]);
    ```

    ### `hopp.request.removeParam(name: string)`

    Removes a query parameter from the request.

    ```javascript theme={null}
    hopp.request.removeParam("userId");
    ```

    ### `hopp.request.setBody(body: Partial<HoppRESTReqBody>)`

    Sets the body of the request.

    ```javascript theme={null}
    hopp.request.setBody({ body: '{"key": "value"}' });
    ```

    ### `hopp.request.setAuth(auth: Partial<HoppRESTAuth>)`

    Sets the authentication for the request.

    ```javascript theme={null}
    hopp.request.setAuth({ authType: "bearer", token: "token" });
    ```

    #### Request Variables

    ### `hopp.request.variables.get(key: string)`

    Retrieves the value of a request variable.

    ```javascript theme={null}
    const value = hopp.request.variables.get("varName");
    ```

    ### `hopp.request.variables.set(key: string, value: string)`

    Sets the value of a request variable.

    ```javascript theme={null}
    hopp.request.variables.set("varName", "value");
    ```

    > Please note that only updates to request variables get persisted and reflected in the UI while the remaining are specific to the session.

    ## `hopp.response` Namespace

    Response access with multiple data formats and comprehensive metadata.

    #### Response Metadata

    ### `hopp.response.statusCode`

    The HTTP status code of the response.

    ```javascript theme={null}
    const status = hopp.response.statusCode;
    ```

    ### `hopp.response.statusText`

    The status text of the response.

    ```javascript theme={null}
    const statusText = hopp.response.statusText;
    ```

    ### `hopp.response.headers`

    The headers of the response.

    ```javascript theme={null}
    const headers = hopp.response.headers;
    ```

    ### `hopp.response.responseTime`

    The response time in milliseconds.

    ```javascript theme={null}
    const time = hopp.response.responseTime;
    ```

    ### Response Body Access Methods

    ### `hopp.response.body.asJSON()`

    Parses the response body as JSON.

    ```javascript theme={null}
    const data = hopp.response.body.asJSON();
    ```

    ### `hopp.response.body.asText()`

    Returns the response body as text.

    ```javascript theme={null}
    const text = hopp.response.body.asText();
    ```

    ### `hopp.response.body.bytes()`

    Returns the response body as a Uint8Array.

    ```javascript theme={null}
    const bytes = hopp.response.body.bytes();
    ```

    ## `hopp.cookies` Namespace

    Domain-aware cookie management with comprehensive CRUD operations.

    ### `hopp.cookies.get(domain: string, cookieName: string)`

    Retrieves a cookie by domain and name.

    ```javascript theme={null}
    const cookie = hopp.cookies.get("example.com", "sessionId");
    ```

    ### `hopp.cookies.set(domain: string, cookie: Cookie)`

    Sets a cookie for a domain.

    ```javascript theme={null}
    hopp.cookies.set("example.com", {
      name: "session_id",
      value: "abc123",
      domain: "api.example.com",
      path: "/api",
      expires: new Date(Date.now() + 86400000).toISOString(), // 24 hours from now
      maxAge: 86400, // 24 hours in seconds
      httpOnly: true,
      secure: true,
      sameSite: "Lax",
    });
    ```

    ### `hopp.cookies.has(domain: string, cookieName: string)`

    Checks if a cookie exists for a domain.

    ```javascript theme={null}
    const exists = hopp.cookies.has("example.com", "sessionId");
    ```

    ### `hopp.cookies.getAll(domain: string)`

    Retrieves all cookies for a domain.

    ```javascript theme={null}
    const cookies = hopp.cookies.getAll("example.com");
    ```

    ### `hopp.cookies.delete(domain: string, cookieName: string)`

    Deletes a cookie for a domain.

    ```javascript theme={null}
    hopp.cookies.delete("example.com", "sessionId");
    ```

    ### `hopp.cookies.clear(domain: string)`

    Clears all cookies for a domain.

    ```javascript theme={null}
    hopp.cookies.clear("example.com");
    ```

    ## `hopp.test` and `hopp.expect` Testing Framework

    Comprehensive testing API with custom assertions and Chai.js-powered BDD assertions for advanced API testing.

    ### `hopp.test(testName: string, testFunction: () => void)`

    Creates a group of tests with a name.

    ```javascript theme={null}
    hopp.test("API Tests", () => {
      hopp.expect(1).toBe(1);
    });
    ```

    ### `hopp.expect(actual: any)`

    Returns an expectation object for assertions. Hoppscotch extends the testing framework with comprehensive Chai.js BDD assertion support, enabling advanced testing patterns with 50+ assertion methods.

    ```javascript theme={null}
    hopp.expect(value).toBe(expected);
    ```

    #### Basic Custom Assertions

    ### `hopp.expect(value).toBe(expected: any)`

    Tests for exact equality.

    ```javascript theme={null}
    hopp.expect(1).toBe(1);
    ```

    ### `hopp.expect(value).toBeType(type: string)`

    Tests for type equality.

    ```javascript theme={null}
    hopp.expect("hello").toBeType("string");
    ```

    ### `hopp.expect(value).toHaveLength(number: number)`

    Tests that a value has a specific length.

    ```javascript theme={null}
    hopp.expect([1,2,3]).toHaveLength(3);
    ```

    ### `hopp.expect(value).toInclude(item: any)`

    Tests that a value includes an item.

    ```javascript theme={null}
    hopp.expect([1,2,3]).toInclude(2);
    ```

    #### HTTP Status Code Level Assertions

    ### `hopp.expect(statusCode).toBeLevel2xx()`

    Tests that the status code is in the 2xx range.

    ```javascript theme={null}
    hopp.expect(200).toBeLevel2xx();
    ```

    ### `hopp.expect(statusCode).toBeLevel3xx()`

    Tests that the status code is in the 3xx range.

    ```javascript theme={null}
    hopp.expect(302).toBeLevel3xx();
    ```

    ### `hopp.expect(statusCode).toBeLevel4xx()`

    Tests that the status code is in the 4xx range.

    ```javascript theme={null}
    hopp.expect(404).toBeLevel4xx();
    ```

    ### `hopp.expect(statusCode).toBeLevel5xx()`

    Tests that the status code is in the 5xx range.

    ```javascript theme={null}
    hopp.expect(500).toBeLevel5xx();
    ```

    #### Negation Support

    All assertions support `.not` for negation.

    ```javascript theme={null}
    hopp.expect(1).not.toBe(2);
    hopp.expect("hello").not.toBeType("number");
    hopp.expect([1,2]).not.toHaveLength(3);
    hopp.expect([1,2]).not.toInclude(3);
    hopp.expect(200).not.toBeLevel4xx();
    ```

    ## Chai.js Assertion Support

    Hoppscotch includes comprehensive Chai.js BDD assertion support through `hopp.expect()` for native scripts and `pm.expect()` for Postman compatibility, enabling advanced testing patterns with 50+ assertion methods.

    ### Type Assertions

    Check value types and instances:

    ```javascript theme={null}
    // Basic type checking
    hopp.test("Type validation", () => {
      hopp.expect(hopp.response.statusCode).to.be.a('number')
      hopp.expect(hopp.response.body.asJSON()).to.be.an('object')
      hopp.expect([1, 2, 3]).to.be.an.instanceOf(Array)
      hopp.expect(new Date()).to.be.an.instanceOf(Date)
    })
    ```

    ### Equality Assertions

    Test for strict and deep equality:

    ```javascript theme={null}
    hopp.test("Equality checks", () => {
      hopp.expect(hopp.response.statusCode).to.equal(200)
      hopp.expect(hopp.response.body.asJSON()).to.eql({ userId: 1, name: 'John' })
      hopp.expect(hopp.response.statusCode).to.deep.equal(200)
    })
    ```

    ### Property Assertions

    Validate object properties and nested structures:

    ```javascript theme={null}
    hopp.test("Response structure", () => {
      const data = hopp.response.body.asJSON()
      hopp.expect(data).to.have.property('userId')
      hopp.expect(data).to.have.own.property('email')
      hopp.expect(data).to.have.nested.property('profile.name')
      hopp.expect(data).to.have.all.keys('id', 'name', 'email')
      hopp.expect(data).to.have.any.keys('id', 'name')
    })
    ```

    ### Collection and Array Assertions

    Validate arrays and collections:

    ```javascript theme={null}
    hopp.test("Array validation", () => {
      const tags = hopp.response.body.asJSON().tags
      hopp.expect(tags).to.have.lengthOf(3)
      hopp.expect(tags).to.include('nodejs')
      hopp.expect(tags).to.have.members(['nodejs', 'javascript', 'api'])
      hopp.expect(tags).to.have.ordered.members(['api', 'javascript', 'nodejs'])
    })
    ```

    ### Numeric Comparisons

    Perform numeric comparisons and range checks:

    ```javascript theme={null}
    hopp.test("Numeric assertions", () => {
      const responseTime = hopp.response.responseTime
      hopp.expect(responseTime).to.be.below(500)
      hopp.expect(responseTime).to.be.above(0)
      hopp.expect(responseTime).to.be.within(0, 1000)
      hopp.expect(3.14159).to.be.closeTo(3.14, 0.01)
    })
    ```

    ### String Assertions

    Validate string content and patterns:

    ```javascript theme={null}
    hopp.test("String validation", () => {
      const contentType = hopp.response.headers['content-type']
      hopp.expect(contentType).to.include('application/json')
      hopp.expect(contentType).to.match(/^application\/json/)
      hopp.expect('hello').to.have.lengthOf(5)
    })
    ```

    ### Boolean State Assertions

    Check boolean values and states:

    ```javascript theme={null}
    hopp.test("Boolean checks", () => {
      hopp.expect(true).to.be.true
      hopp.expect(false).to.be.false
      hopp.expect(1).to.be.ok
      hopp.expect(null).to.be.null
      hopp.expect(undefined).to.be.undefined
      hopp.expect({}).to.exist
      hopp.expect([]).to.not.be.empty
    })
    ```

    ### Complex Assertion Chains

    Combine multiple assertions for comprehensive validation:

    ```javascript theme={null}
    hopp.test("Complex validation", () => {
      const data = hopp.response.body.asJSON()
      hopp.expect(data)
        .to.be.an('object')
        .and.have.property('userId')
        .that.is.a('number')
        .and.is.above(0)
    })
    ```

    ### Real-World Example: API Pagination

    ```javascript theme={null}
    hopp.test("Pagination metadata validation", () => {
      const data = hopp.response.body.asJSON()
      
      // Validate pagination structure
      hopp.expect(data).to.have.all.keys('items', 'page', 'total', 'hasMore')
      hopp.expect(data.items).to.be.an.instanceOf(Array)
      hopp.expect(data.items).to.have.lengthOf.at.most(50)
      
      // Validate each item
      data.items.forEach(item => {
        hopp.expect(item).to.have.all.keys('id', 'name', 'createdAt')
        hopp.expect(item.id).to.be.a('string')
      })
      
      // Store next page cursor
      if (data.hasMore) {
        hopp.env.active.set('nextPage', String(data.page + 1))
      }
    })
    ```

    ### Complete Assertion Reference

    **Type assertions:**

    * `.a(type)` / `.an(type)` - Check value type
    * `.instanceof(constructor)` - Check instance type

    **Equality assertions:**

    * `.equal(value)` / `.eq(value)` - Strict equality (===)
    * `.eql(value)` - Deep equality

    **Property assertions:**

    * `.property(name)` - Has property
    * `.own.property(name)` - Has own property (not inherited)
    * `.nested.property(path)` - Has nested property (e.g., 'a.b.c')

    **Collection assertions:**

    * `.include(value)` / `.contain(value)` - Contains value
    * `.members(array)` - Has members (order-independent)
    * `.ordered.members(array)` - Has members in order
    * `.keys(...keys)` - Has keys
    * `.lengthOf(n)` - Length equals n
    * `.lengthOf.at.least(n)` - Minimum length
    * `.lengthOf.at.most(n)` - Maximum length

    **Comparison assertions:**

    * `.above(n)` / `.gt(n)` - Greater than
    * `.below(n)` / `.lt(n)` - Less than
    * `.at.least(n)` / `.gte(n)` - Greater than or equal
    * `.at.most(n)` / `.lte(n)` - Less than or equal
    * `.within(min, max)` - Within range
    * `.closeTo(expected, delta)` - Approximately equal

    **Boolean assertions:**

    * `.ok` - Truthy
    * `.true` - Strictly true
    * `.false` - Strictly false
    * `.null` - Strictly null
    * `.undefined` - Strictly undefined
    * `.exist` - Not null or undefined
    * `.empty` - Empty (string, array, object)

    **String assertions:**

    * `.match(regex)` - Matches regular expression
    * `.string(substring)` - Contains substring

    **Function assertions:**

    * `.throw()` / `.throw(ErrorType)` - Throws error
    * `.respondTo(method)` - Has method

    **Object state assertions:**

    * `.extensible` - Object.isExtensible()
    * `.sealed` - Object.isSealed()
    * `.frozen` - Object.isFrozen()

    **Modifiers:**

    * `.not` - Negation
    * `.deep` - Deep comparison
    * `.own` - Own properties only
    * `.ordered` - Order matters
    * `.nested` - Nested property access
    * `.all` - All items/keys
    * `.any` - Any items/keys
    * `.to` / `.be` / `.is` / `.that` / `.and` / `.have` / `.with` - Language chains for readability

    ## `pm` Namespace - Postman Compatibility Layer

    Postman API compatibility for seamless migration with experimental Postman collection import support (v2.0/v2.1). The `pm` namespace provides `pm.expect()` with full Chai.js assertion support for Postman-compatible testing.

    <Info>
      **Experimental Script Import:** When importing Postman collections, Hoppscotch can now import pre-request scripts and test scripts (experimental feature requiring user consent). This enables you to migrate your existing Postman workflows including their scripting logic.
    </Info>

    ### Core APIs

    ```javascript theme={null}
    // Environment and variable management
    pm.environment.get(key: string): string | null
    pm.environment.set(key: string, value: string): void
    pm.environment.unset(key: string): void
    pm.environment.has(key: string): boolean

    pm.globals.get(key: string): string | null
    pm.globals.set(key: string, value: string): void
    pm.globals.unset(key: string): void
    pm.globals.has(key: string): boolean

    pm.variables.get(key: string): string | null
    pm.variables.set(key: string, value: string): void
    pm.variables.has(key: string): boolean
    pm.variables.replaceIn(template: string): string

    // Request access (read-only)
    pm.request.url: URL-like (toString available; additional properties may be limited initially)
    pm.request.method: string
    pm.request.headers: HoppRESTHeader[]
    pm.request.body: HoppRESTReqBody
    pm.request.auth: HoppRESTAuth

    // Response access (post-request only)
    pm.response.code: number
    pm.response.status: string
    pm.response.responseTime: number  // ms
    pm.response.json(): Record<string, any>
    pm.response.text(): string
    pm.response.headers.get(name: string): string | null
    pm.response.headers.has(name: string): boolean
    pm.response.headers.all(): HoppRESTResponseHeader[]
    pm.response.stream: Uint8Array  // Raw response bytes

    // Testing integration
    pm.test(testName: string, testFunction: () => void): void
    pm.expect(actual: any): Expectation

    // Script context information
    pm.info.eventName: string  // "pre-request" or "post-request"
    pm.info.requestName: string
    pm.info.requestId: string

    // Asynchronous requests
    pm.sendRequest(request: string | Object, callback: (err: any, res: any) => void): void
    ```

    ### Postman Chai.js Assertions

    Use `pm.expect()` with full Chai.js BDD assertion support for Postman-compatible scripts:

    ```javascript theme={null}
    // Basic assertions
    pm.test("Status code is 200", () => {
      pm.expect(pm.response.code).to.equal(200)
      pm.expect(pm.response.responseTime).to.be.below(500)
    })

    // Response body validation
    pm.test("Response structure", () => {
      const jsonData = pm.response.json()
      pm.expect(jsonData).to.have.property('success')
      pm.expect(jsonData.success).to.be.true
      pm.expect(jsonData.data).to.be.an('array')
    })

    // Array validation
    pm.test("Array contains expected items", () => {
      const items = pm.response.json().items
      pm.expect(items).to.have.lengthOf.at.least(1)
      pm.expect(items).to.include('apple')
      pm.expect(items).to.have.members(['apple', 'banana', 'cherry'])
    })

    // Header validation
    pm.test("Headers are correct", () => {
      pm.expect(pm.response.headers.get('content-type')).to.include('application/json')
    })
    ```

    ### Postman Response Assertions

    Postman-specific response validation methods:

    ```javascript theme={null}
    pm.test("Response validation", () => {
      pm.expect(pm.response.to.have.status(200))
      pm.expect(pm.response.to.have.header('content-type'))
      pm.expect(pm.response.to.have.body())
      pm.expect(pm.response.to.have.jsonBody())
      pm.expect(pm.response.to.be.ok) // 2xx status
      pm.expect(pm.response.to.be.json)
    })

    pm.test("JSON body validation", () => {
      pm.expect(pm.response.to.have.jsonBody('userId'))
      pm.expect(pm.response.to.have.jsonBody('profile.name'))
      pm.expect(pm.response.to.have.jsonSchema({
        type: 'object',
        required: ['userId', 'email'],
        properties: {
          userId: { type: 'number' },
          email: { type: 'string' }
        }
      }))
    })
    ```

    ### OAuth Token Handling Example

    ```javascript theme={null}
    pm.test("OAuth token handling", () => {
      const response = pm.response.json()
      const expiresIn = response.expires_in // 3600 seconds
      const expiryTime = Date.now() + (expiresIn * 1000)

      // Auto-converts number to string
      pm.environment.set('token_expiry', expiryTime)
      pm.environment.set('access_token', response.access_token)

      // Verify storage
      pm.expect(pm.environment.get('access_token')).to.equal(response.access_token)
    })
    ```

    ### PM-Specific Response Assertions

    The following assertions are specific to the Postman compatibility layer:

    * `pm.response.to.have.status(code)` - Status code check
    * `pm.response.to.have.header(name)` - Header existence
    * `pm.response.to.have.body()` - Has response body
    * `pm.response.to.have.jsonBody()` - JSON body exists
    * `pm.response.to.have.jsonBody(path)` - JSON property exists
    * `pm.response.to.have.jsonSchema(schema)` - Validates JSON schema
    * `pm.response.to.be.ok` - 2xx status code
    * `pm.response.to.be.success` - Alias for ok
    * `pm.response.to.be.json` - JSON content type

    ### Sending Requests

    The `pm.sendRequest` method allows you to send HTTP requests asynchronously from your scripts. This is useful for chaining requests or fetching data from other APIs.

    ```javascript theme={null}
    pm.sendRequest("https://postman-echo.com/get", (err, res) => {
      if (err) {
        console.log(err);
      } else {
        pm.expect(res).to.have.property('code', 200);
        pm.expect(res).to.have.property('status', 'OK');
      }
    });
    ```

    <Note>
      It is recommended to use the Agent interceptor on the Web App and the Native interceptor on the Desktop App for `fetch()`, `hopp.fetch()` and `pm.sendRequest()` usages.
    </Note>

    ### Unsupported Postman Features

    The following Postman features are not currently supported:

    * `pm.visualizer`
    * `pm.collectionVariables`
    * `pm.iterationData`
    * `pm.execution.setNextRequest()`
    * Legacy patterns like global `responseBody` variable, `require()`, etc.

    <Note>
      These limitations are documented in error messages when attempting to use unsupported APIs. The supported version range for Postman collections is v2.0/v2.1.
    </Note>

    ## `pw` Namespace - Legacy Compatibility

    Maintained for backwards compatibility with existing scripts:

    ```javascript theme={null}
    // Legacy environment operations
    pw.env.get(key: string): string | null
    pw.env.getResolve(key: string): string | null
    pw.env.set(key: string, value: string): void
    pw.env.unset(key: string): void
    pw.env.resolve(template: string): string

    // Legacy response access
    pw.response.status: number
    pw.response.body: any
    pw.response.headers: HoppRESTResponseHeader[]

    // Legacy testing framework
    pw.test(testName: string, testFunction: () => void): void
    pw.expect(actual: any): Expectation
    ```

    ## Cookie Object Structure

    Cookies are represented as objects with the following properties:

    ```javascript theme={null}
    type Cookie = {
      name: string           // Cookie name
      value: string          // Cookie value
      domain: string         // Domain the cookie belongs to
      path: string           // Path scope of the cookie (default: "/")
      expires?: string       // Expiration date in ISO format, null for session cookies
      maxAge?: number        // Maximum age in seconds, null if not set
      httpOnly: boolean      // Whether cookie is HTTP-only
      secure: boolean        // Whether cookie should only be sent over HTTPS
      sameSite: 'None' | 'Lax' | 'Strict'  // SameSite attribute
    }
    ```

    ## Usage Examples

    ### Environment Management

    ```javascript theme={null}
    // Set and get environment variables
    hopp.env.set("api_token", "abc123")
    const token = hopp.env.get("api_token")

    // Scope-specific operations
    hopp.env.global.set("base_url", "https://api.example.com")
    hopp.env.active.set("user_id", "12345")

    // Reset to initial values
    hopp.env.reset("api_token")
    ```

    ### Request Manipulation

    ```javascript theme={null}
    // Modify request before sending
    hopp.request.setHeader("Authorization", "Bearer " + hopp.env.get("token"))
    hopp.request.setUrl("https://api.example.com/users/" + hopp.env.get("user_id"))
    hopp.request.setMethod("POST")
    ```

    ### Response Testing

    ```javascript theme={null}
    hopp.test("API responds successfully", () => {
      hopp.expect(hopp.response.statusCode).toBeLevel2xx()
      hopp.expect(hopp.response.responseTime).toBe(1000)

      const data = hopp.response.body.asJSON()
      hopp.expect(data).toBeType("object")
      hopp.expect(data.users).toHaveLength(10)
    })
    ```

    ### Cookie Management

    ```javascript theme={null}
    // Set authentication cookie
    hopp.cookies.set("api.example.com", {
      name: "session_id",
      value: "abc123",
      domain: "api.example.com",
      path: "/api",
      expires: new Date(Date.now() + 86400000).toISOString(), // 24 hours from now
      maxAge: 86400, // 24 hours in seconds
      httpOnly: true,
      secure: true,
      sameSite: "Lax",
    })

    // Check if cookie exists
    if (hopp.cookies.has("api.example.com", "session_id")) {
      const cookie = hopp.cookies.get("api.example.com", "session_id")
      hopp.env.set("session_token", cookie.value)
    }
    ```
  </Tab>

  <Tab title="pw [Legacy]">
    Hoppscotch provides [ECMAScript](https://tc39.es/ecma262) APIs that can be used in writing pre-request scripts and building tests. You can enter your code and run the necessary scripts.

    ## The `pw` object

    The `pw` object provides access to request and response data and variables in your Hoppscotch instance.

    The `pw` object houses the following methods:

    ## `pw.env.set("variable", "value")`

    `pw.env.set()` can be used directly for quick and convenient environment variable definition.

    ```javascript theme={null}
    pw.env.set("baseURL", "https://httpbin.org");
    ```

    Here are some practical examples that show how you can use `pw.env.set()` to encode and decode strings with Base64:

    ### 1.  `pw.env.set("variable", atob("value"))`

    Use the `atob()` function to **decode a Base64 encoded string** and set it as an environment variable.

    ```javascript theme={null}
    pw.env.set("atob", atob("SG9wcHNjb3RjaA=="));
    ```

    ### 2.  `pw.env.set("variable", btoa("value"))`

    Use the `btoa()` function to **encode a regular string into Base64** and set it as an environment variable.

    ```javascript theme={null}
    pw.env.set("btoa", btoa("Hoppscotch"));
    ```

    ## `pw.env.unset("variable")`

    `pw.env.unset()` can be used to remove the value of the variable present in the current active environment

    ```javascript theme={null}
    pw.env.unset("baseURL");
    ```

    ## `pw.env.get("variable")`

    Retrieves the value of the selected environment's variable. Accepts an environment variable as an argument.

    ```javascript theme={null}
    pw.env.get("variable");
    pw.env.get("baseURL");
    ```

    ## `pw.env.getResolve("variable")`

    Retrieves the value of the selected environment's variable recursively. Accepts an environment variable as an argument.

    ```javascript theme={null}
    pw.env.getResolve("variable");
    pw.env.getResolve("baseURL");
    ```

    ## `pw.env.resolve("variable")`

    Retrieves the value of the selected environment's variable recursively. Accepts an environment variable string as an argument.

    ```javascript theme={null}
    pw.env.resolve("<<variable_1>><<variable_2>>");
    pw.env.resolve("<<baseURL>><<basePath>>");
    ```

    ## `pw.expect(value)`

    The expect method returns an expectation object, on which you can call matcher functions.

    The example below calls the matcher function `toBe` on the expectation object that is returned by calling `pw.expect` with the response id, `pw.response.body.id` as an argument.

    Use `pw.expect` directly for quick and convenient testing. Every `pw.expect` statement will generate a line on the test report.

    ```javascript theme={null}
    // This test will pass
    pw.expect(1).toBe(1);

    // This test will fail
    pw.expect(2).not.toBe(2);
    ```

    ## `pw.test(name, function)`

    To create a group of tests, with the name as a string and fn as a callback function to write tests associated with the group. The test results will include the given name for better organization.

    Let's wrap expect statements with `pw.test` to the group and describe related statements.

    ```javascript theme={null}
    // This will return 4 lines on the test report, grouped under "Arithmetic operations"
    pw.test("Arithmetic operations", () => {
      const size = 500 + 500;
      pw.expect(size).toBe(1000);
      pw.expect(size - 500).toBe(500);
      pw.expect(size * 4).toBe(4000);
      pw.expect(size / 4).toBe(250);
    });
    ```

    If neither a `pw.expect` nor a `pw.test` statement is present, no test reports will be generated.

    ```javascript theme={null}
    // This will not generate any test reports
    (99 + 1).toBe(100);
    ```

    ## `pw.toBe(value)`

    Test for exact equality using `toBe`.

    ```javascript theme={null}
    pw.expect(pw.response.body.category).toBe("Sneakers");
    ```

    `toBe` uses strict equality and is recommended for primitive data types.

    ```javascript theme={null}
    // These tests will fail
    pw.expect("hello").toBe("Hello");
    pw.expect(5).toBe("5");
    pw.expect([]).toBe([]);
    ```

    ## `pw.not()`

    Test for negation by adding `.not` before calling the matcher function.

    ```javascript theme={null}
    // These tests will pass
    pw.expect(true).not.toBe(false);
    pw.expect(200).not.toBeLevel3xx();
    ```

    ## `pw.toBeLevelxxx()`

    There are four different matcher functions for quick and convenient testing of the http status code that is returned:

    * `toBeLevel2xx()`
    * `toBeLevel3xx()`
    * `toBeLevel4xx()`
    * `toBeLevel5xx()`

    For example, an argument passed to expect must be within `200` and `299` inclusive to pass `toBeLevel2xx()`.

    ```javascript theme={null}
    // These tests will pass
    pw.expect(204).toBeLevel2xx();
    pw.expect(308).toBeLevel3xx();
    pw.expect(404).toBeLevel4xx();
    pw.expect(503).toBeLevel5xx();
    ```

    If the argument passed to `expect()` is a non-numeric value, it is first parsed with `parseInt()`.

    ```javascript theme={null}
    // This test will pass
    pw.expect("404").toBeLevel4xx();
    ```

    ## `pw.toBeType(type)`

    Use `.toBeType(type)` for type checking. The argument for this method should be either of the following `string`, `boolean`, `number`, `object`, `undefined`, `bigint`, `symbol`, or `function`.

    ```javascript theme={null}
    // These tests will pass
    pw.expect(5).toBeType("number");
    pw.expect("Hello, world!").toBeType("string");

    pw.expect(5).not.toBeType("string");
    pw.expect("Hello, world!").not.toBeType("number");
    ```

    ## `pw.toHaveLength(number)`

    Use `.toHaveLength(number)` to check that an object has a `.length` property and it is set to a certain numeric value.

    ```javascript theme={null}
    // These expectations will pass
    pw.expect("hoppscotch").toHaveLength(10);
    pw.expect("hoppscotch").not.toHaveLength(9);

    pw.expect(["apple", "banana", "coconut"]).toHaveLength(3);
    pw.expect(["apple", "banana", "coconut"]).not.toHaveLength(4);
    ```

    ## `pw.toInclude(value)`

    Use `.toInclude(value)` to check that a string/array has a value entry.

    ```javascript theme={null}
    // These expectations will pass
    pw.expect("hoppscotch").toInclude("hopp");
    pw.expect("hoppscotch").not.toInclude("scotch");

    pw.expect(["apple", "banana", "coconut"]).toInclude("banana");
    pw.expect(["apple", "banana", "coconut"]).not.toInclude("grape");
    ```

    ## `pw.response`

    Assert response data by accessing the `pw.response` object.

    ```javascript theme={null}
    // This test will pass
    pw.test("Response is ok", () => {
      pw.expect(pw.response.status).toBe(200);
    });
    ```

    Currently supports the following response values:

    * `status`: -number- The status code as an integer.
    * `headers`: -object- The response headers.
    * `body`: -object- the data in the response. In many requests, this is the JSON sent by the server.

    ### Setting Environment Variables from API Responses

    By following these steps, you can store data from one API response and access it later using Environment Variables, making it available for use in subsequent API calls.

    Assume in this example that the payload returns `access_token` and `id_token` as part of a JSON response.

    1. Create Environment Variables without setting their values initially. For example:

    * `idToken`
    * `accessToken`

    2. In the "Tests" tab of the first API request (that returns the tokens), add the following code:

    ```javascript theme={null}
    const jsonData = pw.response.body; // Save the JSON payload response

    pw.env.set("accessToken", jsonData.access_token); // Set "accessToken" to the value of "access_token" in the response

    pw.env.set("idToken", jsonData.id_token); // Set "idToken" to the value of "id_token" in the response
    ```

    3. Use these Environment Variables in subsequent API calls within the same collection using the `<<variableName>>` syntax as usual.
  </Tab>
</Tabs>

<CardGroup>
  <Card title="Scripts" icon="circle-arrow-right" href="/documentation/getting-started/rest/pre-request-scripts">
    Read about pre-request scripts.
  </Card>

  <Card title="Tests" icon="circle-arrow-right" href="/documentation/getting-started/rest/tests">
    Read about post-request tests.
  </Card>

  <Card title="Environments" icon="circle-arrow-right" href="/documentation/features/environments">
    Read about environments.
  </Card>
</CardGroup>


# Shortcuts
Source: https://docs.hoppscotch.io/documentation/features/shortcuts

Keyboard shortcuts for Hoppscotch.

You can improve your workflow by efficiently performing actions straight from your keyboard.

<Tip>Bring up the shortcuts sidebar on Hoppscotch using `Ctrl/Cmd` + `/`.</Tip>

## General shortcuts

| Shortcut         | Action                |
| ---------------- | --------------------- |
| `?`              | Help menu             |
| `K`              | Search & command menu |
| `Ctrl/Cmd` + `/` | Keyboard Shortcuts    |
| `esc`            | Close current menu    |

## Request shortcuts

| Shortcut             | Action                                |
| -------------------- | ------------------------------------- |
| `Ctrl/Cmd` + `enter` | Send request                          |
| `Ctrl/Cmd` + `S`     | Save to collections                   |
| `Ctrl/Cmd` + `U`     | Generate and copy request link        |
| `Ctrl/Cmd` + `I`     | Reset Request to `echo.hoppscotch.io` |
| `Alt/Option` + `↑`   | Select Next method                    |
| `Alt/Option` + `↓`   | Select Previous method                |
| `Alt/Option` + `G`   | Select GET method                     |
| `Alt/Option` + `H`   | Select HEAD method                    |
| `Alt/Option` + `P`   | Select POST method                    |
| `Alt/Option` + `U`   | Select PUT method                     |
| `Alt/Option` + `X`   | Select DELETE method                  |

## Response shortcuts

| Shortcut         | Action                      |
| ---------------- | --------------------------- |
| `Ctrl/Cmd` + `J` | Download response as a file |
| `Ctrl/Cmd` + `.` | Copy response to clipboard  |

## Navigation shortcuts

| Shortcut           | Action                   |
| ------------------ | ------------------------ |
| `Ctrl/Cmd` + `←`   | Go back to previous page |
| `Ctrl/Cmd` + `→`   | Go forward to next page  |
| `Alt/Option` + `R` | Go to REST page          |
| `Alt/Option` + `Q` | Go to GraphQL page       |
| `Alt/Option` + `W` | Go to Realtime page      |
| `Alt/Option` + `S` | Go to Settings page      |
| `Alt/Option` + `M` | Go to Profile page       |

## Miscellaneous shortcuts

| Shortcut         | Action                      |
| ---------------- | --------------------------- |
| `Ctrl/Cmd` + `M` | Invite people to Hoppscotch |


# Code Snippets
Source: https://docs.hoppscotch.io/documentation/features/snippets

Generate code snippets for your API in a variety of languages and frameworks.

Code snippets allows you to rapidly build your API integration in a variety of languages and frameworks.

## Generate code snippets

To generate a code snippet for your API, locate the **Code Generate** `<>` icon in the right sidebar, alongside collections, environments, and history. Then, select the language in which you prefer to receive your API request.

## Copy code snippets

Choose the language and framework you want to generate the code snippet for and click the "**Copy**" button to copy the code snippet to your clipboard.

## Supported languages

* Shell
* Javascript
* Node
* C
* Java
* PHP
* Objective-C
* Swift
* Python
* Ruby
* C#
* Go
* OCaml

## Preview request setup

1. Open the "**Generate Code**" tab from the sidebar.
2. Click on the drop-down to select the language.
3. Select "**HTTP - HTTP 1.1 Request String**" from the language list.

This displays the current request setup in HTTP 1.1 Request String syntax.


# Spotlight
Source: https://docs.hoppscotch.io/documentation/features/spotlight

Powerful search and command palette.

<Tip>Press   ⌘ + K   anytime to open Spotlight.</Tip>

Spotlight is an innovative feature introduced in Hoppscotch, designed to enhance your interaction with the application. By utilizing Spotlight, you can efficiently navigate through various functionalities and perform tasks swiftly.

## Activation

To activate the Spotlight search functionality, you can employ the following key combinations based on their operating systems:

* On macOS: Press `Cmd` + `K`
* On Windows or Linux: Press `Ctrl` + `K`

## Spotlight Interface

Upon triggering the Spotlight search, a search field will be displayed, allowing you to provide input. As you type, relevant suggestions will dynamically appear, aiding in quickly finding desired functionalities.

## Navigation and Selection

Spotlight not only offers dynamic suggestions but also facilitates their navigation and selection. The presented suggestions are ranked by relevance, enabling you to easily identify your desired options. Navigation can be achieved through:

* Arrow keys: Use the arrow keys to move through the suggestions.
* Enter key: Press the enter key to select the highlighted suggestion.

Alternatively, you can achieve the same functionality using the mouse or trackpad.

Spotlight revolutionizes the user experience within Hoppscotch by streamlining various tasks and reducing unnecessary clicks. With Spotlight, you can accomplish the following tasks more efficiently:

* Navigate to any page within the app.
* Search and find requests in your collections.
* Create, edit, and quickly switch, workspaces and environments.
* Rename, save, and send requests.


# Variables
Source: https://docs.hoppscotch.io/documentation/features/variables

Dynamic placeholders for your API interactions.

Hoppscotch provides you the ability to create and use variable throughout the app. This helps you reuse values throughout Hoppscotch just by invoking the variable name.

Hoppscotch considers an objects within an angular brackets as a variable `<<variable>>`

## Variable Scopes

Hoppscotch provides you different variables scopes, allowing you to use different scopes for different contexts.

1. **Global Variables:** can be accessed throughout Hoppscotch and has the broadest scope of all variables.
2. **Environment Variables:** allow your variables to be scoped to an environment. Environment variables are useful when you have the same set of variables for two environments such as production and staging.
3. **Request Variables:** are scoped to just an individual request, request variables are useful when you want to use variables in your URL path or when you want to embed a variable URL.
4. **Predefined Variables:** are automatically generated at runtime and can be accessed globally throughout Hoppscotch using the `$` symbol, such as `$guid` or `$timestamp`.
5. **Collection Variables:** are scoped to individual collection and child folders, perfect for sharing base URLs, tokens and defaults across a set of requests without leaking to other workspaces.

The scope of each variable can be identified from the color of the variable name. If a variable with same name exist it is resolved in the order of priority.

| Variable Scope | Color | Priority |
| -------------- | ----- | -------- |
| Request        | 🟠    | 1        |
| Collection     | 🟣    | 2        |
| Predefined     | 🟡    | 3        |
| Environment    | 🟢    | 4        |
| Global         | 🔵    | 5        |
| Non resolvable | 🔴    | -        |

## Types of Variables

1. **A regular variable**: allows users to reference the variable throughout Hoppscotch, and anyone can see the value associated with the variable.
   In a workspace, regular environment variable-value pairs will be synced to the server, making them available to all workspace members.
   However, you have the option to choose whether to sync a regular variable value present in your personal workspace
2. **A secret variable:** enables users to specify secrets and reference the values as variables. The values of secret variables in any workspace will never be synced to the server or shared with any workspace members.
   It is expected that in a collaborative workspace the user will populate the value of the variable at runtime.
   All secret variable values in Hoppscotch will be masked using asterisks (\*\*\*). Secret Variables cannot be scoped to a request and can only be scoped in an environment or globally

<Note>
  Secret variables values will not be exported when an environment is exported.
</Note>

3. **A predefined variable:** is automatically generated at runtime and provides dynamic, context-specific data. Predefined variables are available throughout your requests and responses and are useful for incorporating system-level information or dynamic values into your API interactions without manual configuration.
   All predefined variables are accessible throughout Hoppscotch and can be retrieved using the `$` symbol. Below is the list of predefined variables whose values are dynamically generated during the request or collection run:

> | **Variable Name** | **Description**                                                                               | **Example**                            |
> | ----------------- | --------------------------------------------------------------------------------------------- | -------------------------------------- |
> | `$guid`           | A v4 style unique (GUID) identifier for each request.                                         | `123e4567-e89b-12d3-a456-426614174000` |
> | `$timestamp`      | The current UNIX timestamp in seconds                                                         | `1693047645`                           |
> | `$isoTimestamp`   | The current date and time in ISO-8601 format at zero UTC (also known as "Zulu time" or UTC-0) | `2024-09-25T00:00:00.000Z`             |
> | `$randomUUID`     | A random 36-character UUID.                                                                   | `6929bb52-3ab2-448a-9796-d6480ecad36b` |
>
> ### <ins>Numbers, Text, and Colors</ins>
>
> | **Variable Name**     | **Description**                                                          | **Example**             |
> | --------------------- | ------------------------------------------------------------------------ | ----------------------- |
> | `$randomAlphaNumeric` | A random alpha-numeric character.                                        | `A9X1Z3`                |
> | `$randomBoolean`      | A random boolean value.                                                  | `true` , `false`        |
> | `$randomInt`          | A random integer value between 0 and 1000.                               | `29` , `432` , `786`    |
> | `$randomColor`        | A random color amongst **red, green, blue, yellow, purple, and orange.** | `yellow`                |
> | `$randomHexColor`     | A random hex value.                                                      | `#f2a729`               |
> | `$randomAbbreviation` | A random abbreviation.                                                   | `SQL` , `JSON` , `HTML` |
>
> ### <ins>Internet and IP addresses</ins>
>
> | **Variable Name**   | **Description**                                | **Example**                               |
> | ------------------- | ---------------------------------------------- | ----------------------------------------- |
> | `$randomIP`         | A random IPv4 address                          | `192.168.0.101`                           |
> | `$randomIPV6`       | A random IPv6 address                          | `2001:0db8:85a3:0000:0000:8a2e:0370:7334` |
> | `$randomMACAddress` | A random MAC address.                          | `00:1B:44:11:3A:B7`                       |
> | `$randomPassword`   | A random 15-character alpha-numeric password.  | `H8w72Sx93KlqA1b`                         |
> | `$randomLocale`     | A random two-letter language code (ISO 639-1). | `en`, `fr`, `es`                          |
> | `$randomUserAgent`  | A random user agent.                           | `Mozilla/5.0 (Windows NT 10.0; Win64)`    |
> | `$randomProtocol`   | A random internet protocol.                    | `https`, `ftp`                            |
> | `$randomSemver`     | A random semantic version number.              | `1.2.3`                                   |
>
> ### <ins>Names</ins>
>
> | **Variable Name**   | **Description**       | **Example**                                         |
> | ------------------- | --------------------- | --------------------------------------------------- |
> | `$randomFirstName`  | A random first name.  | `Ethan` , `Chandler`, `John`                        |
> | `$randomLastName`   | A random last name.   | `Schaden` , `Schneider` , `Doe`                     |
> | `$randomFullName`   | A random Full name.   | `Ethan Schaden` , `Chandler Schneider` , `John Doe` |
> | `$randomNamePrefix` | A random name prefix. | `Dr.` , `Miss.` , `Prof.`                           |
> | `$randomNameSuffix` | A random name suffix. | `MD` , `PhD` , `Jr.`                                |
>
> ### <ins>Addresses and Profession</ins>
>
> | **Variable Name**      | **Description**          | **Example**                                        |
> | ---------------------- | ------------------------ | -------------------------------------------------- |
> | `$randomCity`          | A random city name.      | `New York` , `Houston` , `Philadelphia`            |
> | `$randomJobArea`       | A random job area.       | `Intranet` , `Development` , `Testing`             |
> | `$randomJobDescriptor` | A random job descriptor. | `Corporate` , `Lead` , `Principal`                 |
> | `$randomJobTitle`      | A random job title.      | `Global Branding Officer` , `Productivity Analyst` |
> | `$randomJobType`       | A random job type.       | `Manager` , `Coordinator` , `Director`             |

<CardGroup>
  <Card title="Environments" icon="circle-arrow-right" href="/documentation/features/environments">
    Choose the environment that aligns best with your development workflow.
  </Card>
</CardGroup>


# Widgets
Source: https://docs.hoppscotch.io/documentation/features/widgets

Embed Hoppscotch in your website.

Widgets are small, interactive components that can be embedded in HTML pages to provide a seamless experience for your audience. Hoppscotch offers three types of widgets: links, buttons, and embeds.

## Links

Links are the most basic type of widget. They are simply a URL that can be shared with others. You can generate links to your requests in three different formats: raw, HTML, and Markdown.

## Buttons

Buttons are a more advanced type of widget. They are a link that can be embedded in HTML or Markdown files. You can customize the button's appearance and behavior to suit your needs. You can also generate buttons in two different formats: HTML and Markdown.

## Embeds

Embeds are the most advanced type of widget. They are a mini version of Hoppscotch that can be embedded in an HTML page, enabling your audience to interact seamlessly with your API request. You can customize the embed's appearance and behavior to suit your needs.

## Shared requests

Sharing a request does not provide others with access to your request. Instead, it generates a link that can be shared with others. It's important to note that if a shared request contains any environment variables, proper functionality may be compromised unless the recipient has access to the same environment variables. Therefore, it is advisable to share requests that do not contain environment variables or replace any environment variables with their corresponding values before sharing.

### Create a shared request:

#### Sharing a request in a collection:

1. Right-click on a saved request within a collection and select "**Share Request**".
2. Choose between link, button, and embed widgets.
3. Click on the "**Create**" button.
4. Copy the share link.

#### Sharing a request in workspace:

1. Click on the "**Share request**" button in drop-down menu next to the "**Save**" button.
2. Choose between link, button, and embed widgets.
3. Click on the "**Create**" button.
4. Copy the share link.

### View your shared requests:

1. Click on the "**Shared Requests**" button in the sidebar.
2. You will see a list of all your shared requests.
3. Click on the request to open it in a new tab.
4. You can also customize the widget, copy the link, or delete the shared request by right-clicking on it or 3-dot menu.


# Workspaces
Source: https://docs.hoppscotch.io/documentation/features/workspaces

Organize your requests, collections, and environments into different workspaces. You can also invite other users to your workspace to collaborate.

Once you are logged into Hoppscotch, you can toggle between multiple workspaces to organize your workflow.

You can choose between your workspace titled "**Personal Workspace**" or create a workspace for your teams so that you can collaborate.

<Note>Currently, organizing requests across multiple shared workspaces is limited to RESTful protocol. GraphQL and Realtime APIs are available only in the personal workspace and are not supported for collaboration in shared workspaces.</Note>

## Create a workspace

To create a workspace, click on the **"+"** icon on the top right corner of the workspace switcher. Alternatively, you can also click on the "**Create new workspace**" button on the "[Profile](https://hoppscotch.io/profile)" page under the "**Workspaces**" section.

Creating a workspace makes you the owner of the workspace. You can invite other users to the workspace and assign them roles.

## Invite users to a workspace

To invite users to a workspace, click on the "**Invite**" button and enter the email address of the user you want to invite. You can invite multiple users at once by adding the email addresses in the input field entries.

## Switch between workspaces

To switch between workspaces, click on the workspace switcher in the top right corner of the app and select the workspace you want to switch to.

## Edit a workspace

<Warning>You can only edit a workspace if you are the owner of the workspace.</Warning>

### Rename a workspace

To rename a workspace, click on the workspace settings button on the top right corner of the app. Then click on the workspace name and enter the new name.

### Remove a user from a workspace

To remove a user from a workspace, click on the workspace settings button on the top right corner of the app. Then click on the "**Delete**" button on the user you want to remove from the workspace.

### Leave a workspace

To leave a workspace, click on the workspace settings button on the top right corner of the app. Then click on the "**Delete**" button on the workspace you want to leave.

You can only leave a workspace if you are not the owner of the workspace. If you are the owner of the workspace, you will have to delete the workspace to leave it. Alternatively, you can also transfer the ownership of the workspace to another user and then leave the workspace.

### Change member role

There are three types of roles for members in a workspace:

* **Owner**: The owner of the workspace has full access to the workspace and can invite other users to the workspace. The owner can also delete the workspace.
* **Editor**: The editor of the workspace has edit access to the workspace and can create, edit, and delete collections, environments, and requests in the workspace.
* **Viewer**: The viewer of the workspace has read-only access to the workspace and can only view the collections, environments, and requests in the workspace.

To change the role of a member in a workspace, click on the workspace settings button on the top right corner of the app. Then click on the "**Role**" drop-down on the user you want to change the role of. Then select the role you want to assign to the user then click "**Save**".

### Delete a workspace

To delete a workspace, click on the "**Delete**" button on the workspace you want to delete on the "[Profile](https://hoppscotch.io/profile)" page under the "**Workspaces**" section.


# Hoppscotch Clients
Source: https://docs.hoppscotch.io/documentation/getting-started/clients

Access Hoppscotch from anywhere.

Hoppscotch has multiple clients that you can use to develop and test your APIs. You can use Hoppscotch on the web, desktop, and terminal.

<CardGroup>
  <Card title="Web" icon="globe" href="/documentation/clients/web" />

  <Card title="Desktop" icon="desktop" href="/documentation/clients/desktop" />

  <Card title="CLI" icon="square-terminal" href="/documentation/clients/cli/overview" />
</CardGroup>

## Navigating Hoppscotch Interface

<Frame>
  <img />

  <img />
</Frame>

## Understanding the user interface

Hoppscotch has a simple and intuitive UI. The UI is divided into multiple sections:

### Topbar

The top bar is where you can find the search, login, workspace selector, and more.

### Menu

The menu is where you will find the different platforms that Hoppscotch offers and switch between them. You can also access the settings page from the menu.

### Sidebar

The sidebar is where you can see additional features depending on the platform you are working on. The sidebar houses features like history and collections.

### Main

The main panel is where you will spend most of your time. This is where you will create and send requests and view the responses.

### Footer

The footer houses the status bar. The status bar allows you to toggle the sidebar, go full screen, get help and support, and more.


# Running a simple query
Source: https://docs.hoppscotch.io/documentation/getting-started/graphql/creating-a-query

Learn how to run a simple query using Hoppscotch.

## Connecting to a GraphQL server

Switch to the GraphQL platform on Hoppscotch and connect to the below GraphQL server.

```
https://echo.hoppscotch.io/graphql
```

Once a successful connection has been made, you can view both **documentation** and the **schema** using Hoppscotch.

It is important to explore the schema to understand the different **queries, mutations, types, and subscriptions** that are offered by the endpoint.

## Running the query

You can execute queries to retrieve data from the GraphQL server by following these steps:

* Open the **Documentation** panel to explore the available queries for the endpoint.
* Click on `query` under **Root Types** to view the listed query fields.
* Click the **"+"** button next to a query field to add it to the Query editor with a structured template.
* Expand the query by clicking on it, then use the **"+"** button to add specific fields, arguments, or filters.
* Customize the query as needed by modifying fields, adding arguments, or setting variables directly in the Query editor.

## Fetching Countries Data

Let's explore a sample query using the Countries GraphQL API.

1. Open Hoppscotch, switch to the [GraphQL client](https://hoppscotch.io/graphql) and connect to the endpoint below:

   ```
   https://countries.trevorblades.com/graphql
   ```

2. Explore the schema and documentation to understand more about the endpoint.

3. Select the `countries` query, cherry-pick the fields, and add a filter to return results where the `name` field is equal to **"Germany"**.

   ```graphql theme={null}
   {
     countries (filter: {name: {eq: "Germany"}}) {
       name
       code
       capital
       emoji
       currencies
     }
   }
   ```

4. Click on the run button to execute the query.

5. The query will return the following response.

   ```json theme={null}
   {
     "data": {
       "countries": [
         {
           "name": "Germany",
           "code": "DE",
           "capital": "Berlin",
           "emoji": "🇩🇪",
           "currencies": [
             "EUR"
           ]
         }
       ]
     }
   }
   ```


# Using variables in a GraphQL query
Source: https://docs.hoppscotch.io/documentation/getting-started/graphql/using-variables

Learn how to use variables in a GraphQL query.

Hoppscotch allows you to pass variables in the query to fetch data dynamically.

To demonstrate the use of variables, let's write a query to get countries by their `name` and `continent`. For example, we will fetch the details of **"Bahrain"** from the **"Asia"** continent.

## Variables

Go to the variables section and define the variable.

```json theme={null}
{
  "countryName": "Bahrain",
  "continentCode": "AS"
}
```

## Using the variable in the query

Now create a query `getCountries` with variables as shown below:

```graphql theme={null}
  query getCountries($countryName: String!, $continentCode: String!) {
    countries(filter: {name: {eq: $countryName}, continent: {eq: $continentCode}}) {
      name
      continent {
        name
      }
      code
      emoji
      currencies
    }
  }
```

Hoppscotch will retrieve the value of the variable and execute the query to get the below response.

```json theme={null}
  {
    "data": {
      "countries": [
        {
          "name": "Bahrain",
          "continent": {
            "name": "Asia"
          },
          "code": "BH",
          "emoji": "🇧🇭",
          "currencies": [
            "BHD"
          ]
        }
      ]
    }
  }
```


# Introduction to Hoppscotch
Source: https://docs.hoppscotch.io/documentation/getting-started/introduction

Open-source API development ecosystem.

Hoppscotch is a lightweight, web-based API development suite. It was built from the ground up with ease of use and accessibility in mind providing all the functionality needed for developers with minimalist, unobtrusive UI.

<Frame>
  <img />

  <img />
</Frame>

<Steps>
  <Step icon="heart" title="Open-source code">
    Source code is open and auditable. Built with privacy and security in mind.
  </Step>

  <Step icon="certificate" title="Cross-platform apps">
    Works on Web, Mac, Windows, Linux, and CLI. No installation is required.
  </Step>

  <Step icon="server" title="Self-Host support">
    Host Hoppscotch on your own server and use it with your team.
  </Step>

  <Step icon="rocket" title="Fast and reliable">
    Built with performance in mind and designed to be seamless and instant.
  </Step>

  <Step icon="face-smile" title="Community driven">
    Built on top of open source technologies by the community, for the community.
  </Step>

  <Step icon="layer-group" title="Built for developers">
    Have all your teams in one place and collaborate on your APIs with ease.
  </Step>

  <Step icon="keyboard" title="Keyboard first design">
    Designed to be intuitive and easy to use with keyboard shortcuts.
  </Step>

  <Step icon="lock" title="Safe and secure">
    Built with security in mind and designed to be safe and secure.
  </Step>
</Steps>


# Quick start
Source: https://docs.hoppscotch.io/documentation/getting-started/quick-start

Get started with Hoppscotch.

## Platforms

### Hoppscotch Cloud

Hoppscotch Cloud is our hosted API development and testing platform that allows you to share your APIs with your team with ease. No need to worry about hosting, scaling, and maintenance. Hoppscotch Cloud is built for individuals and teams.

[Get started for free on Hoppscotch Cloud](https://hoppscotch.io)

### Hoppscotch Self-Host

For full data ownership and control over your API development and testing, you can self-host Hoppscotch on your infrastructure.

<CardGroup>
  <Card title="Community Edition" icon="circle-arrow-right" href="/documentation/self-host/community-edition/getting-started">
    Hoppscotch Community Edition is free and open-source. It is licensed under the MIT License. You can use it for personal and commercial projects. It is a great choice for individuals and small teams.
  </Card>

  <Card title="Enterprise Edition" icon="circle-arrow-right" href="/documentation/self-host/enterprise-edition/getting-started">
    SAML-based SSO, on-prem deployment, audit logs, and more. Hoppscotch Enterprise Edition is a self-hosted version of Hoppscotch Cloud with enterprise-ready features for teams and organizations.
  </Card>
</CardGroup>

<Tip>Hoppscotch Enterprise Edition is available for on-premise deployment with priority support. [Contact Hoppscotch Support](/support/getting-started/contact)</Tip>

***

## Solutions

### Hoppscotch Web App

The easiest way to get started with Hoppscotch is with our hosted cloud plan. Get unlimited collections with no limits and all of our features are built for individuals and teams.

[Open Hoppscotch Web App](https://hoppscotch.io)

### Hoppscotch Desktop App

Hoppscotch Desktop App is a cross-platform desktop application built with Tauri and Hoppscotch Web Client. It is a standalone version of Hoppscotch that can be installed on your computer and used without a browser. Hoppscotch Desktop App is available for Mac, Windows and Linux.

[Download Hoppscotch Desktop App](https://hoppscotch.com/download)

### Hoppscotch CLI

Hoppscotch CLI is a command-line tool that allows you to run Hoppscotch on your terminal and CI/CD pipelines.

[Install Hoppscotch CLI](/documentation/clients/cli/overview)


# MQTT
Source: https://docs.hoppscotch.io/documentation/getting-started/realtime/mqtt

MQTT is a lightweight publish-subscribe messaging protocol.

## Connect to a MQTT server

1. Enter the MQTT server "**URL**" and click on "**Connect**".

   ```
   wss://test.mosquitto.org:8081
   ```

2. Check the log to see if the connection was successful or not.

3. To test your server add messages under a topic and publish it.

4. Other devices in the server that have subscribed to the topic will get your messages.

5. You can receive messages by subscribing to a topic that another device in the server transmits.

6. Monitor the log for results.

## Sending messages

Write your message in the "**Message**" input field under the "**Communication**" tab and click on the "**Publish**" button. Type in the "**Topic**" input field to send a message with a topic. The message you send will be displayed on the "**Logs**" pane.

## Subscriptions

Click on the "**New Subscription**" button to add a new subscription. Enter the topic name and click on the "**Subscribe**" button to subscribe to the topic. The messages you receive will be displayed on the "**Logs**" pane.

## Troubleshooting

1. Make sure you enter a valid MQTT URL, they always start with the protocol format `ws://`.
2. Do not add invalid/incorrect authorization tokens before you connect to a MQTT server.


# Socket.IO
Source: https://docs.hoppscotch.io/documentation/getting-started/realtime/socket-io

Learn how to use the Socket.IO testing tool in Hoppscotch.

The Hoppscotch Socket.io testing tool lets you test out your socket.io services.

## Connect to a socket.io server

1. Add the "**URL**", "**path**" and click on "**Connect**".
2. Listen to events broadcasted by the server, shown in the log.
3. Use the sidebar to add an event name and send messages to the server.

## Sending messages

Write your message in the "**Message**" input field under the "**Communication**" tab and click on the "**Send**" button. Type in the "**Event**" input field to send a message with an event name. The message you send will be displayed on the "**Logs**" pane.

## Troubleshooting

1. Make sure you enter a valid socket.io URL, they always start with the protocol format `ws://`.
2. Do not add an invalid/incorrect authorization token before you connect to a socket.io server.


# Server-Sent Events
Source: https://docs.hoppscotch.io/documentation/getting-started/realtime/sse

Server-Sent Events (SSE) is a server push technology enabling a client to receive automatic updates from a server via HTTP connection.

The Hoppscotch SSE testing tool lets you test out your SSE services.

## Connect to a SSE server

1. Add the SSE "**URL**" and "**path**" and click on "**Connect**".
2. Choose the event type that you want to subscribe to and connect.
3. Message from the SSE server will continuously updated in the log until either the server or client (you) terminate the connection.

## Listening to events

The events sent by the server will be displayed in the log pane.

## Troubleshooting

1. Make sure you enter valid SSE URLs, they always start with the protocol format `http://` or `https://`.
2. Make sure the server is sending the correct event type.


# Websocket
Source: https://docs.hoppscotch.io/documentation/getting-started/realtime/websocket

Connect to a WebSocket and send messages.

Enter your WebSocket "**URL**", valid protocols, and click on "**Connect**".

You can also disconnect from the WebSocket by clicking on the "**Disconnect**" button.

## Sending messages

Write your message in the "**Message**" input field under the "**Communication**" tab and click on the "**Send**" button. The message you send will be displayed on the "**Logs**" pane.

## Troubleshooting

1. Make sure you enter a valid WebSocket URL, they always start with the protocol format `ws://`.
2. Do not add invalid/blank protocol before you connect to a WebSocket.


# Using auth tokens
Source: https://docs.hoppscotch.io/documentation/getting-started/rest/auth-tokens

Learn how to use authentication tokens in Hoppscotch.

In this section, we'll look at passing Authorization and Authentication information in our requests, by accessing the [GitHub REST API](https://docs.github.com/en/rest).

Let's try making a `GET` request to the URL `https://api.github.com/user`.

You'll get the following response:

```json theme={null}
{
  "message": "Requires authentication",
  "documentation_url": "https://docs.github.com/rest/reference/users#get-the-authenticated-user"
}
```

This is because you are not authorized to access the API and to gain access you would need to authenticate yourself. We use tokens to authenticate a user and to do so we first need to generate an access token from GitHub.

## Generating access token

To get access to the GitHub API, you first need to generate a personal access token. For our demonstration, we will generate one granting access to public repositories.

1. Login to the GitHub account.
2. Goto your [personal access tokens page](https://github.com/settings/tokens) and click on "**Generate new token**".
3. Select tokens (classic).
4. Specify the note as "**Hoppscotch API**" so that you can remember why you created it.
5. Under the "Select scopes" section only check `public_repo`.
6. Scroll down and click on "**Generate token**".
7. You just generated your access token, now copy the token to your clipboard.

## Storing auth token in a variable

<Tip>It is a recommended safe practice to have your auth details in environment variables rather than inputting them directly to the authorization tab.</Tip>

1. Click on the "**Global**" environment to add a variable.
2. Create a variable called `token` and paste the token from GitHub as its value.
3. Now open the Authorization tab and select `Bearer` from the dropdown list.
4. Input the token as shown below, make sure that you reference the token in variable format, i.e. `<<token>>`.
5. Click on "**Send**".

You should now see the response including details about your GitHub account.


# Creating a request
Source: https://docs.hoppscotch.io/documentation/getting-started/rest/creating-a-request

Learn how to create a request in Hoppscotch.

The RESTful protocol is the default protocol that is active when you open Hoppscotch. Hoppscotch allows you to make API requests and examine the responses.

You can enter the API endpoint and choose the HTTP method according to your needs from the dropdown menu.
Once it is configured, click on the "**Send**" button and you will see the response returned by the server. It's that simple.

Now try it yourself, copy the below API endpoint, and create a request.

```
https://echo.hoppscotch.io
```

Let's try another API.

We'll be using the [Pokemon API](https://github.com/PokeAPI/pokeapi). Go ahead and create a `GET` request to the endpoint below:

```
https://pokeapi.co/api/v2
```

If your request was successful, then you should get a JSON response as shown below:

```json theme={null}
{
  "ability": "https://pokeapi.co/api/v2/ability/",
  "berry": "https://pokeapi.co/api/v2/berry/",
  "pokedex": "https://pokeapi.co/api/v2/pokedex/",
  "pokemon": "https://pokeapi.co/api/v2/pokemon/",
  "version-group": "https://pokeapi.co/api/v2/version-group/"
}
```

The Pokemon API has returned several new API endpoints or URLs, let's pick the character's URL and explore it.

To explore the characters create a `GET` request to the URL `https://pokeapi.co/api/v2/pokemon` by copy-pasting the URL below:

```
https://pokeapi.co/api/v2/pokemon
```

The API should have returned a huge amount of data, something similar to the one below:

```json theme={null}
{
  "count": 1279,
  "next": "https://pokeapi.co/api/v2/pokemon?offset=20&limit=20",
  "previous": null,
  "results": [
    {
      "name": "bulbasaur",
      "url": "https://pokeapi.co/api/v2/pokemon/1/"
    },
    {
      "name": "ivysaur",
      "url": "https://pokeapi.co/api/v2/pokemon/2/"
    },
  ]
}
```

Try experimenting with the `/pokedex`, `/berry`, and the other endpoints as well.

<Card title="RESTful protocol" icon="circle-arrow-right" href="/documentation/protocols/rest">
  Learn more about RESTful protocol.
</Card>


# Environment variables
Source: https://docs.hoppscotch.io/documentation/getting-started/rest/environment-variables

Learn how to use environment variables in your requests and scripts.

Environment variables allow you to store and reuse values in your requests and scripts.

By storing a value in a variable:

* You can reference it throughout your request section.
* You can change its value by updating it in a single place.
* You increase your ability to work efficiently and minimize the likelihood of errors.

## Adding environment variables

You can create a new environment by clicking the environments icon on the sidebar and clicking the `new` button. Let's label the environment as `Pokemon Envs`.

Now, let's create an environment variable called `baseURL` pointing to `https://pokeapi.co/api/v2`.

Similarly, you can create multiple environments and environment variables.

## Accessing environment variable

If you have more than one environment, select the environment whose variables you want to access. You can access the variables in the request section by referencing the variable in the following format `<<variable_name>>`, in our case the variable will be `<<baseURL>>` and the complete URL will be `<<baseURL>>/pokemon/ditto`.

<Tip>You can add your variables to the `Global` environment, which can be accessed globally, ie. in every other environments.</Tip>


# Organizing requests
Source: https://docs.hoppscotch.io/documentation/getting-started/rest/organizing-requests

Organize your requests categorically for future reference or collaboration with your team using collections.

It is always a best practice to organize your requests when you test multiple API endpoints. You can organize your requests categorically for future reference or collaboration with your team using collections.

You can create a new collection on Hoppscotch by clicking the collections icon on the sidebar and clicking the "**+ New**" button.

Let's try making a collection for our [Pokemon API](https://github.com/PokeAPI/pokeapi) called `Pokemon API`.

## Adding requests to a collection

Now, let's save our current query as `GET three Pokemon` and save it in our `Pokemon API` Collection.

1. Click on the "**Save**" button.
2. Give your request a name.
3. Add it to your collection.

<Tip>You can add multiple requests to a collection and even create subfolders inside a collection to further organize your requests.</Tip>


# Pre-request scripts
Source: https://docs.hoppscotch.io/documentation/getting-started/rest/pre-request-scripts

Learn how to use pre-request scripts in Hoppscotch.

## Scripts

Hoppscotch lets you add dynamic behavior to REST API requests. This allows you to write test suites and build requests that can contain dynamic parameters. You can add [ECMAScript](https://tc39.es/ecma262) code that executes based on events in the flow:

* Pre-request scripts are executed before a request is sent to the server.
* You can add multiple pre-request scripts to a request.
* You can add pre-request scripts to both requests saved and not saved in a collection.

<Tip>Hoppscotch will then execute the scripts along with the requests in the specified order.</Tip>

## Pre-request script

Pre-request script is a piece of code that will run before the execution of the request.

You can use the pre-request script for a pre-processing task such as:

* Setting parameters, headers.
* Adding body data.
* Adding variable values.
* Including timestamps in request headers.

## Writing pre-request scripts

Hoppscotch provides a special `pw` object containing various methods to create scripts and tests. The `pw` object is global and can be referenced by name to access methods.

For example, to set an environment variable, you can use the `pw.env.set()` method.

```javascript theme={null}
pw.env.set("variable", "value");
```

## Examples

Let us look at some examples of how you can use Hoppscotch to write pre-request scripts.

### Setting environment variables

`pw.env.set()` can be used directly for quick and convenient environment variable definition. It can be used to better organize request codes.

```javascript theme={null}
pw.env.set("baseURL", "https://httpbin.org");
pw.env.set("method", "get");
```

Goto the pre-request script tab and copy-paste the above [ECMAScript](https://tc39.es/ecma262) code as shown below:

These variables can be accessed in the request section by referencing them in double angle brackets `<<variable_name>>`. So the URL will be `<<baseURL>>/<<method>>`.

### Generating random Values to test API

Let us take a case where we need to test random test-user data available at an endpoint.

Let us use the following GET API endpoint `https://reqres.in/api/users/`.

Add `<<randomValue>>` to the endpoint URL.

```
https://reqres.in/api/users/<<randomValue>>
```

Now in the pre-request script tab add the following logic.

```javascript theme={null}
var random = Math.floor(Math.random() * 10);
pw.env.set("randomValue", random.toString());
```

The [ECMAScript](https://tc39.es/ecma262) code will assign a random number to the environment variable `randomValue` and the API will return a random user associated with the random value.

You will get a similar response as shown below:

```json theme={null}
{
  "data": {
    "id": 4,
    "email": "eve.holt@reqres.in",
    "first_name": "Eve",
    "last_name": "Holt",
    "avatar": "https://reqres.in/img/faces/4-image.jpg"
  },
  "support": {
    "url": "https://reqres.in/#support-heading",
    "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
  }
}
```


# Request headers
Source: https://docs.hoppscotch.io/documentation/getting-started/rest/request-headers

Request Headers allow you to pass additional information with requests, helping to control how the server responds.

Request Headers are key-value pairs that the client sends to the server with an HTTP request. These headers carry extra details about your request, helping the server understand its context and tailor the response to fit.

## Headers Tab

In Hoppscotch, you can easily set and manage request headers using the **Headers tab**. This tab allows you to define **`key-value`** pairs, and you can also add a **`description`** for each header to keep track of its purpose.

Here are a few common headers you might set:

| **Header**        | **Description**                                                                           |
| ----------------- | ----------------------------------------------------------------------------------------- |
| **Authorization** | Used for passing credentials, such as tokens, to authenticate the client with the server. |
| **Content-Type**  | Indicates the format of the data being sent, like `application/json`.                     |
| **Accept**        | Tells the server what media types the client can handle in the response.                  |
| **Cache-Control** | Controls caching behavior in both requests and responses.                                 |
| **User-Agent**    | Provides information about the client making the request.                                 |

<Note> When the **Authorization and Content-Type** values are set through their respective sections, the description fields in their auto-generated headers are disabled for manual input, leaving the value empty. In contrast, for **Inherited** headers, the specified values are automatically populated in the description fields. </Note>

Hoppscotch offers a variety of header options beyond these five examples, allowing you to customize how the server processes your requests to meet specific requirements.

### Bulk edit request headers

Using the  <Icon icon="pen-to-square" />  **Bulk edit** feature in Hoppscotch's request headers tab, you can input and manage multiple headers simultaneously, with each header on a new line and the key and value separated by a **colon (:)**. For example,

```yaml theme={null}
Authorization: Bearer token123
Content-Type: application/json
# User-Agent: CustomAgent/1.0
```


# Request parameters
Source: https://docs.hoppscotch.io/documentation/getting-started/rest/request-parameters

Request parameters help you to filter and request specific data from an API endpoint.

Query parameters help you to filter and request specific data from an API endpoint.

<Tip>
  You can add query parameters in two ways:

  1. Add them in the URL.
  2. Add them in the parameters tab.
</Tip>

## Adding parameters in the URL

To add a parameter in the URL, append `?` at the end of the URL and add a parameter in `key=value` format.

You can add multiple parameters by separating them using `&`.

For example, the below URL is filtered to get the data of the first three Pokemon.

```
https://pokeapi.co/api/v2/pokemon/?offset=6&limit=3
```

For which you will get a similar response:

```json theme={null}
{
  "count": 1281,
  "next": "https://pokeapi.co/api/v2/pokemon?offset=9&limit=3",
  "previous": "https://pokeapi.co/api/v2/pokemon?offset=3&limit=3",
  "results": [
    {
      "name": "squirtle",
      "url": "https://pokeapi.co/api/v2/pokemon/7/"
    },
    {
      "name": "wartortle",
      "url": "https://pokeapi.co/api/v2/pokemon/8/"
    },
    {
      "name": "blastoise",
      "url": "https://pokeapi.co/api/v2/pokemon/9/"
    }
  ]
}
```

## Using the parameters tab

You can use the **Parameters tab** to set **`key-value`** pairs for your API requests. This tab also lets you add a **`description`** for each parameter, helping you provide a clear explanation of what each parameter does and why it's important.

Hoppscotch also offers a <Icon icon="pen-to-square" />  **Bulk edit** feature, allowing you to add or modify multiple request parameters at once, with each key-value pair on a new line separated by a **colon (:)**. For example,

```yaml theme={null}
param1: value1
param2: value2
# param3: value3
```

Try using the parameters tab to see if you get the same response as adding parameters in the URL.


# Response handling
Source: https://docs.hoppscotch.io/documentation/getting-started/rest/response-handling

View, interpret and manage responses from your API requests.

A REST API response is the data returned by the API after an application makes an HTTP request. It typically includes an HTTP status code indicating the result of the request, a response body that contains the requested data, and headers that provide metadata. The response may also include cookies set by the server.

Hoppscotch uplifts this experience by providing an intuitive interface for analyzing responses, making it easier for you to visualize and interact with API data effectively.

## **Response Body**

Depending on the content type of the response, Hoppscotch automatically presents the data in the appropriate format:

* **JSON:** Formats the response in a structured JSON format for easy readability.
* **HTML:** Renders the response as HTML for visual representation and structure content as a web page.
* **XML:** Shows the response in XML format for compatibility with XML-based APIs.
* **Image:** Displays image responses directly in the interface.

<Tabs>
  <Tab title="JSON">
    ```json theme={null}
    {
      "name": "Hoppscotch",
      "type": "Open-source API Development Ecosystem",
      "description": "A powerful platform for developing and testing APIs with an intuitive interface.",
      "url": "https://hoppscotch.io"
    }
    ```
  </Tab>

  <Tab title="HTML">
    ```html theme={null}
    <!DOCTYPE html><html lang="en">
      <head>
          <meta charset="UTF-8">
          <meta name="viewport" content="width=device-width, initial-scale=1.0">
          <title>Hoppscotch API</title>
      </head>
      <body>
          <h1>Hoppscotch</h1>
          <p><strong>Type:</strong> Open-source API Development Ecosystem</p>
          <p><strong>Description:</strong> A powerful platform for developing and testing APIs with an intuitive interface.</p>
          <p><strong>URL:</strong> <a href="https://hoppscotch.io">https://hoppscotch.io</a></p>
      </body>
      </html>
    ```
  </Tab>

  <Tab title="XML">
    ```xml theme={null}
    <?xml version="1.0" encoding="UTF-8"?>
      <api>
          <name>Hoppscotch</name>
          <type>Open-source API Development Ecosystem</type>
          <description>A powerful platform for developing and testing APIs with an intuitive interface.</description>
          <url>https://hoppscotch.io</url>
      </api>
    ```
  </Tab>

  <Tab title="Image">
    <Frame>
      <img />
    </Frame>
  </Tab>
</Tabs>

### Raw Response

The **Raw** response tab in Hoppscotch presents the unprocessed response body, allowing you to view the exact data returned by the API without any formatting which can be particularly used for debugging or when you need to inspect the original response directly.

## Response Headers

Response **Headers** give you important information about the API response that goes beyond just the data itself. They include information such as the content type, which indicates the format of the response (e.g., `application/json` or `text/html`), caching directives that control how the response can be stored and reused, security settings like CORS (Cross-Origin Resource Sharing) that help manage access, and various server-related information, like the server type and version.

## Test Results

The **Test Results** section displays the outcomes of any assertions made on the API response, allowing you to verify key aspects such as status codes, response times, and the presence of expected data.

## Save a response as an Example

In Hoppscotch, an example connects a specific request with its response, providing a complete view of how an API behaves. Each example includes the essential request details alongside the response information. You can create multiple examples for a single request, which is valuable for illustrating how the same endpoint might respond differently under various conditions.

**To save a response as an example in Hoppscotch, follow these steps:**

* Navigate to the right-sidebar and select the collection with your request.
* Choose the request and hit **"Send.”**
* In the response section, click the **"Save as Example"** icon.
* The example will be stored in request's history in the collection for easy retrieval and reference later.
* Click on the example and select **"Try"** to open it as a request in a new tab.

You can easily `Edit` the response details using the **<Icon icon="ellipsis-vertical" />** menu icon, `Save` any changes made to the examples, and `Duplicate` them to generate various iterations.

**Using examples for API mocking:**

Saved examples can be used to create [mock servers](/documentation/features/mock) in Hoppscotch. When you create a mock server from a collection, each saved example automatically becomes a mock route with the exact response you captured. This lets you quickly convert real API behavior into mock endpoints for testing, prototyping, or development without a backend.

<Tip>Hoppscotch also supports **importing** collections with **examples** attached to each request from various platforms, including **Postman, Insomnia, OpenAPI, and Hoppscotch.**</Tip>

## Filter Response Body

To extract specific data points from the response body, you can apply filters using [jq](https://jqlang.github.io/jq/) syntax. jq is a powerful and flexible command-line JSON processor that allows you to slice, filter, map, and transform JSON data with ease.

<Warning>**Migration Notice:** JSONPath has been replaced with jq for JSON response filtering. If you have existing JSONPath filters, you'll need to migrate them to jq syntax. Refer to the [jq manual](https://jqlang.github.io/jq/manual/) for detailed documentation on jq syntax and features.</Warning>

## **Download Response**

You can download the response in various formats (JSON, XML, etc.) for offline analysis or record-keeping. Click the **"Download"** button and choose the format you wish to save.

## **Copy Response**

To copy the entire response to the clipboard, simply click the **"Copy"** button.

## **Generate Data Schema**

Using the **"More"** menu, you can generate a structured representation of the response data tailored to specific programming languages. You can **download the file** or **copy the response** in languages like TypeScript, C#, Go, and others, making it simpler for you to incorporate API responses into your applications.


# Tests
Source: https://docs.hoppscotch.io/documentation/getting-started/rest/tests

Tests are executed after a response is received from the server. You can add multiple tests to a request. You can add tests to both requests saved and not saved in a collection.

## Scripts

Hoppscotch lets you add dynamic behavior to REST requests. This allows you to write test suites and build requests that can contain dynamic parameters. You can add JavaScript code that executes at two events in the flow:

* Tests are executed after a response is received from the server
* You can add multiple tests to a request
* You can add tests to both requests saved and not saved in a collection

<Tip>Hoppscotch will then execute the scripts after the response is received.</Tip>

## Post-request tests

As you introduce new code, tests ensure that your API is working as intended. The higher your test coverage, the more flexible and bug-resistant your code will be. You'll be spending less time wondering why [deleting a picture of a coconut breaks your code](https://www.thegamer.com/this-coconut-jpg-in-team-fortress-2s-game-files-if-deleted-breaks-the-game-and-no-one-knows-why).

## Writing post-request tests

Hoppscotch ships a powerful API called `pw` which can handle post-request scripts as well as tests. Here we'll use `pw` to run tests on the response received from APIs.

## Examples

Let us look at some examples of how you can use Hoppscotch to write tests.

### Test response status code

Let us write a test to check whether the response to our request has a status code of 200. Which means that there are no errors in the response body. We'll use the below URL with the GET method.

```
https://www.httpbin.org/status/200
```

In this case, we'll need to write two expect statements one for checking the status and another for checking the response body. However, we can wrap expect statements with the `test` method from the `pw` API to group related statements.

There are two ways to test the status code:

| Condition                       | Code                                           |
| ------------------------------- | ---------------------------------------------- |
| Check if response code is `200` | `pw.expect(pw.response.status).toBe(200)`      |
| In-built matcher function       | `pw.expect(pw.response.status).toBeLevel2xx()` |

<CodeGroup>
  ```javascript Response code 200 theme={null}
  pw.test("Response is ok", () => {
    pw.expect(pw.response.status).toBe(200);
  });
  ```

  ```javascript Matcher function theme={null}
  pw.test("Response is ok", () => {
    pw.expect(pw.response.status).toBeLevel2xx();
  });
  ```
</CodeGroup>

The tests will have passed once you click on the "**Send**" button.

### Assert response payload

In this example, we test whether a user id points to a particular user.
Let us use the following GET API endpoint

```
https://reqres.in/api/users/10
```

We will use `.toBe()` to assert specific values and `.toBeType()` to assert specific data types as shown in the code snippet below:

```javascript theme={null}
pw.test("Check first name", () => {
  const user = pw.response.body.data;
  pw.expect(user.first_name).toBe("Byron");
  pw.expect(user.first_name).toBeType("string");
});
```

Running the test will produce the result as shown below:

```json theme={null}
  {
    "data": {
      "id": 10,
      "email": "byron.fields@reqres.in",
      "first_name": "Byron",
      "last_name": "Fields",
      "avatar": "https://reqres.in/img/faces/10-image.jpg"
    },
    "support": {
      "url": "https://contentcaddy.io?utm_source=reqres&utm_medium=json&utm_campaign=referral",
      "text": "Tired of writing endless social media content? Let Content Caddy generate it for you."
    }
  }
```


# Uploading data
Source: https://docs.hoppscotch.io/documentation/getting-started/rest/uploading-data

Learn how to upload data to an API using Hoppscotch.

APIs can also be used to upload encoded content to a server. This is usually done with `PUT` or `POST` methods.

The most common content types are:

* `application/json`: for content in JSON format
* `multipart/form-data`: for uploading encoded files
* `application/octet-stream`: for uploading binary data directly

## Uploading a file

To upload a file, the data you send in a `POST` request must be of the content types `application/x-www-form-encoded` and `multipart/form-data`.

## Uploading an image

Let's take a look at **uploading an image** file to an API using Hoppscotch:

1. Select the `POST` HTTP method and set your API Endpoint URL.
2. Add the necessary headers.
3. To add your image file click in the body tab and select `multipart/form-data` in the content-type dropdown.
4. Give your file a name and click on `choose files` to select your file.
5. Click "**Send**" to upload your file.

The <Icon icon="pen-to-square" />  **Bulk Edit** feature is available for `multipart/form-data` as well. Instead of adding or editing key-value pairs one by one, you can now manage them all at once.

### Set Content Type for Specific Parameters in `multipart/form-data`

When sending multiple types of data in a single request using `multipart/form-data`, you can assign a specific content type to each parameter in Hoppscotch. Here's how:

1. Go to the **Body** tab and select `multipart/form-data` from the **Content Type** dropdown.
2. Add the required data for your request by uploading files or entering values.
3. To specify content types for parameters, enable the **"Show Content Type"** option. Then, choose the appropriate content type for each parameter (e.g., `text/plain` for plain text, `image/png` for a PNG image or `application/json` for JSON data).
4. Click **Send** to submit the multipart data, with each parameter using its specified content type.

## Uploading Binary Data

When uploading binary files, you may want to send raw binary data instead of files in a multipart form. This is typically done using the `application/octet-stream` content type. Follow these steps to upload binary data:

1. Select the **POST** or **PUT** HTTP method and set your API Endpoint URL.
2. In the **Body** tab, select `application/octet-stream` from the **Content Type** dropdown.
3. Upload your binary data by selecting the file from your local machine.
4. Click **Send** to upload the binary data.

<Note> Currently, the **Hoppscotch Desktop App** does **NOT** support uploading **Binary files** directly as request bodies for APIs. </Note>


# Setup Hoppscotch
Source: https://docs.hoppscotch.io/documentation/getting-started/setup

Learn how to setup Hoppscotch.

To get started with Hoppscotch, you need to choose a platform to use it on. Hoppscotch is available on the following platforms:

* [Web](#web-app)
* [Desktop](#desktop-app)
* [CLI](#cli)

## Web

To get started with Hoppscotch web client, head to [hoppscotch.io](https://hoppscotch.io) and start using it right away for free.

<CardGroup>
  <Card title="Learn more" icon="circle-arrow-right" href="/documentation/clients/web" />

  <Card title="Open Web App" icon="circle-arrow-right" href="https://hoppscotch.io" />
</CardGroup>

## Desktop

Hoppscotch Desktop App is a cross-platform desktop application built with Tauri and Hoppscotch Web Client. It is a standalone version of Hoppscotch that can be installed on your computer and used without a browser. Hoppscotch Desktop App is available for Mac, Windows and Linux.

<CardGroup>
  <Card title="Learn more" icon="circle-arrow-right" href="/documentation/clients/desktop" />

  <Card title="Download Desktop App" icon="circle-arrow-right" href="https://hoppscotch.com/download" />
</CardGroup>

## CLI

Hoppscotch CLI is the command-line interface for Hoppscotch. It is a standalone version of Hoppscotch that can be installed on your computer and used without a browser. Hoppscotch CLI is available as an npm package.

<CardGroup>
  <Card title="Learn more" icon="circle-arrow-right" href="/documentation/clients/cli/overview" />

  <Card title="Install CLI" icon="circle-arrow-right" href="https://www.npmjs.com/package/@hoppscotch/cli" />
</CardGroup>


# Troubleshooting
Source: https://docs.hoppscotch.io/documentation/getting-started/troubleshooting

Facing issues with Hoppscotch? Check out this page to resolve them.

If you're facing issues with Hoppscotch, you can try the following steps to resolve them.

## Connectivity

If Hoppscotch fails to send your request, it could be because you may be experiencing connectivity issues. Check your connection by attempting to open a page in your web browser.

## Firewalls

Sometimes firewalls may be configured to block non-browser connections. You might need to contact your network administrator so that Hoppscotch can work seamlessly.

## Incorrect protocol

You might have specified the wrong protocol, check if you're using `https://` or `http://` in your URL or vice-versa.

## Hoppscotch errors

It could also be possible that Hoppscotch might be making invalid requests to your API server. You can confirm this by checking your server logs (if available). If you believe this is happening, do get in touch with the Hoppscotch team.

## CORS restrictions

CORS or Cross-Origin Resource Sharing is a security mechanism built into modern web browsers. It may cause the following error when testing API endpoints or some other API endpoints with Hoppscotch.

This is because the API not sending the proper API headers (`Access-Control-Allow-Origin`) and can be solved in the following ways:

1. Use the [Hoppscotch Desktop App](/documentation/clients/desktop) which is not subject to CORS restrictions.
2. Use middleware like the Proxy mode, [Proxy Interceptor](https://github.com/hoppscotch/proxyscotch), or the [Hoppscotch Browser Extension](https://github.com/hoppscotch/hoppscotch-extension), and enable it in the "**Interceptor**" section of "**Settings**".

## Something went wrong

If you're still facing issues, with an error message that says "Something went wrong", help us to better understand the issue by:

1. Opening the developer tools in your browser (usually by pressing `F12` or `Ctrl/Cmd`+`Shift`+`I`).
2. Switch to the "**Console**" tab.
3. Reproduce the issue.
4. Take a screenshot of the console and send it to us.

<Info>Report a bug by [opening a new issue](https://github.com/hoppscotch/hoppscotch/issues/new/choose).</Info>


# i18n
Source: https://docs.hoppscotch.io/documentation/i18n

Internationalization and localization.

Thanks for showing your interest in helping us to translate the software.

## Creating a new translation

Before you start working on a new language, please look through the [open pull requests](https://github.com/hoppscotch/hoppscotch/pulls) to see if anyone is already working on a translation. If you find one, please join the discussion and help us keep the existing translations up to date.

if there is no existing translation, you can create a new one by following these steps:

1. **[Fork the repository](https://github.com/hoppscotch/hoppscotch/fork).**
2. **Checkout the `main` branch for latest translations.**
3. **Create a new branch for your translation with base branch `main`.**
4. **Create target language file in the [`/packages/hoppscotch-common/locales`](https://github.com/hoppscotch/hoppscotch/tree/main/packages/hoppscotch-common/locales) directory.**
5. **Copy the contents of the source file [`/packages/hoppscotch-common/locales/en.json`](https://github.com/hoppscotch/hoppscotch/blob/main/packages/hoppscotch-common/locales/en.json) to the target language file.**
6. **Translate the strings in the target language file.**
7. **Add your language entry to [`/packages/hoppscotch-common/languages.json`](https://github.com/hoppscotch/hoppscotch/blob/main/packages/hoppscotch-common/languages.json).**
8. **Save and commit changes.**
9. **Send a pull request.**

*You may send a pull request before all steps above are complete: e.g., you may want to ask for help with translations, or getting tests to pass. However, your pull request will not be merged until all steps above are complete.*

Completing an initial translation of the whole site is a fairly large task. One way to break that task up is to work with other translators through pull requests on your fork. You can also [add collaborators to your fork](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/inviting-collaborators-to-a-personal-repository) if you'd like to invite other translators to commit directly to your fork and share responsibility for merging pull requests.

## Updating a translation

### Corrections

If you notice spelling or grammar errors, typos, or opportunities for better phrasing, open a pull request with your suggested fix. If you see a problem that you aren't sure of or don't have time to fix, [open an issue](https://github.com/hoppscotch/hoppscotch/issues/new/choose).

### Broken links

When tests find broken links, try to fix them across all translations. Ideally, only update the linked URLs, so that translation changes will definitely not be necessary.


# GraphQL
Source: https://docs.hoppscotch.io/documentation/protocols/graphql

GraphQL is a query language for APIs that queries the server and provides the client only the data that is requested by the client. GraphQL enables you to fetch data from multiple APIs in a single query thus helping you build better-performing applications.

## Platform

Hoppscotch has a built-in GraphQL platform that can be used to execute GraphQL queries. The GraphQL platform can be accessed by clicking on the `GraphQL` tab in the left sidebar.

The GraphQL platform has the following features:

* **GraphQL editor** - The GraphQL editor can be used to write GraphQL queries. The editor has syntax highlighting and auto-completion support for GraphQL queries.
* **Collections** - The GraphQL platform supports collections. You can save your GraphQL queries in a collection and execute them later.
* **Variables** - The GraphQL platform supports variables. You can define variables in the GraphQL query and pass the values of the variables in the variables section.
* **Headers** - The GraphQL platform supports headers. You can add custom headers to the GraphQL query.
* **Authentication** - The GraphQL platform supports authentication. You can add authentication to the GraphQL query.
* **Schema Explorer** - The GraphQL platform has a schema explorer. You can use the schema explorer to explore the GraphQL schema.
* **Documentation Explorer** - The GraphQL platform has a documentation explorer. You can use the documentation explorer to explore the documentation of the GraphQL schema.

## API Testing

Hoppscotch's GraphQL API platform provides you with the best experience to test and play around with GraphQL.

It's primarily divided into two sections along with other features to help you build and test queries.

## Request

The request section houses the feature to enter your server endpoint and initiate a connection.

Once the connection is made, the `query` builder assists you in designing queries to fetch the data that you require and run it.

You can also add dynamic behavior to your queries by defining `variables`, `headers`, and `authorization`.

## Response

This is where you see the responses to your API endpoints. You can download and copy the returned responses for further use.

## Schema

GraphQL is a query language for APIs that queries the server and provides the client only the data that is requested by the client. GraphQL enables you to fetch data from multiple APIs in a single query thus helping you build better-performing applications.

GraphQL server uses a GraphQL Schema to describe the structure of your data. Given below is an example of a GraphQL Schema.

```graphql theme={null}
type Laptop {
  model: String
  maker: Maker
}

type Maker {
  name: String
  laptops: [Laptop]
}
```

The above schema defines two types `Laptop` and `Maker`. The `Laptop` type has two fields `model` and `maker`. The `Maker` type has two fields `name` and `laptops`. The `laptops` field in the `Maker` type is an array of the `Laptop` type.

GraphQL queries are written in the GraphQL query language. Given below is an example of a GraphQL query.

```graphql theme={null}
query {
  maker(name: "Apple") {
    name
    laptops {
      model
    }
  }
}
```

The above query fetches the `name` and `laptops` of the `Maker` with the name `Apple`.

GraphQL queries can be executed using a GraphQL client. Hoppscotch has a built-in GraphQL client that can be used to execute GraphQL queries.

## Other features

### Documentation

GraphQL documentation is where you can view the documentation provided by the developer.

### Explorer

GraphQL uses a schema to define the structure of the data, the schema explorer helps you to understand how your data is structured.

The GraphQL platform also houses other features like:

* [Environments](/documentation/features/environments)
* [Collections](/documentation/features/collections)
* [History](/documentation/features/history)


# Realtime
Source: https://docs.hoppscotch.io/documentation/protocols/realtime

Hoppscotch's Realtime API platform helps you test your real-time APIs easily.

## Platform

Hoppscotch has a built-in real-time platform that can be used to execute real-time requests. The real-time client platform can be accessed by clicking on the `Realtime` tab in the left sidebar.

Realtime protocols are used in communication, entertainment, and even in the Internet of Things (IoT) to deliver and handle real-time messages, audio, etc.

With Hoppscotch you can work with the following real-time protocols:

* WebSocket
* Socket.IO
* SSE
* MQTT

## API Testing

Hoppscotch's Realtime API platform helps you test your real-time APIs easily.

It's primarily divided into two sections the request section and the response section.

## Request

The request section houses the feature to enter your server endpoint and initiate a connection. You also get the option to choose from four different protocols `WebSocket`, `SSE`, `Socket.IO`, and `MQTT`.

## Response

Once the connection is established, you can view the responses and logs in the response section.

## WebSocket

WebSockets are an alternative to HTTP communication in Web Applications. They offer a long-lived, bidirectional communication channel between client and server. Once established, the channel is kept open, offering a very fast connection with low latency and overhead. This makes them ideal for real-time applications.

WebSockets are perfect for scenarios such as:

* When you need to support real-time communication between the client and the server.
* When you need to support a protocol that is more efficient than HTTP.
* When you need to support a protocol that is more efficient than long polling.

## Socket.IO

Socket.io is a real-time event-based communication library built on webSocket. It enables real-time, bi-directional communication between web clients and servers.

Socket.io is perfect for scenarios such as:

* When you need to support older browsers that don't support WebSockets.
* When you need to support polling transports for mobile devices.
* When you need to support multiple transports for a single connection.

## SSE

SSE is a standard describing how servers can initiate data transmission towards clients once an initial client connection has been established. An SSE connection can discard processed messages without accumulating all of them in memory making it a memory-efficient implementation of XHR streaming.

SSE is perfect for scenarios such as:

* When an efficient unidirectional communication protocol is needed that won't add unnecessary server load (which is what happens with long polling).
* When you need a protocol with a predefined standard for handling errors.
* When you want to use HTTP-based methods for real-time data streaming.

## MQTT

Message Queuing Telemetry Transport (MQTT) protocol is a publish/subscribe protocol that is lightweight and requires minimal memory, CPU, and bandwidth to connect IoT devices. Unlike HTTP's request/response paradigm, MQTT is event-driven and enables messages to be pushed to clients.

Once connected to the MQTT server, you can either publish a message under a topic or subscribe to a topic to get messages about that topic being sent across the server in real time.

MQTT is perfect for scenarios such as:

* When you need to support real-time communication between the client and the server.
* When you need to support a protocol that is more efficient than HTTP.


# RESTful
Source: https://docs.hoppscotch.io/documentation/protocols/rest

RESTful API testing with Hoppscotch.

## Platform

Hoppscotch has a built-in REST platform that can be used to execute REST API requests. The REST platform can be accessed by clicking on the `REST` tab in the menu.

The REST platform has the following features:

* **Request editor** - The request editor can be used to write REST API requests. The editor has syntax highlighting and auto-completion support for REST API requests.
* **Collections** - The REST platform supports collections. You can save your REST API requests in a collection and execute them later.
* **Variables** - The REST client supports variables. You can define variables in the REST API request and pass the values of the variables in the variables section.
* **Headers** - The REST platform supports headers. You can add custom headers to the REST API request.
* **Authentication** - The REST platform supports authentication. You can add authentication to the REST API request.
* **Pre-request scripts** - The REST platform supports pre-request scripts. You can write pre-request scripts to modify the request before it is sent to the server.
* **Tests** - The REST platform supports tests. You can write tests to verify the response of the REST API request.
* **Response viewer** - The REST platform has a response viewer. You can use the response viewer to view the response of the REST API request.
* **Environments** - The REST platform supports environments. You can create multiple environments and switch between them.

Representational State Transfer (REST) API is a software interface that enables two systems to communicate on the Internet. A REST API can do operations like creating, deleting, and modifying data. REST APIs are built on top of the HTTP protocol and have dedicated HTTP methods to perform operations.

REST APIs are stateless, which means that the server does not store any information about the client. This makes REST APIs scalable and easy to maintain.

## API Testing

Hoppscotch's REST API platform provides you with a fast and seamless experience to test and debug your API endpoints.

It's primarily divided into two sections along with other features to help you build better APIs.

## Request

The request section provides you the capability to define your API endpoint and initiate the communication.

You can select from a range of HTTP methods such as `GET`, `POST`, `PUT` etc. You can read more about HTTP methods in [RESTful protocol](/documentation/protocols/rest).

You can also add dynamic behaviors to your requests by specifying `Headers`, `Request Body`, `Authorization Headers`, `Parameters`, and `Pre-request scripts`.

Hoppscotch also provides the capability to run `Tests` on the responses you receive.

## Response

This is where you see the responses to your API endpoints. You can download and copy the returned responses for further use.

## HTTP Methods

REST APIs use HTTP methods to perform operations. The most common HTTP methods are:

| HTTP Method | Usage                                            |
| ----------- | ------------------------------------------------ |
| GET         | Retrieve information about the REST API resource |
| POST        | Create a REST API resource                       |
| PUT         | Update a REST API resource                       |
| DELETE      | Delete a REST API resource or related component  |

Other methods like `HEAD`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH` and other `CUSTOM` methods can also be used.

## HTTP Status Codes

HTTP status codes are used to indicate the status of the HTTP request. The most common HTTP status codes are:

| Status Code | Description           |
| ----------- | --------------------- |
| 200         | OK                    |
| 201         | Created               |
| 204         | No Content            |
| 400         | Bad Request           |
| 401         | Unauthorized          |
| 403         | Forbidden             |
| 404         | Not Found             |
| 405         | Method Not Allowed    |
| 500         | Internal Server Error |

Other status codes like `301`, `302`, `304`, `307`, `308`, and other `5XX` codes can also be used.

## Other features

The REST API platform also houses other features like:

* [Environments](/documentation/features/environments)
* [Collections](/documentation/features/collections)
* [History](/documentation/features/history)


# Admin dashboard
Source: https://docs.hoppscotch.io/documentation/self-host/community-edition/admin-dashboard

Get started with the Hoppscotch Admin Dashboard.

The Admin Dashboard serves as the central hub for managing your workspaces and user-related activities. From here, you can efficiently oversee and control various aspects of your platform.

* Insights Dashboard: Gain valuable insights into platform usage.
* Manage Users: Handle user-related actions, such as inviting, elevating admins, and deleting users.
* Manage Workspaces: Create, edit, and delete workspaces while managing workspace-specific details and user memberships.

## Dashboard

The Dashboard section provides an overview of essential metrics and statistics regarding users, workspaces, and activity. This snapshot allows you to track the usage and performance of your platform.

Get insights into your organization's usage of Hoppscotch.

* Number of Users: Monitor the count of registered users.
* Number of Workspaces: Keep track of the total number of workspaces.
* Number of Requests: Measure the volume of requests made by your organization.
* Number of Collections: Track the quantity of collections within the platform.

## Manage users

The Users section empowers you to effectively control user-related actions. It streamlines the process of user management, making it simple to oversee the user base.

<Info>In Hoppscotch Community Edition, any user can create an account and use the platform.</Info>

* User List: View a comprehensive list of all users on your platform.
* Invite Users: Send invitations to new users, welcoming them to the platform.
* Admin Privileges: Elevate users to administrative roles for increased permissions.
* User Deletion: Delete users when necessary.

### Invite Users

Admins can invite new users to their Hoppscotch instance. Depending on whether SMTP is configured, the process differs slightly.

#### With SMTP

When SMTP is enabled from the Admin Dashboard and the required SMTP configurations are correctly set, follow these steps to invite a new user:

1. Go to the **Users** section within the Admin Dashboard.
2. Select the **Invite User** button to open the invitation modal.
3. Enter the email address of the user you want to invite and click **Add User** to send an invitation.
4. An email containing an invite link (`http://localhost:3000`) will be sent to the invitee. They can use this link to log in to the Hoppscotch web app.
5. Alternatively, you can copy the invite link and share it through other platforms with the new user. Make sure the user signs in using the email address specified during the invitation process.

#### Without SMTP

If SMTP is disabled from the Admin Dashboard, the invitation process is slightly different:

1. Go to the **Users** section within the Admin Dashboard.
2. Select the **Invite User** button to open the invitation modal.
3. Enter the email address of the user you want to invite and click **Add User**.
4. An invite link (`http://localhost:3000`) will be generated and displayed. Copy this link and share it with the user via your preferred communication channel. Make sure the user signs in to Hoppscotch using the same email address you provided during the invitation.

### Pending Invites

Within the **Users** section, admins can view a list of all users who have been invited but have not yet joined the organization. To access this list, simply click on the **Pending Invites** button next to "Invite User". Here, you'll see all the invitations you've sent, along with details such as:

* **Invitee Email:** The email address to which the invite was sent.
* **Invited By:** The email address of the user who sent the invitation
* **Invited on:** The date and time when the invitation was sent.

**You can also consider the following actions:**

* **Copy Invite Link:** If you need to resend the invitation, you can easily `copy` the invite link and share it with the user via any communication platform.
* **Revoke Invitation:** If you wish to cancel an invitation, click the `Revoke Invitation` button next to the specific user invite in the **Action** column. This will remove the pending invite from the list and prevent the user from accessing your Hoppscotch instance using that link.

## Manage Workspaces

In the Manage Workspace section, you can efficiently handle workspace-related operations, ensuring that collaborations and projects run smoothly.

* Workspace Creation: Establish new workspace tailored to specific projects or departments.
* Workspace Editing: Modify workspace details and configurations as needed.
* Workspace Deletion: Disband workspaces that are no longer relevant.
* User Memberships: View and manage the users associated with each workspace.

## Infra-tokens

InfraTokens are special UUID tokens that provide a secure way for admins to interface with Self-Hosted APIs. They are exclusively accessible to admins, ensuring that only authorized personnel can manage sensitive operations. Unlike Personal Access Tokens, which are tied to individual users, InfraTokens are scoped at the instance level, granting access to all admins within the instance.

#### Generate an InfraToken

Follow these steps to create a new InfraToken:

1. After logging into your Self-Hosted instance using your admin credentials, go to **Settings > Infra Tokens** in your Admin Dashboard.
2. Click **Generate new token**.
3. Enter a title for the token and select an expiration date. Available options include 7 days, 30 days, 60 days, 90 days, or no expiry.
4. Confirm creation. **The new InfraToken will be displayed once — copy it securely** to your clipboard for immediate use.
5. To delete a token, return to the **Infra Tokens** section and remove it.

<Note>The details of the admin who created the InfraToken are stored for audit purposes. All admins can view and manage these tokens.</Note>

#### How to use InfraTokens

InfraTokens are used as **Bearer tokens**. When making requests to the User Management APIs, include the `InfraToken` in the `Authorization` header as follows:

```bash theme={null}
Bearer <Your_InfraToken>
```

#### APIs for User Management

The RESTful APIs designed for User Management enable admins to perform a wide range of user-related actions, such as inviting new users, deleting existing ones, and updating user details. These APIs provide admins with the ability to efficiently manage user accounts and permissions. The table below introduces nine key APIs that give admins greater control over user management.

| User Activity                          | Description                                                                   | Method | Endpoint                                       |
| -------------------------------------- | ----------------------------------------------------------------------------- | ------ | ---------------------------------------------- |
| Invite a New User                      | Allows admins to invite a new user to the instance.                           | POST   | `<base-url>/v1/infra/user-invitations`         |
| View Pending Invites                   | Retrieves a list of all pending invites sent to new users.                    | GET    | `<base-url>/v1/infra/user-invitations`         |
| Delete Pending Invites                 | Enables admins to delete specific pending invites using their Email ID.       | DELETE | `<base-url>/v1/infra/user-invitations`         |
| View All Users                         | Provides a list of all users in the instance.                                 | GET    | `<base-url>/v1/infra/users`                    |
| View a Particular User                 | Fetches details of a specific user in the instance by their User ID.          | GET    | `<base-url>/v1/infra/users/{uid}`              |
| Delete an existing User                | Enables admins to delete an existing user from the instance by their User ID. | DELETE | `<base-url>/v1/infra/users/{uid}`              |
| Update User Details                    | Allows admins to update the details of an existing user.                      | PATCH  | `<base-url>/v1/infra/users/{uid}`              |
| Manage Admin Status                    | Enables admins to add or remove admin status for an existing user.            | PATCH  | `<base-url>/v1/infra/users/{uid}/admin-status` |
| Fetch User's involvement in Workspaces | Retrieves workspace details that a user is part of, including their role.     | GET    | `<base-url>/v1/infra/users/{uid}/workspaces`   |

<Info>To interact with the User Management APIs, ensure that your backend service is running, either on your local machine or on a server. The API documentation is accessible at the `/api-docs` endpoint relative to your backend service URL. For example, if your backend is running locally, you can access the API docs at [http://localhost:3170/api-docs](http://localhost:3170/api-docs). You can also retrieve the OpenAPI v3 JSON format at [http://localhost:3170/api-docs-json](http://localhost:3170/api-docs-json).</Info>

## Server Settings

In the **Server Settings** section, you have the ability to both view and edit the environment variables that were configured during the setup of your self-hosted instance.

### Configurations

1. **Configure Authentication Providers:**
   Customize authentication providers, including Google, Microsoft, GitHub, and email, directly from the settings page.

2. **Configure SMTP Settings:**
   Set up your SMTP settings for seamless email integration.

3. **History Configurations:**
   Control the logging of request history for all users with a simple toggle option.

   * **When enabled:** Request history is visible in the Hoppscotch app, and new entries are actively logged and stored in the database.

   * **When disabled:** Request history is hidden from the Hoppscotch app, and no new request logs are written to the database.

   You can also optionally choose to purge all existing history from the database, ensuring complete removal of previously logged request data.

4. **Data sharing:**
   Enable or disable anonymous data sharing to help improve Hoppscotch. [Learn more about the metrics collected](./telemetry).

5. **Reset Configurations:**
   If needed, reset your configurations back to their original state.

After making any configuration updates, be sure to save the changes. The server will automatically restart to apply the modifications.

## Hard Reset Configurations

If you need to perform a hard reset of the server configurations, execute the following command in your terminal to reset all your environment variables:

```bash theme={null}
docker exec -it <db_container_id> psql -d hoppscotch -c "TRUNCATE \"InfraConfig\";"
```

You can replace `<db_container_id>` with the actual ID of your Docker container.


# Deploy and upgrade
Source: https://docs.hoppscotch.io/documentation/self-host/community-edition/deploy-and-upgrade

Deploy and upgrade Hoppscotch Community Edition on your infrastructure.

This section contains instructions for deploying and upgrading Hoppscotch Community Edition.

## Deploy

Deploy Hoppscotch Community Edition on your infrastructure.

<Info>Instructions for deploying Hoppscotch on your infrastructure are coming soon.</Info>

## Upgrade

Upgrading Hoppscotch Community Edition is a simple process. Follow the instructions below to upgrade your Hoppscotch Community Edition instance.

### Using individual containers for the services

1. Check if there is a new version available by running the following command:

   ```bash theme={null}
   docker images
   ```

2. Update the image to the latest version by running the following command:

   ```bash theme={null}
   docker pull hoppscotch/hoppscotch-frontend:latest
   docker pull hoppscotch/hoppscotch-backend:latest
   docker pull hoppscotch/hoppscotch-admin:latest
   ```

   <Tip>If you want to update to a specific version, run the following command:</Tip>

   ```bash theme={null}
   docker pull hoppscotch/hoppscotch-frontend:<version>
   docker pull hoppscotch/hoppscotch-backend:<version>
   docker pull hoppscotch/hoppscotch-admin:<version>
   ```

3. Start the new container by following the instructions in the [Install and build](/documentation/self-host/community-edition/install-and-build#docker) section.

<Info>For minor version upgrades, you might not need to run the database migrations. However, for major version upgrades, you will need to run the database migrations. Refer to the [Database migrations](/documentation/self-host/community-edition/install-and-build#migrations) section for more information.</Info>

### Using the AIO container

1. Check if there is a new version available by running the following command:

   ```bash theme={null}
   docker images
   ```

2. Update the image to the latest version by running the following command:

   ```bash theme={null}
   docker pull hoppscotch/hoppscotch:latest
   ```

   <Tip>If you want to update to a specific version, run the following command:</Tip>

   ```bash theme={null}
   docker pull hoppscotch/hoppscotch:<version>
   ```

3. Start the new container by following the instructions in the [Install and build](/documentation/self-host/community-edition/install-and-build#docker) section.

<Info>For minor version upgrades, you might not need to run the database migrations. However, for major version upgrades, you will need to run the database migrations. Refer to the [Database migrations](/documentation/self-host/community-edition/install-and-build#migrations) section for more information.</Info>


# Getting started
Source: https://docs.hoppscotch.io/documentation/self-host/community-edition/getting-started

Learn how to get started with Hoppscotch Community Edition.

Community Edition is the perfect starting point for individual developers or small teams looking to integrate Hoppscotch into their workflow without additional costs. It's open-source, meaning you can modify it as needed, though you'll manage updates and maintenance yourself. With Self Host Community edition you get access to Admin Dashboard which acts as a central hub for managing your workspaces and overseeing user-related activities.

<CardGroup>
  <Card title="Prerequisites" icon="circle-arrow-right" href="/documentation/self-host/community-edition/prerequisites">
    Prerequisites to self-host Hoppscotch Community Edition on your infrastructure.
  </Card>

  <Card title="Install and build" icon="circle-arrow-right" href="/documentation/self-host/community-edition/install-and-build">
    Install and build Hoppscotch Community Edition on your infrastructure.
  </Card>

  <Card title="Admin dashboard" icon="circle-arrow-right" href="/documentation/self-host/community-edition/admin-dashboard">
    Manage your Hoppscotch Community Edition instance with the Admin dashboard.
  </Card>
</CardGroup>


# Install and build
Source: https://docs.hoppscotch.io/documentation/self-host/community-edition/install-and-build

Learn how to install and build Hoppscotch Community Edition.

<Tip>If you're interested in deploying <ins>Hoppscotch on Kubernetes</ins>, you can conveniently skip this guide and proceed directly to the [Helm chart deployment guide](/documentation/self-host/helm-chart-deployment/getting-started).</Tip>

## Configuring the environment

Before you get started with the installation, you need to configure the environment variables. Create a `.env` file in the root directory of the project and add the following environment variables:

<Warning>**<u>Ensure that the environment values are not enclosed within quotes \[""].</u>**</Warning>
<Note>To enable desktop app support for self-hosted instances, make sure you've enabled [subpath based access](#subpath-based-access).</Note>

```yaml theme={null}
#-----------------------Backend Config------------------------------#

# Prisma Config
DATABASE_URL=postgresql://username:password@url:5432/dbname # or replace with your database URL

# (Optional) By default, the AIO container (when in subpath access mode) exposes the endpoint on port 80. Use this setting to specify a different port if needed.
HOPP_AIO_ALTERNATE_PORT=80

# Sensitive Data Encryption Key while storing in Database (32 character)
DATA_ENCRYPTION_KEY=********************************

# Whitelisted origins for the Hoppscotch App.
# This list controls which origins can interact with the app through cross-origin comms.
# - localhost ports (3170, 3000, 3100): app, backend, development servers and services
# - app://localhost_3200: Bundle server origin identifier
#   NOTE: `3200` here refers to the bundle server (port 3200) that provides the bundles,
#   NOT where the app runs. The app itself uses the `app://` protocol with dynamic
#   bundle names like `app://{bundle-name}/`
WHITELISTED_ORIGINS=http://localhost:3170,http://localhost:3000,http://localhost:3100,app://localhost_3200,app://hoppscotch

#-----------------------Frontend Config------------------------------#

# Base URLs
VITE_BASE_URL=http://localhost:3000
VITE_SHORTCODE_BASE_URL=http://localhost:3000
VITE_ADMIN_URL=http://localhost:3100

# Backend URLs
VITE_BACKEND_GQL_URL=http://localhost:3170/graphql
VITE_BACKEND_WS_URL=wss://localhost:3170/graphql
VITE_BACKEND_API_URL=http://localhost:3170/v1

# Terms Of Service And Privacy Policy Links (Optional)
VITE_APP_TOS_LINK=https://docs.hoppscotch.io/support/terms
VITE_APP_PRIVACY_POLICY_LINK=https://docs.hoppscotch.io/support/privacy

# Set to `true` for subpath based access
ENABLE_SUBPATH_BASED_ACCESS=false
```

Let's understand the major environment variables:

1. `DATABASE_URL`: This is where you add your Postgres database URL.
2. `HOPP_AIO_ALTERNATE_PORT`: This is an optional variable that lets you specify an alternate port for the AIO container's endpoint when operating in subpath access mode. By default, this endpoint is exposed on port 80.
3. `DATA_ENCRYPTION_KEY`: A 32-character key used for encrypting sensitive data stored in the database.
4. `WHITELISTED_ORIGINS`: URLs of Hoppscotch backend, admin dashboard, frontend app and the bundle server that are allowed to interact with the desktop app.
5. `VITE_BASE_URL`: This is the URL where your deployment will be accessible from.
6. `VITE_SHORTCODE_BASE_URL`: A URL to generate shortcodes for sharing, can be the same as `VITE_BASE_URL`.
7. `VITE_BACKEND_GQL_URL`: The URL for GraphQL within the instance.
8. `VITE_BACKEND_WS_URL`: The URL for WebSockets within the instance.
9. `VITE_BACKEND_API_URL`: The URL for REST APIs within the instance.
10. `VITE_APP_TOS_LINK` and `VITE_APP_PRIVACY_POLICY_LINK` are optional and are used to configure the links to the Terms & Conditions and Privacy Policy.

Third-party auth configs have to be obtained from the respective providers. You can choose and configure the auth providers by following the [configuring OAuth guide](/documentation/self-host/community-edition/prerequisites#oauth).

## Docker

Once the environment variables are configured, you may proceed to the next step of setting up the Hoppscotch instance. Currently, there are two ways to set up Hoppscotch:

1. Using individual containers for the services.
2. Using the AIO container.

* Before proceeding further, ensure that you have a running instance of Postgres.

### Using individual containers for the services

To self-host Hoppscotch Community Edition, you will need the following services running via Docker:

* Hoppscotch frontend
* Hoppscotch backend
* Hoppscotch admin dashboard

Pull the containers from DockerHub with the following command:

```bash theme={null}
docker pull hoppscotch/hoppscotch-frontend
docker pull hoppscotch/hoppscotch-backend
docker pull hoppscotch/hoppscotch-admin
```

After pulling the containers, start Hoppscotch by running all three services:

```bash theme={null}
docker run -p 3000:3000 --env-file .env --restart unless-stopped hoppscotch/hoppscotch-frontend
docker run -p 3170:3170 --env-file .env --restart unless-stopped hoppscotch/hoppscotch-backend
docker run -p 3100:3100 --env-file .env --restart unless-stopped hoppscotch/hoppscotch-admin
```

<Tip>Ensure that the environment variables are configured in the `.env` file and the restart policy is mentioned.</Tip>

<Note>
  To enable desktop app support for your self-hosted Hoppscotch instance, make sure you expose the web app server which is a part of the frontend container. You can do this by running the following command:

  ```bash theme={null}
  docker run -p 3000:3000 -p 3200:3200 --env-file .env --restart unless-stopped hoppscotch/hoppscotch-frontend
  ```
</Note>

Open [admin dashboard](http://localhost:3100) or [`PORT 3100`](http://localhost:3100) in the browser to [setup and access](/documentation/self-host/community-edition/setup-and-access) the Hoppscotch instance.

### Using the AIO container

The All-In-One (AIO) container is a single container that provides all the services required to run Hoppscotch.

Pull the container from DockerHub with the following command:

```bash theme={null}
docker pull hoppscotch/hoppscotch
```

After pulling the container, start Hoppscotch by running the container:

```bash theme={null}
docker run -p 3000:3000 -p 3100:3100 -p 3170:3170 --env-file .env --restart unless-stopped hoppscotch/hoppscotch
```

<Tip>Ensure that the environment variables are configured in the `.env` file and the restart policy is mentioned.</Tip>

Open [admin dashboard](http://localhost:3100) or [`PORT 3100`](http://localhost:3100) in the browser to [setup and access](/documentation/self-host/community-edition/setup-and-access) the Hoppscotch instance.

## Subpath Based Access

To enable subpath based access the following `.env` variable must be set to true, it is set to false by default.

```
ENABLE_SUBPATH_BASED_ACCESS=true
```

<Note>To enable desktop app support for your self-hosted Hoppscotch instance, make sure to set `ENABLE_SUBPATH_BASED_ACCESS` to `true` in your `.env` file.</Note>

When set to true the following is the expected behavior:

### Using individual containers for the services

When using the individual containers it is up to the users to configure a reverse proxy to allow requests made to a specific route to be rerouted to the relevant containers.

### Using the AIO container

When using AIO, when subpath access is set to true the services can be accessed from the following routes

| Service              | Route      |
| -------------------- | ---------- |
| Hoppscotch App       | `/`        |
| Hoppscotch Admin App | `/admin`   |
| Hoppscotch Backend   | `/backend` |

<Warning>
  By default, the AIO container exposes the app on port 80. This can cause conflicts if you're running on a host system where
  port 80 is privileged, such as with Rootless Docker, Podman, or hardened environments like OpenShift. If you experience issues on these setups, try setting `HOPP_AIO_ALTERNATE_PORT` to bind the app to a non-privileged port.
</Warning>

## Migrations

Once the instance of Hoppscotch is up, you need to run migrations on the database to ensure that it has the relevant tables. Depending on how Hoppscotch was set up, the method to run the migrations changes.

### Using individual containers for the services

Run the following command to copy the ID of the **backend container**:

```bash theme={null}
docker ps
```

### Using the AIO container

Run the following command to copy the ID of the **AIO container**:

```bash theme={null}
docker ps
```

### Running migrations

Once the respective container ID is copied, execute the following command to open an interactive shell within the container to execute the migration command:

```bash theme={null}
docker exec -it <container_id> /bin/sh
```

Once inside the container, run the migration using:

```bash theme={null}
pnpm exec prisma migrate deploy
```

Should the user ever encounter the following error:

```bash theme={null}
Database migration not found. Please check the documentation for assistance: https://docs.hoppscotch.io/documentation/self-host/community-edition/install-and-build#running-migrations
```

It means the user is trying to start the backend (or AIO) service before the database has all the relevant tables in it. In order to run the migration to populate the database run the following command.

```bash theme={null}
docker run -it --entrypoint sh --env-file .env <container_name>
```

Making sure to pass in the `.env` file containing the right `.env` variables for the instance. On executing the aforementioned command will result in a shell being opened inside a instance of the container following which user can execute a database migration normally with

```bash theme={null}
pnpm exec prisma migrate deploy
```

Once the database has been successfully run and the database populated with tables the backend containers ( or AIO container) can be started normally.

Note: If user is using `docker compose` to run the services the following command can be used to open a shell inside the backend (or AIO) service.

```bash theme={null}
docker compose run --entrypoint sh <Service_name>
```


# Prerequisites
Source: https://docs.hoppscotch.io/documentation/self-host/community-edition/prerequisites

Prerequisites for installing Hoppscotch on your own infrastructure.

Hoppscotch is a self-hosted API development platform, packaged as a set of Docker containers. You can install and run Hoppscotch on any operating system that can run a [Docker Engine](https://docs.docker.com/engine). You can use Hoppscotch on your local machine or a cloud provider of your choice.

## System Requirements

Hoppscotch is designed to run well on both small and large deployments. The minimum requirements to run Hoppscotch are an operating system that supports Docker and 4 CPU cores + 4GB of RAM to generate the build image and as little as 1 CPU core + 2GB of RAM to host the generated output files.

## Install Node.js, npm, pnpm

### Node.js + npm

Install [`Node.js`](https://nodejs.org/en) (v18+) and [`npm`](https://www.npmjs.com) (v9+).

* [Node.js + npm installation guide](https://nodejs.org/en/download)

Verify Node.js and npm installation by running the following commands in your terminal:

```bash theme={null}
node -v
```

```bash theme={null}
npm -v
```

### pnpm

Install [`pnpm`](https://pnpm.io) (v6+).

* [pnpm installation guide](https://pnpm.io/installation)

Verify pnpm installation by running the following command in your terminal:

```bash theme={null}
pnpm -v
```

## Docker

Install [`Docker`](https://www.docker.com) (v20+).

* [Docker installation guide](https://docs.docker.com/engine/install)

Verify Docker installation by running the following command in your terminal:

```bash theme={null}
docker -v
```

It is recommended to use Compose V2. To switch to Compose V2, use the `docker compose` CLI plugin or activate the **Use Docker Compose V2** setting in Docker Desktop. For more information, see the [Evolution of Compose](https://docs.docker.com/compose/compose-v2).

## Git

Install [`Git`](https://git-scm.com) (v2+).

* [Git installation guide](https://git-scm.com/download)

Verify Git installation by running the following command in your terminal:

```bash theme={null}
git --version
```

## Email delivery (optional)

Hoppscotch comes with support for easy integrations with 3rd party SMTP providers. You will need emails so that you can invite your team to use Hoppscotch and for emails to work, you will need to set up proper SMTP configuration as described below.

To enable email delivery, you will need to generate a valid SMTP URL in the below format:

```
smtps://user@domain.com:pass@smtp.domain.com
```

For example, if you are using Gmail as your SMTP server your SMTP URL will look like something shown below:

```
smtps://user@gmail.com:pass@smtp.gmail.com
```

You can also use [mailcatcher](https://mailcatcher.me/) as a simple SMTP server.

### Custom SMTP configuration

For more advanced needs, such as production-level email delivery or gaining more control over your email configurations, you can set up a custom SMTP server.

To enable the custom mailer configuration, in addition to setting the `MAILER_USE_CUSTOM_CONFIGS` to `true`, you'll also need the following details in the specified format:

| Requirement   | Description                                  | Format                                 |
| ------------- | -------------------------------------------- | -------------------------------------- |
| SMTP Host     | Address of your SMTP server                  | `smtp.customdomain.com`                |
| SMTP Port     | Communication port used by your SMTP server  | `587` for **TLS** or `465` for **SSL** |
| SMTP User     | Username for your SMTP account               | `user@customdomain.com`                |
| SMTP Password | Corresponding password for your SMTP account | `custompass`                           |

You can use services like [SendGrid](https://sendgrid.com/), [Amazon SES](https://awss.amazon.com/ses/), or your own SMTP server to set up custom email delivery with Hoppscotch.

## Postgres database

Hoppscotch uses a Postgres database to store all the data. You can use any Postgres database provider of your choice - hosted locally or on a cloud provider. Make sure you have a valid Postgres database URL in the below format:

```
postgresql://username:password@url:5432/dbname
```

## OAuth

You also need to configure an OAuth provider to enable third-party authentication. Hoppscotch supports the following OAuth providers:

1. Email
2. GitHub
3. Google
4. Microsoft

### Choosing OAuth Providers

Hoppscotch allows you to choose which authentication providers to enable for your workspace during the onboarding flow in the admin dashboard. You can easily select from options like Google, GitHub, Microsoft, and Email directly through the setup interface.

```yaml theme={null}
VITE_ALLOWED_AUTH_PROVIDERS=GOOGLE,GITHUB,MICROSOFT,EMAIL
```

### Configuring third-party providers

To configure the third-party authentication, you will need to generate a valid OAuth client ID and client secret for the OAuth provider of your choice. You will also need to provide a valid callback URL for the OAuth provider.

For example, if you are using GitHub as your OAuth provider, you will need to generate a valid OAuth client ID and client secret for GitHub. You will also need to provide a valid callback URL for GitHub. The credentials for the GitHub OAuth provider can be entered during onboarding in the admin dashboard, and will look like the following:

```yaml theme={null}
GITHUB_CLIENT_ID=*****
GITHUB_CLIENT_SECRET=*****
GITHUB_CALLBACK_URL=http://localhost:3170/v1/auth/github/callback
GITHUB_SCOPE=user:email
```

The `CALLBACK_URL` variable is the URL that is invoked after the authorization is done and it follows the pattern `http://localhost:3170/v1/auth/[auth_provider_name]/callback`.

The `SCOPE` variable defines the scope of the data that the OAuth provider passes on to Hoppscotch.

The links to configure OAuth for various providers are given below:

1. [**GitHub**](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) (scope: email)
2. [**Google**](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid#get_your_google_api_client_id) (scope: email, profile)
3. [**Microsoft**](https://learn.microsoft.com/en-us/azure/active-directory/develop/scenario-web-app-sign-user-app-registration?tabs=nodejs#register-an-app-by-using-the-azure-portal) (scope: user with read permission)

<Note>It is recommended that you secure your deployments by issuing TLS certificates and using **HTTPS** since we use **secure HTTP cookies** for authenticating users.</Note>

## Support for standard `HTTP/s` ports

From the December 2023 release onwards containers now support ingress via standard HTTP/S ports on port `80` and `443` by default, moving forward it is recommended users switch to using these ports. We currently do still support the services being exposed from ports `3000`, `3100` and `3170` respectively but support for this will be dropped in the future and all containers will work over standard HTTP/s ports.


# Setup and access
Source: https://docs.hoppscotch.io/documentation/self-host/community-edition/setup-and-access

Learn how to set up and access Hoppscotch Community Edition.

After successfully running the necessary containers, the next step involves creating an administrator account to manage Hoppscotch.

<Warning>The system automatically designates the first user who logs in through the admin dashboard as the administrator.</Warning>

## Creating an administrator account

1. Open a new browser tab and visit [`http://localhost:3100`](http://localhost:3100).
2. This will grant you access to the admin dashboard.
3. Login using your credentials or create a new account.
4. The first user to log in will be given administrator privileges.

<Card title="Admin dashboard" icon="circle-arrow-right" href="/documentation/self-host/community-edition/admin-dashboard">
  Learn how to manage your Hoppscotch instance using the admin dashboard.
</Card>

## Accessing the Hoppscotch app

With the administrator account set up, you can now start using the Hoppscotch app for API testing and development.

1. Open a new browser tab and visit [`http://localhost:3000`](http://localhost:3000).
2. Begin testing and developing your APIs seamlessly with Hoppscotch.

<Tip>Hoppscotch Enterprise Edition is available for on-premise deployment with priority support. [Contact Hoppscotch Support](/support/getting-started/contact)</Tip>


# Telemetry
Source: https://docs.hoppscotch.io/documentation/self-host/community-edition/telemetry

Telemetry and data sharing in Hoppscotch Community Edition

Telemetry in Hoppscotch Self-Host refers to anonymous data shared with Hoppscotch. This helps identify the usage patterns of Hoppscotch.

# Data Collected by Hoppscotch

Hoppscotch does not capture any data from your APIs. All captured data is anonymous and pertains to instance usage.

## Instance Usage

The instance usage ping is sent once a week to indicate that the instance is operational. You can disable this event by navigating to the settings page and turning off data sharing settings.

```json theme={null}
{
  "uuid": "976fcae1-4079-4e83-881a-48723f694475",
  "event": "sh_instance",
  "properties": {
    "type": "COMMUNITY",
    "total_user_count": 10,
    "total_workspace_count": 2,
    "version": "2024.3.0",
    "$lib": "posthog-node",
    "$lib_version": "3.6.3",
    "$geoip_disable": true,
    "$ip": "127.0.0.1",
    "$sent_at": "2024-02-20T06:14:20.041000+00:00",
    "$plugins_succeeded": [
      "GeoIP (8000)"
    ],
    "$plugins_failed": [],
    "$plugins_deferred": []
  },
  "timestamp": "2024-02-20T06:14:20.591000Z",
  "team_id": 15871,
  "distinct_id": "9bdec3aae9330af51ba91313d3de99b46ae928da",
  "elements_chain": "",
  "created_at": "2024-02-20T06:14:20.835000Z"
}

```

# Turning off data sharing

You can turn off your data sharing preferences from your Hoppscotch admin dashboard and heading over to the Data Sharing section in the settings page


# Activity logs
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/activity-logs

Track all changes made to collections and requests within a workspace, and monitor user interactions through Activity Logs.

**Activity Logs** provide a clear record of actions performed within a workspace, including changes to collections, requests, and user interactions. These logs help maintain visibility and traceability of modifications across the workspace.

## Configuring Activity Logs

Activity Logs are controlled via a unified toggle in the Admin Dashboard.

1. Go to **Admin Dashboard → Logging Configurations.**
2. **Enable the toggle** in this section to start recording Activity Logs.

<Note> Activity Logs operate independently and do not require ClickHouse credentials. However, if Audit Logs are needed, [ClickHouse credentials must be configured](/documentation/self-host/enterprise-edition/prerequisites#clickhouse). </Note>

## Accessing Activity Logs

To access Activity Logs in a workspace:

1. Navigate to the specific workspace from the workspace switcher present in the top right corner of the app.
2. Locate and click on the **clock** icon in the right sidebar.
3. In the `History` tab, you will find a chronological timeline of all changes made to collections and requests.
4. Logs are ordered from the latest to the oldest for easier navigation, with entries grouped by date.

## Permissions

* **OWNER** and **EDITOR** roles: Actions performed by users with these roles are logged.
* **VIEWER** role: Viewers cannot make changes, but they can view the activity logs of changes made by others.

## **Logged Actions**

Activity Logs track the following actions within the workspace:

### **Workspace-Level Events**

| **Action**                          | **Logged Activity Example**                             |
| ----------------------------------- | ------------------------------------------------------- |
| Creating a new workspace            | `Created` new workspace `Statging`                      |
| Renaming a Workspace                | `Renamed` workspace from `Staging` to `Production`      |
| Adding a user to the workspace      | John Doe was `added` to the workspace as `Viewer`       |
| Updating a user's role in workspace | John Doe's role was `updated` from `Viewer` to `Editor` |
| Removing a user from the workspace  | John Doe was `removed` from the workspace               |

### **Collection-Level Events**

| **Action**                | **Logged Activity Example**                                      |
| ------------------------- | ---------------------------------------------------------------- |
| Creating a new collection | `Created` new collection `Authentication APIs`                   |
| Renaming a collection     | `Renamed` collection from `User Management` to `Role Management` |
| Importing a collection    | `Imported` collection `Payment Gateway APIs`                     |
| Duplicating a collection  | `Duplicated` collection `Microservices APIs`                     |
| Deleting a collection     | `Deleted` collection `Authentication APIs`                       |

### **Request-Level Events**

| **Action**             | **Logged Activity Example**             |
| ---------------------- | --------------------------------------- |
| Creating a new request | `Created` new request `Fetch User Data` |
| Deleting a request     | `Deleted` request `Fetch User Data`     |

<Note> Users with the **OWNER** role have the authority to `DELETE` activity logs. </Note>

## **Log Entry Details**

Each log entry provides detailed information about the recorded action, including:

* **Timestamp:** The exact time when the action occurred.
* **Action Summary:** A summary of changes made in the operation.
* **User Information:** The name of the user who performed the action.


# Admin dashboard
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/admin-dashboard

Get started with the Hoppscotch Admin Dashboard.

The Admin Dashboard serves as the central hub for managing your workspace and user-related activities. From here, you can efficiently oversee and control various aspects of your platform.

* Insights Dashboard: Gain valuable insights into platform usage.
* Manage Users: Handle user-related actions, such as inviting, elevating admins, and deleting users.
* Manage Workspaces: Create, edit, and delete workspaces while managing workspace-specific details and user memberships.

## Dashboard

The Dashboard section provides an overview of essential metrics and statistics regarding users, workspace, and activity. This snapshot allows you to track the usage and performance of your platform.

Get insights into your organization's usage of Hoppscotch.

* Number of Users: Monitor the count of registered users.
* Number of Workspaces: Keep track of the total number of workspaces.
* Number of Requests: Measure the volume of requests made by your organization.
* Number of Collections: Track the quantity of collections within the platform.

## Manage users

<Info>In Hoppscotch Enterprise Edition, a user needs to be explicitly invited by the admin to create an account on the platform.</Info>

The Users section empowers you to effectively control user-related actions. It streamlines the process of user management, making it simple to oversee the user base.

* User List: View a comprehensive list of all users and their activity on your platform
* Invite Users: Send invitations to new users, welcoming them to the platform.
* Admin Privileges: Elevate users to administrative roles for increased permissions.
* User Deletion: Delete users when necessary.

### Invite Users

Admins can easily bring new users to their Hoppscotch instance by sending them invitations. Depending on whether SMTP is configured, the process differs slightly. Here's how you can invite users:

#### With SMTP

When SMTP is enabled from the admin dashboard and the required SMTP configurations are correctly set, follow these steps to invite a new user:

1. Go to the **Users** section within the Admin Dashboard.
2. Select the **Invite User** button to open the invitation modal.
3. Input the email address of the user you want to invite and click **Add User** to send an invitation.
4. An email containing an invite link (`http://localhost:3000`) will be sent to the invitee. They can use this link to log in to Hoppscotch web app.
5. Alternatively, you can copy the invite link and share it through other platforms with the new user, but make sure the user signs in using the email address specified during the invitation process.

#### Without SMTP

If SMTP is disabled from the admin dashboard, the invitation process is slightly different:

1. Go to the **Users** section within the Admin Dashboard.
2. Select the **Invite User** button to open the invitation modal.
3. Input the email address of the user you want to invite and click **Add User**.
4. An invite link (`http://localhost:3000`) will be generated and displayed before you. Copy this link and share it with the user via your preferred communication channel. Make sure that the user signs in to Hoppscotch using the same email address you provided during the invitation.

### Pending Invites

Within the **Users** section, admins can view a list of all users who have been invited but have not yet joined the organization. To access this list, simply click on the **Pending Invites** button next to "Invite User". Here, you'll see all the invitations you've sent, along with details such as:

* **Invitee Email:** The email address to which the invite was sent.
* **Invited By:** The email address of the user who sent the invitation
* **Invited on:** The date and time when the invitation was sent.

**You can also consider the following actions:**

* **Copy Invite Link:** If you need to resend the invitation, you can easily `copy` the invite link and share it with the user via any communication platform.
* **Revoke Invitation:** If you wish to cancel an invitation, simply click the `Revoke Invitation` button next to the specific user invite in the **Action** column. This will remove the pending invite from the list and prevent the user from accessing your Hoppscotch instance using that link.

## Manage Workspaces

In the Manage Workspace section, you can efficiently handle workspace-related operations, ensuring that collaborations and projects run smoothly.

* Workspace Creation: Establish new workspaces tailored to specific projects or departments.
* Workspace Editing: Modify workspace details and configurations as needed.
* Workspace Deletion: Disband workspaces that are no longer relevant.
* User Memberships: View and manage the users associated with each workspace.

## Infra-tokens

InfraTokens are special UUID tokens that provide a secure way for admins to interface with Self-Hosted APIs. They are exclusively accessible to admins, ensuring that only authorized personnel can manage sensitive operations. Unlike Personal Access Tokens, which are tied to individual users, InfraTokens are scoped at the instance level, granting access to all admins within the instance.

#### Generate an InfraToken

Follow these steps to create a new InfraToken:

1. After logging into your Self-Hosted instance using your admin credentials, you can access the **“Infra Tokens”** under the “Settings” section from your admin dashboard.
2. Click on **"Generate new token."**
3. Enter a title for the token and select an expiration date. Available options include 7 days, 30 days, 60 days, 90 days, or no expiry.
4. After providing the necessary details, confirm the creation. **The new InfraToken will be displayed once, make sure to copy it securely** to your clipboard for immediate use.
5. If you decide that you no longer need the token, you can delete it by navigating back to **“Infra Tokens"** section.

<Note> The details of the admin who created the InfraToken are stored for audit purposes. All admins can view and manage these tokens. </Note>

#### How to use InfraTokens

InfraTokens are to be used as **Bearer tokens**. When making requests to the User Management APIs, include the `InfraToken` in the `Authorization` header as follows:

```bash theme={null}
Bearer <Your_InfraToken>
```

#### APIs for User Management

The RESTful APIs designed for User Management enable admins to perform a wide range of user-related actions, such as inviting new users, deleting existing ones, and updating user details. These APIs provide admins with the ability to efficiently manage user accounts and permissions. The table below introduces nine key APIs that give admins greater control over user management.

| User Activity                          | Description                                                                                                | Method | Endpoint                                       |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------ | ---------------------------------------------- |
| Invite a New User                      | Allows admins to invite a new user to the instance.                                                        | POST   | `<base-url>/v1/infra/user-invitations`         |
| View Pending Invites                   | Retrieves a list of all pending invites sent to new users.                                                 | GET    | `<base-url>/v1/infra/user-invitations`         |
| Delete Pending Invites                 | Enables admins to delete specific pending invites using their Email ID.                                    | DELETE | `<base-url>/v1/infra/user-invitations`         |
| View All Users                         | Provides a list of all users in the instance.                                                              | GET    | `<base-url>/v1/infra/users`                    |
| View a Particular User                 | Fetches details of a specific user in the instance by their User ID.                                       | GET    | `<base-url>/v1/infra/users/{uid}`              |
| Delete an existing User                | Enables admins to delete an existing user from the instance by their User ID.                              | DELETE | `<base-url>/v1/infra/users/{uid}`              |
| Update User Details                    | Allows admins to update the details of an existing user.                                                   | PATCH  | `<base-url>/v1/infra/users/{uid}`              |
| Manage Admin Status                    | Enables admins to add or remove admin status for an existing user.                                         | PATCH  | `<base-url>/v1/infra/users/{uid}/admin-status` |
| Fetch User's involvement in Workspaces | Retrieves workspace details that a user is part of, including their role.                                  | GET    | `<base-url>/v1/infra/users/{uid}/workspaces`   |
| Deactivate User Account                | Allows admins to deactivate a user account, preventing them from accessing the instance until reactivated. | POST   | `<base-url>/v1/infra/users/{uid}/deactivate`   |
| Reactivate User Account                | Allows admins to activate a user account that was previously deactivated.                                  | POST   | `<base-url>/v1/infra/users/{uid}/reactivate`   |

<Info> To interact with the **User Management APIs**, ensure that your backend service is running, either on your local machine or on a server. The API documentation is accessible at the `/api-docs` endpoint relative to your backend service URL. For example, if your backend is running locally, you can access the API docs at [http://localhost:3170/api-docs](http://localhost:3170/api-docs). You can also retrieve the OpenAPI v3 JSON format at [http://localhost:3170/api-docs-json](http://localhost:3170/api-docs-json). </Info>

#### APIs for Workspace Management

We've introduced new **APIs** to make **workspace management** and **collaboration** easier for **admins**. These APIs enable quick actions like creating new workspaces, updating existing workspace details, and deleting workspaces as needed. Check out the table below for **fourteen** APIs that give admins a greater control over managing Hoppscotch workspaces.

| **Workspace Activity**                    | **Description**                                                                         | **Method** | **Endpoint**                                                       |
| ----------------------------------------- | --------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------------ |
| Create a Workspace                        | Create a new workspace within the instance.                                             | POST       | `<base-url>/v1/infra/workspaces`                                   |
| View All Workspaces                       | Retrieves a list of all workspaces available.                                           | GET        | `<base-url>/v1/infra/workspaces`                                   |
| View Workspace Details                    | List details about a specific workspace like name, members, roles, and pending invites. | GET        | `<base-url>/v1/infra/workspaces/{id}`                              |
| Delete a workspace                        | Remove an existing workspace using its ID.                                              | DELETE     | `<base-url>/v1/infra/workspaces/{id}`                              |
| Update details for an existing workspace. | Modify settings and preferences for an existing workspace.                              | PATCH      | `<base-url>/v1/infra/workspaces/{id}`                              |
| List Members of a Workspace               | Retrieves a list of all members in a specific workspace.                                | GET        | `<base-url>/v1/infra/workspaces/{id}/ members`                     |
| Get Workspace Owners count                | Fetches number of Workspace members with "OWNER" permissions                            | GET        | `<base-url>/v1/infra/workspaces/{id}/ owners-count`                |
| Get Workspace Editors count               | Fetches number of Workspace members with "EDITOR" permissions                           | GET        | `<base-url>/v1/infra/workspaces/{id}/ editors-count`               |
| Get Workspace Viewers count               | Fetches number of Workspace members with "VIEWER" permissions                           | GET        | `<base-url>/v1/infra/workspaces/{id}/ viewers-count`               |
| Add User to a workspace                   | Add a user and assign roles (Owner, Editor, and Viewer) in a workspace.                 | POST       | `<base-url>/v1/infra/workspaces/{id}/ user`                        |
| Change User roles in a workspace          | Update the role (Owner, Editor, and Viewer) of a user within a workspace                | PATCH      | `<base-url>/v1/infra/workspaces/{id}/ user/{uid}/role`             |
| Remove User from a workspace              | Remove a user from a workspace using their ID                                           | DELETE     | `<base-url>/v1/infra/workspaces/{id}/ user/{uid}`                  |
| View all pending workspace invites.       | List all pending invites for workspace access.                                          | GET        | `<base-url>/v1/infra/workspaces/{id}/ invitations`                 |
| Delete pending workspace invites.         | Revoke Workspace invitations using invitation IDs.                                      | DELETE     | `<base-url>/v1/infra/workspaces/{id}/ invitations/{invitation_id}` |

<Info> To interact with the **Workspace Management APIs**, ensure that your backend service is running, either on your local machine or on a server. The API documentation is accessible at the `/api-docs` endpoint relative to your backend service URL. For example, if your backend is running locally, you can access the API docs at [http://localhost:3170/api-docs](http://localhost:3170/api-docs). You can also retrieve the OpenAPI v3 JSON format at [http://localhost:3170/api-docs-json](http://localhost:3170/api-docs-json). </Info>

## Server Settings

In the **Server Settings** section, you have the ability to both view and edit the environment variables that were configured during the setup of your self-hosted instance.

### Configurations

1. **Access Control Settings:** Manage and restrict user access to ensure only authorized users can interact with your Hoppscotch instance.

   * **Site Protection:**
     When site protection is activated, all visitors to your Hoppscotch instance will be prompted to create an account and log in to use Hoppscotch. Site protection is enabled by default on Hoppscotch Enterprise and can be disabled as needed.

   * **Domain Whitelisting:**
     Domain Whitelisting enables organization admins to grant access to users with email addresses under the organization's domain without explicit approval.

   To enable domain whitelisting, activate the "Enable Whitelisted Domains" option and simply add the domains used by your organization for email addresses.

2. **Configure Authentication Providers:**
   Customize authentication providers, including Google, Microsoft, GitHub, and email, directly from the settings page.

3. **Configure SMTP Settings:**
   Configure your SMTP settings for seamless email integration.

4. **Configure SAML Settings:**
   Configure your SAML settings for your SAML based Single sign on.

5. **Configure OIDC Settings:**
   Configure your OIDC Settings for Single Sign-On based authentication.

6. **User Provisioning:**
   Enable SCIM provisioning to manage user creation, updates, and deprovisioning directly from your Identity Provider (IdP). [Learn how to set up SCIM provisioning in Hoppscotch and Okta](/documentation/self-host/enterprise-edition/user-provisioning).

7. **Configure Logging Settings:**
   Manage activity and audit logging configurations for your Hoppscotch instance. Enable or disable logs through a unified setting, configure ClickHouse credentials, and download audit logs in CSV format.

8. **History Configurations:**
   Control the logging of request history for all users with a simple toggle option.

   * **When enabled:**
     Request history is visible in the Hoppscotch app, and new entries are actively logged and stored in the database.

   * **When disabled:**
     Request history is hidden from the Hoppscotch app, and no new request logs are written to the database.

   You can also optionally choose to purge all existing history from the database, ensuring complete removal of previously logged request data.

9. **Data sharing:**
   Enable or disable anonymous data sharing to help improve Hoppscotch. [Learn more about the metrics collected](./telemetry).

10. **Reset Configurations:**
    If needed, reset your configurations back to their original state.

### Custom Banner

**Custom banners** allow self-host admin to share important announcements such as a scheduled maintenance or instance upgrade with the rest of your team.

* **Create Announcements:** Navigate to the `Banners` tab and toggle the **"Show Banner"** action. Select the **type of banner** (Information, Warning, or Danger), craft and preview the **message** content, and `save` it to activate announcement immediately.

* **Edit Announcements:** You can modify the announcements directly by editing the message or changing the banner type and further saving the changes to implement them.

* **Delete Announcements:** Manually end an announcement by toggling the **"Show Banner"** action **OFF**.

### License Settings

The **License Settings** enable you to both configure and view your enterprise license information.

You have the following options:

* **Edit and Configure License Key:**
  You can modify and configure your license key as needed.

* **View License Status:**
  Obtain insights into the current status of your license. This includes details such as License Status, Issued to, Number of seats purchased, and expiry date.

## Hard Reset Configurations

If you need to perform a hard reset of the server configurations, execute the following command in your terminal to reset all your environment variables:

```bash theme={null}
docker exec -it <db_container_id> psql -d hoppscotch -c "TRUNCATE \"InfraConfig\";"
```

You can replace `<db_container_id>` with the actual ID of your Docker container.


# Deploy and upgrade
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/deploy-and-upgrade

Deploy and upgrade Hoppscotch Enterprise Edition on your infrastructure.

This section contains instructions for deploying and upgrading Hoppscotch Enterprise Edition.

## Deploy

Deploy Hoppscotch Enterprise Edition on your infrastructure.

* Instructions for deploying Hoppscotch on your infrastructure are coming soon.

## Upgrade

Upgrading Hoppscotch Enterprise Edition is a simple process. Follow the instructions below to upgrade your Hoppscotch Enterprise Edition instance.

### Using individual containers for the services

1. Check if there is a new version available by running the following command:

   ```bash theme={null}
   docker images
   ```

2. Update the image to the latest version by running the following command:

   ```bash theme={null}
   docker pull hoppscotch/hoppscotch-enterprise-frontend:latest
   docker pull hoppscotch/hoppscotch-enterprise-backend:latest
   docker pull hoppscotch/hoppscotch-enterprise-admin:latest
   ```

   <Tip>If you want to update to a specific version, run the following command:</Tip>

   ```bash theme={null}
   docker pull hoppscotch/hoppscotch-enterprise-frontend:<version>
   docker pull hoppscotch/hoppscotch-enterprise-backend:<version>
   docker pull hoppscotch/hoppscotch-enterprise-admin:<version>
   ```

3. Start the new container by following the instructions in the [Install and build](/documentation/self-host/enterprise-edition/install-and-build#docker) section.

<Info>For minor version upgrades, you might not need to run the database migrations. However, for major version upgrades, you will need to run the database migrations. Refer to the [Database migrations](/documentation/self-host/enterprise-edition/install-and-build#migrations) section for more information.</Info>

### Using the AIO container

1. Check if there is a new version available by running the following command:

   ```bash theme={null}
   docker images
   ```

2. Update the image to the latest version by running the following command:

   ```bash theme={null}
   docker pull hoppscotch/hoppscotch-enterprise:latest
   ```

   <Tip>If you want to update to a specific version, run the following command:</Tip>

   ```bash theme={null}
   docker pull hoppscotch/hoppscotch-enterprise:<version>
   ```

3. Start the new container by following the instructions in the [Install and build](/documentation/self-host/enterprise-edition/install-and-build#docker) section.

<Info>For minor version upgrades, you might not need to run the database migrations. However, for major version upgrades, you will need to run the database migrations. Refer to the [Database migrations](/documentation/self-host/enterprise-edition/install-and-build#migrations) section for more information.</Info>


# Getting started
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/getting-started

Learn how to get started with Hoppscotch Enterprise Edition.

Enterprise Edition builds on top of the Community Edition foundation by adding powerful features designed for larger organizations that require robust security measures like SAML-based SSO, OIDC, audit logs, and on-premise deployment options. It also comes with dedicated support to help adapt Hoppscotch to your company's specific needs. The self-hosted enterprise version is open-core in nature, meaning it is accompanied by a set of advanced features that are only available through a commercial license.

<CardGroup>
  <Card title="Prerequisites" icon="circle-arrow-right" href="/documentation/self-host/enterprise-edition/prerequisites">
    Prerequisites to self-host Hoppscotch Enterprise Edition on your infrastructure.
  </Card>

  <Card title="Install and build" icon="circle-arrow-right" href="/documentation/self-host/enterprise-edition/install-and-build">
    Install and build Hoppscotch Enterprise Edition on your infrastructure.
  </Card>

  <Card title="Admin dashboard" icon="circle-arrow-right" href="/documentation/self-host/enterprise-edition/admin-dashboard">
    Manage your Hoppscotch Enterprise Edition instance with the Admin dashboard.
  </Card>
</CardGroup>


# Install and build
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/install-and-build

Learn how to install and build Hoppscotch Enterprise Edition.

<Tip>If you're interested in deploying <ins>Hoppscotch on Kubernetes</ins>, you can conveniently skip this guide and proceed directly to the [Helm chart deployment guide](/documentation/self-host/helm-chart-deployment/getting-started).</Tip>

## Configuring the environment

Before you get started with the installation, you need to configure the environment variables. Create a `.env` file in the root directory of the project and add the following environment variables:

<Warning>**<u>Ensure that the environment values are not enclosed within quotes \[""].</u>**</Warning>
<Note>To enable desktop app support for self-hosted instances, make sure you've enabled [subpath based access](#subpath-based-access).</Note>

```yaml theme={null}
#-----------------------Backend Config------------------------------#

# Enterprise License Key
# Get your license key from https://enterprise.hoppscotch.com
ENTERPRISE_LICENSE_KEY=***************************************

# (Optional) By default, the AIO container (when in subpath access mode) exposes the endpoint on port 80. Use this setting to specify a different port if needed.
HOPP_AIO_ALTERNATE_PORT=80

# Prisma Config
DATABASE_URL=postgresql://username:password@url:5432/dbname # or replace with your database URL

# Enable/Disable Horizontal Scaling
# Set to 'true' to enable horizontal scaling across multiple backend instances
# When enabled, Redis is required for session management and data synchronization
HORIZONTAL_SCALING=false

# Redis Config
# Note: Configure Redis only if HORIZONTAL_SCALING is set to true
REDIS_URL=redis://username:password@host:6379/0

# Sensitive Data Encryption Key while storing in Database (32 character)
DATA_ENCRYPTION_KEY=********************************

# Whitelisted origins for the Hoppscotch App.
# This list controls which origins can interact with the app through cross-origin comms.
# - localhost ports (3170, 3000, 3100): app, backend, development servers and services
# - app://localhost_3200: Bundle server origin identifier
#   NOTE: `3200` here refers to the bundle server (port 3200) that provides the bundles,
#   NOT where the app runs. The app itself uses the `app://` protocol with dynamic
#   bundle names like `app://{bundle-name}/`
WHITELISTED_ORIGINS=http://localhost:3170,http://localhost:3000,http://localhost:3100,app://localhost_3200,app://hoppscotch

#-----------------------Frontend Config------------------------------#

# Base URLs
VITE_BASE_URL=http://localhost:3000
VITE_SHORTCODE_BASE_URL=http://localhost:3000
VITE_ADMIN_URL=http://localhost:3100

# Backend URLs
VITE_BACKEND_GQL_URL=http://localhost:3170/graphql
VITE_BACKEND_WS_URL=wss://localhost:3170/graphql
VITE_BACKEND_API_URL=http://localhost:3170/v1

# Terms Of Service And Privacy Policy Links (Optional)
VITE_APP_TOS_LINK=https://docs.hoppscotch.io/support/terms
VITE_APP_PRIVACY_POLICY_LINK=https://docs.hoppscotch.io/support/privacy

# Set to `true` for subpath based access
ENABLE_SUBPATH_BASED_ACCESS=false

# Optional: Local Proxy Server Config
# Enables a local proxy server for routing API requests.
# This will only work if ENABLE_SUBPATH_BASED_ACCESS is set to `true`.
LOCAL_PROXY_SERVER_ENABLE=false

# Optional: Route all API requests via a proxy server for added security.
# Set your proxy server URL here, or remove this variable to send requests directly.
PROXY_APP_URL=https://proxy.hoppscotch.io
```

Let's understand the major environment variables:

1. `ENTERPRISE_LICENSE_KEY`: The license key required to use Hoppscotch Enterprise.
2. `DATABASE_URL`: This is where you add your Postgres database URL.
3. `HOPP_AIO_ALTERNATE_PORT`: This is an optional variable that lets you specify an alternate port for the AIO container's endpoint when operating in subpath access mode. By default, this endpoint is exposed on port 80.
4. `HORIZONTAL_SCALING`: Set to true to enable horizontal scaling, which uses Redis for managing pub-sub and state across instances.
5. `DATA_ENCRYPTION_KEY`: A 32-character key used for encrypting sensitive data stored in the database.
6. `WHITELISTED_ORIGINS`: URLs of Hoppscotch backend, admin dashboard, frontend app and the bundle server that are allowed to interact with the desktop app.
7. `VITE_BASE_URL`: This is the URL where your deployment will be accessible from.
8. `VITE_SHORTCODE_BASE_URL`: A URL to generate shortcodes for sharing, can be the same as `VITE_BASE_URL`.
9. `VITE_BACKEND_GQL_URL`: The URL for GraphQL within the instance.
10. `VITE_BACKEND_WS_URL`: The URL for WebSockets within the instance.
11. `VITE_BACKEND_API_URL`: The URL for REST APIs within the instance.
12. `VITE_APP_TOS_LINK` and `VITE_APP_PRIVACY_POLICY_LINK` are optional and are used to configure the links to the Terms & Conditions and Privacy Policy.

Third-party auth configs have to be obtained from the respective providers. You can choose and configure the auth providers by following the [configuring OAuth guide](/documentation/self-host/enterprise-edition/prerequisites#oauth).

## Docker

Once the environment variables are configured, you may proceed to the next step of setting up the Hoppscotch instance. Currently, there are two ways to set up Hoppscotch:

* Using individual containers for the services

* Using the AIO container

* Before proceeding further, ensure that you have a running instance of Postgres.

### Using individual containers for the services

To self-host Hoppscotch Enterprise Edition, you will need the following services running via Docker:

* Hoppscotch enterprise frontend
* Hoppscotch enterprise backend
* Hoppscotch enterprise admin dashboard

Pull the containers from DockerHub with the following command:

```bash theme={null}
docker pull hoppscotch/hoppscotch-enterprise-frontend
docker pull hoppscotch/hoppscotch-enterprise-backend
docker pull hoppscotch/hoppscotch-enterprise-admin
```

After pulling the containers, start Hoppscotch by running all three services:

```bash theme={null}
docker run -p 3000:3000 --env-file .env --restart unless-stopped hoppscotch/hoppscotch-enterprise-frontend
docker run -p 3170:3170 --env-file .env --restart unless-stopped hoppscotch/hoppscotch-enterprise-backend
docker run -p 3100:3100 --env-file .env --restart unless-stopped hoppscotch/hoppscotch-enterprise-admin
```

<Tip>Ensure that the environment variables are configured in the `.env` file and the restart policy is mentioned.</Tip>

<Note>
  To enable desktop app support for your self-hosted Hoppscotch instance, make sure you expose the web app server which is a part of the frontend container. You can do this by running the following command:

  ```bash theme={null}
  docker run -p 3000:3000 -p 3200:3200 --env-file .env --restart unless-stopped hoppscotch/hoppscotch-frontend
  ```
</Note>

Open [admin dashboard](http://localhost:3100) or [`PORT 3100`](http://localhost:3100) in the browser to [setup and access](/documentation/self-host/enterprise-edition/setup-and-access) the Hoppscotch instance.

### Using the AIO container

The All-In-One (AIO) container is a single container that provides all the services required to run Hoppscotch.

Pull the container from DockerHub with the following command:

```bash theme={null}
docker pull hoppscotch/hoppscotch-enterprise
```

After pulling the container, start Hoppscotch by running the container:

```bash theme={null}
docker run -p 3000:3000 -p 3100:3100 -p 3170:3170 --env-file .env --restart unless-stopped hoppscotch/hoppscotch-enterprise
```

<Tip>Ensure that the environment variables are configured in the `.env` file and the restart policy is mentioned.</Tip>

Open [admin dashboard](http://localhost:3100) or [`PORT 3100`](http://localhost:3100) in the browser to [setup and access](/documentation/self-host/community-edition/setup-and-access) the Hoppscotch instance.

## Subpath Based Access

To enable subpath based access the following `.env` variable must be set to true, it is set to false by default.

```
ENABLE_SUBPATH_BASED_ACCESS=true
```

<Note>To enable desktop app support for your self-hosted Hoppscotch instance, make sure to set `ENABLE_SUBPATH_BASED_ACCESS` to `true` in your `.env` file.</Note>

When set to true the following is the expected behavior:

### Using individual containers for the services

When using the individual containers it is up to the users to configure a reverse proxy to allow requests made to a specific route to be rerouted to the relevant containers.

### Using the AIO container

When using AIO, when subpath access is set to true the services can be accessed from the following routes

| Service              | Route      |
| -------------------- | ---------- |
| Hoppscotch App       | `/`        |
| Hoppscotch Admin App | `/admin`   |
| Hoppscotch Backend   | `/backend` |

<Warning>
  By default, the AIO container exposes the app on port 80. This can cause conflicts if you're running on a host system where
  port 80 is privileged, such as with Rootless Docker, Podman, or hardened environments like OpenShift. If you experience issues on these setups, try setting `HOPP_AIO_ALTERNATE_PORT` to bind the app to a non-privileged port.
</Warning>

## Migrations

Once the instance of Hoppscotch is up, you need to run migrations on the database to ensure that it has the relevant tables. Depending on how Hoppscotch was set up, the method to run the migrations changes.

### Using individual containers for the services

Run the following command to copy the ID of the **backend container**:

```bash theme={null}
docker ps
```

### Using the AIO container

Run the following command to copy the ID of the **AIO container**:

```bash theme={null}
docker ps
```

### Running migrations

Once the respective container ID is copied, execute the following command to open an interactive shell within the AIO container to execute the migration command:

```bash theme={null}
docker exec -it <container_id> /bin/sh
```

Once inside the container, run the migration using:

```bash theme={null}
pnpm exec prisma migrate deploy
```

Should the user ever encounter the following error:

```bash theme={null}
Database migration not found. Please check the documentation for assistance: https://docs.hoppscotch.io/documentation/self-host/community-edition/install-and-build#running-migrations
```

It means the user is trying to start the backend (or AIO) service before the database has all the relevant tables in it. In order to run the migration to populate the database run the following command.

```bash theme={null}
docker run -it --entrypoint sh --env-file .env <container_name>
```

Making sure to pass in the `.env` file containing the right `.env` variables for the instance. On executing the aforementioned command will result in a shell being opened inside a instance of the container following which user can execute a database migration normally with

```bash theme={null}
pnpm exec prisma migrate deploy
```

Once the database has been successfully run and the database populated with tables the backend containers ( or AIO container) can be started normally.

Note: If user is using `docker compose` to run the services the following command can be used to open a shell inside the backend (or AIO) service.

```bash theme={null}
docker compose run --entrypoint sh <Service_name>
```

## ClickHouse setup

To start saving the [audit logs](/guides/articles/audit-logs) into ClickHouse, first you need to create the relevant databases with the relevant tables in them. Follow the following instructions to set up ClickHouse to start saving logs:

1. Ensure that all the relevant containers are running.

2. Run the following command to get the ID of the ClickHouse container:

   ```bash theme={null}
   docker ps
   ```

3. Once the ClickHouse container is also running, open an interactive bash into it using the `clickhouse-client`:

   ```bash theme={null}
   docker exec -it <clickhouse_container_id> clickhouse-client
   ```

4. Once inside the container, execute the following SQL commands:

   ```sql theme={null}
   # Create a database called logs
   CREATE DATABASE logs

   # Create a table called audit_logs in the logs database
   CREATE TABLE IF NOT EXISTS logs.audit_logs
   (
       `event` String,
       `timestamp` DateTime,
       `user` Tuple(id String, email String, name String),
       `group` Tuple(type LowCardinality(String), id String),
       `resource` Tuple(type LowCardinality(String), metadata String),
       `statusCode` Int16,
       `errorMessage` String,
       `result` LowCardinality(String),
       `server_version` String
   )
   ENGINE = MergeTree
   ORDER BY timestamp
   ```

## SAML Configuration

When you use SAML authentication, by default Hoppscotch only pulls the email of the user as the platform uses it as the unique identifier to verify the user.
Starting from `v2024.9.2` onwards, Hoppscotch Enterprise Edition instances support pulling the following attributes from the SAML response to fill in additional user details:

* `displayName`: The name of the user which is displayed within the Hoppscotch platform.
* `photoURL`: The URL where to find the user's profile picture. **Do not** set this attribute if a profile picture doesn't exist.
* `isAdmin` (optional): A boolean attribute (true or false) that automatically assigns the Admin role to users who belong to a designated group in the configured Identity Provider (e.g., Okta).

<Note> The `isAdmin` attribute is evaluated only during the user's first login or signup. Subsequent logins or signups will not re-evaluate this flag. </Note>

| Name        | Name Format | Value                                                       |
| ----------- | ----------- | ----------------------------------------------------------- |
| displayName | Basic       | user.displayName                                            |
| photoURL    | Basic       | user.profileURL                                             |
| isAdmin     | Basic       | isMemberOfGroupName("Hoppscotch Admins") ? "true" : "false" |

You have to configure your **SAML IdP (Identity Provider)** to include these attributes *exactly* in the response. For example, for Okta, you can follow [this guide](https://support.okta.com/help/s/article/How-to-define-and-configure-a-custom-SAML-attribute-statement?language=en_US) to configure the attributes.


# Observability
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/observability

Monitor and improve your Hoppscotch instance with OpenTelemetry integration.

Observability support helps you understand what's happening inside your self-hosted Hoppscotch instance. With OpenTelemetry integration, you can track performance, diagnose issues faster, and gain insights into how your APIs are being used.

This feature provides real-time visibility into your application's health, making it easier to maintain a reliable service for your team.

## What is Observability?

Observability gives you the ability to understand your system's internal state by analyzing the data it produces. Instead of guessing why something went wrong, you can see exactly what happened and when.

With Hoppscotch's observability integration, you get access to:

* **Traces**: Follow the complete journey of each API request through your system
* **Metrics**: Monitor performance indicators like response times and request volumes
* **Logs**: Access detailed records of events with full context

## Why Use Observability?

Implementing observability in your Hoppscotch instance helps you:

* **Spot Issues Quickly**: Identify performance bottlenecks and errors as they happen
* **Reduce Downtime**: Cut the time it takes to find and fix problems
* **Understand Usage**: See how your team uses the platform and which APIs are most active
* **Improve Performance**: Make data-driven decisions about optimizing your instance
* **Debug with Confidence**: Get complete context when investigating issues

## How It Works

Hoppscotch uses OpenTelemetry, an industry-standard framework for collecting observability data. OpenTelemetry is vendor-neutral, meaning you can use it with your preferred monitoring tools.

Here's how the data flows:

1. **Your Hoppscotch instance** generates observability data as users make API requests
2. **OpenTelemetry Collector** receives and processes this data
3. **Storage backends** like Jaeger (traces) and Prometheus (metrics) store the data
4. **Visualization tools** like Grafana display dashboards and insights

This setup gives you complete visibility without vendor lock-in.

## Key Features

### Distributed Tracing

Track every API request from start to finish, even as it moves through different parts of your system. See exactly how long each step takes and where delays occur.

* View the complete path of every request
* Identify slow database queries or external API calls
* Understand dependencies between different services

### Real-Time Metrics

Monitor your instance's health with up-to-the-minute performance data:

* Request rates and response times
* Error rates and success percentages
* System resource usage (CPU, memory)
* Database performance indicators
* Custom business metrics that matter to your team

### Contextual Logging

Access detailed logs that include trace IDs, making it easy to find all related information when investigating an issue:

* Searchable structured logs
* Automatic correlation with traces and metrics
* Configurable log levels for different environments
* Long-term retention for compliance and analysis

### Intelligent Alerting

Set up alerts to notify you when something needs attention:

* Define thresholds for key metrics
* Receive notifications through your preferred channels
* Create custom alert rules based on your needs
* Prevent alert fatigue with smart grouping

## Getting Started

### Prerequisites

Before enabling observability, make sure you have:

* Hoppscotch Enterprise Edition deployed
* Admin access to your instance
* Basic familiarity with Docker or Kubernetes (depending on your deployment)

### Setup Options

You can deploy the observability stack in two ways:

#### Option 1: Docker Deployment

Best for smaller instances or teams getting started. This approach is quick to set up and works well for most use cases.

* Simple configuration
* Fast deployment
* Lower resource requirements
* Ideal for single-server setups

<Tip>Check out our detailed guide: [Set Up OpenTelemetry Stack with Docker](/guides/articles/set-up-opentelemetry-stack-with-docker)</Tip>

#### Option 2: Kubernetes Deployment

Recommended for larger organizations with high-traffic instances requiring high availability and automatic scaling.

* Automatic scaling based on load
* High availability and fault tolerance
* Advanced monitoring capabilities
* Better suited for production environments

### Configuration Steps

1. **Deploy the OpenTelemetry Collector**

   Set up the Collector to receive data from your Hoppscotch instance. You can use our example configuration or customize it for your needs.

2. **Connect Storage Backends**

   Choose where to store your observability data:

   * Jaeger for distributed traces
   * Prometheus for metrics
   * Your preferred log management solution

3. **Configure Hoppscotch**

   From the Admin Dashboard, navigate to the Observability settings and enter your Collector endpoint details.

4. **Set Up Visualization**

   Deploy Grafana or your preferred tool to create dashboards and visualize your data.

## Understanding Your Data

### Traces

Traces show you the complete story of each request:

* **Request Entry**: When the request arrived at Hoppscotch
* **Processing Steps**: Each operation performed (authentication, validation, etc.)
* **External Calls**: Requests to databases or other APIs
* **Response**: When and how the request completed

Each step includes timing information, making it easy to spot slow operations.

### Metrics

Metrics give you quantitative insights:

* **HTTP Metrics**: Request counts, status codes, response times
* **System Metrics**: CPU usage, memory consumption, disk I/O
* **Database Metrics**: Query performance, connection pool status
* **Business Metrics**: Active users, API calls per workspace, collection sizes

### Correlation

All observability data is linked together. When you're investigating an issue, you can:

* Start with a metric spike and drill down to individual traces
* Click on a trace to see all related logs
* Follow connections between different services

## Best Practices

### Start Simple

Don't try to monitor everything at once. Begin with:

1. HTTP request metrics
2. Error tracking
3. Basic system health indicators

Add more advanced monitoring as you become comfortable with the basics.

### Set Meaningful Thresholds

Create alerts based on what matters to your team:

* Response times exceeding your SLA
* Error rates above acceptable levels
* Resource utilization that could impact performance

### Regular Review

Schedule time to review your observability data:

* Weekly: Check for trends in usage and performance
* Monthly: Review and adjust alert thresholds
* Quarterly: Assess what metrics are most valuable

### Optimize Performance

Observability itself uses resources. Balance insight with overhead:

* Use sampling for high-volume traces
* Set appropriate retention periods
* Monitor the monitoring infrastructure

## Privacy and Security

Your observability data may contain sensitive information. Hoppscotch automatically:

* Sanitizes authentication tokens and credentials
* Encrypts data in transit
* Supports access controls for observability tools
* Maintains audit trails of who accessed what data

You can further customize what data is collected and retained based on your privacy requirements.

## Performance Impact

The observability features are designed to have minimal impact on your instance:

* Less than 5% increase in request latency
* Approximately 3% additional CPU usage
* Around 50MB extra memory per service

These overheads are typically insignificant compared to the benefits of having comprehensive monitoring.

## Data Retention

Configure how long to keep observability data:

* **Traces**: Typically 7-30 days (detailed request information)
* **Metrics**: Usually 30-90 days (aggregated performance data)
* **Logs**: 30-90 days or longer for compliance needs

Adjust these based on your storage capacity and regulatory requirements.

## Troubleshooting

### Data Not Appearing

If you don't see data in your observability tools:

1. Verify the Collector is running and accessible
2. Check the endpoint configuration in Admin Dashboard
3. Review Collector logs for connection errors
4. Ensure firewall rules allow traffic between components

### High Resource Usage

If the observability stack is using too many resources:

1. Reduce trace sampling rate
2. Adjust batch sizes in the Collector configuration
3. Consider deploying the Collector on dedicated infrastructure
4. Review and optimize retention policies

### Missing Traces

If some traces are incomplete:

1. Verify all services are configured correctly
2. Check for network issues between components
3. Review sampling configuration
4. Ensure trace context is properly propagated

## Getting Help

If you need assistance with observability:

* Review the [OpenTelemetry Stack Setup Guide](/guides/articles/set-up-opentelemetry-stack-with-docker)
* Contact Hoppscotch Enterprise Support for dedicated help
* Join our community forums to discuss with other users

<Info>Observability is available exclusively in Hoppscotch Enterprise Edition. [Learn more about Enterprise Edition](/documentation/self-host/enterprise-edition/getting-started) or [contact us](/support/getting-started/contact) for a demo.</Info>

## Next Steps

Now that you understand observability, you can:

* Set up the OpenTelemetry stack for your instance
* Create custom dashboards for your team's needs
* Configure alerts for critical metrics
* Explore advanced features like performance profiling

Monitor your instance effectively and maintain a reliable, high-performance API development platform for your organization.


# Prerequisites
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/prerequisites

Prerequisites for installing Hoppscotch on your own infrastructure.

Hoppscotch is a self-hosted API development platform, packaged as a set of Docker containers. You can install and run Hoppscotch on any operating system that can run a [Docker Engine](https://docs.docker.com/engine). You can use Hoppscotch on your local machine or a cloud provider of your choice.

## Enterprise License Key

To start using Hoppscotch Enterprise, you will need to purchase a license from the [Hoppscotch Enterprise Store](https://enterprise.hoppscotch.com). Once you have purchased a license, you will receive an email with the license key. You can also find the license key in your [Hoppscotch Enterprise Dashboard](https://enterprise.hoppscotch.com/dashboard).

* [Guide: Manage an Enterprise License Key](/guides/articles/manage-an-enterprise-license-key)

## System Requirements

Hoppscotch is designed to run well on both small and large deployments. The minimum requirements to run Hoppscotch are an operating system that supports Docker and 4 CPU cores + 4GB of RAM to generate the build image and as little as 1 CPU core + 2GB of RAM to host the generated output files.

* For support regarding horizontal scaling, please reach out to [support@hoppscotch.io](mailto:support@hoppscotch.io).

## Install Node.js, npm, pnpm

### Node.js + npm

Install [`Node.js`](https://nodejs.org/en) (v18+) and [`npm`](https://www.npmjs.com) (v9+).

* [Node.js + npm installation guide](https://nodejs.org/en/download)

Verify Node.js and npm installation by running the following commands in your terminal:

```bash theme={null}
node -v
```

```bash theme={null}
npm -v
```

### pnpm

Install [`pnpm`](https://pnpm.io) (v6+).

* [pnpm installation guide](https://pnpm.io/installation)

Verify pnpm installation by running the following command in your terminal:

```bash theme={null}
pnpm -v
```

## Docker

Install [`Docker`](https://www.docker.com) (v20+).

* [Docker installation guide](https://docs.docker.com/engine/install)

Verify Docker installation by running the following command in your terminal:

```bash theme={null}
docker -v
```

It is recommended to use Compose V2. To switch to Compose V2, use the `docker compose` CLI plugin or activate the **Use Docker Compose V2** setting in Docker Desktop. For more information, see the [Evolution of Compose](https://docs.docker.com/compose/compose-v2).

## Git

Install [`Git`](https://git-scm.com) (v2+).

* [Git installation guide](https://git-scm.com/download)

Verify Git installation by running the following command in your terminal:

```bash theme={null}
git --version
```

## Email delivery (optional)

Hoppscotch comes with support for easy integrations with 3rd party SMTP providers. You will need emails so that you can invite your team to use Hoppscotch and for emails to work, you will need to set up proper SMTP configuration as described below.

To enable email delivery, you will need to generate a valid SMTP URL in the below format:

```
smtps://user@domain.com:pass@smtp.domain.com
```

For example, if you are using Gmail as your SMTP server your SMTP URL will look like something shown below:

```
smtps://user@gmail.com:pass@smtp.gmail.com
```

You can also use [mailcatcher](https://mailcatcher.me/) as a simple SMTP server.

### Custom SMTP configuration

For more advanced needs, such as production-level email delivery or gaining more control over your email configurations, you can set up a custom SMTP server.

To enable the custom mailer configuration, in addition to setting the `MAILER_USE_CUSTOM_CONFIGS` to `true`, you'll also need the following details in the specified format:

| Requirement   | Description                                  | Format                                 |
| ------------- | -------------------------------------------- | -------------------------------------- |
| SMTP Host     | Address of your SMTP server                  | `smtp.customdomain.com`                |
| SMTP Port     | Communication port used by your SMTP server  | `587` for **TLS** or `465` for **SSL** |
| SMTP User     | Username for your SMTP account               | `user@customdomain.com`                |
| SMTP Password | Corresponding password for your SMTP account | `custompass`                           |

You can use services like [SendGrid](https://sendgrid.com/), [Amazon SES](https://awss.amazon.com/ses/), or your own SMTP server to set up custom email delivery with Hoppscotch.

## Postgres database

Hoppscotch uses a Postgres database to store all the data. You can use any Postgres database provider of your choice - hosted locally or on a cloud provider. Make sure you have a valid Postgres database URL in the below format:

```
postgresql://username:password@url:5432/dbname
```

## ClickHouse

Hoppscotch uses ClickHouse to store all audit logs. You can use a locally hosted ClickHouse instance via [Docker](https://hub.docker.com/r/clickhouse/clickhouse-server) or a [managed instance](https://clickhouse.com/cloud). Ensure that the values for the following are assigned properly in admin dashboard.

```bash theme={null}
#ClickHouse Config
CLICKHOUSE_HOST=**************
CLICKHOUSE_USER=default
CLICKHOUSE_PASSWORD=''
```

You can enable/disable audit logging from your instance of Hoppscotch from admin dashboard. You can read more about audit logs [here](/guides/articles/audit-logs).

## OAuth

You also need to configure an OAuth provider to enable third-party authentication. Hoppscotch supports the following OAuth providers:

1. Email
2. GitHub
3. Google
4. Microsoft
5. SAML SSO
6. Open ID Connect

### Choosing OAuth Providers

Hoppscotch allows you to choose which authentication providers to enable for your workspace during the onboarding flow in the admin dashboard. You can easily select from options like Google, GitHub, Microsoft, SAML, Open ID Connect and Email directly through the setup interface.

```yaml theme={null}
VITE_ALLOWED_AUTH_PROVIDERS=GOOGLE,GITHUB,MICROSOFT,EMAIL,SAML,OIDC
```

### Configuring SAML

You may use services like [OneLogin](https://www.onelogin.com/) or [Okta](https://www.okta.com/) or other services to fetch the following parameters for SAML.

```yaml theme={null}
SAML_ISSUER=**********
SAML_AUDIENCE=nestjs-saml
SAML_CALLBACK_URL=http://localhost:3170/v1/auth/saml/callback
SAML_CERT=**********
SAML_ENTRY_POINT=**********
SAML_WANT_ASSERTIONS_SIGNED=true
SAML_WANT_RESPONSE_SIGNED=false
```

### Configuring OpenID Connect

You may use services like [OneLogin](https://www.onelogin.com/) or [Okta](https://www.okta.com/) or other services to fetch the following parameters for OIDC.

```yaml theme={null}
OIDC_PROVIDER_NAME=************************************************
OIDC_ISSUER=************************************************
OIDC_AUTH_URL=************************************************
OIDC_TOKEN_URL=************************************************
OIDC_USER_INFO_URL=************************************************
OIDC_CLIENT_ID=************************************************
OIDC_CLIENT_SECRET=************************************************
OIDC_CALLBACK_URL=http://localhost:3170/v1/auth/oidc/callback
OIDC_SCOPE=openid profile email
```

### Configuring third-party providers

To configure the third-party authentication, you will need to generate a valid OAuth client ID and client secret for the OAuth provider of your choice. You will also need to provide a valid callback URL for the OAuth provider.

For example, if you are using GitHub as your OAuth provider, you will need to generate a valid OAuth client ID and client secret for GitHub. You will also need to provide a valid callback URL for GitHub. The credentials for the GitHub OAuth provider can be entered during onboarding in the admin dashboard, and will look like the following:

```yaml theme={null}
GITHUB_CLIENT_ID=*****
GITHUB_CLIENT_SECRET=*****
GITHUB_CALLBACK_URL=http://localhost:3170/v1/auth/github/callback
GITHUB_SCOPE=user:email

# Set to 'true' if you are using github enterprise
IS_GITHUB_ENTERPRISE_ENABLED=false

# Change domain to respective org domain, if using Github Enterprise Cloud use github.com as domain
GITHUB_AUTHORIZATION_URL=https://{domain}/login/oauth/authorize
GITHUB_TOKEN_URL=https://{domain}/login/oauth/access_token

# If using Github Enterprise Cloud use api.github.com as domain for 2 fields below
GITHUB_USER_PROFILE_URL=https://{domain}/users
GITHUB_USER_EMAIL_URL=https://{domain}/user/emails
```

The `CALLBACK_URL` variable is the URL that is invoked after the authorization is done and it follows the pattern `http://localhost:3170/v1/auth/[auth_provider_name]/callback`.

The `SCOPE` variable defines the scope of the data that the OAuth provider passes on to Hoppscotch.

The links to configure OAuth for various providers are given below:

1. [**GitHub**](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/creating-an-oauth-app) (scope: email)
2. [**Google**](https://developers.google.com/identity/gsi/web/guides/get-google-api-clientid#get_your_google_api_client_id) (scope: email, profile)
3. [**Microsoft**](https://learn.microsoft.com/en-us/azure/active-directory/develop/scenario-web-app-sign-user-app-registration?tabs=nodejs#register-an-app-by-using-the-azure-portal) (scope: user with read permission)

<Note>It is recommended that you secure your deployments by issuing TLS certificates and using **HTTPS** since we use **secure HTTP cookies** for authenticating users.</Note>

## Support for standard `HTTP/s` ports

From the December 2023 release onwards containers now support ingress via standard HTTP/S ports on port `80` and `443` by default, moving forward it is recommended users switch to using these ports. We currently do still support the services being exposed from ports `3000`, `3100` and `3170` respectively but support for this will be dropped in the future and all containers will work over standard HTTP/s ports.


# Setup and access
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/setup-and-access

Learn how to set up and access Hoppscotch Enterprise Edition.

After successfully running the necessary containers, the next step involves creating an administrator account to manage Hoppscotch.

<Warning>The system automatically designates the first user who logs in through the admin dashboard as the administrator.</Warning>

## Creating an administrator account

1. Open a new browser tab and visit [`http://localhost:3100`](http://localhost:3100).
2. This will grant you access to the admin dashboard.
3. Login using your credentials or create a new account.
4. The first user to log in will be given administrator privileges.

<Card title="Admin dashboard" icon="circle-arrow-right" href="/documentation/self-host/community-edition/admin-dashboard">
  Learn how to manage your Hoppscotch instance using the admin dashboard.
</Card>

## Accessing the Hoppscotch app

With the administrator account set up, you can now start using the Hoppscotch app for API testing and development.

1. Open a new browser tab and visit [`http://localhost:3000`](http://localhost:3000).
2. Begin testing and developing your APIs seamlessly with Hoppscotch.

<Tip>Hoppscotch Enterprise Edition is available for on-premise deployment with priority support. [Contact Hoppscotch Support](/support/getting-started/contact)</Tip>


# Telemetry
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/telemetry

Telemetry and data sharing in Hoppscotch Enterprise Edition

Telemetry in Hoppscotch Self-Host refers to anonymous data shared with Hoppscotch. This helps identify the usage patterns of Hoppscotch.

# Data collected by Hoppscotch

Hoppscotch does not capture any data from your APIs. All captured data is anonymous and pertains to instance usage.

## Instance usage

The instance usage ping is sent once a week to indicate that the instance is operational. You can disable this event by navigating to the settings page and turning off data sharing settings.

```json theme={null}
{
  "uuid": "976fcae1-4079-4e83-881a-48723f694475",
  "event": "sh_instance",
  "properties": {
    "type": "ENTERPRISE",
    "total_user_count": 10,
    "total_workspace_count": 2,
    "version": "2024.3.0",
    "$lib": "posthog-node",
    "$lib_version": "3.6.3",
    "$geoip_disable": true,
    "$ip": "127.0.0.1",
    "$sent_at": "2024-02-20T06:14:20.041000+00:00",
    "$plugins_succeeded": [
      "GeoIP (8000)"
    ],
    "$plugins_failed": [],
    "$plugins_deferred": []
  },
  "timestamp": "2024-02-20T06:14:20.591000Z",
  "team_id": 15871,
  "distinct_id": "9bdec3aae9330af51ba91313d3de99b46ae928da",
  "elements_chain": "",
  "created_at": "2024-02-20T06:14:20.835000Z"
}

```

## Instance usage for billing

The Hoppscotch Enterprise edition sends an additional event to our licensing server to assist with billing. This event is triggered every 12 hours. The licensing server verifies the instance's license and we send the license status and number of seats used as query parameters. Once the license key is validated, the server returns a signed/encrypted text, which the enterprise instance uses to verify the source of the validation and converts it and stores it as a JSON similar to the one below.

```json theme={null}
{
   "status": "valid",
   "issuedTo": "AYQHAG$T1",
   "seats": 10
}

```

<Note>If you require offline license verification, you can request an offline license key by contacting us at [support@hoppscotch.io](mailto:support@hoppscotch.io).</Note>

# Turning off data sharing

You can turn off your data sharing preferences from your Hoppscotch admin dashboard and heading over to the Data Sharing section in the settings page


# User groups
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/user-groups

User groups allow admins to manage user permissions and roles in a shared workspace, providing a structured way to control access and actions within the workspace.

User groups are a powerful feature that enables admins to manage user permissions and roles within a shared workspace. This structured approach allows for efficient control over access and actions, ensuring that users can only perform tasks relevant to their roles.

## Creating a User Group

1. Navigate to the **Admin Dashboard**.
2. Click on the **User** page > **User Groups** tab.
3. Click on the **Create Group** button.
4. Enter a **name** for the group.
5. Optionally, add a **description** to clarify the group's purpose.
6. Click on the **Create** button to finalize the group creation.

## Adding Users to a Group

1. In the **User Groups** tab, select the group you want to add users to.
2. Click on the **Add Users** button.
3. In the pop-up window, search for and select the users you want to add.
4. Click on the **Add** button to confirm your selection.

## Group Permissions

User groups can have different permissions based on their roles. Common permissions include:

* **Viewer**: Can view workspace data but cannot make changes.
* **Editor**: Can view and edit workspace data, but cannot manage user permissions.
* **Owner**: Has full control over the workspace, including managing users and permissions.

When creating or editing a group, admins can assign these roles to users within the group to ensure they have the appropriate level of access.

## Managing User Groups

User groups can be managed by admins to ensure that the right users have the appropriate permissions. This includes:

* **Editing Group Details**: Admins can modify the group's name and description by selecting the group and clicking on the **Edit** button.
* **Removing Users**: To remove users from a group, select the group, click on the **Manage Users** button, and then remove users as needed.
* **Deleting Groups**: If a group is no longer needed, admins can delete it by selecting the group and clicking on the **Delete Group** button.

## Best Practices

* **Define Clear Roles**: Establish clear roles and responsibilities for each user group to avoid confusion and ensure accountability.
* **Regularly Review Groups**: Periodically review user groups to ensure they still align with the organization's needs and that users have the appropriate permissions.
* **Use Descriptions**: Utilize the description field to provide context for each group, making it easier for admins to understand the purpose of each group at a glance.
* **Limit Group Size**: Keep user groups manageable in size to facilitate easier management and communication.


# SCIM Integration for User Provisioning
Source: https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/user-provisioning

Manage users efficiently with SCIM provisioning in Hoppscotch.

User management can become overwhelming as your organization scales. **SCIM (System for Cross-domain Identity Management)** offers a standardized way to handle user provisioning, updates, and deprovisioning. With SCIM integration, Hoppscotch connects directly to your Identity Provider (IdP), helping you manage users in one place and reflect those changes across systems.

## Setting Up SCIM Provisioning

Follow the steps below to configure SCIM-based user provisioning in Hoppscotch and integrate it with your Identity Provider (IdP).

### 1. Enable SCIM in Hoppscotch

* Open the **Admin Dashboard** and navigate to the **Configurations** section.
* Find the **SCIM Provisioning** option under **User Provisioning** block and enable it.
* Copy the **SCIM Base URL (`http(s)://<backend-URL>/scim/v2`)** provided after activation, as it will be needed for the integration.

<Frame>
  <img />
</Frame>

### 2. Generate an InfraToken

* Go to the **[InfraTokens](/documentation/self-host/enterprise-edition/admin-dashboard#infra-tokens)** section of the dashboard.
* Create a new token for SCIM-related operations.
* Copy the InfraToken and store it securely, as it will be used to authenticate SCIM requests from your IdP.

<Frame>
  <img />
</Frame>

### 3. Configure SCIM in your Identity Provider `Example: Okta`

* Log in to your [Okta](https://www.okta.com/) dashboard, select your application, and navigate to the application's settings.
* Enable SCIM provisioning under the **General** tab.

<Frame>
  <img />
</Frame>

* Go to the **Provisioning > Integration** section:
  * Paste the **SCIM Base URL** you copied from Hoppscotch.
  * Specify the unique identifier field for users (e.g., `email`) and configure provisioning actions (e.g., Import New Users, Profile Updates, Push New Users, Push Profile Updates) according to your requirements.
  * Use the `InfraToken` generated in the Hoppscotch Admin Dashboard as the **Authorization Token** and save the configuration.

<Frame>
  <img />
</Frame>

* Under **Provisioning > To App**, enable the following actions:
  * **Create Users**
  * **Update User Attributes**
  * **Deactivate Users**
    Save the settings once done.

<Frame>
  <img />
</Frame>

## Add a custom attribute

SCIM supports extending the user schema to include custom fields to meet your organization's specific requirements:

* In Okta, head to **Directory > Profile Editor** and locate the SCIM application.
* Click **Add Attribute** to create a custom attribute you wish to include in the provisioning process.

<Frame>
  <img />
</Frame>

* Fill in the required fields and assign a valid **External namespace**. For SCIM 2.0, the following namespaces are supported in Okta:

```bash theme={null}
# Use this for basic user attributes
urn:ietf:params:scim:schemas:core:2.0:User

# Use this for enterprise-specific user extensions
urn:ietf:params:scim:schemas:extension:enterprise:2.0:User
```

* Once finished, click **Save Attribute** to apply the changes.

<Frame>
  <img />
</Frame>

The **custom attribute** will now be automatically synchronized during user creation or updates.

<Tip> Once configured, assigning a user or group to the application will trigger user creation in Hoppscotch and grant them access to your instance. If a user is unassigned, they will be removed from Hoppscotch and their access permissions will be revoked. </Tip>


# Getting started
Source: https://docs.hoppscotch.io/documentation/self-host/getting-started

Welcome Hoppscotch Self-Host.

This section will help you get started with self-hosting your instance of Hoppscotch. If you are looking to self-host your instance of [Hoppscotch](https://github.com/hoppscotch/hoppscotch) you will need to have to install a few other dependencies. Go through our prerequisite guide below install all the required dependencies and have the required information ready.

<CardGroup>
  <Card title="Community Edition" icon="circle-arrow-right" href="/documentation/self-host/community-edition/getting-started">
    Hoppscotch Community Edition is free and open-source. It is licensed under the MIT License. You can use it for personal and commercial projects. It is a great choice for individuals and small teams.
  </Card>

  <Card title="Enterprise Edition" icon="circle-arrow-right" href="/documentation/self-host/enterprise-edition/getting-started">
    SAML-based SSO, on-prem deployment, audit logs, and more. Hoppscotch Enterprise Edition is a self-hosted version of Hoppscotch Cloud with enterprise-ready features for teams and organizations.
  </Card>
</CardGroup>

<Info>Hoppscotch Enterprise Edition is available for on-premise deployment with <ins>priority support</ins>. [Contact Hoppscotch Support](/support/getting-started/contact)</Info>

***

## Hoppscotch Self-Host is available in two editions

1. Community Edition
2. Enterprise Edition

Here's a quick comparison of the two editions:

| **Self-Host**            | **Community Edition** (CE)                                                                                                                                                               | **Enterprise Edition** (EE)                                                                                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
|                          | We build software in the open, with permissive licenses and thriving communities because we believe investing in open source will help leave the world a little better than we found it. | Deploy Hoppscotch on-premise with our support. Securely manage, organize, and accelerate API-first development at scale. Hoppscotch Self-Host is the one-stop solution to own control over your APIs, data, and privacy. |
| Distribution             | Open-source.                                                                                                                                                                             | Open-core.                                                                                                                                                                                                               |
| Installation             | Install, administer, and maintain on your own.                                                                                                                                           | Install, administer, and maintain on your own with our **priority support**.                                                                                                                                             |
| Upgrades and maintenance | Update it yourself. Quarterly releases.                                                                                                                                                  | Guaranteed quarterly updates. Take advantage of the priority support for **early birds**.                                                                                                                                |
| Hosting and Deployment   | Self-managed so you can deploy in your own data center or cloud capacity.                                                                                                                | Self-managed so you can deploy in your own data center or cloud capacity.                                                                                                                                                |
| OAuth Providers          | Configure OAuth providers such as Email, GitHub, Google, and Microsoft for third-party authentication.                                                                                   | Configure advanced OAuth providers like **SAML-based SSO and OpenID Connect**, along with Email, GitHub, Google, and Microsoft, to enable comprehensive third-party authentication options.                              |
| Workspace Management     | Invite Workspace Members, Assign roles and remove members with Owner rights.                                                                                                             | Invite Workspace Members, Assign roles and remove members with Owner rights.                                                                                                                                             |
| Advanced admin tools     | Not included.                                                                                                                                                                            | Access **advanced admin tools** to govern, audit, and secure user permissions and data. Includes features like user permissions, audit logs, and more.                                                                   |
| Access Controls          | Not included.                                                                                                                                                                            | Implement robust access controls, including **domain whitelisting and site protection**, to enhance security and restrict access to authorized users only.                                                               |
| Support                  | Community forums.                                                                                                                                                                        | **Dedicated support from the Hoppscotch team** to provide critical response, help establish best practices, and be an on-demand resource for ongoing questions.                                                          |
| Pricing                  | Free.                                                                                                                                                                                    | \$19/user/mo<br />Billed monthly.<br />[Book a demo for a free trial](https://cal.com/hoppscotch/enterprise-demo).                                                                                                       |

<Tip>Jump to the [**Community Edition**](/documentation/self-host/community-edition/getting-started) or [**Enterprise Edition**](/documentation/self-host/enterprise-edition/getting-started) guide to get started.</Tip>


# Index
Source: https://docs.hoppscotch.io/guides/articles

Complete list of articles and guides for Hoppscotch.

<Tip>Interested in writing an article about Hoppscotch? Contact us at `support@hoppscotch.io`.</Tip>

<CardGroup>
  <Card title="RESTful API testing with Hoppscotch" icon="circle-arrow-right" href="/guides/articles/restful-api-testing-with-hoppscotch">
    Representational State Transfer (REST) APIs are a core part of communication between a web/mobile client and a server...
  </Card>

  <Card title="Improving your API workflow" icon="circle-arrow-right" href="/guides/articles/improving-your-api-workflow">
    Hoppscotch provides you with a minimal and blazing platform to design, develop and test your APIs...
  </Card>

  <Card title="Understanding GraphQL" icon="circle-arrow-right" href="/guides/articles/understanding-graphql">
    The GraphQL schema is at the core of any GraphQL server. It defines the capabilities of the API and specifies how clients can access that data...
  </Card>

  <Card title="Downgrading and Restoring Backups" icon="circle-arrow-right" href="/guides/articles/downgrading-and-restoring-backups">
    If an update causes issues with Hoppscotch Desktop, you can downgrade to a previous version and restore your data from an automatic backup...
  </Card>
</CardGroup>

# Community Articles

<CardGroup>
  <Card title="Uplifting Web Experience with Hoppscotch Widgets" icon="circle-arrow-right" href="/guides/articles/uplifting-web-experience-with-hoppscotch-widgets">
    Widgets are interactive components that can be embedded in HTML pages to enhance user experience...
  </Card>
</CardGroup>

<Tip>We're looking for more articles! If you have written an article about Hoppscotch, please [open a pull request](https://github.com/hoppscotch/docs) on our documentation repository. We'll be happy to add it to this list.</Tip>


# Audit Logs in Hoppscotch
Source: https://docs.hoppscotch.io/guides/articles/audit-logs

Learn about the audit logs in Hoppscotch Enterprise.

In Enterprise Hoppscotch, a record of all actions taken on the platform is saved which can be used to know what events happened, who performed them, and when they occurred. With the information present users may be able to draw insights related to the platform.

### Log Format

Every event that occurred on the platform is saved in the following format.

```json theme={null}
{
  "event": "",
  "timestamp": "",
  "user": {
    "id": "",
    "email": "",
    "name": ""
  },
  "group": {
    "type": "TEAM | USER | ADMIN",
    "id": "",
    "name": ""
  },
  "resource": {
    "id": "",
    "type": "",
    "name": "",
    "metadata": ""
  },
  "statusCode": "",
  "errorMessage": "",
  "result": "",
  "server_version": ""
}
```

| Data            | Description                                           | Details                          |
| --------------- | ----------------------------------------------------- | -------------------------------- |
| event           | Action performed                                      |                                  |
| timestamp       | The date and time of a logged event                   |                                  |
| user            | The user who made performed an event                  | `id`, `email`, `name`            |
| group           | Where the user belongs to in the context of the event | `type`, `id`                     |
| resource        | Upon what the action is being carried out             | `id`, `type`, `name`, `metadata` |
| statusCode      | Status code for the action response                   |                                  |
| errorMessage    | Error description if action failed                    |                                  |
| result          | Status of the action                                  |                                  |
| server\_version | Server version being run currently                    |                                  |

An example of an audit log:

```json theme={null}
{
  "event": "admin.team.create",
  "timestamp": "2023-08-30 07:03:05",
  "user": {
    "id": "cllxa1zqt000gp91zaq6tj93d",
    "email": "John@hoppscotch.io",
    "name": "John Doe"
  },
  "group": {
    "type": "ADMIN",
    "id": "cllxa1zqt000gp91zaq6tj93d"
  },
  "resource": {
    "type": "TEAM",
    "metadata": "{\"id\":\"cllxe4ji4000op91zucsbwazj\",\"name\":\"Fellowship of the Hopp\"}"
  },
  "statusCode": 200,
  "errorMessage": "",
  "result": "SUCCESS",
  "server_version": "2023.4.8"
}
```

### Tracked Events

The following table contains all the events that are logged currently.

| EVENT                             | EVENT DESCRIPTION                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------ |
| admin.users.invite                | Event for inviting multiple users to join the platform                               |
| admin.user.invite                 | Event for inviting a single user to join the platform                                |
| admin.user.remove                 | Event for removing a user from the platform                                          |
| admin.user.makeAdmin              | Event for elevating a user to admin status                                           |
| admin.user.makeNormal             | Event for demoting an admin user to normal user status                               |
| admin.team.create                 | Event for creating a new team                                                        |
| admin.team.user.changeRole        | Event for changing the role of a user in a team                                      |
| admin.team.user.remove            | Event for removing a user from a team                                                |
| admin.team.user.add               | Event for adding a user to a team                                                    |
| admin.team.rename                 | Event for renaming a team                                                            |
| admin.team.delete                 | Event for deleting a team                                                            |
| admin.user.revoke                 | Event for revoking a user's team invitation                                          |
| user.auth.magicLinkSent           | Event for when a magic link is sent to a user                                        |
| user.auth.loggedIn                | Event for when a user logs in                                                        |
| user.auth.tokenRefresh            | Event for when a user's auth token is refreshed                                      |
| user.auth.loggedOut               | Event for when a user logs out                                                       |
| user.auth.adminVerify             | Event for when we verify if a user is an admin                                       |
| user.session.update               | Event for updating a user's app session                                              |
| user.account.delete               | Event for deleting a user's account                                                  |
| user.shortcode.create             | Event for creating a shortcode                                                       |
| user.shortcode.revoked            | Event for deleting a shortcode                                                       |
| team.create                       | Event for creating a new team                                                        |
| team.user.leave                   | Event for when a user leaves a team                                                  |
| team.user.remove                  | Event for removing a user from a team                                                |
| team.rename                       | Event for renaming a team                                                            |
| team.delete                       | Event for deleting a team                                                            |
| team.member.roleUpdate            | Event for changing a user's role in a team                                           |
| team.check                        | Event for checking if a team exists                                                  |
| team.member.check                 | Event for checking if a user is a member of a team                                   |
| team.collection.createRoot        | Event for creating a root team collection                                            |
| team.collection.import            | Event for importing a collection from a JSON string                                  |
| team.collection.replace           | Event for replacing an existing collection with new data                             |
| team.collection.createChild       | Event for creating a child collection                                                |
| team.collection.rename            | Event for renaming a collection                                                      |
| team.collection.delete            | Event for deleting a collection                                                      |
| team.collection.move              | Event for moving a collection                                                        |
| team.collection.updateOrder       | Event for updating the order of collections                                          |
| team.collection.collectionCheck   | Event for checking if a collection exists in a team                                  |
| team.environment.environmentCheck | Event for checking if an environment exists in a team                                |
| team.environment.create           | Event for creating an environment                                                    |
| team.environment.delete           | Event for deleting an environment                                                    |
| team.environment.update           | Event for updating an environment                                                    |
| team.environment.clear            | Event for clearing the contents of an environment                                    |
| team.environment.duplicate        | Event for duplicating an environment                                                 |
| team.invitation.create            | Event for creating a team invitation                                                 |
| team.invitation.revoke            | Event for revoking a team invitation                                                 |
| team.invitation.accept            | Event for accepting a team invitation                                                |
| team.invitation.inviteCheck       | Event for checking if an invitation exists                                           |
| team.request.create               | Event for creating a team request                                                    |
| team.request.update               | Event for updating a team request                                                    |
| team.request.delete               | Event for deleting a team request                                                    |
| team.request.updateOrder          | Event for updating the order of team requests                                        |
| team.request.move                 | Event for moving a team request                                                      |
| team.request.requestCheck         | Event for checking if a request exists in a team                                     |
| team.request.roleCheck            | Event for checking if a user has the relevant role to perform an action in a request |
| user.session.update               | Event for updating a user's app session                                              |
| user.delete                       | Event for deleting a user                                                            |
| user.collection.createRoot        | Event for creating a root user collection                                            |
| user.collection.createChild       | Event for creating a child user collection                                           |
| user.collection.rename            | Event for renaming a user collection                                                 |
| user.collection.delete            | Event for deleting a user collection                                                 |
| user.collection.move              | Event for moving a user collection                                                   |
| user.collection.updateOrder       | Event for updating the order of user collections                                     |
| user.collection.import            | Event for importing a collection                                                     |
| user.environment.create           | Event for creating a user environment                                                |
| user.environment.update           | Event for updating a user environment                                                |
| user.environment.delete           | Event for deleting a user environment                                                |
| user.environment.deleteAll        | Event for deleting all personal environments of a user                               |
| user.environment.clearGlobal      | Event for clearing the global environments for a user                                |
| user.history.create               | Event for creating a user history                                                    |
| user.history.toggleStar           | Event for toggling the star on a user history                                        |
| user.history.delete               | Event for deleting a user history                                                    |
| user.history.deleteAll            | Event for deleting all user histories                                                |
| user.request.create               | Event for creating a user request                                                    |
| user.request.update               | Event for updating a user request                                                    |
| user.request.deleted              | Event for deleting a user request                                                    |
| user.request.move                 | Event for moving a user request                                                      |
| user.settings.create              | Event for creating user settings                                                     |
| user.settings.update              | Event for updating user settings                                                     |


# Improving your API workflow
Source: https://docs.hoppscotch.io/guides/articles/improving-your-api-workflow

Learn how to improve your API workflow with Hoppscotch.

Hoppscotch provides you with a minimal and blazing platform to design, develop and test your APIs. Hoppscotch enables you to quickly get started and even helps you to organize your work to help you improve your workflow.

Hoppscotch provides you with three major ways for you to manage your APIs and enhance your development workflow:

* Collections
* Environments
* Workspaces

## Collections

Collections help you save and organize your API requests. You can create collections and add requests to them to share with your team or to use later. You can also import and export collections from Hoppscotch, OpenAPI, and Postman.

## Environments

Environments provide you the functionality to create key-value pairs that can be used as variables in your request URL, headers, and even as auth tokens. You can create several such key-value pairs and group them under a single environment. Environments are self-isolated from each other and an active environment needs to be selected if you have multiple environments created.

## Workspaces

Workspaces help you organize your requests, collections, and environments for specific purposes and project stages. You can create unlimited Workspaces and invite as many collaborators as needed in Hoppscotch. Whether you're working solo or with a team, you can choose between **Personal and Team Workspaces** to fit your needs.

A Personal Workspace is a private area exclusively for you, where collaboration isn't possible. Within a Personal Workspace, you can choose to sync your collections and environment data either with the [Hoppscotch cloud](https://hoppscotch.io) or **keep it stored locally**.

To learn more about setting up new Workspaces and collaborating with your team on APIs, head over to our [documentation for Workspaces](https://docs.hoppscotch.io/documentation/features/workspaces).


# Managing your Enterprise License Key
Source: https://docs.hoppscotch.io/guides/articles/manage-an-enterprise-license-key

Learn how to manage your Hoppscotch Enterprise Edition license key.

This guide provides step-by-step instructions for managing your Hoppscotch Enterprise Edition license key. If you plan to self-host the Hoppscotch Enterprise Edition, you must obtain a License Key.

## Creating an account

To initiate the process, you need to create an account on the Hoppscotch Enterprise Dashboard.

1. Visit [enterprise.hoppscotch.com](https://enterprise.hoppscotch.com) and provide your email.
2. A magic link will be sent to your email address.
3. Click on the magic link to log in, and you will be redirected to a screen to input your organization's information.

Continue by clicking "Next" and enter information about the organization

Continue by clicking "Next" and enter the personal information of the individual responsible for the purchase on behalf of the organization.

To proceed with the purchase, review and accept the end user license agreement.

## Booking a demo

After agreeing to the license terms, you can schedule a demo with our team. Click the "Book a Demo" button.

## Making the purchase

While you can directly purchase by clicking the "Subscribe" button, we recommend scheduling a call with us for personalized assistance.

1. Click the "Subscribe" button.
2. Enter the number of seats required for the license.
3. Click the **Create** button to proceed to checkout and complete the payment.

Upon successful payment, your License Key will be available on the dashboard. Copy it and paste it into the `.env` file in your project's root directory. You can now start utilizing Hoppscotch Enterprise Edition.

## Updating your license

With a valid license, you can manage it to update the seat count or generate a new license under the same account through the enterprise dashboard.

## Offline license verification

<Note>If you require offline license verification, you can request an offline license key by contacting us at [support@hoppscotch.io](mailto:support@hoppscotch.io).</Note>

For more information on self-hosting Hoppscotch Enterprise Edition, consult the guide on [Self-Hosting Hoppscotch Enterprise Edition](/documentation/self-host/enterprise-edition/getting-started).


# RESTful API testing with Hoppscotch
Source: https://docs.hoppscotch.io/guides/articles/restful-api-testing-with-hoppscotch

Learn how to use Hoppscotch to test your RESTful APIs.

Representational State Transfer (REST) APIs are a core part of communication between a web/mobile client and a server. The majority of web-based applications depend on REST APIs to fetch and modify data thus separating the data processing part from the front-end. Hoppscotch provides a fast and intuitive platform to develop and test REST APIs making it easier for developers worldwide to work efficiently.

## Understanding REST

REST usually uses the Hypertext Transfer Protocol (HTTP) to set up communication between the client and the server. REST APIs ensure that the server transfers information in a standard format. A REST API call generally contains the following steps -

1. The client sends a request to the server.
2. The server authenticates the client and ensures that the client is authorized to request the information.
3. The server accepts the requests and processes them.
4. The server responds with a code to tell the client if the request was successful or not and sends the requested information if the request was successful.

Whenever a client requests information, the server always sends back a status code to indicate the status of the request. These are called HTTP status codes and are grouped into five types.

| Status Code   | Response Type |
| ------------- | ------------- |
| 1xx (100-199) | Informational |
| 2xx (200-299) | Success       |
| 3xx (300-399) | Redirection   |
| 4xx (400-499) | Client error  |
| 5xx (500-599) | Server error  |

REST APIs also support HTTP methods to do operations on data. Hoppscotch supports the following methods out of the box.

| HTTP Method | Usage                                                              |
| ----------- | ------------------------------------------------------------------ |
| GET         | Retrieve resource from a server                                    |
| POST        | Create or send new resource                                        |
| PUT         | Updating resource, can also be used for creating resource          |
| PATCH       | Similar to PUT, can be used to modify resources                    |
| DELETE      | Delete resource from the server                                    |
| HEAD        | Read HTTP header information                                       |
| CONNECT     | To start a two-way communication with resource                     |
| OPTIONS     | Requests permitted communication options for a given URL or server |
| TRACE       | Used to debug the path to the target resource                      |
| CUSTOM      | Create custom methods as per your need                             |

## Using Hoppscotch to test your REST APIs

Hoppscotch provides you with a minimal yet robust platform to test your REST APIs. The REST platform is the default platform you see when you open Hoppscotch.

You can enter the API endpoint and choose the HTTP method according to your needs from the dropdown menu. Once it is configured, click on the "**Send**" button and you will see the response returned by the server. It's that simple.

Now try it yourself, copy the below API endpoint, and create a request.

```
https://echo.hoppscotch.io
```

### Locally served APIs

If you are planning to use Hoppscotch to test your locally served APIs, it is recommended that you install the Hoppscotch Browser Extension. Once installed, switch the interceptor on Hoppscotch to Browser Extension from the settings page or bottom bar to add support for [localhost](http://localhost) protocols.

### Adding parameters to your request

You can also parameterize your URLs by specifying parameters in the URL itself or adding parameters manually in the parameters tab. To add a parameter in the URL, append `?` at the end of the URL and add a parameter in `key=value` format.

### Working with environment variables

Environment variables allow you to store and reuse values in your requests and scripts. You can create a new environment by clicking the environments icon on the sidebar and clicking the `new` button.

If you have more than one environment, select the environment whose variables you want to access. You can access the variables in the request section by referencing the variable in the following format`<<variable_name>>`.

### Authentication tokens

Hoppscotch has support for various types of authentication mechanisms such as Basic Auth, Bearer Token, OAuth 2.0, and API Key. You can configure this using the Authorization tab on the request section of Hoppscotch.

These are just a few of the amazing set of features that Hoppscotch provides you to make your life easier as a developer. In addition to this, Hoppscotch supports features such as collections to save your requests, pre-requests to add dynamic behavior to your requests and so much more.


# Self-Host Hoppscotch on your own servers
Source: https://docs.hoppscotch.io/guides/articles/self-host-hoppscotch-on-your-own-servers

Set up Hoppscotch on your servers for complete control and customization.

Self-hosting Hoppscotch gives you complete control over your API development workflow and allows you to deploy Hoppscotch in your own data center or cloud, giving you greater control over data and security.

Self-hosted Hoppscotch comes in two variants - [Community](https://docs.hoppscotch.io/documentation/self-host/community-edition/getting-started) and [Enterprise Edition](https://docs.hoppscotch.io/documentation/self-host/enterprise-edition/getting-started), both of which can be deployed on systems that support Docker. You can host Hoppscotch on your servers, providing a private workspace for the individuals or teams using it.

This guide covers the basics of self-hosting Hoppscotch, including the configurations and settings needed to get started.

## Pre-requisites

Before you start ensure that your system or environment meets the following requirements:

* [Node.js (v18+) and npm (v9+)](https://nodejs.org/en/download/package-manager) - Ensure that both Node.js and npm are up-to-date to support the latest features and security patches.
* [pnpm](https://pnpm.io/installation) (v6+) - Recommended for efficient package management and faster installations.
* [Docker](https://docs.docker.com/engine/install) (v20+) - Docker should be properly installed and configured for containerization of your Hoppscotch instance.
* [Git](https://git-scm.com/download) - Required for version control and managing Hoppscotch source code.

Visit our [documentation](https://docs.hoppscotch.io/documentation/self-host/community-edition/prerequisites) for a detailed guide on installing the prerequisite softwares.

## Configuring the Environment

Create a `.env` file in your working directory, copy the example environment variable configurations provided below into it, and then replace the example values with your actual values.

<Warning> Ensure that there are **NO QUOTES** encapsulating the values of the environment variables and **NO SPACES** around the equals sign (`=`). </Warning>

```yaml theme={null}
#-----------------------Backend Config------------------------------#

# Prisma Config
DATABASE_URL=postgresql://postgres:testpass@hoppscotch-db:5432/hoppscotch

# (Optional) By default, the AIO container (when in subpath access mode) exposes the endpoint on port 80. Use this setting to specify a different port if needed.
HOPP_AIO_ALTERNATE_PORT=80

# Sensitive Data Encryption Key while storing in Database (32 character)
DATA_ENCRYPTION_KEY=********************************

# Whitelisted origins for the Hoppscotch App.
# This list controls which origins can interact with the app through cross-origin comms.
# - localhost ports (3170, 3000, 3100): app, backend, development servers and services
# - app://localhost_3200: Bundle server origin identifier
#   NOTE: `3200` here refers to the bundle server (port 3200) that provides the bundles,
#   NOT where the app runs. The app itself uses the `app://` protocol with dynamic
#   bundle names like `app://{bundle-name}/`
WHITELISTED_ORIGINS="http://localhost:3170,http://localhost:3000,http://localhost:3100,app://localhost_3200,app://hoppscotch"

#-----------------------Frontend Config------------------------------#

# Base URLs
VITE_BASE_URL=http://localhost:3000
VITE_SHORTCODE_BASE_URL=http://localhost:3000
VITE_ADMIN_URL=http://localhost:3100

# Backend URLs
VITE_BACKEND_GQL_URL=http://localhost:3170/graphql
VITE_BACKEND_WS_URL=wss://localhost:3170/graphql
VITE_BACKEND_API_URL=http://localhost:3170/v1

# Terms Of Service And Privacy Policy Links (Optional)
VITE_APP_TOS_LINK=https://docs.hoppscotch.io/support/terms
VITE_APP_PRIVACY_POLICY_LINK=https://docs.hoppscotch.io/support/privacy

# Set to `true` for subpath based access
ENABLE_SUBPATH_BASED_ACCESS=false
```

### 1. Database Configuration

Hoppscotch uses a Postgres database to store all the data. You can use any Postgres database provider of your choice, hosted locally or on a cloud.

Update the `DATABASE_URL` variable in your `.env` file with your custom database connection string, which should include the username, password, and database name.

```jsx theme={null}
DATABASE_URL=postgresql://username:password@url:5432/dbname
```

### 2. **SMTP Configuration**

To invite your team to use Hoppscotch and enable email delivery, you'll need to configure SMTP settings properly.

#### **2.1 Basic SMTP Configuration**

For basic SMTP configuration, you can use [mailcatcher](https://mailcatcher.me). It runs a super simple SMTP server which catches any message sent to it to display in a web interface.

You can set up mailcatcher using Docker with 2 below easy steps:

1. Pull the [Mailcatcher Image](https://hub.docker.com/r/dockage/mailcatcher) from Docker Hub,

   ```jsx theme={null}
   docker pull dockage/mailcatcher:0.9.0
   ```

2. With Mailcatcher set up on your machine, start the Mailcatcher container using `docker run` with the appropriate port mappings (`1080` for the web interface and `1025` for SMTP).

   > Docker containers are isolated from the host by default. When using localhost inside a Docker container, it refers to the container itself, and not the host machine. Since Hoppscotch runs inside a Docker container while Mailcatcher runs on the host machine, you'll need to use the **Docker bridge network IP** instead of `localhost` to ensure that the containerized application can communicate with the Mailcatcher service on the host. To find this IP address, run:
   >
   > ```jsx theme={null}
   > ip addr show docker0
   > ```
   >
   > Look for the inet address associated with the docker0 interface. It's typically in the **172.17.0.0/16** range but may vary based on your Docker network configuration. And If you're using **Docker Desktop**, you can use `host.docker.internal` instead of `localhost`.

   ```bash theme={null}
   docker run --name='mailcatcher' -d \
     --publish=<Docker_bridge_IP or host.docker.internal>:1080:1080 \
     --publish=<Docker_bridge_IP or host.docker.internal>:1025:1025 \
     dockage/mailcatcher:0.9.0
   ```

   Visit `http://<Docker_bridge_IP or host.docker.internal>:1080` to access the Mailcatcher web interface and view email communications.

   Further, configure the below environment variables in your `.env` file:

   ```jsx theme={null}
   MAILER_SMTP_ENABLE=true
   MAILER_USE_CUSTOM_CONFIGS=false
   MAILER_ADDRESS_FROM=from@example.com
   MAILER_SMTP_URL=smtp://<Docker_bridge_IP or host.docker.internal>:1025
   ```

#### **2.2 Custom Mailer Configuration**

For advanced email delivery needs, such as for production environments, you can configure a custom email service by setting `MAILER_USE_CUSTOM_CONFIGS=true`. You can choose from services like [SendGrid](https://sendgrid.com/), [Amazon SES](https://aws.amazon.com/ses/), or your own SMTP server. Once you've set up your chosen service, update your `.env` file with the following details:

```jsx theme={null}
MAILER_SMTP_HOST=smtp.domain.com
MAILER_SMTP_PORT=587
MAILER_SMTP_SECURE=true
MAILER_SMTP_USER=user@domain.com
MAILER_SMTP_PASSWORD=pass
MAILER_TLS_REJECT_UNAUTHORIZED=true
```

### 3. OAuth Configuration

To access the admin dashboard, you'll need to configure an OAuth provider. In the Community Edition, Hoppscotch supports:

1. Google
2. GitHub
3. Microsoft

In the Enterprise Edition, support also includes **SAML SSO, OpenID Connect, and GitHub Enterprise**.

Here's a quick guide to registering an OAuth application with GitHub:

1. Click your profile photo in the upper-right corner and select **Settings**.
2. In the left sidebar, scroll down and click **Developer Settings**.
3. Click **OAuth Apps** in the sidebar.
4. Click **New OAuth App**.
5. Enter the required information and specify the callback URL as indicated in your configuration.
6. After registering the application, copy the Client ID and Client Secret, and add them to your environment file.

Similarly, you can follow the specific setup instructions for other OAuth providers to complete your configuration.

### 4. Subpath Access

Subpath access allows you to host multiple services under a single domain by assigning each service a specific subpath.

When `ENABLE_SUBPATH_BASED_ACCESS=true`, you can access all three services (Hoppscotch App, Admin Dashboard, Hoppscotch Backend) on the same domain using different routes. If subpath access is disabled **(`ENABLE_SUBPATH_BASED_ACCESS=false`)**,  you will need to access the services on different ports.

<Warning>
  By default, the AIO container exposes the app on port 80. This can cause conflicts if you're running on a host system where port 80 is privileged, such as with Rootless Docker, Podman, or hardened environments like OpenShift. If you experience issues on these setups, try setting `HOPP_AIO_ALTERNATE_PORT` to bind the app to a non-privileged port.
</Warning>

## Installing dependencies, running migrations & building the image

Once the environment variables are configured, you may now proceed to the next step of setting up the Hoppscotch instance.

<Steps>
  <Step title="Check Database Connectivity">
    Ensure that the database instance is active and running at the `DATABASE_URL` specified in your `.env` file.

    ```jsx theme={null}
    docker ps
    ```
  </Step>

  <Step title="Select the suitable Hoppscotch instance to self-host">
    There are two ways to set up Hoppscotch:

    1. **Using individual containers for the services** - Hoppscotch Backend, Hoppscotch Frontend and Hoppscotch Admin Dashboard.
    2. **Using the AIO container** - a single container that provides all the services required to run Hoppscotch.

    For a streamlined setup, let's proceed with the AIO container. If you'd like to set up individual containers instead, [refer to the documentation](https://docs.hoppscotch.io/documentation/self-host/community-edition/install-and-build#using-individual-containers-for-the-services).
  </Step>

  <Step title="Pull the latest Hoppscotch container">
    Pull the container from DockerHub with the following command. If a specific version isn't provided, it will automatically pull the latest version:

    ```jsx theme={null}
    docker pull hoppscotch/hoppscotch
    ```
  </Step>

  <Step title="Run Database Migrations">
    After pulling the Hoppscotch image from DockerHub, you need to run database migrations to set up the necessary tables. Use the following commands:

    ```jsx theme={null}
    docker run -it --entrypoint sh --env-file .env hoppscotch/hoppscotch
    # pnpm exec prisma migrate deploy
    ```
  </Step>

  <Step title="Start the Hoppscotch Instance">
    To launch Hoppscotch, run the container with the following command:

    ```jsx theme={null}
    docker run -p 3000:3000 -p 3100:3100 -p 3170:3170 --env-file .env --restart unless-stopped hoppscotch/hoppscotch
    ```
  </Step>
</Steps>

## Accessing Admin Dashboard and Application

* **Accessing the Admin Dashboard**
  * After successfully running the required containers, the next step is to create an **Admin** account.
  * To access the Admin Dashboard, visit [**`http://localhost:3100`**](http://localhost:3100/) if `ENABLE_SUBPATH_BASED_ACCESS=false`.
  * Log in with your credentials or create a new account to obtain admin privileges.
  * Once logged in, you'll find the Dashboard as your central hub for managing workspaces, overseeing user activities, and configuring OAuth environment variables directly from the Settings page.
* **Accessing the Hoppscotch Application**
  * You can access the Hoppscotch application itself at `http://localhost:3000`.

***

In conclusion, this guide has covered how to self-host Hoppscotch, helping you set everything up in one go. If you prefer visual guidance, check out the video below for a detailed walkthrough that complements the instructions provided here. For additional details on each step of self-hosting Hoppscotch, refer to our [documentation](https://docs.hoppscotch.io/documentation/self-host/getting-started).

<iframe title="Step-by-step guide to Self-Host Hoppscotch" />


# Set Up OpenTelemetry Stack with Docker
Source: https://docs.hoppscotch.io/guides/articles/set-up-opentelemetry-stack-with-docker

A guide to setting up the OpenTelemetry stack using Docker.

This guide will help you set up the **OpenTelemetry Collector** on your own server and connect it with **Hoppscotch**.

Hoppscotch will send telemetry data (traces and metrics) to your **OpenTelemetry Collector** instance. From the **Hoppscotch Admin Dashboard**, you can easily configure the connection to your deployed Collector.

<Frame>
  <img />
</Frame>

Once connected, you can integrate with observability tools such as Jaeger (for traces), Prometheus (for metrics), and Grafana (for dashboards).

# Architecture Overview

1. **Hoppscotch** sends telemetry data to your **OpenTelemetry Collector**.
2. The **Collector** processes this data and exports it to your preferred backends:
   * Jaeger (traces)
   * Prometheus (metrics)
   * Grafana (visualizations, via Prometheus)
3. You can also enable debugging by exporting logs directly to the console.

<AccordionGroup>
  <Accordion title="Step 1: Configure OpenTelemetry Collector">
    Create a configuration file named `otel-collector-config.yaml`:

    ```bash theme={null}
    receivers:
    otlp:
        protocols:
        grpc:
            endpoint: 0.0.0.0:4317
        http:
            endpoint: 0.0.0.0:4318

    processors:
    batch:
        timeout: 1s
        send_batch_size: 1024
    memory_limiter:
        limit_mib: 512
        check_interval: 1s

    exporters:
    # Export traces to Jaeger via OTLP (using gRPC)
    otlp/jaeger:
        endpoint: jaeger:4317
        tls:
        insecure: true

    # Export metrics to Prometheus
    prometheus:
        endpoint: "0.0.0.0:8889"

    # Debug exporter - logs telemetry data to console
    debug:
        verbosity: detailed
        sampling_initial: 5
        sampling_thereafter: 200

    service:
    pipelines:
        traces:
        receivers: [otlp]
        processors: [memory_limiter, batch]
        exporters: [otlp/jaeger, debug]

        metrics:
        receivers: [otlp]
        processors: [memory_limiter, batch]
        exporters: [prometheus, debug]

    ```
  </Accordion>

  <Accordion title="Step 2: Configure Prometheus">
    Create a file named `prometheus.yml`:

    ```bash theme={null}
    global:
    scrape_interval: 5s
    evaluation_interval: 5s

    scrape_configs:
    - job_name: "otel-collector"
        static_configs:
        - targets: ["otel-collector:8889"]
        scrape_interval: 5s

    - job_name: "prometheus"
        static_configs:
        - targets: ["localhost:9090"]

    ```
  </Accordion>

  <Accordion title="Step 3: Configure Grafana Data Source">
    Provision Grafana with Prometheus as a data source.

    Create `grafana/provisioning/datasources.yaml`:

    ```bash theme={null}
    apiVersion: 1

    datasources:
    - name: Prometheus
        type: prometheus
        access: proxy
        url: http://prometheus:9090
        isDefault: true

    ```
  </Accordion>

  <Accordion title="Step 4: Docker Compose Setup">
    Use the following `docker-compose.yaml` to deploy everything:

    ```bash theme={null}
    version: "3.8"

    services:
    # OpenTelemetry Collector
    otel-collector:
        image: otel/opentelemetry-collector-contrib:0.92.0
        container_name: otel-collector
        command: ["--config=/etc/otel-collector-config.yaml"]
        volumes:
        - ./otel-collector-config.yaml:/etc/otel-collector-config.yaml
        ports:
        - "4317:4317" # OTLP gRPC receiver
        - "4318:4318" # OTLP HTTP receiver
        - "8889:8889" # Prometheus metrics
        depends_on:
        - jaeger
        - prometheus
        networks:
        - observability

    # Jaeger (for traces)
    jaeger:
        image: jaegertracing/all-in-one:latest
        container_name: jaeger
        ports:
        - "16686:16686" # Jaeger UI
        environment:
        - COLLECTOR_OTLP_ENABLED=true
        networks:
        - observability

    # Prometheus (for metrics)
    prometheus:
        image: prom/prometheus:latest
        container_name: prometheus
        ports:
        - "9090:9090"
        volumes:
        - ./prometheus.yml:/etc/prometheus/prometheus.yml
        networks:
        - observability

    # Grafana (for dashboards)
    grafana:
        image: grafana/grafana:latest
        container_name: grafana
        ports:
        - "3000:3000"
        environment:
        - GF_SECURITY_ADMIN_PASSWORD=***** # replace with a secure password
        volumes:
        - grafana-storage:/var/lib/grafana
        - ./grafana/provisioning:/etc/grafana/provisioning
        networks:
        - observability

    volumes:
    grafana-storage:

    networks:
    observability:
        driver: bridge

    ```
  </Accordion>

  <Accordion title="Step 5: Run the Stack">
    Start the observability stack:

    ```bash theme={null}
    docker-compose up -d
    ```

    * **Jaeger UI**: [http://localhost:16686](http://localhost:16686/)
    * **Prometheus**: [http://localhost:9090](http://localhost:9090/)
    * **Grafana**: [http://localhost:3000](http://localhost:3000/)
  </Accordion>

  <Accordion title="Step 6: Connect Hoppscotch">
    From the **Hoppscotch Admin Dashboard**, configure the OpenTelemetry Collector endpoint (**HTTP**).
  </Accordion>
</AccordionGroup>

Once connected, Hoppscotch will begin sending telemetry data, which you can observe in **Jaeger**, **Prometheus**, and **Grafana**.


# Understanding the GraphQL Schema on Hoppscotch
Source: https://docs.hoppscotch.io/guides/articles/understanding-graphql

Learn how to use the GraphQL schema on Hoppscotch.

The GraphQL schema is at the core of any GraphQL server. It defines the capabilities of the API and specifies how clients can access that data. A schema includes types and fields, queries and mutations, interfaces, and unions. Hoppscotch provides you the functionality to connect to a GraphQL server and explore the GraphQL schema.

A GraphQL schema defines types and the fields on those types. This allows clients to ask for exactly what they need and get exactly that - nothing more and nothing less. The schema also defines queries and mutations, which are entry points into the API to read and write data.

The schema is written using the Schema Definition Language (SDL). The SDL provides a way to describe types and fields, as well as queries and mutations. Here is a very simple example of a schema in SDL:

```graphql theme={null}
type Query {
  hello: String
}
```

This schema has one type, Query, and one field on that type, hello. A client could call the hello query to get the String value returned by that field.

The schema sits at the core of any GraphQL server and defines the capabilities of the API. Understanding the structure and components of a GraphQL schema is fundamental to building and using GraphQL APIs.

Hoppscotch's GraphQL API platform provides you with the best experience to test and play around with GraphQL. Once connected to a GraphQL server, you can view the schema by clicking the schema icon on the sidebar.

For example, try connecting to the following server

```
https://echo.hoppscotch.io/graphql
```

You'll see a schema like the one below:

```graphql theme={null}
schema {
  query: Request
}

type Request {
  method: String
  url: String
  headers: [Header]
}

type Header {
  key: String
  value: String
}
```

The schema has the following types `Request` with queries method, URL, and headers. where the header points to another type `Header`.


# Uplifting web experience with Hoppscotch Widgets
Source: https://docs.hoppscotch.io/guides/articles/uplifting-web-experience-with-hoppscotch-widgets

Create and add interactive and dynamic elements to your website using Hoppscotch Widgets.

Widgets are interactive components that can be embedded in HTML pages to enhance
user experience. Hoppscotch offers three types of widgets: links, buttons, and
embeds. These widgets allow you to easily integrate dynamic elements into your
website or project.

## Links

Links are the simplest way to share your Hoppscotch requests. You can create and share
them with others in three formats: raw, HTML, and Markdown.

Use this link to easily share your request with others or include it in
documentation and blogs.

**Example:** [Run in Hoppscotch](https://hopp.sh/r/r0338F6yoJrJ)

## Buttons

Buttons take things up a notch. These can be embedded directly into HTML or
Markdown files, and you can customize them to match your site's look and feel.

Add this button in your project's documentation, website or blogs to provide easy access to
your requests with a simple click.

**Example:**
[![Run in Hoppscotch](https://hopp.sh/badge.svg)](https://hopp.sh/r/r0338F6yoJrJ)

## Embeds

Embeds are the most advanced widgets, allowing you to integrate a mini version
of Hoppscotch right into your HTML page. This lets your audience interact
directly with your API requests. You can also customize how the embed looks and
functions to match your preferences.

**Example:** [See Embed in Action](https://hoppscotch-embed-widget.netlify.app/)

<Tip>
  Customize the width, height, and other attributes of the embed code to fit
  your needs.
</Tip>

## Shared Request

The **Shared Request** feature allows you to create widgets like links, buttons,
and embeds that can be shared with others. When you share a request, it doesn't
give direct access to your actual request; instead, it generates a shareable
link that others can use.

<Warning>
  If a shared request uses environment variables, replace them with actual
  values before sharing to ensure it works correctly.
</Warning>

### How to Access Shared Request

Steps to Create a Shared Request:

1. Click the icon next to the **Save** button and select **"Share Request."**
2. Choose the widget type: **Link**, **Button**, or **Embed**.
3. Click the **"Create"** button to generate the widget.
4. Customize your request as needed in the subsequent **"Customize Request"**
   panel.
5. You can choose different formats like **Raw, HTML, or Markdown** to embed the
   request in your app.

<Tip>
  After selecting the **"Shared Request"** option and clicking the **"Create"**
  button, at the right-hand sidebar, the current request is saved for easy
  access in the **"Shared Requests"** panel.
</Tip>

### How to Manage Shared Request

To view your shared requests:

1. Click on the **"Shared Requests"** icon in the right-hand sidebar.
2. You will see a list of all your shared requests.
3. Click on any request to access it.
4. Right-click or use the three-dot menu on a request to **customize the widget,
   copy the link, edit, or delete** the shared request.


# Introduction
Source: https://docs.hoppscotch.io/guides/getting-started/introduction

Guides and tutorials to help you get started with Hoppscotch.

Hoppscotch is a free and open-source API development platform to help you build, test, and document APIs faster. It is a web-based API development environment that allows you to send requests and view responses in a single interface.

Find articles, guides, and tutorials to help you get started with Hoppscotch.

## Try Hoppscotch

You can try Hoppscotch by visiting [hoppscotch.io](https://hoppscotch.io) and start sending requests to your APIs.

[Learn more](/documentation/getting-started/introduction)

## Features

* History

* Collections

* Environments

* Workspaces

* Code Snippets

* Share Requests

* Visit [documentation tab](/documentation/getting-started/introduction) for full list of features.


# Code of conduct
Source: https://docs.hoppscotch.io/support/code-of-conduct

Code of conduct for Hoppscotch.

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual
identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the overall
  community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or advances of
  any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email address,
  without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
[support@hoppscotch.io](mailto:support@hoppscotch.io).
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series of
actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or permanent
ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within the
community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code\_of\_conduct.html][v2.1].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available at
[https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org

[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html

[Mozilla CoC]: https://github.com/mozilla/diversity

[FAQ]: https://www.contributor-covenant.org/faq

[translations]: https://www.contributor-covenant.org/translations


# Contact
Source: https://docs.hoppscotch.io/support/getting-started/contact

Contact us to get technical support, report a bug, suggest a new feature or improvement, or join our community.

## Technical support

Contact us to book a slot for a private consulting session with our team. We will help you get started with Hoppscotch and answer any questions you may have.

[Talk to experts](/support/solutions/experts)

## Report a bug

If you find a bug, please report it to us by creating a new issue on our [GitHub repository](https://github.com/hoppscotch/hoppscotch).

[Report a bug](https://github.com/hoppscotch/hoppscotch/issues/new?assignees=\&labels=bug%2Cneed+testing\&template=--bug-report.yaml\&title=%5Bbug%5D%3A+)

## Suggest a new feature or improvement

If you have a feature request or an improvement suggestion, please create a new issue on our [GitHub repository](https://github.com/hoppscotch/hoppscotch).

[Request a feature](https://github.com/hoppscotch/hoppscotch/issues/new?assignees=\&labels=feature\&template=--feature-request.yaml\&title=%5Bfeature%5D%3A+)

## Contribute

We are always looking for contributors to help us improve Hoppscotch. If you are interested in contributing, please check out our [contributing guide](/documentation/develop), [code of conduct](https://github.com/hoppscotch/hoppscotch/blob/main/CODE_OF_CONDUCT.md), and our [GitHub repository](https://github.com/hoppscotch/hoppscotch).

## Join our community

Join our [community channels](/support/solutions/community) to get help from our team and other Hoppscotch users. You can also share your feedback and ideas with us. We would love to hear from you.


# Frequently Asked Questions
Source: https://docs.hoppscotch.io/support/getting-started/faq

These are the most frequently asked questions about Hoppscotch.

Find answers to the most frequently asked questions about Hoppscotch.

## General

<AccordionGroup>
  <Accordion title="What is Hoppscotch?">
    Hoppscotch is a free and open-source API development environment that helps you to quickly test and debug APIs. It is a web-based alternative to Postman, Insomnia, and Paw.
  </Accordion>

  <Accordion title="What is the difference between Hoppscotch and Postman/Insomnia/Paw/Httpie?">
    Hoppscotch is a web-based alternative to Postman, Insomnia, and Paw. It is a free and open-source API development environment that helps you to quickly test and debug APIs.
  </Accordion>
</AccordionGroup>

## How-to

<AccordionGroup>
  <Accordion title="How to use Hoppscotch?">
    You can use Hoppscotch by visiting [hoppscotch.io](https://hoppscotch.io) and start making API requests. You can learn more about Hoppscotch by reading our [Getting started](/guides/getting-started/introduction) guide.
  </Accordion>

  <Accordion title="How to install Hoppscotch?">
    You can install Hoppscotch on your desktop by visiting [hoppscotch.io](https://hoppscotch.io) and clicking on the "**Install +**" button. You can also install Hoppscotch on your mobile device by visiting [hoppscotch.io](https://hoppscotch.io) and clicking on the "**Install +**" button.
  </Accordion>

  <Accordion title="How to use Hoppscotch on mobile?">
    We're deprecating mobile support for Hoppscotch. You can still use Hoppscotch on mobile by visiting [hoppscotch.io](https://hoppscotch.io) and clicking on the "**Install +**" button.
  </Accordion>

  <Accordion title="How to use Hoppscotch on a desktop?">
    Download the desktop app from [Downloads page](https://hoppscotch.com/downloads) and install it on your desktop. You can also use Hoppscotch on your desktop by visiting [hoppscotch.io](https://hoppscotch.io) and clicking on the "**Install +**" button to install the [Progressive Web App](/documentation/clients/web).
  </Accordion>
</AccordionGroup>

## Features

<AccordionGroup>
  <Accordion title="What are the features of Hoppscotch?">
    Hoppscotch has a lot of features that you can use to make your API development experience better. You can learn more about Hoppscotch features by reading our [features](/documentation/features) page.
  </Accordion>

  <Accordion title="How does Collections work?">
    Collections are a way to organize your API requests. You can create a collection by clicking on the "Collections" button on the left sidebar. You can learn more about Collections by reading our [Collections guide](/documentation/features/collections).
  </Accordion>

  <Accordion title="How does Environments work?">
    Environments are a way to store variables that you can use in your API requests. You can create an environment by clicking on the "Environments" button on the left sidebar. You can learn more about Environments by reading our [Environments guide](/documentation/features/environments).
  </Accordion>
</AccordionGroup>

## Bugs

<AccordionGroup>
  <Accordion title="How to report a bug?">
    You can report a bug by clicking on the "Report a bug" button on the left sidebar. You can also report a bug by visiting our [GitHub repository](https://github.com/hoppscotch/hoppscotch/issues/new/choose).
  </Accordion>

  <Accordion title="How to report a security vulnerability?">
    You can report a security vulnerability by visiting our [GitHub repository](https://github.com/hoppscotch/hoppscotch/security/policy).
  </Accordion>

  <Accordion title="Localhost is not working">
    If you're using Hoppscotch on your local machine, you might need to enable `CORS`. You can learn more about `CORS` by reading our [Set up guide](/documentation/getting-started/setup#locally-served-apis).
  </Accordion>
</AccordionGroup>

## Support

<AccordionGroup>
  <Accordion title="How to get support?">
    You can get support by visiting our [Support page](/support/solutions/community).
  </Accordion>
</AccordionGroup>


# Introduction
Source: https://docs.hoppscotch.io/support/getting-started/introduction

We're here to help you get started with Hoppscotch.

Discover the different support offers to answer your questions, help you get started, and provide you with the best experience possible.

## Guides

[Guides](/guides/getting-started/introduction) are a great way to get started with Hoppscotch. They are a collection of articles that will help you get started with Hoppscotch.

## FAQ

Read our [Frequently Asked Questions](/support/getting-started/faq) to get answers to the most common questions about Hoppscotch.

## Contact

If you have any questions, feel free to [contact us](/support/getting-started/contact).


# License
Source: https://docs.hoppscotch.io/support/license

Hoppscotch is licensed under MIT License.

```
MIT License

Copyright (c) 2022

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


# Privacy policy
Source: https://docs.hoppscotch.io/support/privacy

Privacy policy for Hoppscotch.

This Privacy Policy describes how Hoppscotch Limited. (“**Hoppscotch**,” “**we**,” “**us**,” or “**our**”) processes personal information that we collect through our digital or online properties or services that link to this Privacy Policy (including as applicable, our website, mobile application, social media pages, marketing activities, and other activities described in this Privacy Policy (collectively, the “**Service**”)).

This Privacy Policy does not apply to information we process on behalf of our business customers while providing them with the Hoppscotch platform/services. Our agreements with such customers govern our use of this information. If you have concerns regarding personal information that we process on behalf of a business customer, please direct your concerns to that enterprise customer.

# **Personal information we collect**

**Information you provide to us.** Personal information you may provide to us through the Service or otherwise includes:

* **Contact data**, such as your first and last name, salutation, email address, billing and mailing addresses, professional title and company name, and phone number.
* **Demographic data**, such as your city, state, country of residence, postal code, and age.
* **Profile data**, such as the username and password that you may set to establish an online account on the Service and any other information that you add to your account profile.
* **Communications data** based on our exchanges with you, including when you contact us through the Service, social media, or otherwise.
* **User-generated content data**, such as photos, images, comments, questions, messages, prompts, works of authorship, and other content or information that you generate, transmit, include in a document, or otherwise make available on the Service, as well as associated metadata. Metadata includes information on how, when, where, and by whom a piece of content was collected and how that content has been formatted or edited. Metadata also includes information that users can add or can have added to their content, such as keywords, geographical or location information, and other similar data.
* **Marketing data**, such as your preferences for receiving our marketing communications and details about your engagement with them.
* **Transactional data**, such as information relating to or needed to complete your orders on or through the Service, including order numbers and transaction history.
* **Payment data** needed to complete transactions, including payment card information or bank account number.
* **Other data** not specifically listed here will be used as described in this Privacy Policy or otherwise disclosed at the time of collection.

**Third-party sources**. We may combine personal information we receive from you with personal information falling within one of the categories identified above that we obtain from other sources, such as:

* **Public sources, such as government agencies, public records, social media platforms, and other publicly available sources.**
* **Data providers, such as information services and data licensors.**
* **Partners, such as marketing partners and event co-sponsors.**
* **Third-party services, such as social media services, that you use to log into, or otherwise link to, your Service account. This data may include your username, profile picture, and other information associated with your account on that third-party service that is made available to us based on your account settings on that service.**

‍\
**Automatic data collection.** We or our service providers may automatically log information about you, your computer or mobile device, and your interaction over time with the Service, our communications, and other online services, such as:

* **Device data**, such as your computer or mobile device's operating system type and version, manufacturer and model, browser type, screen resolution, RAM and disk size, CPU usage, device type (e.g., phone, tablet), IP address, unique identifiers (including identifiers used for advertising purposes), language settings, mobile device carrier, radio/network information (e.g., Wi-Fi, LTE, 3G), and general location information such as city, state or geographic area.
* **Online activity data**, such as pages or screens you viewed, how long you spent on a page or screen, the website you visited before browsing the Service, navigation paths between pages or screens, information about your activity on a page or screen, access times and duration of access, and whether you have opened our emails or clicked links within them.
* **Precise geolocation/Location data** when you authorize (our mobile application/Service) to access your device's location.
* **Communication interaction data** such as your interactions with our email or other communications (e.g., whether you open and/or forward emails) – we may do this through the use of pixel tags (which are also known as clear GIFs), which may be embedded invisibly in our emails.

**Data about others**. We may offer features that help users invite their friends or contacts to use the Service, and we may collect contact details about these invitees so we can deliver their invitations. It's also possible to include information about third parties in your prompts or other information that you upload. Please do not refer someone to us or share their contact details or personal information with us unless you have their permission to do so.

## **Cookies and similar technologies.**

Some of the automatic collection described above is facilitated by the following technologies:

* **Cookies** are small text files that websites store on user devices and that allow web servers to record users' web browsing activities and remember their submissions, preferences, and login status as they navigate a site. Cookies used on our sites include both “session cookies” that are deleted when a session ends, “persistent cookies” that remain longer, “first party” cookies that we place, and “third party” cookies that our third-party business partners and service providers place.
* **Local storage technologies**, like HTML5, provide cookie-equivalent functionality but can store larger amounts of data on your device outside of your browser in connection with specific applications.
* **Chat technologies**, such as those provided by Crisp employ cookies and software code to operate the chat features that you can use to communicate with us through the Service.  Crisp and other third parties may access and use information about webpages visited on our website, your IP address, your general geographic information (e.g., city, state), and other personal information you share through online chats for the purposes described in this Privacy Policy.
* **Session-replay technologies,** such as those provided by PostHog employ software code to record users' interactions with the Services in a manner that allows us to watch video replays of those user sessions. The replays include users' clicks, taps, mouse movements, scrolls, and keystrokes/key touches during those sessions. These replays help us diagnose usability problems and identify areas for improvement. You can learn more about PostHog and how to opt out of session recording by PostHog at [https://posthog.com/privacy](https://posthog.com/privacy).
* **Web beacons**, also known as pixel tags or clear GIFs, are used to demonstrate that a webpage or email was accessed or opened, or that certain content was viewed or clicked.

#

# **How we use your personal information**

We may use your personal information for the following purposes or as otherwise described at the time of collection:

## **Service delivery and operations. We may use your personal information to:**

* provide, operate, and improve the Service and our business;
* establish and maintain your user profile on the Service;
* personalize the Service, including remembering the devices from which you have previously logged in and remembering your selections and preferences as you navigate the Service;
* communicate with you about the Service, including by sending Service-related announcements, security alerts, and support and administrative messages;
* enable security features of the Service;

**Service improvement and analytics.** We may use your personal information to analyze your usage of the Service, improve the Service and our business, help us understand user activity on the Service, including which pages are most and least visited and how visitors move around the Service, as well as user interactions with our emails, and to develop new products and services.

**Marketing and advertising.** We and our service providers may collect and use your personal information for the following purposes:

* **Direct marketing. We may send you direct marketing communications and may personalize these messages based on your needs and interests. You may opt out of our marketing communications as described in the Opt-out of Marketing section below.**
* **Interest-based advertising.** We and our third-party advertising partners may use cookies and other technologies to collect information about your interaction (including the data described in the automatic data collection section above) with the Service, our communications, and other online services over time, and use that information to serve online ads that they think will interest you. This is called interest-based advertising. We may also share information about our users with these companies to facilitate interest-based advertising to those or similar users on other online platforms. You can learn more about your choices for limiting interest-based advertising in Your choices.

##

## **Compliance and protection. We may use your personal information to:**

* comply with applicable laws, lawful requests, and legal processes, such as responding to subpoenas, investigations, or requests from government authorities;
* protect our, your or others' rights, privacy, safety, or property (including by making and defending legal claims);
* audit our internal processes for compliance with legal and contractual requirements or our internal policies;
* enforce the terms and conditions that govern the Service; and
* Prevent, identify, investigate, and deter fraudulent, harmful, unauthorized, unethical, or illegal activity, including cyberattacks and identity theft.

**To create aggregated, de-identified, and/or anonymized data.** We may create aggregated, de-identified, and/or anonymized data from your personal information and other individuals whose personal information we collect. We make personal information into de-identified and/or anonymized data by removing information that makes the data identifiable to you. We may use this aggregated, de-identified, and/or anonymized data and share it with third parties for our lawful business purposes, including to analyze and improve the Service and promote our business.

**With your consent.** In some cases, we may specifically ask for your consent to collect, use, or share your personal information, such as when required by law.

**Cookies and similar technologies.** In addition to the other uses included in this section, we may use the Cookies and similar technologies described above for the following purposes:

* **Technical operation**. To allow the technical operation of the Service, such as by remembering your selections and preferences as you navigate the site.
* **Functionality**. To enhance the performance and functionality of our services.
* **Analytics**. To help us understand user activity on the Service, including which pages are most and least visited and how visitors move around the Service, as well as user interactions with our emails. For example, we use Google Analytics and PostHog for this purpose. You can learn more about Google Analytics and how to prevent the use of Google Analytics relating to your use of our sites here: [https://tools.google.com/dlpage/gaoptout?hl=en](https://tools.google.com/dlpage/gaoptout?hl=en). You can learn more about PostHog and how to prevent the use of PostHog Analytics relating to your use of our sites here: [https://posthog.com/privacy](https://posthog.com/privacy).

#

# **How we share your personal information**

We may share your personal information with the following parties and as otherwise described in this Privacy Policy, in other applicable notices, or at the time of collection.

**Affiliates.** Our corporate parent, subsidiaries, and affiliates.

**Service providers.** Third parties that provide services on our behalf or help us operate the Service or our business (such as hosting, information technology, customer support, online chat functionality providers, email delivery, marketing, consumer research, and website analytics).

**Payment processors.** Any payment card information you use to purchase the Service is collected and processed directly by our payment processors such as Stripe. Stripe may use your payment data through its privacy policy, [https://stripe.com/privacy](https://stripe.com/privacy).

**Third parties designated by you.** We may share your personal information with third parties where you have instructed us or provided your consent to do so.

**Partners.** We may share your personal information with business partners to provide you with a product or service you have requested.

**Artificial Intelligence Partners.** We partner with OpenAI, the creators of GPT-4o mini, to offer you enhanced API development and testing capabilities. In doing so, we may share the user-generated information you include in your prompts and APIs to generate content and provide enhanced AI capabilities. OpenAI may use your data by its privacy policy, [https://openai.com/policies/privacy-policy](https://openai.com/policies/privacy-policy).

**Professional advisors.** Professional advisors, such as lawyers, auditors, bankers, and insurers, where necessary in the course of the professional services that they render to us.

**Authorities and others.** Law enforcement, government authorities, and private parties, as we believe in good faith are necessary or appropriate for the Compliance and protection purposes described above.

**Business transferees**. We may disclose personal information in the context of actual or prospective business transactions (*e.g.,* investments in Hoppscotch, financing of Hoppscotch, public stock offerings, or the sale, transfer, or merger of all or part of our business, assets, or shares), for example, we may need to share certain personal information with prospective counterparties and their advisers. We may also disclose your personal information to an acquirer, successor, or assignee of Hoppscotch as part of any merger, acquisition, sale of assets, or similar transaction, and/or in the event of an insolvency, bankruptcy, or receivership in which personal information is transferred to one or more third parties as one of our business assets.

# **Your choices**

**Access or update your information.** If you have registered for an account with us through the Service, you may review and update certain account information by logging into the account.

**Opt-out of communications.** You may opt out of marketing-related emails by following the opt-out or unsubscribe instructions at the bottom of the email, or by contacting us. Please note that if you choose to opt out of marketing-related emails, you may continue to receive service-related and other non-marketing emails.

**Cookies and other technologies**. Most browsers let you remove or reject cookies. To do this, follow the instructions in your browser settings. Many browsers accept cookies by default until you change your settings. Please note that if you set your browser to disable cookies, the Service may not work properly. For more information about cookies, including how to see what cookies have been set on your browser and how to manage and delete them, visit [www.allaboutcookies.org](http://www.allaboutcookies.org). You can also configure your device to prevent images from loading to prevent web beacons from functioning.

**Blocking images/clear gifs:** Most browsers and devices allow you to configure your device to prevent images from loading. To do this, follow the instructions in your particular browser or device settings.

**Advertising choices.** You may be able to limit the use of your information for interest-based advertising through the following settings/options/tools:

* **Browser settings.** Changing your internet web browser settings to block third-party cookies.

* **Privacy browsers/plug-ins.** Using privacy browsers and/or ad-blocking browser plug-ins that let you block tracking technologies.

* **Platform settings.** Certain platforms offer opt-out features that let you opt out of the use of your information for interest-based advertising. For example, you may be able to exercise that option for Google and Facebook, respectively, at the following websites:

* Google: [https://adssettings.google.com/](https://adssettings.google.com/)

* Facebook: [https://www.facebook.com/about/ads](https://www.facebook.com/about/ads)

* **Ad industry tools.** Opting out of interest-based ads from companies that participate in the following industry opt-out programs:

* Network Advertising Initiative: [http://www.networkadvertising.org/managing/opt\\\_out.asp](http://www.networkadvertising.org/managing/opt\\_out.asp)

* Digital Advertising Alliance: [http://optout.aboutads.info](http://optout.aboutads.info).

* AppChoices mobile app, available at [http://www.youradchoices.com/appchoices](http://www.youradchoices.com/appchoices), will allow you to opt out of interest-based ads in mobile apps served by participating members of the Digital Advertising Alliance.

* **Mobile settings.** Use your mobile device settings to limit the use of the advertising ID associated with your mobile device for interest-based advertising purposes.

You will need to apply these opt-out settings on each device and browser from which you wish to limit the use of your information for interest-based advertising purposes.

We cannot offer any assurances as to whether the companies we work with participate in the opt-out programs described above.

**Do Not Track.** Some Internet browsers may be configured to send “Do Not Track” signals to the online services that you visit. We currently do not respond to “Do Not Track” signals. To find out more about “Do Not Track,” please visit [http://www.allaboutdnt.com](http://www.allaboutdnt.com).

**Declining to provide information.** We may need to collect personal information to provide certain services. If you do not provide the information we identify as required or mandatory, we may not be able to provide those services.\
‍

# **Other sites and services**

The Service may contain links to websites, mobile applications, and other online services operated by third parties. In addition, our content may be integrated into web pages or other online services that are not associated with us. These links and integrations are not an endorsement of or representation that we are affiliated with, any third party. We do not control websites, mobile applications, or online services operated by third parties, and we are not responsible for their actions. We encourage you to read the privacy policies of the other websites, mobile applications, and online services you use.

# **Security**

We employ several technical, organizational, and physical safeguards designed to protect the personal information we collect. However, security risk is inherent in all internet and information technologies and we cannot guarantee the security of your personal information.

# **International data transfer**

We are headquartered in the United States and may use service providers that operate in other countries. Your personal information may be transferred to the United States or other locations where privacy laws may not be as protective as those in your state, province, or country.

# **Children**

The Service is not intended for use by anyone under 18 years of age. If you are a parent or guardian of a child from whom you believe we have collected personal information in a manner prohibited by law, please contact us. If we learn that we have collected personal information through the Service from a child without the consent of the child's parent or guardian as required by law, we will comply with applicable legal requirements to delete the information.

# **Changes to this Privacy Policy**

We reserve the right to modify this Privacy Policy at any time. If we make material changes to this Privacy Policy, we will notify you by updating the date of this Privacy Policy and posting it on the Service or other appropriate means. Any modifications to this Privacy Policy will be effective upon our posting the modified version (or as otherwise indicated at the time of posting). In all cases, your use of the Service after the effective date of any modified Privacy Policy indicates your acknowledging that the modified Privacy Policy applies to your interactions with the Service and our business.

# **How to contact us**

* **Email**: [support@hoppscotch.io](mailto:support@hoppscotch.io)


# Security policy
Source: https://docs.hoppscotch.io/support/security-policy

Security procedures and general policies for Hoppscotch.

This document outlines security procedures and general policies for the Hoppscotch project.

* [Security Policy](#security-policy)
  * [Reporting a security vulnerability](#reporting-a-security-vulnerability)
  * [Incident response process](#incident-response-process)

## Reporting a security vulnerability

Report security vulnerabilities by emailing the Hoppscotch Support team at [support@hoppscotch.io](mailto:support@hoppscotch.io).

The primary security point of contact from Hoppscotch Support team will acknowledge your email within 48 hours, and will send a more detailed response within 48 hours indicating the next steps in handling your report. After the initial reply to your report, the security team will endeavor to keep you informed of the progress towards a fix and full announcement, and may ask for additional information or guidance.

**Do not create a GitHub issue ticket to report a security vulnerability.**

The Hoppscotch team and community take all security vulnerability reports in Hoppscotch seriously. Thank you for improving the security of Hoppscotch. We appreciate your efforts and responsible disclosure and will make every effort to acknowledge your contributions.

Report security bugs in third-party modules to the person or team maintaining the module.

## Incident response process

In case an incident is discovered or reported, we will follow the following  process to contain, respond, and remediate:

1. Confirm the problem and determine the affected versions.
2. Audit code to find any potential similar problems.
3. Prepare fixes for all releases still under maintenance. These fixes will be deployed as fast as possible to production.


# Community
Source: https://docs.hoppscotch.io/support/solutions/community

Hoppscotch is an open-source project. Community is at the heart of everything we do.

## GitHub Issues

If you have a bug to report or a feature request, please [open an issue](https://github.com/hoppscotch/hoppscotch/issues/new/choose) on our GitHub repository. We will try to respond to your issue as soon as possible.

## GitHub Discussion

Our active community is comprised of more than 2,000 contributors. Asking your questions on our [GitHub Discussion](https://github.com/hoppscotch/hoppscotch/discussions) board is a free and efficient way to ensure that you find solutions to your problems.

## Discord

Our [Discord server](https://hoppscotch.io/discord) is a good place to have real-time exchanges with members of the community. You can ask questions, get help, and discuss the future of Hoppscotch. Join our Discord server to get started.

## Other platforms

We are also present on other platforms such as [X](https://hoppscotch.io/twitter), StackOverflow, and Reddit. You can follow us on these platforms to get the latest updates about Hoppscotch.


# Hoppscotch Experts
Source: https://docs.hoppscotch.io/support/solutions/experts

Get help from our experts.

Our expert network is a group of experienced engineers with expertise in Hoppscotch, carefully selected by the Hoppscotch team. They are available to help you with your questions and issues.

They act as an external workforce for the Hoppscotch team and are qualified to take on any consulting mission on behalf of the Hoppscotch team, such as:

* Consultation
* Technical support
* Self-Hosting

## Quote

Contact us at `support@hoppscotch.io` for a quote.

## Join experts network

If you are an experienced engineer with expertise in Hoppscotch, you can join our experts network. Contact us at `support@hoppscotch.io` for more details.


# Terms and conditions
Source: https://docs.hoppscotch.io/support/terms

Terms and conditions for Hoppscotch.

Hoppscotch Limited is committed to ensuring that the app is as useful and efficient as possible. For that reason, we reserve the right to make changes to the app or to charge for its services at any time and for any reason. We will not charge you for the app or its services without making it clear to you exactly what you're paying for.

Please note that there are certain things that Hoppscotch Limited will not take responsibility for. Certain functions of the app will require an active internet connection. The connection can be Wi-Fi or provided by your mobile network provider, but Hoppscotch Limited cannot take responsibility if the app doesn't work at full functionality due to a lack of Wi-Fi or data allowance.

If you use the app outside an area with Wi-Fi, your terms of agreement with your mobile network provider will still apply. As a result, you may be charged by your mobile provider for the cost of data for the duration of the connection while accessing the app, or other third-party charges. By using the app, you're accepting responsibility for any such charges, including roaming data charges if you use the app outside of your home territory (i.e., region or country) without turning off data roaming. If you're not the bill payer for the device on which you're using the app, please be aware that we assume that you have received permission from the bill payer to use the app.

Along the same lines, Hoppscotch Limited cannot always take responsibility for the way you use the app, such as ensuring that your device stays charged. If your device runs out of battery and you can't turn it on to avail of the service, Hoppscotch Limited cannot accept responsibility.

Concerning Hoppscotch Limited's responsibility for your use of the app, it's important to bear in mind that although we endeavor to ensure that it is updated and correct at all times, we do rely on third parties to provide information to us so that we can make it available to you. Hoppscotch Limited accepts no liability for any loss, direct or indirect, you experience as a result of relying solely on the functionality of the app.

At some point, we may wish to update the app. The app is currently available on the web and CLI – the requirements for both systems (and for any additional systems we decide to extend the availability of the app to) may change, and you'll need to download the updates if you want to keep using the app. Hoppscotch Limited does not promise that it will always update the app so that it is relevant to you and/or works with the web & CLI version that you have installed on your device. However, you promise to accept updates to the application when offered to you. We may also wish to stop providing the app and terminate its use at any time without giving notice of termination to you. Unless we tell you otherwise, upon any termination, (a) the rights and licenses granted to you in these terms will end; (b) you must stop using the app, and (if needed) delete it from your device.

## Changes to these terms and conditions

We may update our terms and conditions from time to time. Thus, you are advised to review this page periodically for any changes. We will notify you of any changes by posting the new terms and conditions on this page.

These terms and conditions are effective as of 2023-04-08.

## Contact us

If you have any questions or suggestions about our terms and conditions, please do not hesitate to contact us at `support@hoppscotch.io`.


