# Source: https://docs.curator.interworks.com/site_content_design/pages/manual_embed_iframes.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manual Embed - (iFrames) 

> Embed content from external websites and legacy systems using iFrames and custom embed code.

Sometimes you need to go beyond Curator's standard embedding capabilities and embed content from your unique or legacy
systems into Curator. That's where Curator's **Manual Embeds** feature comes to the rescue! We'll walk you through the
steps to seamlessly embed any other website, using iFrames, into your Curator pages!

**Important Considerations:**

* While you're adding Manual Embeds, keep in mind that the embed code should come from trusted sources. This will help
  you avoid any security risks or funky user experiences.
* Some systems might require some extra configuration or customization to display perfectly within an iFrame. Check out
  the documentation or support resources for the specific system you're embedding to ensure compatibility and the best
  possible display.
* Don't forget to pay attention to the dimensions and aspect ratio of the iFrame content. We want it to fit smoothly
  within your Curator page. Adjust those dimensions if needed, so you avoid any cropping or weird distortions.

## Adding a Manual Embed to a Page

1. Login to the backend of your Curator instance (e.g. `https://www.curatorexample.com/backend` ).
2. Navigate to the **Content** > **Pages** section from the left-hand menu.
3. Find the page you'd like to add your Manual Embed to, or click the "+ New Page" button.
4. On the page builder editor, click the section you'd like to add your embed to, or click the "+" icon on the page
   builder page to add a new section.
5. Click the "Additional Elements" tab from the "Add Element" popup and select the **Embed** content type.
6. Choose the dropdown option that best fits your need from the options below
   * iFrame: For use when pasting in a simple URL (e.g. `https://mycuratorexample.com/embed`)
   * Embed Code (HTML): For use when copying embed code from another website - this will be in HTML and can be
     identified by searching the copied code for `</iframe>` - if this string is found in your code it means you are using
     an iFrame to embed.
7. Once you've pasted the correct information in, click "Add"
