# Source: https://gitbook.com/docs/documentation/zh/publishing-documentation/site-structure/variants.md

# Source: https://gitbook.com/docs/documentation/fr/publishing-documentation/site-structure/variants.md

# Source: https://gitbook.com/docs/publishing-documentation/site-structure/variants.md

# Source: https://gitbook.com/docs/documentation/zh/publishing-documentation/site-structure/variants.md

# Source: https://gitbook.com/docs/documentation/fr/publishing-documentation/site-structure/variants.md

# Source: https://gitbook.com/docs/publishing-documentation/site-structure/variants.md

# Content variants

You can publish multiple versions of the same documentation as part of a single docs site. These variants will be available to the end users via the space switcher in the top-left corner of the published site.

<figure><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F2cQxJ5sTMVUkXOcuDEU8%2FAdding%20a%20section%402x.png?alt=media&#x26;token=2bd96c5f-0945-4d86-a835-a94102e627d9" alt="A GitBook screenshot showing a docs site&#x27;s structure"><figcaption></figcaption></figure>

### Add multiple languages or versions

A site with multiple variants is useful if you need to group together the content of your spaces — such as if you’re documenting multiple versions of an API (v1, v2, v3, etc.), or documenting your content in different languages.

{% hint style="info" %}
The spaces you link can contain any content, but it’s recommended to use variants as *variations of the same content*. If the spaces you link are semantically different from each other, consider adding them as [site sections](https://gitbook.com/docs/publishing-documentation/site-structure/site-sections) instead.
{% endhint %}

When adding a translation or multiple languages as a variant, it’s best practice to set the language of your variant to give your users the best experience when navigating your docs.

Adding multiple variants with languages set will move the language picker to the upper right, giving a cleaner, more direct experience from the default variant picker.

### Adding a variant to your docs site

From your docs site’s dashboard, open the **Settings** tab in the site header, then click **Structure**. Here you can see all the content of your site.

To add a variant, click the **Add variant** button in the section you'd like to add to, then choose a space to link. The new variant is then added to the list of variants within the chosen section and will be available to visitors in the variant dropdown on your site.

### Changing a variant

You can change the name and slug of each of your variants by clicking the <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> **Edit** button in the table row of the variant you’d like to edit. This will open a modal. Edit the field(s) you'd like to change, then click the **Save** button to save. You can also delete the variant by clicking the **Delete variant** button in the lower left.

{% hint style="info" %}
Changing a linked space's slug will change the space's canonical URL. GitBook will create an automatic redirect from the old URL to the new one. You can also [manually create redirects](https://gitbook.com/docs/publishing-documentation/site-redirects).
{% endhint %}

To replace a variant’s linked space with a different space, first delete it by clicking its **Edit** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F8pD8Y2BfBxCEZoi99Pnk%2Fedit%20-%20dark.svg?alt=media&#x26;token=89496678-7347-4845-8c98-ee8dd9bedaec" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FA3OfGjPkE5GnOQvN36jN%2Fedit.svg?alt=media&#x26;token=6f70239f-d889-4e64-9ec6-4801df47a48d" alt="The Edit icon in GitBook"></picture> button, then click the **Delete** button in the lower left of the modal. Once the variant is deleted, click the **Add variant** button to add the new space.

### Reordering variants

Your site displays variants in the order that they appear in your **Site structure** table. Variants can be reordered by grabbing the **Drag handle** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FjYRg42UtM4u1pHmJl4Ln%2Fdrag%20-%20dark.svg?alt=media&#x26;token=4c219b2b-37d2-449e-9130-19b6ba3d38d2" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FaS1QvPIBVYwhpFTGcPBN%2Foptions-menu.svg?alt=media&#x26;token=3ee40bbf-f4fb-41fa-aa30-306b559cbe88" alt="The Options menu icon in GitBook"></picture> and moving it up or down. The changed order will be reflected on your site immediately.

You can also use the keyboard to select and move content: select a section or variant with the space bar, then use the arrow keys to move it up or down. Hit the space bar again to confirm the new position.

### Setting a default variant

If you have multiple variants within a section, one variant will be marked as the default. This variant is shown when visitors arrive on your site (or when they visit a section). Other variants each have a slug that is appended to the site's URL.

To set a variant as default, click on the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> in the variant’s table row and then click **Set as default**.

{% hint style="info" %}
Setting a variant as default removes its slug field, as it will be served from the section root instead. GitBook will redirect the variant's slug to the appropriate path, to ensure visitors keep seeing your content.
{% endhint %}

### Remove a variant from a site

To remove a variant from a site, open the **Settings** tab from your docs site dashboard, then click **Structure** to find the content you want to remove.

Open the **Actions menu** <picture><source srcset="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2FQ4IsWwmEEi5QM7PSXNsN%2Factions%20-%20dark.svg?alt=media&#x26;token=ebff54f4-9825-4ab0-99bc-633e1c449371" media="(prefers-color-scheme: dark)"><img src="https://1050631731-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNkEGS7hzeqa35sMXQZ4X%2Fuploads%2F89MTSo5XRpPMVr1T0rxS%2Factions.svg?alt=media&#x26;token=2b5d001e-560a-4f29-8d22-de8163725ca1" alt="The Actions menu icon in GitBook"></picture> for the variant you want to remove and choose **Remove**.

{% hint style="success" %}
Removing a variant from your site will remove it from the published site, but **will not delete the space or the content within it**.
{% endhint %}
