# Apple Developer Documentation

Unified source for Apple framework documentation from developer.apple.com/documentation/.

## Structure

Each subdirectory corresponds to one Apple framework, matching the URL path at developer.apple.com/documentation/{framework}/. Apple organizes docs by framework, not by platform — a single framework page covers all platforms it supports (macOS, iOS, tvOS, watchOS, visionOS).

## Covered Frameworks

| Framework | Files | Content |
|---|---|---|
| applescript | 91 | Mac Automation Scripting Guide (complete) |
| osascript | 3 | CLI reference, JXA guide |

## Adding a New Framework

1. Create a subdirectory named after the framework (lowercase): `apple-developer-docs/{framework}/`
2. Add markdown files with key classes, protocols, common patterns, and code examples
3. Update this index

## Sourcing Strategy

Apple Developer Documentation (developer.apple.com) is dynamically rendered and not easily scrapeable. Approaches in priority order:

1. **llms.txt** — check developer.apple.com/llms.txt (not available as of Mar 2026)
2. **DocC archives** — shipped with Xcode, can be converted to markdown
3. **GitHub repos** — some frameworks have open-source repos with docs (Swift, swift-argument-parser)
4. **WWDC transcripts** — available as text, good for concepts and patterns
5. **Community mirrors** — GitHub repos with Apple docs in markdown
6. **Headless browser scrape** — last resort

## Full Framework Inventory

Apple ships ~371 frameworks. See DOCS-12047 in trckr for the complete list with tickets.
Only add frameworks as needed — don't try to scrape all 371 at once.
