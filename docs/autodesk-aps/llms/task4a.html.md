# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/tutorials/tutorial-02/task4a.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="get-element-instances-in-a-category-by-version">
<h1>Get Element Instances in a Category by Version</h1>
<p>In this guide, you will learn how to retrieve all instances of a particular category from an elementGroup at a specific version. Also, you can request only those instances that match your filter criteria.</p>
<p>Letâs try to retrieve all instances of the category <code class="docutils literal notranslate"><span class="pre">Walls</span></code> from the second version of the model <strong>Snowdon Towers Sample Architecture.rvt</strong>.</p>
<p>By the end of this guide, you will be able to:</p>
<ul class="simple">
<li>Fetch Instance Elements of a category <code class="docutils literal notranslate"><span class="pre">Walls</span></code> from a specific version of the elementGroup and define the property filter with <code class="docutils literal notranslate"><span class="pre">versionNumber</span></code>.</li>
<li>Use advanced operators like <code class="docutils literal notranslate"><span class="pre">greater</span> <span class="pre">than</span></code>, <code class="docutils literal notranslate"><span class="pre">less</span> <span class="pre">than</span></code>, <code class="docutils literal notranslate"><span class="pre">and</span></code>, and  <code class="docutils literal notranslate"><span class="pre">or</span></code>.</li>
</ul>
<p>You will use the following queries in this guide:</p>
<div class="table-section"><table><thead><tr><th>Type</th><th>Operation</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>Query</td>
<td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementsbyelementgroup">ElementsByElementGroup</a></td>
<td>Retrieves elementGroups in the given project, using additional RSQL filters if provided.</td>
</tr>
</tbody></table></div>
<section id="step-1-request-elements-matching-the-specified-classification-filter">
<a href="#step-1-request-elements-matching-the-specified-classification-filter"><h2>Step 1: Request elements matching the specified classification filter</h2></a>
<p>The <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementsbyelementgroup">ElementsByElementGroup</a> query returns <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elements">Elements</a> object, which contains an array of Elements objects.</p>
<dl class="docutils">
<dt>For this exercise, we request all elements instances that contain:</dt><dd><ul class="simple">
<li>Elements id, name field, and properties.</li>
<li>Name and value fields in the properties object.</li>
</ul>
</dd>
</dl>
<ol class="arabic">
<li>In <a class="reference external" href="https://aecdatamodel-explorer.autodesk.io/">AEC Data Model Explorer</a>, the query is populated by default in the <strong>Query Pane</strong>. You can also edit or update the query as per your requirement and run it.</p>
<blockquote>
<div><p><strong>Query</strong></p>
<blockquote>
<div><div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span>GetWallsElementsByElementGroupIdAtVersion<span class="o">(</span><span class="nv">$elementGroupId</span>:<span class="w"> </span>ID!,<span class="w"> </span><span class="nv">$versionNumber</span>:<span class="w"> </span>Int!,<span class="w"> </span><span class="nv">$propertyFilter</span>:<span class="w"> </span>String!<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">  </span>elementsByElementGroupAtVersion<span class="o">(</span>elementGroupId:<span class="w"> </span><span class="nv">$elementGroupId</span>,<span class="w"> </span>versionNumber:<span class="w"> </span><span class="nv">$versionNumber</span>,<span class="w"> </span>filter:<span class="w"> </span><span class="o">{</span><span class="w"> </span>query:<span class="w"> </span><span class="nv">$propertyFilter</span><span class="o">}</span>,<span class="w"> </span>pagination<span class="w"> </span>:<span class="w"> </span><span class="o">{</span><span class="w"> </span>limit<span class="w"> </span>:<span class="w"> </span><span class="m">5</span><span class="w"> </span><span class="o">})</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>pagination<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>cursor
<span class="w">    </span><span class="o">}</span>
<span class="w">    </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">      </span>id
<span class="w">      </span>name
<span class="w">      </span>properties<span class="w"> </span><span class="o">{</span>
<span class="w">        </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">          </span>name
<span class="w">          </span>value
<span class="w">          </span>displayValue
<span class="w">        </span><span class="o">}</span>
<span class="w">      </span><span class="o">}</span>
<span class="w">    </span><span class="o">}</span>
<span class="w">  </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
<p><strong>Query Variables</strong></p>
<blockquote>
<div><ul>
<li>In the Query Variables Pane, replace the value of the <code class="docutils literal notranslate"><span class="pre">elementGroupId</span></code> variable with the elementGroup ID that you used in <a class="reference external" href="/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements">Navigate to Elementgroups</a>.</li>
<li>In the Query Variables Pane, replace the value of the <code class="docutils literal notranslate"><span class="pre">property</span> <span class="pre">filter</span></code> with the property filter of your choice. For ease of understanding, here we have added the filter based on property name and category as <code class="docutils literal notranslate"><span class="pre">Walls</span></code>.</p>
<p><strong>Note</strong>: To know the list of supported metadata filtering options, refer <a class="reference external" href="/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering">Advanced Filtering Capabilities</a>  page.</p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="o">{</span>
<span class="w">    </span><span class="s2">"elementGroupId"</span><span class="w"> </span>:<span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB"</span>,
<span class="w">    </span><span class="s2">"versionNumber"</span>:<span class="w"> </span><span class="m">1</span>,
<span class="w">    </span><span class="s2">"propertyFilter"</span>:<span class="w"> </span><span class="s2">"property.name.category==Walls and 'property.name.Element Context'==Instance"</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</li>
</ul>
</div></blockquote>
</div></blockquote>
</li>
<li>Click <strong>Play</strong>. The list of elements available within that elementGroup of property âfamilyâ and category ââWallsâ is displayed in the response. The response should be similar to the following code-block:</p>
<blockquote>
<div><p><strong>Response</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"elementsByElementGroupAtVersion"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Y3Vyc341fjU"</span>
<span class="w">      </span><span class="p">},</span>
<span class="w">      </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTc5NQ"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"_Not Defined"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Angle"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Angle"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">1.0668000000000002</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1.0668000000000002"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"049439b4-5467-47c4-a72e-459e7fd736c2-00101795"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"049439b4-5467-47c4-a72e-459e7fd736c2-00101795"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">2.4928982400006445</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2.4928982400006445"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"04b3cqL6T7nASkHPv$no5N"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"04b3cqL6T7nASkHPv$no5N"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Curtain Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Curtain Wall"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"_Not Defined"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"_Not Defined"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Justification"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Beginning"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Beginning"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Justification"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Beginning"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Beginning"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Number"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Number"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">4</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"true"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.8128000000000001</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.8128000000000001"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-2.3368</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"-2.3368"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">2.3368000000006037</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2.3368000000006037"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1054613"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1054613"</span>
<span class="w">              </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdhNQ"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">1.4383160862420683</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1.4383160862420683"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"049439b4-5467-47c4-a72e-459e7fd736c2-001017a5"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"049439b4-5467-47c4-a72e-459e7fd736c2-001017a5"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.2317665212142757</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"3.2317665212142757"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.9860739215865809</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.9860739215865809"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"04b3cqL6T7nASkHPv$no5d"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"04b3cqL6T7nASkHPv$no5d"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"true"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.9398000000000002</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"-0.9398000000000002"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">4.546600000000602</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4.546600000000602"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1054629"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1054629"</span>
<span class="w">              </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdhNg"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Solar Wall (Parapet)"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">1.6460776368749865</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1.6460776368749865"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"049439b4-5467-47c4-a72e-459e7fd736c2-001017a6"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"049439b4-5467-47c4-a72e-459e7fd736c2-001017a6"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">1.376465981556736</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1.376465981556736"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.687905392562603</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.687905392562603"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"04b3cqL6T7nASkHPv$no5a"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"04b3cqL6T7nASkHPv$no5a"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Solar Wall (Parapet)"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Solar Wall (Parapet)"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"true"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.9398000000000002</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"-0.9398000000000002"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Tapered"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Tapered"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"3"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Exterior Angle"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.17453292519943278</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.17453292519943278"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Interior Angle"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Enable Angle Overrides"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Bottom Width"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.6387870964698155</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.6387870964698155"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Width"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.47307500000000025</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.47307500000000025"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.9397999999999986</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.9397999999999986"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1054630"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1054630"</span>
<span class="w">              </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdhNw"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">1.0626540981910537</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1.0626540981910537"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"049439b4-5467-47c4-a72e-459e7fd736c2-001017a7"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"049439b4-5467-47c4-a72e-459e7fd736c2-001017a7"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.768650122285474</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"3.768650122285474"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">1.1019842226549768</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1.1019842226549768"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"04b3cqL6T7nASkHPv$no5b"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"04b3cqL6T7nASkHPv$no5b"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Exterior - 12 5/8\" Rainscreen w Insultation on Metal Stud"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"true"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.9398000000000002</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"-0.9398000000000002"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">4.546600000000602</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4.546600000000602"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1054631"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1054631"</span>
<span class="w">              </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">          </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEwMTdhOA"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Solar Wall (Parapet)"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">1.2009675475581287</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1.2009675475581287"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"049439b4-5467-47c4-a72e-459e7fd736c2-001017a8"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"049439b4-5467-47c4-a72e-459e7fd736c2-001017a8"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.901755704546776</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.901755704546776"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.43464459760001195</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.43464459760001195"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"04b3cqL6T7nASkHPv$no5g"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"04b3cqL6T7nASkHPv$no5g"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Solar Wall (Parapet)"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Solar Wall (Parapet)"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"true"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.9398000000000002</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"-0.9398000000000002"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Tapered"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Tapered"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">3</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"3"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Exterior Angle"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.17453292519943278</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.17453292519943278"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Interior Angle"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Enable Angle Overrides"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Bottom Width"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.6387870964698155</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.6387870964698155"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Width"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.47307500000000025</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.47307500000000025"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"false"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.9397999999999986</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.9397999999999986"</span>
<span class="w">              </span><span class="p">},</span>
<span class="w">              </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1054632"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1054632"</span>
<span class="w">              </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
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
<p>After working through the steps mentioned above, you should see a screen similar to the following image:</p>
<blockquote>
<div><img alt="../../../../_images/elementsByElementGroupAtVersion.png" src="../../../../_images/elementsByElementGroupAtVersion.png">
</div></blockquote>
</section>
</section>


            <div class="clearer"></div>
          </div>