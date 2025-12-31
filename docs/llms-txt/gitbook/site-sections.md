# Source: https://gitbook.com/docs/developers/gitbook-api/api-reference/docs-sites/site-sections.md

# Source: https://gitbook.com/docs/documentation/zh/publishing-documentation/site-structure/site-sections.md

# Source: https://gitbook.com/docs/documentation/fr/publishing-documentation/site-structure/site-sections.md

# Source: https://gitbook.com/docs/publishing-documentation/site-structure/site-sections.md

# Source: https://gitbook.com/docs/developers/gitbook-api/api-reference/docs-sites/site-sections.md

# Source: https://gitbook.com/docs/documentation/zh/publishing-documentation/site-structure/site-sections.md

# Source: https://gitbook.com/docs/documentation/fr/publishing-documentation/site-structure/site-sections.md

# Source: https://gitbook.com/docs/publishing-documentation/site-structure/site-sections.md

# Site sections

{% hint style="info" %}
This feature is available on the [Ultimate site plan](https://www.gitbook.com/pricing).
{% endhint %}

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FAfqBhbHbvEllbHg6s9I0%2Fsite_sections%402x.png?alt=media&#x26;token=40811255-7158-49fb-9938-7ebb878b5296" alt="A GitBook screenshot showing site sections on a docs site"><figcaption><p>Example of a GitBook site with site sections</p></figcaption></figure>

With site sections, you can centralize all your documentation and create a seamless experience for your users.

Site sections are perfect for organizing your documentation — whether you’re managing separate products, or catering to both end-users and developers with content tailored to each.

You can also [group site sections together](#create-a-site-section-group). Doing so will create a drop-down menu in your navigation bar — ideal for adding hierarchy to your site sections.

{% hint style="info" %}

### Sections or variants?

Each site section is a space in GitBook. You can create site sections from any space you like, but we recommend you use sections as semantically different parts of your docs.

If you want to add variations of the same content — such as localizations or historical versions of the same product — consider using [content variants](https://gitbook.com/docs/publishing-documentation/site-structure/variants) instead.
{% endhint %}

### Adding a section to your docs site

From your docs site’s dashboard, open the **Settings** tab in the site header, then click **Structure**. Here you can see all the content of your site.

To add a site section, click the **New section** button underneath the table and choose a space to link as a section. The new section is then added to the table and will be available to visitors as a tab at the top of your site.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FF2eMGMOFBOtjgd2ELMXE%2Fstructure%20tree%402x.png?alt=media&#x26;token=83fe9dd0-bbfd-42a7-954c-52d895eae78a" alt="A GitBook screenshot showing site section structure"><figcaption><p>Add structure to your docs with site sections.</p></figcaption></figure>

### Create a site section group

You can group site sections together under a single heading. Site section groups will appear as a drop-down in your site’s nav. Site sections in a group can also include an optional description, which appears below the section title in the drop-down menu.

To create a group, click the arrow next to the **New section** button and choose **New section group**. Give your new group a name, then click **Add section** in the modal to add sections to your group. You can add existing sections of your site to the new group, or select another space you want to add using the menu.

### Editing a section

You can change the name, icon and slug of each of your sections by tapping the <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> **Edit** button in the table row of the section you’d like to edit. This will open a modal. Edit the field(s) you’d like to change, then click the **Save** button. You can also delete the variant by clicking the **Delete variant** button in the lower left.

{% hint style="info" %}
Changing a section’s slug will change its canonical URL. GitBook will create an automatic redirect from the old URL to the new one. You can also [manually create redirects](https://gitbook.com/docs/publishing-documentation/site-redirects).
{% endhint %}

Site sections within a group can also optionally display a description, which will appear in the drop-down menu of your site’s nav bar when the section group is hovered. See the image at the top of this page to see an example of how this can look in your published documentation.

### Reordering sections

Your site displays sections in the order that they appear in your Site structure table. Sections can be reordered by grabbing the **Drag handle** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FjYRg42UtM4u1pHmJl4Ln%2Fdrag%20-%20dark.svg?alt=media&#x26;token=4c219b2b-37d2-449e-9130-19b6ba3d38d2" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FaS1QvPIBVYwhpFTGcPBN%2Foptions-menu.svg?alt=media&#x26;token=3ee40bbf-f4fb-41fa-aa30-306b559cbe88" alt="The Options menu icon in GitBook"></picture> and moving it up or down. All the spaces within that section will be moved with it. The changed order will be reflected on your site immediately.

You can also use the keyboard to select and move content: select a section with the space bar, then use the arrow keys to move it up or down. Hit the space bar again to confirm the new position.

### Setting a default section

If you have multiple sections in your site, one section will be marked as the default. This section is shown when visitors arrive on your site, and is served from your site’s root URL. Other sections each have a slug that is appended to the root URL.

To set a section as default, click on the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> in the section's table row and then click **Set as default**.

### Remove a section

To remove a section from a site, click the **Settings** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F6uYUpJto7WTkJf9BUPHv%2Fsettings%20-%20dark.svg?alt=media&#x26;token=bf52415f-e999-43a2-9a1a-c85176a014cd" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FwkBqgOPry9HAcW4cxJk0%2Fsettings.svg?alt=media&#x26;token=67bdbb00-ebf3-4a2d-9df8-0c822406f71c" alt="The Settings icon in GitBook"></picture> button from your docs site dashboard, then click **Structure** to find the content you want to remove. Click the **Edit** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> button next to the section you want to remove, then click the **Delete** button in the lower left of the modal. This will remove the section, along with all the variants within it, from the published site. It will not delete the spaces itself, or the content within them.

To remove a section from a site, open the **Settings** tab from your docs site dashboard, then click **Structure** to find the content you want to remove.

Open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> for the space you want to remove and choose **Remove**.

{% hint style="success" %}
Removing a section from your site will remove it — and all variants within it — from the published site, but **will not delete any of the spaces or the content within them**.
{% endhint %}
