# Module: Nokogiri::XML::Searchable
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Node, NodeSet
  
  

  
  
    Defined in:
    lib/nokogiri/xml/searchable.rb
  
  

## Overview

  
    

The Searchable module declares the interface used for searching your DOM.

```
It implements the public methods #search, #css, and #xpath,
as well as allowing specific implementations to specialize some
of the important behaviors.

```

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        LOOKS_LIKE_XPATH =
          
  
    

Regular expression used by Searchable#search to determine if a query string is CSS or XPath

  

  

        
        

```
%r{^(\./|/|\.\.|\.$)}
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**>**(selector)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   >(selector) → NodeSet.

  

      
        
- 
  
    
      #**at**(*args)  ⇒ Object 
    

    
      (also: #%)
    
  
  
  
  
  
  
  
  

  
    

call-seq:   at(*paths, [namespace-bindings, xpath-variable-bindings, custom-handler-class]).

  

      
        
- 
  
    
      #**at_css**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq:   at_css(*rules, [namespace-bindings, custom-pseudo-class]).

  

      
        
- 
  
    
      #**at_xpath**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq:   at_xpath(*paths, [namespace-bindings, variable-bindings, custom-handler-class]).

  

      
        
- 
  
    
      #**css**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq:   css(*rules, [namespace-bindings, custom-pseudo-class]).

  

      
        
- 
  
    
      #**search**(*args)  ⇒ Object 
    

    
      (also: #/)
    
  
  
  
  
  
  
  
  

  
    

call-seq:   search(*paths, [namespace-bindings, xpath-variable-bindings, custom-handler-class]).

  

      
        
- 
  
    
      #**xpath**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq:   xpath(*paths, [namespace-bindings, variable-bindings, custom-handler-class]).

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**>**(selector)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
>(selector) → NodeSet

```

Search this node’s immediate children using CSS selector `selector`

  

  

  
    
      

```

201
202
203
204
```

    
    
      

```
# File 'lib/nokogiri/xml/searchable.rb', line 201

def >(selector) # rubocop:disable Naming/BinaryOperatorParameterName
  ns = document.root&.namespaces || {}
  xpath(CSS.xpath_for(selector, prefix: "./", ns: ns).first)
end
```

    
  

    
      
  
### 
  
    #**at**(*args)  ⇒ Object 
  

  
    Also known as:
    %
    
  

  

  
    

call-seq:

```
at(*paths, [namespace-bindings, xpath-variable-bindings, custom-handler-class])

```

Search this object for `paths`, and return only the first result. `paths` must be one or more XPath or CSS queries.

See Searchable#search for more information.

  

  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/nokogiri/xml/searchable.rb', line 74

def at(*args)
  search(*args).first
end
```

    
  

    
      
  
### 
  
    #**at_css**(*args)  ⇒ Object 
  

  

  

  
    

call-seq:

```
at_css(*rules, [namespace-bindings, custom-pseudo-class])

```

Search this object for CSS `rules`, and return only the first match. `rules` must be one or more CSS selectors.

See Searchable#css for more information.

  

  

  
    
      

```

143
144
145
```

    
    
      

```
# File 'lib/nokogiri/xml/searchable.rb', line 143

def at_css(*args)
  css(*args).first
end
```

    
  

    
      
  
### 
  
    #**at_xpath**(*args)  ⇒ Object 
  

  

  

  
    

call-seq:

```
at_xpath(*paths, [namespace-bindings, variable-bindings, custom-handler-class])

```

Search this node for XPath `paths`, and return only the first match. `paths` must be one or more XPath queries.

See Searchable#xpath for more information.

  

  

  
    
      

```

193
194
195
```

    
    
      

```
# File 'lib/nokogiri/xml/searchable.rb', line 193

def at_xpath(*args)
  xpath(*args).first
end
```

    
  

    
      
  
### 
  
    #**css**(*args)  ⇒ Object 
  

  

  

  
    

call-seq:

```
css(*rules, [namespace-bindings, custom-pseudo-class])

```

Search this object for CSS `rules`. `rules` must be one or more CSS selectors. For example:

```
node.css('title')
node.css('body h1.bold')
node.css('div + p.green', 'div#one')

```

A hash of namespace bindings may be appended. For example:

```
node.css('bike|tire', {'bike' => 'http://schwinn.com/'})

```

💡 Custom CSS pseudo classes may also be defined which are mapped to a custom XPath function.  To define custom pseudo classes, create a class and implement the custom pseudo class you want defined. The first argument to the method will be the matching context NodeSet. Any other arguments are ones that you pass in. For example:

```
handler = Class.new {
  def regex(node_set, regex)
    node_set.find_all { |node| node['some_attribute'] =~ /#{regex}/ }
  end
}.new
node.css('title:regex("\w+")', handler)

```

💡 Some XPath syntax is supported in CSS queries. For example, to query for an attribute:

```
node.css('img > @href') # returns all +href+ attributes on an +img+ element
node.css('img / @href') # same

# ⚠ this returns +class+ attributes from all +div+ elements AND THEIR CHILDREN!
node.css('div @class')

node.css

```

💡 Array-like syntax is supported in CSS queries as an alternative to using :nth-child().

⚠ NOTE that indices are 1-based like `:nth-child` and not 0-based like Ruby Arrays. For example:

```
# equivalent to 'li:nth-child(2)'
node.css('li[2]') # retrieve the second li element in a list

```

⚠ NOTE that the CSS query string is case-sensitive with regards to your document type. HTML tags will match only lowercase CSS queries, so if you search for “H1” in an HTML document, you’ll never find anything. However, “H1” might be found in an XML document, where tags names are case-sensitive (e.g., “H1” is distinct from “h1”).

  

  

  
    
      

```

129
130
131
132
133
```

    
    
      

```
# File 'lib/nokogiri/xml/searchable.rb', line 129

def css(*args)
  rules, handler, ns, _ = extract_params(args)

  css_internal(self, rules, handler, ns)
end
```

    
  

    
      
  
### 
  
    #**search**(*args)  ⇒ Object 
  

  
    Also known as:
    /
    
  

  

  
    

call-seq:

```
search(*paths, [namespace-bindings, xpath-variable-bindings, custom-handler-class])

```

Search this object for `paths`. `paths` must be one or more XPath or CSS queries:

```
node.search("div.employee", ".//title")

```

A hash of namespace bindings may be appended:

```
node.search('.//bike:tire', {'bike' => 'http://schwinn.com/'})
node.search('bike|tire', {'bike' => 'http://schwinn.com/'})

```

For XPath queries, a hash of variable bindings may also be appended to the namespace bindings. For example:

```
node.search('.//address[@domestic=$value]', nil, {:value => 'Yes'})

```

💡 Custom XPath functions and CSS pseudo-selectors may also be defined. To define custom functions create a class and implement the function you want to define, which will be in the `nokogiri` namespace in XPath queries.

The first argument to the method will be the current matching NodeSet. Any other arguments are ones that you pass in. Note that this class may appear anywhere in the argument list. For example:

```
handler = Class.new {
  def regex node_set, regex
    node_set.find_all { |node| node['some_attribute'] =~ /#{regex}/ }
  end
}.new
node.search('.//title[nokogiri:regex(., "\w+")]', 'div.employee:regex("[0-9]+")', handler)

```

See Searchable#xpath and Searchable#css for further usage help.

  

  

  
    
      

```

54
55
56
57
58
59
60
61
62
```

    
    
      

```
# File 'lib/nokogiri/xml/searchable.rb', line 54

def search(*args)
  paths, handler, ns, binds = extract_params(args)

  xpaths = paths.map(&:to_s).map do |path|
    LOOKS_LIKE_XPATH.match?(path) ? path : xpath_query_from_css_rule(path, ns)
  end.flatten.uniq

  xpath(*(xpaths + [ns, handler, binds].compact))
end
```

    
  

    
      
  
### 
  
    #**xpath**(*args)  ⇒ Object 
  

  

  

  
    

call-seq:

```
xpath(*paths, [namespace-bindings, variable-bindings, custom-handler-class])

```

Search this node for XPath `paths`. `paths` must be one or more XPath queries.

```
node.xpath('.//title')

```

A hash of namespace bindings may be appended. For example:

```
node.xpath('.//foo:name', {'foo' => 'http://example.org/'})
node.xpath('.//xmlns:name', node.root.namespaces)

```

A hash of variable bindings may also be appended to the namespace bindings. For example:

```
node.xpath('.//address[@domestic=$value]', nil, {:value => 'Yes'})

```

💡 Custom XPath functions may also be defined. To define custom functions create a class and implement the function you want to define, which will be in the `nokogiri` namespace.

The first argument to the method will be the current matching NodeSet. Any other arguments are ones that you pass in. Note that this class may appear anywhere in the argument list. For example:

```
handler = Class.new {
  def regex(node_set, regex)
    node_set.find_all { |node| node['some_attribute'] =~ /#{regex}/ }
  end
}.new
node.xpath('.//title[nokogiri:regex(., "\w+")]', handler)

```

  

  

  
    
      

```

179
180
181
182
183
```

    
    
      

```
# File 'lib/nokogiri/xml/searchable.rb', line 179

def xpath(*args)
  paths, handler, ns, binds = extract_params(args)

  xpath_internal(self, paths, handler, ns, binds)
end
```