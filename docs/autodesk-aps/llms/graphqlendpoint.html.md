# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/reference/graphqlendpoint.html

<div class="api-documentation"><div class="title-category">GraphQL Endpoint</div>
<meta name="sphinx-version" content="5.0.0">
            
  
<section id="post-aec-graphql">
<div class="display--table"><span class="display--table-cell"><div class="method-badge method-badge--post">POST</div></span><span class="display--table-cell"><h1> aec/graphql</h1></span></div>
<p>Sends GraphQL requests to AEC Data Model GraphQL service and returns responses in the JSON format.</p>
<section id="resource-information">
<a href="#resource-information"><h2>Resource Information</h2></a>
<div class="table-section"><table><thead></thead><tbody><tr><td><span class="name">Method and URI</span></td><td><div class="display--table"><span class="name"><span class="display--table-cell"><div class="method-badge method-badge--post">POST</div></span><span class="display--table-cell"> <a class="reference external" href="https://developer.api.autodesk.com/aec/graphql">https://developer.api.autodesk.com/aec/graphql</a></span></span></div></td></tr><tr><td><span class="name">Authentication Context</span></td><td><div class="display--table"><span class="name">user context required</span></div></td></tr><tr><td><span class="name">Required OAuth Scopes</span></td><td><div class="display--table"><span class="name"><code class="docutils literal notranslate"><span class="pre">data:create</span></code> <code class="docutils literal notranslate"><span class="pre">data:read</span></code> <code class="docutils literal notranslate"><span class="pre">data:write</span></code></span></div></td></tr><tr><td><span class="name">Data Format</span></td><td><div class="display--table"><span class="name">JSON</span></div></td></tr></tbody></table></div>
<section id="request">
<h3>Request</h3>
</section>
</section>
<section id="headers">
<a href="#headers"><h2>Headers</h2></a>
<div class="table-section"><table><thead></thead><tbody><tr><td><span class="name">Authorization</span><span class="required">*</span><div class="type">string</div></td><td>Must be <code class="docutils literal notranslate" style="background: #f2f2f2;"><span class="pre" style="background: none;">Bearer</span> <span class="pre" style="background: none;">&lt;TOKEN&gt;</span></code>, where <code class="docutils literal notranslate" style="background: #f2f2f2;"><span class="pre" style="background: none;">&lt;TOKEN&gt;</span></code> is an access token obtained by a <a class="reference external" href="/en/docs/oauth/v2/tutorials/get-3-legged-token">three-legged</a> OAuth flow.</td></tr><tr><td><span class="name">Content-Type</span><div class="type">string</div></td><td>Must be <code class="docutils literal notranslate" style="background: #f2f2f2;"><span class="pre" style="background: none;">application/json</span></code>.</td></tr><tr><td><span class="name">Region</span><div class="type">string</div></td><td>Must be <code class="docutils literal notranslate" style="background: #f2f2f2;"><span class="pre" style="background: none;">US</span></code>, <code class="docutils literal notranslate" style="background: #f2f2f2;"><span class="pre" style="background: none;">EMEA</span></code> or <code class="docutils literal notranslate" style="background: #f2f2f2;"><span class="pre" style="background: none;">AUS</span></code>. Default value is <code class="docutils literal notranslate" style="background: #f2f2f2;"><span class="pre" style="background: none;">US</span></code>. Determines the region where the request is sent.</td></tr></tbody></table><div class="text-required">* Required</div></div>
<section id="id1">
<h3>Request</h3>
</section>
</section>
<section id="body-structure">
<a href="#body-structure"><h2>Body Structure</h2></a>
<p>Request body to send a GraphQL query.</p>
<div class="table-section"><table><thead></thead><tbody><tr><td><span class="name">query</span><span class="required">*</span><div class="type">object</div></td><td>Contains the GraphQL query or mutation to send to the AEC Data Model service.</td></tr><tr><td><span class="name">variables</span><div class="type">object</div></td><td>Contains a set of key-value pairs, where the keys correspond to the names of the variables defined in your GraphQL query, and the values represent the values of those variables.</td></tr></tbody></table><div class="text-required">* Required</div></div>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
<section id="example-1">
<a href="#example-1"><h2>Example 1</h2></a>
<p>This example demonstrates how to use cURL to send a GraphQL query to the AEC Data Model service.</p>
<section id="id2">
<h3>Request</h3>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>curl<span class="w"> </span>-v<span class="w"> </span><span class="s1">'https://developer.api.autodesk.com/aec/graphql'</span><span class="w"> </span><span class="se">\</span>
-X<span class="w"> </span><span class="s1">'POST'</span><span class="w"> </span><span class="se">\</span>
-H<span class="w"> </span><span class="s1">'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a...'</span><span class="w"> </span><span class="se">\</span>
-H<span class="w"> </span><span class="s1">'Content-Type: application/json'</span><span class="w"> </span><span class="se">\</span>
-d<span class="w"> </span><span class="s1">'{</span>
<span class="s1">      "query":"query GetProjects($hubId: String!) {</span>
<span class="s1">         projects(hubId: $hubId) {</span>
<span class="s1">          results {</span>
<span class="s1">            id</span>
<span class="s1">            name</span>
<span class="s1">          }</span>
<span class="s1">        }",</span>
<span class="s1">        "variables":{</span>
<span class="s1">          "hubId":"a.YnVzaW5lc3M6YXV0b2Rlc2syMDA2"</span>
<span class="s1">       }</span>
<span class="s1">    }'</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
<section id="response">
<h3>Response</h3>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">   </span><span class="nt">"data"</span><span class="p">:{</span>
<span class="w">      </span><span class="nt">"projects"</span><span class="p">:{</span>
<span class="w">         </span><span class="nt">"results"</span><span class="p">:[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">               </span><span class="nt">"id"</span><span class="p">:</span><span class="s2">"a.YnVzaW5lc3M6YXV0b2Rlc2syMDM5I0QyMDIyMDEzMTUwMzg3NDE5"</span><span class="p">,</span>
<span class="w">               </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"Default Project"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">               </span><span class="nt">"id"</span><span class="p">:</span><span class="s2">"a.YnVzaW5lc3M6YXV0b2Rlc2syMDM5I0QyMDIyMDEzMTUwMzg3NDQ0"</span><span class="p">,</span>
<span class="w">               </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"Admin Project"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">               </span><span class="nt">"id"</span><span class="p">:</span><span class="s2">"a.YnVzaW5lc3M6YXV0b2Rlc2syMDM5I0QyMDIyMDEzMTUwMzg3NDY5"</span><span class="p">,</span>
<span class="w">               </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"Assets"</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">         </span><span class="p">]</span>
<span class="w">      </span><span class="p">}</span>
<span class="w">   </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
</section>
<section id="example-2">
<a href="#example-2"><h2>Example 2</h2></a>
<p>This example demonstrates how to use Axios in JavaScript to send a GraphQL query to the AEC Data Model service.</p>
<section id="id3">
<h3>Request</h3>
<div class="highlight-javascript notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="nx">axios</span><span class="p">({</span>
<span class="w">  </span><span class="nx">method</span><span class="o">:</span><span class="w"> </span><span class="s1">'POST'</span><span class="p">,</span>
<span class="w">  </span><span class="nx">url</span><span class="o">:</span><span class="w"> </span><span class="s1">'https://developer.api.autodesk.com/aec/graphql'</span><span class="p">,</span>
<span class="w">  </span><span class="nx">data</span><span class="o">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nx">query</span><span class="o">:</span><span class="w"> </span><span class="sb">`{</span>
<span class="sb">      hubs {</span>
<span class="sb">        results {</span>
<span class="sb">          name</span>
<span class="sb">        }</span>
<span class="sb">      }</span>
<span class="sb">    }`</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">})</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Note:</strong> Axios automatically sets the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header to <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p>
</section>
<section id="id4">
<h3>Response</h3>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"data"</span><span class="p">:{</span>
<span class="w">    </span><span class="nt">"hubs"</span><span class="p">:{</span>
<span class="w">       </span><span class="nt">"results"</span><span class="p">:[</span>
<span class="w">          </span><span class="p">{</span>
<span class="w">             </span><span class="nt">"id"</span><span class="p">:</span><span class="s2">"a.YnVzaW5lc3M6YXV0b2Rlc2s2MTA0"</span><span class="p">,</span>
<span class="w">             </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"L2-Forge-Data-Team"</span>
<span class="w">          </span><span class="p">},</span>
<span class="w">          </span><span class="p">{</span>
<span class="w">             </span><span class="nt">"id"</span><span class="p">:</span><span class="s2">"a.YnVzaW5lc3M6YXV0b2Rlc2s0NTA5"</span><span class="p">,</span>
<span class="w">             </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"Michelangeloâs Playground"</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">       </span><span class="p">]</span>
<span class="w">    </span><span class="p">}</span>
<span class="w"> </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
</section>
<section id="example-3">
<a href="#example-3"><h2>Example 3</h2></a>
<p>This example demonstrates how to use send and receive http request and response in C# to the AEC Data Model service.</p>
<section id="id5">
<h3>Request</h3>
<div class="highlight-c# notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="k">static</span><span class="w"> </span><span class="k">async</span><span class="w"> </span><span class="n">Task</span><span class="w"> </span><span class="nf">getHubs</span><span class="p">(){</span>
<span class="kt">var</span><span class="w"> </span><span class="n">clientHandler</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">HttpClientHandler</span><span class="p">();</span>
<span class="kt">var</span><span class="w"> </span><span class="n">client</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">HttpClient</span><span class="p">(</span><span class="n">clientHandler</span><span class="p">);</span>
<span class="kt">var</span><span class="w"> </span><span class="n">request</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">HttpRequestMessage</span>
<span class="p">{</span>
<span class="w">   </span><span class="n">Method</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">HttpMethod</span><span class="p">.</span><span class="n">Post</span><span class="p">,</span>
<span class="w">   </span><span class="n">RequestUri</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">Uri</span><span class="p">(</span><span class="s">"https://developer.api.autodesk.com/aec/graphql"</span><span class="p">),</span>
<span class="w">   </span><span class="n">Headers</span><span class="w"> </span><span class="o">=</span>
<span class="w">   </span><span class="p">{</span>
<span class="w">      </span><span class="p">{</span><span class="w"> </span><span class="s">"Authorization"</span><span class="p">,</span><span class="w"> </span><span class="s">"Bearer &lt;&lt;YOUR TOKEN HERE&gt;&gt;"</span><span class="w"> </span><span class="p">}</span>
<span class="w">   </span><span class="p">},</span>
<span class="w">   </span><span class="n">Content</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">StringContent</span><span class="p">(</span><span class="s">@"{""query"":""query GetHubs {hubs {pagination{cursor}results{name id}}}"",""variables"":{}}"</span><span class="p">)</span>
<span class="w">   </span><span class="p">{</span>
<span class="w">      </span><span class="n">Headers</span><span class="w"> </span><span class="o">=</span>
<span class="w">      </span><span class="p">{</span>
<span class="w">      </span><span class="n">ContentType</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">new</span><span class="w"> </span><span class="n">System</span><span class="p">.</span><span class="n">Net</span><span class="p">.</span><span class="n">Http</span><span class="p">.</span><span class="n">Headers</span><span class="p">.</span><span class="n">MediaTypeHeaderValue</span><span class="p">(</span><span class="s">"application/json"</span><span class="p">)</span>
<span class="w">      </span><span class="p">}</span>
<span class="w">   </span><span class="p">}</span>
<span class="p">};</span>
<span class="k">using</span><span class="w"> </span><span class="p">(</span><span class="kt">var</span><span class="w"> </span><span class="n">response</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">await</span><span class="w"> </span><span class="n">client</span><span class="p">.</span><span class="n">SendAsync</span><span class="p">(</span><span class="n">request</span><span class="p">))</span>
<span class="p">{</span>
<span class="w">   </span><span class="n">response</span><span class="p">.</span><span class="n">EnsureSuccessStatusCode</span><span class="p">();</span>
<span class="w">   </span><span class="kt">var</span><span class="w"> </span><span class="n">body</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="k">await</span><span class="w"> </span><span class="n">response</span><span class="p">.</span><span class="n">Content</span><span class="p">.</span><span class="n">ReadAsStringAsync</span><span class="p">();</span>
<span class="w">   </span><span class="n">Console</span><span class="p">.</span><span class="n">WriteLine</span><span class="p">(</span><span class="n">body</span><span class="p">);</span>
<span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
<section id="id6">
<h3>Response</h3>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">   </span><span class="nt">"data"</span><span class="p">:{</span>
<span class="w">      </span><span class="nt">"hubs"</span><span class="p">:{</span>
<span class="w">         </span><span class="nt">"pagination"</span><span class="p">:{</span>
<span class="w">            </span><span class="nt">"cursor"</span><span class="p">:</span><span class="kc">null</span>
<span class="w">         </span><span class="p">},</span>
<span class="w">         </span><span class="nt">"results"</span><span class="p">:[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">               </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"JM Test"</span><span class="p">,</span>
<span class="w">               </span><span class="nt">"id"</span><span class="p">:</span><span class="s2">"a.YnVzaW5lc3M6YXV0b2Rlc2s1ODcy"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">               </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"AEC Data Model Account"</span><span class="p">,</span>
<span class="w">               </span><span class="nt">"id"</span><span class="p">:</span><span class="s2">"b.03f98b13-ec95-461b-b945-765f496165c1"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">               </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"Developer Advocacy Support"</span><span class="p">,</span>
<span class="w">               </span><span class="nt">"id"</span><span class="p">:</span><span class="s2">"b.489c5e7a-c6c0-4212-81f3-3529a621210b"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">               </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"Construction Records Testing"</span><span class="p">,</span>
<span class="w">               </span><span class="nt">"id"</span><span class="p">:</span><span class="s2">"b.768cae14-76b3-4531-9030-25212dab4e48"</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">         </span><span class="p">]</span>
<span class="w">      </span><span class="p">}</span>
<span class="w">   </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
</section>
</section>


            <div class="clearer"></div>
          </div>