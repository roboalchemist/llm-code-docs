# Source: https://docs.firehydrant.com/docs/internal-status-pages.md

# Internal Status Pages

> 📘 Note:
>
> Internal status pages are only available on [Pro and Enterprise Plans](https://firehydrant.com/pricing/). Please [reach out](https://firehydrant.com/demo/) to our sales team for more information.

Also called **per-incident status pages**, each incident on FireHydrant will have a dedicated ephemeral status page that summarizes high-level details and includes key links. All incident notes/updates posted via Slack (`/fh update`) or via Command Center are posted to the Internal Status Page. See [Posting Updates](https://docs.firehydrant.com/docs/posting-updates) for more details.

This page disappears 48 hours after the resolution of the incident. These pages have long, obscure URLs and are set to not be indexed by search engines.

<Image alt="Example internal status page" align="center" width="650px" src="https://files.readme.io/859b27b-internal-status-page.png">
  Example internal status page
</Image>

Some of the details shown include:

* Incident name
* Description
* Severity
* Milestone (current status)
* Duration
* Responders
* Impact
* Status Updates

## Visibility

For **public** (to your organization) incidents, these internal status pages do not require auth or a FireHydrant license to view. This link can be freely shared with other team members throughout your organization\*.

> 📘 Note:
>
> This default behavior can be adjusted. Please [reach out to Support](https://support.firehydrant.com/hc/en-us/requests/new) if you'd like to restrict these status pages only to users logged into FireHydrant (requires licenses for them to access).

For private incidents (restricted to users with **Private** access), internal status pages will be restricted to only users who are logged into FireHydrant ***and*** have **Private** access. To read more about access levels, see [Role-Based Access Controls](https://docs.firehydrant.com/docs/role-based-access-controls).

## Next Steps

* Read about [External Status Pages](https://docs.firehydrant.com/docs/external-status-pages) and the delineation between internal/external status pages