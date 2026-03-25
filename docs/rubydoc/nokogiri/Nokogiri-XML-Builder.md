# Class: Nokogiri::XML::Builder
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::Builder
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      ClassResolver
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/builder.rb
  
  

## Overview

  
    

Nokogiri builder can be used for building XML and HTML documents.

## Synopsis:

```
builder = Nokogiri::XML::Builder.new do |xml|
  xml.root {
    xml.products {
      xml.widget {
        xml.id_ "10"
        xml.name "Awesome widget"
      }
    }
  }
end
puts builder.to_xml

```

Will output:

```
<?xml version="1.0"?>
<root>
  <products>
    <widget>
      <id>10</id>
      <name>Awesome widget</name>
    </widget>
  </products>
</root>

```

### Builder scope

The builder allows two forms.  When the builder is supplied with a block that has a parameter, the outside scope is maintained.  This means you can access variables that are outside your builder.  If you don’t need outside scope, you can use the builder without the “xml” prefix like this:

```
builder = Nokogiri::XML::Builder.new do
  root {
    products {
      widget {
        id_ "10"
        name "Awesome widget"
      }
    }
  }
end

```

## Special Tags

The builder works by taking advantage of method_missing.  Unfortunately some methods are defined in ruby that are difficult or dangerous to remove.  You may want to create tags with the name “type”, “class”, and “id” for example.  In that case, you can use an underscore to disambiguate your tag name from the method call.

Here is an example of using the underscore to disambiguate tag names from ruby methods:

```
@objects = [Object.new, Object.new, Object.new]

builder = Nokogiri::XML::Builder.new do |xml|
  xml.root {
    xml.objects {
      @objects.each do |o|
        xml.object {
          xml.type_   o.type
          xml.class_  o.class.name
          xml.id_     o.id
        }
      end
    }
  }
end
puts builder.to_xml

```

The underscore may be used with any tag name, and the last underscore will just be removed.  This code will output the following XML:

```
<?xml version="1.0"?>
<root>
  <objects>
    <object>
      <type>Object</type>
      <class>Object</class>
      <id>48390</id>
    </object>
    <object>
      <type>Object</type>
      <class>Object</class>
      <id>48380</id>
    </object>
    <object>
      <type>Object</type>
      <class>Object</class>
      <id>48370</id>
    </object>
  </objects>
</root>

```

## Tag Attributes

Tag attributes may be supplied as method arguments.  Here is our previous example, but using attributes rather than tags:

```
@objects = [Object.new, Object.new, Object.new]

builder = Nokogiri::XML::Builder.new do |xml|
  xml.root {
    xml.objects {
      @objects.each do |o|
        xml.object(:type => o.type, :class => o.class, :id => o.id)
      end
    }
  }
end
puts builder.to_xml

```

### Tag Attribute Short Cuts

A couple attribute short cuts are available when building tags.  The short cuts are available by special method calls when building a tag.

This example builds an “object” tag with the class attribute “classy” and the id of “thing”:

```
builder = Nokogiri::XML::Builder.new do |xml|
  xml.root {
    xml.objects {
      xml.object.classy.thing!
    }
  }
end
puts builder.to_xml

```

Which will output:

```
<?xml version="1.0"?>
<root>
  <objects>
    <object class="classy" id="thing"/>
  </objects>
</root>

```

All other options are still supported with this syntax, including blocks and extra tag attributes.

## Namespaces

Namespaces are added similarly to attributes.  Nokogiri::XML::Builder assumes that when an attribute starts with “xmlns”, it is meant to be a namespace:

```
builder = Nokogiri::XML::Builder.new { |xml|
  xml.root('xmlns' => 'default', 'xmlns:foo' => 'bar') do
    xml.tenderlove
  end
}
puts builder.to_xml

```

Will output XML like this:

```
<?xml version="1.0"?>
<root xmlns:foo="bar" xmlns="default">
  <tenderlove/>
</root>

```

### Referencing declared namespaces

Tags that reference non-default namespaces (i.e. a tag “foo:bar”) can be built by using the Nokogiri::XML::Builder#[] method.

For example:

```
builder = Nokogiri::XML::Builder.new do |xml|
  xml.root('xmlns:foo' => 'bar') {
    xml.objects {
      xml['foo'].object.classy.thing!
    }
  }
end
puts builder.to_xml

```

Will output this XML:

```
<?xml version="1.0"?>
<root xmlns:foo="bar">
  <objects>
    <foo:object class="classy" id="thing"/>
  </objects>
</root>

```

Note the “foo:object” tag.

### Namespace inheritance

In the Builder context, children will inherit their parent’s namespace. This is the same behavior as if the underlying Document set `namespace_inheritance` to `true`:

```
result = Nokogiri::XML::Builder.new do |xml|
  xml["soapenv"].Envelope("xmlns:soapenv" => "http://schemas.xmlsoap.org/soap/envelope/") do
    xml.Header
  end
end
result.doc.to_xml
# => <?xml version="1.0" encoding="utf-8"?>
#    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
#      <soapenv:Header/>
#    </soapenv:Envelope>

```

Users may turn this behavior off by passing a keyword argument `namespace_inheritance:false` to the initializer:

```
result = Nokogiri::XML::Builder.new(namespace_inheritance: false) do |xml|
  xml["soapenv"].Envelope("xmlns:soapenv" => "http://schemas.xmlsoap.org/soap/envelope/") do
    xml.Header
    xml["soapenv"].Body # users may explicitly opt into the namespace
  end
end
result.doc.to_xml
# => <?xml version="1.0" encoding="utf-8"?>
#    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
#      <Header/>
#      <soapenv:Body/>
#    </soapenv:Envelope>

```

For more information on namespace inheritance, please see Document#namespace_inheritance

## Document Types

To create a document type (DTD), use the Builder#doc method to get the current context document.  Then call Node#create_internal_subset to create the DTD node.

For example, this Ruby:

```
builder = Nokogiri::XML::Builder.new do |xml|
  xml.doc.create_internal_subset(
    'html',
    "-//W3C//DTD HTML 4.01 Transitional//EN",
    "http://www.w3.org/TR/html4/loose.dtd"
  )
  xml.root do
    xml.foo
  end
end

puts builder.to_xml

```

Will output this xml:

```
<?xml version="1.0"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<root>
  <foo/>
</root>

```

  

  

  
## Direct Known Subclasses

  

HTML4::Builder, HTML5::Builder, HTML::Builder

## Defined Under Namespace

  
    
  
    
      **Classes:** NodeBuilder
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DEFAULT_DOCUMENT_OPTIONS =
          
        
        

```
{ namespace_inheritance: true }

```

      
    
  

  
  
  
### Constants included
     from ClassResolver

  

ClassResolver::VALID_NAMESPACES

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**arity**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

:nodoc:.

  

    
      
- 
  
    
      #**context**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

A context object for use when the block has no arguments.

  

    
      
- 
  
    
      #**doc**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The current Document object being built.

  

    
      
- 
  
    
      #**parent**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The parent of the current node being built.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**with**(root, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a builder with an existing root object.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**<<**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Append the given raw XML `string` to the document.

  

      
        
- 
  
    
      #**[]**(ns)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Build a tag that is associated with namespace `ns`.

  

      
        
- 
  
    
      #**cdata**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a CDATA Node with content of `string`.

  

      
        
- 
  
    
      #**comment**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a Comment Node with content of `string`.

  

      
        
- 
  
    
      #**initialize**(options = {}, root = nil, &block)  ⇒ Builder 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Create a new Builder object.

  

      
        
- 
  
    
      #**method_missing**(method, *args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**text**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a Text Node with content of `string`.

  

      
        
- 
  
    
      #**to_xml**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert this Builder object to XML.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(options = {}, root = nil, &block)  ⇒ Builder 
  

  

  

  
    

Create a new Builder object.  `options` are sent to the top level Document that is being built.

Building a document with a particular encoding for example:

```
Nokogiri::XML::Builder.new(:encoding => 'UTF-8') do |xml|
  ...
end

```

  

  

  
    
      

```

307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 307

def initialize(options = {}, root = nil, &block)
  if root
    @doc = root.document
    @parent = root
  else
    @parent = @doc = related_class("Document").new
  end

  @context = nil
  @arity = nil
  @ns = nil

  options = DEFAULT_DOCUMENT_OPTIONS.merge(options)
  options.each do |k, v|
    @doc.send(:"#{k}=", v)
  end

  return unless block

  @arity = block.arity
  if @arity <= 0
    @context = eval("self", block.binding)
    instance_eval(&block)
  else
    yield self
  end

  @parent = @doc
end

```

    
  

  

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
### 
  
    #**method_missing**(method, *args, &block)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

394
395
396
397
398
399
400
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
# File 'lib/nokogiri/xml/builder.rb', line 394

def method_missing(method, *args, &block) # :nodoc:
  if @context&.respond_to?(method)
    @context.send(method, *args, &block)
  else
    node = @doc.create_element(method.to_s.sub(/[_!]$/, ""), *args) do |n|
      # Set up the namespace
      if @ns.is_a?(Nokogiri::XML::Namespace)
        n.namespace = @ns
        @ns = nil
      end
    end

    if @ns.is_a?(Hash)
      node.namespace = node.namespace_definitions.find { |x| x.prefix == @ns[:pending] }
      if node.namespace.nil?
        raise ArgumentError, "Namespace #{@ns[:pending]} has not been defined"
      end

      @ns = nil
    end

    insert(node, &block)
  end
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**arity**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

278
279
280
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 278

def arity
  @arity
end

```

    
  

    
      
      
      
  
### 
  
    #**context**  ⇒ Object 
  

  

  

  
    

A context object for use when the block has no arguments

  

  

  
    
      

```

276
277
278
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 276

def context
  @context
end

```

    
  

    
      
      
      
  
### 
  
    #**doc**  ⇒ Object 
  

  

  

  
    

The current Document object being built

  

  

  
    
      

```

270
271
272
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 270

def doc
  @doc
end

```

    
  

    
      
      
      
  
### 
  
    #**parent**  ⇒ Object 
  

  

  

  
    

The parent of the current node being built

  

  

  
    
      

```

273
274
275
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 273

def parent
  @parent
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**with**(root, &block)  ⇒ Object 
  

  

  

  
    

Create a builder with an existing root object.  This is for use when you have an existing document that you would like to augment with builder methods.  The builder context created will start with the given `root` node.

For example:

```
doc = Nokogiri::XML(File.read('somedoc.xml'))
Nokogiri::XML::Builder.with(doc.at_css('some_tag')) do |xml|
  # ... Use normal builder methods here ...
  xml.awesome # add the "awesome" tag below "some_tag"
end

```

  

  

  
    
      

```

294
295
296
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 294

def self.with(root, &block)
  new({}, root, &block)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**<<**(string)  ⇒ Object 
  

  

  

  
    

Append the given raw XML `string` to the document

  

  

  
    
      

```

390
391
392
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 390

def <<(string)
  @doc.fragment(string).children.each { |x| insert(x) }
end

```

    
  

    
      
  
### 
  
    #**[]**(ns)  ⇒ Object 
  

  

  

  
    

Build a tag that is associated with namespace `ns`.  Raises an ArgumentError if `ns` has not been defined higher in the tree.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 358

def [](ns)
  if @parent != @doc
    @ns = @parent.namespace_definitions.find { |x| x.prefix == ns.to_s }
  end
  return self if @ns

  @parent.ancestors.each do |a|
    next if a == doc

    @ns = a.namespace_definitions.find { |x| x.prefix == ns.to_s }
    return self if @ns
  end

  @ns = { pending: ns.to_s }
  self
end

```

    
  

    
      
  
### 
  
    #**cdata**(string)  ⇒ Object 
  

  

  

  
    

Create a CDATA Node with content of `string`

  

  

  
    
      

```

345
346
347
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 345

def cdata(string)
  insert(doc.create_cdata(string))
end

```

    
  

    
      
  
### 
  
    #**comment**(string)  ⇒ Object 
  

  

  

  
    

Create a Comment Node with content of `string`

  

  

  
    
      

```

351
352
353
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 351

def comment(string)
  insert(doc.create_comment(string))
end

```

    
  

    
      
  
### 
  
    #**text**(string)  ⇒ Object 
  

  

  

  
    

Create a Text Node with content of `string`

  

  

  
    
      

```

339
340
341
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 339

def text(string)
  insert(@doc.create_text_node(string))
end

```

    
  

    
      
  
### 
  
    #**to_xml**(*args)  ⇒ Object 
  

  

  

  
    

Convert this Builder object to XML

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 377

def to_xml(*args)
  if Nokogiri.jruby?
    options = args.first.is_a?(Hash) ? args.shift : {}
    unless options[:save_with]
      options[:save_with] = Node::SaveOptions::AS_BUILDER
    end
    args.insert(0, options)
  end
  @doc.to_xml(*args)
end

```