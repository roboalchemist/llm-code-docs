# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/developers_guide/usage.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="using-the-aec-data-model-api">
<h1>Using the AEC Data Model API</h1>
<p>To access the AEC Data Model API, follow these steps:</p>
<ul class="simple">
<li>If you are using this API for the first time, follow these steps:</p>
<ol class="arabic simple">
<li>Activate AEC Data Model API capabilities through the ACC Account Adiministrator. For more details, see <a class="reference external" href="/en/docs/aecdatamodel/v1/developers_guide/onboarding">API Onboarding</a>.</li>
<li><a class="reference external" href="/en/docs/oauth/v2/tutorials/create-app/">Create an App</a>.</li>
<li>Select the <strong>AEC Data Model API</strong> and <strong>Data Management API</strong> services to use the AEC Data Model API.</li>
<li>Note down the Client ID and Client secret so that you have the Client ID and Client secret readily available for future reference.</li>
</ol>
</li>
</ul>
<div class="line-block">
<div class="line"><br></div>
</div>
<ul class="simple">
<li>To add AEC Data Model service to an existing APS account, select the AEC Data Model API, Data Management API, and Model Derivative API services to use the AEC Data Model API. For more information refer to <a class="reference external" href="https://tutorials.autodesk.io/">Add Forge Services to Existing App</a>.</li>
</ul>
<section id="endpoint">
<a href="#endpoint"><h2>Endpoint</h2></a>
<p>All the GraphQL queries must be sent to <code class="docutils literal notranslate"><span class="pre">https://developer.api.autodesk.com/aec/graphql</span></code>.</p>
</section>
<section id="obtain-a-3-legged-access-token-to-authenticate-queries">
<a href="#obtain-a-3-legged-access-token-to-authenticate-queries"><h2>Obtain a 3-Legged access token to authenticate queries</h2></a>
<p>All AEC Data Model API queries require a 3-legged access token. See <a class="reference external" href="https://aps.autodesk.com/en/docs/oauth/v2/tutorials/get-3-legged-token/">Get a 3-Legged Token with Authorization Code Grant</a> for instructions on how to obtain a 3-legged access token. Make sure that you specify the following scopes:</p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span>data:read<span class="w"> </span>data:create<span class="w"> </span>data:write
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
<section id="executing-graphql-queries">
<a href="#executing-graphql-queries"><h2>Executing GraphQL queries</h2></a>
<p>You can execute GraphQL queries by sending a POST request to <code class="docutils literal notranslate"><span class="pre">https://developer.api.autodesk.com/aec/graphql</span></code>. Each request must have an <code class="docutils literal notranslate"><span class="pre">Authorization</span></code> header, which must be <code class="docutils literal notranslate"><span class="pre">Bearer</span> <span class="pre">&lt;YOUR_ACCESS_TOKEN&gt;</span></code>. For example;</p>
<section id="request">
<h3>Request</h3>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>curl<span class="w"> </span>-v<span class="w"> </span><span class="s1">'https://developer.api.autodesk.com/aec/graphql'</span><span class="w"> </span><span class="se">\</span>
-X<span class="w"> </span><span class="s1">'POST'</span><span class="w"> </span><span class="se">\</span>
-H<span class="w"> </span><span class="s1">'Authorization: Bearer AuIPTf4KYLTYGVnOHQ0cuolwCW2a'</span><span class="w"> </span><span class="se">\</span>
-H<span class="w"> </span><span class="s1">'Content-Type: application/graphql'</span><span class="w"> </span><span class="se">\</span>
-d<span class="w"> </span><span class="s1">'{</span>
<span class="s1">      hubs {</span>
<span class="s1">        results {</span>
<span class="s1">          name</span>
<span class="s1">        }</span>
<span class="s1">      }</span>
<span class="s1">    }'</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
<section id="response">
<h3>Response</h3>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"hubs"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"results"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"Autodesk-Forge"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"ME-FLC"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"ACC-Cloud-Team"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"PIM-ME-Release"</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">      </span><span class="p">]</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<div class="line-block">
<div class="line"><br></div>
</div>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
</section>
<section id="specifying-the-content-type-header">
<a href="#specifying-the-content-type-header"><h2>Specifying the Content Type Header</h2></a>
<p>The <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header plays a vital role in indicating the request format. When working with the GraphQL API endpoint, the value for the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header depends on the data format used (as in the cURl code sample as described previously). If the data is sent in GraphQL format, the Content-Type should be set as application/graphql. However, some clients like Axios format the GraphQL query as a JSON object instead as shown in the following code block.</p>
<div class="highlight-javascript notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="nx">axios</span><span class="p">({</span>
<span class="w">  </span><span class="nx">method</span><span class="o">:</span><span class="w"> </span><span class="s1">'POST'</span><span class="p">,</span>
<span class="w">  </span><span class="nx">url</span><span class="o">:</span><span class="w"> </span><span class="s1">'&lt;GraphQL endpoint&gt;'</span><span class="p">,</span>
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
<p>Axios automatically sets the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header value to <code class="docutils literal notranslate"><span class="pre">application/json</span></code>.</p>
</section>
</section>


            <div class="clearer"></div>
          </div>