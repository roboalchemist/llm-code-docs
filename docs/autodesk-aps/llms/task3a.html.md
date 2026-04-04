# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/tutorials/tutorial-02/task3a.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="get-element-instances-of-a-particular-type">
<h1>Get Element Instances of a Particular Type</h1>
<p>In this guide, you will learn how to retrieve all instances of a particular type from a Design at Tip. Additionally, you can request select properties like Area, Volume, etc. of these instances and their type to be returned.
Let us try to retrieve all basic wall instances of the type <code class="docutils literal notranslate"><span class="pre">Foundation</span> <span class="pre">-</span> <span class="pre">24\"</span> <span class="pre">Concrete</span></code> from the Snowdon Towers Sample Architecture.rvt.</p>
<p>By the end of this guide, you will be able to:</p>
<ul class="simple">
<li>Fetch Instance Elements of a Type using <code class="docutils literal notranslate"><span class="pre">referencedBy</span> <span class="pre">(name:</span> <span class="pre">"Type")</span></code> relationship and <code class="docutils literal notranslate"><span class="pre">propertyFilter</span></code> to define the Category <code class="docutils literal notranslate"><span class="pre">Walls</span></code> &amp; Type <code class="docutils literal notranslate"><span class="pre">Foundation</span> <span class="pre">-</span> <span class="pre">24\"</span> <span class="pre">Concrete</span></code>.</li>
<li>Return only the properties that you need. For example: Area, Volume, Element Context, Element Name.</li>
<li>Use advance operators like contains, and, etc.</li>
</ul>
<p>You will use the following query in this guide:</p>
<div class="table-section"><table><thead><tr><th>Type</th><th>Operation</th><th>Description</th></tr></thead><tbody>
<tr class="row-even"><td>Query</td>
<td><a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementsByElementGroup">elementsByElementGroup</a></td>
<td>Retrieves element from given elementGroup, using additional RSQL filters.</td>
</tr>
</tbody></table></div>
<section id="step-1-request-for-a-list-of-elements-in-an-elementgroup">
<a href="#step-1-request-for-a-list-of-elements-in-an-elementgroup"><h2>Step 1: Request for a list of elements in an ElementGroup</h2></a>
<p>The <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/queries/elementsByElementGroup">elementsByElementGroup</a> query returns an <a class="reference external" href="/en/docs/aecdatamodel/v1/reference/objects/elements">Elements</a> object.</p>
<ol class="arabic">
<li>In <a class="reference external" href="https://aecdatamodel-explorer.autodesk.io/">AEC Data Model Explorer</a>, the query is populated by default in the <strong>Query Pane</strong>. You can also edit or update the query as per your requirement and run it.</p>
<blockquote>
<div><p><strong>Query</strong></p>
<blockquote>
<div><div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query<span class="w"> </span><span class="o">(</span><span class="nv">$elementGroupId</span>:<span class="w"> </span>ID!,<span class="w"> </span><span class="nv">$propertyFilter</span>:<span class="w"> </span>String!<span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">    </span>elementsByElementGroup<span class="o">(</span>
<span class="w">        </span>elementGroupId:<span class="w"> </span><span class="nv">$elementGroupId</span>
<span class="w">        </span>filter:<span class="w"> </span><span class="o">{</span><span class="w"> </span>query:<span class="w"> </span><span class="nv">$propertyFilter</span><span class="w"> </span><span class="o">}</span>
<span class="w">        </span>pagination:<span class="w"> </span><span class="o">{</span>limit:<span class="w"> </span><span class="m">5</span><span class="o">}</span>
<span class="w">    </span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">        </span>pagination<span class="w"> </span><span class="o">{</span>
<span class="w">            </span>cursor
<span class="w">        </span><span class="o">}</span>
<span class="w">        </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">            </span>id
<span class="w">            </span>name
<span class="w">            </span>properties<span class="w"> </span><span class="o">{</span>
<span class="w">                </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">                </span>name
<span class="w">                </span>value
<span class="w">                </span><span class="o">}</span>
<span class="w">            </span><span class="o">}</span>
<span class="w">            </span>referencedBy<span class="o">(</span>name:<span class="w"> </span><span class="s2">"Type"</span><span class="o">)</span><span class="w"> </span><span class="o">{</span>
<span class="w">                </span>pagination<span class="w"> </span><span class="o">{</span>
<span class="w">                    </span>cursor
<span class="w">                </span><span class="o">}</span>
<span class="w">                </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">                    </span>id
<span class="w">                    </span>name
<span class="w">                    </span>alternativeIdentifiers<span class="w"> </span><span class="o">{</span>
<span class="w">                        </span>externalElementId
<span class="w">                    </span><span class="o">}</span>
<span class="w">                    </span>properties<span class="w"> </span><span class="o">{</span>
<span class="w">                        </span>results<span class="w"> </span><span class="o">{</span>
<span class="w">                            </span>name
<span class="w">                            </span>value
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
<ol class="arabic simple">
<li>In the Query Variables Pane, replace the value of the <code class="docutils literal notranslate"><span class="pre">elementGroupId</span></code> variable with the elementGroup ID that you used in <a class="reference external" href="/en/docs/aecdatamodel/v1/tutorials/tutorial-01/nav-elements/">Navigate to Elementgroups</a> of previous tutorial.</li>
<li>In the Query Variables Pane, replace the value of the <a href="#id2"><span class="problematic" id="id3">``</span></a>propertyFilter <a href="#id4"><span class="problematic" id="id5">``</span></a>with the property filter of your choice.</li>
</ol>
<p><strong>Note</strong>: To know about the list of supported metadata filtering options, refer <a class="reference external" href="/en/docs/aecdatamodel/v1/developers_guide/filtering/advanced-filtering/">Advanced Filtering Capabilities</a> page.</p>
<blockquote>
<div><div class="highlight-shell notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="o">{</span>
<span class="w">    </span><span class="s2">"elementGroupId"</span>:<span class="w"> </span><span class="s2">"YWVjZH42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVB"</span>,
<span class="w">    </span><span class="s2">"propertyFilter"</span>:<span class="w"> </span><span class="s2">"'property.name.category'=contains=Walls and 'property.name.Element Context'==Type and 'property.name.Element Name'=contains='Foundation - 24'"</span>
<span class="o">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</div></blockquote>
</li>
<li>Click <strong>Play</strong>. The list of elements with its tip ID and name will appear in the response.</p>
<blockquote>
<div><p>The response should be similar to the following code-block:</p>
<p><strong>Response</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"elementsByElementGroup"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzEyYTFiNQ"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Description"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Manufacturer"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Model"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Type Comments"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"URL"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Absorptance"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.7</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Heat Transfer Coefficient (U)"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.30218381255198806</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Roughness"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">3</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Thermal Mass"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">921166.5599999999</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Thermal Resistance (R)"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.582791586998088</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Coarse Scale Fill Color"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cost"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"9bd3aa6c-2785-4080-985d-83d6cac9401d-0012a1b5"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Fire Rating"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4 HR"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Function"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export Type to IFC"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Default"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export Type to IFC As"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Type IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Type IfcGUID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2Rqwfi9uL0W9XTWzRAs_6e"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Keynote"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Type"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Assembly Code"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"A1010200"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Assembly Description"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation Walls"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Width"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.6096</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Type Mark"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"C04"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Wrapping at Ends"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"None"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Wrapping at Inserts"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Do not wrap"</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1221045"</span>
<span class="w">            </span><span class="p">}</span>
<span class="w">            </span><span class="p">]</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="nt">"referencedBy"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"pagination"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">            </span><span class="nt">"cursor"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NDY1"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-00097465"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">14.389100000000056</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-00097465"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">50.7037695600002</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">30.909017923776116</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1G_I00WlX2MBQekqB04dJ5"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.5052000000000003</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"619621"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NDY2"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-00097466"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.162299999999996</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-00097466"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">10.550301479999995</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">6.431463782207994</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1G_I00WlX2MBQekqB04dJ6"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.5052000000000003</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"619622"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NDY3"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-00097467"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">21.015009407150227</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-00097467"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">114.5973418770376</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">68.69976110255986</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1G_I00WlX2MBQekqB04dJ7"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">5.3086</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"619623"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NjBk"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760d"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">18.516599999999997</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760d"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">42.779189806685366</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">24.885678424383006</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1G_I00WlX2MBQekqB04dQj"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.5052000000000003</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"620045"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NjBl"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760e"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.688334025144647</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760e"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">5.522060309977901</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.366247964962528</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1G_I00WlX2MBQekqB04dQk"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">4.2545</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"620046"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NjBm"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760f"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">6.959599999999995</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-0009760f"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">28.312846599999972</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">17.259511287359985</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1G_I00WlX2MBQekqB04dQl"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">4.2545</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"620047"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBXzk3NjEw"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-00097610"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">9.110132736414313</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"50f92000-82f8-4258-b6a8-bb42c01b00a0-00097610"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">42.54464127343791</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">25.870041820730258</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1G_I00WlX2MBQekqB04dQm"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.508</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">4.8006</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"620048"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2E1ZGJj"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"717ca888-caa1-4d79-a802-1815f215117a-000a5dbc"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">24.744186068650656</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"717ca888-caa1-4d79-a802-1815f215117a-000a5dbc"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">103.2902726290742</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">62.45983083152432</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1nVAY8og5DUQW261No7qp6"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">4.2545</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"679356"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2E3ZDhk"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ba8abc87-1993-4a27-9c7e-28f6d5ef2e36-000a7d8d"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">9.44880000000004</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ba8abc87-1993-4a27-9c7e-28f6d5ef2e36-000a7d8d"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">38.68756554362559</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">23.385969951459128</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2wYho76PDA9vn_AFRLvLEx"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">4.2545</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"687501"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2E3ZTBh"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ba8abc87-1993-4a27-9c7e-28f6d5ef2e36-000a7e0a"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">11.32652046598141</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ba8abc87-1993-4a27-9c7e-28f6d5ef2e36-000a7e0a"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">48.27367622366221</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">29.375820134206812</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2wYho76PDA9vn_AFRLvL0y"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">4.2545</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"687626"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2FhNDY0"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"8b2fcbb6-3350-4536-a114-8d91a78c59b4-000aa464"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">7.25169999999995</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"8b2fcbb6-3350-4536-a114-8d91a78c59b4-000aa464"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">25.685755079999822</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">15.658036296767891</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2BByksCr15Dg4KZP6dXltG"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.5052000000000003</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"697444"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2FhNDhk"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"8b2fcbb6-3350-4536-a114-8d91a78c59b4-000aa48d"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">15.430499999999984</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"8b2fcbb6-3350-4536-a114-8d91a78c59b4-000aa48d"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">52.27925027999992</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">31.386274775711957</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2BByksCr15Dg4KZP6dXlqv"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.5052000000000003</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"697485"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2I4ZmNl"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"5ec49cf7-f328-41e6-8f02-263b961f3b28-000b8fce"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">9.07033402514468</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"5ec49cf7-f328-41e6-8f02-263b961f3b28-000b8fce"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">25.3814803232309</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">15.472550405041552</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1Un9ptyoX1vey29ZkM5BJc"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.6096</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">2.8956000000000004</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"757710"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2I5MDM0"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"5ec49cf7-f328-41e6-8f02-263b961f3b28-000b9034"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">9.070334025152942</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"5ec49cf7-f328-41e6-8f02-263b961f3b28-000b9034"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">25.38148032323287</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">15.472550405042778</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1Un9ptyoX1vey29ZkM5AiS"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.6096</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">2.8956000000000004</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"757812"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2NmZDg1"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"487309ac-3af1-4fab-a7bb-9b30a3910b36-000cfd85"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">6.270019527898146</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"487309ac-3af1-4fab-a7bb-9b30a3910b36-000cfd85"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">31.310036735424237</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">19.019273381248762</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"18SmciEl5FgwUxcp2ZdVQp"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">5.3086</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"851333"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
<span class="w">                </span><span class="p">}</span>
<span class="w">            </span><span class="p">},</span>
<span class="w">            </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZX42SUpGQXdONExWTG5JZXZiQk5GNU1IX0wyQ35yRWRKT0NPcVIwZWt5SkJCWWxSOUVBX2ZmYzFi"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span><span class="p">,</span>
<span class="w">                </span><span class="nt">"alternativeIdentifiers"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"externalElementId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"c40d2a77-58c6-4479-8315-653c702baee6-000ffc1b"</span>
<span class="w">                </span><span class="p">},</span>
<span class="w">                </span><span class="nt">"properties"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">                </span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Comments"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">2.933699999999996</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Design Option"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Main Model"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Mark"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"External ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"c40d2a77-58c6-4479-8315-653c702baee6-000ffc1b"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Area"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">10.86046214999999</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Volume"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">6.620537726639986</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"By Type"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Export to IFC As"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IFC Predefined Type"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">null</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"IfcGUID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"343IftMCP4UOCLPJnm95Bz"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Category Type Id"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Walls"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Basic Wall"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Name"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Foundation - 24\" Concrete"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Element Context"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Instance"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Related to Mass"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Room Bounding"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.1524</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Base is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Cross-Section"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Vertical"</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Location Line"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Usage"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Extension Distance"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top is Attached"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Top Offset"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Unconnected Height"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="mf">4.2545</span>
<span class="w">                    </span><span class="p">},</span>
<span class="w">                    </span><span class="p">{</span>
<span class="w">                    </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Revit Element ID"</span><span class="p">,</span>
<span class="w">                    </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1047579"</span>
<span class="w">                    </span><span class="p">}</span>
<span class="w">                </span><span class="p">]</span>
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
<p>After working through the steps mentioned above, you should see a screen similar to the following image:</p>
<blockquote>
<div><img alt="../../../../_images/elementsbyelementgroup.png" src="../../../../_images/elementsbyelementgroup.png">
</div></blockquote>
</div></blockquote>
</li>
</ol>
</section>
</section>


            <div class="clearer"></div>
          </div>