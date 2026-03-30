# Source: https://docs.base44.com/Building-your-app/managing-your-pages.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing your app pages

> Learn how to add pages, move between them, control which pages appear in your navigation, and understand how pages relate to login and visibility in Base44.

Pages are the core screens of your Base44 app. Each page has its own URL path (such as `/`, `/Home`, or `/Products`) and appears in the page drop-down at the top of the app editor. You can add new pages, access pages, and decide which pages are visible in your menus or used for login and landing experiences.

<Frame caption="Navigating your app pages">
    <img src="https://mintcdn.com/base44/Vo3HE1GylzgvScy8/images/pagesmenu.png?fit=max&auto=format&n=Vo3HE1GylzgvScy8&q=85&s=ac18ad8ad80fa68de964c773e69f0464" alt="Navigating your app pages" width="850" height="427" data-path="images/pagesmenu.png" />
</Frame>

***

## Adding pages

You can add pages at any time. The fastest way is to describe the page you want in AI chat.

### Adding a new page

1. Go to your app editor.
2. In AI chat, describe the page you want. For example:\
   `Create a new About page with a hero section, text about our company, and a contact button.`

<Frame caption="Adding a new page to your app with the AI chat">
    <img src="https://mintcdn.com/base44/vyZ6HEARIdqrgiI1/images/addpage.png?fit=max&auto=format&n=vyZ6HEARIdqrgiI1&q=85&s=48a9fca38617774a4d8fb518cd43d28d" alt="Adding a new page to your app with the AI chat" width="1302" height="956" data-path="images/addpage.png" />
</Frame>

### Duplicating a page

1. Open the page you want to reuse in the editor.
2. In AI chat, describe what you want to duplicate. For example:\
   `Duplicate this page and keep the same layout, but change the title to "Pricing".`
3. After the AI chat has finishes, open the new page from the page drop-down to customize the content.

<Frame caption="Duplicating a page on your app using the AI chat">
    <img src="https://mintcdn.com/base44/tzxdHQgJZr0YYZrD/images/duplicatepage.png?fit=max&auto=format&n=tzxdHQgJZr0YYZrD&q=85&s=cabd6af12138c254a168d7c595521d07" alt="Duplicating a page on your app using the AI chat" width="1347" height="957" data-path="images/duplicatepage.png" />
</Frame>

***

## Switching between pages

You can move between pages from the page drop-down above the preview.

**To switch pages in the app editor:**

1. Go to your app editor.
2. Click the page drop-down.
3. Click the page you want to open.

<Frame caption="Switching between pages in the app editor">
    <img src="https://mintcdn.com/base44/Vo3HE1GylzgvScy8/images/pagesdropdown.png?fit=max&auto=format&n=Vo3HE1GylzgvScy8&q=85&s=82ec30bde5c1918a52c1cfc6ff62aee5" alt="Switching between pages in the app editor" width="791" height="527" data-path="images/pagesdropdown.png" />
</Frame>

<Tip>
  If you are not sure what a page is called, ask the AI: `Show me a list of all pages in this app and what each one does.`
</Tip>

***

## Searching for pages

When your app has many pages, it can be hard to remember every page name. Start typing the page name in the pages drop-down to search for the one you need.

<Frame caption="Searching for a page in the pages drop-down">
    <img src="https://mintcdn.com/base44/Vo3HE1GylzgvScy8/images/searchingforapage.png?fit=max&auto=format&n=Vo3HE1GylzgvScy8&q=85&s=748f170acf99d1f09eb019d4ec592b89" alt="Searching for a page in the pages drop-down" width="719" height="391" data-path="images/searchingforapage.png" />
</Frame>

<Tip>
  **Tip:** You can also ask AI chat to help you find the right page by name, URL path, or purpose. For example:

  * `Which page is used as the checkout page?`
  * `Which page handles the /Success route?`
  * `Find the page that shows the list of projects.`
</Tip>

***

## Managing your page navigation

A clear navigation menu helps people move between pages, discover key areas of your app, and understand how your content is organized. It also improves internal linking, which can help search engines understand your app structure.

Some apps start with a single page and do not have a visible navigation menu at first. As you add more pages, you can ask the AI to create a header, sidebar, or footer menu and wire it up to your main routes.

Use the AI chat to create a navigation menu when your app does not yet have a header, sidebar, or footer with links.

<Tip>
  If you want the same navigation on every page, ask AI to make the menu global. For example: `Add the header navigation to all pages in the app.`
</Tip>

### Adding a header menu

1. Go to your app editor.
2. In the AI chat, describe the menu you want. For example:
   * `Add a header navigation bar with links to /Home and /Products.`
   * `Create a top navigation menu that includes Home and Contact.`
3. Once the AI has finished, check the preview to make sure the new navigation appears where you expect and test the links.

<Frame caption="Adding a navigation menu to the top of your app">
    <img src="https://mintcdn.com/base44/iEH4Y6BNLZQ0n0S-/images/navigationmenu.png?fit=max&auto=format&n=iEH4Y6BNLZQ0n0S-&q=85&s=b1b16b69281f4e976d3dcece6316a186" alt="Adding a navigation menu to the top of your app" width="1913" height="957" data-path="images/navigationmenu.png" />
</Frame>

### Adding a sidebar menu

1. Go to your app editor.
2. In AI chat, explain what you need. For example:
   * `Add a vertical sidebar navigation on the left with links to /Dashboard, /Reports, and /Settings.`
   * `Add a footer navigation with links to Privacy Policy and Terms of Service.`
3. Once the AI has finished, check the preview to make sure the new navigation appears where you expect and test the links.

<Frame caption="Adding a vertical sidebar navigation to your app">
  <img title="Verticalsidebar" className="hidden dark:block" src="https://mintcdn.com/base44/ZJy2_Y0URAmh8dUb/images/sidebar-1.png?fit=max&auto=format&n=ZJy2_Y0URAmh8dUb&q=85&s=5abec7be49c4b5275a10e2f79c08a81a" alt="Adding a vertical sidebar navigation to your app" width="1912" height="954" data-path="images/sidebar-1.png" />

  <img title="Verticalsidebar" className="dark:hidden" src="https://mintcdn.com/base44/ZJy2_Y0URAmh8dUb/images/sidebar.png?fit=max&auto=format&n=ZJy2_Y0URAmh8dUb&q=85&s=be39a3556cca1518542ca2cadc398b42" alt="Adding a vertical sidebar navigation to your app" width="1912" height="954" data-path="images/sidebar.png" />
</Frame>

### Changing the menu style

You can use different navigation styles to match your app’s layout and audience, such as a horizontal bar, tabs, or a hamburger menu that collapses on smaller screens.

**To change your navigation style with AI chat:**

1. Go to your app editor.
2. In AI chat, describe the style you want. For example:
   * Tabs: `Change the main navigation into a tab-style menu at the top of the page.`
   * Sidebar: `Move the navigation into a vertical sidebar on the left.`
   * Hamburger menu: `Turn the main navigation into a hamburger menu that opens a panel on the right.`
3. Once the AI has finished, check the preview to make sure the navigation appears where you expect and test the links.

<Tip>
  You can combine styles. For example, keep a horizontal menu with tabs on desktop and use a hamburger menu on smaller screens. Describe both behaviors clearly in your AI prompt.
</Tip>

### Changing the menu items

Once a navigation menu exists, you can add, remove, or rename links so people can reach the right pages. Make sure the page you want to link to already exists if you are adding a new item.

**To manage your menu items with AI chat:**

1. Go to your app editor.
2. In AI chat, describe how the menu should change. For example:
   * `Add a "Shop" link to the main navigation that points to the /Products page.`
   * `Add an "About" item to the top menu that links to /About and place it after Home.`
   * `Remove the "Blog" link from the header navigation.`
   * `Rename the "Shop All" menu item to "All Products".`
   * `Reorder the menu so that Home, Shop, About, and Contact appear in that order.`
3. Check the preview and click your menu items to confirm that everything looks and behaves as expected.

<Tip>
  If your app uses multiple navigation areas (such as a top menu and a footer menu), be specific in your prompt. For example: `Update only the header navigation, not the footer links.`
</Tip>

***

## Working with hidden pages

Some pages are meant to be internal, such as admin dashboards, success screens, or callback pages. You may want them available in your app without showing them in navigation or search results.

### Hiding pages from your menu

You can remove any page from your visible menus while still keeping it live and functional.

**To hide a page from your navigation with AI chat:**

1. Go to your app editor.
2. In AI chat, describe what should be hidden. For example:\
   `Remove the /Success page from all visible navigation, but keep it working as a redirect after checkout.`
3. Check that the link no longer appears in the header, sidebar, or footer.

<Frame caption="Creating internal hidden pages on your app">
  <img src="https://mintcdn.com/base44/iEH4Y6BNLZQ0n0S-/images/internalpage.png?fit=max&auto=format&n=iEH4Y6BNLZQ0n0S-&q=85&s=d81a88ccfa77a42ad5d2a66fe1ac3497" alt="Creating internal hidden pages on your app" className="mx-auto" style={{ width:"94%" }} width="1170" height="948" data-path="images/internalpage.png" />
</Frame>

<Note>
  A page that is hidden from your navigation can still be opened directly if someone knows its URL, or if you add a button or link to it elsewhere in your app.
</Note>

### Creating an admin-only area

You can keep sensitive pages, such as dashboards or management tools, available only to admins by placing them in an admin section of your navigation and protecting access.

**To create an admin-only navigation area with AI chat:**

1. Go to your app editor.
2. In AI chat, describe the admin section you want. For example:
   * `Add an Admin section in the sidebar that only admins can see, and move the /Wishlist page into it.`
   * `Create an admin-only area in the header navigation with links to /AdminDashboard and /Reports.`

<Frame caption="Creating an admin-only area on your app">
    <img src="https://mintcdn.com/base44/vyZ6HEARIdqrgiI1/images/adminaccess.png?fit=max&auto=format&n=vyZ6HEARIdqrgiI1&q=85&s=7058f1f0a828152f9803df3749a2a68c" alt="Creating an admin-only area on your app" width="1355" height="954" data-path="images/adminaccess.png" />
</Frame>

<Tip>
  To test your admin-only pages with **Act as**, click **Act as** in the preview toolbar, choose an admin role and check that the admin section and its pages are visible to them, then use **Act as** again to switch to a non-admin role and confirm that the admin section is hidden from the navigation and that admin-only pages cannot be opened directly.
</Tip>

### Hiding pages from search results

Base44 automatically includes all public, published pages in your sitemap at `/sitemap.xml` so search engines can find them. There are no per-page SEO switches such as “noindex” or page-level robots.txt controls.

To keep a page out of search engines, make sure the page is not public, or avoid linking to that page from any public parts of your app.

<Note>
  For full details on how indexing works, see our [SEO guide](/Performance-and-SEO/SEO-and-search-visibility).
</Note>

***

## Public landing page with private pages

Base44 does not currently support making some pages public and others private using visibility settings alone. Instead, you can use a combination of a public landing page and logic that redirects people to login for private areas.

**To set up a public landing page with login for other pages:**

1. Set your app to **Public (no login required)** in your app visibility settings.
2. Use the AI chat to create a landing page, for example:\
   `Create a landing page with login and sign-up buttons and make it my main page.`
3. Ask the AI to require login on the rest of your app. For example:\
   `Require login for all non-landing pages and redirect visitors who are not logged in back to the landing page.`

<Warning>
  It is not currently possible to mark individual pages as public or private using a per-page visibility setting. All visibility is controlled at the app level, combined with your routing and data access rules.
</Warning>

***

## FAQs

Click a question below to learn more about pages, login, and navigation.

<AccordionGroup>
  <Accordion title="How do I change the page people see first when they open my app?">
    **To change your landing page:**

    1. Click **Dashboard** in your app editor.
    2. Click **Settings** and then **App Settings**.
    3. In the **Main Page** drop-down under **General Settings**, select the page you want as your default landing page.

    You can also ask AI chat to change your landing page.
  </Accordion>

  <Accordion title="Are there limits on how many pages my app can have?">
    Yes. Base44 apps support up to 600 pages.

    If your app has more than 600 pages, you may see issues such as:

    * The builder becoming unavailable or very slow.
    * Pages not loading correctly in the editor or live app.
    * Publishing problems or errors when you deploy updates.

    **To stay within the limit:**

    1. Review your existing pages and remove any that are no longer needed.
    2. Consolidate similar content into fewer pages when possible.
    3. Use entities and filtered views instead of creating a separate static page for every item.

    Keeping your app below 600 pages helps the editor stay responsive and keeps your app stable.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).