# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/tutorials/tutorial-02/task1a.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="get-elementgroups-based-on-metadata">
<h1>Get ElementGroups Based on Metadata</h1>
<p>In this guide, you will learn how to query hubs based on metadata using RSQL (a query language designed for filtering and querying data) and receive responses from the AEC Data Model server.</p>
<p>By the end of this guide, you will be able to:</p>
<ul class="simple">
<li>Fetch elementGroups from a hub based on the metadata using AEC Data Model Explorer.</li>
<li>Use filters on metadata like createdOn or createdBy on elementGroups with greater than or less than operators.</li>
<li>Understand the options and fields in the documentation on the <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementgroupsbyhub">elementGroupsByHub</a> query and <a class="reference external" href="en/docs/aecdatamodel/v1/reference/objects/elementgroup">elementGroup</a> object.</li>
</ul>
<p>You will use the following query in this guide:</p>
<div class="line-block">
<div class="line"><br></div>
</div>
<div class="table-section"><table><thead><tr><th>Type</th><th>Operation</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>Query</td>
<td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementgroupsbyhub">elementGroupsByHub</a></td>
<td>Retrieves elementGroups in the given hub, using additional RSQL filters if provided.</td>
</tr>
</tbody></table></div>
<div class="line-block">
<div class="line"><br></div>
</div>
<section id="step-1-request-elementgroups-by-hub">
<a href="#step-1-request-elementgroups-by-hub"><h2>Step 1: Request ElementGroups by Hub</h2></a>
<p>The <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementgroupsbyhub">elementGroupsByHub</a> query returns an <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elementgroups">ElementGroups</a> object.  While the ElementGroups object has many fields, for this exercise, we will be requesting the <code class="docutils literal notranslate"><span class="pre">id</span></code> and the <code class="docutils literal notranslate"><span class="pre">name</span></code> fields only.</p>
<blockquote>
<div><ol class="arabic simple">
<li>In <a class="reference external" href="https://aecdatamodel-explorer.autodesk.io/">AEC Data Model Explorer</a>, the query is populated by default in the <strong>Query Pane</strong>. You can also edit or update the query as per your requirement and run it.</li>
</ol>
<blockquote>
<div><p><strong>Query</strong></p>
<blockquote>
<div><div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span>elementGroupsByHub<span class="o">(</span><span class="nv">$hubId</span>:<span class="w"> </span>ID!,<span class="w"> </span><span class="nv">$filter</span>:<span class="w"> </span>ElementGroupFilterInput,<span class="w"> </span><span class="nv">$pagination</span>:<span class="w"> </span>PaginationInput<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>elementGroupsByHub<span class="o">(</span>hubId:<span class="w"> </span><span class="nv">$hubId</span>,<span class="w"> </span>filter:<span class="w"> </span><span class="nv">$filter</span>,<span class="w"> </span>pagination:<span class="w"> </span><span class="nv">$pagination</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>pagination<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>cursor
<span class="w">    </span><span class="o">}</span>
<span class="w">    </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>id
<span class="w">      </span>name
<span class="w">      </span>alternativeIdentifiers<span class="w"> </span><span class="o">{</span>
<span class="w">        </span>fileUrn
<span class="w">        </span>fileVersionUrn
<span class="w">      </span><span class="o">}</span>
<span class="w">    </span><span class="o">}</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="2">
<li>In the Query Variables Pane, replace the value of the <code class="docutils literal notranslate"><span class="pre">hubId</span></code> variable with the hub ID of the project obtained previously in <a class="reference external" href="/en/docs/aecdatamodel/v1/tutorials/tutorial-01/gethubs/#step-1-request-a-list-of-hubs">Get Started with AEC Data Model APIâ tutorialâs Get Hubs</a> task.</li>
<li>In the Query variables pane, set the metadata filter according to your preferences. This will allow you to query the data that you need.</li>
<li>In the Query variables pane, set the pagination limit to any required value. For clarity, we are setting the limit value to 5.</li>
</ol>
<blockquote>
<div><p><strong>Note</strong>: For information on the supported metadata filtering options, refer <a class="reference external" href="/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering">Advanced Filtering Capabilities</a>   page.</p>
<p><strong>Query Variables</strong></p>
<blockquote>
<div><div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="o">{</span>
<span class="w">  </span><span class="s2">"hubId"</span>:<span class="w"> </span><span class="s2">"urn:adsk.ace:prod.scope:dccde3e3-c20c-40d3-a27c-7ac53b051b6e"</span>,
<span class="w">  </span><span class="s2">"filter"</span>:<span class="w"> </span><span class="o">{</span>
<span class="w">    </span><span class="s2">"query"</span>:<span class="w"> </span><span class="s2">"metadata.createdOn&gt;2024-05-01T06:37:13.472Z"</span>
<span class="w">  </span><span class="o">}</span>,
<span class="w">  </span><span class="s2">"pagination"</span>:<span class="w"> </span><span class="o">{</span>
<span class="w">      </span><span class="s2">"limit"</span>:<span class="w"> </span><span class="m">5</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic" start="5">
<li>Click <strong>Play</strong>. A list of elementGroups that you have access to is displayed in the response section. It should be similar to the following code-block:</p>
<blockquote>
<div><p><strong>Response</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"elementGroupsByHub"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Y3Vyc341fjU"</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35uUVpyS1BEUVJVS0VFOWtmWWNHV0VB"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample HVAC.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:nQZrKPDQRUKEE9kfYcGWEA"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.nQZrKPDQRUKEE9kfYcGWEA?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35fR1IzdHpORlI3LV9tclFBOGR4TWN3"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Electrical.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:_GR3tzNFR7-_mrQA8dxMcw"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf._GR3tzNFR7-_mrQA8dxMcw?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Architectural.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:rEdJOCOqR0ekyJBBYlR9EA"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.rEdJOCOqR0ekyJBBYlR9EA?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRR"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Site.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:LvosTJ57RXefNY1bachQTQ"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.LvosTJ57RXefNY1bachQTQ?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1n"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Facades.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:fWDufB-ySmq5Fwn6Fj1_-g"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.fWDufB-ySmq5Fwn6Fj1_-g?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">      </span><span class="p">]</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</div></blockquote>
</li>
</ol>
</div></blockquote>
<p>Note down the ID of the elementGroup that you wish to use. You will need this ID for the remaining tasks. For illustration, in this tutorial we have used the ID of the elementGroup named <code class="docutils literal notranslate"><span class="pre">Snowdon</span> <span class="pre">Towers</span> <span class="pre">Sample</span> <span class="pre">Architectural.rvt</span></code>.</p>
<p>After working through the steps mentioned above, you should see a screen similar to the following image:</p>
<blockquote>
<div><img alt="../../../../_images/elementgroupsbyhub.png" src="../../../../_images/elementgroupsbyhub.png">
</div></blockquote>
</section>
</section>


            <div class="clearer"></div>
          </div>