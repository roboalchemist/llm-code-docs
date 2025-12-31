# Source: https://gitbook.com/docs/help-center/where-can-i-find-api-ids.md

# Where can I find API ids?

When interacting with the GitBook API, you'll frequently need to provide specific identifiers. The most common of these are the Organization ID, Space ID, and Site ID. Fortunately, locating these IDs is straightforward – they are embedded directly within the GitBook app's URL as you navigate through your content.

**Locating Your Organization and Space IDs:**

When you're actively working within a specific space in the GitBook application, take a look at the URL displayed in your browser's address bar. It will typically resemble the following structure:

```
https://app.gitbook.com/o/<your_organization_id>/s/<your_space_id>
```

In a URL like `https://app.gitbook.com/o/50mEth1Ng/s/RaNd0Mstr1NG`, the segment following `/o/`, which is `50mEth1Ng` in this case, represents your **Organization ID**. Similarly, the portion after `/s/`, here `RaNd0Mstr1NG`, is your **Space ID**.

**Identifying Your Site ID:**

To find your Site ID, go to the dashboard for the specific site you are interested in within the GitBook app. Once on the dashboard, examine the URL in your browser. You should find a section that looks like `/sites/<your_site_id>`.

For example, if the URL contains `/sites/site_w0r1d`, then `site_w0r1d` is your **Site ID**.
