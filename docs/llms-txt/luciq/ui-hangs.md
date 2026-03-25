# Source: https://docs.luciq.ai/references/application-performance-monitoring/ui-hangs.md

# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/application-performance-monitoring/ui-hangs.md

# UI Hangs

Luciq automatically captures any UI hangs happening in your app. A hang is when the app isn't responding to the user's input for more than **250 ms**.

The SDK automatically groups and aggregates data based on the **screen name**, which is the name of your `UIViewController` class. A visit starts when your `viewDidAppear` is called and ends when `viewWillDisapear` is called. Screen visits are referred to as Auto UI Traces. You can create Custom UI Traces as explained [here](https://app.gitbook.com/s/AM8wNfllcup3GnWJ1WtW/setup-luciq-for-ios/setup-application-performance-monitoring/setup-screen-rendering/custom-ui-traces).

For every screen visit, the SDK reports the duration percentage during which the user encountered UI hangs. Let's take an example:

* A user visits your home screen and stays there for 10000 ms.
* During this screen visit, they encountered three hang incidents. The first one lasted 250 ms, the second one lasted 300 ms, and the last one lasted 400 ms. The cumulative hang duration for this screen visit is `250+300+400=950 ms`. That means the hang % is `950 / 10000 = 9.5%`.

***

### Custom UI Traces

In case you are looking for more control over how occurrences are grouped, you can create your own groups with custom names by leveraging the relevant start and stop APIs. It is worth mentioning that:

* You can run only **one** custom UI trace at a given time; a trace must be ended before a new one can be started.
* The SDK will end any occurrence that wasn't explicitly ended via the end API.

***

### UI Hangs Apdex

Luciq calculates an apdex score for any UI trace in your app, whether it is an automatically detected screen or a custom UI trace that you defined. Apdex score ranges between 0 and 1. The higher the value, the closer you are to satisfying a user experience:

* Apdex score ≥ 0.94 equates to **Excellent** performance.
* Apdex score ≥ 0.85 and < 0.94 equates to **Good** performance.
* Apdex score ≥ 0.7 and < 0.85 equates to **Fair** performance.
* Apdex score ≥ 0.5 and < 0.7 equates to **Poor** performance.
* Apdex score < 0.5 is considered **Unacceptable**.

#### How Is the UI Trace Apdex Calculated?

When a screen visit or custom UI trace occurrence is collected, it is flagged as follows:

* **Satisfying:** if its hang% ≤ 2%
* **Tolerable:** if its hang% > 2 and ≤ 5%
* **Frustrating:** its hang% > 5%

Then, based on the bucketing explained above, the apdex is calculated:

* `Total occurrences = Satisfying occurrences + Tolerable occurrences + Frustrating occurrences`
* `Apdex score = (Satisfying occurrences + 0.5 * Tolerable occurrences) / Total occurrences`
