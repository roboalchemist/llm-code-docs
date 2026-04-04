# Meilisearch is typo-tolerant:
hits = Article.search('deepre')
hits.first
```

We strongly recommend using the frontend search to enjoy the swift and responsive search-as-you-type experience.

### Frontend search

For testing purposes, you can explore the records using our built-in [search preview](/learn/getting_started/search_preview).

<img alt="Searching through Rails table data with Meilisearch search preview UI" />

We also provide resources to help you quickly build your own [frontend interface](/guides/front_end/front_end_integration).

## Next steps

When you're ready to use your own data, make sure to configure your [index settings](/reference/api/settings) first to follow [best practices](/learn/indexing/indexing_best_practices). For a full configuration example, see the [meilisearch-rails gem README](https://github.com/meilisearch/meilisearch-rails?tab=readme-ov-file#%EF%B8%8F-settings).