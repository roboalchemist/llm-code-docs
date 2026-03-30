# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/reference/queries/elementsbyhub.html

<div class="api-documentation"><div class="title-category">Queries</div>
<meta name="sphinx-version" content="5.0.0">
            
  <section id="elementsbyhub">
<h1>elementsByHub</h1>
<p><a class="reference external" href="#"><img alt="query" src="../../../../_images/badge_query.png" style="height: 21px;"></a></p>
<p>Retrieves elements from given hub, using additional RSQL filters if provided.</p>
<p><strong>Template for Query:</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span>query<span class="w"> </span>GetElementsByHub<span class="o">(</span><span class="nv">$hubId</span>:<span class="w"> </span>ID!,<span class="w"> </span><span class="nv">$filter</span>:<span class="w"> </span>ElementFilterInput,<span class="w"> </span><span class="nv">$pagination</span>:<span class="w"> </span>PaginationInput<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>elementsByHub<span class="o">(</span>hubId:<span class="w"> </span><span class="nv">$hubId</span>,<span class="w"> </span>filter:<span class="w"> </span><span class="nv">$filter</span>,<span class="w"> </span>pagination:<span class="w"> </span><span class="nv">$pagination</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="c1"># ElementsByHub Fields</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Template for Query Variables:</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"hubId"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;SOME-ID-TYPE-SCALAR-VALUE&gt;"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"filter"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;SOME-ELEMENTFILTER-INPUT-TYPE-VALUE&gt;"</span><span class="p">,</span>
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
<div class="table-section"><table><thead></thead><tbody><tr><td><span class="name">hubId</span><span class="required">*</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/scalars">ID!</a> <code class="docutils literal notranslate"><span class="pre">non-null</span></code></div></td><td>Hub to retrieve elements from.</td></tr><tr><td><span class="name">filter</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/inputs/elementfilterinput">ElementFilterInput</a></div></td><td>RSQL filter to use for searching elements.</td></tr><tr><td><span class="name">pagination</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/inputs/paginationinput">PaginationInput</a></div></td><td>Specifies how to split the response into multiple pages.</td></tr></tbody></table><div class="text-required">* Required</div></div>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
<section id="possible-returns">
<a href="#possible-returns"><h2>Possible Returns</h2></a>
<div class="table-section"><table><thead><tr><th>Value Type</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elements">Elements</a></td>
<td>Contains a list of Elements returned in response to a query.</td>
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
<section id="example-1">
<h3>Example 1</h3>
<p>Retrieves elements of category âWindowsâ across elementgroups under a hub by hub ID.</p>
<p><strong>Query:</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span>GetElementsByHub<span class="o">(</span><span class="nv">$hubId</span>:<span class="w"> </span>ID!,<span class="w"> </span><span class="nv">$filter</span>:<span class="w"> </span>ElementFilterInput,<span class="w"> </span><span class="nv">$pagination</span>:<span class="w"> </span>PaginationInput<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>elementsByHub<span class="o">(</span>hubId:<span class="w"> </span><span class="nv">$hubId</span>,<span class="w"> </span>filter:<span class="w"> </span><span class="nv">$filter</span>,<span class="w"> </span>pagination:<span class="w"> </span><span class="nv">$pagination</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>pagination<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>pageSize
<span class="w">      </span>cursor
<span class="w">    </span><span class="o">}</span>
<span class="w">    </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>id
<span class="w">      </span>name
<span class="w">    </span><span class="o">}</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Query Variables:</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"hubId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"b.e4fbd315-2dc5-4026-8ca3-80f09d24ff42"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"filter"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"query"</span><span class="p">:</span><span class="w"> </span><span class="s2">"property.name.category==Windows and 'property.name.Element Context'==Instance"</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"limit"</span><span class="p">:</span><span class="w"> </span><span class="mi">5</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Response:</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"elementsByHub"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"pageSize"</span><span class="p">:</span><span class="w"> </span><span class="mi">5</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWRjdXJzfk5VTEx-QlE9PX41"</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QQllLNWlOb1NsQ283QVpEOVdUM0V3XzEyM2ViN2M"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"32.10-sparing tbv installaties_1400x600"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QQllLNWlOb1NsQ283QVpEOVdUM0V3XzEyM2ViN2Q"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"32.10-sparing tbv installaties_1100x650"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QQllLNWlOb1NsQ283QVpEOVdUM0V3XzEyM2ViODY"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"32.10-sparing tbv installaties_500x300"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QQllLNWlOb1NsQ283QVpEOVdUM0V3XzEyM2ViOGE"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"32.10-sparing tbv installaties_625x150"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QQllLNWlOb1NsQ283QVpEOVdUM0V3XzEyM2ViOGM"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"32.10-sparing tbv installaties_400x150"</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">      </span><span class="p">]</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
</section>
</section>


            <div class="clearer"></div>
          </div>