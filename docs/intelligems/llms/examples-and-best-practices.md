# Source: https://docs.intelligems.io/developer-resources/mcp-server/examples-and-best-practices.md

# Examples & Best Practices

## For Agencies

**1. Monthly Client Performance Review** *Use when preparing for monthly client calls*

```
For [CLIENT NAME], give me a comprehensive analysis of all tests completed this month. Include:
1. Which tests reached statistical significance and their winners
2. The estimated revenue impact of implementing winners
3. Key insights to share with the client
4. Any tests that should be ended early or extended

```

**What you'll get:** List of completed tests with win/loss status, revenue per visitor and gross profit uplift percentages, statistical confidence levels, and actionable recommendations for client discussion.

***

**2. Cross-Test Pattern Analysis** *Use to find winning strategies that work consistently*

```
Analyze all completed tests for [CLIENT NAME] over the past 3 months.
What patterns appear across multiple winning tests?
What concepts (urgency, trust, social proof, simplification, etc.)
consistently win or lose for this customer base?

```

**What you'll get:** Patterns across winning variations, concepts that resonate with the client's audience, and strategic direction for future testing.

***

**3. Customer Segment Intelligence** *Use to understand how different customer types respond*

```
For [CLIENT NAME], compare how these segments respond across all tests:
- Mobile vs Desktop visitors
- New vs Returning customers

Are there segments consistently outperforming? Should we be running
segment-specific tests? Where's the biggest opportunity gap?

```

**What you'll get:** Conversion rates by device type, performance differences between new vs returning visitors, and recommendations for segment-specific optimization.

***

**4. Profit Trap Detection** *Use to catch tests where more conversions = less profit*

```
Review all tests for [CLIENT NAME] and identify any "profit traps" -
tests where conversion rate improved but revenue per visitor or
gross profit per visitor decreased.

Flag any tests where we might be winning the battle but losing the war.

```

**What you'll get:** Tests where conversion went up but profit went down, warnings about implementing harmful "winners", and true profit-focused recommendations.

***

**5. Quarterly Test Roadmap** *Use for strategic planning*

```
Based on [CLIENT NAME]'s test history:
1. What test categories have delivered the best ROI?
2. What areas haven't been tested yet (blind spots)?
3. Based on winners, what specific follow-up tests should we run?
4. Prioritize 5 test ideas for next quarter by potential impact.

```

**What you'll get:** Analysis of highest-performing test categories, untested areas, and a prioritized test roadmap for the next quarter.

***

## For Brand Operators

**1. Weekly Test Pulse Check** *Use for quick status instead of reviewing dashboards*

```
Give me a quick status on all my running tests:
- Which have reached statistical significance?
- Which are trending positive vs negative?
- Any that should be ended early (clear winner/loser)?
- Any that need more time to reach significance?

```

**What you'll get:** Status of all running tests, statistical significance levels, clear winner/loser identification, and recommendations for early stopping or extension.

***

**2. Profit Opportunity Scan** *Use to find biggest revenue opportunities*

```
Looking at my completed tests from the past 6 months:
1. Which winning variations had the highest revenue per visitor lift?
2. Which had the highest gross profit per visitor lift?
3. Are there any winners I haven't implemented yet?
4. Rank my top 3 profit opportunities by potential monthly revenue impact.

```

**What you'll get:** Ranked list of winners by revenue impact, un-implemented winners leaving money on the table, and a prioritized implementation list.

***

**3. My Best Customer Segments** *Use to know where to focus optimization efforts*

```
Across my tests, which customer segments perform best?
Compare response rates by:
- Device (Mobile vs Desktop)
- Customer type (New vs Returning)
- Traffic source (if available)

Where should I focus my optimization efforts for maximum ROI?

```

**What you'll get:** Performance breakdown by device type, new vs returning comparison, and recommendations for resource allocation.

***

**4. Testing Strategy Health Check** *Use to evaluate testing program effectiveness*

```
Review my testing history and tell me:
1. How many tests have I completed in the past 3 months?
2. What's my win rate (% of tests with significant winners)?
3. What types of tests am I running most? What am I missing?
4. Am I building on previous learnings or testing randomly?
5. What's my testing velocity compared to best practices?

```

**What you'll get:** Test completion count, win rate analysis, test type distribution, and recommendations for improving your testing program.

***

**5. Price Sensitivity Analysis** *Use to understand customer price tolerance*

```
Based on my price tests and offer tests:
1. What have I learned about my customers' price sensitivity?
2. Are there products or categories that are more price-sensitive?
3. Do new vs returning customers respond differently to pricing?
4. What's the optimal discount threshold based on test data?

```

**What you'll get:** Price sensitivity insights from test data, segment-specific price response differences, and data-backed discount recommendations.

## Best Practices

### Organization Context

* Always specify the `organization` parameter when working with multiple organizations
* Use `getOrganizationsList` first to see available organizations
* Cache organization IDs in your workflow to avoid repeated lookups

### Security

* Never share your access tokens
* Tokens are scoped to all organizations you have access to
* Revoke access immediately if compromised
