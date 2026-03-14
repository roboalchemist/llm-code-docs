# Source: https://developers.make.com/custom-apps-documentation/app-review/prerequisites.md

# Prerequisites

When you want to make your custom app public and share it with all Make users, your app has to conform to Make standards. Following Make app development standards is a prerequisite to get an app review. Make app standards encompass:

* [Custom app functionality](#custom-app-functionality)
* [Custom app code best practices](#custom-app-code)
* [Testing your custom app with test scenarios](#testing-your-custom-app)

Review the following sections to learn more about each prerequisite.

## Custom app functionality

In Make, we develop apps to provide value to our users. Your custom app should use a service that Make doesn't integrate yet. All apps in Make require from the user only credentials that are necessary to create a connection to the service API. If you want to make your custom app public, your app functionality has to follow the same principles:

* Your custom app uses a web service that is not already available in Make.
* Your custom app and its modules have to connect to a web service API. Avoid duplicating the same functionality as iterators, aggregators, or other tools in Make.
* Avoid using APIs that have strong dependencies on other APIs, or APIs that function as redirects to other APIs.
* Avoid using APIs that don't have their own domain, or have their domain associated with service platforms like Heroku or AWS.
* Your custom app has to use only credentials that the service requires to create a connection. Don't request any additional credentials from the user.
* If your custom app is a scraper app, it can't include the name of a third-party service in your app or module names.

## Custom app code

When developing a custom app in Make, you should first go through our [Best Practices guide](https://developers.make.com/custom-apps-documentation/best-practices/overview) and apply them to your code. By following our best practices, you will ensure that the review and publication process of your app is as smooth as possible.

Before sending an app for review, check that:

* The base and connection have [sanitization](https://developers.make.com/custom-apps-documentation/app-components/base/sanitization) of sensitive data, e. g. API key or token.
* The base and connection have [error handling](https://developers.make.com/custom-apps-documentation/app-components/base/error-handling).
* The [base](https://developers.make.com/custom-apps-documentation/app-components/base) and connection use an endpoint in the app's API.
* The connection is [using a correct URL](https://developers.make.com/custom-apps-documentation/best-practices/connections). If the user uses incorrect credentials, they get an error.
* Modules have correct [labels](https://developers.make.com/custom-apps-documentation/best-practices/naming-conventions/modules/module-labels) and [descriptions](https://developers.make.com/custom-apps-documentation/best-practices/naming-conventions/modules/module-descriptions).
* The app has a [universal module](https://developers.make.com/custom-apps-documentation/app-components/modules/universal-module).
* All modules have the [correct interface](https://developers.make.com/custom-apps-documentation/best-practices/output-parameters/interface) depending on the output from the module.
* All dates are formatted or parsed in the [mappable parameters](https://developers.make.com/custom-apps-documentation/best-practices/modules/search-modules) and [interface](https://developers.make.com/custom-apps-documentation/best-practices/output-parameters/interface).
* Search modules, trigger modules, and [RPCs](https://developers.make.com/custom-apps-documentation/best-practices/remote-procedure-calls#pagination-and-limits) have a `limit` [parameter](https://developers.make.com/custom-apps-documentation/best-practices/modules/search-modules).
* Search modules, trigger modules, and RPCs have [pagination](https://developers.make.com/custom-apps-documentation/component-blocks/api/pagination) if it's supported in the service API.

{% hint style="warning" %}
The items above are mandatory for each app.
{% endhint %}

## Testing your custom app

After you check the code of your custom app, you must create test scenarios to show that the custom app works. Use each module of the custom app in at least one test scenario.

{% hint style="warning" %}
Make sure that the testing scenarios and their execution logs don't contain personal or sensitive data.
{% endhint %}

### Best practices for test scenarios

* Do not use scenarios with another app's webhook.
* Try to put all of the app's modules in one scenario and run the scenario without errors. Connect the app modules based on the object the modules work with or the action the modules perform.\
  For example, **Create a Task** > **Create a Subtask** (in order to create a subtask, the task has to be created first).

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-e31fa24632aec8e45b071cd9b4fafd4dfedba55a%2FScreen%20Shot%202022-08-29%20at%2019.25.52.png?alt=media" alt="" width="563"><figcaption><p>Example of a test scenario</p></figcaption></figure>

* Put the search and list modules at the end of separate scenario routes to avoid multiple runs of the subsequent modules.
* Run your search and list modules to have logs with pagination. If you don't know how to test pagination, [follow the steps here](https://developers.make.com/custom-apps-documentation/debug-your-app/debugging-of-pagination-in-list-search-modules).
* Create a separate scenario that produces an error message. Run the scenario to get an error:

<div align="center"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-626f671bd03f8c11264de0fab99aa2209d388143%2Ferror_example.png?alt=media" alt="" width="563"><figcaption><p>Example of an error</p></figcaption></figure></div>

Run the test scenarios right before you request the custom app review and every time you fix issues. The scenario execution logs have a data retention limit and the reviewer won't be able to access old logs.
