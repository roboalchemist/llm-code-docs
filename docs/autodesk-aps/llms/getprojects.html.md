# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/tutorials/tutorial-01/getprojects.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="get-projects">
<h1>Get Projects</h1>
<p>In this guide, you will learn how to retrieve a list of all projects available within the hubs you have access to.</p>
<p>By the end of this guide, you will be able to:</p>
<ul class="simple">
<li>Fetch project information like project ID and name of the project.</li>
<li>Understand the options and fields in the documentation on the <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/projects">projects</a>  query, <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/projects">Projects</a> object, and <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/project">Project</a> object.</li>
</ul>
<p>You will use the following query in this guide:</p>
<div class="table-section"><table><thead><tr><th>Type</th><th>Operation</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>Query</td>
<td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/projects">projects</a></td>
<td>Retrieves all projects within a specified hub.</td>
</tr>
</tbody></table></div>
<section id="step-1-request-for-a-list-of-projects-within-a-hub">
<a href="#step-1-request-for-a-list-of-projects-within-a-hub"><h2>Step 1: Request for a list of Projects within a Hub</h2></a>
<p>The <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/projects">projects</a>  query returns a <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/projects">Projects</a> object. The Projects object contains an array of <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/project">Project</a> objects. In this exercise, we query for the <code class="docutils literal notranslate"><span class="pre">project</span> <span class="pre">id</span></code> and <code class="docutils literal notranslate"><span class="pre">project</span> <span class="pre">name</span></code> fields.</p>
<blockquote>
<div><ol class="arabic">
<li>In the <a class="reference external" href="https://aecdatamodel-explorer.autodesk.io/">AEC Data Model Explorer</a>, the query is populated by default in the <strong>Query Pane</strong>. You can also edit or update the query as per your requirement and run it.</p>
<blockquote>
<div><p><strong>Query</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span>GetProjects<span class="o">(</span><span class="nv">$hubId</span>:<span class="w"> </span>ID!<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>projects<span class="o">(</span>hubId:<span class="w"> </span><span class="nv">$hubId</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">      </span>pagination<span class="w"> </span><span class="o">{</span>
<span class="w">        </span>cursor
<span class="w">      </span><span class="o">}</span>
<span class="w">      </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">        </span>id
<span class="w">        </span>name
<span class="w">        </span>alternativeIdentifiers<span class="o">{</span>
<span class="w">          </span>dataManagementAPIProjectId
<span class="w">        </span><span class="o">}</span>
<span class="w">      </span><span class="o">}</span>
<span class="w">    </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li>In the Query Variables Pane, enter the value of the <code class="docutils literal notranslate"><span class="pre">hubId</span></code> obtained from <a class="reference external" href="/en/docs/aecdatamodel/v1/tutorials/tutorial-01/gethubs">Get Hubs</a> topic.</p>
<blockquote>
<div><p><strong>Query Variables</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="o">{</span>
<span class="w">  </span><span class="s2">"hubId"</span>:<span class="w"> </span><span class="s2">"urn:adsk.ace:prod.scope:dccde3e3-c20c-40d3-a27c-7ac53b051b6e"</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li>Click <strong>Play</strong>. The list of projects available within that hub is displayed in the response. Note down the ExternalIDs and Project IDs of one of the projects. You will need these IDs for the remaining tasks. In this tutorial, we will use the ID of the project named âAEC DM Bootcamp Projectâ. The response should be similar to the following code-block:</p>
<blockquote>
<div><p><strong>Response</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"projects"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"urn:adsk.workspace:prod.project:39208068-e548-4d9e-b8a7-e000fdf2a9b4"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"AEC DM Bootcamp Project"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"dataManagementAPIProjectId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"b.ddcecd34-68b7-41af-ad65-2ce571186c6c"</span>
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
<div><img alt="../../../../_images/getprojects.png" src="../../../../_images/getprojects.png">
</div></blockquote>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
</section>


            <div class="clearer"></div>
          </div>