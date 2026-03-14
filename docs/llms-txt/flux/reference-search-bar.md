# Source: https://docs.flux.ai/reference/reference-search-bar.md

# Global Search

Find other Flux users, organizations or publicly available projects.

![](https://uploads.developerhub.io/prod/86Yw/6m3q87ip8zb8dsjvd5p635jhtdqy260jm7pmo9bbrezmx63wv1rnws4tgt599xia.png)

## Overview

Global search allows you to find users, organizations, publicly available projects, and templates. You'll see the global search field on any profile page, but not in the editor. Locate it in the top left corner of your screen in the navigation bar. 

To use global search, click the search field and start typing your query. You'll see an autocomplete list of users. Tap enter or return on your keyboard to see the full list results. In that results page, you can filter by projects, components, users, and organizations. 

![](https://uploads.developerhub.io/prod/86Yw/lfi4nc1nh8nm36huh0uhnylwfw9ytdx5csepk86147uiompklpjsu77v8u1kvogv.gif)

## Advanced Search

Global search supports a few basic search commands to narrow down results:

- **Phrase query**: a specific sequence of terms that must be matched next to one another. A phrase query needs to be surrounded by double quotes `""`. For example, the query `"Arduino Compatible"` only returns a record if it contains `“Arduino Compatible”` exactly in at least one attribute. 
    - _Note:_ _ __Typo tolerance is disabled inside the phrase_ _(i.e. within the quotes)._

- **Prohibit operator**: excludes records that contain a specific term. To exclude a term, you need to prefix it with a minus `-`. The engine only interprets the minus `-` as a prohibit operator when you place it at the start of a word. A minus `-` within double quotes `""` is not treated as a prohibit operator. Some examples:
    - `Arduino -Compatible` only matches records containing “Arduino”, but not “compatible”
    - `arduino-compatible` matches records containing “arduino-compatible” (there’s no exclusion because the minus `-` is in the middle of a word)
    - `-compatible` matches every record except those containing “compatible”
    - `-arduino compatible` matches records containing “compatible”, but not “arduino”
    - `"-arduino"` matches records containing “-arduino” (no exclusion performed because of the inclusion of the double quotes `""`)

## Further reading

- We've put together a [full tutorial](https://docs.flux.ai/flux/tutorials/reusing-community-projects) if you need help finding the right project.