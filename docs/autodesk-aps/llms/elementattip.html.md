# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/reference/queries/elementattip.html

<div class="api-documentation"><div class="title-category">Queries</div>
<meta name="sphinx-version" content="5.0.0">
            
  <section id="elementattip">
<h1>elementAtTip</h1>
<p><a class="reference external" href="#"><img alt="query" src="../../../../_images/badge_query.png" style="height: 21px;"></a></p>
<p>Retrieves element using given ID.</p>
<p><strong>Template for Query:</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span>query<span class="w"> </span>GetElementAtTip<span class="o">(</span><span class="nv">$elementId</span>:<span class="w"> </span>ID!<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>elementAtTip<span class="o">(</span>elementId:<span class="w"> </span><span class="nv">$elementId</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="c1"># ElementAtTip Fields</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Template for Query Variables:</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"elementId"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"&lt;SOME-ID-TYPE-SCALAR-VALUE&gt;"</span>
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
<div class="table-section"><table><thead></thead><tbody><tr><td><span class="name">elementId</span><span class="required">*</span><div class="type"><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/scalars">ID!</a> <code class="docutils literal notranslate"><span class="pre">non-null</span></code></div></td><td>Element to retrieve.</td></tr></tbody></table><div class="text-required">* Required</div></div>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
<section id="possible-returns">
<a href="#possible-returns"><h2>Possible Returns</h2></a>
<div class="table-section"><table><thead><tr><th>Value Type</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/element">Element</a></td>
<td>Represents an element type.</td>
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
<p>Retrieves an element at tip by element ID along with its properties.</p>
<p><strong>Query:</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span>GetElementAtTip<span class="o">(</span><span class="nv">$elementId</span>:<span class="w"> </span>ID!,<span class="w"> </span><span class="nv">$propertiesPagination</span>:<span class="w"> </span>PaginationInput<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>elementAtTip<span class="o">(</span>elementId:<span class="w"> </span><span class="nv">$elementId</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>id
<span class="w">    </span>name
<span class="w">    </span>properties<span class="o">(</span>pagination:<span class="w"> </span><span class="nv">$propertiesPagination</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">      </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">        </span>name
<span class="w">        </span>value
<span class="w">      </span><span class="o">}</span>
<span class="w">    </span><span class="o">}</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Query Variables:</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"elementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QV0hqdllJalM3NmNWbURQTXJFMXZRXzEwMDAwMA"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"propertiesPagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"limit"</span><span class="p">:</span><span class="w"> </span><span class="mi">5</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Response:</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"elementAtTip"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX5FMnRqOFJFOXRsSlRQNU9WVzBiaDZ4X0wyQ35QV0hqdllJalM3NmNWbURQTXJFMXZRXzEwMDAwMA"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2.5\" x 5\" rectangular (Orange)"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"pageSize"</span><span class="p">:</span><span class="w"> </span><span class="mi">5</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Y3Vyc341fjU"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">          </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">1.2192</span>
<span class="w">          </span><span class="p">},</span>
<span class="w">          </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">          </span><span class="p">},</span>
<span class="w">          </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.24032209999999998</span>
<span class="w">          </span><span class="p">},</span>
<span class="w">          </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.0098322384</span>
<span class="w">          </span><span class="p">},</span>
<span class="w">          </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">]</span>
<span class="w">      </span><span class="p">}</span>
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