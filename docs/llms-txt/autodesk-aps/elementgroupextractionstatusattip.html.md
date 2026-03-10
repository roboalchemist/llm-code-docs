# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/reference/queries/elementgroupextractionstatusattip.html

<div class="api-documentation"><div class="title-category">Queries</div>
<meta name="sphinx-version" content="5.0.0">
            
  <section id="elementgroupextractionstatusattip">
<h1>elementGroupExtractionStatusAtTip</h1>
<p><a class="reference external" href="#"><img alt="query" src="../../../../_images/badge_query.png" style="height: 21px;"></a></p>
<p>Retrieves the extraction status of the given elementGroup for the latest version.</p>
<p><strong>Template for Query:</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span>query<span class="w"> </span>GetElementGroupExtractionStatusAtTip<span class="o">(</span><span class="nv">$fileUrn</span>:<span class="w"> </span>ID!,<span class="w"> </span><span class="nv">$accProjectId</span>:<span class="w"> </span>ID!<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>elementGroupExtractionStatusAtTip<span class="o">(</span>fileUrn:<span class="w"> </span><span class="nv">$fileUrn</span>,<span class="w"> </span>accProjectId:<span class="w"> </span><span class="nv">$accProjectId</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="c1"># ElementGroupExtractionStatusAtTip Fields</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Template for Query Variables:</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"fileUrn"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;SOME-ID-TYPE-SCALAR-VALUE&gt;"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"accProjectId"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;SOME-ID-TYPE-SCALAR-VALUE&gt;"</span>
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
<div class="table-section"><table><thead></thead><tbody><tr><td><span class="name">fileUrn</span><span class="required">*</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel-beta/v1/reference/scalars">ID!</a> <code class="docutils literal notranslate"><span class="pre">non-null</span></code></div></td><td>File to retrieve elementGroup extraction status from.</td></tr><tr><td><span class="name">accProjectId</span><span class="required">*</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel-beta/v1/reference/scalars">ID!</a> <code class="docutils literal notranslate"><span class="pre">non-null</span></code></div></td><td>ACC Project Id of the elementGroup.</td></tr></tbody></table><div class="text-required">* Required</div></div>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
<section id="possible-returns">
<a href="#possible-returns"><h2>Possible Returns</h2></a>
<div class="table-section"><table><thead><tr><th>Value Type</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elementgroupextractionstatus">ElementGroupExtractionStatus</a></td>
<td>Information about elementGroup extraction status.</td>
</tr>
</tbody></table></div>
<div class="line-block">
<div class="line"><br></div>
</div>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
</section>


            <div class="clearer"></div>
          </div>