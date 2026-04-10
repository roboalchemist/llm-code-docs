# Source: https://developers.kit.com/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://developers.kit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

> Developer platform updates and new features.

<Update label="March 2026" tags={["Kit App Store"]}>
  ## 🚀 App Store Search

  The Kit App Store now has free-text search. Creators can search by app name, category, or description with real-time debounced results and fuzzy/partial matching. The category filter has moved into a dropdown co-located with the search input. No API changes — this is an in-product UI feature available at `app.kit.com` under Automate > Apps. See the [App Store overview](https://developers.kit.com/kit-app-store/overview) and [app details page](https://developers.kit.com/kit-app-store/app-details-page) for context on the App Store surface.
</Update>

<Update label="February 2026" tags={["Documentation"]}>
  ## 🚀 Kit Developer Docs MCP server

  Connect your AI coding agent directly to Kit's developer documentation using the [Kit Developer Docs MCP server](https://developers.kit.com/mcp/kit-developer-docs-mcp). Supported clients can query the full API reference on demand, make live API calls on your behalf, and spin up local OAuth servers for testing.
</Update>

<Update label="February 2026" tags={["API", "Webhooks"]}>
  ## 🚀 Custom Field Webhooks & Bulk Updates

  * Introduced 3 new webhook events for custom fields: `custom_field.field_created`, `custom_field.field_deleted`, and `custom_field.field_value_updated`, enabling real-time sync with third-party apps.
  * Added a bulk update endpoint (`POST /v4/bulk/custom_fields/subscribers`) to update multiple custom field values for multiple subscribers in a single API call.
  * [Learn more about webhooks](https://developers.kit.com/api-reference/webhooks/create-a-webhook) and [bulk updates](https://developers.kit.com/api-reference/custom-fields/bulk-update-subscriber-custom-field-values).
</Update>

<Update label="January 2026" tags={["Plugins"]}>
  ## 🚀 Transparent color option now available in color picker

  The [color picker component](https://developers.kit.com/plugins/component-library/color-picker) now supports an `allow_transparent` property that displays a "Transparent" toggle, allowing creators to set colors to transparent.
</Update>

<Update label="December 2025" tags={["Kit App Store"]}>
  ## 🚀 App Settings now live in Kit App Store

  Developers can now set an external "App Settings" URL in their app settings, allowing Creators to be able to customize their app setup post-installation, reducing account bloat by controlling data creation and sync. Read about best practices of how to implement this [here](https://developers.kit.com/kit-app-store/app-details-page#how-to-configure).
</Update>

<Update label="November 2025" tags={["Kit App Store"]}>
  ## 🔧 Improved Kit App Store Sorting

  * Default sorting now highlights the most popular apps by all-time installations.
  * Introduced a "Trending" category for apps gaining traction across our creators.
  * Renamed "Last added" to "Newest" for clarity.
</Update>

<Update label="October 2025" tags={["API", "Analytics"]}>
  ## 🚀 New API endpoints: "List stats for a subscriber" and "Filter subscribers based on engagement"

  Developers can now use Kit's API to filter subscribers by events like `opened`, `clicked`, `sent`, `delivered`, and `subscribed` with customizable date ranges and event counts. [Explore the API](https://developers.kit.com/api-reference/subscribers/filter-subscribers-based-on-engagement) to enhance subscriber engagement tracking. Additionally, the `List stats` endpoint now supports specifying date ranges for subscriber engagement data. [Learn more](https://developers.kit.com/api-reference/subscribers/list-stats-for-a-subscriber).
</Update>

<Update label="October 2025" tags={["Automation", "Plugins"]}>
  ## 🚀 Automation nodes app plugin environment launched

  Developers can now integrate third-party apps with [Kit Visual Automations](https://kit.com/features/automations) using action and event nodes. This opens up powerful new ways for developers to build with Kit, and for creators to automate their workflows.

  * [Event nodes](https://developers.kit.com/plugins/automation-nodes/plugin-flow#event-node) trigger automations on conditions like "call booked" or "survey completed".
  * [Action nodes](https://developers.kit.com/plugins/automation-nodes/plugin-flow#action-node) perform tasks in external systems such as "send an SMS" or "enroll a subscriber in a course".
  * Apps like [Shopify](https://app.kit.com/apps/330), [Thinkific](https://app.kit.com/apps/1451), and [Calendly](https://app.kit.com/apps/2063) are already utilizing these nodes.

  Explore more in our [documentation](https://developers.kit.com/plugins/automation-nodes/overview).
</Update>

<Update label="October 2025" tags={["Kit App Store", "Authentication"]}>
  ## 🚀 Dynamic return URLs for app installations

  Developers can now redirect users back to specific pages after completing an app install using the `return_to` query parameter in [installation flows](https://developers.kit.com/kit-app-store/authentication#externally-initiating-installations), enabling smoother integration experiences that originate from partner sites.
</Update>

<Update label="September 2025" tags={["Documentation"]}>
  ## 📖 Developer changelog now live

  <Frame>
        <img src="https://mintcdn.com/kit-314e57c1/i-AvK0JCWNO96-y6/images/changelog/2025-09-changelog.png?fit=max&auto=format&n=i-AvK0JCWNO96-y6&q=85&s=03d99b89af1c56bf2563463e7546f321" alt="Developer changelog interface" width="2880" height="1450" data-path="images/changelog/2025-09-changelog.png" />
  </Frame>

  Stay up to date with Kit's latest developer platform updates through our new changelog featuring:

  * **Emoji categories**: 🚀 Added, 🔧 Changed, 🐛 Fixed, ⚠️ Breaking Changes
  * **RSS subscription**: Never miss an update with the RSS feed button
  * **Smart filtering**: Filter by product area including Kit App Store, Plugins, API, Authentication, and more
  * **Copy functionality**: Easily share updates with the copy page feature

  [Subscribe to updates](https://developers.kit.com/changelog/rss.xml) to stay informed about the latest changes.
</Update>

<Update label="September 2025" tags={["API"]}>
  ## 🚀 New subscriber stats endpoint available

  Get comprehensive engagement metrics for individual subscribers including sends, opens, clicks, bounce rates, and timestamps via the new [subscriber stats API endpoint](https://developers.kit.com/api-reference/subscribers/list-stats-for-a-subscriber).
</Update>

<Update label="August 2025" tags={["Plugins"]}>
  ## 🚀 New plugin components and dependency support now available

  * New plugin components: [Radio Group](https://developers.kit.com/plugins/component-library/radio-group), [Slider](https://developers.kit.com/plugins/component-library/slider), [Textarea](https://developers.kit.com/plugins/component-library/textarea), [Toggle](https://developers.kit.com/plugins/component-library/toggle), [Numerical Input](https://developers.kit.com/plugins/component-library/numerical-input)
  * New plugin capabilities: [Group](https://developers.kit.com/plugins/component-library/group), [Dependencies](https://developers.kit.com/plugins/component-library/dependencies)
  * Plugin enhancements: Transparency and weights in [Font Picker](https://developers.kit.com/plugins/component-library/font-picker), a11y improvements across all components
</Update>

<Update label="August 2025" tags={["Kit App Store"]}>
  ## 🔧 Kit App Store and app management UX improvements

  * [Entire app cards](https://app.kit.com/apps) now clickable with streamlined navigation and consistent button hierarchy
  * New install button directly on [Build tab](https://app.kit.com/apps?is=created) for faster app testing workflows
  * In app settings (`https://app.kit.com/apps/:app_id/auth`), API and Plugin Authentication separated into distinct sections with clearer plugin type display
</Update>

<Update label="August 2025" tags={["Kit App Store", "Authentication"]}>
  ## 🚀 App Versioning now available for seamless authentication updates

  Developers can now ensure creators have access to their latest functionality through [app versioning](https://developers.kit.com/kit-app-store/app-versioning):

  * Apps automatically create new versions when authentication requirements change
  * Creators receive smart notifications and can update permissions without reinstalling
  * Plugin-level scope control with cumulative permission tracking across all plugins
</Update>

<Update label="August 2025" tags={["Authentication", "API"]}>
  ## 🔧 OAuth flow now starts from api.kit.com

  Kit's OAuth flow [is now initiated](https://developers.kit.com/api-reference/authentication) from `api.kit.com/v4/oauth` for consistency with other API endpoints, replacing the previous `app.kit.com` requirement.
</Update>

<Update label="June 2025" tags={["Kit App Store"]}>
  ## 🚀 Direct app installation URLs now available

  Developers can now [drive app installations directly from their websites](https://developers.kit.com/kit-app-store/authentication#externally-initiating-installations) using `https://app.kit.com/apps/:app_id/install?k_app_id=k_:app_id` without requiring users to first visit Kit App Store.
</Update>

<Update label="June 2025" tags={["Kit App Store"]}>
  ## 🔧 App icons now display consistently across the Kit App Store

  App thumbnails now display as uniform squares (60x60px on detail pages, 40x40px elsewhere) with proper cropping and centering, ensuring professional appearance regardless of original image dimensions.
</Update>

<Update label="June 2025" tags={["Kit App Store", "Plugins"]}>
  ## 🚀 Plugin deletion now available for developers

  Developers can now permanently [delete plugins from their Kit apps](https://developers.kit.com/plugins/managing-plugins#deleting-plugins) to better manage their plugin inventory.
</Update>

<Update label="June 2025" tags={["Documentation", "API", "Kit App Store"]}>
  ## 🚀 Brand new developer documentation platform

  We've completely rebuilt our developer documentation from the ground up, centralizing all developer resources in one comprehensive hub at [developers.kit.com](https://developers.kit.com).

  ### Key improvements include:

  * **Unified resource center**: All guides, tutorials, and API documentation now live in one carefully structured location
  * **Updated content**: Every piece of documentation has been refreshed and expanded, from app creation guides to OAuth implementation tutorials
  * **Enhanced navigation**: Improved site structure makes finding relevant information faster and more intuitive

  ## 🚀 New interactive features

  ### API Sandbox

  * Test Kit's V4 API directly in the documentation
  * Input your API key and make live requests without leaving the docs
  * Perfect for rapid prototyping and testing

  ### Advanced Search & AI Support

  * Full-text search across all documentation
  * Built-in "Ask AI" functionality for instant answers
  * Industry-standard llms.txt and llms-full.txt support for AI integrations

  ## 🔧 Developer experience improvements

  * **Dark mode support**: Documentation now adapts to your preferred viewing mode
  * **SEO optimized**: Better discoverability for developers searching for Kit integration help
  * **Quick action CTAs**: Streamlined paths to sign up, join the developer community, and contact support
  * **Mobile responsive**: Optimized experience across all devices
</Update>


Built with [Mintlify](https://mintlify.com).