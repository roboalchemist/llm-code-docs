# Source: https://docs.base44.com/Performance-and-SEO/SEO-and-search-visibility.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting your app found in search

> Base44 provides a solid technical SEO and GEO foundation for your app so you can focus on content, trust, and visibility.

Base44 manages your app’s core technical SEO so search engines and AI assistants can discover, crawl, and index your content. The same elements that search engines reward, like high-quality content, structured data, and a strong backlink profile, are also signals that AI models use when they decide what to trust. The principles of strong SEO remain the core of being found, both in search results and in AI-generated answers.

When an AI assistant generates a list of recommended businesses, the site name and favicon are often the only brand assets someone sees. This makes them very important for brand recognition and credibility in an AI-first search landscape. They are not only browser assets, they are key parts of your client’s digital identity.

When you publish your app on a custom domain, Base44 creates and maintains essential files and settings for you in the background. These include clean HTML, structured headings, XML sitemaps, robots.txt, canonical tags, and performance-focused hosting.

You do not need to upload or manage technical SEO files yourself. Your main focus is to publish on a custom domain and provide clear, trustworthy content that supports both search engine optimization (SEO) and generative engine optimization (GEO) across major search engines such as Google and Bing.

<Note>
  **Note:** Base44’s SEO setup is designed and supported for apps that are published on a [custom domain](/Setting-up-your-app/Setting-up-your-custom-domain). Free Base44 URLs can still be crawled by search engines, but they are not intended for long-term, production SEO.
</Note>

***

## How your app’s SEO works

Base44 sets up and maintains the main technical elements that search engines expect. This covers how your pages are discovered, how they are crawled, and how your app is represented across the web and in AI-generated answers. These technical signals support both search engine optimization (SEO) and generative engine optimization (GEO).

<Info>
  **Info:** Base44 apps are client-side rendered (CSR) by default, so most AI crawlers do not execute your app’s JavaScript or see the full content directly. Instead, many AI assistants query search engines such as Google and Bing and use the pages those engines have already crawled and indexed. By optimizing your app for search engines, you also improve its visibility to AI assistants that depend on those search indexes.
</Info>

**Core SEO features handled automatically:**

For apps published on a custom domain, Base44 automatically manages:

* **Meta titles:** Each page has a unique meta title based on its URL (for pages without URL parameters). This helps search engines distinguish between pages and show clear titles in results.
* **Heading structure and semantic HTML:** Pages follow a logical heading structure (H1, H2, H3) and use semantic HTML. This makes it easier for search engines and assistive technologies to understand your content.
* **Canonical tags for clean URLs:** Base44 adds self-referencing canonical tags for pages that use clean URLs without parameters. This reduces duplicate content issues and signals the preferred URL for each page.\
  For URLs that include parameters (such as query strings), Base44 avoids adding self-referencing canonicals that can cause conflicts.
* **Sitemap (sitemap.xml):** Base44 automatically generates and serves a sitemap at `/sitemap.xml`. Public, indexable pages are included, while private or internal pages are excluded. You can submit this sitemap directly in Google Search Console and other webmaster tools.
* **robots.txt:** Base44 creates and serves a `robots.txt` file for both free and paid apps. It allows search engines to crawl your public content while protecting non-public or technical routes from indexing.
* **Clean URLs and routing:** Your app uses clean, readable URLs rather than duplicate or unnecessary paths. This supports better crawl behavior and improves clarity for visitors.
* **Internal linking:** Navigation and internal links use proper anchor tags and clean URLs so search engines can follow and understand your app structure.
* **Social sharing tags and previews (Open Graph and Twitter):** Base44 sets social metadata so links to your app show a sensible title, description, and image when shared on social platforms. Social card images are automatically resized to 1200 × 630 and include the correct URL metadata, which reduces Open Graph and card size warnings and helps previews display consistently across major platforms such as Facebook, X (Twitter), LinkedIn, and WhatsApp. These previews use the title, description, and logo you configure in your app’s settings.
* **Mobile-friendly layout:** Apps generated with Base44 are responsive and adapt to different screen sizes. This supports mobile-first indexing and improves your visitors’ experience on phones and tablets.
* **Image optimization and performance:** Images and assets are served in optimized ways where possible, and the hosting environment is tuned for good performance. Strong performance helps with Core Web Vitals and overall search quality signals.
* **Other site metadata:** Base44 manages technical files such as the web app manifest and favicon for custom domains. These help browsers and devices display your app correctly in tabs, shortcuts, and installable views.

In addition, you can use the Code tab in your dashboard to edit the generated `index.html` file for your app. This lets you add trusted `<meta>` tags and `<script>` tags that need to appear directly in the HTML source, such as analytics, advertising, verification, or other third-party scripts.

<Warning>
  **Important:** If you recently published or switched to a custom domain, it can take anywhere from a few days to a few weeks for new or updated apps to be indexed by Google and other search engines, depending on their crawl schedule.
</Warning>

**What Base44 does not generate automatically:**

There are some SEO elements that Base44 does not create by default.

* **Meta descriptions:** Base44 does not set a custom meta description tag for each page. Search engines usually generate the text they show in results from the visible content on your page. Write clear, focused headings and body copy for each important page so search engines can create useful, relevant snippets.
* **Structured data (schema.org) for rich results:** Base44 does not inject schema types such as `FAQPage`, `Article`, `Product`, `LocalBusiness`, or `Organization` by default. When you have matching visible content and are comfortable working with schema, you can ask the AI to add JSON-LD structured data into your app or add it in code, then validate the markup using tools such as Google’s Rich Results Test and the schema.org validator.
* **Advanced prerendering or proxy-based optimizations:** External prerendering services and similar proxy-based setups are not included by default. In very complex or highly competitive SEO cases, your team can add these on top of Base44 at the hosting or proxy layer as an advanced configuration.

Off-page SEO signals, such as backlinks, external reviews, and PR coverage, are always managed outside of Base44 and are part of your broader marketing efforts.

***

## Strengthening trust and authority

Search engines and AI systems look for signs that your app represents a real, trustworthy organization. You can use the AI chat to add these signals into your layout and content.

<AccordionGroup>
  <Accordion title="Add clear business details">
    Make it obvious that there is a real business behind the app.

    **Prompt example:** `Add a clear business details section in the footer with the registered business name, full physical address, phone number, and a professional contact email.`

    This type of information helps search engines confirm that your app belongs to a legitimate organization and reduces the risk of being treated as low quality or automatically generated.

    You can also create or update a Google Business Profile using the same name, address, and phone number that appear in your app.
  </Accordion>

  <Accordion title="Introduce the people behind the content">
    Show who is responsible for the product and the information on the site.

    **Prompt example:** `Create a Team section on the About page that includes each team member’s name, role, a short bio, and a link to their professional profile.`

    Named team members and authors help demonstrate experience and expertise, especially in areas where trust is important.
  </Accordion>

  <Accordion title="Add social proof and testimonials">
    Social proof can improve visitor confidence and engagement.

    **Prompt example:** `Add a Testimonials section with short quotes from real customers, including their name, role, company, and a small photo where possible.`

    **Prompt example:** `Add a Trusted by section near the top of the homepage that displays logos of well-known clients or partners.`

    Visible testimonials and recognizable logos show that real people and organizations rely on your product or service.
  </Accordion>

  <Accordion title="Include legal and policy pages">
    Policy pages are a basic expectation for a professional site.

    **Prompt example:** `Create links in the footer to Privacy Policy, Terms of Service, and an Accessibility statement, and generate clear, plain language content for each page that matches our business.`

    Apps that clearly show their policies are more likely to be treated as reliable resources by visitors and by search quality systems.
  </Accordion>
</AccordionGroup>

***

## Creating content for search intent

On top of a strong technical foundation, your content should match the language and questions your audience actually uses.

<AccordionGroup>
  <Accordion title="Use your audience’s language">
    Guide the AI to write with the same words and phrases that your audience uses, not internal jargon.

    **Prompt example:** `For this page, our main topic is "[insert topic]". Rewrite the headings and body copy using the natural language our customers use for this topic, avoiding internal jargon. Use a clear H1, and H2 or H3 headings based on real questions they ask.`

    You can refine your wording by:

    * Asking non-experts how they would describe what you do.
    * Looking at Google’s autocomplete suggestions when you type your main topic.
    * Checking "Related searches" and "People also ask" sections for your main query.
  </Accordion>

  <Accordion title="Turn common questions into FAQ content">
    Frequently asked questions help both visitors and search engines understand your app.

    **Prompt example:** `Add an FAQ section at the bottom of this page that answers the most common questions about this topic in a direct, factual style. Format it with clear Question and Answer labels.`

    Structured question-and-answer content is easier for search engines and AI systems to reuse when responding to related queries.
  </Accordion>

  <Accordion title="Improve headings and internal links">
    Headings and internal links help search engines understand how your content is organized and which pages are most important.

    **Prompt example:** `Rewrite the H2 and H3 headings on this page so that each one describes a specific subtopic related to "[insert topic]". Add internal links from relevant pages to this page using descriptive anchor text rather than generic "click here" wording.`

    Clear headings and useful internal links support better crawling and help visitors find what they need.
  </Accordion>
</AccordionGroup>

***

## Adding structured data for rich results

Structured data (schema.org) is a way to describe your content in a machine-readable format. When implemented correctly, it can enable rich results, such as FAQ drop-downs or star ratings, in search results.

Base44 does not add structured data automatically, but you can ask the AI to inject JSON-LD code into the appropriate parts of your app.

Well-structured content and valid schema also help AI assistants understand what your app does when they generate answers that include links or references to external sites. This is an important part of generative engine optimization (GEO).

<Note>
  Always validate your structured data using [Google’s Rich Results Test](https://search.google.com/test/rich-results) before relying on it for SEO. Only add schema that accurately reflects the visible content on the page and follows Google’s structured data guidelines.
</Note>

<AccordionGroup>
  <Accordion title="Organization or brand schema">
    Use Organization schema to help search engines connect your app with your brand.

    **Prompt example:** `Add valid JSON-LD Organization schema to the homepage that includes our organization name, logo URL, main website URL, and links to our main social media profiles, using the schema.org "Organization" type.`
  </Accordion>

  <Accordion title="FAQ schema">
    If you already have an FAQ section on a page, you can mark it up so that some questions may appear directly in search results.

    **Prompt example:** `Wrap the existing FAQ section on this page in valid JSON-LD "FAQPage" schema markup so that each question-and-answer pair follows Google's structured data guidelines.`
  </Accordion>

  <Accordion title="Local business schema (optional)">
    If you operate from a physical location or serve a specific local area, LocalBusiness schema can support local visibility.

    **Prompt example:** `Generate JSON-LD "LocalBusiness" schema for our business and add it to the Contact page, including our name, address, phone number, opening hours, and geo-coordinates.`
  </Accordion>
</AccordionGroup>

These additions do not guarantee rich results, but they help search engines understand your content and eligibility for supported result types.

***

## Connecting Google Search Console

Google Search Console (GSC) is a free tool from Google that shows how your app appears in search results. It lets you:

* Confirm that Google can access and index your app.
* See which queries bring visitors to your pages.
* Monitor indexing coverage and resolve technical issues.

Base44 generates your sitemap and robots.txt, but setting up GSC is still a separate step that you complete in your Google account. You can also use tools such as Bing Webmaster Tools to see how Bing indexes your app. Because many AI assistants rely on both Google and Bing, keeping these views healthy supports GEO as well.

<Note>
  You can connect both custom domains and free Base44 URLs to Google Search Console.
</Note>

<AccordionGroup>
  <Accordion title="Step 1 | Open Google Search Console">
    1. Go to [Google Search Console](https://search.google.com/search-console/about).
    2. Sign in with your Google account.
    3. Click **Start now** or **Add property** if you already have other sites or apps connected.
  </Accordion>

  <Accordion title="Step 2 | Add your app as a URL prefix property">
    1. In the property setup dialog, select the **URL prefix** option.
    2. Enter your full app URL, including protocol (for example, `https://www.yourdomain.com` or `https://project-name-abc123.base44.app/`).
    3. Click **Continue**.

    <Note>
      **Note:** Make sure you are verifying the full URL, including `https://` and any `www` or subdomain.
    </Note>

    <img src="https://mintcdn.com/base44/WGiuRV-vbkZ8d-Mx/images/0b7331d1-b175-4958-9411-9e1bcf9112ea.png?fit=max&auto=format&n=WGiuRV-vbkZ8d-Mx&q=85&s=6cfd084fc3e23a1bc21f1a1dbceddc49" alt="Setting up a URL prefix property in Google Search Console" title="Adding a URL prefix property in Google Search Console" className="mx-auto" style={{ width:"63%" }} width="726" height="568" data-path="images/0b7331d1-b175-4958-9411-9e1bcf9112ea.png" />
  </Accordion>

  <Accordion title="Step 3 | Get the HTML tag verification code">
    1. On the **Verify ownership** page, scroll to the **HTML tag** method.
    2. Expand the HTML tag option.
    3. Copy the meta tag code snippet that looks like:

    ```html  theme={null}
    <meta name="google-site-verification" content="...">
    ```

    Do not edit the `content` value.

    <img src="https://mintcdn.com/base44/mAzqubCEQOYZcQeG/images/bf619cf8-44c9-482b-82ce-de72bc0986c5.png?fit=max&auto=format&n=mAzqubCEQOYZcQeG&q=85&s=9b09c8fb04a47e6bf393a47d7a917455" alt="Google Search Console HTML tag verification option" title="Copying the HTML verification tag in Google Search Console" className="mx-auto" style={{ width:"74%" }} width="597" height="407" data-path="images/bf619cf8-44c9-482b-82ce-de72bc0986c5.png" />
  </Accordion>

  <Accordion title="Step 4 | Add the verification tag in index.html">
    You now need to place this meta tag inside the `<head>` of your app so Google can see it.

    **To add the verification tag:**

    1. In your Base44 app editor, click **Dashboard**.
    2. Click the **Code** tab.
    3. In the file list, click `index.html` to open it.
    4. Paste the verification meta tag anywhere inside the `<head>` section, without changing the `content` value.
    5. Click **Save**, then click **Publish** so the change is live at the URL you entered in Google Search Console.

    <Frame>
            <img src="https://mintcdn.com/base44/dCYQLLdIO1Kk9NoP/images/htmltaggsc.png?fit=max&auto=format&n=dCYQLLdIO1Kk9NoP&q=85&s=a0ae61b9d50456c55f5c32dd59a944db" alt="Htmltaggsc" width="1274" height="785" data-path="images/htmltaggsc.png" />
    </Frame>

    <Warning>
      **Important:** Do not remove the verification meta tag from `index.html`, or your property may lose its verified status.
    </Warning>
  </Accordion>

  <Accordion title="Step 5 | Verify ownership in Google Search Console">
    1. Return to Google Search Console.
    2. Under the HTML tag method, click **Verify**.
    3. If Google finds the meta tag on your homepage, you see a success message confirming that ownership is verified.

    If verification fails, check that:

    * The meta tag appears in the `<head>` of the live site (not just in preview).
    * The tag matches exactly what GSC provided.
    * The URL in GSC matches the URL of your published app, including protocol, subdomain, and path.
  </Accordion>

  <Accordion title="Step 6 | Submit your sitemap">
    Base44 serves your sitemap at `/sitemap.xml` on your custom domain.

    1. In Google Search Console, select your verified property.
    2. From the left menu, click **Sitemaps**.
    3. In the **Add a new sitemap** field, enter:

    ```text  theme={null}
    sitemap.xml
    ```

    The full path is usually `https://www.yourdomain.com/sitemap.xml`. 4. Click **Submit**.

    Google then uses this sitemap to discover and process your app’s pages more efficiently.
  </Accordion>

  <Accordion title="Optional | Ask Google to recrawl a key page">
    You can also ask Google to recrawl an important page sooner:

    * In Google Search Console, open **URL inspection** in the left menu.
    * Enter the full URL of the page you want Google to check.
    * Click **Request indexing** if it is available.

    This is optional, but can help new or recently updated key pages get processed faster.
  </Accordion>
</AccordionGroup>

***

## SEO best practices checklist

Use the checklist below to make sure you are getting the most from Base44’s SEO foundation.

<Card icon="list-check" title="SEO checklist for your app">
  <Icon icon="check" /> **Use a custom domain:** Automatic SEO features such as sitemap.xml, robots.txt, and social previews are designed for apps on custom domains.

  <Icon icon="check" /> **Add clear, unique content to each key page:** Give every important page a descriptive H1, supporting H2 headings, and focused body text that matches the questions your audience asks.

  <Icon icon="check" /> **Show business details and trust signals:** Include your business name, address, contact details, team information, testimonials, and policy pages where relevant.

  <Icon icon="check" /> **Structure common questions as FAQs:** Add question-and-answer sections for frequent queries and consider wrapping them in `FAQPage` schema when appropriate.

  <Icon icon="check" /> **Use descriptive internal links:** Link between related pages using meaningful anchor text so search engines understand how your content is connected.

  <Icon icon="check" /> **Connect search console tools:** Verify your app in Google Search Console and, if relevant, Bing Webmaster Tools. Submit your sitemap so you can monitor indexing, search queries, and technical issues, and understand how your app appears in search results and AI-generated answers.
</Card>

***

## FAQs

Click a question below to learn more about your app's SEO.

<AccordionGroup>
  <Accordion title="Why doesn’t my app show up in search yet?">
    New or updated apps do not appear in search results immediately. Search engines need time to discover and crawl your content. Make sure your app is:

    * Published on a custom domain
    * Public and accessible (not restricted behind authentication)
    * Connected to your correct URL in Google Search Console (optional but recommended) or similar tools such as Bing Webmaster Tools.

    Indexing can still take from a few days to a few weeks, depending on each search engine’s crawl schedule. Once your app appears reliably in search results, it is more likely to be included in AI-generated answers that rely on those indexes.
  </Accordion>

  <Accordion title="Can Base44 guarantee good rankings in search or AI answers?">
    No platform can guarantee rankings in search results or placement in AI-generated answers. Base44 gives you a strong technical foundation (sitemap, robots.txt, clean URLs, performance) and tools to add high-quality content, trust signals, and structured data. Your actual visibility depends on your content, competition, backlinks, and broader marketing efforts.
  </Accordion>

  <Accordion title="How do I make my app appear in search results?">
    Your app can appear in search results on major search engines such as Google and Bing when it is public, published, and available on a custom domain. Base44 manages the technical SEO foundation, such as the sitemap and robots.txt. For better monitoring and control, you can also connect your app to Google Search Console and similar tools like Bing Webmaster Tools, then submit your sitemap. Improving these SEO fundamentals usually also improves generative engine optimization (GEO) and your chances of appearing in AI-generated answers.
  </Accordion>

  <Accordion title="Can I customize meta tags or the page description?">
    Base44 sets core meta tags such as titles and canonical tags for you. Meta descriptions are not generated automatically, and there is no dedicated interface for editing all meta tags manually. Focus on clear page titles, headings, and on-page content, as search engines usually create their own snippets from the text on your pages.
  </Accordion>

  <Accordion title="Do I need to submit my sitemap or manage SEO files manually?">
    Base44 automatically generates and serves your sitemap at `/sitemap.xml` and manages robots.txt and other core files for you on custom domains. You do not need to upload these files yourself. Submitting your sitemap directly in Google Search Console or other webmaster tools is still recommended so search engines can process your URLs more efficiently.
  </Accordion>

  <Accordion title="Can I control which pages are indexed or hidden?">
    Base44 includes all public, published pages in your sitemap and makes them available for indexing. There are currently no per-page indexing controls or manual robots.txt editing options in the product. To keep a page out of search, make sure it is not public or not linked from your live app.
  </Accordion>

  <Accordion title="Can I use structured data to get rich results (FAQ, local, stars)?">
    Yes. Base44 does not add schema.org structured data automatically, but you can add your own JSON‑LD for types such as `Organization` or `LocalBusiness` using prompts or code. Always validate your structured data with Google’s Rich Results Test, and remember that rich results are never guaranteed, even when your schema is valid.
  </Accordion>

  <Accordion title="How do I add or edit a manifest.json for my app?">
    Base44 creates and manages the `manifest.json` file for you automatically on custom domains. There is no need to manually upload or edit this file. Your app’s metadata is updated by the system in the background.
  </Accordion>

  <Accordion title="Can I customize or replace the auto-generated sitemap.xml with my own?">
    Base44 automatically generates and serves the sitemap at `/sitemap.xml` and there is no option to disable, override, or replace this default sitemap. The static deployment always takes precedence, so external tools or edge logic (such as a CDN or worker routes) cannot intercept or change it.\
    \
    If you need a custom sitemap, you can:

    * Host your sitemap at a different URL path, for example `/sitemaps/custom.xml`
    * Submit that custom sitemap URL directly in Google Search Console or other search engine webmaster tools, in addition to the default sitemap.
  </Accordion>

  <Accordion title="How do I set the language of my app for browsers and search engines?">
    Your app’s HTML includes a `lang` attribute that tells browsers and search engines what language the page is written in. Setting this correctly helps tools detect your language, improves accessibility, and can reduce incorrect auto-translation prompts.

    To change the language declaration, edit the `<html>` tag in your app’s `index.html` file in the Code tab and update the `lang` value, for example from `lang="en"` to `lang="fr"` or `lang="es"`.

    Use standard language codes (such as `en`, `fr`, `de`, or `pt-BR`) and only set a language code that matches the main content of the app.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).