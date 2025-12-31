# Source: https://docs.replit.com/tutorials/build-a-notion-powered-website.md

# Build a Notion-powered website

> Learn how to build a website that uses Notion as a Content Management System (CMS) with Replit Agent.

export const YouTubeEmbed = ({videoId, title = "YouTube video", startAt}) => {
  if (!videoId) {
    return null;
  }
  let url = "https://www.youtube.com/embed/" + videoId;
  if (startAt) {
    url = url + "?start=" + startAt;
  }
  return <Frame>
      <iframe src={url} title={title} allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowFullScreen></iframe>
    </Frame>;
};

export const AuthorCard = ({img = "https://replit.com/cdn-cgi/image/width=256,quality=80,format=auto/https://storage.googleapis.com/replit/images/1730840970400_e885f16578bbbb227adbfeb7b979be34.jpeg", href = "https://youtube.com/@mattpalmer", name = "Matt Palmer", role = "Head of Developer Relations"}) => {
  return <a href={href} target="_blank" className="card block not-prose font-normal group relative my-2 ring-2 ring-transparent rounded-xl bg-white/50 dark:bg-codeblock/50 border border-gray-100 shadow-md dark:shadow-none shadow-gray-300/10 dark:border-gray-800/50 overflow-hidden cursor-pointer hover:!border-primary dark:hover:!border-primary-light">
      <div className="flex items-center gap-2 p-4">
        <div className="flex-shrink-0">
          <img src={img} alt={name} className="w-12 h-12 rounded-full object-cover" />
        </div>
        <div className="flex-grow">
          <h3 className="text-base font-semibold mb-0.5 text-inherit">{name}</h3>
          <p className="text-sm text-gray-600 dark:text-gray-400 m-0">{role}</p>
        </div>
      </div>
    </a>;
};

<AuthorCard />

## Build a Notion-powered blog with Replit Agent

Notion is a powerful tool for organizing information, and it excels as a Content Management System (CMS). By integrating Notion with Replit, you can manage your website's content—like blog posts, portfolio items, or product listings—directly from your Notion workspace.

Replit, powered by [Replit Agent](/replitai/agent), handles the coding, hosting, and deployment, letting you go from idea to a published application quickly. Effective prompting is key to guiding Agent; for a comprehensive guide, see [Efficient prompting with Replit AI](/tutorials/effective-prompting) and [How to vibe code effectively](/tutorials/how-to-vibe-code).

<YouTubeEmbed videoId="AOYqTONf07o" />

This tutorial guides you through building a minimalistic blog that pulls its posts from a Notion table. You will:

* Use Replit Agent to generate the initial application
* Connect your Replit app to a Notion database
* Learn to guide the AI and troubleshoot common issues using effective prompting techniques
* Publish your blog for the world to see

<Frame caption="Final result: A minimalistic blog powered by Notion">
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/final-app.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=8189975b31f2c1c47e9e8577df926bd6" alt="Screenshot of the final Notion-powered blog application with minimalist design" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/tutorials/notion-cms/final-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/final-app.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=4a1d5fab430a210cca18b284813c447a 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/final-app.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b08d3bb340b624c1408d545797dbda29 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/final-app.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=f2b1c96fb54ce94d256ba433224fd0be 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/final-app.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=1576aade2b7a9f524bd0423af7491378 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/final-app.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d4984c2b9b145af5e09aa83a76201732 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/final-app.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=a2d9dcbfe9c7957f5ec7e82fb688c971 2500w" />
</Frame>

The tutorial will follow largely from the video above, but with some additional context and steps to help you understand the process.

## Prerequisites

To follow this tutorial, you'll need:

* A Replit account
* A Notion account
* Familiarity with basic Replit Agent interactions. If you're new to Agent, check out the [Replit Agent documentation](/replitai/agent).

## Step 1: Prepare your Notion database

Before prompting Agent, set up your content source in Notion. This involves thinking procedurally about what your blog needs, similar to planning a product.

<Steps>
  <Step title="Create a Notion integration">
    1. In Notion, go to **Settings & members** (usually in the top-left sidebar).
    2. Navigate to **Connections** (previously "Integrations").
    3. Select **Develop or manage integrations**.
    4. Select **+ New integration**.

    <Frame caption="Creating a new integration in Notion">
      <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-1.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=36613d11085fa2589511be942ce03218" alt="Notion developer portal showing the New integration button" data-og-width="3794" width="3794" data-og-height="2168" height="2168" data-path="images/tutorials/notion-cms/new-integration-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-1.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=81feec38d907347646b618ff3b0c08a1 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-1.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c53b0d36ec01bfa80d3fed53d8f09b7f 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-1.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d3343419910c313189c1a901ec13fbdb 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-1.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=bfea367a0c3841be7281a378263d4215 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-1.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=ff9ec4fd764606038549ad76406f31b2 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-1.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=f32d227d920dd933637a376e7ac883c1 2500w" />
    </Frame>

    5. Name your integration (e.g., "My Replit Blog Integration").
    6. Associate it with your desired workspace.

    <Frame caption="Configuring your Notion integration">
      <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-2.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=649a346838203ef40f1293f69125916f" alt="Notion integration configuration screen with name and workspace selection" data-og-width="3796" width="3796" data-og-height="2168" height="2168" data-path="images/tutorials/notion-cms/new-integration-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-2.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=cf5926f205c068ea4620fab22fc61b33 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-2.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=6d1998ee508320b3367c7f017b82b385 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-2.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c5dcb4b683b357eb2445fe55c9b245f0 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-2.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=723236fdf036b128c64034dbdf4c4f85 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-2.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=bb10e9c53dc7cd643ae7f984518fd687 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-2.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9e3bc12f8676abd057b0e5db679b8b21 2500w" />
    </Frame>

    7. For "Integration type," choose **Internal Integration**.
    8. Select **Submit**.
    9. Copy your **Internal Integration Secret** (token) and save it securely. This is your Notion API key.

    <Frame caption="Obtaining your Integration Secret">
      <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-3.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=22cb64a8c057b70293b955b0edcdb55d" alt="Notion integration secrets page showing the integration token" data-og-width="3796" width="3796" data-og-height="2168" height="2168" data-path="images/tutorials/notion-cms/new-integration-3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-3.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=72527c744a43e91967a81acc134e9efe 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-3.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=8fef1d4482a0e7e8c67de1ead99bb498 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-3.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=91c9276980d428afef4f6e49c136529a 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-3.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=69cb7fd38c3bec14b16d3e4ae928543e 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-3.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b7779aa0cfdadb237ba2378050312a23 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/new-integration-3.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=5a9b8ff8c36bc5fa6dca43edb3593962 2500w" />
    </Frame>

    10. Under **Capabilities**, ensure "Read content" is enabled. For this tutorial, reading is sufficient. If you later want to write data to Notion, enable "Insert content" and "Update content."

    <Info>
      Create a new integration for each project to manage permissions granularly. This is a security best practice.
    </Info>

    For more detailed instructions, refer to [Notion's official documentation on creating an integration](https://developers.notion.com/docs/create-a-notion-integration).

    You can directly access Notion's integrations dashboard at [notion.so/my-integrations](https://notion.so/my-integrations).
  </Step>

  <Step title="Create a Notion page with a database">
    1. Create a new page in Notion for your blog content.
    2. On this page, add a new **Table** database.
    3. Name your table (e.g., "Blog Posts").
    4. Define columns for your posts. **Specify** these clearly in your mind, as you'll soon tell Agent about them:
       * `Title` (Text, default title property)
       * `Body` (Text, for main post content)
       * `Slug` (Text, for URL-friendly identifiers)
       * `PublishedDate` (Date, or use "Created time" / "Last edited time")
       * `ReadingTime` (Text or Number, e.g., "5 min read")
       * `Description` (Text, short summary for previews)

    <Frame caption="Example Notion database setup for blog posts">
      <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/blog-posts.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=18b381c19ccdddc74a2c67a523400d60" alt="Notion database configured with columns for blog posts" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/tutorials/notion-cms/blog-posts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/blog-posts.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=15eedb79bc692f87683fb548b4e112d7 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/blog-posts.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=39d59dec94fcfe4a68ed5e08b0190335 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/blog-posts.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=b7a9a4fa92b23571d30c6af423ab487f 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/blog-posts.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=5c474b2739f43e1e1b870d8eaab7fabe 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/blog-posts.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=7882d16ad8630a009f5cfd2fa29ef717 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/blog-posts.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=c22f7f3fce25c0169110b5c59f5a0b52 2500w" />
    </Frame>

    5. Add a few sample posts. You can use Notion's AI features to help generate content!
  </Step>

  <Step title="Connect your integration to the page">
    1. Open the Notion page containing your database.
    2. Click the **•••** (three dots) menu in the top-right corner.

    <Frame caption="Access the integration menu in Notion">
      <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=20d1052e1ec46366a2727cce6bcf0c50" alt="Notion connections menu showing how to add your integration to the page" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/tutorials/notion-cms/add-integration.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=6b6ecd6f718989b71b247d06f7d28deb 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d777146a4cbc6b3361f81fdedb9232f5 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=417244e225be5cfb1482e80279bbd50a 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=499b8f6c584c1a635a9821a4f148208b 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=cb2e8617bdb29d48858b83a1f1b81c65 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=6771d45d50ddabee26b92d3fd6f8dcbd 2500w" />
    </Frame>

    3. Select **+ Add connections**.
    4. Search for and select the integration you created (e.g., "My Replit Blog Integration").

    <Frame caption="Adding your integration to the Notion page">
      <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration-menu.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=f3c0325b2e9e8de79b8b7b126974b636" alt="Notion page showing the three dots menu to add integrations" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/tutorials/notion-cms/add-integration-menu.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration-menu.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=1842e5114825b3d8122e917bb4c86d6d 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration-menu.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=3febebd4eed713135de0c7fabe9c3af0 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration-menu.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=80da050fbbb7a6d4053f754267e56423 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration-menu.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=9f1037113c72da931b4144980bb4a377 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration-menu.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=290696b8009e1c9fa0ece26b371a85b3 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-integration-menu.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=1f971324bc7c8aaf9ddfef1bfa1025c1 2500w" />
    </Frame>

    5. Confirm the connection. This allows Replit (via the integration token) to access this page and its database.
  </Step>
</Steps>

## Step 2: Prompt Replit Agent

With Notion set up, let's get Replit Agent to build our blog's foundation. **Plan before you prompt**: a clear outline of features leads to more focused prompts.

<Steps>
  <Step title="Open Replit Agent">
    Navigate to the Replit homepage and open **Agent**.
  </Step>

  <Step title="Write your prompt">
    Provide Agent with a detailed prompt. **Simplify** your language, but be **specific** about requirements, constraints, and desired outputs. Here's an example:

    ```text  theme={null}
    Help me create a hyper-minimalistic blog using Notion as a CMS.
    The blog should pull posts from a Notion page.
    The table on the Notion page has the following columns: Title, Body, Slug, PublishedDate, ReadingTime, Description.
    You should generate a slug for each post based on its title if the Slug column is empty.
    Make the blog theme black with white text. Keep it extremely minimal.
    The posts should be listed on the homepage, and clicking a post should navigate to a page displaying the full post content.
    ```

    <Tip>
      For more tips on writing effective prompts, see our guide on [Efficient prompting with Replit AI](/tutorials/effective-prompting).
      You can also **show** Agent what you mean by providing a URL to scrape for initial styling or content ideas (e.g., your personal portfolio) by adding: `Scrape the content of [URL] for initial design inspiration and placeholder text.`
    </Tip>

    Agent will generate a plan. Review it to ensure it aligns with your expectations, then approve it. This is your first **checkpoint** in the AI-assisted building process.
  </Step>

  <Step title="Review the initial preview">
    Agent will then generate a visual preview. Check if the basic layout and styling are heading in the right direction. Refinements will come later.
  </Step>
</Steps>

## Step 3: Connect Replit to Notion with Secrets

Agent will likely need your Notion integration details to fetch data.

<Steps>
  <Step title="Add Secrets in Replit">
    Typically, you'll need:

    1. `NOTION_API_KEY`: Your Internal Integration Secret from Step 1.
    2. `NOTION_DATABASE_ID`: The ID of your Notion database.

    **How to find your Notion Database ID:**

    * Open your Notion page with the database in a browser.
    * The URL might be `https://www.notion.so/your-workspace/PAGE_TITLE-PAGE_ID?v=DATABASE_VIEW_ID`. The `PAGE_ID` is often the database ID if the database is the page's main element.
    * **More reliably**: Click the **•••** menu on your database view, select **Copy link to view**, and paste it. The link `https://www.notion.so/your-workspace/DATABASE_ID?v=VIEW_ID` contains the `DATABASE_ID` before `?v=`.

    Go to the **Secrets** tool (🔒 icon) in your Replit Workspace. Add these:

    * Key: `NOTION_API_KEY`, Value: `[Your_Notion_Integration_Secret]`
    * Key: `NOTION_DATABASE_ID`, Value: `[Your_Notion_Database_ID]`

    <Frame caption="Adding your Notion secrets to Replit">
      <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-secrets.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d96b903522fbf7e189c77d3c1901352e" alt="Replit Secrets tool with Notion API key and Database ID added" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/tutorials/notion-cms/add-secrets.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-secrets.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=38bed2d393b7af8798f04f5673b1f1fd 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-secrets.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=8429940773b23673eb3eca774b4326de 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-secrets.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=67c13ee1b8487c82cbdb519c7dcaaea3 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-secrets.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=e32d921c6d87c3f5d50e61ae2f729e3d 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-secrets.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=dd586dce1d6e3ef089e6d34a28ec4baa 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/add-secrets.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=76482c549e2d36d986f63c198f1d30a5 2500w" />
    </Frame>

    Agent should automatically use these secrets and attempt to connect. The app will likely restart.
  </Step>
</Steps>

## Step 4: Debugging and refining with Agent

Building with AI is iterative. Expect errors or imperfections. This is where guiding the AI effectively—often called "vibe coding"—is key. For a deeper dive into this skill, check out our tutorial on [How to vibe code effectively](/tutorials/how-to-vibe-code). **Master context** by providing only relevant information for each debugging step.

<Tip>
  Keep the **Console** in your Replit Workspace open. It provides valuable error messages and logs.
</Tip>

<Frame caption="Debugging your Notion app using the Replit Console">
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/console-debug.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=7cc562bec25b26e5302b74793f002c00" alt="Replit Console showing error messages while debugging the Notion integration" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/tutorials/notion-cms/console-debug.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/console-debug.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=e6399abbb7c6c41023513d08a89e6fd0 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/console-debug.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=4ad41a570d3ccef91c7c9b380448dc83 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/console-debug.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=8ac0665c3d46ede6b4202767461420a1 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/console-debug.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=e1c8668e8b2123ddcb54b8985f4e8f91 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/console-debug.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=5ab861d7d1ada3c00ae6ab69d7435597 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/console-debug.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=f2e0aab2d0a1714947757060644317cc 2500w" />
</Frame>

Here are common scenarios and how to address them by **debugging methodically**:

### Scenario 1: "Failed to load posts" or property errors

#### Symptom

The app runs but doesn't display posts. Console errors might mention "Could not find sort property with name ID created\_time" or other column mismatches.

#### Cause

Agent might assume column names or properties (e.g., `created_time` for sorting) that don't exist or are named differently in your Notion database.

#### Troubleshooting

1. **Verify Notion Database**: Ensure column names in your database exactly match Agent's expectations or your prompt. If Agent seeks `created_time` and you have `PublishedDate`, it's a mismatch.
2. **Prompt Agent with error (Debug principle)**: Copy the *exact* console error and **select** relevant code snippets if you've identified them. Provide this focused context to Agent:
   ```text  theme={null}
   There's an error fetching posts. Console: "Could not find sort property with name ID created_time".
   My Notion database uses 'PublishedDate'. Please use this for sorting/fetching. Here's the suspected code from `services/notion.js`: [code snippet]
   ```
3. **Iterate (Experiment principle)**: If Agent's fix fails, provide more specifics. "Posts still not loading. Error persists. Show me the code for fetching/sorting Notion posts." If you added a column like `created_time` in Notion as a quick fix, you can later ask Agent: "Remove reliance on 'created\_time', use 'PublishedDate' instead." Remember to use Agent's **Checkpoints** to save working states.

### Scenario 2: Incorrect data display or formatting

#### Symptom

Data appears, but incorrectly (e.g., reading time wrong on homepage but right on post page; Markdown rendering issues).

#### Troubleshooting

1. **Be specific (Specify principle)**: Describe the issue and location clearly:
   ```text  theme={null}
   On the homepage, post reading time is incorrect, but it's correct on individual post pages.
   Also, display 'PublishedDate' on the homepage for each post summary.
   ```
2. **Markdown issues (Show principle)**: If Notion "Body" Markdown renders incorrectly (e.g., extra spaces, formatting errors):
   * Inspect raw content in Notion; its formatting can introduce subtle characters.
   * Prompt Agent clearly. You can even **show** an example:
     ```text  theme={null}
     Markdown rendering issue: In post X, bold text like '**this**' appears as ' ** this **' and fails to render. Ensure Markdown parsing handles such cases or trims whitespace. Example of correct rendering for bold: **This is bold**.
     ```
   * Testing with known good Markdown (e.g., from ChatGPT pasted into Notion) can isolate if the issue is source data or rendering logic.

### General debugging flow

1. **Observe**: Note the error or incorrect behavior.
2. **High-level prompt (Simplify)**: Describe the problem to Agent clearly.
3. **Check Console/DevTools (Debug)**: Look for detailed errors.
4. **Iterate & provide context (Select, Show)**: If Agent's fix fails, provide more context (error message, relevant code, your goal, attempts made).
5. **Incremental changes (Checkpoint)**: Ask Agent to fix one thing at a time. Use **Checkpoints** in Agent to save progress.
6. **Rollback**: If prompts worsen things, roll back to a working **Checkpoint** and try a new approach.

<Note>
  Don't hesitate to examine Agent-generated code. Even without expertise in the language, you can often spot logical issues or understand data flow, helping you write better prompts. Files like `notionService.js` usually handle Notion API calls.
</Note>

## Step 5: Further enhancements

Once core functionality works, ask Agent to add features. Use positive, direct language (**Instruct** principle). Here are ideas:

<AccordionGroup>
  <Accordion title="Implement caching and prefetching">
    Ask Agent: "Implement post caching and prefetching from Notion for a super-fast site."
    This reduces Notion API calls and speeds up page loads.
  </Accordion>

  <Accordion title="Enhance styling">
    Ask Agent: "Add a hover effect to homepage blog post links." or "Improve post typography for readability."
    Small visual tweaks significantly improve user experience. You can **show** Agent examples of styles you like.
  </Accordion>

  <Accordion title="Configure data refresh strategy">
    Consider how often to fetch new Notion data. For simple blogs, on page load or server restart might be enough.
    For dynamic content, ask Agent: "Explore options to auto-refresh Notion posts hourly." This might involve background polling (adds complexity but keeps content current).
  </Accordion>
</AccordionGroup>

## Step 6: Publish your website

Happy with your site? Time to share it!

1. Select **Publish** in the Replit Workspace (top right).
2. Review publishing settings (project name, tier). For more details, see [About Deployments](/cloud-services/deployments/about-deployments).
3. Select **Publish**.

<Frame caption="Publishing your Notion-powered website">
  <img src="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/deploy.png?fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=3f5a9b1b5946fc3461fc8e93f29dcac9" alt="Replit publishing interface showing how to publish your Notion-powered website" data-og-width="3840" width="3840" data-og-height="2160" height="2160" data-path="images/tutorials/notion-cms/deploy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/deploy.png?w=280&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=2da4307be0e126b9b9b3328aee7bb7fa 280w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/deploy.png?w=560&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=ae31ea8f23b5d4fb416b0c08dbf9e06a 560w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/deploy.png?w=840&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=19bb17274ef2769e0bf171fcf393fa60 840w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/deploy.png?w=1100&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=d8d393879026cfcabeadfe5d233c6f3a 1100w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/deploy.png?w=1650&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=852b74fb110a9b2d2cefacb4dc6079aa 1650w, https://mintcdn.com/replit/0ixNWaRF232g0Gwn/images/tutorials/notion-cms/deploy.png?w=2500&fit=max&auto=format&n=0ixNWaRF232g0Gwn&q=85&s=be9341bf862c08ed7ae070b88a231986 2500w" />
</Frame>

Replit builds, bundles, and publishes your app to a public URL.

## What you've learned

By following this tutorial, you've learned to:

* Set up Notion as a CMS with an integration and structured database
* Prompt Replit Agent to build a web app connected to Notion, applying principles like **planning, specifying, and simplifying**
* Securely manage API keys using Replit Secrets
* Iteratively debug and refine an AI-generated app using techniques like **providing context, showing examples, and using checkpoints**
* Publish your Notion-powered website on Replit

For detailed information about checkpoints and rollbacks, see [Checkpoints and Rollbacks](/replitai/checkpoints-and-rollbacks).

Building with AI like Replit Agent is collaborative. Procedural thinking, clear instructions, and methodical debugging are crucial for turning ideas into reality, fast.

## Next steps

Continue developing your Notion-powered website:

<AccordionGroup>
  <Accordion title="Experiment with content types">
    Try adding diverse content from Notion: image galleries, embedded videos, or categorized items.
  </Accordion>

  <Accordion title="Leverage advanced Notion features">
    Explore Notion's formulas, rollups, and relations for complex data structures. Work with Agent to display this rich data on your Replit site.
  </Accordion>

  <Accordion title="Combine with other Replit integrations">
    Enhance your app by merging Notion data with other [Replit AI](/category/replit-ai) tools or [Agent integrations](/replitai/integrations). For example, use Replit Auth for private content or OpenAI for AI-generated summaries from Notion data within your app.
  </Accordion>
</AccordionGroup>

Happy building! We can't wait to see what you create.
