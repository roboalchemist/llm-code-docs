# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/tutorials/tutorial-02/task2a.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="get-versions-of-an-elementgroup">
<h1>Get Versions of an ElementGroup</h1>
<p>In this guide, you will learn how to query the versions of a specific elementGroup using the AEC Data Model Explorer. You will retrieve the version history of an elementGroup, including the version number and creation date.</p>
<p>By the end of this guide, you will be able to:</p>
<ul class="simple">
<li>Fetch versions for a particular elementGroup.</li>
<li>Understand the options and fields in the documentation on theâ¯elementGroupAtTip query, elementGroup object, andâ¯history / versions object.</li>
</ul>
<p>You will use the following query in this guide:</p>
<div class="table-section"><table><thead><tr><th>Type</th><th>Operation</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>Query</td>
<td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementGroupAtTip">elementGroupAtTip</a></td>
<td>Retrieves elementGroup at tip.</td>
</tr>
</tbody></table></div>
<section id="step-1-request-for-a-particular-elementgroup">
<a href="#step-1-request-for-a-particular-elementgroup"><h2>Step 1: Request for a particular ElementGroup</h2></a>
<p>The <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementGroupnAtTip">elementGroupnAtTip</a>  query returns a <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elementGroup">ElementGroup</a> object. The ElementGroup object contains an array of <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elements">elements</a> objects. For this exercise, we request the <code class="docutils literal notranslate"><span class="pre">name</span></code> field and the entire history object of the elementGroup.</p>
<ol class="arabic">
<li>In the <a class="reference external" href="https://aecdatamodel-explorer.autodesk.io/">AEC Data Model Explorer</a>, the query is populated by default in the <strong>Query Pane</strong>. You can also edit or update the query as per your requirement and run it.</p>
<blockquote>
<div><p><strong>Query</strong></p>
<blockquote>
<div><div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span><span class="o">(</span><span class="nv">$elementGroupId</span>:<span class="w"> </span>ID!<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>elementGroupAtTip<span class="o">(</span>elementGroupId:<span class="w"> </span><span class="nv">$elementGroupId</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>id
<span class="w">    </span>name
<span class="w">    </span>alternativeIdentifiers<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>fileUrn
<span class="w">      </span>fileVersionUrn
<span class="w">    </span><span class="o">}</span>
<span class="w">    </span>versionHistory<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>versions<span class="w"> </span><span class="o">{</span>
<span class="w">        </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">          </span>versionNumber
<span class="w">          </span>createdOn
<span class="w">        </span><span class="o">}</span>
<span class="w">      </span><span class="o">}</span>
<span class="w">    </span><span class="o">}</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</div></blockquote>
</li>
<li><dl>
<dt>In the Query variables pane, set the value of the <code class="docutils literal notranslate"><span class="pre">elementGroupId</span></code> obtained in <a class="reference external" href="/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements">Navigate to Elementgroups within projects</a></dt><dd><p><strong>Query Variables</strong></p>
<blockquote>
<div><div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="o">{</span>
<span class="w">    </span><span class="s2">"elementGroupId"</span><span class="w"> </span>:<span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB"</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</dd>
</dl>
</li>
<li>Click <strong>Play</strong>.  All the previously published versions of that elementGroup will be displayed in the response. The response should be similar to the following code-block:</p>
<blockquote>
<div><p><strong>Response</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"elementGroupAtTip"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Architectural.rvt"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:rEdJOCOqR0ekyJBBYlR9EA"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.rEdJOCOqR0ekyJBBYlR9EA?version=1"</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="nt">"versionHistory"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"versions"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">              </span><span class="nt">"versionNumber"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w">              </span><span class="nt">"createdOn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2024-06-18T12:59:46.718Z"</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">          </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">      </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</div></blockquote>
</li>
</ol>
<p>After working through the steps mentioned above, you should see a screen similar to the following image:</p>
<blockquote>
<div><img alt="../../../../_images/elementgroupattip.png" src="../../../../_images/elementgroupattip.png">
</div></blockquote>
</section>
</section>


            <div class="clearer"></div>
          </div>