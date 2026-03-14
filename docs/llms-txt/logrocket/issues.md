# Source: https://docs.logrocket.com/docs/issues.md

# Issues

Intelligently grouped problems impacting your users

## Overview

The Issues page enables users to review all their frontend issues in one place and prioritize and learn more about the issues that are actually affecting the customer experience.

Currently, LogRocket's available issue types are Errors, Network Errors, Rage Clicks, Dead Clicks, Frustrating Network Requests, Error States, and Mobile Crashes, with more issue types planned in the future. You can toggle between these types or choose to view all with the dropdown in the upper righthand corner of the page.

### Issue Types

* **Errors** - JavaScript (client-side), iOS, and Android errors. These errors may or may not directly impact the UI.
* **Network Errors** - Failed network requests and GraphQL errors. These errors may or may not directly impact the UI.
* **Rage Clicks** - Occur when a user clicks repeatedly in frustration on an element.
* **Dead Clicks** - Occur when a user clicks on an interactive element (button, link, etc), but the click had no visible effect (ie. a DOM change).
* **Frustrating Network Requests** - Compound events where a user shows impatient mouse actions during a particularly long network request.
* **Error States** - Triggered by the occurrence of Element Visible Definitions that are designated as "error states".
* **Mobile Crashes** - Occur when an iOS or Android app crashes.

Issues are retained for 1 month from the last instance of an issue. So if an issue stops occurring, it is available for 1 month after the last time it occurs. Issues retention is independent of an organization's session retention.

> 📘 Pro & Enterprise plan issue types
>
> Network Error, Rage Click, Dead Click, Frustrating Network Request, Error State, and Mobile Crash issues are available for Pro and Enterprise plan customers only.

## Severe Issues via Galileo AI

See the [Severe Issues doc](https://docs.logrocket.com/docs/severe-issues) to learn more about AI-recommended issues based on detection of significant user impact, with natural language descriptions.

## Issues filters

Issues filters give users the ability to narrow the Issues list down to a specific subset of Issues more meaningful to their needs. Filters include:

* [Issue Type](https://docs.logrocket.com/docs/issues#issue-types)
* Time Range
* [Severity](https://docs.logrocket.com/docs/severe-issues)
* First Detected (in time range)
* Page Definition / URL
* [Triage Status](https://docs.logrocket.com/docs/issues#triage-status)
* [Platform](https://docs.logrocket.com/docs/issues#platform-filter)
* Issue Title

<Image align="center" alt="Issues filters" border={true} caption="Issues filters" src="https://files.readme.io/17aefd5423dd9127d231f181a3d5037b24035a5faee3a1ed58fb292b22880c13-Issues_Filters.png" />

## Issues Tabs

Users often have several groups of filters they go back to over and over again. To make this workflow easy, Issues have Tabs that let you save and name the groups of Issues filters that mean the most to you and your team. Issues comes pre-loaded with several Issues Tabs to get you started:

<Image align="center" alt="Saved Issues filters" border={true} caption="Issues Tabs" src="https://files.readme.io/8119013ddfc8a194e35ae44fb8da4700eb2753426f37e2f6040de32916fc428a-Issue_Tabs.png" />

## Issues list

Below the Issues filters, you'll see a list of Issues from across your application, along with metadata about each issue.

<Image align="center" alt="single issue" border={true} caption="Issues list view" src="https://files.readme.io/4a8991ce0c8dcfe18f490d21a7d0662e931abe1b91dad2ec7c3799cd0d2c83f0-Issues_List.png" />

To the right of the issue title, you'll see the triage status of the issue, as well as a frequency histogram of its occurrences. At the end of the row, you'll see some additional metadata, including the number of sessions the specific issue has affected.

### Card View

Screenshots can be see in the Card view of Issues. Toggle to "Card" in the top right corner of the Issues list.

<Image align="center" alt="Issues Card view" border={true} caption="Issues Card view" src="https://files.readme.io/1519e62b807264c06fb9faec1106f20f6945f793cd88ac3349a2bd26a5be25f0-Issues_Card_View.png" />

## Triage status

Triage status gives users the ability to categorize, with discretion, the impact of issues. The triage statuses are "Untriaged", "High Impact", "Low Impact", and "Ignored". To filter the list to issues of a specific triage status, click "Add Filter" in the Issues filters section and click "Triage Status". From here you can select one or more of the statuses to view.

<Image align="center" alt="Triage status filter" border={true} caption="Triage status filter" src="https://files.readme.io/9a328691db016595fcbfd6b2dce46a75984eff14d8828eae6a739f6ddffdc617-Triage_status.png" />

## Grouping issues

In order to categorize an issue directly from here, click the dropdown labeled **Untriaged** in the issue row and select whether the issue is High impact, Low impact, or should be Ignored completely.

<Image align="center" alt="triage status modal" border={true} caption="Issue triaging popover" title="Screenshot 2023-01-09 at 10.05.14 AM.png" src="https://files.readme.io/1d640c2b51b535f8d972056e5632260783efff3527b69c43dbc1cc987420b6de-Grouping_issues_1.png" />

You can also choose to open the **Configure Issue** modal. This allows you to assign the issue a custom name and also add custom rules to group issues together and assign them the same status. Setting custom issue group conditions can be done for Errors, Network Errors, and Frustrating Requests.

<Image align="center" alt="Configure network error issue" border={false} caption="Configure Issue modal for updating impact score and issue grouping conditions" title="Screenshot 2023-01-09 at 10.05.52 AM.png" src="https://files.readme.io/b6ea1d134f4b2d34f707ee5f25e6027ada1a939987acb81ba62597cb5d31aefb-Grouping_issues_2.png" />

Any new issues that arise within your application and match any of these rules will be auto-categorized into the selected status.

You can also categorize and group issues directly from their **Issue Detail** page.

> 📘 Grouping issues must be of the same type
>
> Please note that you can currently only group issues of the same type.  For example, you can create groups that contain different types of JavaScript exceptions as well as groups that bundle different types of Network Errors, but you cannot create a group containing both of these types.

## Error State Issue Type

The Error State issue type groups instances where users receive a message indicating that something went wrong. This can include error pages, modals, or views. Error States are defined by the user for the each project in Definitions.

To enable Error State issues, on the Issues view click the Issue Types filter and click "Setup" next to the "Error States" option.

A Definitions side modal will open. Click "Add Definition" and create new "Element visible" definitions with the "Use as Error State" checkbox checked.

<Image align="center" alt={1080} border={false} caption="Chart failed to load error state, element visible definition" title="Screen Shot 2022-08-02 at 4.58.30 PM.png" src="https://files.readme.io/9598430390928a8da367a7f7d2224e4f4b885d650198824788a9cad54c8df1d6-Error_State_Issue_Type.png" />

As you create these definitions, error state issues will begin to be recorded in LogRocket. Note: Element visible definitions are non-retroactive, meaning they will record events after being defined, but will not look back in time before their creation date. This means that once Error State definitions have been created, new Error State issues will start appearing from that point on, so you may need to check back in a few hours after creation to see the error states that users have hit.

> 📘 Quickstart: Start out with default error state definitions
>
> The quickest way to get started with Error State issues is to let LogRocket create them for you!
>
> Check out the [Default Error State Definitions doc](https://docs.logrocket.com/docs/definitions#default-error-state-definitions) to see how to bootstrap default error state definitions.

## Page Definitions / URL filter

In order to see issues that only occurred in specific areas of your app, use the "Page Definitions / URL" filter. Once Page Definitions are selected, issues listed will be ones that have occurred within those Page Definitions (on those specific URLs) in your app.

[Definitions](https://docs.logrocket.com/docs/definitions) (using the "Visited URL" filter) are a shared feature of LogRocket and can be found in the main navigation. To add Definitions, either click the definitions icon to the right of the "URL / Mobile Page" input within the Page Definition / URL modal, or [go to the "Definitions" page](https://app.logrocket.com/r/definitions) and add new Page Definitions.

<Image align="center" alt={685} border={true} caption="Definitions filter for Issues" title="Screenshot 2023-01-12 at 10.18.50 AM.png" src="https://files.readme.io/736c947fd69dc959824fe113a77390b370cf5c5df4a8079e9342723d5c315abc-Page_Definitions___URL_filter.png" />

## First Detected filter

By default, issues listed have occurred any time within the selected time range. You can use the First Detected filter to identify issues that have occurred for the first time within the selected time range, but may have continued occurring afterwards. Note that the 1 month issues retention also applies to the First Detected filter, so the first occurrence of an issue is based on events within the past month.

<Image align="center" alt="First seen filter for Issues" border={true} caption="First seen filter for Issues" src="https://files.readme.io/a4b3766ab8dd255eeaf2b83fddcc8aea6754234d0145410d37afe9e13ad1fbd6-first-detected-issues-filter.png" />

## Platform filter

Each issue is comprised of events from a single platform - Browser, iOS, or Android. The Platform filter allows you narrow the scope of Issues to one of these platforms. Since React Native compiles to native code, apps that use the React Native SDK will find issues in the iOS and Android platforms.

<Image align="center" alt="Platform filter for Issues: Browser, iOS, and Android" border={true} caption="Platform filter for Issues: Browser, iOS, and Android" src="https://files.readme.io/f37d0b37eaab8915688afd8fe7c24a5feeb5abc750f45685183c514946ce4323-Platform_filter.png" />

## Issue Detail page

You can click through on an individual issue to view more detailed information about the issue, including a sample playback of a user encountering the issue within a session. This is designed to give you information to help you categorize the priority of the issue. For example, issues that block users within a critical sign-up or checkout flow may be deemed higher-priority than issues that occur silently with no real user impact.

<Image align="center" border={true} src="https://files.readme.io/47084d275f147abf8d534a8e97cfa43fc260607b8a497cf5d2af254470a2d198-Issue_Detail_page.png" className="border" />

Below the playback is additional information related to the error. This includes stack traces if you have provided us with [sourcemaps](/docs/stacktraces), and request and response information if the issue type is a network error.

The list to the left of the session playback shows the metadata associated with the specific session playback.

The 2nd tab, "Breakdown", reveals cumulative information about the issue, such as frequency of occurrence, most common browser, and number of users and sessions impacted.

### Issue Analyzer

<Callout icon="🚧" theme="warn">
  Issue Analyzer is currently in Beta
</Callout>

Issue Analyzer is a Galileo AI-powered feature that automatically analyzes your issues to save you time and provide deeper insights into user impact and root causes. Instead of manually reviewing multiple session replays to understand an issue's true impact, Issue Analyzer does this work for you by intelligently analyzing patterns across all related sessions.

<Image align="center" alt="Issue Analyzer report" border={true} src="https://files.readme.io/5069afe8c57e8c9eb68afab723ec00f73ca9ee4e7f1ba32c653003560a920d5a-issue-analyzer-report.png" className="border" />

#### What Issue Analyzer Does

Issue Analyzer automatically:

* **Analyzes user impact**: Determines whether the issue actually affects the user experience or occurs silently in the background
* **Identifies root causes**: Examines session replays to pinpoint the underlying cause of the issue
* **Provides severity assessment**: Evaluates how critical the issue is based on user behavior and outcomes
* **Suggests next steps**: Recommends specific areas for further investigation or immediate action (when available)

#### Key Benefits

* **Time savings**: Eliminates the need to manually review dozens of session replays to understand issue impact
* **Consistent analysis**: Provides objective assessment across all issues, removing guesswork from prioritization
* **Actionable insights**: Delivers specific, actionable recommendations rather than just identifying problems
* **Better prioritization**: Helps teams focus on issues that genuinely impact user experience

#### Availability

Currently available to all Pro/Enterprise customers. Look for the "Analysis" tab in the Issue Details view:

<Image align="center" alt="Issue Analyzer empty state" border={true} src="https://files.readme.io/980d527a9903cb42df6369d335c8c62897e2f78a67ead2d613c0a873c0fa8894-issue-analyzer-empty.png" className="border" />

<br />

## URL Grouping Configurations

Network Errors and Frustrating Network Request issue types have optional URL grouping configurations that can be adjusted in the Issues Settings view. This provides better visibility into the scope of issues in apps with subdomains or domain extensions that represent the same basic experience.

<Image align="center" border={true} caption="URL Grouping configs in Issues Settings" src="https://files.readme.io/95e46db9033aad9c6c9b0403880bf74302b30edc5245025673be8e6a35718c06-issue-settings.png" />

**Exclude URL Subdomains** should be enabled when an API's multiple subdomains represent the same basic API. For example, for apps that use account keys as subdomains, like `customer1.app.com/foo/bar` and `customer2.app.com/foo/bar`. This will group across subdomains: `*.app.com/foo/bar` for Network Errors and Frustrating Network Requests issues.

**Exclude URL Domain Extensions** should be enabled when an API uses multiple domain extensions that all represent the same basic API, such as `app.com/foo/bar` and `app.co.uk/foo/bar`.  This will group across domain extensions: `app.*/foo/bar` for Network Errors and Frustrating Network Requests issues.

## High-Volume Boost

For customers with >1M monthly sessions, enabling High-Volume Boost for Issues will increase the speed at which Issues load across the app. This configuration intelligently queries Issues in an optimized way especially tuned for customers who have higher counts of issue events. Note: this configuration is not recommended for users with \<1M monthly sessions.

<Image align="center" border={true} caption="Issues setting for High-Volume Boost" src="https://files.readme.io/7002ea0105fa9832c993db3ade16d13c3eedb7e98ac7be5359504c48a74c952e-high-volume-boost.png" />