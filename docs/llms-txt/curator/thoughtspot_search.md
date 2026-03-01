# Source: https://docs.curator.interworks.com/embedding_using_analytics/thoughtspot_content/thoughtspot_search.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ThoughtSpot Search

> Integrate ThoughtSpot search functionality for natural language query capabilities within Curator.

If you have [integrated ThoughtSpot](/creating_integrations/thoughtspot_connection/integrating_thoughtspot_with_curator)
you can follow this guide to add ThoughtSpot Search to Curator.

## Creating the ThoughtSpot Search

1. Navigate to the Curator backend > ThoughtSpot > ThoughtSpot Searches and click the "New ThoughtSpot Search" button.
2. Choose the Org where the data you'd like to search against lives.
3. Choose the type of search. The types include:
   1. Spotter - ThoughtSpot's new natural language search feature (replaces deprecated Sage)
   2. Standard Search - The standard ThoughtSpot Search experience
   3. Standard Search w/ Pre-made Answer - The standard Search experience, but initially loading with an Answer
4. Choose the data source or Answer you'd like the Search to load with, or none if you'd like the user to begin with a
   blank slate.
5. In the "Details" section, add a title. This will automatically generate a slug but feel free to overwrite it.
6. In the "Discovery" section, add keywords, a description, etc.
7. Hit the "Save" button.

## Adding the ThoughtSpot Search to the Curator Frontend

The ThoughtSpot Search is now created and accessible to Curator users, assuming they have ThoughtSpot users on the Org
being searched against. You can make the Search more discoverable in several ways:

1. Add it to your navigation.
2. Add it to a [page](/site_content_design/pages/pages_overview) directly.
3. Add it to a page as a [tile](/site_content_design/pages/tiles).
4. Add keywords so it can be easily found via Curator's search or in the [explorer](/site_content_design/pages/explorer).
