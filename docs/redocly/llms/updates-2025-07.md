# Source: https://redocly.com/blog/updates-2025-07.md

# June and July 2025 updates âï¸

Summer has been a busy season at Redocly.
Over the past two months, we've rolled out powerful new features, accessibility improvements, analytics, and developer enhancements across our product suite â Realm, Reef, Revel, and Reunite.
We also released version 2.0 of Redocly CLI.

Here's what's new:

## ð Internationalization and accessibility

- Built-in translations: Out-of-the-box translations for multiple languages without extra setup.
- [Skip to content button](/docs/end-user/navigate-project#skip-to-content): Improves keyboard navigation and accessibility.
- Page and label properties: Customize navigation buttons with front matter for a smoother reading experience.
-  Font Awesome icons: Add icons to your sidebar, navbar, footer, or Markdoc content to bring more clarity and personality to your docs â we even added them to ours.


## ð¤ Smarter docs with LLM actions

We're continuing to integrate AI into documentation workflows.
Now every page includes LLM-related actions:

- View or copy the page as Markdown.
- Query ChatGPT or Claude directly about the page content.


This makes docs more interactive and helps your readers get answers faster.

## ð Analytics in Reunite

Reunite now has [built-in analytics](/docs/realm/reunite/project/analytics)!
Teams can track:

- Page views
- Searches (including âno resultsâ queries)
- AI search activity


These insights help you measure support deflection, identify documentation gaps, and understand developer behavior â all **without adding third-party trackers**.

## ð¡ AsyncAPI documentation improvements

We've shipped a smoother AsyncAPI docs experience, making it easier to document and explore websockets, message queues, and other event-driven APIs.

## ð ï¸ Developer experience upgrades

- API Functions logs now include function names for easier debugging.
- New hooks in React pages:
  - `usePageVersions` and `useActivePageVersion` â work with versioned content.
  - `useUserTeams` â access the teams assigned to the active user.
- GraphQL docs:
  - Rendering behavior now consistent with OpenAPI docs.
  - Deprecated queries, mutations, and subscriptions are now displayed.
- Arazzo compatibility: Variables replaced with servers and inputs, plus a new Path tab for editing request parameters.
- Improved code walkthroughs: Smarter trigger points for step changes.
- Syntax highlighting in Reunite editor for `.cjs` and `.mjs` files.


## ð Richer documentation formats

- Code groups: Use the new [code-group Markdoc tag](/docs/realm/content/markdoc-tags/code-group) for side-by-side tabbed language examples or a language dropdown menu.
- Request/response samples: The new [openapi-response-sample tag](/docs/realm/content/markdoc-tags/openapi-response-sample) separates request and response snippets for more granular rendering.
- Markdoc dropdown updates from the Reunite editor: Quickly insert built-in or custom functions.


## â¡ Quality of life enhancements

- Highlighting path parameters in request URLs.
- Branch deployments in Reunite for more flexible workflows.
- Removed old/deprecated rules (`path-excludes-patterns`, `info-license-url`) to keep things clean.


## ð Redocly CLI 2.0

We shipped **Redocly CLI 2.0** â a major release that modernizes the CLI and cleans up years of deprecated options, while adding new security and validation features.

### What's new

- Modernized and streamlined
  - Dropped legacy support for the old API Registry and Reference Docs products â CLI now works exclusively with Reunite.
  - Simplified configuration: only redocly.yaml is supported, with deprecated options removed.
  - Migrated to ES Modules for better code organization and modern Node.js support (current LTS or newer).
- Security and validation improvements
  - New x-security extension for Respect â define authentication at the step level and automatically transform secrets into headers or query params.
  - Sensitive fields (tokens, passwords) are now masked automatically in logs and outputs.
  - Added validation for JSON Schema format and stricter spec rulesets for OpenAPI, AsyncAPI, Arazzo, and Overlays.
  - New no-duplicated-tag-names rule plus improvements to schema type mismatch checks.
- Developer quality-of-life
  - Environment variable support for CLI arguments.
  - Extracted nullable-type-sibling rule for finer control over nullable validation.
  - Updated Respect command with new options for better test control.
  - Numerous fixes for config validation, server handling, and error reporting.


If you're upgrading from `1.x`, check out [our changelog](/docs/cli/changelog) â most changes are straightforward, but you'll want to update configs to match the streamlined rules and commands.

## ð Build Redocly with Us!

We're hiring software engineers to help shape the future of API documentation.

â Passionate about APIs?
â Excited by cutting-edge developer tools?

Join our team and be part of something big.

[Apply now â](https://redocly.com/careers#software-engineer)

## ð® Roadmap sneak peek

We're continuing to invest in features that make building and running with Redocly even more powerful:

- **MCP servers** â deeper integration with external tools and workflows.
- **Runtime logs** â richer visibility into what's happening behind the scenes.
- **Catalog** â richer ways to describe APIs, entities, and relationships.
- **Visual workflows builder** â model API interactions visually.
- **Performance** â faster response times and improved stability across large projects.


That's it for June and July. ð
As always, we'd love your feedback â let us know what you think!