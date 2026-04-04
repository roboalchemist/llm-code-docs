# Source: https://scrapfly.io/docs/mcp/examples

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/mcp/examples

Markdown Content:
MCP Examples & Use Cases
------------------------

Real-world examples of what you can build with the Scrapfly MCP Server-from simple data extraction to complex multi-step workflows. You don't write code-you just ask your AI in natural language, and it figures out which tools to use and how to chain them together.

[Detailed Examples](https://scrapfly.io/docs/mcp/examples#detailed-examples)
----------------------------------------------------------------------------

Let's dive deeper into specific scenarios with full workflows.

#### Scenario

You want to find all remote Python developer jobs posted today on multiple job boards.

#### Prompt

"Search for remote Python developer jobs on LinkedIn, Indeed, and AngelList. Filter for positions posted in the last 24 hours. Create a summary table with company name, position, salary range, and application link."

#### What Happens Behind the Scenes

1.   AI calls `scraping_instruction_enhanced` to understand best practices
2.   AI uses `web_get_page` to scrape LinkedIn jobs page
3.   AI uses `web_scrape` with `extraction_model: "job_listing"` for Indeed
4.   AI uses `web_get_page` for AngelList
5.   AI parses all results and filters by date
6.   AI creates a formatted table with all matching positions

#### Scenario

Build an automated price tracking system that monitors products across multiple retailers, tracks historical trends, and identifies the best time to buy. Perfect for deal hunters, price comparison apps, or dynamic pricing strategies.

#### Prompt

"I want to buy Sony WH-1000XM5 headphones but I'm looking for the best deal. Check current prices on Amazon, Best Buy, Target, and Walmart. For each retailer, get the price, stock status, shipping options, and any current promotions or discounts. Tell me which retailer has the best overall value considering price, shipping, and availability. Also check if there are any bundle deals or extended warranties included."

#### What Happens Behind the Scenes

1.   AI calls `scraping_instruction_enhanced` to get optimal scraping parameters
2.   AI uses `web_scrape` with `extraction_model: "product"` for each retailer's product page
3.   AI extracts comprehensive data: price, original price, discount %, stock status, shipping cost, delivery time, and warranty info
4.   AI checks for promotional codes, bundle offers, and financing options
5.   AI calculates total cost (price + shipping + taxes) for accurate comparison
6.   AI compares value propositions: free shipping, faster delivery, return policies
7.   AI generates detailed comparison with recommendation based on best overall value

#### Example Response

###### Price Comparison for Sony WH-1000XM5 Headphones

| Retailer | Price | Shipping | Total | Stock | Delivery |
| --- | --- | --- | --- | --- | --- |
| **Amazon** | $349.99 -13% | Free | **$349.99** | In Stock | 2-day Prime |
| **Best Buy** | $399.99 | Free | **$399.99** | In Stock | Same-day pickup |
| **Target** | $379.99 | $5.99 | **$385.98** | In Stock | 3-5 days |
| **Walmart** | $364.99 | Free | **$364.99** | Low Stock | 4-7 days |

**Best Overall Value: Amazon - $349.99**

*   **Lowest price:** $50 off MSRP (13% discount)
*   **Fast shipping:** Free 2-day Prime delivery
*   **Good stock:** Available now, no delays
*   **Easy returns:** 30-day return policy
*   **Total savings:** $50 vs. Best Buy, $36 vs. Target

Additional Findings:

*   **Best Buy:** Includes free 2-year Geek Squad protection ($79 value) with purchase
*   **Amazon:** Currently has 15% off coupon available (clip coupon on product page)
*   **Target:** Extra 5% off with RedCard ($19 additional savings)
*   **Walmart:** Offers 24-month financing at 0% APR

**Price History Insight:**

Based on current pricing, this is the lowest price in the last 90 days. Historical average: $389. **Great time to buy!**

**Pro Tip:** Set up automated monitoring by scheduling this prompt to run daily. Use `cache: true` with `cache_ttl: 3600` (1 hour) to track price changes efficiently. Combine with webhooks to get instant notifications when prices drop below your target.

#### Scenario

Conduct comprehensive research by gathering, analyzing, and synthesizing information from multiple authoritative sources. Perfect for market research, academic literature reviews, trend analysis, or competitive intelligence.

#### Prompt

"I'm writing a whitepaper on quantum computing breakthroughs in 2024. Research the latest developments from MIT News, Nature.com, Quanta Magazine, and ArXiv from the past 3 months. For each breakthrough, extract: the discovery/advancement, lead researchers and institutions, publication date, practical applications, and any benchmarks or performance metrics mentioned. Identify common themes, compare different approaches (superconducting vs. photonic vs. topological qubits), and highlight which institutions are leading the field. Create a timeline of major announcements and summarize the most promising developments."

#### What Happens Behind the Scenes

1.   AI calls `scraping_instruction_enhanced` for best practices
2.   AI constructs search queries for each source (filtering by topic and date range)
3.   AI uses `web_scrape` with `extraction_model: "article"` for article listing pages
4.   AI visits individual articles and extracts: title, authors, publication date, abstract, key findings, methodologies, and citations
5.   AI filters articles by publication date (last 90 days) and relevance score
6.   AI identifies recurring themes, breakthrough categories, and research trends
7.   AI maps researchers to institutions and tracks collaboration networks
8.   AI extracts quantitative metrics: qubit counts, error rates, coherence times, gate fidelities
9.   AI synthesizes findings into structured report with timeline, thematic analysis, and institutional rankings

#### Example Response

###### Quantum Computing Research Summary (Q1 2024)

Research Timeline:

**March 15, 2024** - Major Breakthrough

**IBM Achieves 1,000+ Qubit Processor**

IBM Research announced "Condor," a 1,121 superconducting qubit processor with 20% improvement in error rates. Lead: Dr. Jay Gambetta (IBM Quantum). Source: Nature Physics

**March 8, 2024**

**Google Demonstrates Error Correction Milestone**

Achieved logical error rate below physical error rate using surface codes on 72 qubits. Lead: Dr. Hartmut Neven (Google Quantum AI). Source: Nature

**February 22, 2024**

**QuEra Demonstrates Neutral-Atom Advantage**

280-qubit neutral-atom system solves optimization problems 100x faster than classical computers. Lead: Dr. Mikhail Lukin (Harvard). Source: Science

**January 30, 2024**

**PsiQuantum Secures $620M for Photonic Approach**

Funding round to build fault-tolerant photonic quantum computer by 2027. Room-temperature operation advantage. Source: MIT News

Key Technology Comparisons:

| Approach | Leading Institutions | Qubit Count | Key Advantage | Challenge |
| --- | --- | --- | --- | --- |
| **Superconducting** | IBM, Google, Rigetti | 1,000+ | Scalability & speed | Requires cryogenic cooling |
| **Neutral Atom** | Harvard, QuEra, Pasqal | 280+ | Long coherence times | Gate fidelity improvements needed |
| **Photonic** | PsiQuantum, Xanadu | Theoretical | Room temperature operation | Manufacturing complexity |
| **Trapped Ion** | IonQ, Honeywell | 32+ | Highest gate fidelity (99.9%) | Slower operations |

Leading Institutions by Impact:

1.   **IBM Research** - 12 publications, focus on superconducting scalability
2.   **Google Quantum AI** - 8 publications, error correction breakthroughs
3.   **Harvard University** - 7 publications, neutral-atom innovations
4.   **MIT** - 6 publications, algorithm development and materials science
5.   **Stanford** - 5 publications, quantum networking protocols

Emerging Themes:

*   **Error Correction Focus:** 65% of papers emphasize quantum error correction as critical path to fault tolerance
*   **Hybrid Approaches:** Growing interest in combining classical and quantum processors for practical advantage
*   **Application-Driven:** Shift from "quantum supremacy" to solving real problems (drug discovery, optimization, cryptography)
*   **Collaborations:** 40% of breakthroughs involved multi-institutional partnerships

**Most Promising Development:**

Google's error correction milestone represents a turning point - demonstrating that logical qubits can be more reliable than physical qubits. This validates the path to fault-tolerant quantum computing within the next 5-10 years. Combined with IBM's 1,000+ qubit processors, we're entering the era of "utility-scale" quantum computing for practical applications.

**Pro Tip:** For ongoing research monitoring, use `format: "markdown"` to get clean, AI-friendly content. Chain this with sentiment analysis or citation tracking by asking the AI to extract reference networks. You can also use `screenshots` to capture figures, charts, and diagrams from papers for visual analysis.

#### Scenario

Track competitor features, pricing changes, and marketing strategies across multiple SaaS platforms to inform your product roadmap.

#### Prompt

"Analyze my top 3 SaaS competitors: Ahrefs, SEMrush, and Moz. For each one, extract their pricing tiers, features included in each tier, and any special promotions on their pricing pages. Also check their blogs for recent product announcements from the last month. Create a comparison table showing feature gaps and pricing strategies."

#### What Happens Behind the Scenes

1.   AI calls `scraping_instruction_enhanced` to get optimal scraping parameters
2.   AI uses `web_scrape` with `render_js: true` to load each competitor's pricing page (dynamic content)
3.   AI uses `extraction_prompt` to extract: pricing tiers, features per tier, discounts, and trial terms
4.   AI visits each blog/news page and uses `extraction_model: "article"` to get recent announcements
5.   AI filters articles by publication date (last 30 days)
6.   AI analyzes and compares pricing structures, feature availability, and positioning
7.   AI generates a competitive analysis report with feature gaps, pricing insights, and strategic recommendations

#### Example Response

###### Competitive Analysis Summary

Pricing Comparison:

| Competitor | Entry Tier | Mid Tier | Enterprise |
| --- | --- | --- | --- |
| **Ahrefs** | $99/mo | $179/mo | $399/mo |
| **SEMrush** | $119/mo | $229/mo | $449/mo |
| **Moz** | $79/mo | $149/mo | $249/mo |

Key Feature Gaps:

*   Missing Real-time rank tracking (Ahrefs & SEMrush have it)
*   Missing Content optimization AI (SEMrush exclusive)
*   Advantage More generous API rate limits vs. Moz

Recent Product Updates (Last 30 Days):

*   **Ahrefs:** Launched AI-powered content brief generator (March 15)
*   **SEMrush:** Added YouTube keyword research tool (March 20)
*   **Moz:** Updated domain authority algorithm (March 10)

**Pro Tip:** Schedule this prompt to run weekly to track competitor pricing changes and new feature releases automatically. Use `cache: true` with appropriate `cache_ttl` to reduce costs for frequently monitored pages.

#### Scenario

Research the real estate market in a specific area by aggregating property listings, analyzing price trends, and comparing neighborhoods.

#### Prompt

"I'm looking to invest in rental properties in Austin, Texas. Search Zillow, Redfin, and Realtor.com for 3-bedroom properties under $500k in the following zip codes: 78704, 78702, and 78751. For each listing, extract: address, price, square footage, bedrooms/bathrooms, estimated rental income, year built, and listing URL. Create a summary showing which neighborhood has the best rental yield and price per square foot."

#### What Happens Behind the Scenes

1.   AI calls `scraping_instruction_enhanced` to get best practices for real estate scraping
2.   AI constructs search URLs for each platform with filters (location, price, bedrooms)
3.   AI uses `web_scrape` with `extraction_model: "real_estate_property_listing"` for listing pages
4.   AI visits individual property detail pages using `extraction_model: "real_estate_property"` to get full details
5.   AI extracts key data: price, size, features, rental estimates, HOA fees, property tax
6.   AI calculates rental yield: (annual rental income / property price) × 100
7.   AI calculates price per square foot for each property
8.   AI groups by neighborhood (zip code) and generates comparative analysis with investment recommendations

#### Example Response

###### Austin Real Estate Investment Analysis

Neighborhood Comparison:

| Zip Code | Avg Price | Avg $/sqft | Est. Rental Yield | Properties Found |
| --- | --- | --- | --- | --- |
| **78702** (East Austin) | $425,000 | $298 | **6.8%** | 12 |
| **78704** (South Austin) | $485,000 | $342 | 5.2% | 8 |
| **78751** (Hyde Park) | $495,000 | $365 | 4.9% | 5 |

Top Investment Opportunities:

**1. 1402 E 6th St, Austin TX 78702** - Best Value

*   **Price:** $399,000 | **Size:** 1,350 sqft | **$/sqft:** $295
*   **Est. Monthly Rent:** $2,800 | **Rental Yield:** 8.4%
*   **Year Built:** 2018 | **HOA:** None
*   [View on Zillow →](https://zillow.com/...)

**2. 3312 Govalle Ave, Austin TX 78702**

*   **Price:** $415,000 | **Size:** 1,420 sqft | **$/sqft:** $292
*   **Est. Monthly Rent:** $2,650 | **Rental Yield:** 7.7%
*   **Year Built:** 2020 | **HOA:** $50/mo
*   [View on Redfin →](https://redfin.com/...)

Investment Recommendation:

**Best Area: 78702 (East Austin)**

*   **Highest rental yield:** 6.8% average (vs. 5.2% in 78704)
*   **Best value:** $298/sqft (16% cheaper than 78751)
*   **Strong rental demand:** Near downtown, UT campus, and tech offices
*   **Market trend:** Appreciating 8.2% YoY based on recent sales data

**Pro Tip:** Use `screenshots` parameter to capture property photos for visual comparison. You can also chain this with review scraping using `extraction_model: "review_list"` to research neighborhood safety and amenities on platforms like Nextdoor or Google Maps.

[Advanced Workflows](https://scrapfly.io/docs/mcp/examples#advanced-workflows)
------------------------------------------------------------------------------

Complex scenarios that chain multiple tools and steps.

Comprehensive product analysis across multiple e-commerce sites with sentiment analysis.

1.   **Gather data** - Scrape product listings from 5 e-commerce sites
2.   **Extract features** - Use `extraction_model: "product_listing"`
3.   **Analyze pricing** - Identify pricing patterns and outliers
4.   **Check reviews** - Scrape reviews using `extraction_model: "review_list"`
5.   **Sentiment analysis** - Analyze review sentiment
6.   **Generate report** - Create comprehensive market analysis

Build and enrich contact lists automatically with data validation and scoring.

1.   **Search directories** - Find companies matching criteria
2.   **Extract contact info** - Get company details, founders, emails
3.   **Enrich data** - Look up founders on LinkedIn
4.   **Validate** - Check company websites for relevance
5.   **Score leads** - Rank by fit and priority
6.   **Export** - Format as CSV for CRM import

Track website changes over time with automated alerts and version archiving.

1.   **Initial capture** - Take screenshot and save HTML
2.   **Schedule checks** - Scrape page periodically
3.   **Compare** - Detect changes in content or layout
4.   **Alert** - Notify when changes detected
5.   **Archive** - Store historical versions

[Industry-Specific Use Cases](https://scrapfly.io/docs/mcp/examples#industry-use-cases)
---------------------------------------------------------------------------------------

Real-world applications across different industries.

*   Price monitoring and competitive intelligence
*   Product availability tracking
*   Review aggregation and sentiment analysis
*   Trend identification and market research

*   Financial news aggregation
*   Stock data collection from multiple sources
*   Economic indicator tracking
*   Real estate listing analysis

*   Job posting aggregation
*   Candidate research (LinkedIn, GitHub, portfolios)
*   Salary benchmarking
*   Company culture research

*   Property listing aggregation
*   Price trend analysis
*   Neighborhood research
*   Rental market analysis

*   Hotel price comparison
*   Flight deal monitoring
*   Review aggregation for destinations
*   Event and attraction research

[Tips & Best Practices](https://scrapfly.io/docs/mcp/examples#tips-and-tricks)
------------------------------------------------------------------------------

Optimize your scraping workflows with these proven strategies.

##### Best Practices

*   **Call `scraping_instruction_enhanced` first** - Get latest POW parameter
*   **Be specific in prompts** - "Get product prices" beats "check website"
*   **Use extraction models** - Pre-trained models are faster
*   **Handle errors gracefully** - Retry with different parameters

##### Cost Optimization

*   Use `web_get_page` for simple pages
*   Disable `render_js` for static content
*   Use datacenter proxies by default
*   Cache frequently accessed pages

##### Performance

*   Request multiple pages in parallel
*   Use `format: "markdown"` for AI
*   Set appropriate `rendering_wait`
*   Use `format_options: ["only_content"]`

### Ready to Build?

Start with a simple prompt like "Get me the top posts from Hacker News" and watch your AI use Scrapfly MCP tools to make it happen!

[Next Steps](https://scrapfly.io/docs/mcp/examples#next-steps)
--------------------------------------------------------------
