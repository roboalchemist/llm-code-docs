# Source: https://learn.microsoft.com/en-us/clarity/clarity-filters

Title: Filters overview

URL Source: https://learn.microsoft.com/en-us/clarity/clarity-filters

Markdown Content:
Clarity offers a wide range of powerful filters to help you sort and customize Recordings, Heatmaps, and Dashboard. By choosing the right filter for your needs, you can find interesting patterns in your data and make better-informed decisions.

Use filters to drill deep into user behavior at page or a session-level. For example, you can use page filters to focus on data related only to a specific page on your site. You can also use session filters to understand how diverse types of users interact with your site.

Tip

Save your favorite filter combinations as a segment so you can easily find them later.

With any of your projects open, you can find the filters from **Dashboard**, **Recordings**, or **Heatmaps** pages.

On the **Dashboard**, select **Filters** to show the filters.

![Image 1: Filters on dashboard.](https://learn.microsoft.com/en-us/clarity/media/filters-on-dashboard.png)

On **Session Recordings**, select **Filters** to show the filters.

![Image 2: Filters on session recordings.](https://learn.microsoft.com/en-us/clarity/media/filters-on-sessions.png)

On **Heatmaps**, select **Filters** to show the filters.

![Image 3: Filters on heatmaps.](https://learn.microsoft.com/en-us/clarity/media/filters-on-heatmaps.png)

Note

Filters set in one of these three areas usually remain in effect when you switch your view from one to another. For example, you can set a browser filter in Heatmaps and use it again on your Dashboard or Recordings. The exception is when a filter is applied only for one specific area (e.g., session filters).

There are 30+ filters available, so Clarity organized them into groups based on relevant categories.

Navigate through the filters by using the left bar. You can choose from the following groups on the navigation bar:

| **Group** | **Exclude Selection** | **Regular Expressions** | **Multiple Selection** |
| --- | --- | --- | --- |
| [User Info](https://learn.microsoft.com/en-us/clarity/clarity-filters#filtering-by-user-info) | ✔ Browser ✔ Operating System ✔ Location | ✘ | ✔ Days of the Week ✔ Device ✔ Browser ✔ Operating System ✔ Location |
| [User Actions](https://learn.microsoft.com/en-us/clarity/clarity-filters#filtering-by-user-actions) | ✔ Smart Events | ✘ | ✔ Insights ✔ Actions ✔ Intentions ✔ Smart Events |
| [Path](https://learn.microsoft.com/en-us/clarity/clarity-filters#filtering-by-path) | ✘ | ✔ | ✔ |
| [Traffic](https://learn.microsoft.com/en-us/clarity/clarity-filters#filtering-by-traffic) | ✔ Source ✔ Medium ✔ Campaign | ✘ | ✔ Source ✔ Medium ✔ Campaign ✔ Channel ✔ Bot Traffic |
| [Performance](https://learn.microsoft.com/en-us/clarity/clarity-filters#filtering-by-performance) | ✘ | ✘ | ✔ Performance Score ✔ LCP ✔ INP ✔ CLS |
| [Product](https://learn.microsoft.com/en-us/clarity/clarity-filters#filtering-by-product) | ✔ Brand | ✘ |  |
| [Session](https://learn.microsoft.com/en-us/clarity/clarity-filters#filtering-by-session) | ✘ | ✘ | ✘ |
| [Page](https://learn.microsoft.com/en-us/clarity/clarity-filters#filtering-by-page) | ✔ JavaScript Errors | ✘ | ✘ |
| [Custom Filters](https://learn.microsoft.com/en-us/clarity/clarity-filters#filtering-with-custom-filters) | ✔ Custom User ID ✔ Custom Session ID ✔ Custom Page ID ✔ Custom Labels | ✘ | ✔ Custom Labels |

The**User info**filter group helps you to screen results by information about your visitors:

![Image 4: Filters by user info.](https://learn.microsoft.com/en-us/clarity/media/filters-user-info.png)

1.   **Time frame**: Select a date range for your results. You can choose options between today and the last 30 days or enter a custom range. For a custom time frame, you can customize both the date and time.

2.   **Day of the week**: Select a day or days of the week from the drop-down.

3.   **Device**: Select one or more devices from the list of PC, Tablet, Mobile, and Other.

4.   **Browser**: Select one or more browsers from a list that include Chrome, Microsoft Edge, and Safari. You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.

5.   **Operating system**: Select one or more OS from a list, including Windows and macOS. You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.

6.   **Location**: Select one or more countries/regions from the list. As you select a Country/Region, choose a State and City from the drop-down. You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.

7.   **Clarity user ID**: Enter a specific Clarity user ID (text type) to include only results from that Clarity user. You can get the user ID from the Session details view. You can also view visitor profiles of the specific clarity user. Learn more about [Visitor profile](https://learn.microsoft.com/en-us/clarity/session-recordings/visitor-profile).

**Example**: You can use the Browser filter to compare user data related to visitors on Chrome and Microsoft Edge. Apply the filter with Chrome selected first, inspect your results, and then run another query with Microsoft Edge.

8.   **User type**: Select **Sessions with new users** or **Sessions with returning users** from the dropdown.

The**User actions**filter group allows you to screen results by user activity on your website:

![Image 5: Filters by user actions.](https://learn.microsoft.com/en-us/clarity/media/filters-user-actions.png)

1.   **Insights**filter group helps you to screen results by insights generated from Clarity Insights:

    *   **Rage clicks**: Select data where a user repeatedly clicked in a clustered area within a brief period. This filter helps identify frustration points in your design.

    *   **Dead clicks**: Select data where a user clicked somewhere, but there was no response. This filter helps find UX bugs.

    *   **Excessive scrolling**: Select data when a user scrolled through site content at a higher rate than expected for standard content consumption. This filter helps identify users who are lost on your page.

    *   **Quick backs**: Select data where a user went to a new page then quickly returned to the previous one. This filter helps you find confusing navigation or content.

2.   **Actions**filter based on user interaction with your page or app.

    *   **Cursor movement**: Select data where a user moved their mouse. For mobile devices and tablets, this metric captures user swipes on the screen. This filter helps you identify when a user is active on your page, without any clicks on it.

    *   **Entered text**: Select data where a user-typed content or pasted text in a text box, input box, or form element.

    *   **Selected text**: Select data where a user-selected text on the page. This data helps you in identifying the content the user is reading or copying.

    *   **Resized page**: Select data where a user changes the size of their browser window or switches between landscape/portrait on a mobile phone.

    *   **Clicked 'Jump to recipe'**: Available only for food blogs, select data when a user clicked 'Jump to recipe' button on a page.

    *   **Visited recipe page**: Available only for food blogs, select data to display when a visitor views a recipe page during a session.

    *   **Refreshed page**: Select data where a user refreshes their browser on this page.

3.   **Intentions**: Select data that categorizes quality of sessions based on the user interactions. Learn more about [User intent metrics](https://learn.microsoft.com/en-us/clarity/insights/user-intent-metrics).

4.   **Clicked text**: Select data where a user clicked on a specific element with this text in it.

5.   **Page scroll depth**: Select data where a user scrolled an exact depth down a page. Enter the depth scrolled in a percentage.

**Example**: Set **Page scroll depth** less than your site's average fold to better understand users who left the page without getting to the average fold. You can also add more filters or check out individual session recordings. You can find your site's average fold by using Clarity's scroll maps.

6.   **Smart events**: Select data that capture key user actions. Clarity automatically defines smart events, and you can customize them or define new events. Learn more about [Smart events](https://learn.microsoft.com/en-us/clarity/setup-and-installation/smart-events).

7.   **Funnels**: Select data that capture ordered group of user actions. You can customize or define funnels. Learn more about [Funnels](https://learn.microsoft.com/en-us/clarity/setup-and-installation/funnels).

8.   **Reader type**: Available only for content blogs, select data that categorizes sessions based on the number of articles viewed. The types are:

    *   **One and done**: Select data where users viewed only one article.
    *   **Casual**: Select data where users viewed 2 to 3 articles.
    *   **Serious**: Select data where users viewed four or more articles.

9.   **Reading behavior**: Available only for content blogs, select data that categorizes pageviews based on how users read the article.

    *   **Engaged**: Select data where users finished reading the article.
    *   **Abandoned at headline**: Select data where the user only read the article headline.

10.   **Viewed recipe card**: Available only for food blogs, select data to display when a visitor sees the recipe card.

The**Path** filter group helps you to screen results by user interaction with specific URLs on your site:

![Image 6: Filters by path.](https://learn.microsoft.com/en-us/clarity/media/filters-path.png)

1.   **Entry URL**: Select data where a user entered the site on a specific page. This filter helps you to watch and analyze user behavior on particular pages.

2.   **Exit URL**: Select data where a user left the site on a specific page. This filter helps you to evaluate why users left a particular page.

3.   **Visited URL**: Select data that includes a specific page. This filter helps you analyze how users navigate away from a particular page during a more extensive journey on your website.

Learn more about the [supported operators](https://learn.microsoft.com/en-us/clarity/filters/path-filters-operators).

Note

Clarity supports RegEx in path filters. You can select specific groups of pages using [regular expressions](https://learn.microsoft.com/en-us/clarity/filters/regular-expressions).

The**Traffic**filter group helps you to screen results by criteria related to your site's traffic flow:

![Image 7: Filters by traffic.](https://learn.microsoft.com/en-us/clarity/media/filters-traffic.png)

1.   **Referring site**: Select data where the URL of a specified page matches the one the user visited before your site, if available to Clarity. The referring site isn't available in cases where no data is passed in the HTTP headers.

2.   **Source**: Select data from a specific "utm_source," which is the domain name of the link that sent a visitor to your site. You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.

3.   **Medium**: Select data from a specific "utm_medium," which is the advertising or marketing medium for your traffic source. You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.

4.   **Campaign**: Select data from a specific campaign if you used a UTM code to track your online marketing campaign. You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.

5.   **Channel**: Select data that groups the traffic either "utm_source" or "utm_medium." Available channels are Organic Search, Direct, Social, Referral, Email, [AIPlatform](https://learn.microsoft.com/en-us/clarity/insights/ai-channel-group), [PaidAIPlatform](https://learn.microsoft.com/en-us/clarity/insights/ai-channel-group), PaidSearch, Social, and Other. This filter allows you to check the performance of your traffic channels.

6.   **Bot traffic**: Select sessions detected as bots.

7.   **Ad campaign**: Select data associated with your advertising campaigns. Learn more about [Ad campaigns](https://learn.microsoft.com/en-us/clarity/advertising-dashboard/ad-campaign-details).

The**Performance**filter group helps you to screen results related to critical metrics that affect loading performance, interactivity, and visual stability. Learn more about [Performance metrics](https://learn.microsoft.com/en-us/clarity/insights/performance-widget).

![Image 8: Filters by performance.](https://learn.microsoft.com/en-us/clarity/media/filters-performance.png)

1.   **Performance score**:

    *   A score between (0-50) indicate poor performance.
    *   A score between (51-80) indicate a need for improvement.
    *   A score between (81-100) indicate a good performance.

2.   **Largest Contentful Paint (LCP)**: Select data where the loading performance of the primary content of a page is measured.

    *   An ideal LCP occurs within 2.5 seconds of the initiation of page loading.
    *   LCP less than 4 seconds indicate a need for improvement.
    *   Poor LCP occurs beyond 4 seconds.

3.   **Interaction to Next Paint (INP)**: Select data to measure your page's overall responsiveness based on the worst interaction latency of the page.

    *   The target for INP is 200 milliseconds or less.
    *   INP within 500 milliseconds indicates a need for improvement.
    *   Poor INP occurs beyond 500 milliseconds.

4.   **Cumulative Layout Shift (CLS)**: Select data to assess the stability of your page layout.

    *   CLS with 0.1 seconds or less is considered good.
    *   CLS within 0.25 seconds indicates a need for improvement.
    *   Poor CLS occurs beyond 0.25 seconds.

The **Product** filter group helps you to screen results by criteria related to your e-commerce site. Learn more about [E-commerce Insights](https://learn.microsoft.com/en-us/clarity/insights/e-commerce-insights).

Note

1.   Filters 1-6 are available for site instrumenting with Product JSON-LD.
2.   Filter 7 is available for Clarity projects of Shopify sites.
3.   Filter 8 is available for only Shopify plus sites.

![Image 9: Filters by product.](https://learn.microsoft.com/en-us/clarity/media/filters-product.png)

1.   **Price**: Select data for the price value of the product viewed based on the currency used on your site. Choose to view data based on the minimum and maximum values you input.

2.   **Brand**: Select data that includes the product brand. This filter helps you to view more from the specific brand. You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.

3.   **Product name**: Select data based on a product name.

4.   **Availability**: Select data that includes whether a viewed product was in stock or not. The dropdown list includes In stock, None, Out of stock.

5.   **Rating**: Select data with average user rating. Enter the star min and max rating from 1 to 5.

6.   **Number of ratings**: Select data with the total number of users rated. Enter a numeric input in min and max count.

7.   **Purchases**: Select the sessions where site visitors did or didn't purchase a product. Choose to view sessions based on "Yes" or "No."

8.   **Checkout abandonment**: Select the sessions where the user abandoned the checkout process at a specific step. Choose to view sessions based on the step in the checkout process that was abandoned. See [Checkout abandonment](https://learn.microsoft.com/en-us/clarity/insights/e-commerce-insights#checkout-abandonment) for step information.

The**Session**filter group helps you to screen results by criteria you choose:

![Image 10: Filters by sessions.](https://learn.microsoft.com/en-us/clarity/media/filters-session.png)

1.   **Session duration**: Select the duration of user sessions in minutes. For "one minute 30 seconds," enter "1.5". Choose to view sessions based on the minimum and maximum values you input.

2.   **Session click count**: Select the sessions where users clicked a specific number of times. Choose to view sessions based on the minimum and maximum values you input.

3.   **Session page count**: Select the sessions where users visited a specific number of pages. Choose to view sessions based on the minimum and maximum values you input.

**Example**: Find out why users didn't interact with your site using Session click count. Enter few clicks to see user sessions with lower interactivity. And for a balancing perspective, enter a higher number of clicks to view sessions with many interactions. Dig into the details to better understand what makes your site engaging and what doesn't.

The**Page** filters group helps you to screen results by criteria related to the pages viewed:

![Image 11: Filters by page.](https://learn.microsoft.com/en-us/clarity/media/filters-page.png)

1.   **Page duration**: Select the amount of time the user spent on a page. Enter the duration in minutes. For "one minute 30 seconds," enter "1.5". Choose to view sessions based on the minimum and maximum values you input.

2.   **Page click count**: Select the number of clicks on a page. Enter the number of clicks per page. Choose to view sessions based on the minimum and maximum values you input.

3.   **JavaScript errors**: Select data where a JavaScript error is detected while executing JavaScript on the browser. View multiple errors on a page using logical **OR** or logical **AND** functions. The top 500 JavaScript errors are shown in the drop-down. You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.

    *   **Click error**: Select data where a JavaScript error is detected after a user click. You can view multiple errors on a page using logical **OR** or logical **AND** functions. You can find Click errors drop-down below the JavaScript errors.

![Image 12: JavaScript errors.](https://learn.microsoft.com/en-us/clarity/media/javascript-errors.gif)

4.   **Page size**: Input the width and height of your page in pixels. Choose to view data greater than, less than, or equal to the selected page size.

5.   **Screen resolution**: Select the screen resolution of the page in pixels. Choose to view data greater than, less than, or equal to the selected screen resolution.

6.   **Visible page**: Select the amount of time that the page was visible to a user. Choose to view sessions based on the minimum and maximum values you input.

7.   **Hidden page**: Select the amount of time the page was open but hidden, such as set behind another tab. Choose to view sessions based on the minimum and maximum values you input.

**Example**: You might want to investigate if you're implementing responsive web design well. Are visitors more likely to come across problems when they visit your site with small screen widths? Do they interact more when looking at your screen with large displays? To learn more, you can filter data by page size or screen resolution.

Clarity's custom tags are customizable filters that allow you to analyze recordings and heat maps in different directions. Learn more about:

*   [Custom tags](https://learn.microsoft.com/en-us/clarity/filters/custom-tags)
*   [Custom IDs](https://learn.microsoft.com/en-us/clarity/clarity-filters#custom-ids)
*   [Custom labels](https://learn.microsoft.com/en-us/clarity/session-recordings/clarity-labels)

![Image 13: Filters with custom criteria.](https://learn.microsoft.com/en-us/clarity/media/filters-custom.png)

Custom IDs allow you to filter using user ID, session ID, and page ID. These properties are set similar to custom tags. The custom identifiers are set up using [Clarity client API](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api#javascript-apis).

The following are the IDs that you can custom set:

*   **Custom user ID**: The website owner creates and retrieves the text type custom user ID using [Clarity API custom identifiers](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api#javascript-apis). You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.
*   **Custom session ID**: The website owner creates and retrieves the text type custom session ID using [Clarity API custom identifiers](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api#javascript-apis). You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.
*   **Custom page ID**: The website owner creates and retrieves the text type custom user ID using [Clarity API custom identifiers](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-api#javascript-apis). You can [exclude this filter](https://learn.microsoft.com/en-us/clarity/filters/exclusion-filters) by selecting **Exclude selection** checkbox.

| Image | Description |
| --- | --- |
| ![Image 14: Dark blue label.](https://learn.microsoft.com/en-us/clarity/media/dark-blue-label.png) | * This label indicates that the applied filter is from a heat map. * Once applied, this filter appears on Recordings, Dashboard, and Heatmaps vertical. * You can access it at a later point by saving it as a segment or sharing it. **Limitations:** * This filter can't be set directly from the filters. * If you close the filter, you have to set it through heat maps again. |
| ![Image 15: Light blue label.](https://learn.microsoft.com/en-us/clarity/media/light-blue-label.png) | * This label indicates an applied universal filter. * This filter can be accessed Recordings, Dashboard, and Heatmaps vertical. * You can share it and also save it as a segment. |
| ![Image 16: Gray label.](https://learn.microsoft.com/en-us/clarity/media/gray-label.png) | * This label indicates a filter that can’t be applied to a particular vertical. * You can still share it and save it as a segment. |

For more answers, refer to [Filters FAQ](https://learn.microsoft.com/en-us/clarity/faq#filters).
