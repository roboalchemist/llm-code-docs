# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/tutorials/tutorial-02/task5a.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="get-project-elements-with-specific-properties">
<h1>Get Project Elements with Specific Properties</h1>
<p>In this guide, you will learn how to retrieve elements in a project based on specific properties using the AEC Data Model Explorer. You will retrieve elements that match certain criteria, such as walls with a length rating greater than 10.</p>
<p>By the end of this guide, you will be able to:</p>
<ul class="simple">
<li>Fetch wall elements with a length greater than 10 from all elementGroups in a project and information like id and properties.</li>
<li>Understand the options and fields in the documentation on the elements query, elements object, and Properties object.</li>
</ul>
<p>You will use the following query in this guide:</p>
<div class="table-section"><table><thead><tr><th>Type</th><th>Operation</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>Query</td>
<td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementsbyproject">elementsByProject</a></td>
<td>Retrieves element in the given project, using additional RSQL filters if provided.</td>
</tr>
</tbody></table></div>
<section id="step-1-request-elements-matching-the-specified-classification-filter">
<a href="#step-1-request-elements-matching-the-specified-classification-filter"><h2>Step 1: Request Elements Matching the Specified Classification Filter</h2></a>
<p>The <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementsbyproject">elementsByProject</a> query returns <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elements">Elements</a> object, which contains an array of Elements objects.</p>
<dl class="docutils">
<dt>For this exercise, we request all elements instances with</dt><dd><ul class="simple">
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
<div><div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span>GetElementsInProject<span class="o">(</span><span class="nv">$projectId</span>:<span class="w"> </span>ID!,<span class="w"> </span><span class="nv">$propertyFilter</span>:<span class="w"> </span>String!<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>elementsByProject<span class="o">(</span>projectId:<span class="w"> </span><span class="nv">$projectId</span>,<span class="w"> </span>filter:<span class="w"> </span><span class="o">{</span>query:<span class="w"> </span><span class="nv">$propertyFilter</span><span class="o">})</span><span class="w"> </span><span class="o">{</span>
<span class="w">        </span>pagination<span class="w"> </span><span class="o">{</span>
<span class="w">            </span>cursor
<span class="w">        </span><span class="o">}</span>
<span class="w">        </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">            </span>id
<span class="w">            </span>name
<span class="w">            </span>properties<span class="o">(</span>
<span class="w">                </span>includeReferencesProperties:<span class="w"> </span><span class="s2">"Type"</span>
<span class="w">                </span>filter:<span class="w"> </span><span class="o">{</span>names:<span class="w"> </span><span class="o">[</span><span class="s2">"Family Name"</span>,<span class="w"> </span><span class="s2">"Element Name"</span>,<span class="w"> </span><span class="s2">"Element Context"</span>,<span class="w"> </span><span class="s2">"Fire Rating"</span><span class="o">]}</span>
<span class="w">            </span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">                </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">                    </span>name
<span class="w">                    </span>value
<span class="w">                    </span>displayValue
<span class="w">                    </span>definition<span class="w"> </span><span class="o">{</span>
<span class="w">                        </span>units<span class="o">{</span>
<span class="w">                        </span>name
<span class="w">                        </span><span class="o">}</span>
<span class="w">                    </span><span class="o">}</span>
<span class="w">                </span><span class="o">}</span>
<span class="w">            </span><span class="o">}</span>
<span class="w">        </span><span class="o">}</span>
<span class="w">    </span><span class="o">}</span>
<span class="o">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
<p><strong>Query Variables</strong></p>
<blockquote>
<div><ul class="simple">
<li>In the Query Variables Pane, replace the value of the <code class="docutils literal notranslate"><span class="pre">projectId</span></code> variable with the  project ID that you used in <a class="reference external" href="/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements">Navigate to Elementgroups</a>.</li>
<li>In the Query Variables Pane, replace the value of the <code class="docutils literal notranslate"><span class="pre">propertyFilter</span></code> with the property filter of your choice.</li>
</ul>
<p><strong>Note</strong>: To know the list of supported metadata filtering options, refer to the <a class="reference external" href="/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering">Advanced Filtering Capabilities</a>   page.</p>
<div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="o">{</span>
<span class="w">    </span><span class="s2">"projectId"</span>:<span class="w"> </span><span class="s2">"urn:adsk.workspace:prod.project:39208068-e548-4d9e-b8a7-e000fdf2a9b4"</span>,
<span class="w">    </span><span class="s2">"propertyFilter"</span>:<span class="w"> </span><span class="s2">"'property.name.Family Name'=='Basic Wall' and property.name.Length &gt; 10 and 'property.name.Element Context'==Instance"</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</div></blockquote>
</li>
<li>Click <strong>Play</strong>. The list of elements available within that elementGroup of property âfamilyâ and value ââBasic Wallâ is displayed in the response. The response should be similar to the following code-block:</p>
<blockquote>
<div><p><strong>Note</strong>: The following code is a subset data of complete response, hence do not use this as reference.</p>
<p><strong>Response</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"elementsByProject"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWRjdXJzfjB-NTB-NTA"</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ340VFVtRnF0WFJVVy1CS09Gb1cyd3FRXzE4NTI4MQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ340VFVtRnF0WFJVVy1CS09Gb1cyd3FRXzE4NTI4Mg"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ340VFVtRnF0WFJVVy1CS09Gb1cyd3FRXzE4NTI4Mw"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ340VFVtRnF0WFJVVy1CS09Gb1cyd3FRXzE4NTI4NA"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 200mm"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzExNjJiYw"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Retaining - 12\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Retaining - 12\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Retaining - 12\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzExNjJiZA"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Retaining - 12\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Retaining - 12\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Retaining - 12\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNGM2Nw"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTYzNQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTYzNg"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTcxMg"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTcxMw"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTcxNA"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTcxNQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35Mdm9zVEo1N1JYZWZOWTFiYWNoUVRRXzEzNTcxNw"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35fR1IzdHpORlI3LV9tclFBOGR4TWN3XzE4NGNkMg"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Proposed Partition 4\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Proposed Partition 4\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Proposed Partition 4\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEwNTc3ZQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 39 - L2 Entablature"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 39 - L2 Entablature"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 39 - L2 Entablature"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEwNTg3Yg"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEwNTkwZA"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEwNjk1Zg"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEwNjk4OQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmI5Zg"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmJiNQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmJjNQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmMwMQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmMxOA"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmMyYQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmM0Nw"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmM2YQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmM4Yg"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEyZmZmNQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEzMDBlZg"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEzMDFiYw"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzEzMDRmNA"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDI5"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJh"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 6\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 6\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 6\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJi"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 6\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 6\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 6\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJj"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 43"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 43"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 43"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJk"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJl"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDJm"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 12\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDMx"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 37"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 37"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 37"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDMy"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 37"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 37"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Block 37"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDM2"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDQx"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDQ0"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDQ3"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDRh"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDRk"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDUw"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35mV0R1ZkIteVNtcTVGd242RmoxXy1nXzkwZDc3"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Generic - 10\""</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"displayValue"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"units"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">]</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</div></blockquote>
</li>
</ol>
<p>After working through the steps mentioned above, your Explorer should look similar to the following image:</p>
<blockquote>
<div><img alt="../../../../_images/elementsByProject.png" src="../../../../_images/elementsByProject.png">
</div></blockquote>
</section>
</section>


            <div class="clearer"></div>
          </div>