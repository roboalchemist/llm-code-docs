# Source: https://docs.intelligems.io/analytics/experiment-analytics/filters.md

# Experiment Filters

Intelligems offers several filters that you can use to drill down on the sessions and orders included in experiment results.

## Default Filters

There are a few filters that are always on behind the scenes:

**Orders**

* Recurring subscription orders (i.e., orders that are placed automatically, and are not the first in a recurring series) are excluded
* Refunds, voids, and cancellations are excluded, unless you disable this setting as explained [here](https://docs.intelligems.io/order-and-revenue-accounting#refunds-and-cancellations)
* Free orders (i.e., orders with $0 in net revenue) are excluded
* Orders placed while an experiment is paused
* Orders that only include gift cards

**Sessions / Visitors**

* Sessions that started before an experiment was started, or while an experiment was paused, are excluded
* Visitors who open an experiment in Intelligems preview mode are excluded
* Bots are excluded

## Filter by Time

You can use the date picker to filter by date and time. Only sessions started and orders placed during the filtered period will be included in results. Intelligems uses your store’s local timezone for all dates and times. You can see this timezone in the information bar at the top of the Key Metrics analytics page.

<div data-full-width="false"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-489979a6e97d175f649f5cd685d003abfc0c330d%2FScreenshot%202025-07-14%20at%204.47.00%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure></div>

## Filters Pane

All other filters are available in the filters pane, which you can open by clicking the “Filter” button in the analytics header, circled in red in the screenshot below:

<div data-full-width="false"><figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-b90f71abff0fbc6f6fb598d6908fb2aa7e506bba%2FScreenshot%202025-07-14%20at%204.43.54%E2%80%AFPM.png?alt=media" alt=""><figcaption></figcaption></figure></div>

Filters are “ANDed” together across sections, and “ORed” together within sections. For example, if you were to select “Desktop” from the Device Type filter section and check off “Paid Social” and “Google” from the Source Channels & Sites section, this will filter to visitors on a Desktop device who came from either a Paid Social source or from Google.

### Available Filters

**Device Type**: Filter between Desktop vs. Mobile visitors. Tablets like iPads are generally included in “Mobile”.

**Visitor Type**: Filter between New vs. Returning visitors. A “Returning” visitor is a visitor who had visited the site while Intelligems was installed in a prior session before the experiment was started. Note that on initial installation, Intelligems won’t have seen your visitors before, so all visitors will be treated as new. It typically takes about 2 weeks for this data to normalize, and will become more accurate over time.

**Source Channels & Source Sites**: Filter to visitors who came from certain sources. If you check off multiple sources, they’ll be “ORed” together, for example, checking off Paid Social and Google will filter to visitors who came from either a Paid Social source or from Google. Visitors who had multiple sessions are attributed to the source for their first session in the experiment. For example, if a visitor comes through a Paid Social ad and then comes back directly to the site, they would be considered Paid Social.

**URL Parameter**: Filter the url parameters (eg, UTM parameters) set on a visitor’s landing page during their first session in the experiment. The parameters used here are those that were on the first page of the first session during which the visitor was exposed to the experiment, even if the visitor was not exposed on that page. For example, say a test is running targeted on a product page, and the visitor comes through an ad and lands on a landing page, then clicks through to a product page. The URL parameters considered for this filter are those that were set on that first landing page, even if they do not persist beyond that point.

**User Behavior**: Filter by user behavior, including conversion funnel stage:

* **Conversion Funnel:** For the conversion funnel, a visitor counts towards a stage if they reached at least that stage. For example, a visitor who started checkout and reached no further would be included in the “All Stages,” “Added to Cart,” and “Started Checkout” filters.
* **Views:** When "Orders with Target Products" is active, "Visited Product Page" means "Visited *Target* Product Page."

**Custom Events**: If you have set up and associated custom events with an experiment ([see here](https://docs.intelligems.io/analytics/custom-events) for more), you’ll see them show up in this section. A visitor counts towards a custom event if they triggered it at least once. Custom event filters are “ORed” together, i.e., selecting multiple custom events will filter to visitors who triggered any of those events.

**Filter Orders by Product**: This filter is available only for price tests, or if you have chosen “Count only orders containing certain products” during experiment setup.

<figure><img src="https://2052204893-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F2SvefuMLsJyJPAcVXeWc%2Fuploads%2Fgit-blob-2fa2a2260b46b2acf847b7884a791380ddd7b30e%2Fimage.png?alt=media" alt=""><figcaption></figcaption></figure>

**When “All Orders” is selected:** All eligible orders are included ([see here](https://docs.intelligems.io/analytics/how-orders-and-sessions-are-attributed-to-experiments) for more on how orders are attributed to experiments).

**When “Orders with Target Products” is selected:** Only orders that contained at least one target product are included.

* For example, say product ID 123 is selected as a target product, and my order had two line items, one unit of product ID 123 and one unit of product ID 456, my order would be counted (because it contained product ID 123), and my whole order (including both product 123 and product 456) would contribute to revenue metrics, unit quantity, etc..
* When this filter is active, it also applies to add to cart, begin checkout, and view product rate metrics and filters. For example, when this filter is active, the Add to Cart rate is the % of visitors who added at least one target product to cart.

**Z-Score**: Filter to exclude outlier orders. Each order is assigned a z-score which is the number of standard deviations its net revenue is above the average order value for the store, as of the creation time of the order. For example, a z-score of 3 means that the order is 3 standard deviations above the average for the store. Intelligems must have at least 750 orders in its dataset before it starts assigning z-scores to orders. By default, orders with a z-score >3 are excluded from analytics. You can change this filter on a case-by-case basis from the filters pane, or you can change the default for your store on the settings page.

**Countries**: Filter to visitors from specific countries.

**Landing Page:** Filter by the page a visitor first landed on on the site.
