# Source: https://docs.asapp.com/generativeagent/configuring/connecting-your-knowledge-base.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connecting your Knowledge Base

> Learn how to import, sync, and deploy your Knowledge Base for GenerativeAgent.

Your knowledge base is crucial for GenerativeAgent to provide accurate and contextually relevant responses to users. You have full control over which articles you include, their update frequency, and how you deploy those updates.

All content and update management occurs within the ASAPP dashboard.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6a3bd50e-2c74-39f2-9b37-2453e719cda5.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=e817381078ff093b959fcbde4d20a2ec" data-og-width="2048" width="2048" data-og-height="1294" height="1294" data-path="image/uuid-6a3bd50e-2c74-39f2-9b37-2453e719cda5.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6a3bd50e-2c74-39f2-9b37-2453e719cda5.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=62497f327b17c0673cfae8af229139a6 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6a3bd50e-2c74-39f2-9b37-2453e719cda5.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=0d501ab9e729d94aa7a280218cd94e22 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6a3bd50e-2c74-39f2-9b37-2453e719cda5.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=0103c9a8cf6bbadab0a68141bf65e377 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6a3bd50e-2c74-39f2-9b37-2453e719cda5.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=c795c116119bf57df8c195e2bb3d2971 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6a3bd50e-2c74-39f2-9b37-2453e719cda5.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=31d45539ac56cc7a7fa351feea76aa99 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6a3bd50e-2c74-39f2-9b37-2453e719cda5.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=bf8c5f27b70f3694657274bcfb2d44bb 2500w" />
</Frame>

GenerativeAgent's Knowledge Base is designed to store reference material that GenerativeAgent can use to answer a variety of customer questions—both explicit (“What is the return policy?”) and implicit (“I don't understand ‘eligible for store credit’”).

GenerativeAgent determines if a question should be answered from the Knowledge Base and searches for the most relevant content.

To configure your Knowledge Base, you need to:

1. Import your knowledge base
2. Configure sync and deployment preferences
3. Deploy knowledge base articles

<Note>
  Do not upload internal, agent-facing knowledge base material intended only for live agents. Use GenerativeAgent’s task instructions for internal-only guidance.
</Note>

## Step 1: Importing Your Knowledge Base

You can import content by:

* Navigating to GenerativeAgent > Knowledge in the ASAPP dashboard
* Clicking **Add content**
* Choosing from:
  * **Import from URL**
  * **Create Snippet**
  * **Add via API**

<Tabs>
  <Tab title="Import from URL">
    Importing from a URL lets you specify a site or page for the crawler to harvest articles.

    1. Select **Import from URL**
    2. Enter the URL to start the import
    3. (Optional) Use URL Prefixes or Excluded URLs to target specific sections

    <Frame>
      <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ExcludeURLs.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=19f7bb548136e0218ede267b3e87cd1b" data-og-width="1009" width="1009" data-og-height="240" height="240" data-path="images/generativeagent/ExcludeURLs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ExcludeURLs.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=66b8c25c02bb08355d0353d5e2fcf799 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ExcludeURLs.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=334fd37d2f74515ac5c5c3cbe41edf18 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ExcludeURLs.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=24ad30a9c7146f9e31811bb4a0dcb931 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ExcludeURLs.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=a9f46b133972355006eeaba078a6520d 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ExcludeURLs.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=9bbeb8b51545219df0affcf6313c4ad2 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ExcludeURLs.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=b87acc41d381cfffa0cf522062ccc4da 2500w" />
    </Frame>

    <Frame>
      <img src="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/url_prefix.png?fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=508d717961e37e309cc55f99aec084bf" data-og-width="980" width="980" data-og-height="134" height="134" data-path="images/generativeagent/url_prefix.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/url_prefix.png?w=280&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=8252f1cb82c1b309d362422c4108e189 280w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/url_prefix.png?w=560&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=29bc0fb9c1ec9697b6497e1bff3c642c 560w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/url_prefix.png?w=840&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=e5ca50f4c1cbbc33fdb327649e20003a 840w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/url_prefix.png?w=1100&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=1eadbfc690f7a26fcf1cebc1900289df 1100w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/url_prefix.png?w=1650&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=c942fa3df6b8b2673ade8ab0c5e40b89 1650w, https://mintcdn.com/asapp/bSPknm73NAzIX3Ak/images/generativeagent/url_prefix.png?w=2500&fit=max&auto=format&n=bSPknm73NAzIX3Ak&q=85&s=94713b14683fcd02d00b103b79ee12de 2500w" />
    </Frame>
  </Tab>

  <Tab title="Import from Zendesk KB">
    Importing from Zendesk KB lets you import articles from your Zendesk Knowledge Base.

    1. Select **Import from Zendesk KB**
    2. Enter your Zendesk subdomain. This is the unique identifier for your Zendesk account.
    3. Enter your Zendesk API credentials as an Authentication Method.
    4. Optionally specify how to filter the content by:

    * Locale
    * Categories
    * Sections
    * Labels

    <Frame>
      <img src="https://mintcdn.com/asapp/lmYFI1iPuxPVNIzz/images/generativeagent/configuring/zendesk-kb-options.png?fit=max&auto=format&n=lmYFI1iPuxPVNIzz&q=85&s=fed3fc294f77dc3753d701b2a988c7bf" data-og-width="2190" width="2190" data-og-height="1918" height="1918" data-path="images/generativeagent/configuring/zendesk-kb-options.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/lmYFI1iPuxPVNIzz/images/generativeagent/configuring/zendesk-kb-options.png?w=280&fit=max&auto=format&n=lmYFI1iPuxPVNIzz&q=85&s=920a5ffba2152bb726c15bc202361a59 280w, https://mintcdn.com/asapp/lmYFI1iPuxPVNIzz/images/generativeagent/configuring/zendesk-kb-options.png?w=560&fit=max&auto=format&n=lmYFI1iPuxPVNIzz&q=85&s=23eec8bb61686ae213efe57f9398b6c7 560w, https://mintcdn.com/asapp/lmYFI1iPuxPVNIzz/images/generativeagent/configuring/zendesk-kb-options.png?w=840&fit=max&auto=format&n=lmYFI1iPuxPVNIzz&q=85&s=4d332de35b8a16efb15a7100a3d25c7c 840w, https://mintcdn.com/asapp/lmYFI1iPuxPVNIzz/images/generativeagent/configuring/zendesk-kb-options.png?w=1100&fit=max&auto=format&n=lmYFI1iPuxPVNIzz&q=85&s=e691b84de7a7c2e0eb76a584540a2c46 1100w, https://mintcdn.com/asapp/lmYFI1iPuxPVNIzz/images/generativeagent/configuring/zendesk-kb-options.png?w=1650&fit=max&auto=format&n=lmYFI1iPuxPVNIzz&q=85&s=731f279eaf8b054477829157b3ffb84b 1650w, https://mintcdn.com/asapp/lmYFI1iPuxPVNIzz/images/generativeagent/configuring/zendesk-kb-options.png?w=2500&fit=max&auto=format&n=lmYFI1iPuxPVNIzz&q=85&s=3d635f343b4465a4b1b65869f11e6657 2500w" />
    </Frame>
  </Tab>

  <Tab title="Create Snippet">
    Snippets are stand-alone articles created manually.

    1. Click **Create Snippet**
    2. Enter the article’s title and content
    3. Optionally add instructions and metadata

    <Frame>
      <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a5f488c1-8d55-60fa-2b18-c2b185fb5546.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=69d690c22eb3c2d28439f3261c6d17d6" data-og-width="2880" width="2880" data-og-height="1872" height="1872" data-path="image/uuid-a5f488c1-8d55-60fa-2b18-c2b185fb5546.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a5f488c1-8d55-60fa-2b18-c2b185fb5546.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2e8d6dc64bf496f99c79b0f2a51616dd 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a5f488c1-8d55-60fa-2b18-c2b185fb5546.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=097f2061662791514f7b28ebe3e770e8 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a5f488c1-8d55-60fa-2b18-c2b185fb5546.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=aa9d51846ce52e9f78b5ba5508a0acff 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a5f488c1-8d55-60fa-2b18-c2b185fb5546.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e73e72c63f506b24ab151d18a2eacadd 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a5f488c1-8d55-60fa-2b18-c2b185fb5546.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c172cd47abf8b20da97ee4ae035727bd 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a5f488c1-8d55-60fa-2b18-c2b185fb5546.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=b5d203e9aa6aa090b17f4f808a110073 2500w" />
    </Frame>
  </Tab>

  <Tab title="Add via API">
    Programmatically add or update articles using the Knowledge Base Article Submission API.

    <Frame>
      <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2a26fb87-81b2-e453-8307-d0d62b33b117.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=bae5c631c716009085e7bf17ac2bb481" data-og-width="1440" width="1440" data-og-height="900" height="900" data-path="image/uuid-2a26fb87-81b2-e453-8307-d0d62b33b117.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2a26fb87-81b2-e453-8307-d0d62b33b117.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a3cac8431d49dfd6e5f4a1a2a8dd08e0 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2a26fb87-81b2-e453-8307-d0d62b33b117.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=bfbbb2c334af89c505a487a7e4d81412 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2a26fb87-81b2-e453-8307-d0d62b33b117.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=9aa5301132911d347b7cc267070e870f 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2a26fb87-81b2-e453-8307-d0d62b33b117.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=438ddb21a6068a3fa722ba9a82284200 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2a26fb87-81b2-e453-8307-d0d62b33b117.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0a9c5e9ef6a986674ba34ac56dc6d5cb 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2a26fb87-81b2-e453-8307-d0d62b33b117.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=669c3a6213e9c04271b6319c60b8d5db 2500w" />
    </Frame>
  </Tab>
</Tabs>

## Step 2: Configure Sync & Deployment Preferences

When adding or modifying a content source, you now have advanced control over how and when it syncs and how updates are deployed to production.

**Automatic update options:**

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d60991544408edcc59048fe3e016d82f" alt="Automatic updates dialog" data-og-width="2218" width="2218" data-og-height="1022" height="1022" data-path="images/generativeagent/KBAutoDeploy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7507be3f1bfa199d78945a8d1cfecec0 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8cb94ed1f45d413852348bc548acf2ac 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=25b57b54afc7b31666f5cbd710b16f7a 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7955403056759a22955512bac5dc3ffe 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8b85131a343f9c67317e5844e2e4e57c 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBAutoDeploy.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7e4a97f2e29c37bd791da2d02b665fc7 2500w" />
</Frame>

* **Enable with review notification**\
  Scrapes and cleans content every 24 hours. Updates require manual review before deployment.
* **Enable with auto-deployment**\
  Scrapes and cleans content every 24 hours. The system *immediately* deploys updates to production, bypassing the review process.
* **Turn off**\
  Import content only once. No automated updates.

> You can adjust this setting anytime in the content source management screen. The system visually indicates the current sync mode for each source.

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBLastActivityAutoDeploy.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=1b0293d1770a76dc9d46614ac8a6358a" alt="Auto-deploy indicator in Production table" data-og-width="640" width="640" data-og-height="348" height="348" data-path="images/generativeagent/KBLastActivityAutoDeploy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBLastActivityAutoDeploy.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0f1981047af2604d7567a9531a84f23a 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBLastActivityAutoDeploy.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=52d568402102adf4e8ca35cd0d21536c 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBLastActivityAutoDeploy.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0256e93fdb9614c837396953de07c6de 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBLastActivityAutoDeploy.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=f6169b9447fd48e5fd3dca98e1ba08df 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBLastActivityAutoDeploy.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=84be7b5556a89581a0a3e0599146c6ad 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBLastActivityAutoDeploy.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=49f16e6042f43ff42ac283a28726aa83 2500w" />
</Frame>

## Step 3: Article-Level Frequent Refresh (Critical Updates Only)

You can override the sync and deployment setting of the content source for specific, time-sensitive articles:

1. Click the three-dot menu next to the article and select **Set refresh frequency**.

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=e8ef182fb1cf1f2c7139de01dbe60fdd" alt="Set refresh frequency dropdown" data-og-width="376" width="376" data-og-height="344" height="344" data-path="images/generativeagent/KBSetRefreshFrequency.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=2edbfa7b937723b29b4bcab5999e467f 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=8304bfa59b4618879af32812345c6ae0 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=1ed571410ee2461d72b66a2e9ee86f26 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=f7a283bbe5c1837ce5195996a463f6be 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=e187d58610367d1bec8c208d073f3204 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0fd1ec805f4d1568ae4aee8ea147dfa6 2500w" />
</Frame>

2. In the dialog, enable **refresh frequency** for updates every 15 minutes.
   * The system will auto-deploy updates to production immediately, even if your content source normally requires review.
   * Disabling will revert to the content source's settings.

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a83e93fa21e826debd49bc49e88fff63" alt="Set refresh frequency dialog" data-og-width="1316" width="1316" data-og-height="540" height="540" data-path="images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=2d57d236b38ad6492f9eada2265d2682 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=bad9a018dd06e44c30c2f12912788767 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=660032038785ca09c4acf3c19e70c2d9 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0a8170d814a39560ee47ff7b7b702f78 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=36703d8d7a2cb4f6191ead166d7b11ee 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSetRefreshFrequency_DialogAutoDeploy.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=59ea85fd895c31174dd0255e761eae04 2500w" />
</Frame>

<Warning>
  Use frequent refresh and auto-deploy only for critical, time-sensitive articles (e.g., live incident or service disruption updates). These changes will go live immediately without review.
</Warning>

## Step 4: Deploying Your Knowledge Base

Once imported and configured, deploy your Knowledge Base and changes to your desired environment for GenerativeAgent. This ensures users receive the most accurate and timely information.

You manage deployment as part of the [generative agent deployment process](/generativeagent/configuring/deploying-to-generativeagent).

## Reviewing Imported Articles

By default, imported articles (from URL/API) require review and publishing (unless auto-deploy is enabled for the source or article).

If articles are pending review, a banner will appear at the top of the Knowledge Base page.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6980a63d-3e9a-1ddd-1eb3-5395d3ece938.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=6d2ea451e3984b9d594e94bed08d9dbd" data-og-width="2880" width="2880" data-og-height="1820" height="1820" data-path="image/uuid-6980a63d-3e9a-1ddd-1eb3-5395d3ece938.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6980a63d-3e9a-1ddd-1eb3-5395d3ece938.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=0ee610d65738bb588efbe68bbaab9c5b 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6980a63d-3e9a-1ddd-1eb3-5395d3ece938.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=2ceacb9f9b7a98d5ef51a58402b8b098 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6980a63d-3e9a-1ddd-1eb3-5395d3ece938.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=5b2ee7dfe8102cf0f91cdd6a47172ae7 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6980a63d-3e9a-1ddd-1eb3-5395d3ece938.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=b4bb543cde9666d1c144cb5795b1f66f 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6980a63d-3e9a-1ddd-1eb3-5395d3ece938.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=905da39bfe767b67a7baa917fab97e81 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-6980a63d-3e9a-1ddd-1eb3-5395d3ece938.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1a4cc78355c93f76e4716355e49baa5d 2500w" />
</Frame>

You can choose between a cleaned-up or raw version of each article before publishing.

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DetailedReview.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=0685331e2e0d35d33014d06360c1b670" data-og-width="1600" width="1600" data-og-height="991" height="991" data-path="images/generativeagent/DetailedReview.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DetailedReview.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=cb6794c09344d5eeb57abd429a9f1370 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DetailedReview.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=043cccf33fea1428b1fb9fe55490ff47 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DetailedReview.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=a5f568c7274ed2ccb421ab34d2a53914 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DetailedReview.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=a8610d50653b9edfeb1ad7c0887a766e 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DetailedReview.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=ca463d5f5caccff0f7fe0b6f841ecdac 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/DetailedReview.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=9ff6cc31d23db3891dbba86ec33bf2d3 2500w" />
</Frame>

> If the system updates an article (by new crawl or API update), the same rules apply:
>
> * Requires re-review if the parent content source is in review mode
> * Deploys instantly if in auto-deploy or frequent refresh mode

## Visual Indicators & Notifications

* The system shows sync and deployment status both for sources and individual articles.
* Recent auto-sync and deployment activity can be reviewed in audit logs or dashboards.

***

## Optimizing GenerativeAgent Article Usage

Boost GenerativeAgent’s accuracy and retrieval behavior by leveraging:

### Query Examples

Add typical customer questions to help surface relevant content:

1. In the “GenerativeAgent Instructions” column, click **Add query example**
2. Enter common questions as needed

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a6143054-92eb-a857-86e5-35434a80907a.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=3bcef58bc85896e79a9a8fc86ca86631" data-og-width="393" width="393" data-og-height="313" height="313" data-path="image/uuid-a6143054-92eb-a857-86e5-35434a80907a.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a6143054-92eb-a857-86e5-35434a80907a.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=08b4bd98328e4867e2813b20f2eb28e1 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a6143054-92eb-a857-86e5-35434a80907a.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=1bca2e4e00674ffaf84187704c296070 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a6143054-92eb-a857-86e5-35434a80907a.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=10093228afbdeaeb6d69f8d8cd02e3c1 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a6143054-92eb-a857-86e5-35434a80907a.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=78b97baf4b3e846950b2009b6db66327 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a6143054-92eb-a857-86e5-35434a80907a.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=8bc1cbdcbe4872de91889dc0cea0117f 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-a6143054-92eb-a857-86e5-35434a80907a.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e4b7a39b8263f188d9627b075d4681ed 2500w" />
</Frame>

### Additional Instructions

Provide special clarifications or company-specific answers:

1. Click **Add Instruction**
2. Write a clear clarification or sample response

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2165b887-ca8e-b93b-975a-03c9ec4eadbf.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=e7ed1a307a0f1d20f3fc33f27dff31f2" data-og-width="281" width="281" data-og-height="230" height="230" data-path="image/uuid-2165b887-ca8e-b93b-975a-03c9ec4eadbf.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2165b887-ca8e-b93b-975a-03c9ec4eadbf.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=6b77043cfea15a8b080f372a23e221a1 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2165b887-ca8e-b93b-975a-03c9ec4eadbf.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=7f12446b4eaa5503220d1559d2ffe06a 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2165b887-ca8e-b93b-975a-03c9ec4eadbf.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=578fbc8df1ab5dd895ccbe18a62d8ac0 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2165b887-ca8e-b93b-975a-03c9ec4eadbf.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=b8d9d4a50b7ee3608a0e6fb92d754afe 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2165b887-ca8e-b93b-975a-03c9ec4eadbf.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=0e3923c048d5e0e42a9f0359ed8c5f6a 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-2165b887-ca8e-b93b-975a-03c9ec4eadbf.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=051dee07a92ea37986d6256e901fbe9a 2500w" />
</Frame>

### Article Metadata

Use metadata to ensure GenerativeAgent uses specific articles only for relevant tasks.

1. Navigate to the article and click **Edit Metadata**.
2. Add or modify metadata keys to enable targeted article discovery and control.

### Search & Filter

Easily find or bulk manage articles using metadata, status, content source, creator, or deployment state.

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchBar.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=e32dbfe068dee83806e96a357d66c7da" data-og-width="1600" width="1600" data-og-height="1011" height="1011" data-path="images/generativeagent/KBSearchBar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchBar.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=03edbb5f3379ad75ac3b739257b242e5 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchBar.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=aec9b25d105c3c34ea5bfabd9cdb5cb1 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchBar.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=625cf866735471d41a4e17df24d1fe0c 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchBar.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=3264691c561185921860d39f12a54513 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchBar.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=365cd247779f930b7886153d8d1a9a46 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchBar.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7c7fd23d98c535c71624cd5b0efea095 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchFilters.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d0e0279bda18cc8a27f50535889d1b42" data-og-width="1148" width="1148" data-og-height="708" height="708" data-path="images/generativeagent/KBSearchFilters.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchFilters.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=b9f3666aa56576ad45a9ffedd9d34575 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchFilters.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=361d8362187292af0cb5588511a0ebb5 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchFilters.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=be08b17801807f52ed5a3d2b5f4abb2c 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchFilters.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0462f01f70f03a2a1479f3c9c97d05ad 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchFilters.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=cdbbc46e1b966b58a6c4b16466ee9e14 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/KBSearchFilters.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=44a54b3965d248fa32d0ff69ed82e6ae 2500w" />
</Frame>

<Note>
  You can select and combine multiple filters with "AND" for precise searching.
</Note>

## Preview

Quickly test live how GenerativeAgent uses your knowledge base:

1. Click the eye icon next to "Deploy"

<Frame>
  <img src="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-357991fb-7e28-1e16-80eb-4861ec9bc6ef.png?fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=855f9e8b60cc8fc46aacc5aff91c01dd" data-og-width="278" width="278" data-og-height="437" height="437" data-path="image/uuid-357991fb-7e28-1e16-80eb-4861ec9bc6ef.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-357991fb-7e28-1e16-80eb-4861ec9bc6ef.png?w=280&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=a5e837fc2bb7171e77332694fa76f412 280w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-357991fb-7e28-1e16-80eb-4861ec9bc6ef.png?w=560&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=1e7773e2258d001e48778c18b708d44a 560w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-357991fb-7e28-1e16-80eb-4861ec9bc6ef.png?w=840&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=92e2cacc850862cdff10bb6807a046a7 840w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-357991fb-7e28-1e16-80eb-4861ec9bc6ef.png?w=1100&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=7b5bcc28633ecc87b35056dafcb48747 1100w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-357991fb-7e28-1e16-80eb-4861ec9bc6ef.png?w=1650&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=d09a0edf8e9cf4843e209ec199cead03 1650w, https://mintcdn.com/asapp/BoXlOITRW7VjgmOG/image/uuid-357991fb-7e28-1e16-80eb-4861ec9bc6ef.png?w=2500&fit=max&auto=format&n=BoXlOITRW7VjgmOG&q=85&s=91c6f2215a1541450eaa04ec86ce5fc2 2500w" />
</Frame>

2. Start a test conversation to see answers pulled from your knowledge base

<Frame>
  <img src="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8a53588-8543-d39d-a267-cd8d7e793be6.png?fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=7cccd161029a1d7169639361d95dcd2a" data-og-width="534" width="534" data-og-height="520" height="520" data-path="image/uuid-a8a53588-8543-d39d-a267-cd8d7e793be6.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8a53588-8543-d39d-a267-cd8d7e793be6.png?w=280&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=24b1ba023842d0bb59f456bd934cf7ff 280w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8a53588-8543-d39d-a267-cd8d7e793be6.png?w=560&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=b96e4fa07de40ba235d9237b7a4abf9b 560w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8a53588-8543-d39d-a267-cd8d7e793be6.png?w=840&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=7490306a14892773513e1285b490ed0b 840w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8a53588-8543-d39d-a267-cd8d7e793be6.png?w=1100&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=633c5cccd6376bb71866b75be943e095 1100w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8a53588-8543-d39d-a267-cd8d7e793be6.png?w=1650&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=4fe38aee1c199800ecfe78d9dca81e9e 1650w, https://mintcdn.com/asapp/V0FXHedP7HW51oOw/image/uuid-a8a53588-8543-d39d-a267-cd8d7e793be6.png?w=2500&fit=max&auto=format&n=V0FXHedP7HW51oOw&q=85&s=fcd3285c42311f79489e8b64b973ca28 2500w" />
</Frame>

For more details, see the [Previewer guide](/generativeagent/configuring/previewer).

## Next Steps

Explore further integration topics:

<CardGroup>
  <Card title="Connecting Your APIs" href="/generativeagent/configuring/connect-apis" />

  <Card title="Integrating GenerativeAgent" href="/generativeagent/integrate" />
</CardGroup>
