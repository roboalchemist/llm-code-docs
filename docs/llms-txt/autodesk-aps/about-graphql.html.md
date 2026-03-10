# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/developers_guide/about-graphql.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="about-graphql">
<h1>About GraphQL</h1>
<p>GraphQL is an open-source query language for APIs that was developed by Facebook as an alternative to REST API. It was released to the public in 2015 and hosted by the Linux Foundation atâ¯<a class="reference external" href="https://graphql.org/">GraphQL.org</a>.</p>
<p>Using GraphQL, you can query, create, update, and delete data withâ¯mutations. Queries and mutations follow the same syntax. The following examples taken fromâ¯<a class="reference external" href="https://graphql.org/">GraphQL.org</a>.orgâ¯show how queries and mutations are sent to a GraphQL server that hosts information about Star Wars.</p>
<section id="examples">
<a href="#examples"><h2>Examples</h2></a>
<section id="example-1-query">
<h3>Example 1 - Query</h3>
<p><strong>Query</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span>HeroNameAndFriends<span class="w"> </span><span class="o">{</span>
<span class="w">  </span>hero<span class="w"> </span><span class="o">{</span>
<span class="w">    </span>name
<span class="w">    </span>friends<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>name
<span class="w">    </span><span class="o">}</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Result</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:{</span>
<span class="w">    </span><span class="nt">"hero"</span><span class="p">:{</span>
<span class="w">      </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"R2-D2"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"friends"</span><span class="p">:[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"Luke Skywalker"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"Han Solo"</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="s2">"Leia Organa"</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">      </span><span class="p">]</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</section>
<section id="example-2-mutation">
<h3>Example 2 - Mutation</h3>
<p><strong>Mutation</strong></p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>mutation<span class="w"> </span>CreateReviewForEpisode<span class="o">(</span><span class="nv">$ep</span>:<span class="w"> </span>Episode!,<span class="w"> </span><span class="nv">$review</span>:<span class="w"> </span>ReviewInput!<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>createReview<span class="o">(</span>episode:<span class="w"> </span><span class="nv">$ep</span>,<span class="w"> </span>review:<span class="w"> </span><span class="nv">$review</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>stars
<span class="w">    </span>commentary
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>

Variables:
<span class="o">{</span>
<span class="w">  </span><span class="s2">"ep"</span>:<span class="s2">"JEDI"</span>,
<span class="w">  </span><span class="s2">"review"</span>:<span class="o">{</span>
<span class="w">    </span><span class="s2">"stars"</span>:5,
<span class="w">    </span><span class="s2">"commentary"</span>:<span class="s2">"This is a great movie!"</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p><strong>Result</strong></p>
<div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:{</span>
<span class="w">    </span><span class="nt">"createReview"</span><span class="p">:{</span>
<span class="w">      </span><span class="nt">"stars"</span><span class="p">:</span><span class="mi">5</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"commentary"</span><span class="p">:</span><span class="s2">"This is a great movie!"</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
<p>See this <a class="reference external" href="https://graphql.org/learn/queries/">Tutorial on GraphQL Queries and mutations</a> for more information on Queries and mutations.</p>
<p>When the schema of the data is known, you can query for and change the information in the exact shape the data is organized and fetch only the data you need. In contrast, REST APIs respond with a predefined payload, regardless of whether you need all the information or not.</p>
<p>For more information on GraphQL, see:</p>
<ul class="simple">
<li><a class="reference external" href="https://www.howtographql.com/basics/0-introduction/">How to GraphQL</a></li>
<li><a class="reference external" href="https://graphql.org/learn/">Introduction to GraphQL</a></li>
</ul>
<p>The AEC Data Model API provides a unified interface by federating multiple services. For example, to work with Hubs, Projects, and Folders, you must use the APS Data Management REST API. AEC Data Model API, based on GraphQL service handles the interaction with Forge Data Management to provide you with a unified API experience.</p>
<div class="line-block">
<div class="line"><br></div>
</div>
</section>
</section>
</section>


            <div class="clearer"></div>
          </div>