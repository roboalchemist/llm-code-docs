# Source: https://docs.logrocket.com/docs/logrocket-filters.md

# Filters

Detailed explanation for all LogRocket filters

LogRocket has many powerful filters that allow you to filter over sessions with a wide variety of properties. Filters labeled with *Pro* are available through our Professional plan.

## Configuring Filters

Filters can be configured on any LogRocket page using the Omnibar, at the top of the page. Filters configured in the Omnibar will refresh the data on the page to only show data from sessions that match that filter. These filters will persist as you navigate through LogRocket until you remove them. Omnibar filters can be saved as Segments (see below).

Omnibar filters can be configured by clicking into the Omnibar and either selecting your desired filter from the dropdown, or by typing the name of the filter.

Filters can also be configured within specific [Metrics](https://docs.logrocket.com/docs/logrocket-metrics), such as Timeseries, Tables, Path Analysis, Conversion Funnels, and others. Filters configured within a Metric are specific to that metric and do not persist into other areas of LogRocket.

### User Identification Filters

*Available for Web and Mobile SDK Sessions*:

**Email** - match sessions with identified users that were identified with the given email address.

**Name** - match sessions with identified users that were identified with the given name.

**City** - match sessions based on the city in which the user was located.

**Country** - match sessions based on the country in which the user was located.

**IP Address** - match sessions based on the user's IP address.

**Signed up status** - match only sessions with users identified through our `.identify()` methods.

**State/Region** - match sessions based on the state or region in which the user was located.

**User First Seen** - match sessions with users that were *first* seen within the given time period. This may include sessions outside of the given time period.

**User ID** - match sessions with users that were identified with the given user ID. Anonymous users also have user IDs.

**User Last Seen**- match sessions with users that were *last* seen within the given time period. This may include sessions outside of the given time period.

**User Session Count** - list all sessions for users that meet a criteria based on how many sessions they have recorded.

**User Time on Site** - list all sessions for users that have a total accumulative session time within the given range.

**User Trait** - match sessions where identified users has a given value for a user trait.

> 🚧 A Note on Location
>
> LogRocket uses IP reverse-lookup to determine a user City and Country. If you have disabled IP addresses from being sent to LogRocket, these filters will not be available as the data will not exist within the session

### Session Metadata Filters

These filters are all about data *about* sessions, with the exception of user-related metadata. There is always only one piece of data returned by these filters for the entire session.

*Available for Web and Mobile SDK Sessions:*

**Active Time in Session** - match sessions that have an **active time** duration above or below a certain amount of time.

**Device** - match sessions by device type. Devices will be identified as either Desktop, Mobile, or Tablet.

**SDK Type** - match sessions based on whether they were recorded using our web or mobile SDKs.

**NPS** (*Pro*) - match sessions in which an NPS score has been submitted matching the given value.  This filter supports Wootric and Delighted.

**UTM Tracking** - match session based on value of UTM parameter for Medium, Source, or Campaign.

**Event Count** - match sessions by total event count. An event is defined as any user action taken within the session (e.g., clicks or navigation).

**Referrer URL** - match sessions based on the URL from which the session had been referred (the page the user visited before the session began).

**Release** - match sessions by what release they happened in. This is configured via the `release` option of `LogRocket.init()`. [See the SDK documentation for more details](https://docs.logrocket.com/reference#release).

**OS** - match sessions by operating system.

*Available for Web SDK Sessions:*

**Browser** - match sessions where the user visited from a specific browser.

**Viewport Size** - match session based on the size of the user's browser.  You can search based on pixel size of width or height of the browser.

### Session Activity Filters

These filters are all about data *within* a session, such as user activity clicks or app-related data. There can be multiple pieces of data returned by these filters for each session.

*Available for Web and Mobile SDK Sessions:*

**Visited URL** or **Visited Mobile Page** - match sessions where the user visited a given URL or mobile page. You can optionally specify a duration criteria for time spent on a given URL. For Mobile Sessions, this filter applies to View Controller for iOS, Activity for Android, and to the values that have been recorded using `.tagPage`.

> 📘 Using the LIKE operator for the 'Visited URL' filter
>
> If you are looking for a more specific way to choose URLs to filter on, try using our LIKE operator.  This supports searching with wildcards (entered as asterisks) as part of the query.  For example, you could search for something like `https://app.logrocket.com/*/*`

**Browser Navigated** - match sessions where user clicked the Back or Forward button on a particular URL (note that Page Refresh is a separate filter)

**Clicked** or **Touched** - match sessions where the user clicked on a piece of text or a specific element, optionally on a specific page. Please note that if any element clicked is [hidden or sanitized from LogRocket](https://docs.logrocket.com/docs/privacy#section-exclude-dom-data-from-logrocket-), then it will not appear in the search as sanitized data is not sent to LogRocket.

**Custom Event** - matches sessions that had a custom event triggered during the session. These are triggered by `LogRocket.track()`. [See the SDK documentation for more details](https://docs.logrocket.com/reference#track).

**Redux Action Type** - matches sessions that had the given Redux action. This filter is only available if you set up Redux integration with LogRocket. [See the SDK documentation for more details](https://docs.logrocket.com/reference#redux-logging).

**Rage Clicked** - match sessions that have "rage clicks". A rage click is defined as a series of rapid, repeated clicks on the same element.

**Text Input** - match sessions based on values that a user inputs to text fields. You can specify text input to any field, or narrow it down to specific fields based on selector or component type.

**Network Error** (*Pro*) - match sessions that contain a network *error* with the specified parameters.  Please note that this includes errors with a status of 0.  This filter type is retroactive to June 2025.

**Network Request** (*Pro*) - match sessions that contain a network request with the given parameters. You can filter by URL, status code, method, duration, request and response body text. For each parameter you can specify multiple values.

**Page Refreshed** - match sessions in which the user clicked the browser refresh button on a particular URL

**Feedback Rating** - match sessions based on the results recorded in [Feedback](https://docs.logrocket.com/docs/feedback).

**Landing Page** - match sessions based on the first page visited during the session.

**Log Message** (*Pro*) - match sessions where a specific console message occurred. Used to find sessions where console INFO, WARNING, and ERROR messages occurred. Console messages that contain javascript Objects instead of text strings are *not* searched by this filter.

**Element Visible** and **Element Not Visible** (*Pro*) - match sessions that either rendered or did not render a specific DOM element. DOM elements can be specified by either its ID, CSS class, tag name, or inner text.

**Error Message** - match sessions where a specific issue with specific error text occurred.

**Any Issue** - match sessions where any [Issue](https://docs.logrocket.com/docs/issues) has been detected.

*Available for Web SDK Sessions:*

**Dead Clicked** - match sessions where a user recorded a "dead click" somewhere on your site. A dead click is defined as a click that did not result in a DOM change.

**Scroll Depth** (*Pro*) - matches sessions that have scrolled to a certain pixel depth within the specified URL

> 📘 Filtering based on text, selectors, and components
>
> Many session activity filters allow you to specify criteria for where on your application an event occurred. The three options that you will typically see are:
>
> * `on text`: matches sessions where a user clicked on an element with the given text. This is capped to 20 characters and is case-insensitive.
>
> * `on selector`: matches sessions where a user clicked on the a DOM node identified by the [given selector](https://developer.mozilla.org/en-US/docs/Web/API/Document_object_model/Locating_DOM_elements_using_selectors). The supported selector syntax is a simplified version of the official one, containing only IDs, class names, and element names. We also support nth-child pseudo-selectors, but only with number values (odd, even, and variable notation is not supported).
>
> In order to be as accurate as possible we record the node path from the document root to the DOM node the user clicked on. We stop recording the selector after it reaches 250 characters, in which case we discard the highest-level selectors.
>
> * `on component`: matches sessions where the user clicked on the given React component. Please note that for this to work you must be using the [LogRocket React plugin](https://docs.logrocket.com/reference/react-plugin-1).

### Performance Filters

*All performance filters are available on our Professional plan only.*

*Available for Web and Mobile SDK sessions:*

**Time Between Events** - match sessions based on how much time elapsed between two events. The following event types can be included in this filter:

* Custom Events added by calling `LogRocket.track()`
* Redux Actions
* Clicked or Touched
* Navigation
* Network Request
* Element Visible
* Log / Error Message

**Crash Reported** - For web sessions, this will match sessions where a browser crash occurred. Please note that this feature requires your server to send a[ `Report-To`](https://docs.logrocket.com/docs/crash-logging-configuration) header in the event of a crash. For mobile sessions,  match sessions where an app crash occurred. No additional setup is required to capture Mobile Crashes.

**Average CPU Load** - match sessions that observed the average CPU load above or below a specified percentage. This filter optionally supports specifying a URL, ViewController, or Activity for more granular filtering. Please note that average CPU load is approximate.

**Average Memory Usage** - match sessions that observed the average memory above or below a specified size. This filter optionally supports specifying a URL, ViewController, or Activity for more granular filtering. Please note that average memory is approximate. For Web sessions, this can only be measured on sessions within Google Chrome.

*Available for Web SDK Sessions Only:*

\***DOM Complete** - match sessions where the time to DOM complete was within the given time frame, for the *first* real page load that happened in the session. DOM complete measures when all processing on the page is complete and resources have finished downloading.

**Time to First Byte** - match sessions where the duration from the user or client making an HTTP request to the first byte of the page being received by the client's browser is within the given time frame.

**Cumulative Layout Shift** - match sessions with a Cumulative Layout Shift value within the selected range.  This can be specified for a specific URL or can search across all pages.  CLS measures individual layout shift scores for every unexpected layout shift that occurs during the lifespan of the page.  This may be inaccurate in particular for single-page applications.  For more information, see [here](https://web.dev/cls/).

**First Input Delay Time** - match sessions with a First Input Delay time within the given time frame, for the *first* real page load that happens in the session.  FID measures the time from when a user first *interacts* with a page to the time when the browser is actually able to begin processing event handlers in response to that interaction.  For more information, see [here](https://web.dev/lcp/).

**Largest Contentful Paint Time** - match sessions with a Largest Contentful Paint time within the given time frame, for the *first* real page load that happens in the session.  LCP reports the render time of the largest image or text block within the viewport, providing a user-focused method for measuring actual time of page load.  For more information, see [here](https://web.dev/lcp/).

**Frustrating Network Request** - match sessions that observed a user expressing frustration while waiting for an unusually long network request. Types of frustrated user behaviors include scrolling, clicking, and mouse movement.

*Available for Mobile SDK Sessions Only:*

**Mobile App Startup** - match sessions that observed a cold, warm, or hot start above or below a specified time. This filter optionally supports specifying a URL, ViewController, or Activity for more granular filtering. A cold start is when a user launches your app for the first time after rebooting, or when the app has not been launched for a long time. A warm start occurs when the app is running in memory, but some of the cold start tasks need to be re-run. A hot start, or a resume, is when the user reenters your app from app switcher or the home screen.

**Frozen Frames** - match sessions that experienced at least one 'frozen' frame, or a frame that took longer than 700 milliseconds to render. An optional view/page name can be specified for the filter, or the total frame render time (note that due to the time threshold for a frame to be considered frozen, this will never be less than 700ms). For more information, see the entry on Frozen Frames [here](https://docs.logrocket.com/docs/performance-monitoring#available-for-mobile-only).

## Filter Markers in the Timeline

The following filters will show up in the timeline as a green marker at the time when the relevant action took place:

* Clicked or Touched
* Rage Clicked
* Dead Clicked
* Visited URL
* Custom Event
* Redux Action
* Element Visible (pro)
* Network Request (pro)

<Image align="center" alt={172} caption="Example filter marker" title="Screen Shot 2018-02-13 at 5.39.36 PM.png" src="https://files.readme.io/f89e35885282869d40597870307ca52496beff59ebf67693c80d9beb0bdb1a76-Filter_Markers_in_the_Timeline.png" />

## Using Multiple Filters

Multiple filters can be used when searching through sessions. When chaining filters together, AND logic will be used to ensure that all criteria is met in a search.

## Saving Filters as Segments

Filters can be saved to the dashboard for reusability, these are called Saved Segments. Filters can be saved as either a public or private filter.

**Public Filters** will appear under Team Filters in the dashboard's lefthand navigation.

<Image align="center" alt="Creating a public filter" caption="Creating a public filter" src="https://files.readme.io/d5789ec-Screenshot_2023-03-30_at_1.57.12_PM.png" width="500px" />

**Private Filters** will appear under My Filters in the dashboard's lefthand navigation.

<Image align="center" alt="Creating a private filter" caption="Creating a private filter" src="https://files.readme.io/63be719-Screenshot_2023-03-30_at_1.58.24_PM.png" width="500px" />

## Non-Retroactive Filters

Some filters cannot be applied to historical session data. For these filters, you will only see data moving forward from when the filter is saved.

Any search containing one of these filter types will be considered non-retroactive and thus must be saved before sessions will meet the search criteria:

* Time Between Events
* Log/Error Message
* Element Not Visible

> 📘 'Element Visible' and 'Network Request' filters
>
> The Element Visible and Network Request filters are partially retroactive for LogRocket's SaaS offering.  They will need to be saved before showing results, but you will see some historical data start to appear quickly