# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/tutorials/tutorial-01/nav-elements.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="navigate-to-elementgroups-within-a-project">
<h1>Navigate to ElementGroups within a Project</h1>
<p>In this guide, you will learn how to retrieve a list of ElementGroups within a specific project. ElementGroups are collections of elements that can be used to organize and manage data in Autodesk AEC applications.</p>
<p>By the end of this guide, you will be able to:</p>
<ul class="simple">
<li>Fetch elementGroup files available in a project.</li>
<li>Understand the options and fields in the documentation on the <code class="docutils literal notranslate"><span class="pre">elementGroupsByProject</span></code> query, the results, and versions.</li>
</ul>
<p>You will use the following query in this guide:</p>
<div class="table-section"><table><thead><tr><th>Type</th><th>Operation</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>Query</td>
<td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementGroupsByProject">elementGroupsByProject</a></td>
<td>Retrieves all elementGroups within a specific project.</td>
</tr>
</tbody></table></div>
<section id="step-1-request-for-a-list-of-elementgroups-within-a-project">
<a href="#step-1-request-for-a-list-of-elementgroups-within-a-project"><h2>Step 1: Request for a list of ElementGroups within a Project</h2></a>
<p>The <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementgroupsbyproject">elementGroupsByProject</a>  query returns   <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elementgroups">ElementGroups</a> object. The <code class="docutils literal notranslate"><span class="pre">ElementGroups</span></code> object contains a list of ElementGroups.</p>
<blockquote>
<div><ol class="arabic">
<li>In <a class="reference external" href="https://aecdatamodel-explorer.autodesk.io/">AEC Data Model Explorer</a>, the query is populated by default in the <strong>Query Pane</strong>. You can also edit or update the query as per your requirement and run it.</p>
<blockquote>
<div><p><strong>Query</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span>GetElementGroupsByProject<span class="o">(</span><span class="nv">$projectId</span>:<span class="w"> </span>ID!<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>elementGroupsByProject<span class="o">(</span>projectId:<span class="w"> </span><span class="nv">$projectId</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">      </span>pagination<span class="w"> </span><span class="o">{</span>
<span class="w">        </span>cursor
<span class="w">      </span><span class="o">}</span>
<span class="w">      </span>results<span class="o">{</span>
<span class="w">        </span>name
<span class="w">        </span>id
<span class="w">        </span>alternativeIdentifiers<span class="o">{</span>
<span class="w">          </span>fileUrn
<span class="w">          </span>fileVersionUrn
<span class="w">        </span><span class="o">}</span>
<span class="w">      </span><span class="o">}</span>
<span class="w">    </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li>In the Query Variables Pane, enter the value of the <code class="docutils literal notranslate"><span class="pre">projectId</span></code> obtained from <a class="reference external" href="/en/docs/aecdatamodel/v1/tutorials/tutorial-01/getprojects">Get Projects</a> topic.</p>
<blockquote>
<div><p><strong>Query Variables</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="o">{</span>
<span class="w">  </span><span class="s2">"projectId"</span>:<span class="w"> </span><span class="s2">"urn:adsk.workspace:prod.project:39208068-e548-4d9e-b8a7-e000fdf2a9b4"</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li>Click <strong>Play</strong>. The list of elementGroups available within that project is displayed in the response. Note down the ElementGroup IDs of one of the Revit models (this case .rvt file you want to work with). You will need these IDs for the remaining guides. For this tutorial, we will use the ID of the item named âSnowdon Towers Sample Architectural.rvtâ.</p>
<blockquote>
<div><p>The response should be similar to the following code-block:</p>
<p><strong>Response</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"elementGroupsByProject"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample HVAC.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35uUVpyS1BEUVJVS0VFOWtmWWNHV0VB"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:nQZrKPDQRUKEE9kfYcGWEA"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.nQZrKPDQRUKEE9kfYcGWEA?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Electrical.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35fR1IzdHpORlI3LV9tclFBOGR4TWN3"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:_GR3tzNFR7-_mrQA8dxMcw"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf._GR3tzNFR7-_mrQA8dxMcw?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Architectural.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:rEdJOCOqR0ekyJBBYlR9EA"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.rEdJOCOqR0ekyJBBYlR9EA?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Site.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRR"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:LvosTJ57RXefNY1bachQTQ"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.LvosTJ57RXefNY1bachQTQ?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Facades.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1n"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:fWDufB-ySmq5Fwn6Fj1_-g"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.fWDufB-ySmq5Fwn6Fj1_-g?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Structural.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ350OU0xX0J3VVRObVllbXRoUVBYNHh3"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:t9M1_BwUTNmYemthQPX4xw"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.t9M1_BwUTNmYemthQPX4xw?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Snowdon Towers Sample Plumbing.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35CR2QwdEpOc1NHNlZWSFFibkZ6cFFR"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:BGd0tJNsSG6VVHQbnFzpQQ"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.BGd0tJNsSG6VVHQbnFzpQQ?version=1"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"areatest.rvt"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ340VFVtRnF0WFJVVy1CS09Gb1cyd3FR"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"fileUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:dm.lineage:4TUmFqtXRUW-BKOFoW2wqQ"</span><span class="p">,</span>
<span class="w">            </span><span class="nt">"fileVersionUrn"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.wipprod:fs.file:vf.4TUmFqtXRUW-BKOFoW2wqQ?version=3"</span>
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
<p>After working through the steps mentioned above, you should see a screen similar to the following image:</p>
<blockquote>
<div><img alt="../../../../_images/elementgroupsfromproject.png" src="../../../../_images/elementgroupsfromproject.png">
</div></blockquote>
</section>
<section id="step-2-to-preview-the-model">
<a href="#step-2-to-preview-the-model"><h2>Step 2: To preview the model</h2></a>
<blockquote>
<div><ol class="arabic simple">
<li>Enter the <cite>fileVersionUrn</cite> of the model. For example, refer to the ID <cite>urn:adsk.wipprod:fs.file:vf.rEdJOCOqR0ekyJBBYlR9EA?version=1</cite> as mentioned in the Revit model <cite>Snowdon Towers Sample Architectural.rvt</cite>.</li>
<li>Click <strong>Viewer</strong> to preview the model.</li>
</ol>
<blockquote>
<div><dl>
<dt>After working through the steps mentioned above, you should see a screen similar to the following image:</dt><dd><img alt="../../../../_images/viewerpreview.png" src="../../../../_images/viewerpreview.png">
</dd>
</dl>
</div></blockquote>
</div></blockquote>
</section>
</section>


            <div class="clearer"></div>
          </div>