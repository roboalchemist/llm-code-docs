# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/reference/queries/elementgroupbyversionnumber.html

<div class="api-documentation"><div class="title-category">Queries</div>
<meta name="sphinx-version" content="5.0.0">
            
  <section id="elementgroupbyversionnumber">
<h1>elementGroupByVersionNumber</h1>
<p><a class="reference external" href="#"><img alt="query" src="../../../../_images/badge_query.png" style="height: 21px;"></a></p>
<p>Retrieves elementGroup by version number and ID.</p>
<p><strong>Template for Query:</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span>query<span class="w"> </span>GetElementGroupByVersionNumber<span class="o">(</span><span class="nv">$elementGroupId</span>:<span class="w"> </span>ID!,<span class="w"> </span><span class="nv">$versionNumber</span>:<span class="w"> </span>Int!<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>elementGroupByVersionNumber<span class="o">(</span>elementGroupId:<span class="w"> </span><span class="nv">$elementGroupId</span>,<span class="w"> </span>versionNumber:<span class="w"> </span><span class="nv">$versionNumber</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="c1"># ElementGroupByVersionNumber Fields</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Template for Query Variables:</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"elementGroupId"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;SOME-ID-TYPE-SCALAR-VALUE&gt;"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"versionNumber"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;SOME-INT-TYPE-SCALAR-VALUE&gt;"</span>
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
<div class="table-section"><table><thead></thead><tbody><tr><td><span class="name">elementGroupId</span><span class="required">*</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/scalars">ID!</a> <code class="docutils literal notranslate"><span class="pre">non-null</span></code></div></td><td>The ID of the elementGroup.</td></tr><tr><td><span class="name">versionNumber</span><span class="required">*</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/scalars">Int!</a> <code class="docutils literal notranslate"><span class="pre">non-null</span></code></div></td><td>Version number to be retrieved.</td></tr></tbody></table><div class="text-required">* Required</div></div>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
<section id="possible-returns">
<a href="#possible-returns"><h2>Possible Returns</h2></a>
<div class="table-section"><table><thead><tr><th>Value Type</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elementgroup">ElementGroup</a></td>
<td>Represents a Revit model.</td>
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