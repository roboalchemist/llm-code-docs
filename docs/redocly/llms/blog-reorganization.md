# Source: https://redocly.com/blog/blog-reorganization.md

# Reorganizing our blog for better discovery and SEO

We just reorganized our entire blogâover 200 posts spanning years of content about APIs, OpenAPI, developer portals, documentation, and more.

The goal was simple: make it easier for people to find what they're looking for.

But the impact goes beyond navigation.
Better organization improves SEO.
It helps search engines understand our content.
It helps readers discover related topics.
And it helps us understand what we've written about.

Here's what we did and why it matters.

## The problem: Flat categories don't scale

Our blog had grown organically over the years.
We had categories like "OpenAPI," "API design," "Developer portal," and "Docs-as-code."
But as we published more content, those categories became too broad.

A post about "OpenAPI parameter types" and a post about "OpenAPI 3.2.0 support" both lived under "OpenAPI."
A post about "API governance best practices" and a post about "linting rulesets" both lived under "API governance."

Readers looking for something specific had to scroll through dozens of posts to find what they needed.
Search engines had less context about what each post actually covered.

We needed a better system.

## The solution: Hierarchical categories and subcategories

We moved to a hierarchical category structure using categories and subcategories.

Instead of just "OpenAPI," we now have:

- `api-specifications:openapi` â Posts specifically about OpenAPI
- `api-specifications:asyncapi` â Posts about AsyncAPI
- `api-specifications:arazzo` â Posts about Arazzo workflows
- `api-specifications:contract-patterns` â Posts about contract patterns and standards


Instead of just "API governance," we now have:

- `api-governance` â General governance topics
- `api-governance:linting-rulesets` â Posts about linting and rulesets
- `api-governance:review-workflows` â Posts about review processes
- `api-governance:compliance-quality` â Posts about compliance and quality
- `api-governance:lifecycle-gates` â Posts about lifecycle management


Instead of just "Technical documentation," we now have:

- `technical-documentation:tutorials-onboarding` â Getting started guides
- `technical-documentation:writing-style` â Writing and style guidance
- `technical-documentation:docs-ux` â Documentation user experience
- `technical-documentation:conceptual-documentation` â Conceptual content
- `technical-documentation:ai-assisted-docs` â AI-assisted documentation


This structure gives readers and search engines much more context.
A post tagged with `api-lifecycle:design` is clearly about API design within the lifecycle context.
A post tagged with `api-documentation:reference-docs` is specifically about reference documentation, not general API docs.

## Better navigation for readers

The most immediate benefit is better navigation.

When someone reads a post about OpenAPI parameter types, they can now easily find related posts about:

- OpenAPI examples (`api-specifications:openapi`)
- API design (`api-lifecycle:design`)
- OpenAPI best practices (`api-specifications:openapi`)


The hierarchical structure creates natural pathways through our content.
Readers can drill down into specific topics or explore broader themes.

This isn't just about convenienceâit's about helping people learn.
When related content is easier to discover, readers can build deeper understanding faster.

## SEO benefits: Better signals for search engines

Better organization also improves SEO.

Search engines use category structures to understand content relationships.
When we tag a post with `api-specifications:openapi` and `api-lifecycle:design`, we're telling search engines:

- This post is about OpenAPI (a specific specification)
- It's also about API design (a lifecycle concern)
- It relates to other posts in both categories


This helps search engines:

- **Understand topic clusters** â They can see that we have multiple posts about OpenAPI and API design, establishing topical authority
- **Improve internal linking** â Related posts are easier to discover and link together
- **Enhance context** â The subcategory provides additional semantic meaning


For people searching outside of Redoclyâmaybe someone searching for "OpenAPI parameter types" or "API governance best practices"âour better-organized content provides clearer signals about relevance.

The hierarchical structure also helps with:

- **Topic modeling** â Search engines can better understand what topics we cover comprehensively
- **Content freshness** â They can see when we publish new content in specific subcategories
- **User intent matching** â Subcategories help match queries to the right level of specificity


## From idea to implementation in two days

One of the most satisfying parts of this project was how quickly we could move from idea to implementation.

We have a great junior developer (shoutout to Daryna) on the team who took on this reorganization.
And completed it...

**All in two days.**

This is what good tooling and clear processes enable.
When you have:

- Clear category definitions
- Scripts to help with bulk updates
- A developer who can move fast
- A team that trusts them to execute


You can go from "we should reorganize the blog" to "the blog is reorganized" in 48 hours.

That speed matters.
It means we can improve the experience for readers immediately.
It means we don't spend months planningâwe just do it.

## What's next

The reorganization is complete, but the benefits will compound over time.

As we publish new content, we'll use the hierarchical categories from the start.
Readers will have better ways to discover related posts.
Search engines will have clearer signals about our content.

And we'll learn from the data.
Which subcategories get the most traffic?
Which topics do readers explore together?
What gaps exist in our content?

The better organization doesn't just help readers find contentâit helps us understand what content we should create next.

Also, how about an RSS feed?

## The takeaway

Good organization scales.

What starts as "a few blog posts" becomes hundreds.
What starts as "simple categories" needs structure.
What starts as "easy to navigate" becomes overwhelming.

But with the right structureâhierarchical categories that provide contextâyou can maintain clarity even as content grows.

And when you have the right team and processes, you can make those improvements quickly.

Two days to reorganize 200+ posts.
Two days to improve navigation for every reader.
Two days to give search engines better signals.

That's the power of good organization and a great team.