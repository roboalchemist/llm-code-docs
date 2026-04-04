# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/reference/queries/elementgroupsbyproject.html

<div class="api-documentation"><div class="title-category">Queries</div>
<meta name="sphinx-version" content="5.0.0">
            
  <section id="elementgroupsbyproject">
<h1>elementGroupsByProject</h1>
<p><a class="reference external" href="#"><img alt="query" src="../../../../_images/badge_query.png" style="height: 21px;"></a></p>
<p>Retrieves elementGroups in the given project, using additional RSQL filters if provided.</p>
<p><strong>Template for Query:</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span>query<span class="w"> </span>GetElementGroupsByProject<span class="o">(</span><span class="nv">$projectId</span>:<span class="w"> </span>ID!,<span class="w"> </span><span class="nv">$filter</span>:<span class="w"> </span>ElementGroupFilterInput,<span class="w"> </span><span class="nv">$pagination</span>:<span class="w"> </span>PaginationInput<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>elementGroupsByProject<span class="o">(</span>projectId:<span class="w"> </span><span class="nv">$projectId</span>,<span class="w"> </span>filter:<span class="w"> </span><span class="nv">$filter</span>,<span class="w"> </span>pagination:<span class="w"> </span><span class="nv">$pagination</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="c1"># ElementGroupsByProject Fields</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Template for Query Variables:</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"projectId"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;SOME-ID-TYPE-SCALAR-VALUE&gt;"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"filter"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;SOME-ELEMENTGROUPFILTER-INPUT-TYPE-VALUE&gt;"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"pagination"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;SOME-PAGINATION-INPUT-TYPE-VALUE&gt;"</span>
<span class="p">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<div class="line-block">
<div class="line"><br></div>
</div>
<div class="line-block">
<div class="line"><br></div>
</div>
<section id="arguments">
<a href="#arguments"><h2>Arguments</h2></a>
<div class="table-section"><table><thead></thead><tbody><tr><td><span class="name">projectId</span><span class="required">*</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/scalars">ID!</a> <code class="docutils literal notranslate"><span class="pre">non-null</span></code></div></td><td>Project to retrieve elementGroups from.</td></tr><tr><td><span class="name">filter</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/inputs/elementgroupfilterinput">ElementGroupFilterInput</a></div></td><td>RSQL filter to use for searching elementGroups.</td></tr><tr><td><span class="name">pagination</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/inputs/paginationinput">PaginationInput</a></div></td><td>Specifies how to split the response into multiple pages.</td></tr></tbody></table><div class="text-required">* Required</div></div>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
<section id="possible-returns">
<a href="#possible-returns"><h2>Possible Returns</h2></a>
<div class="table-section"><table><thead><tr><th>Value Type</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elementgroups">ElementGroups!</a> <code class="docutils literal notranslate"><span class="pre">non-null</span></code></td>
<td>Contains a list of ElementGroups returned in response to a query.</td>
</tr>
</tbody></table></div>
<div class="line-block">
<div class="line"><br></div>
</div>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
<section id="examples">
<a href="#examples"><h2>Examples</h2></a>
</section>
</section>


            <div class="clearer"></div>
          </div>