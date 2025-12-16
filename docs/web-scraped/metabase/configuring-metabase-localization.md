# Source: https://www.metabase.com/docs/latest/configuring-metabase/localization

<div>

1.  [Home](/docs/latest/)
2.  [Configuring Metabase](/docs/latest/configuring-metabase/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Languages and localization

Admins can update the localization settings for the instance:

1.  Click on the **gear** icon in the upper right.
2.  Click **Admin settings**.
3.  In the **Settings** tab, click on **Localization** in the left sidebar.

These localization settings allow you to set global language and formatting defaults for dates, times, numbers, and currencies.

You can also override these localization options for specific fields or questions. For more info, see [Formatting](../data-modeling/formatting).

## Supported languages

Thanks to our amazing user community, Metabase has been translated into many different languages. Due to [the way we collect translations](#translations), languages may be added or removed during major releases depending on translation coverage.

Supported languages include:

  Language                 Code
  ------------------------ -------------------------------------------------
  English                  `en`
  Albanian                 `sq`
  Arabic                   `ar`
  Arabic (Saudi Arabia)    `ar-SA`
  Bulgarian                `bg`
  Catalan                  `ca`
  Chinese (Hong Kong)      `zh-HK`
  Chinese (Simplified)     `zh-CN`
  Chinese (Taiwanese)      `zh-TW`
  Czech                    `cs`
  Dutch                    `nl`
  Farsi/Persian            `fa`
  Finnish                  `fi`
  French                   `fr`
  German                   `de`
  Hebrew                   `he`
  Hungarian                `hu`
  Indonesian               `id`
  Italian                  `it`
  Japanese                 `ja`
  Korean                   `ko`
  Latvian                  `lv`
  Malay                    `ms`
  Norwegian Bokmål         `nb`
  Polish                   `pl`
  Portuguese (Brazilian)   `pt-BR`
  Russian                  `ru`
  Serbian                  `sr`
  Slovak                   `sk`
  Spanish                  `es`
  Swedish                  `sv`
  Turkish                  `tr`
  Ukrainian                `uk`
  Vietnamese               `vi`

The locale codes are relevant for setting the language in [static embeds](../embedding/static-embedding-parameters#setting-the-language-for-a-static-embed).

> While Metabase can support languages that read right to left, the Metabase UI is designed around languages that read left to right.

## Translations

Our community contributes to Metabase translations on our [Crowdin project](https://crowdin.com/project/metabase-i18n).

If you'd like to help make Metabase available in a language you're fluent in, we'd love your help!

For a new language to be added to Metabase, it must reach 100%. Once it does, we add it in the next major or minor release of Metabase. All *existing* languages in Metabase *must stay at 100%* to continue being included in the next *major* version of Metabase. This rule ensures that no one encounters a confusing mishmash of English and another language when using Metabase.

We understand that this is a high bar, so we commit to making sure that before each major release, any additions or changes to text in the product are completed at least 10 calendar days before the release ships, at which point we notify all translators that a new release will be happening soon.

Note that while we only remove languages in major releases, we are happy to add them back for minor releases, so it's always a good time to jump in and start translating.

### Contributing to translations for Metabase

If you'd like to help make Metabase available in a language you're fluent in, we'd love your help! Check out our [Crowdin project](https://crowdin.com/project/metabase-i18n).

## Instance settings

### Instance language

Here you can set the default language (also called the "instance language") across your Metabase UI, system [emails](./email), [dashboard subscriptions](../dashboards/subscriptions), and [alerts](../questions/alerts).

People can override these settings in their personal [account settings](../people-and-groups/account-settings).

Some translations are created by the Metabase community, and might not be perfect.

### Report timezone

Use **report timezone** to set a default display time zone for dates and times in Metabase. The report timezone setting is a display setting only, so changing the report timezone won't affect the time zone of any data in your database.

Report timezone doesn't apply to `timestamp without time zone` data types, including the output of [`convertTimezone`](../questions/query-builder/expressions/converttimezone) expressions. For example:

  Raw timestamp in your database                                                     Data type                                                               Report time zone   Displayed as
  ---------------------------------------------------------------------------------- ----------------------------------------------------------------------- ------------------ ------------------------
  `2022-12-28T12:00:00 AT TIME ZONE 'CST'`   `timestamp with time zone`      'Canada/Eastern'   Dec 28, 2022, 7:00 AM
  `2022-12-28T12:00:00-06:00`                `timestamp with offset`         'Canada/Eastern'   Dec 28, 2022, 7:00 AM
  `2022-12-28T12:00:00`                      `timestamp without time zone`   'Canada/Eastern'   Dec 28, 2022, 12:00 AM

Report timezone is only supported for the following databases:

-   BigQuery
-   Druid
-   MySQL
-   Oracle
-   PostgreSQL
-   Presto
-   Redshift
-   Vertica

### First day of the week

If you need to, you can change the first day of the week for your instance (the default is Sunday).

Setting the first day of the week affects how the [query builder](../questions/query-builder/editor) filters or groups by week. People can, however, use the `week` function to override this default when filtering or grouping by week of year. See [using a different first week of the year](../questions/query-builder/expressions/week#using-a-different-first-week-of-the-year).

This setting doesn't affect [SQL queries](../questions/native-editor/writing-sql).

## Dates and times

-   **Date style:** the way dates should be displayed in tables, axis labels, and tooltips.
-   **Date separators:** you can choose between slashes (`2022/12/14`), dashes (`2022-12-14`), and dots (`2022.12.14`).
-   **Abbreviate names of days and months:** whenever a date is displayed with the day of the week and/or the month written out, turning this setting on will display e.g. "January" as "Jan" or "Monday" as "Mon".
-   **Time style:** choose to display the time using either a 12 or 24-hour clock (e.g., 3:00 PM or 15:00).

## Numbers

-   **Separator style:** some people use commas to separate thousands places, and others use periods. Here's where you can indicate which camp you belong to.

## Currency

-   **Unit of currency:** if you do most of your business in a particular currency, you can specify that here.
-   **Currency label style:** whether you want to have your currencies labeled with a symbol, a code (like "USD"), or its full name.
-   **Where to display the unit of currency:** this pertains specifically to tables, and lets you choose whether you want the currency labels to appear only in the column heading, or next to each value in the column.

## Localizing embedded Metabase

You can translate both Metabase UI elements (like button labels) and content (like dashboard names) in static embeds. See [Setting the language for static embeds](../embedding/static-embedding-parameters#setting-the-language-for-a-static-embed) and [Translating embedded dashboards and questions](../embedding/translations).

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/configuring-metabase/localization.md) ]