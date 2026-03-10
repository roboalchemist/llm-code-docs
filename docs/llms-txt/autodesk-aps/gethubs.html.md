# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/tutorials/tutorial-01/gethubs.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="get-hubs">
<h1>Get Hubs</h1>
<p>In this guide, you will learn how to retrieve a list of all the hubs you have access to.</p>
<p>By the end of this guide, you will be able to:</p>
<ul class="simple">
<li>Send a query using AEC Data Model Explorer.</li>
<li>Understand the fields in the <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/hubs">hubs</a>  query, <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/hubs">Hubs</a>  object, and <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/hub">Hub</a> objects.</li>
</ul>
<p>You will use the following query in this guide:</p>
<div class="table-section"><table><thead><tr><th>Type</th><th>Operation</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>Query</td>
<td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/hubs">hubs</a></td>
<td>Retrieves all hubs accessible to you.</td>
</tr>
</tbody></table></div>
<section id="step-1-request-a-list-of-hubs">
<a href="#step-1-request-a-list-of-hubs"><h2>Step 1: Request a list of Hubs</h2></a>
<p>The <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/hubs">hubs</a> query returns a <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/hubs">Hubs</a> object. The Hubs object contains an array of <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/hub">Hub</a> objects. While the Hub object has many fields, for this exercise, we will be requesting the <code class="docutils literal notranslate"><span class="pre">id</span></code> and the <code class="docutils literal notranslate"><span class="pre">name</span></code> fields only.</p>
<blockquote>
<div><ol class="arabic">
<li>In <a class="reference external" href="https://aecdatamodel-explorer.autodesk.io/">AEC Data Model Explorer</a>, the query is populated by default in the <strong>Query Pane</strong>. You can also edit or update the query as per your requirement and run it.</p>
<blockquote>
<div><p><strong>Query</strong></p>
<blockquote>
<div><div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span>GetHubs<span class="w"> </span><span class="o">{</span>
<span class="w">  </span>hubs<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>pagination<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>cursor
<span class="w">    </span><span class="o">}</span>
<span class="w">    </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>name
<span class="w">      </span>id
<span class="w">    </span><span class="o">}</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</div></blockquote>
</li>
<li>Click <strong>Play</strong>. A list of hubs that you have access to is displayed in the response section. It should be similar to the following code-block:</p>
<blockquote>
<div><p><strong>Response</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"hubs"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"AEC DM Developer Advocacy Support"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.ace:prod.scope:dccde3e3-c20c-40d3-a27c-7ac53b051b6e"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Developer Advocacy Support"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.ace:prod.scope:c0c44a35-fc67-4a8d-8967-f2d975bc03ec"</span>
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
<p>Note down the ID of the hubs that you wish to use. You will need this ID for the remaining guides.</p>
<p>After working through the steps mentioned above, you should see a screen similar to the following image:</p>
<img alt="../../../../_images/gethubs.png" src="../../../../_images/gethubs.png">
</div></blockquote>
</section>
</section>


            <div class="clearer"></div>
          </div>