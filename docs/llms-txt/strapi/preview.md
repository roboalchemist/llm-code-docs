# Preview

With the Preview feature, you can preview your front end application directly from Strapi's admin panel. This is helpful to see how updates to your content in the Edit View of the Content Manager will affect the final result.

</IdentityCard>

<!-- TODO: add a dark mode screenshot -->

</Tabs>

<details>
<summary>Caching in Next.js:</summary>

In Next.js, [cache persistence](https://nextjs.org/docs/app/building-your-application/caching) may require additional steps. You might need to invalidate the cache by making an API call from the client side to the server, where the revalidation logic will be handled. Please refer to Next.js documentation for details, for instance with the [revalidatePath() method](https://nextjs.org/docs/app/building-your-application/caching#revalidatepath).
<br/>

</details>

#### Content source maps

Live Preview is able to identify the parts of your frontend that correspond to fields in Strapi. This is done through content source maps, which are metadata encoded as hidden characters in your string-based content (e.g., text fields). It uses the  library to encode and decode this metadata.

Metadatas will only be added in your Content API responses when the `strapi-encode-source-maps` header is set to `true`. You can set this header in your data fetching utility. Make sure to only pass the header when you detect that your site is rendered in a preview context.

For a Next.js application, you may use the `draftMode()` method from `next/headers` to detect if draft mode is enabled, and set the header accordingly in all your API calls:

```typescript {20-23}

  contentType: string,
  params: Record = {}
): Promise {
  // Check if Next.js draft mode is enabled
  const { isEnabled: isDraftMode } = await draftMode();
  
  try {
    const queryParams = { ...params };
    // Add status=draft parameter when draft mode is enabled
    if (isDraftMode) {
      queryParams.status = "draft";
    }
    
    const url = `${baseURL}/${contentType}?${qs.stringify(queryParams)}`;
    const response = await fetch(url, {
      headers: {
        // Enable content source maps in preview mode
        "strapi-encode-source-maps": isDraftMode ? "true" : "false",
      },
    });
    if (!response.ok) {
      throw new Error(
        `Failed to fetch data from Strapi (url=${url}, status=${response.status})`
      );
    }
    return await response.json();
  } catch (error) {
    console.error("Error fetching content:", error);
    throw error;
  }
}
```

## Usage

**Path to use the feature:**  Content Manager, edit view of your content type

:::strapi Preview vs. Live Preview
Based on your CMS plan, your experience with Preview will be different:
- With the Free plan, Preview will be full screen only.
- With the  and  plans, you get access to an enhanced experience called Live Preview. With Live Preview, you can see the Preview alongside the Edit view of the Content Manager, and you can also edit the content directly within the preview itself by double-clicking on any content.
:::

Once the Preview feature is properly set up, an **Open preview** button is visible on the right side of the [Content Manager's edit view](/cms/features/content-manager#overview). Clicking it will display the preview of your content as it will appear in your front-end application, but directly within Strapi's the admin panel.

<!-- TODO: add a dark mode GIF -->

Once the Preview is open, you can:

- click the close button  in the upper left corner to go back to the Edit View of the Content Manager,
- switch between the Desktop and Mobile preview using the dropdown above the previewed content,
- switch between previewing the draft and the published version (if [Draft & Publish](/cms/features/draft-and-publish) is enabled for the content-type),
- and click the link icon  in the upper right corner to copy the preview link. Depending on the preview tab you are currently viewing, this will either copy the link to the preview of the draft or the published version.

:::note
In the Edit view of the Content Manager, the Open preview button will be disabled if you have unsaved changes. Save your latest changes and you should be able to preview content again.
:::

### Live Preview

Live Preview is the enhanced Preview experience available with Strapi’s paid CMS plans.

With Live Preview, in addition to what’s included in the Free plan, you can:

* Use the Side Editor to view both the entry’s Edit view in the Content Manager and the front-end preview side by side. You can also switch between full-screen and side-by-side preview using the  and  buttons.
* Double-click any content in the preview pane to edit it in place. This opens a popover that syncs the front-end content with the corresponding field in Strapi.

<!-- TODO: add dark mode GIF -->

:::caution Experimental feature
This feature is currently experimental. Feel free to share  or  with the Strapi team.

The current version of Live Preview comes with the following limitations:
* Blocks fields are not detected, and changing them in the Side Editor won’t be reflected in the preview. Clicking on Save after updates should however still work.
* Media assets and fields in dynamic zones are not handled.
:::