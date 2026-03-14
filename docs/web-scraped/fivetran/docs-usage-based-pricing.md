# Source: https://fivetran.com/docs/usage-based-pricing

Title: Usage-Based Pricing | Monthly Active Rows

URL Source: https://fivetran.com/docs/usage-based-pricing

Markdown Content:
Fivetran’s pricing model involves four basic principles:

*   _Pricing is usage-based_. You are charged based on what you use each month.
*   _Your connection and activation usage is measured in [Monthly Active Rows (MAR)](https://fivetran.com/docs/usage-based-pricing#monthlyactiverows)_. MAR are unique identifiers, or primary keys, that we use to track transfers from your source system to your destination each month. These keys are counted separately for each account, destination, connection, table, activation, and activation sync. Once a row is active, it is only counted once per month - no matter how many updates are made that month.
*   _Your [transformation usage](https://fivetran.com/docs/usage-based-pricing/transformations-pricing) is measured in monthly model runs_. Monthly model runs is the total number of models successfully executed as part of your transformation jobs in a given month.
*   _You can choose which pricing plan fits your requirements_. See [Billing and Plans](https://fivetran.com/docs/usage-based-pricing/billing-and-plans) for more information.

* * *

Monthly Active Rows[](https://fivetran.com/docs/usage-based-pricing#monthlyactiverows)
--------------------------------------------------------------------------------------

MAR is the number of distinct rows synced from the source system to your destination system in a given calendar month. We determine MAR usage by tracking distinct primary keys. A primary key is a unique identifier that specifies a distinct row within a table. We separately count primary keys by account, destination, connection, table, activation, and activation sync. If a primary key is not available, we create a synthetic (hashed) primary key to ensure consistency. Fivetran uses a hash sampling re-sync detection algorithm to detect and classify row changes.

For both connections and activations, we detect and charge for inserts and updates, including deletes.

We only count a row once per month, even if it syncs multiple times. It doesn’t matter how many times a row is updated in a month; you don’t pay multiple times for updates on the same row in the same month. For example, if we sync a distinct primary key more than once in a month, then the distinct primary key counts as only a single MAR.

Monthly active rows are similar to total monthly synced rows but are less prone to variation and outliers. For example, a distinct primary key synced 30 times during a month counts as one MAR. Row-based pricing models, such as monthly synced rows, would charge you multiple times in that situation. Fivetran does not.

To understand what monthly active rows mean, and how they differ from monthly synced rows, consider the following simplified example:

Suppose you have a small table with a primary key **id** and one attribute, **counter**:

| id | counter |
| --- | --- |
| a | 1 |
| b | 2 |
| c | 3 |

You update **counter** from 3 to 4 in row **c**:

| id | counter |
| --- | --- |
| a | 1 |
| b | 2 |
| c | 3 |
| c | 4 |

This operation generates 1 active row. Now suppose you update the same **counter** again in the same month:

| id | counter |
| --- | --- |
| a | 1 |
| b | 2 |
| c | 3 |
| c | 4 |
| c | 5 |

This is still just 1 active row for this month. On the other hand, if you update row **a**, then you have 2 active rows:

| id | counter |
| --- | --- |
| a | 1 |
| a | 10 |
| b | 2 |
| c | 3 |
| c | 4 |
| c | 5 |

We sync most connections using incremental updates where we only update the new, deleted, or updated rows each sync. Thus, you only pay for a subset of the data in the source every month. What percentage of a table or a connection is imported per month depends on how you use your source system. For example:

*   If you opt to modify only new records, we import only a small percentage of the table or connection per month that causes a small percentage of the tables to have MAR.
*   If you opt to modify years-old historical records every sync, we re-import the complete source data that may cause a very high percentage of the tables to have MAR depending on the number of changes in your source system.

* * *

MAR types[](https://fivetran.com/docs/usage-based-pricing#martypes)
-------------------------------------------------------------------

Learn about the different types of MAR that exist to better understand your usage.

### Historical MAR[](https://fivetran.com/docs/usage-based-pricing#historicalmar)

Historical MAR represents data that already exists in the source or was synced when the table or connection was created.

Examples of historical MAR include:

*   Initial table syncs
*   Table schema changes that lead to a full table re-sync (for example, new added columns)
*   Manually triggered re-syncs
*   Data added during the first sync after a new account or project is added
*   Periodic re-syncs of additional data to avoid data integrity issues
*   Source-specific data integrity issues that require re-syncs
*   Migration syncs
*   Bug fixes that require re-syncs

### Free MAR[](https://fivetran.com/docs/usage-based-pricing#freemar)

Free MAR represents rows that are synced but do not count towards paid MAR. The following counts towards free MAR:

*   [Initial syncs](https://fivetran.com/docs/getting-started/glossary#initialsync)
*   [Connection trials](https://fivetran.com/docs/getting-started/free-trials#newconnectionfreeuseperiod)
*   [Private preview](https://fivetran.com/docs/core-concepts#releasephases) connectors (excluding destinations)
*   [Fivetran system tables](https://fivetran.com/docs/usage-based-pricing#fivetransystemtables)
*   [Fivetran Platform connector](https://fivetran.com/docs/logs/fivetran-platform#fivetranplatformconnector)
*   [Re-syncs](https://fivetran.com/docs/usage-based-pricing#resyncs)
*   [HVR Troubleshooting Window](https://fivetran.com/docs/usage-based-pricing/hvr#troubleshootingwindow)
*   Accounts with a legacy pricing plan
*   Free plan
*   [Promotions](https://fivetran.com/docs/usage-based-pricing/troubleshooting/promotions#whatisapromotionandhowdoienroll)

### Incremental MAR[](https://fivetran.com/docs/usage-based-pricing#incrementalmar)

Incremental MAR represents new or updated data in the source since the last sync.

Examples of incremental MAR include:

*   Overlapping incremental syncs
*   Changes in re-imported table syncs
*   Reporting connector [rollback syncs](https://fivetran.com/docs/getting-started/glossary#rollbacksync) that occur during a [conversion window](https://fivetran.com/docs/connectors/applications/google-ads#conversionwindow)

* * *

Understand your MAR usage[](https://fivetran.com/docs/usage-based-pricing#understandyourmarusage)
-------------------------------------------------------------------------------------------------

Learn how operations in your Fivetran account impact your MAR usage.

To learn how to monitor and optimize your MAR usage, see our [Monitor and Optimize Usage documentation](https://fivetran.com/docs/usage-based-pricing/tracking-and-optimizing-usage).

### Connections[](https://fivetran.com/docs/usage-based-pricing#connections)

Learn how connections can affect your MAR usage in specific circumstances.

#### New connections[](https://fivetran.com/docs/usage-based-pricing#newconnections)

[Every new connection you create has 14 days of free usage](https://fivetran.com/docs/getting-started/free-trials/new-connector-free-trial).

#### Connection base charge[](https://fivetran.com/docs/usage-based-pricing#connectionbasecharge)

We apply a $5 base charge to all connections that have a monthly usage between 1 MAR and 1M MAR. This _does not_ apply to accounts on the Free plan, which remains entirely free.

For more details, see our [2026 Pricing Updates FAQs](https://fivetran.com/docs/usage-based-pricing/pricing-updates/2026-pricing-updates) and in the [service consumption table](https://www.fivetran.com/legal/service-consumption-table).

#### Multiple connections based on the same connector[](https://fivetran.com/docs/usage-based-pricing#multipleconnectionsbasedonthesameconnector)

Each connection in your account contributes towards your monthly active rows. It is not the connector but the instance of the connection that matters. Even if the connections sync the same data from the same source (with the same primary keys), they contribute separately to your MAR.

#### Same source, multiple destinations[](https://fivetran.com/docs/usage-based-pricing#samesourcemultipledestinations)

If you have two or more connections of the same type that sync from one source to multiple destinations, we count each connection’s active monthly rows separately. For example, if you have two Salesforce connections, where one syncs to your staging destination and the other to production, we count the MAR of the connections separately. The sum of rows synced through each connection counts towards your MAR.

#### Release phases[](https://fivetran.com/docs/usage-based-pricing#releasephases)

Every connection based on a Private Preview connector is free, excluding destinations. We charge for connections when the associated connector is in Beta or Generally Available, and pricing varies on functionality. See our [core concepts documentation](https://fivetran.com/docs/core-concepts#releasephases) for more information.

### Syncs[](https://fivetran.com/docs/usage-based-pricing#syncs)

Learn how different sync types affect your MAR usage.

#### Initial syncs[](https://fivetran.com/docs/usage-based-pricing#initialsyncs)

[Initial syncs](https://fivetran.com/docs/getting-started/glossary#initialsync) don't incur a cost for the historical data they sync, but tracked incremental updates may count towards paid MAR outside the connection free trial period.

#### Re-syncs[](https://fivetran.com/docs/usage-based-pricing#resyncs)

In the following scenarios, re-syncs are free:

*   Historical data from adding a column
*   Unchanged rows in re-import tables
*   Post-trial MAR that was already seen in the trial
*   All other historical syncs

The free re-sync scenarios mentioned above apply to the updated pricing launched on March 1, 2025. If you are on an annual contract signed before March 1, 2025, transition to the latest pricing by renewing your contract.

#### Rollback syncs[](https://fivetran.com/docs/usage-based-pricing#rollbacksyncs)

If your connection performs a [rollback sync](https://fivetran.com/docs/getting-started/glossary#rollbacksync) as part of its sync strategy, the sync may fetch additional data from the previous month. We consider these past records as new unique records for the current month, and these rows count towards your MAR.

#### Priority-first syncs[](https://fivetran.com/docs/usage-based-pricing#priorityfirstsyncs)

[Priority-first syncs](https://fivetran.com/docs/using-fivetran/features#priorityfirstsync) fetch your most recent data first so that it's quickly ready for you to use. If you add a new source account to a connection that supports priority-first sync when an incremental sync is running, it impacts your MAR usage.

**Expand to see a list of connectors that support priority-first sync**

| Connector | Priority Fetch Period | Tables synced on a priority-first basis | Backward Sync Duration |
| --- | --- | --- | --- |
| AccuLynx | 30 days | `JOB` table | 6 hours |
| Acumatica | 7 days | All tables | 6 hours |
| Adjust | 30 days | All tables | 6 hours |
| Adobe Analytics | 15 days | All reporting tables | 6 hours |
| AdRoll | 30 days | All reporting tables | 6 hours |
| Afterpay | 120 days | `PAYMENT` table and its child tables | 6 hours |
| Algolia | 30 days | `AVERAGE_CLICK_POSITION`, `CLICK_POSITION`, `CLICK_THROUGH_RATE`, `CONVERSION_RATE`, `COUNTRY`, `FILTER`, `HIT`, `SEARCH`, `SEARCH_COUNT`, `SEARCH_NO_CLICK`, `SEARCH_NO_CLICK_RATE`, `SEARCH_NO_RESULT`, `SEARCH_NO_RESULT_RATE`, and `USER_COUNT` tables | 6 hours |
| Amazon Ads | 30 days | All reporting tables | 6 hours |
| Amazon Selling Partner | 7 days | `REPORTS`, `FINANCE`, and `ORDERS` modules | 6 hours |
| Amplitude | 15 days | All tables | 6 hours |
| Appcues | 7 days | `EVENT` table and its child tables | 12 hours |
| Apple Search Ads | 30 days | All reporting tables | 6 hours |
| Assembled | 15 days | `AGENT_STATE`, `DAILY_REPORT_METRIC`, `EVENT_CHANGE`, `FORECAST`, `FORECAST_TOTAL`, `HOURLY_REPORT_METRIC`, and `REQUIREMENT` tables |  |
| Auth0 | 180 days | `USERS` table | 6 hours |
| BigCommerce | 15 days | `CHANNEL`, `CUSTOMER`, `ORDERS`, `PRODUCT`, `PRICE_LIST`, and `SUBSCRIBER` tables and their child tables | 6 hours |
| Bizzabo | 15 days | `ATTENDEE_ANALYTICS`, `CONTACT`, `EVENT`, `EVENT_GOAL`, `EVENT_TEMPLATE` and `REGISTRATION` tables | 6 hours |
| Boostr | 15 days | `ACCOUNT`, `ACTIVITY`, `CONTACT`, `DEAL`, and `USERS` tables and their child tables | 6 hours |
| Braintree | 2 days | `CREDIT_CARD_VERIFICATION` table | 6 hours |
| Brex | 30 days | `EXPENSE` table | 6 hours |
| Brightpearl | 30 days | `CONTACT`, `ORDER_DETAIL`, and `PRODUCT` tables and their child tables | 6 hours |
| Canvas Data 2 by Instructure | 30 days | All tables | 6 hours |
| Ceridian Dayforce | 30 days | `EMPLOYEE_PUNCH` and `EMPLOYEE_RAW_PUNCH` tables | 6 hours |
| Chargebee Product Catalog 2.0 | 30 days | `QUOTE` and `QUOTE_SUBSCRIPTION` tables | 6 hours |
| Checkout.com | 7 days | `BALANCE_REPORT`, `CUSTOMER`, `DISPUTE`, `FINANCIAL_ACTION_REPORT`, `INSTRUMENT`, `PAYMENT`, `PAYMENT_ACTION`, `PAYOUT_REPORT`, and `REPORT` tables and their child tables | 6 hours |
| ChurnZero | 15 days | `CHURN_SCORE_CALCULATION` and `CHURN_SCORE_FACTOR_CALCULATION` tables | 6 hours |
| CloudTalk | 30 days | `CALL_HISTORY` table and its child tables | 6 hours |
| Commercetools | 30 days | `CART`, `CUSTOMER`, `INVENTORY`, `ORDERS`, `PAYMENT`, and `PRODUCT` tables and their child tables | 6 hours |
| Cornerstone | 30 days | `CERTIFICATION`, `CURRICULUM`, `PERFORMANCE_REVIEW`, `RECRUITING`, `REQUISITION`, `TRAINING`, `USERS`, and `USER_CUSTOMER_FIELD` tables | 6 hours |
| Criteo | 30 days | All reporting tables | 6 hours |
| Crunchbase | 30 days | `AQUISITION`, `INVESTMENT`, `JOB`, `ORGANISATION`, and `PEOPLE` tables | 6 hours |
| Datadog | 1 day | `AUDIT`, `CI_VISIBILITY_PIPELINE`, `CI_VISIBILITY_TEST`, and `EVENT` tables | 6 hours |
| Deposco | 30 day | `BILLABLE_TRANSACTION`, `BILLING_INVOICE`, `PURCHASE_ORDER`, `SALES_ORDER`, and `SHIPMENT` tables | 6 hours |
| Dialpad | 15 day | `CALL` | 6 hours |
| Donus | 1 day | `GRANTS`, `GRANTS_REPORT`, `MEMBER`, and `PAYMENT` tables and their child tables | 5 hours |
| Duoplane | 7 days | `PURCHASE_ORDER`, `PRODUCT`, and `SHIPMENT` tables | 6 hours |
| Everflow | 15 days | `ADVERTISER`, `COUPON_CODE`, `CUSTOM_CAP`, `CUSTOM_PAYOUT_REVENUE`, `OFFER_URL`, `SMART_LINK_CAMPAIGN`, and `TRAFFIC_CONTROL` tables and their child tables | 6 hours |
| EasyPost | 50 days | `CASH_FLOW_REPORT`, `PAYMENT_LOG_REPORT`, `SHIPMENT`, and `SHIPMENT_INVOICE_REPORT` tables | 6 hours |
| Eloqua | 7 days | `CONTACT_ACTIVITY` and custom object tables | 6 hours |
| Facebook Ads | 30 days | All reporting tables | 6 hours |
| Facebook Pages | 30 days | All page insights tables | 6 hours |
| Flywheel Digital | 30 days | `CONTENT_RESULT`, `PRODUCT`, and `SEARCH_TERM_RESULT` tables and their child tables | 6 hours |
| FourKites | 7 days | `SHIPMENT` table | 6 hours |
| Front | 30 days | `CONTACT` and `CONVERSATION` tables and their child tables | 6 hours |
| G2 | 30 days | `CATEGORY` and `HISTORY` tables | 6 hours |
| Fulfil | 7 days | `SALES_ORDER`, `SALES_ORDER_LINE`, `SHIPMENT`, and `SHIPMENT_RETURN` tables and their child tables | 6 hours |
| Gainsight Product Experience | 7 days | `CUSTOM_EVENT`, `EMAIL_EVENT`, `ENGAGEMENT_VIEW_EVENT`, `EVENT_IDENTIFICATION`, `FEATURE_MATCH_EVENT`, `FORM_SUBMIT_EVENT`, `LEAD_EVENT`, `PAGEVIEW_EVENT`, `SEGMENT_MATCH_EVENT`, `SESSION_EVENT`, `SURVEY_RESPONSE`, and `USERS` tables | 6 hours |
| Genesys | 30 days | `ANALYTIC_USER_DETAILS` table and its child tables | 6 hours |
| Google Analytics 360 | 15 days | All tables | 6 hours |
| Google Analytics 4 | 30 days | Reporting tables | 6 hours |
| Google Analytics 4 Export | 1 day | All tables | 6 hours |
| Google Display & Video 360 | 30 days | All tables | 6 hours |
| Google Search Ads 360 | 15 days | All tables | 6 hours |
| Google Search Console | 7 days | Reporting tables | 6 hours |
| Healthie | 30 days | `APPOINTMENT` and `FORM_ANSWER_GROUP` tables | 6 hours |
| Helpdesk | 30 days | `TICKET` tables | 6 hours |
| Help Scout | 15 days | `CUSTOMER_HISTORY` and `CONVERSATION_HISTORY` tables and their child tables | 6 hours |
| Hilti On!Track | 60 days | `TRANSFER` table | 6 hours |
| HubSpot | 1 day | `CONTACT`, `CONTACT_PROPERTY_HISTORY`, `CONTACT_FORM_SUBMISSION`, `CONTACT_COMPANY`, `CONTACT_CONTACT`, `CUSTOM_EVENT`, `EMAIL_EVENT_BOUNCE`, `EMAIL_EVENT_CLICK`, `EMAIL_EVENT_DEFERRED`, `EMAIL_EVENT_DELIVERED`, `EMAIL_EVENT_DROPPED`, `EMAIL_EVENT_FORWARD`, `EMAIL_EVENT_OPEN`, `EMAIL_EVENT_PRINT`, `EMAIL_EVENT_SENT`, `EMAIL_EVENT_SPAM_REPORT`, `EMAIL_EVENT_STATUS_CHANGE`, `EMAIL_EVENT_SUPPRESSED`, `EVENT`, `FEEDBACK_SUBMISSION`, `FEEDBACK_SUBMISSION_CONTACT`, `FEEDBACK_SUBMISSION_PROPERTY_HISTORY`, `FEEDBACK_SUBMISSION_TICKET`, `LEAD`, `LEAD_COMPANY`, `LEAD_CONTACT`, `LEAD_PROPERTY_HISTORY`, `INVOICE`, `INVOICE_COMPANY`, `INVOICE_CONTACT`, `INVOICE_DEAL`, `INVOICE_LINE_ITEM`, `INVOICE_TICKET`, and `INVOICE_PROPERTY_HISTORY` tables. | 6 hours |
| Instagram Business | 29 days | `USER_INSIGHTS` table | 6 hours |
| Ibacos | 30 days | `ASSESSMENT` and `REALM` tables. | 6 hours |
| Iterable | 7 days | `EVENT` table | 6 hours |
| Ivanti | 7 days | `CI` and `INCIDENT` tables | 6 hours |
| JobNimbus | 30 days | All tables | 6 hours |
| Klaviyo | 7 days | `EVENT` tables | 6 hours |
| Leap CRM | 30 days | `APPOINTMENT`, `CUSTOMER`, and `JOB` tables | 6 hours |
| Learn Amp | 30 days | `ACTIVITY`, `ENROLLMENT`, `EVENT`, `TASK`, and `USERS` tables | 6 hours |
| Liftoff | 30 days | `REPORT` table | 6 hours |
| LinkedIn Ad Analytics | 30 days | All reporting tables | 6 hours |
| Lucca | 30 days | `USERS` table and its child tables | 6 hours |
| Maileon | 30 days | `BOUNCE`, `CLICK`, `CONTACT`, `CONVERSION`, `OPENS`, `RECIPIENT`, `SUBSCRIBER`, `UNIQUE_CLICK`, `UNIQUE_OPENS`, and `UNSUBSCRIPTION` tables | 6 hours |
| Mailjet | 15 days | `CONTACT_LIST_SIGNUP`, `MESSAGE`, `MESSAGE_INFORMATION`,`GEO_STATISTICS`,`TOPLINK_CLICKED`, and `CLICK_STAT` tables | 6 hours |
| Marketo | 0 days | All activity (and dependent) tables and `LEAD` table | 6 hours |
| Maxio Chargify | 7 days | `EVENT`, `INVOICE`, `PRODUCTS_PRICE_POINT`, `PRODUCT`, `SUBSCRIPTION`, and `SUBSCRIPTION_COMPONENT` tables | 6 hours |
| Microsoft Advertising | 30 days | All reporting tables | 6 hours |
| Microsoft Power BI | 30 days | `REPORT` table | 6 hours |
| Mixpanel | 15 days | `EVENT` table | 6 hours |
| Nice | 30 days | `AGENT_PERFORMANCE`, `DISPOSITION`, `INTERACTION_HISTORY`, `SKILL_CALL_DATA`, `SKILL_SUMMARY`, `SLA_SUMMARY`, `STATE_HISTORY`, `WFM_DATA_ADHERENCE`, `WFM_DATA_CONTACT`, `WFM_DATA_PERFORMANCE`, and `WFM_DATA_SCORECARD` tables | 6 hours |
| On24 | 30 days | `ATTENDEE`, `EVENT`, `LEAD`, `PRESENTER`, and `REGISTRANT` tables | 6 hours |
| OnceHub | 15 days | `BOOKING` and `CONTACT` tables | 6 hours |
| OneTrust | 7 days | `DATA_SUBJECT` table | 6 hours |
| Optimizely | 30 days | `CONVERSION` and `DECISION` tables and their child tables | 6 hours |
| Oracle Fusion Field Service | 30 days | `ACTIVITY` , `RESOURCE_WORK_SKILL`, and `RESOURCE_WORK_ZONE` tables and their child tables | 6 hours |
| Ordergroove | 30 days | `ITEM`, `ORDERS`, and `SUBSCRIPTION` tables | 6 hours |
| Ordway | 7 days | `INVOICE`, `JOURNAL`, `PAYMENTS`, `REVENUE_SCHEDULE`, and `USAGE` tables and their child tables | 6 hours |
| Outbrain | 30 days | All reporting tables | 6 hours |
| Packiyo | 15 days | `ORDERS` table | 6 hours |
| Paddle | 30 days | `TRANSACTION` table and its child tables | 6 hours |
| PagerDuty | 15 days | `LOG_ENTRIES` table | 5 hours |
| Pardot | 14 days | `EMAIL`, `EXTERNAL_ACTIVITY`, `VISIT`, `VISITOR_ACTIVITY` and `VISITOR_PAGE_VIEW` tables | 6 hours |
| Pendo | 7 days | `ACCOUNT_HISTORY`, `EVENT`, `FEATURE_EVENT`, `GUIDE_EVENT`, `PAGE_EVENT`, `POLL_EVENT`, `TRACK_TYPE_EVENT`, and `VISITOR_HISTORY` tables | 6 hours |
| Pinterest Ads | 30 days | All reporting tables | 6 hours |
| Playvox Workforce Management | 15 days | `CONTACT`, `SCHEDULE_METRICS`, `SHIFT`, `WORK_ACTIVITY_TASK`, `WORKSTREAM`, `WORKSTREAM_AGENT_METRICS`, `WORKSTREAM_INTERACTION`, and `WORKSTREAM_METRICS` tables | 6 hours |
| Qmatic Data Connect | 30 days | `AGENT`, `AGENT_DAEMON_EVENT`, `APPOINTMENT_CANCELLED_DATE`, `APPOINTMENT_CREATED_DATE`, `DATE`, `DEVICE`, `DEVICE_CONTROLLER`, `DEVICE_CONTROLLER_EVENT`, `DEVICE_EVENT`, `FEEDBACK_DATE`, `MARK_TRANSACTION_DATE`, `OUTCOME`, `UNIT`, `VISIT`, `VISIT_TRANSACTION`, and `WORK_PROFILE` tables | 6 hours |
| Qualtrics | 7 days | `DISTRIBUTION`, `DIRECTORY_CONTACT`, `SURVEY_RESPONSE`, and `TICKET` tables | 6 hours |
| Quorum | 7 days | `BILL` table | 6 hours |
| ReBound Returns | 15 days | `RETURN` and `TRACKING` tables and their child tables | 6 hours |
| Recharge | 15 days | `ADDRESS`, `ADDRESS_DISCOUNT`, `ADDRESS_SHIPPING_LINE`, `CHARGE`, `CHARGE_DISCOUNT`, `CHARGE_LINE_ITEM`, `CHARGE_ORDER_ATTRIBUTE`, `CHARGE_SHIPPING_LINE`, `CHARGE_TAX_LINE`, `CHECKOUT`, `CHECKOUT_LINE_ITEM`, `CUSTOMER`, `DISCOUNT`, `METAFIELD`, `ONE_TIME_PRODUCT`, `ORDER`, `ORDER_LINE_ITEM`, `PAYMENT_METHOD`, `PLAN`, `SUBSCRIPTION`, `SUBSCRIPTION_HISTORY`, and `UTM_TAG` tables | 6 hours |
| Reddit Ads | 30 days | All reporting tables | 6 hours |
| Reltio | 7 days | `ENTITY`, `INTERACTION`, `MATCH`, and `RELATION` tables | 6 hours |
| Retently | 60 days | `REPORT` table | 6 hours |
| Ricochet360 | 30 days | `LEAD` table and its child tables | 6 hours |
| Rithum | 15 days | `ORDERS` and `PRODUCT` tables | 6 hours |
| Salesforce Commerce Cloud | 15 days | `CAMPAIGN`, `COUPON_REDEMPTION`, `CUSTOMER`, `ORDER`, and `PRODUCT` tables | 6 hours |
| Salesforce Marketing Cloud | 1 day | `CHAT_INBOUND_MESSAGE_LOG`, `CHAT_POTENTIAL_UNSUBS`, `CHAT_TRACKING`, `EMAIL`, `EVENT`, `LIST`, `LIST_SUBSCRIBER`, `MOBILE_PUSH_DETAIL_EXTRACT`, `PUSH_MESSAGE`, `SEND`, `SMS_MESSAGE_TRACKING`, `SUBSCRIBER`, and `TRIGGERED_SEND` tables | 6 hours |
| Samsara | 30 days | `AMBIENT_AIR_TEMPERATURE_MILLI_C`, `BAROMETRIC_PRESSURE_PA`, `DEF_LEVEL_MILLI_PERCENT`, `ECU_SPEED_MPH`, `ENGINE_COOLANT_TEMPERATURE_MILLI_C`, `ENGINE_LOAD_PERCENT`, `ENGINE_RPM`, and `INTAKE_MANIFOLD_TEMPERATURE_MILLI_C` tables | 6 hours |
| Shiphero | 30 days | `INVENTORY_CHANGE`, `LINE_ITEM_PICK`, `ORDERS`, `PACK_PER_DAY`, `PRODUCT`, `PURCHASE_ORDER`, and `RETURN` tables and their child tables | 6 hours |
| ShipNetwork | 15 days | `BACKORDER_BUSINESS`, `BACKORDER_CONSUMER`, `BACKORDER_DROPSHIP`, `BACKORDER_WHOLESALE`, `ORDER_BUSINESS`, `ORDER_CONSUMER`, `ORDER_DROPSHIP`, and `ORDER_WHOLESALE` tables and their child tables | 6 hours |
| Shopify | 15 days | `ABANDONED_CHECKOUT`, `COLLECTION`, `COMPANY`, `CUSTOMER`, `DRAFT_ORDER`, `ORDER`, `PRICE_RULE`, `PRODUCT`, and `TENDER_TRANSACTION` tables | 6 hours |
| Showpad | 30 days | `EVENT` table | 6 hours |
| Snapchat Ads | 30 days | All reporting tables | 6 hours |
| Spotify Ads | 30 days | All reporting tables | 6 hours |
| StarRez | 15 days | All tables except `BOOKING_TYPE`, `CUSTOM_FIELD_USAGE_TYPE_ENUM`, `ENROLLMENT_TYPE_ENUM`, `ENTRY_STATUS_ENUM`, `FIELD_DATA_TYPE_ENUM`, `GENDER_ENUM`, `GL_POSTING_TYPE_ENUM`, `GROUP_STATUS_ENUM`, `NATIONALITY`, `ROOM_RATE_DURATION_ENUM`, `ROOM_SPACE_TYPE_ENUM`, `ROOMSPACE_CLOSED_REASON`, and `TRANSACTION_TYPE_ENUM` tables | 6 hours |
| sticky.io | 15 days | `CONTACT` and `ORDERS` tables | 6 hours |
| Stripe | 30 days | All tables and their child tables except `APPLE_PAY_DOMAIN`, `CARD_PAYMENTS_FEES_TRANSACTION_LEVEL_1`, `CHECKOUT_SESSION`, `CREDIT_NOTE`, `EARLY_FRAUD_WARNING`, `PLAN`, and `SKU` tables | 6 hours |
| Taboola | 30 days | All reporting tables | 6 hours |
| The Movie Database | 12 days | `MOVIE` and `TV_SERIES` tables and their child tables | 6 hours |
| The Trade Desk | 30 days | All reporting tables | 6 hours |
| TikTok Ads | 30 days | All reporting tables | 6 hours |
| Totango | 15 days | `EVENT` table | 6 hours |
| Twitter Organic | 30 days | `ORGANIC_TWEET_REPORT` table | 6 hours |
| UKG Pro | 30 days | `DIRECT_DEPOSIT`, `EMPLOYEE`, `EMPLOYEE_CHANGE`, `EMPLOYEE_CONTRACT`, `EMPLOYEE_GLOBAL_BANK`, `EMPLOYEE_GLOBAL_LOCALIZATION_ELEMENT`, `EMPLOYEE_PAY_DEDUCTION_ELEMENT`, and `EMPLOYMENT` tables | 6 hours |
| Uptempo | 30 days | `FINANCE`, `LINE_ITEM` tables and its child tables | 6 hours |
| Veeva Vault | 7 days | `DOCUMENTS` table and the tables that contain the `modified_date__v` column | 6 hours |
| Walmart DSP | 30 days | All reporting tables | 6 hours |
| Workleap Officevibe | 15 days | `ENGAGEMENT`and `FEEDBACK` tables | 6 hours |
| Xactly | 30 days | All tables except `COMMISSION_SUMMARY` and `QUOTA_SUMMARY` tables | 6 hours |
| Yahoo DSP | 30 days | All reporting tables | 6 hours |
| Zonka Feedback | 15 days | `RESPONSE` table and its child tables | 6 hours |
| Zendesk Support | 15 days | `CALL_METRIC`, `SATISFACTION_RATING`, `TICKET`, `TICKET_FIELD_HISTORY`, and `TICKET_TAG_HISTORY` tables and their child tables | 12 hours |
| Zip | 15 days | `AUDIT_LOG`, `INVOICE`, `PURCHASE_ORDER`, and `REQUEST` tables and their child tables | 6 hours |

#### Phantom updates[](https://fivetran.com/docs/usage-based-pricing#phantomupdates)

In some rare scenarios, a connection is created without an initial sync. In such scenarios, the source may attempt to update rows that do not exist in the destination. We define these updates as phantom updates. Phantom updates are not visible in the destination, but they contribute to MAR since we capture these updates.

For example, consider that you have a table `TARGET` in the source database, with column `id` as its primary key. Now, consider that you update the value of the `id` column. In the next sync, we see that column for the first time due to an incomplete initial sync, but we also see the update operation. During this sync, we mark it as an update and this row counts towards MAR.

#### Phantom deletes[](https://fivetran.com/docs/usage-based-pricing#phantomdeletes)

In another corner-case scenario, the source attempts to update rows that do not exist in the destination. In this case, phantom deletes occur because we try to mark the `_fivetran_deleted` column `TRUE` for deleted records in the source. Phantom deletes are not visible in the destination, but they contribute to MAR since we capture these changes.

For example, consider that you have a table `TARGET` in the destination, with column `id` as its primary key, and there is no record in the table with `id = 2`. Now, consider that you create a record with `id = 2` in the source and then delete it before your connection syncs the record. The source marks the record with `id = 2` as `deleted`. In the subsequent sync, we retrieve the record with `id = 2` with the `deleted` status. We try to update the `_fivetran_deleted` column to `TRUE` in the `TARGET` table. We can't update the record because the record with `id = 2` does not exist in the destination. In the process, we capture a new unique (deleted) row, and this row counts towards MAR.

### Tables and schemas[](https://fivetran.com/docs/usage-based-pricing#tablesandschemas)

Learn how table and schema updates affect your MAR usage.

#### New tables[](https://fivetran.com/docs/usage-based-pricing#newtables)

New tables are treated like an [initial sync](https://fivetran.com/docs/usage-based-pricing#initialsyncs). A table is considered new during an incremental sync if it was not a part of the connection's schema or it was disabled during the connection's initial sync. Common scenarios include:

*   Newly-created tables in the source that the connection can now access.
*   The source connecting user gains access to new tables due to a change in their access policy.
*   A schema change requires the connection to deliver a new table to your destination.

For more details, see our [Do New Tables Count Towards MAR?](https://fivetran.com/docs/usage-based-pricing/troubleshooting/mar-new-tables) article.

#### New columns[](https://fivetran.com/docs/usage-based-pricing#newcolumns)

When you sync a new column of an existing table, that insert doesn't count towards MAR. When adding a new column triggers a table refresh, it still _doesn't_ count towards MAR if there are no data changes. However, if any of the re-synced rows have changes, we detect those and count these changes towards paid MAR.

#### Columns with `null` values[](https://fivetran.com/docs/usage-based-pricing#columnswithnullvalues)

When a connection syncs a `null` value for a column and then the value changes in the next sync, that change counts towards MAR.

On the other hand, if a column doesn't have any value at all, and then your connection syncs a value for that column during the next sync, it doesn't count towards MAR.

#### Automated schema migrations[](https://fivetran.com/docs/usage-based-pricing#automatedschemamigrations)

When we automatically add a column to a connector schema as part of an automated schema migration, rows in the table that are backfilled with data don't count towards MAR.

#### Primary key data type changes[](https://fivetran.com/docs/usage-based-pricing#primarykeydatatypechanges)

If the data type of primary key changes, it doesn't affect your MAR.

Similarly, in a table without a primary key, if the data type of columns from which we generate synthetic (hash) primary key changes, it doesn't affect your MAR.

#### Tables without a primary key[](https://fivetran.com/docs/usage-based-pricing#tableswithoutaprimarykey)

If a table doesn’t have a primary key, we create a synthetic (hash) primary key. The synthetic primary key is a hash of values of the columns defined for that table, so if those columns change, the primary key changes. We calculate the MAR for these tables based on their synthetic primary keys. The composition of this primary key differs by source.

In a table without a primary key, adding or removing columns that we use to generate the synthetic primary key _does_ affect MAR. Each row in the table counts towards MAR.

#### Fivetran system tables[](https://fivetran.com/docs/usage-based-pricing#fivetransystemtables)

The following connector-specific system tables count towards free MAR:

*   `FIVETRAN_QUERY`
*   `FIVETRAN_API_CALL`
*   `FIVETRAN_FORMULA`
*   `FIVETRAN_FORMULA_MODEL`

#### History mode tables[](https://fivetran.com/docs/usage-based-pricing#historymodetables)

Whenever a record’s value changes in a source table with [history mode](https://fivetran.com/docs/core-concepts/sync-modes/history-mode) enabled, we insert a new row into the destination table. This new row counts towards monthly active rows. Your MAR usage depends on the number of tables you have enabled history mode for and how frequently the data in your source system is changing.

The following changes in history mode tables count toward paid MAR:

*   Inserts and updates
*   Repeated updates

We do not charge for rows with no changes.

#### Re-import tables[](https://fivetran.com/docs/usage-based-pricing#reimporttables)

We [re-import tables](https://fivetran.com/docs/getting-started/glossary#reimport) in full during every sync as part of the sync strategy for some of your connections. During a re-import sync, we apply the same logic as for [incremental tables](https://fivetran.com/docs/getting-started/glossary#incrementalsync) that only activate changed rows.

For example, let's say that you have a re-import table with 100 rows from the previous month with zero changes. Fivetran will sync all 100 rows but considering there weren't any changes, it won't count towards MAR. Then, there is another sync 24 hours later and there are 20 new rows and 20 rows with changes. During this second sync, Fivetran re-imports the full 120 rows but the MAR usage is just 40, 20 for the new rows and 20 for the rows with changed data.

#### Data blocking[](https://fivetran.com/docs/usage-based-pricing#datablocking)

You can [block specific columns and tables](https://fivetran.com/docs/using-fivetran/features/data-blocking-column-hashing#datablocking) from replicating to your destination. However, you can't block primary key columns.Updates to a blocked column that is not a primary key column in your source table don't count toward MAR. We exclude blocked columns from your syncs.

#### Deletes in the source[](https://fivetran.com/docs/usage-based-pricing#deletesinthesource)

If a connector supports the [Capture Deletes feature](https://fivetran.com/docs/using-fivetran/features#capturedeletes), and you delete data from your source, it counts toward paid MAR usage. We [soft delete](https://fivetran.com/docs/core-concepts/sync-modes/soft-delete) the corresponding data in your destination by setting the system column `_fivetran_deleted` to `TRUE`. As the delete corresponds to a row update, it counts toward your MAR.

#### Deletes in the destination[](https://fivetran.com/docs/usage-based-pricing#deletesinthedestination)

If you delete data in your destination and later sync it again from your source, it counts towards your MAR.

### Connector-specific functional differences[](https://fivetran.com/docs/usage-based-pricing#connectorspecificfunctionaldifferences)

We calculate MAR in the same way for all our connectors. However, MAR calculations can vary due to significant differences in:

*   API capabilities
*   Individual connection configuration
*   Source configuration
*   Access management
*   Underlying data models
*   Raw data formats

Therefore, some connection types require tailored sync strategies.

#### Ad reporting connectors[](https://fivetran.com/docs/usage-based-pricing#adreportingconnectors)

We _do not_ exclude [historical syncs](https://fivetran.com/docs/getting-started/glossary#historicalsync) when you add a new _source account_ to the connectors listed below. If you add a new source account to the sync when the incremental sync is running, your MAR usage will increase, but only from the incremental data from that new source account.

**Expand to see an extensive list of ad reporting connectors**
*   Adobe Analytics
*   Adobe Analytics Data Feed
*   Adjust
*   AdRoll
*   Amazon Ads
*   Amazon Selling Partner
*   Amplitude
*   Apple Search Ads
*   Braintree
*   Criteo
*   Eloqua
*   Facebook Ads
*   Facebook Pages
*   Google Ad Manager
*   Google Ads
*   Google Analytics 4
*   Google Display & Video 360
*   Google Search Ads 360
*   Google Search Console
*   Help Scout
*   HubSpot
*   Instagram Business
*   Iterable
*   LinkedIn Ad Analytics
*   LinkedIn Company Pages
*   Marketo
*   Microsoft Advertising (formerly Bing Ads)
*   Outbrain
*   Pinterest Ads
*   Recharge
*   Salesforce Marketing Cloud
*   Shopify
*   Snapchat Ads
*   Taboola
*   TikTok Ads
*   Twitter Ads
*   Yahoo DSP
*   YouTube Analytics
*   Zendesk

#### File connectors[](https://fivetran.com/docs/usage-based-pricing#fileconnectors)

File sources don't provide change-tracking data to help us determine if specific rows have been updated in the source. As a result, every time you schedule a sync, we re-sync all the rows from files that were modified.We calculate MAR for a file based on the greatest number of rows we sync from that file during any sync in a given month. For file connectors, we add three columns as [composite primary keys](https://fivetran.com/docs/connectors/files#primarykeys) for a table.

For example, let's assume that you add a new file with 10 rows to your connection's configured location:

1.   Initial sync (May 1st) – file has 10 rows.
2.   Next sync (May 15th) – file has 15 rows, with 10 unchanged rows and 5 inserts.
3.   Last sync (May 31st) – file has 16 rows, with 8 unchanged rows, 2 changed rows, and 6 inserts. The 2 changed rows and 6 inserts count toward paid MAR.

The connection synced 16 rows in total. However, only the 2 changed rows and 6 inserts count toward MAR.

The behavior explained above applies to our updated pricing. If you are on the outdated pricing without enhanced re-sync detection, the greatest number of rows ever synced for a file during the month would be the total MAR. In the example above, your MAR would be 16.

If you configure the **modified file merge** option to `append_only`, all rows will count towards MAR. So, in the previous example, the MAR would be 41 (Free MAR 10 + Paid MAR 31).

#### Fivetran Platform Connector[](https://fivetran.com/docs/usage-based-pricing#fivetranplatformconnector)

The MAR that your Fivetran Platform connections generate is free. You can track your free MAR in the [Usage tab](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings#usage).

Using Fivetran Platform connections may incur costs in your destination if your service provider charges for compute usage. Learn more in our [destination costs documentation](https://fivetran.com/docs/destinations#destinationcosts).

#### Asana[](https://fivetran.com/docs/usage-based-pricing#asana)

Due to how the Asana API uses sync tokens, you may observe periodic increases in MAR consumption. Read our [Asana sync strategy documentation](https://fivetran.com/docs/connectors/applications/asana#syncstrategy) for more information.

#### Iterable[](https://fivetran.com/docs/usage-based-pricing#iterable)

The following tables are append-only:

*   `EVENT`
*   `EVENT_EXTENSION`
*   `USER_HISTORY`
*   `USER_UNSUBSCRIBED_CHANNEL_HISTORY`
*   `USER_UNSUBSCRIBED_MESSAGE_TYPE_HISTORY`
*   `USER_DEVICE_HISTORY`
*   `LIST_USER_HISTORY`
*   `CAMPAIGN_METRICS`

For these tables, we capture events from Iterable using webhooks and the Events API, then write them to the destination. We never overwrite existing events in the destination unless a re-sync is triggered. During a re-sync, we get the same events from the API again and overwrite the events in the destination.

We sync the remaining tables using non-incremental endpoints, so we re-import them during every sync.

#### MongoDB[](https://fivetran.com/docs/usage-based-pricing#mongodb)

We perform an automatic [full re-sync](https://fivetran.com/docs/using-fivetran/features#fullresync) when we see that the oldest [oplog](https://docs.mongodb.com/manual/core/replica-set-oplog/) entry is newer than expected.

See our [MongoDB MAR Management article](https://fivetran.com/docs/usage-based-pricing/tracking-and-optimizing-usage/mongodb) for more details.

#### NetSuite Suite Analytics[](https://fivetran.com/docs/usage-based-pricing#netsuitesuiteanalytics)

We use a hybrid approach to determine the overall MAR for NetSuite:

*   We incrementally update tables with a modified timestamp. The incrementally updated rows count towards monthly active rows.
*   We use a checksum to [capture deletes](https://fivetran.com/docs/connectors/applications/netsuite-suiteanalytics#deletingdata) incrementally. The data ranges of each table where changes are occurring count towards monthly active rows if changes are detected.
*   We [re-import the tables](https://fivetran.com/docs/connectors/applications/netsuite-suiteanalytics#reimport) that we can’t incrementally update. When we re-import a table, we count only changed rows as paid MAR.
*   We only sync new records for `SYSTEM_NOTES` and `SYSTEM_NOTES_CUSTOM` tables. We consider only the records created in the calendar month as monthly active rows.

We update the `TRANSACTIONS` and `TRANSACTION_LINES` tables incrementally. We don't recommend frequent updates of the historical records for the `TRANSACTION_LINES` table, as this significantly increases the count of monthly active rows.

#### Oracle[](https://fivetran.com/docs/usage-based-pricing#oracle)

When you add a new column to an Oracle table that we are syncing, we always trigger a table re-sync. Changes to the table structure interfere with LogMiner and force us to re-sync the table.

The LogMiner capture method is sunset and is no longer available for new Oracle connections.

#### Sailthru[](https://fivetran.com/docs/usage-based-pricing#sailthru)

Due to Sailthru API limitations, you may see a sudden increase in MAR at the start of the month. Read our [Sailthru sync strategy documentation](https://fivetran.com/docs/connectors/applications/sailthru#syncstrategy) for more information on Sailthru's API limits.

* * *

Activations[](https://fivetran.com/docs/usage-based-pricing#activations)
------------------------------------------------------------------------

All general rules pertaining to Fivetran usage and pricing apply to Activations (previously known as Census) as well:

*   We track activation usage in [Monthly Active Rows (MAR)](https://fivetran.com/docs/usage-based-pricing#monthlyactiverows) and charge for inserted and updated data, including deletes. To determine your usage, we track the number of activated rows by using the sync key or matching key specified in each activation sync.
*   We track usage on a per activation basis.
*   Activation usage follows its own consumption curve. The per MAR cost decreases with increased usage. For more details, refer to the [Service Consumption Table](https://www.fivetran.com/legal/service-consumption-table-update-preview).
*   You can track your activation usage on the [Usage tab](https://fivetran.com/dashboard/account/billing-usage/usage) in your dashboard.
*   Each new activation receives a [14-day free trial](https://fivetran.com/docs/getting-started/free-trials#activationtrial). During the trial, your estimated usage and pricing for Activations will be available in the [Pricing Estimator](https://fivetran.com/pricing-estimator), alongside connection and transformation usage.
*   On the [Free plan](https://fivetran.com/docs/usage-based-pricing/billing-and-plans), the maximum consumption limit for Activations is 3,500 MAR per month. The limit applies to account-wide usage.

* * *

Transformations[](https://fivetran.com/docs/usage-based-pricing#transformations)
--------------------------------------------------------------------------------

Transformation usage _does not_ count towards [monthly active rows (MAR)](https://fivetran.com/docs/usage-based-pricing#monthlyactiverows). Instead, we measure transformation usage in [monthly model runs](https://fivetran.com/docs/getting-started/glossary#monthlymodelruns). We only count successful monthly model runs as usage.

Each month, we offer 5,000 free model runs. Once your usage goes past 5,000 monthly model runs, we start charging for transformations usage. Additionally, the higher your paid usage is, the lower the price per model run. See our [Transformations Pricing](https://fivetran.com/docs/usage-based-pricing/transformations-pricing) documentation for more details and instructions on how to monitor and optimize your monthly model run consumption.
