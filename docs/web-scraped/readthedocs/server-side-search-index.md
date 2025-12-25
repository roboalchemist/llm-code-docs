# Source: https://docs.readthedocs.com/platform/latest/server-side-search/index.html

# Server side search[](#server-side-search "Link to this heading")

Read the Docs provides full-text search across all of the pages of all projects, this is powered by [Elasticsearch](https://www.elastic.co/products/elasticsearch).

See also

[[Search query syntax]](syntax.html)

:   Syntax options for searching Read the Docs projects

[[Server side search API]](api.html)

:   Reference to the Server Side Search API

## Search features[](#search-features "Link to this heading")

Read the Docs has the following search features:

Search across [[subprojects]](../subprojects.html)

:   Subprojects allow you to host multiple discrete projects on a single domain. Every subproject hosted on that same domain is included in the search results of the main project.

Search results land on the exact content you were looking for

:   We index every heading in the document, allowing you to get search results exactly to the content that you are searching for. Try this out by searching for ["full-text search"](https://docs.readthedocs.io/en/latest/search.html?q=%22full-text+search%22).

Full control over which results should be listed first

:   Set a custom rank per page, allowing you to deprecate content, and always show relevant content to your users first. See [[search.ranking]](../config-file/v2.html#search-ranking).

Search across projects you have access to

:   Search across all the projects you have access to in your Dashboard. **Don't remember where you found that document the other day? No problem, you can search across them all.**

    You can also specify what projects you want to search using the [`project:`] syntax, for example: ["project:docs project:dev search"](https://docs.readthedocs.io/en/latest/search.html?q=project:docs+project:dev+search). See [[Search query syntax]](syntax.html).

Special query syntax for more specific results

:   We support a full range of search queries. You can see some examples at [[Special queries]](syntax.html#special-queries).

Configurable

:   Tweak search results according to your needs using a [[configuration file]](../config-file/v2.html#search).

Ready to use

:   We override the default search engine of your Sphinx project with ours to provide you with all these benefits within your project. We fallback to the built-in search engine from your project if ours doesn't return any results, just in case we missed something 😄.

API

:   Integrate our search as you like. See [[Server side search API]](api.html).

Analytics

:   Know what your users are searching for. See [[Search analytics]](../search-analytics.html)

<figure id="id1" class="align-center">
<a href="../_images/search-analytics-demo.png" class="reference internal image-reference"><img src="../_images/search-analytics-demo.png" style="width: 50%;" alt="Search analytics demo" /></a>
<figcaption><p><span class="caption-text">Search analytics demo. Read more in <a href="../search-analytics.html" class="reference internal"><span class="doc">Search analytics</span></a>.</span><a href="#id1" class="headerlink" title="Link to this image"></a></p></figcaption>
</figure>