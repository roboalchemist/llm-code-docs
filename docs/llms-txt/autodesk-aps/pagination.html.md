# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/developers_guide/pagination.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="pagination">
<h1>Pagination</h1>
<p>Pagination is a technique used to manage and display large datasets by dividing them into smaller and manageable pages. It allows users or applications to navigate through data incrementally, preventing information overload.</p>
<p>In this task, you will learn how to set up pagination, which allows you to efficiently navigate and work with large datasets. Pagination is a critical feature for user-friendly data navigation and essential for retrieving the right information.</p>
<p><strong>Cursor pagination:</strong> The AEC Data Model API supports data retrieval through cursor-based pagination. It uses a unique identifier (the cursor) associated with each page to fetch the next set of results. This approach provides precise navigation through large datasets, ensuring efficient and responsive data retrieval.</p>
<section id="step-1-retrieving-the-first-page">
<a href="#step-1-retrieving-the-first-page"><h2>Step 1: Retrieving the first page</h2></a>
<p>To access the initial page, you simply need to specify a page limit, and a cursor is not necessary. The cursor, embedded in the first response, aligns with your specified response limit. The cursor facilitates easy navigation to subsequent data pages beyond the first one until all available results have been displayed.</p>
<p>This activity demonstrates how to use the <a class="reference external" href="https://aecdatamodel-explorer.autodesk.io/">AEC Data Model Explorer</a> to fetch the initial page of projects in a hub by setting a specific page limit:</p>
<blockquote>
<div><ol class="arabic">
<li>Enter the following query in the query pane.</p>
<blockquote>
<div><p><strong>Note:</strong> To limit the response to only three results, the pagination limit is set to three as follows: pagination: {limit: 3}. If you do not set a page limit, the query will return responses based on the default page limit.</p>
<p><strong>Query</strong></p>
<p># Task 2 â Get Projects</p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query GetProjects($hubId: ID!) {
  projects(hubId: $hubId, pagination:{limit:3}) {
    pagination {
      cursor
      }
    results {
      id
      name
      alternativeIdentifiers{
        externalProjectId
        }
      }
    }
  }
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li>In the <strong>Query Variables</strong> pane, enter the <code class="docutils literal notranslate"><span class="pre">hubId</span></code> to retrieve the projects from.</p>
<blockquote>
<div><p><strong>Query variables</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"hubId"</span><span class="p">:</span><span class="s2">"b.03f98b13-ec95-461b-b945-765f496165c1"</span>
<span class="p">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li>Click <strong>Play</strong>. The response will display a list of three projects, including an initial cursor value of <code class="docutils literal notranslate"><span class="pre">"cursor":</span> <span class="pre">"Y3Vyc34xfjM"</span></code></p>
<blockquote>
<div><p><strong>Query response</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"projects"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Y3Vyc34xfjM"</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWltcHJvan5iLjAzZjk4YjEzLWVjOTUtNDYxYi1iOTQ1LTc2NWY0OTYxNjVjMX5iLjI1MTg2MzE1LWIyNWMtNDkxMC05MzkxLTllMGE4ZjhmNzA5Zg"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"JM AEC Data Model Samples"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"externalProjectId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"b.25186315-b25c-4910-9391-9e0a8f8f709f"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWltcHJvan5iLjAzZjk4YjEzLWVjOTUtNDYxYi1iOTQ1LTc2NWY0OTYxNjVjMX5iLjg3OGIzMTkxLWRkNmEtNGUxOS04MzQ0LTYzNDU4NjUwNWQ5YQ"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DAS AEC DM TEST PROJECT"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"externalProjectId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"b.878b3191-dd6a-4e19-8344-634586505d9a"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWltcHJvan5iLjAzZjk4YjEzLWVjOTUtNDYxYi1iOTQ1LTc2NWY0OTYxNjVjMX5iLjkyY2Y1ZDMwLTYxZjYtNGE3Yi1iM2JmLWMyZDk0YjZmYjJkYg"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"AECDM API Project"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"externalProjectId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"b.92cf5d30-61f6-4a7b-b3bf-c2d94b6fb2db"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">      </span><span class="p">]</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
</ol>
</div></blockquote>
</section>
<section id="step-2-navigate-to-the-next-page-using-a-cursor">
<a href="#step-2-navigate-to-the-next-page-using-a-cursor"><h2>Step 2: Navigate to the next page using a cursor</h2></a>
<p>This step demonstrates how to use the acquired cursor to browse through the data on the remaining pages that contain the search results. To navigate to the next page, we will use the previously generated encoded cursor value as <code class="docutils literal notranslate"><span class="pre">"cursor":</span> <span class="pre">"Y3Vyc34xfjM"</span></code> in our query to fetch data set. To establish the search index, the obtained encoded cursor must be passed in the query pane like this: <code class="docutils literal notranslate"><span class="pre">pagination:</span> <span class="pre">{cursor:</span> <span class="pre">"Y3Vyc34xfjM"}</span></code>.</p>
<blockquote>
<div><ol class="arabic">
<li>Enter the following query in the query pane.</p>
<blockquote>
<div><p><strong>Query</strong></p>
<blockquote>
<div><p># Task 2 â Get Projects</p>
</div></blockquote>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query GetProjects($hubId: ID!) {
  projects(hubId: $hubId, pagination:{cursor:"dXJuOmFkc2sud29ya3NwYWNlOnByb2QucHJvamVjdDo1NjZkOWNiNi0yOTA3LTRhOWQtYWU4OC0zYmI3Y2YyZjE4Yjd-Mw"}) {
    pagination {
      cursor
      }
    results {
      id
      name
      alternativeIdentifiers{
        dataManagementAPIProjectId
        }
      }
    }
  }
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li>In the Query Variables Pane, enter the <code class="docutils literal notranslate"><span class="pre">hubId</span></code> to retrieve the projects from.</p>
<blockquote>
<div><p><strong>Query variables</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"hubId"</span><span class="p">:</span><span class="s2">"urn:adsk.ace:prod.scope:dccde3e3-c20c-40d3-a27c-7ac53b051b6e"</span>
<span class="p">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li>Click <strong>Play</strong>. You will see one of the following cases:</p>
<blockquote>
<div><ol class="loweralpha simple">
<li>In case your hub still has enough projects to fill additional pages, youâll receive a list with the next three projects and another cursor.</li>
<li>If there arenât enough projects to display an additional page, your response will display the remaining projects and the value <code class="docutils literal notranslate"><span class="pre">"cursor":null</span></code> under pagination.</li>
</ol>
<p><strong>Query response</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"projects"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"dXJuOmFkc2sud29ya3NwYWNlOnByb2QucHJvamVjdDo2NDllNzQ2My0wZTc1LTRjMDMtOWM5Zi0zNDUwNzMzMzc4ZWN-Mw"</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.workspace:prod.project:566d9cb6-2907-4a9d-ae88-3bb7cf2f18b7"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Construction : Sample Project - Seaport Civic Center"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"dataManagementAPIProjectId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"b.9177ea8c-efb4-4612-8ef1-6e4ce114658c"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.workspace:prod.project:336b2f25-ceba-4375-bd9e-75dd03bb1ee9"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DAS Project"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"dataManagementAPIProjectId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"b.2def426a-c49a-4c35-9d9a-0290e254fc1d"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.workspace:prod.project:24dc6d5e-7ea1-4858-8b52-9c72abc2a592"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"JM tests"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"dataManagementAPIProjectId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"b.b5936885-90cd-40a7-aae5-89059ebbd557"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">      </span><span class="p">]</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
</ol>
</div></blockquote>
</section>
<section id="usage">
<a href="#usage"><h2>Usage</h2></a>
<p>Refer to the following table for the reference values:</p>
<div class="table-section"><table><thead><tr><th>Used by query</th><th>Description</th><th>Default limit</th><th>Maximum limit</th></tr></thead><tbody>
<tr class="row-even"><td><a class="reference external" href="en/docs/aecdatamodel/v1/reference/objects/hubs">Hubs</a></td>
<td>Contains a list of hubs returned in response to a query. A hub is a container of projects, shared resources, and users with a common context.</td>
<td>100</td>
<td>200</td>
</tr>
<tr class="row-odd"><td><a class="reference external" href="en/docs/aecdatamodel/v1/reference/objects/projects">Projects</a></td>
<td>Contains a list of projects returned in response to a query.</td>
<td>100</td>
<td>200</td>
</tr>
<tr class="row-even"><td><a class="reference external" href="en/docs/aecdatamodel/v1/reference/objects/folders">Folders</a></td>
<td>Contains a list of hubs returned in response to a query. A hub is a container of projects, shared resources, and users with a common context.</td>
<td>100</td>
<td>200</td>
</tr>
<tr class="row-odd"><td><a class="reference external" href="en/docs/aecdatamodel/v1/reference/objects/elementgroups">Elementgroups</a></td>
<td>Contains a list of object representing versions of drawings, typically returned in response to a query.</td>
<td>50</td>
<td>100</td>
</tr>
<tr class="row-even"><td><a class="reference external" href="en/docs/aecdatamodel/v1/reference/objects/elementgroupversions">Versions</a></td>
<td>Contains a list of object representing versions of drawings, typically returned in response to a query.</td>
<td>50</td>
<td>100</td>
</tr>
<tr class="row-odd"><td><a class="reference external" href="en/docs/aecdatamodel/v1/reference/objects/elements">Elements</a></td>
<td>Contains a list of object representing elements of a specific Elementgroups.</td>
<td>50</td>
<td>500</td>
</tr>
<tr class="row-even"><td><a class="reference external" href="en/docs/aecdatamodel/v1/reference/objects/properties">Properties</a></td>
<td>Contains a list of object representing properties of a specific element.</td>
<td>100</td>
<td>500</td>
</tr>
</tbody></table></div>
</section>
<section id="page-limit">
<a href="#page-limit"><h2>Page limit</h2></a>
<p>You may specify the <code class="docutils literal notranslate"><span class="pre">limit</span></code> attribute for each field, defining the number of items to be retrieved per page. The <code class="docutils literal notranslate"><span class="pre">limit</span></code> attribute is adjustable within the range of 1 to a maximum value based on the queried object. If not specified, it will default to the appropriate value based on the queried object.</p>
</section>
</section>


            <div class="clearer"></div>
          </div>