# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/developers_guide/aec-ratelimit.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="aec-data-model-rate-limits">
<h1>AEC Data Model Rate Limits</h1>
<p>In order to maintain stability and ensure accessibility of our API to all users, weâve implemented certain protection measures on incoming requests to our GraphQL API via rate limits.</p>
<section id="rate-limits">
<a href="#rate-limits"><h2>Rate limits</h2></a>
<p>Calls to the GraphQL API are subjected to rate limiting based on the computed point value of the data thatâs requested within a minute. Each request is given a dynamic point value, which is determined by the complexity of the provided query. For instance, requests that involve complex tasks like aggregations or retrieving a large amount of data will carry a higher point value. Therefore, itâs essential to request only the data that youâll actually use. Thereâs also a cap on the total number of points an application or an individual request can consume within a minute.</p>
<p><strong>Important:</strong></p>
<blockquote>
<div><ul class="simple">
<li>An application request will have a default rate limit of 6000 points per minute. To request a higher rate limit, please contact support.</li>
<li>An individual request has a limit of 1000 points per query. Any queries exceeding this limit will be rejected.</li>
</ul>
</div></blockquote>
</section>
<section id="how-to-calculate-the-point-value-of-a-query">
<a href="#how-to-calculate-the-point-value-of-a-query"><h2>How to calculate the point value of a query?</h2></a>
<p>The point associated with a query is calculated by adding up the points of each field within the query. This calculation is dependent on the type of the field returned. The following points are the default values allocated to each type. However, itâs important to note that the point values for specific individual fields may vary, being either higher or lower.</p>
<p><strong>Default values</strong></p>
<p>The below are the default point values. Specific individual fields can be more or less expensive.</p>
<div class="table-section"><table><thead><tr><th>Field Returns</th><th>Point Value</th></tr></thead><tbody>
<tr class="row-even"><td>Query</td>
<td>10</td>
</tr>
<tr class="row-odd"><td>Object</td>
<td>1</td>
</tr>
<tr class="row-even"><td>Scalar</td>
<td>0</td>
</tr>
<tr class="row-odd"><td>Enum</td>
<td>0</td>
</tr>
<tr class="row-even"><td>Interface</td>
<td>Maximum point value of all implementations</td>
</tr>
<tr class="row-odd"><td>Union</td>
<td>Maximum point value of all implementations</td>
</tr>
<tr class="row-even"><td>Results</td>
<td>Sized according to the returned pagesize</td>
</tr>
<tr class="row-odd"><td>Mutation</td>
<td>10</td>
</tr>
</tbody></table></div>
</section>
<section id="exceeding-the-rate-limit">
<a href="#exceeding-the-rate-limit"><h2>Exceeding the rate limit</h2></a>
<p>When you exceed your rate limit the API will not be return data and instead will return a rate limit Exceeded error. This error will be returned in a 429 HTTPS Response with the following content:</p>
<p>Exceeding the rate limit example:</p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[{</span>
<span class="w">    </span><span class="nt">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Query point value per minute quota exceeded with point value 231 and remaining quota 69. Please try again later."</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"extensions"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"code"</span><span class="p">:</span><span class="s2">"GRAPHQL_VALIDATION_FAILED"</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}]</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
<section id="exceeding-the-maximum-allowed-query-point">
<a href="#exceeding-the-maximum-allowed-query-point"><h2>Exceeding the maximum allowed query point</h2></a>
<p>When you exceed the maximum allowed query point value the API will not return data and instead will return a error. This error will be returned in a 400 HTTPS Response with the following content:</p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"errors"</span><span class="p">:</span><span class="w"> </span><span class="p">[{</span>
<span class="w">    </span><span class="nt">"message"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Query point value 1231 exceeds maximum allowed query point value 1000. To reduce point value, consider setting a lower pagination limit or reducing the number of fields requested."</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"extensions"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"code"</span><span class="p">:</span><span class="s2">"GRAPHQL_VALIDATION_FAILED"</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}]</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
<section id="knowing-the-point-value-of-a-query">
<a href="#knowing-the-point-value-of-a-query"><h2>Knowing the point value of a query</h2></a>
<p>The point value of a query is populated in the extensions field of a response as noted in the example below:</p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>{
  {
      "data": {
          ...
      },
      "extensions": {
          "pointValue": {
              "requestedQueryPointValue": 16
          }
      }
  }
}
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
</section>


            <div class="clearer"></div>
          </div>