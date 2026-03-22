# Class: Nokogiri::XML::NodeSet
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::NodeSet
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Enumerable, Searchable
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/node_set.rb,

  ext/nokogiri/xml_node_set.c

  
  

## Overview

  
    

A NodeSet is an Enumerable that contains a list of Nokogiri::XML::Node objects.

Typically a NodeSet is returned as a result of searching a Document via Nokogiri::XML::Searchable#css or Nokogiri::XML::Searchable#xpath.

Note that the `#dup` and `#clone` methods perform shallow copies; these methods do not copy the Nodes contained in the NodeSet (similar to how Array and other Enumerable classes work).

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        IMPLIED_XPATH_CONTEXTS =
          
  
    

:nodoc:

  

  

        
        

```
[".//", "self::"].freeze

```

      
    
  

  
  
  
### Constants included
     from Searchable

  

Searchable::LOOKS_LIKE_XPATH

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**document**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The Document this NodeSet is associated with.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**&**(node_set)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set Intersection — Returns a new NodeSet containing nodes common to the two NodeSets.

  

      
        
- 
  
    
      #**-**(node_set)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Difference - returns a new NodeSet that is a copy of this NodeSet, removing  each item that also appears in `node_set`.

  

      
        
- 
  
    
      #**==**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Equality – Two NodeSets are equal if the contain the same number of elements and if each element is equal to the corresponding element in the other NodeSet.

  

      
        
- 
  
    
      #**[]**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    start, length

-> NodeSet or nil  [range] -> NodeSet or nil  slice(index) -> Node or nil  slice(start, length) -> NodeSet or nil  slice(range) -> NodeSet or nil.

  

      
        
- 
  
    
      #**add_class**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add the class attribute `name` to all Node objects in the NodeSet.

  

      
        
- 
  
    
      #**after**(datum)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Insert `datum` after the last Node in this NodeSet.

  

      
        
- 
  
    
      #**append_class**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Append the class attribute `name` to all Node objects in the NodeSet.

  

      
        
- 
  
    
      #**at**(*args)  ⇒ Object 
    

    
      (also: #%)
    
  
  
  
  
  
  
  
  

  
    

call-seq: search *paths, [namespace-bindings, xpath-variable-bindings, custom-handler-class].

  

      
        
- 
  
    
      #**attr**(key, value = nil, &block)  ⇒ Object 
    

    
      (also: #set, #attribute)
    
  
  
  
  
  
  
  
  

  
    

Set attributes on each Node in the NodeSet, or get an attribute from the first Node in the NodeSet.

  

      
        
- 
  
    
      #**before**(datum)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Insert `datum` before the first Node in this NodeSet.

  

      
        
- 
  
    
      #**children**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a new NodeSet containing all the children of all the nodes in the NodeSet.

  

      
        
- 
  
    
      #**css**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq: css *rules, [namespace-bindings, custom-pseudo-class].

  

      
        
- 
  
    
      #**deconstruct**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: deconstruct() → Array.

  

      
        
- 
  
    
      #**delete**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Delete `node` from the Nodeset, if it is a member.

  

      
        
- 
  
    
      #**each**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Iterate over each node, yielding  to `block`.

  

      
        
- 
  
    
      #**empty?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Is this NodeSet empty?.

  

      
        
- 
  
    
      #**filter**(expr)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Filter this list for nodes that match `expr`.

  

      
        
- 
  
    
      #**first**(n = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the first element of the NodeSet.

  

      
        
- 
  
    
      #**include?**(node)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if any member of node set equals `node`.

  

      
        
- 
  
    
      #**index**(node = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the index of the first node in self that is == to `node` or meets the given block.

  

      
        
- 
  
    
      #**initialize**(document, list = []) {|_self| ... } ⇒ NodeSet 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Create a NodeSet with `document` defaulting to `list`.

  

      
        
- 
  
    
      #**inner_html**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the inner html of all contained Node objects.

  

      
        
- 
  
    
      #**inner_text**  ⇒ Object 
    

    
      (also: #text)
    
  
  
  
  
  
  
  
  

  
    

Get the inner text of all contained Node objects.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return a nicely formatted string representation.

  

      
        
- 
  
    
      #**last**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the last element of the NodeSet.

  

      
        
- 
  
    
      #**length**  ⇒ Object 
    

    
      (also: #size)
    
  
  
  
  
  
  
  
  

  
    

Get the length of the node set.

  

      
        
- 
  
    
      #**pop**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Removes the last element from set and returns it, or `nil` if the set is empty.

  

      
        
- 
  
    
      #**push**(node)  ⇒ Object 
    

    
      (also: #<<)
    
  
  
  
  
  
  
  
  

  
    

Append `node` to the NodeSet.

  

      
        
- 
  
    
      #**remove_attr**(name)  ⇒ Object 
    

    
      (also: #remove_attribute)
    
  
  
  
  
  
  
  
  

  
    

Remove the attributed named `name` from all Node objects in the NodeSet.

  

      
        
- 
  
    
      #**remove_class**(name = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Remove the class attribute `name` from all Node objects in the NodeSet.

  

      
        
- 
  
    
      #**reverse**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a new NodeSet containing all the nodes in the NodeSet in reverse order.

  

      
        
- 
  
    
      #**shift**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the first element of the NodeSet and removes it.

  

      
        
- 
  
    
      #**slice**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    start, length

-> NodeSet or nil  [range] -> NodeSet or nil  slice(index) -> Node or nil  slice(start, length) -> NodeSet or nil  slice(range) -> NodeSet or nil.

  

      
        
- 
  
    
      #**to_a**  ⇒ Object 
    

    
      (also: #to_ary)
    
  
  
  
  
  
  
  
  

  
    

Return this list as an Array.

  

      
        
- 
  
    
      #**to_html**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert this NodeSet to HTML.

  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert this NodeSet to a string.

  

      
        
- 
  
    
      #**to_xhtml**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert this NodeSet to XHTML.

  

      
        
- 
  
    
      #**to_xml**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert this NodeSet to XML.

  

      
        
- 
  
    
      #**unlink**  ⇒ Object 
    

    
      (also: #remove)
    
  
  
  
  
  
  
  
  

  
    

Unlink this NodeSet and all Node objects it contains from their current context.

  

      
        
- 
  
    
      #**wrap**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   wrap(markup) -> self   wrap(node) -> self.

  

      
        
- 
  
    
      #**xpath**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq: xpath *paths, [namespace-bindings, variable-bindings, custom-handler-class].

  

      
        
- 
  
    
      #**|**(node_set)  ⇒ Object 
    

    
      (also: #+)
    
  
  
  
  
  
  
  
  

  
    

Returns a new set built by merging the set and the elements of the given set.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods included from Searchable

  

#>, #at_css, #at_xpath, #search

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, list = []) {|_self| ... } ⇒ NodeSet 
  

  

  

  
    

Create a NodeSet with `document` defaulting to `list`

  

  

Yields:

  
    
- 
      
      
        (_self)
      
      
      
    
  

Yield Parameters:

  
    
- 
      
        _self
      
      
        (Nokogiri::XML::NodeSet)
      
      
      
        —
        

the object that the method was called on

      
    
  

  
    
      

```

22
23
24
25
26
27
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 22

def initialize(document, list = [])
  @document = document
  document.decorate(self)
  list.each { |x| self << x }
  yield self if block_given?
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**document**  ⇒ Object 
  

  

  

  
    

The Document this NodeSet is associated with

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 19

def document
  @document
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**&**(node_set)  ⇒ Object 
  

  

  

  
    

Set Intersection — Returns a new NodeSet containing nodes common to the two NodeSets.

  

  
  

  
    
      

```

205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 205

static VALUE
intersection(VALUE rb_self, VALUE rb_other)
{
  xmlNodeSetPtr c_self, c_other ;
  xmlNodeSetPtr intersection;

  if (!rb_obj_is_kind_of(rb_other, cNokogiriXmlNodeSet)) {
    rb_raise(rb_eArgError, "node_set must be a Nokogiri::XML::NodeSet");
  }

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);
  TypedData_Get_Struct(rb_other, xmlNodeSet, &xml_node_set_type, c_other);

  intersection = xmlXPathIntersection(c_self, c_other);
  return noko_xml_node_set_wrap(intersection, rb_iv_get(rb_self, "@document"));
}

```

    
  

    
      
  
### 
  
    #**-**(node_set)  ⇒ Object 
  

  

  

  
    

Difference - returns a new NodeSet that is a copy of this NodeSet, removing

```
each item that also appears in +node_set+

```

  

  
  

  
    
      

```

277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 277

static VALUE
minus(VALUE rb_self, VALUE rb_other)
{
  xmlNodeSetPtr c_self, c_other;
  xmlNodeSetPtr new;
  int j ;

  if (!rb_obj_is_kind_of(rb_other, cNokogiriXmlNodeSet)) {
    rb_raise(rb_eArgError, "node_set must be a Nokogiri::XML::NodeSet");
  }

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);
  TypedData_Get_Struct(rb_other, xmlNodeSet, &xml_node_set_type, c_other);

  new = xmlXPathNodeSetMerge(NULL, c_self);
  for (j = 0 ; j < c_other->nodeNr ; ++j) {
    xpath_node_set_del(new, c_other->nodeTab[j]);
  }

  return noko_xml_node_set_wrap(new, rb_iv_get(rb_self, "@document"));
}

```

    
  

    
      
  
### 
  
    #**==**(other)  ⇒ Object 
  

  

  

  
    

Equality – Two NodeSets are equal if the contain the same number of elements and if each element is equal to the corresponding element in the other NodeSet

  

  

  
    
      

```

395
396
397
398
399
400
401
402
403
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 395

def ==(other)
  return false unless other.is_a?(Nokogiri::XML::NodeSet)
  return false unless length == other.length

  each_with_index do |node, i|
    return false unless node == other[i]
  end
  true
end

```

    
  

    
      
  
### 
  
    #**[]**(*args)  ⇒ Object 
  

  

  

  
    start, length

-> NodeSet or nil
range

-> NodeSet or nil

```
slice(index) -> Node or nil
slice(start, length) -> NodeSet or nil
slice(range) -> NodeSet or nil

```

Element reference - returns the node at `index`, or returns a NodeSet containing nodes starting at `start` and continuing for `length` elements, or returns a NodeSet containing nodes specified by `range`. Negative `indices` count backward from the end of the `node_set` (-1 is the last node). Returns nil if the `index` (or `start`) are out of range.

  

  

  
    
      

```

354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 354

static VALUE
slice(int argc, VALUE *argv, VALUE rb_self)
{
  VALUE arg ;
  long beg, len ;
  xmlNodeSetPtr c_self;

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);

  if (argc == 2) {
    beg = NUM2LONG(argv[0]);
    len = NUM2LONG(argv[1]);
    if (beg < 0) {
      beg += c_self->nodeNr ;
    }
    return subseq(rb_self, beg, len);
  }

  if (argc != 1) {
    rb_scan_args(argc, argv, "11", NULL, NULL);
  }
  arg = argv[0];

  if (FIXNUM_P(arg)) {
    return index_at(rb_self, FIX2LONG(arg));
  }

  /* if arg is Range */
  switch (rb_range_beg_len(arg, &beg, &len, (long)c_self->nodeNr, 0)) {
    case Qfalse:
      break;
    case Qnil:
      return Qnil;
    default:
      return subseq(rb_self, beg, len);
  }

  return index_at(rb_self, NUM2LONG(arg));
}

```

    
  

    
      
  
### 
  
    #**add_class**(name)  ⇒ Object 
  

  

  

  
    

Add the class attribute `name` to all Node objects in the NodeSet.

See Nokogiri::XML::Node#add_class for more information.

  

  

  
    
      

```

141
142
143
144
145
146
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 141

def add_class(name)
  each do |el|
    el.add_class(name)
  end
  self
end

```

    
  

    
      
  
### 
  
    #**after**(datum)  ⇒ Object 
  

  

  

  
    

Insert `datum` after the last Node in this NodeSet

  

  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 71

def after(datum)
  last.after(datum)
end

```

    
  

    
      
  
### 
  
    #**append_class**(name)  ⇒ Object 
  

  

  

  
    

Append the class attribute `name` to all Node objects in the NodeSet.

See Nokogiri::XML::Node#append_class for more information.

  

  

  
    
      

```

153
154
155
156
157
158
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 153

def append_class(name)
  each do |el|
    el.append_class(name)
  end
  self
end

```

    
  

    
      
  
### 
  
    #**at**(*args)  ⇒ Object 
  

  
    Also known as:
    %
    
  

  

  
    

call-seq: search *paths, [namespace-bindings, xpath-variable-bindings, custom-handler-class]

Search this object for `paths`, and return only the first result. `paths` must be one or more XPath or CSS queries.

See Searchable#search for more information.

Or, if passed an integer, index into the NodeSet:

```
node_set.at(3) # same as node_set[3]

```

  

  

  
    
      

```

121
122
123
124
125
126
127
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 121

def at(*args)
  if args.length == 1 && args.first.is_a?(Numeric)
    return self[args.first]
  end

  super
end

```

    
  

    
      
  
### 
  
    #**attr**(key, value = nil, &block)  ⇒ Object 
  

  
    Also known as:
    set, attribute
    
  

  

  
    

Set attributes on each Node in the NodeSet, or get an attribute from the first Node in the NodeSet.

To get an attribute from the first Node in a NodeSet:

```
node_set.attr("href") # => "https://www.nokogiri.org"

```

Note that an empty NodeSet will return nil when `#attr` is called as a getter.

To set an attribute on each node, `key` can either be an attribute name, or a Hash of attribute names and values. When called as a setter, `#attr` returns the NodeSet.

If `key` is an attribute name, then either `value` or `block` must be passed.

If `key` is a Hash then attributes will be set for each key/value pair:

```
node_set.attr("href" => "https://www.nokogiri.org", "class" => "member")

```

If `value` is passed, it will be used as the attribute value for all nodes:

```
node_set.attr("href", "https://www.nokogiri.org")

```

If `block` is passed, it will be called on each Node object in the NodeSet and the return value used as the attribute value for that node:

```
node_set.attr("class") { |node| node.name }

```

  

  

  
    
      

```

205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 205

def attr(key, value = nil, &block)
  unless key.is_a?(Hash) || (key && (value || block))
    return first&.attribute(key)
  end

  hash = key.is_a?(Hash) ? key : { key => value }

  hash.each do |k, v|
    each do |node|
      node[k] = v || yield(node)
    end
  end

  self
end

```

    
  

    
      
  
### 
  
    #**before**(datum)  ⇒ Object 
  

  

  

  
    

Insert `datum` before the first Node in this NodeSet

  

  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 65

def before(datum)
  first.before(datum)
end

```

    
  

    
      
  
### 
  
    #**children**  ⇒ Object 
  

  

  

  
    

Returns a new NodeSet containing all the children of all the nodes in the NodeSet

  

  

  
    
      

```

408
409
410
411
412
413
414
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 408

def children
  node_set = NodeSet.new(document)
  each do |node|
    node.children.each { |n| node_set.push(n) }
  end
  node_set
end

```

    
  

    
      
  
### 
  
    #**css**(*args)  ⇒ Object 
  

  

  

  
    

call-seq: css *rules, [namespace-bindings, custom-pseudo-class]

Search this node set for CSS `rules`. `rules` must be one or more CSS selectors. For example:

For more information see Nokogiri::XML::Searchable#css

  

  

  
    
      

```

85
86
87
88
89
90
91
92
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 85

def css(*args)
  rules, handler, ns, _ = extract_params(args)
  paths = css_rules_to_xpath(rules, ns)

  inject(NodeSet.new(document)) do |set, node|
    set + xpath_internal(node, paths, handler, ns, nil)
  end
end

```

    
  

    
      
  
### 
  
    #**deconstruct**  ⇒ Object 
  

  

  

  
    

:call-seq: deconstruct() → Array

```
Returns the members of this NodeSet as an array, to use in pattern matching.

Since v1.14.0

```

  

  

  
    
      

```

442
443
444
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 442

def deconstruct
  to_a
end

```

    
  

    
      
  
### 
  
    #**delete**(node)  ⇒ Object 
  

  

  

  
    

Delete `node` from the Nodeset, if it is a member. Returns the deleted node if found, otherwise returns nil.

  

  
  

  
    
      

```

180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 180

static VALUE
delete (VALUE rb_self, VALUE rb_node)
{
  xmlNodeSetPtr c_self;
  xmlNodePtr node;

  Check_Node_Set_Node_Type(rb_node);

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);
  Noko_Node_Get_Struct(rb_node, xmlNode, node);

  if (xmlXPathNodeSetContains(c_self, node)) {
    xpath_node_set_del(c_self, node);
    return rb_node;
  }
  return Qnil ;
}

```

    
  

    
      
  
### 
  
    #**each**  ⇒ Object 
  

  

  

  
    

Iterate over each node, yielding  to `block`

  

  

  
    
      

```

233
234
235
236
237
238
239
240
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 233

def each
  return to_enum unless block_given?

  0.upto(length - 1) do |x|
    yield self[x]
  end
  self
end

```

    
  

    
      
  
### 
  
    #**empty?**  ⇒ Boolean 
  

  

  

  
    

Is this NodeSet empty?

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

47
48
49
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 47

def empty?
  length == 0
end

```

    
  

    
      
  
### 
  
    #**filter**(expr)  ⇒ Object 
  

  

  

  
    

Filter this list for nodes that match `expr`

  

  

  
    
      

```

132
133
134
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 132

def filter(expr)
  find_all { |node| node.matches?(expr) }
end

```

    
  

    
      
  
### 
  
    #**first**(n = nil)  ⇒ Object 
  

  

  

  
    

Get the first element of the NodeSet.

  

  

  
    
      

```

31
32
33
34
35
36
37
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 31

def first(n = nil)
  return self[0] unless n

  list = []
  [n, length].min.times { |i| list << self[i] }
  list
end

```

    
  

    
      
  
### 
  
    #**include?**(node)  ⇒ Boolean 
  

  

  

  
    

Returns true if any member of node set equals `node`.

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

229
230
231
232
233
234
235
236
237
238
239
240
241
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 229

static VALUE
include_eh(VALUE rb_self, VALUE rb_node)
{
  xmlNodeSetPtr c_self;
  xmlNodePtr node;

  Check_Node_Set_Node_Type(rb_node);

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);
  Noko_Node_Get_Struct(rb_node, xmlNode, node);

  return (xmlXPathNodeSetContains(c_self, node) ? Qtrue : Qfalse);
}

```

    
  

    
      
  
### 
  
    #**index**(node = nil)  ⇒ Object 
  

  

  

  
    

Returns the index of the first node in self that is == to `node` or meets the given block. Returns nil if no match is found.

  

  

  
    
      

```

53
54
55
56
57
58
59
60
61
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 53

def index(node = nil)
  if node
    warn("given block not used") if block_given?
    each_with_index { |member, j| return j if member == node }
  elsif block_given?
    each_with_index { |member, j| return j if yield(member) }
  end
  nil
end

```

    
  

    
      
  
### 
  
    #**inner_html**(*args)  ⇒ Object 
  

  

  

  
    

Get the inner html of all contained Node objects

  

  

  
    
      

```

262
263
264
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 262

def inner_html(*args)
  collect { |j| j.inner_html(*args) }.join("")
end

```

    
  

    
      
  
### 
  
    #**inner_text**  ⇒ Object 
  

  
    Also known as:
    text
    
  

  

  
    

Get the inner text of all contained Node objects

Note: This joins the text of all Node objects in the NodeSet:

```
doc = Nokogiri::XML('<xml><a><d>foo</d><d>bar</d></a></xml>')
doc.css('d').text # => "foobar"

```

Instead, if you want to return the text of all nodes in the NodeSet:

```
doc.css('d').map(&:text) # => ["foo", "bar"]

```

See Nokogiri::XML::Node#content for more information.

  

  

  
    
      

```

255
256
257
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 255

def inner_text
  collect(&:inner_text).join("")
end

```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

Return a nicely formatted string representation

  

  

  
    
      

```

429
430
431
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 429

def inspect
  "[#{map(&:inspect).join(", ")}]"
end

```

    
  

    
      
  
### 
  
    #**last**  ⇒ Object 
  

  

  

  
    

Get the last element of the NodeSet.

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 41

def last
  self[-1]
end

```

    
  

    
      
  
### 
  
    #**length**  ⇒ Object 
  

  
    Also known as:
    size
    
  

  

  
    

Get the length of the node set

  

  
  

  
    
      

```

141
142
143
144
145
146
147
148
149
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 141

static VALUE
length(VALUE rb_self)
{
  xmlNodeSetPtr c_self;

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);

  return c_self ? INT2NUM(c_self->nodeNr) : INT2NUM(0);
}

```

    
  

    
      
  
### 
  
    #**pop**  ⇒ Object 
  

  

  

  
    

Removes the last element from set and returns it, or `nil` if the set is empty

  

  

  
    
      

```

376
377
378
379
380
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 376

def pop
  return if length == 0

  delete(last)
end

```

    
  

    
      
  
### 
  
    #**push**(node)  ⇒ Object 
  

  
    Also known as:
    <<
    
  

  

  
    

Append `node` to the NodeSet.

  

  
  

  
    
      

```

157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 157

static VALUE
push(VALUE rb_self, VALUE rb_node)
{
  xmlNodeSetPtr c_self;
  xmlNodePtr node;

  Check_Node_Set_Node_Type(rb_node);

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);
  Noko_Node_Get_Struct(rb_node, xmlNode, node);

  xmlXPathNodeSetAdd(c_self, node);

  return rb_self;
}

```

    
  

    
      
  
### 
  
    #**remove_attr**(name)  ⇒ Object 
  

  
    Also known as:
    remove_attribute
    
  

  

  
    

Remove the attributed named `name` from all Node objects in the NodeSet

  

  

  
    
      

```

225
226
227
228
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 225

def remove_attr(name)
  each { |el| el.delete(name) }
  self
end

```

    
  

    
      
  
### 
  
    #**remove_class**(name = nil)  ⇒ Object 
  

  

  

  
    

Remove the class attribute `name` from all Node objects in the NodeSet.

See Nokogiri::XML::Node#remove_class for more information.

  

  

  
    
      

```

165
166
167
168
169
170
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 165

def remove_class(name = nil)
  each do |el|
    el.remove_class(name)
  end
  self
end

```

    
  

    
      
  
### 
  
    #**reverse**  ⇒ Object 
  

  

  

  
    

Returns a new NodeSet containing all the nodes in the NodeSet in reverse order

  

  

  
    
      

```

419
420
421
422
423
424
425
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 419

def reverse
  node_set = NodeSet.new(document)
  (length - 1).downto(0) do |x|
    node_set.push(self[x])
  end
  node_set
end

```

    
  

    
      
  
### 
  
    #**shift**  ⇒ Object 
  

  

  

  
    

Returns the first element of the NodeSet and removes it.  Returns `nil` if the set is empty.

  

  

  
    
      

```

385
386
387
388
389
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 385

def shift
  return if length == 0

  delete(first)
end

```

    
  

    
      
  
### 
  
    #**slice**(*args)  ⇒ Object 
  

  

  

  
    start, length

-> NodeSet or nil
range

-> NodeSet or nil

```
slice(index) -> Node or nil
slice(start, length) -> NodeSet or nil
slice(range) -> NodeSet or nil

```

Element reference - returns the node at `index`, or returns a NodeSet containing nodes starting at `start` and continuing for `length` elements, or returns a NodeSet containing nodes specified by `range`. Negative `indices` count backward from the end of the `node_set` (-1 is the last node). Returns nil if the `index` (or `start`) are out of range.

  

  

  
    
      

```

354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 354

static VALUE
slice(int argc, VALUE *argv, VALUE rb_self)
{
  VALUE arg ;
  long beg, len ;
  xmlNodeSetPtr c_self;

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);

  if (argc == 2) {
    beg = NUM2LONG(argv[0]);
    len = NUM2LONG(argv[1]);
    if (beg < 0) {
      beg += c_self->nodeNr ;
    }
    return subseq(rb_self, beg, len);
  }

  if (argc != 1) {
    rb_scan_args(argc, argv, "11", NULL, NULL);
  }
  arg = argv[0];

  if (FIXNUM_P(arg)) {
    return index_at(rb_self, FIX2LONG(arg));
  }

  /* if arg is Range */
  switch (rb_range_beg_len(arg, &beg, &len, (long)c_self->nodeNr, 0)) {
    case Qfalse:
      break;
    case Qnil:
      return Qnil;
    default:
      return subseq(rb_self, beg, len);
  }

  return index_at(rb_self, NUM2LONG(arg));
}

```

    
  

    
      
  
### 
  
    #**to_a**  ⇒ Object 
  

  
    Also known as:
    to_ary
    
  

  

  
    

Return this list as an Array

  

  
  

  
    
      

```

401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 401

static VALUE
to_array(VALUE rb_self)
{
  xmlNodeSetPtr c_self ;
  VALUE list;
  int i;

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);

  list = rb_ary_new2(c_self->nodeNr);
  for (i = 0; i < c_self->nodeNr; i++) {
    VALUE elt = noko_xml_node_wrap_node_set_result(c_self->nodeTab[i], rb_self);
    rb_ary_push(list, elt);
  }

  return list;
}

```

    
  

    
      
  
### 
  
    #**to_html**(*args)  ⇒ Object 
  

  

  

  
    

Convert this NodeSet to HTML

  

  

  
    
      

```

343
344
345
346
347
348
349
350
351
352
353
354
355
356
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 343

def to_html(*args)
  if Nokogiri.jruby?
    options = args.first.is_a?(Hash) ? args.shift : {}
    options[:save_with] ||= Node::SaveOptions::DEFAULT_HTML
    args.insert(0, options)
  end
  if empty?
    encoding = (args.first.is_a?(Hash) ? args.first[:encoding] : nil)
    encoding ||= document.encoding
    encoding.nil? ? "" : "".encode(encoding)
  else
    map { |x| x.to_html(*args) }.join
  end
end

```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    

Convert this NodeSet to a string.

  

  

  
    
      

```

337
338
339
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 337

def to_s
  map(&:to_s).join
end

```

    
  

    
      
  
### 
  
    #**to_xhtml**(*args)  ⇒ Object 
  

  

  

  
    

Convert this NodeSet to XHTML

  

  

  
    
      

```

360
361
362
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 360

def to_xhtml(*args)
  map { |x| x.to_xhtml(*args) }.join
end

```

    
  

    
      
  
### 
  
    #**to_xml**(*args)  ⇒ Object 
  

  

  

  
    

Convert this NodeSet to XML

  

  

  
    
      

```

366
367
368
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 366

def to_xml(*args)
  map { |x| x.to_xml(*args) }.join
end

```

    
  

    
      
  
### 
  
    #**unlink**  ⇒ Object 
  

  
    Also known as:
    remove
    
  

  

  
    

Unlink this NodeSet and all Node objects it contains from their current context.

  

  
  

  
    
      

```

425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 425

static VALUE
unlink_nodeset(VALUE rb_self)
{
  xmlNodeSetPtr c_self;
  int j, nodeNr ;

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);

  nodeNr = c_self->nodeNr ;
  for (j = 0 ; j < nodeNr ; j++) {
    if (! NOKOGIRI_NAMESPACE_EH(c_self->nodeTab[j])) {
      VALUE node ;
      xmlNodePtr node_ptr;
      node = noko_xml_node_wrap(Qnil, c_self->nodeTab[j]);
      rb_funcall(node, rb_intern("unlink"), 0); /* modifies the C struct out from under the object */
      Noko_Node_Get_Struct(node, xmlNode, node_ptr);
      c_self->nodeTab[j] = node_ptr ;
    }
  }
  return rb_self ;
}

```

    
  

    
      
  
### 
  
    #**wrap**(node_or_tags)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
wrap(markup) -> self
wrap(node) -> self

```

Wrap each member of this NodeSet with the node parsed from `markup` or a dup of the `node`.
Parameters

- 

**markup** (String) Markup that is parsed, once per member of the NodeSet, and used as the wrapper. Each node’s parent, if it exists, is used as the context node for parsing; otherwise the associated document is used. If the parsed fragment has multiple roots, the first root node is used as the wrapper.

- 

**node** (Nokogiri::XML::Node) An element that is ‘#dup`ed and used as the wrapper.

Returns

`self`, to support chaining.

⚠ Note that if a `String` is passed, the markup will be parsed **once per node** in the NodeSet. You can avoid this overhead in cases where you know exactly the wrapper you wish to use by passing a `Node` instead.

Also see Node#wrap

**Example** with a `String` argument:

```
doc = Nokogiri::HTML5("<html><body>\n  <a>a</a>\n  <a>b</a>\n  <a>c</a>\n  <a>d</a>\n</body></html>\n")
doc.css("a").wrap("<div></div>")
doc.to_html
# => <html><head></head><body>
#      <div><a>a</a></div>
#      <div><a>b</a></div>
#      <div><a>c</a></div>
#      <div><a>d</a></div>
#    </body></html>

```

**Example** with a `Node` argument

💡 Note that this is faster than the equivalent call passing a `String` because it avoids having to reparse the wrapper markup for each node.

```
doc = Nokogiri::HTML5("<html><body>\n  <a>a</a>\n  <a>b</a>\n  <a>c</a>\n  <a>d</a>\n</body></html>\n")
doc.css("a").wrap(doc.create_element("div"))
doc.to_html
# => <html><head></head><body>
#      <div><a>a</a></div>
#      <div><a>b</a></div>
#      <div><a>c</a></div>
#      <div><a>d</a></div>
#    </body></html>

```

  

  

  
    
      

```

330
331
332
333
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 330

def wrap(node_or_tags)
  map { |node| node.wrap(node_or_tags) }
  self
end

```

    
  

    
      
  
### 
  
    #**xpath**(*args)  ⇒ Object 
  

  

  

  
    

call-seq: xpath *paths, [namespace-bindings, variable-bindings, custom-handler-class]

Search this node set for XPath `paths`. `paths` must be one or more XPath queries.

For more information see Nokogiri::XML::Searchable#xpath

  

  

  
    
      

```

101
102
103
104
105
106
107
```

    
    
      

```
# File 'lib/nokogiri/xml/node_set.rb', line 101

def xpath(*args)
  paths, handler, ns, binds = extract_params(args)

  inject(NodeSet.new(document)) do |set, node|
    set + xpath_internal(node, paths, handler, ns, binds)
  end
end

```

    
  

    
      
  
### 
  
    #**|**(node_set)  ⇒ Object 
  

  
    Also known as:
    +
    
  

  

  
    

Returns a new set built by merging the set and the elements of the given set.

  

  
  

  
    
      

```

251
252
253
254
255
256
257
258
259
260
261
262
263
264
265
266
267
268
```

    
    
      

```
# File 'ext/nokogiri/xml_node_set.c', line 251

static VALUE
rb_xml_node_set_union(VALUE rb_self, VALUE rb_other)
{
  xmlNodeSetPtr c_self, c_other;
  xmlNodeSetPtr c_new_node_set;

  if (!rb_obj_is_kind_of(rb_other, cNokogiriXmlNodeSet)) {
    rb_raise(rb_eArgError, "node_set must be a Nokogiri::XML::NodeSet");
  }

  TypedData_Get_Struct(rb_self, xmlNodeSet, &xml_node_set_type, c_self);
  TypedData_Get_Struct(rb_other, xmlNodeSet, &xml_node_set_type, c_other);

  c_new_node_set = xmlXPathNodeSetMerge(NULL, c_self);
  c_new_node_set = xmlXPathNodeSetMerge(c_new_node_set, c_other);

  return noko_xml_node_set_wrap(c_new_node_set, rb_iv_get(rb_self, "@document"));
}

```