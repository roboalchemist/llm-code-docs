# Source: https://developer.doc.autodesk.com/bPlouYTd/forge-aim-graphql-docs-main-483279/aecdatamodel/v1/tutorials/tutorial-02/distinctvaluesquery.html

<div class="api-documentation">
<meta name="sphinx-version" content="5.0.0">
            
  <section id="get-distinct-values-of-properties">
<h1>Get Distinct Values of Properties</h1>
<p>This page describes how to use the following queries to retrieve distinct values of properties in the AEC Data Model API. These queries enable you to find and retrieve all distinct values of a given property within an element group, either by property definition ID or property name.</p>
<blockquote>
<div><ul class="simple">
<li><strong>distinctPropertyValuesInElementGroupById</strong></li>
<li><strong>distinctPropertyValuesInElementGroupByName</strong></li>
</ul>
</div></blockquote>
<p>Both queries accept an element filter for more advanced queries.</p>
<section id="step-1-retrieve-distinct-values-by-id">
<a href="#step-1-retrieve-distinct-values-by-id"><h2>Step 1: Retrieve distinct values by ID</h2></a>
<p>The following example returns the distinct values of a given property filtered by IDs.</p>
<p><strong>Query</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query ($elementGroupId: ID!, $propertyDefinitionId: ID!, $filter: ElementFilterInput) {
  distinctPropertyValuesInElementGroupById(elementGroupId: $elementGroupId, propertyDefinitionId: $propertyDefinitionId, filter: $filter) {
    values(limit: 200) {
      value,
      count
    }
  }
}
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
<p><strong>Variables</strong></p>
<blockquote>
<div><p><strong>Get all categories in an element group (by ID)</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"elementGroupId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"propertyDefinitionId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"autodesk.revit.parameter:parameter.category-2.0.0"</span>
<span class="p">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</div></blockquote>
<p><strong>Response</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="nt">"values"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Curtain Wall Mullions"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"count"</span><span class="p">:</span><span class="w"> </span><span class="mi">2372</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Analytical Nodes"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"count"</span><span class="p">:</span><span class="w"> </span><span class="mi">1410</span>
<span class="w">    </span><span class="p">}</span>
<span class="p">]</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
<p><strong>IMPORTANT:</strong> The count represents the number of unique assets that have this specific property value. For example, if a property value is only found once on a certain type asset, but that type asset is referenced by multiple instance assets, the count returned will be 1.</p>
<p>(OR)</p>
</section>
<section id="retrieve-distinct-values-by-name">
<a href="#retrieve-distinct-values-by-name"><h2>Retrieve distinct values by Name</h2></a>
<p>The following example returns the distinct values of a given property filtered by name.</p>
<p>When querying for distinct values <strong>by Name</strong>. multiple properties can have the same name so the response contains the distinct values of all properties matching that name:</p>
<p><strong>Query</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span>query ($elementGroupId: ID!, $name: String!, $filter: ElementFilterInput, $pagination: PaginationInput) {
  distinctPropertyValuesInElementGroupByName(elementGroupId: $elementGroupId, name: $name, filter: $filter, pagination: $pagination) {
    pagination {
        cursor
    }
    results {
        definition {
          id
        }
        values(limit: 200) {
          value
          count
        }
    }
  }
}
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
<p><strong>Variables</strong></p>
<p><strong>Get all categories in an element group (by name)</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-default margin-bottom-3"><div class="highlight snippet-container margin-bottom-0 pad-bottom-0"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"elementGroupId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Length"</span>
<span class="p">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
<p><strong>Response</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="nt">"results"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">  </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"autodesk.revit.parameter:structuralFoundationLength-2.0.0"</span><span class="p">,</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="nt">"values"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1.93546015625"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"count"</span><span class="p">:</span><span class="w"> </span><span class="mi">5</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1.0947796875000002"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"count"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">]</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"definition"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"autodesk.revit.parameter:continuousrailEndExtensionLengthParam-2.0.0"</span><span class="p">,</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="nt">"values"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"3.0463569792873577"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"count"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">]</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
<p>If too many properties match the specified name, the result will be paginated.</p>
<p><strong>IMPORTANT:</strong> The count represents the number of unique assets that have this specific property value. For example, if a property value is only found once on a certain type asset, but that type asset is referenced by multiple instance assets, the count returned will be 1.</p>
<section id="vairable-examples-filtering-by-categories-and-materials">
<h3>Vairable examples: Filtering by Categories and Materials</h3>
<p>Besides retrieving distinct values of properties by IDs and names, you can also retrieve by specific categories, families, structural materials used in categories, etc. Refer to the following variable examples to see how to provide the filter values for each of those options.</p>
<p><strong>A few more variable examples:</strong></p>
<ul>
<li><strong>Get all family names in an element group for a given category (Doors, in this example)</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"elementGroupId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Family Name"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"filter"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="nt">"query"</span><span class="p">:</span><span class="w"> </span><span class="s2">"property.name.category==Doors"</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li><strong>Get all types for a given family (Single, in this example)</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"elementGroupId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Type"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"filter"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"query"</span><span class="p">:</span><span class="w"> </span><span class="s2">"'property.name.Family Name'=='Single'"</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li><strong>Get all distinct structural materials used in walls</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"elementGroupId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Structural Material"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"filter"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"query"</span><span class="p">:</span><span class="w"> </span><span class="s2">"property.name.category==Walls"</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
<li><strong>Get all the door widths that are less than 0.9 meters</strong></p>
<blockquote>
<div><div class="highlight-json notranslate x-snippet-block x-snippet-block--height-200 margin-bottom-3"><div class="highlight snippet-container"><pre><code><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"elementGroupId"</span><span class="p">:</span><span class="w"> </span><span class="s2">"YWVjZH5JR0JWdWROM2QxdW1kTkJZRnR2ZlpBX0wyQ35GZGhKOWZxZFJSR2QxTXAwNU1RWkVR"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Width"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"filter"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"query"</span><span class="w"> </span><span class="p">:</span><span class="w"> </span><span class="s2">"property.name.category==Doors"</span><span class="p">,</span>
<span class="w">    </span><span class="s2">"properties"</span><span class="w"> </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"name"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Width"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"valueWithComparator"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"value"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0.9"</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"comparator"</span><span class="p">:</span><span class="w"> </span><span class="s2">"LESS_THAN"</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</code></pre><div class="snippet-toggle js-snippet-toggle">Show More</div></div><div class="clipboard-container"><i class="fui-icon fui-icon-copy clipboard-icon"></i></div>
</div>
</div></blockquote>
</li>
</ul>
</section>
</section>
</section>


            <div class="clearer"></div>
          </div>