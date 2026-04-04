# Source: https://docs.datadoghq.com/dashboards/guide/maintain-relevant-dashboards.md

---
title: Best practices for maintaining relevant dashboards
description: >-
  Guidelines for identifying unused dashboards and best practices for
  maintaining a clean, organized dashboard list.
breadcrumbs: >-
  Docs > Dashboards > Graphing Guides > Best practices for maintaining relevant
  dashboards
---

# Best practices for maintaining relevant dashboards

A cluttered dashboard list page can make finding the right content difficult and pollute a search query with unused or irrelevant results. By combining bulk delete with [**Recently Deleted** dashboards](https://docs.datadoghq.com/dashboards/list/#restore-deleted-dashboards), you can remove unwanted dashboards at scale and restore any accidental deletions. This guide includes:

- General rules for identifying unused dashboards for periodic removal
- Best practices for maintaining a manageable list page

## Finding unused dashboards{% #finding-unused-dashboards %}

While finding every single unused dashboard is tricky, these guidelines can help identify a large majority of unused content and reduce dashboard clutter significantly. Before you start deleting dashboards, a few notes about the list page:

- Start with the **All Custom** preset list. Only custom dashboards can be deleted
- Clicking the checkbox column selects all dashboards on the current page
- Avoid deleting shared dashboards. Dashboards with a public or authenticated sharing link appear with **SHARED** next to their name. It may be safer to avoid deleting these dashboards, since it may affect a public view

To restore accidental deletions, go to the **Recently Deleted** list. This list shows dashboards deleted in the last 30 days and automatically displays the least-recently deleted dashboards first. You can also bulk restore dashboards [through the API](https://docs.datadoghq.com/api/latest/dashboards/#restore-deleted-dashboards).

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/restore_deleted.5130d1a0a6c909b044aa1616f2cf361a.png?auto=format"
   alt="Restore deleted dashboards" /%}

### Deletion guidelines{% #deletion-guidelines %}

#### 1. Reverse sort by popularity

Click the **Popularity** column to reverse sort by popularity. The list automatically puts least-recently modified dashboards at the top. If these dashboards are low popularity and have not been modified in the last three months, it may be safe to delete them.

**Note:** Datadog Miscellany, an unofficial public repo, has a [script to remove dashboards and monitors](https://github.com/DataDog/Miscellany/tree/master/remove_old_dash_monitors) that have not been modified in the last three months.

#### 2. Search for default titles

Search for terms like:

- "'s timeboard"
- "'s screenboard"
- "'s dashboard"

Many dashboards containing these strings have default titles (for example, "Stephanie's Dashboard Thu, Jun 3, 1:41:44 pm"). Default titles can indicate a test dashboard that was created quickly and never renamed. It may be safe to delete these dashboards, especially if they are old or low-popularity. For example, the image below shows a search filtered to **All Custom** with a search for "'s screenboard", reverse sorted by popularity.

**Note:** Datadog Miscellany, an unofficial public repo, has a [script to delete dashboards based on title](https://github.com/DataDog/Miscellany/tree/master/delete_dashboards_by_text_search).

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/screenboard_search.79ca6792dcacb09f9c38a370228d7f16.jpeg?auto=format"
   alt="Search for ''s screenboard'" /%}

#### 3. Search for keywords like "test"

Search for terms that indicate a dashboard was only used temporarily, like `test` or `cloned`. These words can be used to label actively-used dashboards, so delete with caution, or look at dashboard age and popularity alongside title.

## Best practices for dashboard hygiene{% #best-practices-for-dashboard-hygiene %}

Periodic cleans reduce dashboard clutter; good practices for maintaining dashboards can be even more effective. These practices help your team ensure dashboards are manageable in the long-term.

- Use custom lists to find what you need. Search for a keyword like a service name, and select multiple dashboards to add them to a list
- Save one-off explorations for Notebooks or Quick Graphs. When exploring an individual metric or graph, try [Notebooks](https://docs.datadoghq.com/notebooks/#overview), which are unsaved by default, or [Quick Graphs](https://docs.datadoghq.com/dashboards/guide/quick-graphs/#overview) rather than creating a new dashboard that needs to be deleted
- Use [dashboard details](https://www.datadoghq.com/blog/dashboard-details/) to describe what a dashboard is for and how to use it. This helps teammates understand a dashboard's intended purpose and makes a dashboard useful to more people

You can also manage dashboards programmatically with the Dashboards API, which includes endpoints to [bulk delete](https://docs.datadoghq.com/api/latest/dashboards/#delete-dashboards) and [bulk restore](https://docs.datadoghq.com/api/latest/dashboards/#restore-deleted-dashboards) dashboards.

## Appendix{% #appendix %}

**Note**: Datadog Miscellany is an unofficial public repo and is not actively maintained by Datadog.

- [Documentation: Restore deleted dashboards in UI](https://docs.datadoghq.com/dashboards/list/#restore-deleted-dashboards)
- [API: Delete dashboards endpoint](https://docs.datadoghq.com/api/latest/dashboards/#delete-dashboards)
- [API: Restore deleted dashboards endpoint](https://docs.datadoghq.com/api/latest/dashboards/#restore-deleted-dashboards)
- [Datadog Miscellany: Remove old dashboards and monitors](https://github.com/DataDog/Miscellany/tree/master/remove_old_dash_monitors)
- [Datadog Miscellany: Delete dashboards based on text in title](https://github.com/DataDog/Miscellany/tree/master/delete_dashboards_by_text_search)
