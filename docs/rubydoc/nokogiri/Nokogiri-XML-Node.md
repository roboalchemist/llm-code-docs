# Class: Nokogiri::XML::Node
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::Node
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Enumerable, ClassResolver, HTML5::Node, PP::Node, Searchable
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/node.rb,

  lib/nokogiri/xml/node/save_options.rb,
 ext/nokogiri/xml_node.c

  
  

## Overview

  
    

Nokogiri::XML::Node is the primary API you’ll use to interact with your Document.

## Attributes

A Nokogiri::XML::Node may be treated similarly to a hash with regard to attributes. For example:

```
node = Nokogiri::XML::DocumentFragment.parse("<a href='#foo' id='link'>link</a>").at_css("a")
node.to_html # => "<a href=\"#foo\" id=\"link\">link</a>"
node['href'] # => "#foo"
node.keys # => ["href", "id"]
node.values # => ["#foo", "link"]
node['class'] = 'green' # => "green"
node.to_html # => "<a href=\"#foo\" id=\"link\" class=\"green\">link</a>"

```

See the method group entitled Node@Working+With+Node+Attributes for the full set of methods.

## Navigation

Nokogiri::XML::Node also has methods that let you move around your tree:
#parent, #children, #next, #previous

Navigate up, down, or through siblings.

See the method group entitled Node@Traversing+Document+Structure for the full set of methods.

## Serialization

When printing or otherwise emitting a document or a node (and its subtree), there are a few methods you might want to use:
#content, #text, #inner_text, #to_str

These methods will all **emit plaintext**, meaning that entities will be replaced (e.g., < will be replaced with <), meaning that any sanitizing will likely be un-done in the output.
#to_s, #to_xml, #to_html, #inner_html

These methods will all **emit properly-escaped markup**, meaning that it’s suitable for consumption by browsers, parsers, etc.

See the method group entitled Node@Serialization+and+Generating+Output for the full set of methods.

## Searching

You may search this node’s subtree using methods like #xpath and #css.

See the method group entitled Node@Searching+via+XPath+or+CSS+Queries for the full set of methods.

  

  

  
## Direct Known Subclasses

  

AttributeDecl, DTD, Document, DocumentFragment, ElementDecl, EntityDecl, EntityReference, ProcessingInstruction

## Defined Under Namespace

  
    
  
    
      **Classes:** SaveOptions
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ELEMENT_NODE =
          
  
    

Element node type, see Nokogiri::XML::Node#element?

  

  

        
        

```
1
```

      
        ATTRIBUTE_NODE =
          
  
    

Attribute node type

  

  

        
        

```
2
```

      
        TEXT_NODE =
          
  
    

Text node type, see Nokogiri::XML::Node#text?

  

  

        
        

```
3
```

      
        CDATA_SECTION_NODE =
          
  
    

CDATA node type, see Nokogiri::XML::Node#cdata?

  

  

        
        

```
4
```

      
        ENTITY_REF_NODE =
          
  
    

Entity reference node type

  

  

        
        

```
5
```

      
        ENTITY_NODE =
          
  
    

Entity node type

  

  

        
        

```
6
```

      
        PI_NODE =
          
  
    

PI node type

  

  

        
        

```
7
```

      
        COMMENT_NODE =
          
  
    

Comment node type, see Nokogiri::XML::Node#comment?

  

  

        
        

```
8
```

      
        DOCUMENT_NODE =
          
  
    

Document node type, see Nokogiri::XML::Node#xml?

  

  

        
        

```
9
```

      
        DOCUMENT_TYPE_NODE =
          
  
    

Document type node type

  

  

        
        

```
10
```

      
        DOCUMENT_FRAG_NODE =
          
  
    

Document fragment node type

  

  

        
        

```
11
```

      
        NOTATION_NODE =
          
  
    

Notation node type

  

  

        
        

```
12
```

      
        HTML_DOCUMENT_NODE =
          
  
    

HTML document node type, see Nokogiri::XML::Node#html?

  

  

        
        

```
13
```

      
        DTD_NODE =
          
  
    

DTD node type

  

  

        
        

```
14
```

      
        ELEMENT_DECL =
          
  
    

Element declaration type

  

  

        
        

```
15
```

      
        ATTRIBUTE_DECL =
          
  
    

Attribute declaration type

  

  

        
        

```
16
```

      
        ENTITY_DECL =
          
  
    

Entity declaration type

  

  

        
        

```
17
```

      
        NAMESPACE_DECL =
          
  
    

Namespace declaration type

  

  

        
        

```
18
```

      
        XINCLUDE_START =
          
  
    

XInclude start type

  

  

        
        

```
19
```

      
        XINCLUDE_END =
          
  
    

XInclude end type

  

  

        
        

```
20
```

      
        DOCB_DOCUMENT_NODE =
          
  
    

DOCB document node type

  

  

        
        

```
21
```

      
        DECONSTRUCT_KEYS =
          
  
    

:nodoc:

  

  

        
        

```
[:name, :attributes, :children, :namespace, :content, :elements, :inner_html].freeze
```

      
        DECONSTRUCT_METHODS =
          
  
    

:nodoc:

  

  

        
        

```
{ attributes: :attribute_nodes }.freeze
```

      
    
  

  
  
  
### Constants included
     from ClassResolver

  

ClassResolver::VALID_NAMESPACES

  
  
  
### Constants included
     from Searchable

  

Searchable::LOOKS_LIKE_XPATH

  
  
  
### Constants included
     from PP::Node

  

PP::Node::COLLECTIONS

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**new**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc: documented in lib/nokogiri/xml/node.rb.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**<<**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add `node_or_tags` as a child of this Node.

  

      
        
- 
  
    
      #**<=>**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Compare two Node objects with respect to their Document.

  

      
        
- 
  
    
      #**==**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Test to see if this Node is equal to `other`.

  

      
        
- 
  
    
      #**[]**(name)  ⇒ Object 
    

    
      (also: #get_attribute, #attr)
    
  
  
  
  
  
  
  
  

  
    

:call-seq: [](name) → (String, nil).

  

      
        
- 
  
    
      #**[]=**(name, value)  ⇒ Object 
    

    
      (also: #set_attribute)
    
  
  
  
  
  
  
  
  

  
    

:call-seq: []=(name, value) → value.

  

      
        
- 
  
    
      #**accept**(visitor)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Accept a visitor.

  

      
        
- 
  
    
      #**add_child**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add `node_or_tags` as a child of this Node.

  

      
        
- 
  
    
      #**add_class**(names)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: add_class(names) → self.

  

      
        
- 
  
    
      #**add_namespace_definition**(rb_prefix, rb_href)  ⇒ Object 
    

    
      (also: #add_namespace)
    
  
  
  
  
  
  
  
  

  
    

:call-seq:   add_namespace_definition(prefix, href) → Nokogiri::XML::Namespace   add_namespace(prefix, href) → Nokogiri::XML::Namespace.

  

      
        
- 
  
    
      #**add_next_sibling**(node_or_tags)  ⇒ Object 
    

    
      (also: #next=)
    
  
  
  
  
  
  
  
  

  
    

Insert `node_or_tags` after this Node (as a sibling).

  

      
        
- 
  
    
      #**add_previous_sibling**(node_or_tags)  ⇒ Object 
    

    
      (also: #previous=)
    
  
  
  
  
  
  
  
  

  
    

Insert `node_or_tags` before this Node (as a sibling).

  

      
        
- 
  
    
      #**after**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Insert `node_or_tags` after this node (as a sibling).

  

      
        
- 
  
    
      #**ancestors**(selector = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get a list of ancestor Node for this Node.

  

      
        
- 
  
    
      #**append_class**(names)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: append_class(names) → self.

  

      
        
- 
  
    
      #**attribute**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: attribute(name) → Nokogiri::XML::Attr.

  

      
        
- 
  
    
      #**attribute_nodes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: attribute_nodes() → Array<Nokogiri::XML::Attr>.

  

      
        
- 
  
    
      #**attribute_with_ns**(name, namespace)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: attribute_with_ns(name, namespace) → Nokogiri::XML::Attr.

  

      
        
- 
  
    
      #**attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: attributes() → Hash<String ⇒ Nokogiri::XML::Attr>.

  

      
        
- 
  
    
      #**before**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Insert `node_or_tags` before this node (as a sibling).

  

      
        
- 
  
    
      #**blank?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    Returns

`true` if the node is an empty or whitespace-only text or cdata node, else `false`.

  

      
        
- 
  
    
      #**canonicalize**(mode = XML::XML_C14N_1_0, inclusive_namespaces = nil, with_comments = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**cdata?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if this is a CDATA.

  

      
        
- 
  
    
      #**child**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: child() → Nokogiri::XML::Node.

  

      
        
- 
  
    
      #**children**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: children() → Nokogiri::XML::NodeSet.

  

      
        
- 
  
    
      #**children=**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the content for this Node `node_or_tags`.

  

      
        
- 
  
    
      #**classes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: classes() → Array<String>.

  

      
        
- 
  
    
      #**clone**(level = 1, new_parent_doc = document)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   clone → Nokogiri::XML::Node   clone(level) → Nokogiri::XML::Node   clone(level, new_parent_doc) → Nokogiri::XML::Node.

  

      
        
- 
  
    
      #**comment?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if this is a Comment.

  

      
        
- 
  
    
      #**content**  ⇒ Object 
    

    
      (also: #inner_text, #text, #to_str)
    
  
  
  
  
  
  
  
  

  
    

:call-seq:   content() → String   inner_text() → String   text() → String   to_str() → String.

  

      
        
- 
  
    
      #**content=**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq:   content=(input).

  

      
        
- 
  
    
      #**create_external_subset**(name, external_id, system_id)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   create_external_subset(name, external_id, system_id).

  

      
        
- 
  
    
      #**create_internal_subset**(name, external_id, system_id)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   create_internal_subset(name, external_id, system_id).

  

      
        
- 
  
    
      #**css_path**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the path to this node as a CSS expression.

  

      
        
- 
  
    
      #**data_ptr?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**deconstruct_keys**(keys)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: deconstruct_keys(array_of_names) → Hash.

  

      
        
- 
  
    
      #**decorate!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Decorate this node with the decorators set up in this node’s Document.

  

      
        
- 
  
    
      #**default_namespace=**(url)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Adds a default namespace supplied as a string `url` href, to self.

  

      
        
- 
  
    
      #**description**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Fetch the Nokogiri::HTML4::ElementDescription for this node.

  

      
        
- 
  
    
      #**do_xinclude**(options = XML::ParseOptions::DEFAULT_XML) {|options| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Do xinclude substitution on the subtree below node.

  

      
        
- 
  
    
      #**document**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: document() → Nokogiri::XML::Document.

  

      
        
- 
  
    
      #**document?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if this is a Document.

  

      
        
- 
  
    
      #**dup**(level = 1, new_parent_doc = document)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   dup → Nokogiri::XML::Node   dup(level) → Nokogiri::XML::Node   dup(level, new_parent_doc) → Nokogiri::XML::Node.

  

      
        
- 
  
    
      #**each**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Iterate over each attribute name and value pair for this Node.

  

      
        
- 
  
    
      #**element?**  ⇒ Boolean 
    

    
      (also: #elem?)
    
  
  
  
  
  
  
  
  

  
    

Returns true if this is an Element node.

  

      
        
- 
  
    
      #**element_children**  ⇒ Object 
    

    
      (also: #elements)
    
  
  
  
  
  
  
  
  

  
    

:call-seq:   element_children() → NodeSet   elements() → NodeSet.

  

      
        
- 
  
    
      #**encode_special_chars**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: encode_special_chars(string) → String.

  

      
        
- 
  
    
      #**external_subset**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   external_subset().

  

      
        
- 
  
    
      #**first_element_child**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   first_element_child() → Node.

  

      
        
- 
  
    
      #**fragment**(tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a DocumentFragment containing `tags` that is relative to *this* context node.

  

      
        
- 
  
    
      #**fragment?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if this is a DocumentFragment.

  

      
        
- 
  
    
      #**html?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if this is an HTML4::Document or HTML5::Document node.

  

      
        
- 
  
    
      #**initialize**(name, document)  ⇒ Node 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:call-seq:   new(name, document) -> Nokogiri::XML::Node   new(name, document) { |node| … } -> Nokogiri::XML::Node.

  

      
        
- 
  
    
      #**inner_html**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the inner_html for this node’s Node#children.

  

      
        
- 
  
    
      #**inner_html=**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the content for this Node to `node_or_tags`.

  

      
        
- 
  
    
      #**internal_subset**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   internal_subset().

  

      
        
- 
  
    
      #**key?**(attribute)  ⇒ Boolean 
    

    
      (also: #has_attribute?)
    
  
  
  
  
  
  
  
  

  
    

Returns true if `attribute` is set.

  

      
        
- 
  
    
      #**keys**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the attribute names for this Node.

  

      
        
- 
  
    
      #**kwattr_add**(attribute_name, keywords)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   kwattr_add(attribute_name, keywords) → self.

  

      
        
- 
  
    
      #**kwattr_append**(attribute_name, keywords)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   kwattr_append(attribute_name, keywords) → self.

  

      
        
- 
  
    
      #**kwattr_remove**(attribute_name, keywords)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   kwattr_remove(attribute_name, keywords) → self.

  

      
        
- 
  
    
      #**kwattr_values**(attribute_name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   kwattr_values(attribute_name) → Array<String>.

  

      
        
- 
  
    
      #**lang**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Searches the language of a node, i.e.

  

      
        
- 
  
    
      #**lang=**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the language of a node, i.e.

  

      
        
- 
  
    
      #**last_element_child**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   last_element_child() → Node.

  

      
        
- 
  
    
      #**line**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   line() → Integer.

  

      
        
- 
  
    
      #**line=**(num)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the line for this Node.

  

      
        
- 
  
    
      #**matches?**(selector)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if this Node matches `selector`.

  

      
        
- 
  
    
      #**namespace**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   namespace() → Namespace.

  

      
        
- 
  
    
      #**namespace=**(ns)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the default namespace on this node (as would be defined with an “xmlns=” attribute in XML source), as a Namespace object `ns`.

  

      
        
- 
  
    
      #**namespace_definitions**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   namespace_definitions() → Array<Nokogiri::XML::Namespace>.

  

      
        
- 
  
    
      #**namespace_scopes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   namespace_scopes() → Array<Nokogiri::XML::Namespace>.

  

      
        
- 
  
    
      #**namespaced_key?**(attribute, namespace)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if `attribute` is set with `namespace`.

  

      
        
- 
  
    
      #**namespaces**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   namespaces() → Hash<String(Namespace#prefix) ⇒ String(Namespace#href)>.

  

      
        
- 
  
    
      #**native_content=**(input)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the content of this node to `input`.

  

      
        
- 
  
    
      #**next_element**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the next Nokogiri::XML::Element type sibling node.

  

      
        
- 
  
    
      #**next_sibling**  ⇒ Object 
    

    
      (also: #next)
    
  
  
  
  
  
  
  
  

  
    

Returns the next sibling node.

  

      
        
- 
  
    
      #**name**  ⇒ Object 
    

    
      (also: #name)
    
  
  
  
  
  
  
  
  

  
    

Returns the name for this Node.

  

      
        
- 
  
    
      #**name=**(new_name)  ⇒ Object 
    

    
      (also: #name=)
    
  
  
  
  
  
  
  
  

  
    

Set the name for this Node.

  

      
        
- 
  
    
      #**node_type**  ⇒ Object 
    

    
      (also: #type)
    
  
  
  
  
  
  
  
  

  
    

Get the type for this Node.

  

      
        
- 
  
    
      #**parent**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the parent Node for this Node.

  

      
        
- 
  
    
      #**parent=**(parent_node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the parent Node for this Node.

  

      
        
- 
  
    
      #**parse**(string_or_io, options = nil) {|options| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse `string_or_io` as a document fragment within the context of **this** node.

  

      
        
- 
  
    
      #**path**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the path associated with this Node.

  

      
        
- 
  
    
      #**pointer_id**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: pointer_id() → Integer.

  

      
        
- 
  
    
      #**prepend_child**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add `node_or_tags` as the first child of this Node.

  

      
        
- 
  
    
      #**previous_element**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the previous Nokogiri::XML::Element type sibling node.

  

      
        
- 
  
    
      #**previous_sibling**  ⇒ Object 
    

    
      (also: #previous)
    
  
  
  
  
  
  
  
  

  
    

Returns the previous sibling node.

  

      
        
- 
  
    
      #**processing_instruction?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if this is a ProcessingInstruction node.

  

      
        
- 
  
    
      #**read_only?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Is this a read only node?.

  

      
        
- 
  
    
      #**remove_attribute**(name)  ⇒ Object 
    

    
      (also: #delete)
    
  
  
  
  
  
  
  
  

  
    

Remove the attribute named `name`.

  

      
        
- 
  
    
      #**remove_class**(names = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   remove_class(css_classes) → self.

  

      
        
- 
  
    
      #**replace**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Replace this Node with `node_or_tags`.

  

      
        
- 
  
    
      #**serialize**(*args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Serialize Node using `options`.

  

      
        
- 
  
    
      #**swap**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Swap this Node for `node_or_tags`.

  

      
        
- 
  
    
      #**text?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if this is a Text node.

  

      
        
- 
  
    
      #**to_html**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Serialize this Node to HTML.

  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Turn this node in to a string.

  

      
        
- 
  
    
      #**to_xhtml**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Serialize this Node to XHTML using `options`.

  

      
        
- 
  
    
      #**to_xml**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Serialize this Node to XML using `options`.

  

      
        
- 
  
    
      #**traverse** {|_self| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Yields self and all children to `block` recursively.

  

      
        
- 
  
    
      #**unlink**  ⇒ Object 
    

    
      (also: #remove)
    
  
  
  
  
  
  
  
  

  
    

:call-seq:   unlink() → self.

  

      
        
- 
  
    
      #**value?**(value)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Does this Node’s attributes include <value>.

  

      
        
- 
  
    
      #**values**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the attribute values for this Node.

  

      
        
- 
  
    
      #**wrap**(node_or_tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   wrap(markup) -> self   wrap(node) -> self.

  

      
        
- 
  
    
      #**write_html_to**(io, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Write Node as HTML to `io` with `options`.

  

      
        
- 
  
    
      #**write_to**(io, *options) {|config| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   write_to(io, *options).

  

      
        
- 
  
    
      #**write_xhtml_to**(io, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Write Node as XHTML to `io` with `options`.

  

      
        
- 
  
    
      #**write_xml_to**(io, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Write Node as XML to `io` with `options`.

  

      
        
- 
  
    
      #**xml?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns true if this is an XML::Document node.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
  
  
  
  
  
  
  
  
### Methods included from Searchable

  

#>, #at, #at_css, #at_xpath, #css, #search, #xpath

  
  
  
  
  
  
  
  
  
### Methods included from PP::Node

  

#inspect, #pretty_print

  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, document)  ⇒ Node 
  

  

  

  
    

:call-seq:

```
new(name, document) -> Nokogiri::XML::Node
new(name, document) { |node| ... } -> Nokogiri::XML::Node

```

Create a new node with `name` that belongs to `document`.

If you intend to add a node to a document tree, it’s likely that you will prefer one of the Nokogiri::XML::Node methods like #add_child, #add_next_sibling, #replace, etc. which will both create an element (or subtree) and place it in the document tree.

Another alternative, if you are concerned about performance, is Nokogiri::XML::Document#create_element which accepts additional arguments for contents or attributes but (like this method) avoids parsing markup.
Parameters

- 

`name` (String)

- 

`document` (Nokogiri::XML::Document) The document to which the the returned node will belong.

Yields

Nokogiri::XML::Node
Returns

Nokogiri::XML::Node

  

  

  
    
      

```

126
127
128
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 126

def initialize(name, document)
  # This is intentionally empty, and sets the method signature for subclasses.
end
```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**new**(*args)  ⇒ Object 
  

  

  

  
    

:nodoc: documented in lib/nokogiri/xml/node.rb

  

  

  
    
      

```

2078
2079
2080
2081
2082
2083
2084
2085
2086
2087
2088
2089
2090
2091
2092
2093
2094
2095
2096
2097
2098
2099
2100
2101
2102
2103
2104
2105
2106
2107
2108
2109
2110
2111
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 2078

static VALUE
rb_xml_node_new(int argc, VALUE *argv, VALUE klass)
{
  xmlNodePtr c_document_node;
  xmlNodePtr c_node;
  VALUE rb_name;
  VALUE rb_document_node;
  VALUE rest;
  VALUE rb_node;

  rb_scan_args(argc, argv, "2*", &rb_name, &rb_document_node, &rest);

  if (!rb_obj_is_kind_of(rb_document_node, cNokogiriXmlNode)) {
    rb_raise(rb_eArgError, "document must be a Nokogiri::XML::Node");
  }
  if (!rb_obj_is_kind_of(rb_document_node, cNokogiriXmlDocument)) {
    NOKO_WARN_DEPRECATION("Passing a Node as the second parameter to Node.new is deprecated. Please pass a Document instead, or prefer an alternative constructor like Node#add_child. This will become an error in Nokogiri v1.17.0."); // TODO: deprecated in v1.13.0, remove in v1.17.0
  }
  Noko_Node_Get_Struct(rb_document_node, xmlNode, c_document_node);

  c_node = xmlNewNode(NULL, (xmlChar *)StringValueCStr(rb_name));
  c_node->doc = c_document_node->doc;
  noko_xml_document_pin_node(c_node);

  rb_node = noko_xml_node_wrap(
              klass == cNokogiriXmlNode ? (VALUE)NULL : klass,
              c_node
            );
  rb_obj_call_init(rb_node, argc, argv);

  if (rb_block_given_p()) { rb_yield(rb_node); }

  return rb_node;
}
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**<<**(node_or_tags)  ⇒ Object 
  

  

  

  
    

Add `node_or_tags` as a child of this Node.

`node_or_tags` can be a Nokogiri::XML::Node, a ::DocumentFragment, a ::NodeSet, or a String containing markup.

Returns `self`, to support chaining of calls (e.g., root << child1 << child2)

Also see related method `add_child`.

  

  

  
    
      

```

292
293
294
295
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 292

def <<(node_or_tags)
  add_child(node_or_tags)
  self
end
```

    
  

    
      
  
### 
  
    #**<=>**(other)  ⇒ Object 
  

  

  

  
    

Compare two Node objects with respect to their Document.  Nodes from different documents cannot be compared.

  

  

  
    
      

```

1340
1341
1342
1343
1344
1345
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1340

def <=>(other)
  return unless other.is_a?(Nokogiri::XML::Node)
  return unless document == other.document

  compare(other)
end
```

    
  

    
      
  
### 
  
    #**==**(other)  ⇒ Object 
  

  

  

  
    

Test to see if this Node is equal to `other`

  

  

  
    
      

```

1330
1331
1332
1333
1334
1335
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1330

def ==(other)
  return false unless other
  return false unless other.respond_to?(:pointer_id)

  pointer_id == other.pointer_id
end
```

    
  

    
      
  
### 
  
    #**[]**(name)  ⇒ Object 
  

  
    Also known as:
    get_attribute, attr
    
  

  

  
    

:call-seq: [](name) → (String, nil)

Fetch an attribute from this node.

⚠ Note that attributes with namespaces cannot be accessed with this method. To access namespaced attributes, use #attribute_with_ns.
Returns

(String, nil) value of the attribute `name`, or `nil` if no matching attribute exists

**Example**

```
doc = Nokogiri::XML("<root><child size='large' class='big wide tall'/></root>")
child = doc.at_css("child")
child["size"] # => "large"
child["class"] # => "big wide tall"

```

**Example:** Namespaced attributes will not be returned.

⚠ Note namespaced attributes may be accessed with #attribute or #attribute_with_ns

```
doc = Nokogiri::XML(<<~EOF)
  <root xmlns:width='http://example.com/widths'>
    <child width:size='broad'/>
  </root>
EOF
doc.at_css("child")["size"] # => nil
doc.at_css("child").attribute("size").value # => "broad"
doc.at_css("child").attribute_with_ns("size", "http://example.com/widths").value
# => "broad"

```

  

  

  
    
      

```

587
588
589
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 587

def [](name)
  get(name.to_s)
end
```

    
  

    
      
  
### 
  
    #**[]=**(name, value)  ⇒ Object 
  

  
    Also known as:
    set_attribute
    
  

  

  
    

:call-seq: []=(name, value) → value

Update the attribute `name` to `value`, or create the attribute if it does not exist.

⚠ Note that attributes with namespaces cannot be accessed with this method. To access namespaced attributes for update, use #attribute_with_ns. To add a namespaced attribute, see the example below.
Returns

`value`

**Example**

```
doc = Nokogiri::XML("<root><child/></root>")
child = doc.at_css("child")
child["size"] = "broad"
child.to_html
# => "<child size=\"broad\"></child>"

```

**Example:** Add a namespaced attribute.

```
doc = Nokogiri::XML(<<~EOF)
  <root xmlns:width='http://example.com/widths'>
    <child/>
  </root>
EOF
child = doc.at_css("child")
child["size"] = "broad"
ns = doc.root.namespace_definitions.find { |ns| ns.prefix == "width" }
child.attribute("size").namespace = ns
doc.to_html
# => "<root xmlns:width=\"http://example.com/widths\">\n" +
#    "  <child width:size=\"broad\"></child>\n" +
#    "</root>\n"

```

  

  

  
    
      

```

625
626
627
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 625

def []=(name, value)
  set(name.to_s, value.to_s)
end
```

    
  

    
      
  
### 
  
    #**accept**(visitor)  ⇒ Object 
  

  

  

  
    

Accept a visitor.  This method calls “visit” on `visitor` with self.

  

  

  
    
      

```

1324
1325
1326
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1324

def accept(visitor)
  visitor.visit(self)
end
```

    
  

    
      
  
### 
  
    #**add_child**(node_or_tags)  ⇒ Object 
  

  

  

  
    

Add `node_or_tags` as a child of this Node.

`node_or_tags` can be a Nokogiri::XML::Node, a ::DocumentFragment, a ::NodeSet, or a String containing markup.

Returns the reparented node (if `node_or_tags` is a Node), or NodeSet (if `node_or_tags` is a DocumentFragment, NodeSet, or String).

Also see related method <<.

  

  

  
    
      

```

184
185
186
187
188
189
190
191
192
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 184

def add_child(node_or_tags)
  node_or_tags = coerce(node_or_tags)
  if node_or_tags.is_a?(XML::NodeSet)
    node_or_tags.each { |n| add_child_node_and_reparent_attrs(n) }
  else
    add_child_node_and_reparent_attrs(node_or_tags)
  end
  node_or_tags
end
```

    
  

    
      
  
### 
  
    #**add_class**(names)  ⇒ Object 
  

  

  

  
    

:call-seq: add_class(names) → self

Ensure HTML CSS classes are present on `self`. Any CSS classes in `names` that already exist in the “class” attribute are *not* added. Note that any existing duplicates in the “class” attribute are not removed. Compare with #append_class.

This is a convenience function and is equivalent to:

```
node.kwattr_add("class", names)

```

See related: #kwattr_add, #classes, #append_class, #remove_class
Parameters

- 

`names` (String, Array<String>)

CSS class names to be added to the Node’s “class” attribute. May be a string containing whitespace-delimited names, or an Array of String names. Any class names already present will not be added. Any class names not present will be added. If no “class” attribute exists, one is created.

Returns

`self` (Node) for ease of chaining method calls.

**Example:** Ensure that the node has CSS class “section”

```
node                      # => <div></div>
node.add_class("section") # => <div class="section"></div>
node.add_class("section") # => <div class="section"></div> # duplicate not added

```

**Example:** Ensure that the node has CSS classes “section” and “header”, via a String argument

Note that the CSS class “section” is not added because it is already present. Note also that the pre-existing duplicate CSS class “section” is not removed.

```
node                             # => <div class="section section"></div>
node.add_class("section header") # => <div class="section section header"></div>

```

**Example:** Ensure that the node has CSS classes “section” and “header”, via an Array argument

```
node                                  # => <div></div>
node.add_class(["section", "header"]) # => <div class="section header"></div>

```

  

  

  
    
      

```

790
791
792
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 790

def add_class(names)
  kwattr_add("class", names)
end
```

    
  

    
      
  
### 
  
    #**add_namespace_definition**(rb_prefix, rb_href)  ⇒ Object 
  

  
    Also known as:
    add_namespace
    
  

  

  
    

:call-seq:

```
add_namespace_definition(prefix, href) → Nokogiri::XML::Namespace
add_namespace(prefix, href) → Nokogiri::XML::Namespace

```

:category: Manipulating Document Structure

Adds a namespace definition to this node with `prefix` using `href` value, as if this node had included an attribute “xmlns:prefix=href”.

A default namespace definition for this node can be added by passing `nil` for `prefix`.
Parameters

- 

`prefix` (String, `nil`) An XML Name

- 

`href` (String) The URI reference

Returns

The new Nokogiri::XML::Namespace

**Example:** adding a non-default namespace definition

```
doc = Nokogiri::XML("<store><inventory></inventory></store>")
inventory = doc.at_css("inventory")
inventory.add_namespace_definition("automobile", "http://alices-autos.com/")
inventory.add_namespace_definition("bicycle", "http://bobs-bikes.com/")
inventory.add_child("<automobile:tire>Michelin model XGV, size 75R</automobile:tire>")
doc.to_xml
# => "<?xml version=\"1.0\"?>\n" +
#    "<store>\n" +
#    "  <inventory xmlns:automobile=\"http://alices-autos.com/\" xmlns:bicycle=\"http://bobs-bikes.com/\">\n" +
#    "    <automobile:tire>Michelin model XGV, size 75R</automobile:tire>\n" +
#    "  </inventory>\n" +
#    "</store>\n"

```

**Example:** adding a default namespace definition

```
doc = Nokogiri::XML("<store><inventory><tire>Michelin model XGV, size 75R</tire></inventory></store>")
doc.at_css("tire").add_namespace_definition(nil, "http://bobs-bikes.com/")
doc.to_xml
# => "<?xml version=\"1.0\"?>\n" +
#    "<store>\n" +
#    "  <inventory>\n" +
#    "    <tire xmlns=\"http://bobs-bikes.com/\">Michelin model XGV, size 75R</tire>\n" +
#    "  </inventory>\n" +
#    "</store>\n"

```

  

  

  
    
      

```

466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 466

static VALUE
rb_xml_node_add_namespace_definition(VALUE rb_node, VALUE rb_prefix, VALUE rb_href)
{
  xmlNodePtr c_node, element;
  xmlNsPtr c_namespace;
  const xmlChar *c_prefix = (const xmlChar *)(NIL_P(rb_prefix) ? NULL : StringValueCStr(rb_prefix));

  Noko_Node_Get_Struct(rb_node, xmlNode, c_node);
  element = c_node ;

  c_namespace = xmlSearchNs(c_node->doc, c_node, c_prefix);

  if (!c_namespace) {
    if (c_node->type != XML_ELEMENT_NODE) {
      element = c_node->parent;
    }
    c_namespace = xmlNewNs(element, (const xmlChar *)StringValueCStr(rb_href), c_prefix);
  }

  if (!c_namespace) {
    return Qnil ;
  }

  if (NIL_P(rb_prefix) || c_node != element) {
    xmlSetNs(c_node, c_namespace);
  }

  return noko_xml_namespace_wrap(c_namespace, c_node->doc);
}
```

    
  

    
      
  
### 
  
    #**add_next_sibling**(node_or_tags)  ⇒ Object 
  

  
    Also known as:
    next=
    
  

  

  
    

Insert `node_or_tags` after this Node (as a sibling).

`node_or_tags` can be a Nokogiri::XML::Node, a ::DocumentFragment, a ::NodeSet, or a String containing markup.

Returns the reparented node (if `node_or_tags` is a Node), or NodeSet (if `node_or_tags` is a DocumentFragment, NodeSet, or String).

Also see related method `after`.

  

  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

324
325
326
327
328
329
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 324

def add_next_sibling(node_or_tags)
  raise ArgumentError,
    "A document may not have multiple root nodes." if parent&.document? && !(node_or_tags.comment? || node_or_tags.processing_instruction?)

  add_sibling(:next, node_or_tags)
end
```

    
  

    
      
  
### 
  
    #**add_previous_sibling**(node_or_tags)  ⇒ Object 
  

  
    Also known as:
    previous=
    
  

  

  
    

Insert `node_or_tags` before this Node (as a sibling).

`node_or_tags` can be a Nokogiri::XML::Node, a ::DocumentFragment, a ::NodeSet, or a String containing markup.

Returns the reparented node (if `node_or_tags` is a Node), or NodeSet (if `node_or_tags` is a DocumentFragment, NodeSet, or String).

Also see related method `before`.

  

  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

307
308
309
310
311
312
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 307

def add_previous_sibling(node_or_tags)
  raise ArgumentError,
    "A document may not have multiple root nodes." if parent&.document? && !(node_or_tags.comment? || node_or_tags.processing_instruction?)

  add_sibling(:previous, node_or_tags)
end
```

    
  

    
      
  
### 
  
    #**after**(node_or_tags)  ⇒ Object 
  

  

  

  
    

Insert `node_or_tags` after this node (as a sibling).

`node_or_tags` can be a Nokogiri::XML::Node, a Nokogiri::XML::DocumentFragment, or a String containing markup.

Returns `self`, to support chaining of calls.

Also see related method `add_next_sibling`.

  

  

  
    
      

```

354
355
356
357
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 354

def after(node_or_tags)
  add_next_sibling(node_or_tags)
  self
end
```

    
  

    
      
  
### 
  
    #**ancestors**(selector = nil)  ⇒ Object 
  

  

  

  
    

Get a list of ancestor Node for this Node.  If `selector` is given, the ancestors must match `selector`

  

  

  
    
      

```

1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1293

def ancestors(selector = nil)
  return NodeSet.new(document) unless respond_to?(:parent)
  return NodeSet.new(document) unless parent

  parents = [parent]

  while parents.last.respond_to?(:parent)
    break unless (ctx_parent = parents.last.parent)

    parents << ctx_parent
  end

  return NodeSet.new(document, parents) unless selector

  root = parents.last
  search_results = root.search(selector)

  NodeSet.new(document, parents.find_all do |parent|
    search_results.include?(parent)
  end)
end
```

    
  

    
      
  
### 
  
    #**append_class**(names)  ⇒ Object 
  

  

  

  
    

:call-seq: append_class(names) → self

Add HTML CSS classes to `self`, regardless of duplication. Compare with #add_class.

This is a convenience function and is equivalent to:

```
node.kwattr_append("class", names)

```

See related: #kwattr_append, #classes, #add_class, #remove_class
Parameters

- 

`names` (String, Array<String>)

CSS class names to be appended to the Node’s “class” attribute. May be a string containing whitespace-delimited names, or an Array of String names. All class names passed in will be appended to the “class” attribute even if they are already present in the attribute value. If no “class” attribute exists, one is created.

Returns

`self` (Node) for ease of chaining method calls.

**Example:** Append “section” to the node’s CSS “class” attribute

```
node                         # => <div></div>
node.append_class("section") # => <div class="section"></div>
node.append_class("section") # => <div class="section section"></div> # duplicate added!

```

**Example:** Append “section” and “header” to the noded’s CSS “class” attribute, via a String argument

Note that the CSS class “section” is appended even though it is already present

```
node                                # => <div class="section section"></div>
node.append_class("section header") # => <div class="section section section header"></div>

```

**Example:** Append “section” and “header” to the node’s CSS “class” attribute, via an Array argument

```
node                                     # => <div></div>
node.append_class(["section", "header"]) # => <div class="section header"></div>
node.append_class(["section", "header"]) # => <div class="section header section header"></div>

```

  

  

  
    
      

```

834
835
836
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 834

def append_class(names)
  kwattr_append("class", names)
end
```

    
  

    
      
  
### 
  
    #**attribute**(name)  ⇒ Object 
  

  

  

  
    

:call-seq: attribute(name) → Nokogiri::XML::Attr

:category: Working With Node Attributes
Returns

Attribute (Nokogiri::XML::Attr) belonging to this node with name `name`.

⚠ Note that attribute namespaces are ignored and only the simple (non-namespace-prefixed) name is used to find a matching attribute. In case of a simple name collision, only one of the matching attributes will be returned. In this case, you will need to use #attribute_with_ns.

**Example:**

```
doc = Nokogiri::XML("<root><child size='large' class='big wide tall'/></root>")
child = doc.at_css("child")
child.attribute("size") # => #<Nokogiri::XML::Attr:0x550 name="size" value="large">
child.attribute("class") # => #<Nokogiri::XML::Attr:0x564 name="class" value="big wide tall">

```

**Example** showing that namespaced attributes will not be returned:

⚠ Note that only one of the two matching attributes is returned.

```
doc = Nokogiri::XML(<<~EOF)
  <root xmlns:width='http://example.com/widths'
        xmlns:height='http://example.com/heights'>
    <child width:size='broad' height:size='tall'/>
  </root>
EOF
doc.at_css("child").attribute("size")
# => #(Attr:0x550 {
#      name = "size",
#      namespace = #(Namespace:0x564 {
#        prefix = "width",
#        href = "http://example.com/widths"
#        }),
#      value = "broad"
#      })

```

  

  

  
    
      

```

535
536
537
538
539
540
541
542
543
544
545
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 535

static VALUE
rb_xml_node_attribute(VALUE self, VALUE name)
{
  xmlNodePtr node;
  xmlAttrPtr prop;
  Noko_Node_Get_Struct(self, xmlNode, node);
  prop = xmlHasProp(node, (xmlChar *)StringValueCStr(name));

  if (! prop) { return Qnil; }
  return noko_xml_node_wrap(Qnil, (xmlNodePtr)prop);
}
```

    
  

    
      
  
### 
  
    #**attribute_nodes**  ⇒ Object 
  

  

  

  
    

:call-seq: attribute_nodes() → Array<Nokogiri::XML::Attr>

:category: Working With Node Attributes
Returns

Attributes (an Array of Nokogiri::XML::Attr) belonging to this node.

Note that this is the preferred alternative to #attributes when the simple (non-namespace-prefixed) attribute names may collide.

**Example:**

Contrast this with the colliding-name example from #attributes.

```
doc = Nokogiri::XML(<<~EOF)
  <root xmlns:width='http://example.com/widths'
        xmlns:height='http://example.com/heights'>
    <child width:size='broad' height:size='tall'/>
  </root>
EOF
doc.at_css("child").attribute_nodes
# => [#(Attr:0x550 {
#       name = "size",
#       namespace = #(Namespace:0x564 {
#         prefix = "width",
#         href = "http://example.com/widths"
#         }),
#       value = "broad"
#       }),
#     #(Attr:0x578 {
#       name = "size",
#       namespace = #(Namespace:0x58c {
#         prefix = "height",
#         href = "http://example.com/heights"
#         }),
#       value = "tall"
#       })]

```

  

  

  
    
      

```

586
587
588
589
590
591
592
593
594
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 586

static VALUE
rb_xml_node_attribute_nodes(VALUE rb_node)
{
  xmlNodePtr c_node;

  Noko_Node_Get_Struct(rb_node, xmlNode, c_node);

  return noko_xml_node_attrs(c_node);
}
```

    
  

    
      
  
### 
  
    #**attribute_with_ns**(name, namespace)  ⇒ Object 
  

  

  

  
    

:call-seq: attribute_with_ns(name, namespace) → Nokogiri::XML::Attr

:category: Working With Node Attributes
Returns

Attribute (Nokogiri::XML::Attr) belonging to this node with matching `name` and `namespace`.

- 

`name` (String): the simple (non-namespace-prefixed) name of the attribute

- 

`namespace` (String): the URI of the attribute’s namespace

See related: #attribute

**Example:**

```
doc = Nokogiri::XML(<<~EOF)
  <root xmlns:width='http://example.com/widths'
        xmlns:height='http://example.com/heights'>
    <child width:size='broad' height:size='tall'/>
  </root>
EOF
doc.at_css("child").attribute_with_ns("size", "http://example.com/widths")
# => #(Attr:0x550 {
#      name = "size",
#      namespace = #(Namespace:0x564 {
#        prefix = "width",
#        href = "http://example.com/widths"
#        }),
#      value = "broad"
#      })
doc.at_css("child").attribute_with_ns("size", "http://example.com/heights")
# => #(Attr:0x578 {
#      name = "size",
#      namespace = #(Namespace:0x58c {
#        prefix = "height",
#        href = "http://example.com/heights"
#        }),
#      value = "tall"
#      })

```

  

  

  
    
      

```

638
639
640
641
642
643
644
645
646
647
648
649
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 638

static VALUE
rb_xml_node_attribute_with_ns(VALUE self, VALUE name, VALUE namespace)
{
  xmlNodePtr node;
  xmlAttrPtr prop;
  Noko_Node_Get_Struct(self, xmlNode, node);
  prop = xmlHasNsProp(node, (xmlChar *)StringValueCStr(name),
                      NIL_P(namespace) ? NULL : (xmlChar *)StringValueCStr(namespace));

  if (! prop) { return Qnil; }
  return noko_xml_node_wrap(Qnil, (xmlNodePtr)prop);
}
```

    
  

    
      
  
### 
  
    #**attributes**  ⇒ Object 
  

  

  

  
    

:call-seq: attributes() → Hash<String ⇒ Nokogiri::XML::Attr>

Fetch this node’s attributes.

⚠ Because the keys do not include any namespace information for the attribute, in case of a simple name collision, not all attributes will be returned. In this case, you will need to use #attribute_nodes.
Returns

Hash containing attributes belonging to `self`. The hash keys are String attribute names (without the namespace), and the hash values are Nokogiri::XML::Attr.

**Example** with no namespaces:

```
doc = Nokogiri::XML("<root><child size='large' class='big wide tall'/></root>")
doc.at_css("child").attributes
# => {"size"=>#(Attr:0x550 { name = "size", value = "large" }),
#     "class"=>#(Attr:0x564 { name = "class", value = "big wide tall" })}

```

**Example** with a namespace:

```
doc = Nokogiri::XML("<root xmlns:desc='http://example.com/sizes'><child desc:size='large'/></root>")
doc.at_css("child").attributes
# => {"size"=>
#      #(Attr:0x550 {
#        name = "size",
#        namespace = #(Namespace:0x564 {
#          prefix = "desc",
#          href = "http://example.com/sizes"
#          }),
#        value = "large"
#        })}

```

**Example** with an attribute name collision:

⚠ Note that only one of the attributes is returned in the Hash.

```
doc = Nokogiri::XML(<<~EOF)
  <root xmlns:width='http://example.com/widths'
        xmlns:height='http://example.com/heights'>
    <child width:size='broad' height:size='tall'/>
  </root>
EOF
doc.at_css("child").attributes
# => {"size"=>
#      #(Attr:0x550 {
#        name = "size",
#        namespace = #(Namespace:0x564 {
#          prefix = "height",
#          href = "http://example.com/heights"
#          }),
#        value = "tall"
#        })}

```

  

  

  
    
      

```

684
685
686
687
688
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 684

def attributes
  attribute_nodes.each_with_object({}) do |node, hash|
    hash[node.node_name] = node
  end
end
```

    
  

    
      
  
### 
  
    #**before**(node_or_tags)  ⇒ Object 
  

  

  

  
    

Insert `node_or_tags` before this node (as a sibling).

`node_or_tags` can be a Nokogiri::XML::Node, a ::DocumentFragment, a ::NodeSet, or a String containing markup.

Returns `self`, to support chaining of calls.

Also see related method `add_previous_sibling`.

  

  

  
    
      

```

340
341
342
343
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 340

def before(node_or_tags)
  add_previous_sibling(node_or_tags)
  self
end
```

    
  

    
      
  
### 
  
    #**blank?**  ⇒ Boolean 
  

  

  

  
    Returns

`true` if the node is an empty or whitespace-only text or cdata node, else `false`.

**Example:**

```
Nokogiri("<root><child/></root>").root.child.blank? # => false
Nokogiri("<root>\t \n</root>").root.child.blank? # => true
Nokogiri("<root><![CDATA[\t \n]]></root>").root.child.blank? # => true
Nokogiri("<root>not-blank</root>").root.child
  .tap { |n| n.content = "" }.blank # => true

```

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

666
667
668
669
670
671
672
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 666

static VALUE
rb_xml_node_blank_eh(VALUE self)
{
  xmlNodePtr node;
  Noko_Node_Get_Struct(self, xmlNode, node);
  return (1 == xmlIsBlankNode(node)) ? Qtrue : Qfalse ;
}
```

    
  

    
      
  
### 
  
    #**canonicalize**(mode = XML::XML_C14N_1_0, inclusive_namespaces = nil, with_comments = false)  ⇒ Object 
  

  

  

  
    
      

```

1492
1493
1494
1495
1496
1497
1498
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1492

def canonicalize(mode = XML::XML_C14N_1_0, inclusive_namespaces = nil, with_comments = false)
  c14n_root = self
  document.canonicalize(mode, inclusive_namespaces, with_comments) do |node, parent|
    tn = node.is_a?(XML::Node) ? node : parent
    tn == c14n_root || tn.ancestors.include?(c14n_root)
  end
end
```

    
  

    
      
  
### 
  
    #**cdata?**  ⇒ Boolean 
  

  

  

  
    

Returns true if this is a CDATA

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1214
1215
1216
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1214

def cdata?
  type == CDATA_SECTION_NODE
end
```

    
  

    
      
  
### 
  
    #**child**  ⇒ Object 
  

  

  

  
    

:call-seq: child() → Nokogiri::XML::Node

:category: Traversing Document Structure
Returns

First of this node’s children, or `nil` if there are no children

This is a convenience method and is equivalent to:

```
node.children.first

```

See related: #children

  

  

  
    
      

```

688
689
690
691
692
693
694
695
696
697
698
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 688

static VALUE
rb_xml_node_child(VALUE self)
{
  xmlNodePtr node, child;
  Noko_Node_Get_Struct(self, xmlNode, node);

  child = node->children;
  if (!child) { return Qnil; }

  return noko_xml_node_wrap(Qnil, child);
}
```

    
  

    
      
  
### 
  
    #**children**  ⇒ Object 
  

  

  

  
    

:call-seq: children() → Nokogiri::XML::NodeSet

:category: Traversing Document Structure
Returns

Nokogiri::XML::NodeSet containing this node’s children.

  

  

  
    
      

```

708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 708

static VALUE
rb_xml_node_children(VALUE self)
{
  xmlNodePtr node;
  xmlNodePtr child;
  xmlNodeSetPtr set;
  VALUE document;
  VALUE node_set;

  Noko_Node_Get_Struct(self, xmlNode, node);

  child = node->children;
  set = xmlXPathNodeSetCreate(child);

  document = DOC_RUBY_OBJECT(node->doc);

  if (!child) { return noko_xml_node_set_wrap(set, document); }

  child = child->next;
  while (NULL != child) {
    xmlXPathNodeSetAddUnique(set, child);
    child = child->next;
  }

  node_set = noko_xml_node_set_wrap(set, document);

  return node_set;
}
```

    
  

    
      
  
### 
  
    #**children=**(node_or_tags)  ⇒ Object 
  

  

  

  
    

Set the content for this Node `node_or_tags`

`node_or_tags` can be a Nokogiri::XML::Node, a Nokogiri::XML::DocumentFragment, or a String containing markup.

Also see related method `inner_html=`

  

  

  
    
      

```

385
386
387
388
389
390
391
392
393
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 385

def children=(node_or_tags)
  node_or_tags = coerce(node_or_tags)
  children.unlink
  if node_or_tags.is_a?(XML::NodeSet)
    node_or_tags.each { |n| add_child_node_and_reparent_attrs(n) }
  else
    add_child_node_and_reparent_attrs(node_or_tags)
  end
end
```

    
  

    
      
  
### 
  
    #**classes**  ⇒ Object 
  

  

  

  
    

:call-seq: classes() → Array<String>

Fetch CSS class names of a Node.

This is a convenience function and is equivalent to:

```
node.kwattr_values("class")

```

See related: #kwattr_values, #add_class, #append_class, #remove_class
Returns

The CSS classes (Array of String) present in the Node’s “class” attribute. If the attribute is empty or non-existent, the return value is an empty array.

**Example**

```
node         # => <div class="section title header"></div>
node.classes # => ["section", "title", "header"]

```

  

  

  
    
      

```

744
745
746
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 744

def classes
  kwattr_values("class")
end
```

    
  

    
      
  
### 
  
    #**clone**(level = 1, new_parent_doc = document)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
clone → Nokogiri::XML::Node
clone(level) → Nokogiri::XML::Node
clone(level, new_parent_doc) → Nokogiri::XML::Node

```

Clone this node.
Parameters

- 

`level` (optional Integer). 0 is a shallow copy, 1 (the default) is a deep copy.

- 

`new_parent_doc` The new node’s parent Document. Defaults to the the Document of the current node.

Returns

The new Nokogiri::XML::Node

  

  

  
    
      

```

162
163
164
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 162

def clone(level = 1, new_parent_doc = document)
  super().initialize_copy_with_args(self, level, new_parent_doc)
end
```

    
  

    
      
  
### 
  
    #**comment?**  ⇒ Boolean 
  

  

  

  
    

Returns true if this is a Comment

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1209
1210
1211
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1209

def comment?
  type == COMMENT_NODE
end
```

    
  

    
      
  
### 
  
    #**content**  ⇒ Object 
  

  
    Also known as:
    inner_text, text, to_str
    
  

  

  
    

:call-seq:

```
content() → String
inner_text() → String
text() → String
to_str() → String

```

Returns

Contents of all the text nodes in this node’s subtree, concatenated together into a single String.

⚠ Note that entities will *always* be expanded in the returned String.

See related: #inner_html

**Example** of how entities are handled:

Note that `<` becomes `<` in the returned String.

```
doc = Nokogiri::XML.fragment("<child>a < b</child>")
doc.at_css("child").content
# => "a < b"

```

**Example** of how a subtree is handled:

Note that the `<span>` tags are omitted and only the text node contents are returned, concatenated into a single string.

```
doc = Nokogiri::XML.fragment("<child><span>first</span> <span>second</span></child>")
doc.at_css("child").content
# => "first second"

```

  

  

  
    
      

```

770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 770

static VALUE
rb_xml_node_content(VALUE self)
{
  xmlNodePtr node;
  xmlChar *content;

  Noko_Node_Get_Struct(self, xmlNode, node);

  content = xmlNodeGetContent(node);
  if (content) {
    VALUE rval = NOKOGIRI_STR_NEW2(content);
    xmlFree(content);
    return rval;
  }
  return Qnil;
}
```

    
  

    
      
  
### 
  
    #**content=**(string)  ⇒ Object 
  

  

  

  
    

call-seq:

```
content=(input)

```

Set the content of this node to `input`.
Parameters

- 

`input` (String) The new content for this node. Input is considered to be raw content, and so will be entity-escaped in the final DOM string.

Example

Note how entities are handled:

```
doc = Nokogiri::HTML::Document.parse(<<~HTML)
  <html>
    <body>
      <div id="first">asdf</div>
      <div id="second">asdf</div>
HTML

text_node = doc.at_css("div#first").children.first
div_node = doc.at_css("div#second")

value = "You & Me"

text_node.content = value
div_node.content = value

doc.css("div").to_html
# => "<div id=\"first\">You &amp; Me</div>
#     <div id=\"second\">You &amp; Me</div>"

```

For content that is already entity-escaped, use CGI::unescapeHTML to decode it:

```
text_node.content = CGI::unescapeHTML(value)
div_node.content = CGI::unescapeHTML(value)

doc.css("div").to_html
# => "<div id=\"first\">You & Me</div>
#     <div id=\"second\">You & Me</div>"

```

See also: #native_content=

  

  

  
    
      

```

487
488
489
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 487

def content=(string)
  self.native_content = encode_special_chars(string.to_s)
end
```

    
  

    
      
  
### 
  
    #**create_external_subset**(name, external_id, system_id)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
create_external_subset(name, external_id, system_id)

```

Create an external subset

  

  

  
    
      

```

888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 888

static VALUE
create_external_subset(VALUE self, VALUE name, VALUE external_id, VALUE system_id)
{
  xmlNodePtr node;
  xmlDocPtr doc;
  xmlDtdPtr dtd;

  Noko_Node_Get_Struct(self, xmlNode, node);

  doc = node->doc;

  if (doc->extSubset) {
    rb_raise(rb_eRuntimeError, "Document already has an external subset");
  }

  dtd = xmlNewDtd(
          doc,
          NIL_P(name)        ? NULL : (const xmlChar *)StringValueCStr(name),
          NIL_P(external_id) ? NULL : (const xmlChar *)StringValueCStr(external_id),
          NIL_P(system_id)   ? NULL : (const xmlChar *)StringValueCStr(system_id)
        );

  if (!dtd) { return Qnil; }

  return noko_xml_node_wrap(Qnil, (xmlNodePtr)dtd);
}
```

    
  

    
      
  
### 
  
    #**create_internal_subset**(name, external_id, system_id)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
create_internal_subset(name, external_id, system_id)

```

Create the internal subset of a document.

```
doc.create_internal_subset("chapter", "-//OASIS//DTD DocBook XML//EN", "chapter.dtd")
# => <!DOCTYPE chapter PUBLIC "-//OASIS//DTD DocBook XML//EN" "chapter.dtd">

doc.create_internal_subset("chapter", nil, "chapter.dtd")
# => <!DOCTYPE chapter SYSTEM "chapter.dtd">

```

  

  

  
    
      

```

855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 855

static VALUE
create_internal_subset(VALUE self, VALUE name, VALUE external_id, VALUE system_id)
{
  xmlNodePtr node;
  xmlDocPtr doc;
  xmlDtdPtr dtd;

  Noko_Node_Get_Struct(self, xmlNode, node);

  doc = node->doc;

  if (xmlGetIntSubset(doc)) {
    rb_raise(rb_eRuntimeError, "Document already has an internal subset");
  }

  dtd = xmlCreateIntSubset(
          doc,
          NIL_P(name)        ? NULL : (const xmlChar *)StringValueCStr(name),
          NIL_P(external_id) ? NULL : (const xmlChar *)StringValueCStr(external_id),
          NIL_P(system_id)   ? NULL : (const xmlChar *)StringValueCStr(system_id)
        );

  if (!dtd) { return Qnil; }

  return noko_xml_node_wrap(Qnil, (xmlNodePtr)dtd);
}
```

    
  

    
      
  
### 
  
    #**css_path**  ⇒ Object 
  

  

  

  
    

Get the path to this node as a CSS expression

  

  

  
    
      

```

1284
1285
1286
1287
1288
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1284

def css_path
  path.split(%r{/}).filter_map do |part|
    part.empty? ? nil : part.gsub(/\[(\d+)\]/, ':nth-of-type(\1)')
  end.join(" > ")
end
```

    
  

    
      
  
### 
  
    #**data_ptr?**  ⇒ Boolean 
  

  

  

  
    

:nodoc:

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

2286
2287
2288
2289
2290
2291
2292
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 2286

VALUE
rb_xml_node_data_ptr_eh(VALUE self)
{
  xmlNodePtr c_node;
  Noko_Node_Get_Struct(self, xmlNode, c_node);
  return c_node ? Qtrue : Qfalse;
}
```

    
  

    
      
  
### 
  
    #**deconstruct_keys**(keys)  ⇒ Object 
  

  

  

  
    

:call-seq: deconstruct_keys(array_of_names) → Hash

```
Returns a hash describing the Node, to use in pattern matching.

Valid keys and their values:
- +name+ → (String) The name of this node, or "text" if it is a Text node.
- +namespace+ → (Namespace, nil) The namespace of this node, or nil if there is no namespace.
- +attributes+ → (Array<Attr>) The attributes of this node.
- +children+ → (Array<Node>) The children of this node. 💡 Note this includes text nodes.
- +elements+ → (Array<Node>) The child elements of this node. 💡 Note this does not include text nodes.
- +content+ → (String) The contents of all the text nodes in this node's subtree. See #content.
- +inner_html+ → (String) The inner markup for the children of this node. See #inner_html.

*Example*

  doc = Nokogiri::XML.parse(<<~XML)
    <?xml version="1.0"?>
    <parent xmlns="http://nokogiri.org/ns/default" xmlns:noko="http://nokogiri.org/ns/noko">
      <child1 foo="abc" noko:bar="def">First</child1>
      <noko:child2 foo="qwe" noko:bar="rty">Second</noko:child2>
    </parent>
  XML

  doc.root.deconstruct_keys([:name, :namespace])
  # => {:name=>"parent",
  #     :namespace=>
  #      #(Namespace:0x35c { href = "http://nokogiri.org/ns/default" })}

  doc.root.deconstruct_keys([:inner_html, :content])
  # => {:content=>"\n" + "  First\n" + "  Second\n",
  #     :inner_html=>
  #      "\n" +
  #      "  <child1 foo=\"abc\" noko:bar=\"def\">First</child1>\n" +
  #      "  <noko:child2 foo=\"qwe\" noko:bar=\"rty\">Second</noko:child2>\n"}

  doc.root.elements.first.deconstruct_keys([:attributes])
  # => {:attributes=>
  #      [#(Attr:0x370 { name = "foo", value = "abc" }),
  #       #(Attr:0x384 {
  #         name = "bar",
  #         namespace = #(Namespace:0x398 {
  #           prefix = "noko",
  #           href = "http://nokogiri.org/ns/noko"
  #           }),
  #         value = "def"
  #         })]}

Since v1.14.0

```

  

  

  
    
      

```

1553
1554
1555
1556
1557
1558
1559
1560
1561
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1553

def deconstruct_keys(keys)
  requested_keys = DECONSTRUCT_KEYS & keys
  {}.tap do |values|
    requested_keys.each do |key|
      method = DECONSTRUCT_METHODS[key] || key
      values[key] = send(method)
    end
  end
end
```

    
  

    
      
  
### 
  
    #**decorate!**  ⇒ Object 
  

  

  

  
    

Decorate this node with the decorators set up in this node’s Document

  

  

  
    
      

```

168
169
170
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 168

def decorate!
  document.decorate(self)
end
```

    
  

    
      
  
### 
  
    #**default_namespace=**(url)  ⇒ Object 
  

  

  

  
    

Adds a default namespace supplied as a string `url` href, to self. The consequence is as an xmlns attribute with supplied argument were present in parsed XML.  A default namespace set with this method will now show up in #attributes, but when this node is serialized to XML an “xmlns” attribute will appear. See also #namespace and #namespace=

  

  

  
    
      

```

503
504
505
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 503

def default_namespace=(url)
  add_namespace_definition(nil, url)
end
```

    
  

    
      
  
### 
  
    #**description**  ⇒ Object 
  

  

  

  
    

Fetch the Nokogiri::HTML4::ElementDescription for this node.  Returns nil on XML documents and on unknown tags.

  

  

  
    
      

```

1251
1252
1253
1254
1255
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1251

def description
  return if document.xml?

  Nokogiri::HTML4::ElementDescription[name]
end
```

    
  

    
      
  
### 
  
    #**do_xinclude**(options = XML::ParseOptions::DEFAULT_XML) {|options| ... } ⇒ Object 
  

  

  

  
    

Do xinclude substitution on the subtree below node. If given a block, a Nokogiri::XML::ParseOptions object initialized from `options`, will be passed to it, allowing more convenient modification of the parser options.

  

  

Yields:

  
    
- 
      
      
        (options)
      
      
      
    
  

  
    
      

```

530
531
532
533
534
535
536
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 530

def do_xinclude(options = XML::ParseOptions::DEFAULT_XML)
  options = Nokogiri::XML::ParseOptions.new(options) if Integer === options
  yield options if block_given?

  # call c extension
  process_xincludes(options.to_i)
end
```

    
  

    
      
  
### 
  
    #**document**  ⇒ Object 
  

  

  

  
    

:call-seq: document() → Nokogiri::XML::Document

:category: Traversing Document Structure
Returns

Parent Nokogiri::XML::Document for this node

  

  

  
    
      

```

795
796
797
798
799
800
801
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 795

static VALUE
rb_xml_node_document(VALUE self)
{
  xmlNodePtr node;
  Noko_Node_Get_Struct(self, xmlNode, node);
  return DOC_RUBY_OBJECT(node->doc);
}
```

    
  

    
      
  
### 
  
    #**document?**  ⇒ Boolean 
  

  

  

  
    

Returns true if this is a Document

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1229
1230
1231
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1229

def document?
  is_a?(XML::Document)
end
```

    
  

    
      
  
### 
  
    #**dup**(level = 1, new_parent_doc = document)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
dup → Nokogiri::XML::Node
dup(level) → Nokogiri::XML::Node
dup(level, new_parent_doc) → Nokogiri::XML::Node

```

Duplicate this node.
Parameters

- 

`level` (optional Integer). 0 is a shallow copy, 1 (the default) is a deep copy.

- 

`new_parent_doc` (optional Nokogiri::XML::Document) The new node’s parent Document. Defaults to the the Document of the current node.

Returns

The new Nokogiri::XML::Node

  

  

  
    
      

```

144
145
146
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 144

def dup(level = 1, new_parent_doc = document)
  super().initialize_copy_with_args(self, level, new_parent_doc)
end
```

    
  

    
      
  
### 
  
    #**each**  ⇒ Object 
  

  

  

  
    

Iterate over each attribute name and value pair for this Node.

  

  

  
    
      

```

710
711
712
713
714
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 710

def each
  attribute_nodes.each do |node|
    yield [node.node_name, node.value]
  end
end
```

    
  

    
      
  
### 
  
    #**element?**  ⇒ Boolean 
  

  
    Also known as:
    elem?
    
  

  

  
    

Returns true if this is an Element node

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1265
1266
1267
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1265

def element?
  type == ELEMENT_NODE
end
```

    
  

    
      
  
### 
  
    #**element_children**  ⇒ Object 
  

  
    Also known as:
    elements
    
  

  

  
    

:call-seq:

```
element_children() → NodeSet
elements() → NodeSet

```

Returns

The node’s child elements as a NodeSet. Only children that are elements will be returned, which notably excludes Text nodes.

**Example:**

Note that #children returns the Text node “hello” while #element_children does not.

```
div = Nokogiri::HTML5("<div>hello<span>world</span>").at_css("div")
div.element_children
# => [#<Nokogiri::XML::Element:0x50 name="span" children=[#<Nokogiri::XML::Text:0x3c "world">]>]
div.children
# => [#<Nokogiri::XML::Text:0x64 "hello">,
#     #<Nokogiri::XML::Element:0x50 name="span" children=[#<Nokogiri::XML::Text:0x3c "world">]>]

```

  

  

  
    
      

```

1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1113

static VALUE
rb_xml_node_element_children(VALUE self)
{
  xmlNodePtr node;
  xmlNodePtr child;
  xmlNodeSetPtr set;
  VALUE document;
  VALUE node_set;

  Noko_Node_Get_Struct(self, xmlNode, node);

  child = xmlFirstElementChild(node);
  set = xmlXPathNodeSetCreate(child);

  document = DOC_RUBY_OBJECT(node->doc);

  if (!child) { return noko_xml_node_set_wrap(set, document); }

  child = xmlNextElementSibling(child);
  while (NULL != child) {
    xmlXPathNodeSetAddUnique(set, child);
    child = xmlNextElementSibling(child);
  }

  node_set = noko_xml_node_set_wrap(set, document);

  return node_set;
}
```

    
  

    
      
  
### 
  
    #**encode_special_chars**(string)  ⇒ Object 
  

  

  

  
    

:call-seq: encode_special_chars(string) → String

Encode any special characters in `string`

  

  

  
    
      

```

824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 824

static VALUE
encode_special_chars(VALUE self, VALUE string)
{
  xmlNodePtr node;
  xmlChar *encoded;
  VALUE encoded_str;

  Noko_Node_Get_Struct(self, xmlNode, node);
  encoded = xmlEncodeSpecialChars(
              node->doc,
              (const xmlChar *)StringValueCStr(string)
            );

  encoded_str = NOKOGIRI_STR_NEW2(encoded);
  xmlFree(encoded);

  return encoded_str;
}
```

    
  

    
      
  
### 
  
    #**external_subset**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
external_subset()

```

Get the external subset

  

  

  
    
      

```

921
922
923
924
925
926
927
928
929
930
931
932
933
934
935
936
937
938
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 921

static VALUE
external_subset(VALUE self)
{
  xmlNodePtr node;
  xmlDocPtr doc;
  xmlDtdPtr dtd;

  Noko_Node_Get_Struct(self, xmlNode, node);

  if (!node->doc) { return Qnil; }

  doc = node->doc;
  dtd = doc->extSubset;

  if (!dtd) { return Qnil; }

  return noko_xml_node_wrap(Qnil, (xmlNodePtr)dtd);
}
```

    
  

    
      
  
### 
  
    #**first_element_child**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
first_element_child() → Node

```

Returns

The first child Node that is an element.

**Example:**

Note that the “hello” child, which is a Text node, is skipped and the `<span>` element is returned.

```
div = Nokogiri::HTML5("<div>hello<span>world</span>").at_css("div")
div.first_element_child
# => #(Element:0x3c { name = "span", children = [ #(Text "world")] })

```

  

  

  
    
      

```

1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1157

static VALUE
rb_xml_node_first_element_child(VALUE self)
{
  xmlNodePtr node, child;
  Noko_Node_Get_Struct(self, xmlNode, node);

  child = xmlFirstElementChild(node);
  if (!child) { return Qnil; }

  return noko_xml_node_wrap(Qnil, child);
}
```

    
  

    
      
  
### 
  
    #**fragment**(tags)  ⇒ Object 
  

  

  

  
    

Create a DocumentFragment containing `tags` that is relative to *this* context node.

  

  

  
    
      

```

1097
1098
1099
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1097

def fragment(tags)
  document.related_class("DocumentFragment").new(document, tags, self)
end
```

    
  

    
      
  
### 
  
    #**fragment?**  ⇒ Boolean 
  

  

  

  
    

Returns true if this is a DocumentFragment

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1244
1245
1246
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1244

def fragment?
  type == DOCUMENT_FRAG_NODE
end
```

    
  

    
      
  
### 
  
    #**html?**  ⇒ Boolean 
  

  

  

  
    

Returns true if this is an HTML4::Document or HTML5::Document node

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1224
1225
1226
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1224

def html?
  type == HTML_DOCUMENT_NODE
end
```

    
  

    
      
  
### 
  
    #**inner_html**(*args)  ⇒ Object 
  

  

  

  
    

Get the inner_html for this node’s Node#children

  

  

  
    
      

```

1279
1280
1281
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1279

def inner_html(*args)
  children.map { |x| x.to_html(*args) }.join
end
```

    
  

    
      
  
### 
  
    #**inner_html=**(node_or_tags)  ⇒ Object 
  

  

  

  
    

Set the content for this Node to `node_or_tags`.

`node_or_tags` can be a Nokogiri::XML::Node, a Nokogiri::XML::DocumentFragment, or a String containing markup.

⚠ Please note that despite the name, this method will **not** always parse a String argument as HTML. A String argument will be parsed with the `DocumentFragment` parser related to this node’s document.

For example, if the document is an HTML4::Document then the string will be parsed as HTML4 using HTML4::DocumentFragment; but if the document is an XML::Document then it will parse the string as XML using XML::DocumentFragment.

Also see related method `children=`

  

  

  
    
      

```

374
375
376
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 374

def inner_html=(node_or_tags)
  self.children = node_or_tags
end
```

    
  

    
      
  
### 
  
    #**internal_subset**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
internal_subset()

```

Get the internal subset

  

  

  
    
      

```

946
947
948
949
950
951
952
953
954
955
956
957
958
959
960
961
962
963
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 946

static VALUE
internal_subset(VALUE self)
{
  xmlNodePtr node;
  xmlDocPtr doc;
  xmlDtdPtr dtd;

  Noko_Node_Get_Struct(self, xmlNode, node);

  if (!node->doc) { return Qnil; }

  doc = node->doc;
  dtd = xmlGetIntSubset(doc);

  if (!dtd) { return Qnil; }

  return noko_xml_node_wrap(Qnil, (xmlNodePtr)dtd);
}
```

    
  

    
      
  
### 
  
    #**key?**(attribute)  ⇒ Boolean 
  

  
    Also known as:
    has_attribute?
    
  

  

  
    

Returns true if `attribute` is set

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1202
1203
1204
1205
1206
1207
1208
1209
1210
1211
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1202

static VALUE
key_eh(VALUE self, VALUE attribute)
{
  xmlNodePtr node;
  Noko_Node_Get_Struct(self, xmlNode, node);
  if (xmlHasProp(node, (xmlChar *)StringValueCStr(attribute))) {
    return Qtrue;
  }
  return Qfalse;
}
```

    
  

    
      
  
### 
  
    #**keys**  ⇒ Object 
  

  

  

  
    

Get the attribute names for this Node.

  

  

  
    
      

```

704
705
706
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 704

def keys
  attribute_nodes.map(&:node_name)
end
```

    
  

    
      
  
### 
  
    #**kwattr_add**(attribute_name, keywords)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
kwattr_add(attribute_name, keywords) → self

```

Ensure that values are present in a keyword attribute.

Any values in `keywords` that already exist in the Node’s attribute values are *not* added. Note that any existing duplicates in the attribute values are not removed. Compare with #kwattr_append.

A “keyword attribute” is a node attribute that contains a set of space-delimited values. Perhaps the most familiar example of this is the HTML “class” attribute used to contain CSS classes. But other keyword attributes exist, for instance the “rel” attribute.

See also #add_class, #kwattr_values, #kwattr_append, #kwattr_remove
Parameters

- 

`attribute_name` (String) The name of the keyword attribute to be modified.

- 

`keywords` (String, Array<String>) Keywords to be added to the attribute named `attribute_name`. May be a string containing whitespace-delimited values, or an Array of String values. Any values already present will not be added. Any values not present will be added. If the named attribute does not exist, it is created.

Returns

`self` (Nokogiri::XML::Node) for ease of chaining method calls.

**Example:** Ensure that a `Node` has “nofollow” in its `rel` attribute.

Note that duplicates are not added.

```
node                               # => <a></a>
node.kwattr_add("rel", "nofollow") # => <a rel="nofollow"></a>
node.kwattr_add("rel", "nofollow") # => <a rel="nofollow"></a>

```

**Example:** Ensure that a `Node` has “nofollow” and “noreferrer” in its `rel` attribute, via a String argument.

```
Note that "nofollow" is not added because it is already present. Note also that the
pre-existing duplicate "nofollow" is not removed.

 node                                          # => <a rel="nofollow nofollow"></a>
 node.kwattr_add("rel", "nofollow noreferrer") # => <a rel="nofollow nofollow noreferrer"></a>

```

**Example:** Ensure that a `Node` has “nofollow” and “noreferrer” in its `rel` attribute, via an Array argument.

```
node                                               # => <a></a>
node.kwattr_add("rel", ["nofollow", "noreferrer"]) # => <a rel="nofollow noreferrer"></a>

```

Since v1.11.0

  

  

  
    
      

```

967
968
969
970
971
972
973
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 967

def kwattr_add(attribute_name, keywords)
  keywords = keywordify(keywords)
  current_kws = kwattr_values(attribute_name)
  new_kws = (current_kws + (keywords - current_kws)).join(" ")
  set_attribute(attribute_name, new_kws)
  self
end
```

    
  

    
      
  
### 
  
    #**kwattr_append**(attribute_name, keywords)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
kwattr_append(attribute_name, keywords) → self

```

Add keywords to a Node’s keyword attribute, regardless of duplication. Compare with #kwattr_add.

A “keyword attribute” is a node attribute that contains a set of space-delimited values. Perhaps the most familiar example of this is the HTML “class” attribute used to contain CSS classes. But other keyword attributes exist, for instance the “rel” attribute.

See also #append_class, #kwattr_values, #kwattr_add, #kwattr_remove
Parameters

- 

`attribute_name` (String) The name of the keyword attribute to be modified.

- 

`keywords` (String, Array<String>) Keywords to be added to the attribute named `attribute_name`. May be a string containing whitespace-delimited values, or an Array of String values. All values passed in will be appended to the named attribute even if they are already present in the attribute. If the named attribute does not exist, it is created.

Returns

`self` (Node) for ease of chaining method calls.

**Example:** Append “nofollow” to the `rel` attribute.

Note that duplicates are added.

```
node                                  # => <a></a>
node.kwattr_append("rel", "nofollow") # => <a rel="nofollow"></a>
node.kwattr_append("rel", "nofollow") # => <a rel="nofollow nofollow"></a>

```

**Example:** Append “nofollow” and “noreferrer” to the `rel` attribute, via a String argument.

Note that “nofollow” is appended even though it is already present.

```
node                                             # => <a rel="nofollow"></a>
node.kwattr_append("rel", "nofollow noreferrer") # => <a rel="nofollow nofollow noreferrer"></a>

```

**Example:** Append “nofollow” and “noreferrer” to the `rel` attribute, via an Array argument.

```
node                                                  # => <a></a>
node.kwattr_append("rel", ["nofollow", "noreferrer"]) # => <a rel="nofollow noreferrer"></a>

```

Since v1.11.0

  

  

  
    
      

```

1020
1021
1022
1023
1024
1025
1026
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1020

def kwattr_append(attribute_name, keywords)
  keywords = keywordify(keywords)
  current_kws = kwattr_values(attribute_name)
  new_kws = (current_kws + keywords).join(" ")
  set_attribute(attribute_name, new_kws)
  self
end
```

    
  

    
      
  
### 
  
    #**kwattr_remove**(attribute_name, keywords)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
kwattr_remove(attribute_name, keywords) → self

```

Remove keywords from a keyword attribute. Any matching keywords that exist in the named attribute are removed, including any multiple entries.

If no keywords remain after this operation, or if `keywords` is `nil`, the attribute is deleted from the node.

A “keyword attribute” is a node attribute that contains a set of space-delimited values. Perhaps the most familiar example of this is the HTML “class” attribute used to contain CSS classes. But other keyword attributes exist, for instance the “rel” attribute.

See also #remove_class, #kwattr_values, #kwattr_add, #kwattr_append
Parameters

- 

`attribute_name` (String) The name of the keyword attribute to be modified.

- 

`keywords` (String, Array<String>) Keywords to be removed from the attribute named `attribute_name`. May be a string containing whitespace-delimited values, or an Array of String values. Any keywords present in the named attribute will be removed. If no keywords remain, or if `keywords` is nil, the attribute is deleted.

Returns

`self` (Node) for ease of chaining method calls.

**Example:**

Note that the `rel` attribute is deleted when empty.

```
node                                    # => <a rel="nofollow noreferrer">link</a>
node.kwattr_remove("rel", "nofollow")   # => <a rel="noreferrer">link</a>
node.kwattr_remove("rel", "noreferrer") # => <a>link</a>

```

Since v1.11.0

  

  

  
    
      

```

1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1063

def kwattr_remove(attribute_name, keywords)
  if keywords.nil?
    remove_attribute(attribute_name)
    return self
  end

  keywords = keywordify(keywords)
  current_kws = kwattr_values(attribute_name)
  new_kws = current_kws - keywords
  if new_kws.empty?
    remove_attribute(attribute_name)
  else
    set_attribute(attribute_name, new_kws.join(" "))
  end
  self
end
```

    
  

    
      
  
### 
  
    #**kwattr_values**(attribute_name)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
kwattr_values(attribute_name) → Array<String>

```

Fetch values from a keyword attribute of a Node.

A “keyword attribute” is a node attribute that contains a set of space-delimited values. Perhaps the most familiar example of this is the HTML “class” attribute used to contain CSS classes. But other keyword attributes exist, for instance the “rel” attribute.

See also #classes, #kwattr_add, #kwattr_append, #kwattr_remove
Parameters

- 

`attribute_name` (String) The name of the keyword attribute to be inspected.

Returns

(Array<String>) The values present in the Node’s `attribute_name` attribute. If the attribute is empty or non-existent, the return value is an empty array.

**Example:**

```
node                      # => <a rel="nofollow noopener external">link</a>
node.kwattr_values("rel") # => ["nofollow", "noopener", "external"]

```

Since v1.11.0

  

  

  
    
      

```

913
914
915
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 913

def kwattr_values(attribute_name)
  keywordify(get_attribute(attribute_name) || [])
end
```

    
  

    
      
  
### 
  
    #**lang**  ⇒ Object 
  

  

  

  
    

Searches the language of a node, i.e. the values of the xml:lang attribute or the one carried by the nearest ancestor.

  

  
  

  
    
      

```

1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1577

static VALUE
get_lang(VALUE self_rb)
{
  xmlNodePtr self ;
  xmlChar *lang ;
  VALUE lang_rb ;

  Noko_Node_Get_Struct(self_rb, xmlNode, self);

  lang = xmlNodeGetLang(self);
  if (lang) {
    lang_rb = NOKOGIRI_STR_NEW2(lang);
    xmlFree(lang);
    return lang_rb ;
  }

  return Qnil ;
}
```

    
  

    
      
  
### 
  
    #**lang=**  ⇒ Object 
  

  

  

  
    

Set the language of a node, i.e. the values of the xml:lang attribute.

  

  
  

  
    
      

```

1556
1557
1558
1559
1560
1561
1562
1563
1564
1565
1566
1567
1568
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1556

static VALUE
set_lang(VALUE self_rb, VALUE lang_rb)
{
  xmlNodePtr self ;
  xmlChar *lang ;

  Noko_Node_Get_Struct(self_rb, xmlNode, self);
  lang = (xmlChar *)StringValueCStr(lang_rb);

  xmlNodeSetLang(self, lang);

  return Qnil ;
}
```

    
  

    
      
  
### 
  
    #**last_element_child**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
last_element_child() → Node

```

Returns

The last child Node that is an element.

**Example:**

Note that the “hello” child, which is a Text node, is skipped and the `<span>yes</span>` element is returned.

```
div = Nokogiri::HTML5("<div><span>no</span><span>yes</span>skip</div>").at_css("div")
div.last_element_child
# => #(Element:0x3c { name = "span", children = [ #(Text "yes")] })

```

  

  

  
    
      

```

1184
1185
1186
1187
1188
1189
1190
1191
1192
1193
1194
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1184

static VALUE
rb_xml_node_last_element_child(VALUE self)
{
  xmlNodePtr node, child;
  Noko_Node_Get_Struct(self, xmlNode, node);

  child = xmlLastElementChild(node);
  if (!child) { return Qnil; }

  return noko_xml_node_wrap(Qnil, child);
}
```

    
  

    
      
  
### 
  
    #**line**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
line() → Integer

```

Returns

The line number of this Node.

---

** ⚠ The CRuby and JRuby implementations differ in important ways! **

Semantic differences:

- 

The CRuby method reflects the node’s line number *in the parsed string*

- 

The JRuby method reflects the node’s line number *in the final DOM structure* after corrections have been applied

Performance differences:

- 

The CRuby method is O(1) (constant time)

- 

The JRuby method is O(n) (linear time, where n is the number of nodes before/above the element in the DOM)

If you’d like to help improve the JRuby implementation, please review these issues and reach out to the maintainers:

- 

github.com/sparklemotion/nokogiri/issues/1223

- 

github.com/sparklemotion/nokogiri/pull/2177

- 

github.com/sparklemotion/nokogiri/issues/2380

  

  

  
    
      

```

2040
2041
2042
2043
2044
2045
2046
2047
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 2040

static VALUE
rb_xml_node_line(VALUE rb_node)
{
  xmlNodePtr c_node;
  Noko_Node_Get_Struct(rb_node, xmlNode, c_node);

  return LONG2NUM(xmlGetLineNo(c_node));
}
```

    
  

    
      
  
### 
  
    #**line=**(num)  ⇒ Object 
  

  

  

  
    

Sets the line for this Node. num must be less than 65535.

  

  
  

  
    
      

```

2055
2056
2057
2058
2059
2060
2061
2062
2063
2064
2065
2066
2067
2068
2069
2070
2071
2072
2073
2074
2075
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 2055

static VALUE
rb_xml_node_line_set(VALUE rb_node, VALUE rb_line_number)
{
  xmlNodePtr c_node;
  int line_number = NUM2INT(rb_line_number);

  Noko_Node_Get_Struct(rb_node, xmlNode, c_node);

  // libxml2 optionally uses xmlNode.psvi to store longer line numbers, but only for text nodes.
  // search for "psvi" in SAX2.c and tree.c to learn more.
  if (line_number < 65535) {
    c_node->line = (short unsigned)line_number;
  } else {
    c_node->line = 65535;
    if (c_node->type == XML_TEXT_NODE) {
      c_node->psvi = (void *)(ptrdiff_t)line_number;
    }
  }

  return rb_line_number;
}
```

    
  

    
      
  
### 
  
    #**matches?**(selector)  ⇒ Boolean 
  

  

  

  
    

Returns true if this Node matches `selector`

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1090
1091
1092
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1090

def matches?(selector)
  ancestors.last.search(selector).include?(self)
end
```

    
  

    
      
  
### 
  
    #**namespace**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
namespace() → Namespace

```

Returns

The Namespace of the element or attribute node, or `nil` if there is no namespace.

**Example:**

```
doc = Nokogiri::XML(<<~EOF)
  <root>
    <first/>
    <second xmlns="http://example.com/child"/>
    <foo:third xmlns:foo="http://example.com/foo"/>
  </root>
EOF
doc.at_xpath("//first").namespace
# => nil
doc.at_xpath("//xmlns:second", "xmlns" => "http://example.com/child").namespace
# => #(Namespace:0x3c { href = "http://example.com/child" })
doc.at_xpath("//foo:third", "foo" => "http://example.com/foo").namespace
# => #(Namespace:0x50 { prefix = "foo", href = "http://example.com/foo" })

```

  

  

  
    
      

```

1362
1363
1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1362

static VALUE
rb_xml_node_namespace(VALUE rb_node)
{
  xmlNodePtr c_node ;
  Noko_Node_Get_Struct(rb_node, xmlNode, c_node);

  if (c_node->ns) {
    return noko_xml_namespace_wrap(c_node->ns, c_node->doc);
  }

  return Qnil ;
}
```

    
  

    
      
  
### 
  
    #**namespace=**(ns)  ⇒ Object 
  

  

  

  
    

Set the default namespace on this node (as would be defined with an “xmlns=” attribute in XML source), as a Namespace object `ns`. Note that a Namespace added this way will NOT be serialized as an xmlns attribute for this node. You probably want #default_namespace= instead, or perhaps #add_namespace_definition with a nil prefix argument.

  

  

  
    
      

```

513
514
515
516
517
518
519
520
521
522
523
524
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 513

def namespace=(ns)
  return set_namespace(ns) unless ns

  unless Nokogiri::XML::Namespace === ns
    raise TypeError, "#{ns.class} can't be coerced into Nokogiri::XML::Namespace"
  end
  if ns.document != document
    raise ArgumentError, "namespace must be declared on the same document"
  end

  set_namespace(ns)
end
```

    
  

    
      
  
### 
  
    #**namespace_definitions**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
namespace_definitions() → Array<Nokogiri::XML::Namespace>

```

Returns

Namespaces that are defined directly on this node, as an Array of Namespace objects. The array will be empty if no namespaces are defined on this node.

**Example:**

```
doc = Nokogiri::XML(<<~EOF)
  <root xmlns="http://example.com/root">
    <first/>
    <second xmlns="http://example.com/child" xmlns:unused="http://example.com/unused"/>
    <foo:third xmlns:foo="http://example.com/foo"/>
  </root>
EOF
doc.at_xpath("//root:first", "root" => "http://example.com/root").namespace_definitions
# => []
doc.at_xpath("//xmlns:second", "xmlns" => "http://example.com/child").namespace_definitions
# => [#(Namespace:0x3c { href = "http://example.com/child" }),
#     #(Namespace:0x50 {
#       prefix = "unused",
#       href = "http://example.com/unused"
#       })]
doc.at_xpath("//foo:third", "foo" => "http://example.com/foo").namespace_definitions
# => [#(Namespace:0x64 { prefix = "foo", href = "http://example.com/foo" })]

```

  

  

  
    
      

```

1403
1404
1405
1406
1407
1408
1409
1410
1411
1412
1413
1414
1415
1416
1417
1418
1419
1420
1421
1422
1423
1424
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1403

static VALUE
namespace_definitions(VALUE rb_node)
{
  /* this code in the mode of xmlHasProp() */
  xmlNodePtr c_node ;
  xmlNsPtr c_namespace;
  VALUE definitions = rb_ary_new();

  Noko_Node_Get_Struct(rb_node, xmlNode, c_node);

  c_namespace = c_node->nsDef;
  if (!c_namespace) {
    return definitions;
  }

  while (c_namespace != NULL) {
    rb_ary_push(definitions, noko_xml_namespace_wrap(c_namespace, c_node->doc));
    c_namespace = c_namespace->next;
  }

  return definitions;
}
```

    
  

    
      
  
### 
  
    #**namespace_scopes**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
namespace_scopes() → Array<Nokogiri::XML::Namespace>

```

Returns

Array of all the Namespaces on this node and its ancestors.

See also #namespaces

**Example:**

```
doc = Nokogiri::XML(<<~EOF)
  <root xmlns="http://example.com/root" xmlns:bar="http://example.com/bar">
    <first/>
    <second xmlns="http://example.com/child"/>
    <third xmlns:foo="http://example.com/foo"/>
  </root>
EOF
doc.at_xpath("//root:first", "root" => "http://example.com/root").namespace_scopes
# => [#(Namespace:0x3c { href = "http://example.com/root" }),
#     #(Namespace:0x50 { prefix = "bar", href = "http://example.com/bar" })]
doc.at_xpath("//child:second", "child" => "http://example.com/child").namespace_scopes
# => [#(Namespace:0x64 { href = "http://example.com/child" }),
#     #(Namespace:0x50 { prefix = "bar", href = "http://example.com/bar" })]
doc.at_xpath("//root:third", "root" => "http://example.com/root").namespace_scopes
# => [#(Namespace:0x78 { prefix = "foo", href = "http://example.com/foo" }),
#     #(Namespace:0x3c { href = "http://example.com/root" }),
#     #(Namespace:0x50 { prefix = "bar", href = "http://example.com/bar" })]

```

  

  

  
    
      

```

1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1454

static VALUE
rb_xml_node_namespace_scopes(VALUE rb_node)
{
  xmlNodePtr c_node ;
  xmlNsPtr *namespaces;
  VALUE scopes = rb_ary_new();
  int j;

  Noko_Node_Get_Struct(rb_node, xmlNode, c_node);

  namespaces = xmlGetNsList(c_node->doc, c_node);
  if (!namespaces) {
    return scopes;
  }

  for (j = 0 ; namespaces[j] != NULL ; ++j) {
    rb_ary_push(scopes, noko_xml_namespace_wrap(namespaces[j], c_node->doc));
  }

  xmlFree(namespaces);
  return scopes;
}
```

    
  

    
      
  
### 
  
    #**namespaced_key?**(attribute, namespace)  ⇒ Boolean 
  

  

  

  
    

Returns true if `attribute` is set with `namespace`

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1219
1220
1221
1222
1223
1224
1225
1226
1227
1228
1229
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1219

static VALUE
namespaced_key_eh(VALUE self, VALUE attribute, VALUE namespace)
{
  xmlNodePtr node;
  Noko_Node_Get_Struct(self, xmlNode, node);
  if (xmlHasNsProp(node, (xmlChar *)StringValueCStr(attribute),
                   NIL_P(namespace) ? NULL : (xmlChar *)StringValueCStr(namespace))) {
    return Qtrue;
  }
  return Qfalse;
}
```

    
  

    
      
  
### 
  
    #**namespaces**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
namespaces() → Hash<String(Namespace#prefix) ⇒ String(Namespace#href)>

```

Fetch all the namespaces on this node and its ancestors.

Note that the keys in this hash XML attributes that would be used to define this namespace, such as “xmlns:prefix”, not just the prefix.

The default namespace for this node will be included with key “xmlns”.

See also #namespace_scopes
Returns

Hash containing all the namespaces on this node and its ancestors. The hash keys are the namespace prefix, and the hash value for each key is the namespace URI.

**Example:**

```
doc = Nokogiri::XML(<<~EOF)
  <root xmlns="http://example.com/root" xmlns:in_scope="http://example.com/in_scope">
    <first/>
    <second xmlns="http://example.com/child"/>
    <third xmlns:foo="http://example.com/foo"/>
  </root>
EOF
doc.at_xpath("//root:first", "root" => "http://example.com/root").namespaces
# => {"xmlns"=>"http://example.com/root",
#     "xmlns:in_scope"=>"http://example.com/in_scope"}
doc.at_xpath("//child:second", "child" => "http://example.com/child").namespaces
# => {"xmlns"=>"http://example.com/child",
#     "xmlns:in_scope"=>"http://example.com/in_scope"}
doc.at_xpath("//root:third", "root" => "http://example.com/root").namespaces
# => {"xmlns:foo"=>"http://example.com/foo",
#     "xmlns"=>"http://example.com/root",
#     "xmlns:in_scope"=>"http://example.com/in_scope"}

```

  

  

  
    
      

```

1200
1201
1202
1203
1204
1205
1206
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1200

def namespaces
  namespace_scopes.each_with_object({}) do |ns, hash|
    prefix = ns.prefix
    key = prefix ? "xmlns:#{prefix}" : "xmlns"
    hash[key] = ns.href
  end
end
```

    
  

    
      
  
### 
  
    #**native_content=**(input)  ⇒ Object 
  

  

  

  
    

Set the content of this node to `input`.
Parameters

- 

`input` (String) The new content for this node.

⚠ This method behaves differently depending on the node type. For Text, CDATA, Comment, and ProcessingInstruction nodes, it treats the input as raw content, which means that the final DOM will contain the entity-escaped version of the input (see example below). For Element and Attr nodes, it treats the input as parsed content and expects it to be valid markup that is already entity-escaped.

💡 Use Node#content= for a more consistent API across node types.
Example

Note the behavior differences of this method between Text and Element nodes:

```
doc = Nokogiri::HTML::Document.parse(<<~HTML)
  <html>
    <body>
      <div id="first">asdf</div>
      <div id="second">asdf</div>
HTML

text_node = doc.at_css("div#first").children.first
div_node = doc.at_css("div#second")

value = "You & Me"

text_node.native_content = value
div_node.native_content = value

doc.css("div").to_html
# => "<div id=\"first\">You &amp; Me</div>
#     <div id=\"second\">You & Me</div>"

```

See also: #content=

  

  
  

  
    
      

```

1532
1533
1534
1535
1536
1537
1538
1539
1540
1541
1542
1543
1544
1545
1546
1547
1548
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1532

static VALUE
set_native_content(VALUE self, VALUE content)
{
  xmlNodePtr node, child, next ;
  Noko_Node_Get_Struct(self, xmlNode, node);

  child = node->children;
  while (NULL != child) {
    next = child->next ;
    xmlUnlinkNode(child) ;
    noko_xml_document_pin_node(child);
    child = next ;
  }

  xmlNodeSetContent(node, (xmlChar *)StringValueCStr(content));
  return content;
}
```

    
  

    
      
  
### 
  
    #**next_element**  ⇒ Object 
  

  

  

  
    

Returns the next Nokogiri::XML::Element type sibling node.

  

  
  

  
    
      

```

1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1050

static VALUE
next_element(VALUE self)
{
  xmlNodePtr node, sibling;
  Noko_Node_Get_Struct(self, xmlNode, node);

  sibling = xmlNextElementSibling(node);
  if (!sibling) { return Qnil; }

  return noko_xml_node_wrap(Qnil, sibling);
}
```

    
  

    
      
  
### 
  
    #**next_sibling**  ⇒ Object 
  

  
    Also known as:
    next
    
  

  

  
    

Returns the next sibling node

  

  
  

  
    
      

```

1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1014

static VALUE
next_sibling(VALUE self)
{
  xmlNodePtr node, sibling;
  Noko_Node_Get_Struct(self, xmlNode, node);

  sibling = node->next;
  if (!sibling) { return Qnil; }

  return noko_xml_node_wrap(Qnil, sibling) ;
}
```

    
  

    
      
  
### 
  
    #**name**  ⇒ Object 
  

  
    Also known as:
    name
    
  

  

  
    

Returns the name for this Node

  

  
  

  
    
      

```

1642
1643
1644
1645
1646
1647
1648
1649
1650
1651
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1642

static VALUE
get_name(VALUE self)
{
  xmlNodePtr node;
  Noko_Node_Get_Struct(self, xmlNode, node);
  if (node->name) {
    return NOKOGIRI_STR_NEW2(node->name);
  }
  return Qnil;
}
```

    
  

    
      
  
### 
  
    #**name=**(new_name)  ⇒ Object 
  

  
    Also known as:
    name=
    
  

  

  
    

Set the name for this Node

  

  
  

  
    
      

```

1627
1628
1629
1630
1631
1632
1633
1634
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1627

static VALUE
set_name(VALUE self, VALUE new_name)
{
  xmlNodePtr node;
  Noko_Node_Get_Struct(self, xmlNode, node);
  xmlNodeSetName(node, (xmlChar *)StringValueCStr(new_name));
  return new_name;
}
```

    
  

    
      
  
### 
  
    #**node_type**  ⇒ Object 
  

  
    Also known as:
    type
    
  

  

  
    

Get the type for this Node

  

  
  

  
    
      

```

1483
1484
1485
1486
1487
1488
1489
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1483

static VALUE
node_type(VALUE self)
{
  xmlNodePtr node;
  Noko_Node_Get_Struct(self, xmlNode, node);
  return INT2NUM(node->type);
}
```

    
  

    
      
  
### 
  
    #**parent**  ⇒ Object 
  

  

  

  
    

Get the parent Node for this Node

  

  
  

  
    
      

```

1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1609

static VALUE
get_parent(VALUE self)
{
  xmlNodePtr node, parent;
  Noko_Node_Get_Struct(self, xmlNode, node);

  parent = node->parent;
  if (!parent) { return Qnil; }

  return noko_xml_node_wrap(Qnil, parent) ;
}
```

    
  

    
      
  
### 
  
    #**parent=**(parent_node)  ⇒ Object 
  

  

  

  
    

Set the parent Node for this Node

  

  

  
    
      

```

493
494
495
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 493

def parent=(parent_node)
  parent_node.add_child(self)
end
```

    
  

    
      
  
### 
  
    #**parse**(string_or_io, options = nil) {|options| ... } ⇒ Object 
  

  

  

  
    

Parse `string_or_io` as a document fragment within the context of **this** node.  Returns a XML::NodeSet containing the nodes parsed from `string_or_io`.

  

  

Yields:

  
    
- 
      
      
        (options)
      
      
      
    
  

  
    
      

```

1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
1132
1133
1134
1135
1136
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1105

def parse(string_or_io, options = nil)
  ##
  # When the current node is unparented and not an element node, use the
  # document as the parsing context instead. Otherwise, the in-context
  # parser cannot find an element or a document node.
  # Document Fragments are also not usable by the in-context parser.
  if !element? && !document? && (!parent || parent.fragment?)
    return document.parse(string_or_io, options)
  end

  options ||= (document.html? ? ParseOptions::DEFAULT_HTML : ParseOptions::DEFAULT_XML)
  options = Nokogiri::XML::ParseOptions.new(options) if Integer === options
  yield options if block_given?

  contents = if string_or_io.respond_to?(:read)
    string_or_io.read
  else
    string_or_io
  end

  return Nokogiri::XML::NodeSet.new(document) if contents.empty?

  error_count = document.errors.length
  node_set = in_context(contents, options.to_i)

  if document.errors.length > error_count
    raise document.errors[error_count] unless options.recover?

    # TODO: remove this block when libxml2 < 2.13 is no longer supported
    if node_set.empty?
      # libxml2 < 2.13 does not obey the +recover+ option after encountering errors during
      # +in_context+ parsing, and so this horrible hack is here to try to emulate recovery
      # behavior.
      #
      # (Note that HTML4 fragment parsing seems to have been fixed in abd74186, and XML
      # fragment parsing is fixed in 1c106edf. Both are in 2.13.)
      #
      # Unfortunately, this means we're no longer parsing "in context" and so namespaces that
      # would have been inherited from the context node won't be handled correctly. This hack
      # was written in 2010, and I regret it, because it's silently degrading functionality in
      # a way that's not easily prevented (or even detected).
      #
      # I think preferable behavior would be to either:
      #
      # a. add an error noting that we "fell back" and pointing the user to turning off the
      #    +recover+ option
      # b. don't recover, but raise a sensible exception
      #
      # For context and background:
      # - https://github.com/sparklemotion/nokogiri/issues/313
      # - https://github.com/sparklemotion/nokogiri/issues/2092
      fragment = document.related_class("DocumentFragment").parse(contents)
      node_set = fragment.children
    end
  end

  node_set
end
```

    
  

    
      
  
### 
  
    #**path**  ⇒ Object 
  

  

  

  
    

Returns the path associated with this Node

  

  
  

  
    
      

```

1659
1660
1661
1662
1663
1664
1665
1666
1667
1668
1669
1670
1671
1672
1673
1674
1675
1676
1677
1678
1679
1680
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1659

static VALUE
rb_xml_node_path(VALUE rb_node)
{
  xmlNodePtr c_node;
  xmlChar *c_path ;
  VALUE rval;

  Noko_Node_Get_Struct(rb_node, xmlNode, c_node);

  c_path = xmlGetNodePath(c_node);
  if (c_path == NULL) {
    // see https://github.com/sparklemotion/nokogiri/issues/2250
    // this behavior is clearly undesirable, but is what libxml <= 2.9.10 returned, and so we
    // do this for now to preserve the behavior across libxml2 versions.
    rval = NOKOGIRI_STR_NEW2("?");
  } else {
    rval = NOKOGIRI_STR_NEW2(c_path);
    xmlFree(c_path);
  }

  return rval ;
}
```

    
  

    
      
  
### 
  
    #**pointer_id**  ⇒ Object 
  

  

  

  
    

:call-seq: pointer_id() → Integer
Returns

A unique id for this node based on the internal memory structures. This method is used by #== to determine node identity.

  

  

  
    
      

```

810
811
812
813
814
815
816
817
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 810

static VALUE
rb_xml_node_pointer_id(VALUE self)
{
  xmlNodePtr node;
  Noko_Node_Get_Struct(self, xmlNode, node);

  return rb_uint2inum((uintptr_t)(node));
}
```

    
  

    
      
  
### 
  
    #**prepend_child**(node_or_tags)  ⇒ Object 
  

  

  

  
    

Add `node_or_tags` as the first child of this Node.

`node_or_tags` can be a Nokogiri::XML::Node, a ::DocumentFragment, a ::NodeSet, or a String containing markup.

Returns the reparented node (if `node_or_tags` is a Node), or NodeSet (if `node_or_tags` is a DocumentFragment, NodeSet, or String).

Also see related method `add_child`.

  

  

  
    
      

```

204
205
206
207
208
209
210
211
212
213
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 204

def prepend_child(node_or_tags)
  if (first = children.first)
    # Mimic the error add_child would raise.
    raise "Document already has a root node" if document? && !(node_or_tags.comment? || node_or_tags.processing_instruction?)

    first.__send__(:add_sibling, :previous, node_or_tags)
  else
    add_child(node_or_tags)
  end
end
```

    
  

    
      
  
### 
  
    #**previous_element**  ⇒ Object 
  

  

  

  
    

Returns the previous Nokogiri::XML::Element type sibling node.

  

  
  

  
    
      

```

1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1068

static VALUE
previous_element(VALUE self)
{
  xmlNodePtr node, sibling;
  Noko_Node_Get_Struct(self, xmlNode, node);

  sibling = xmlPreviousElementSibling(node);
  if (!sibling) { return Qnil; }

  return noko_xml_node_wrap(Qnil, sibling);
}
```

    
  

    
      
  
### 
  
    #**previous_sibling**  ⇒ Object 
  

  
    Also known as:
    previous
    
  

  

  
    

Returns the previous sibling node

  

  
  

  
    
      

```

1032
1033
1034
1035
1036
1037
1038
1039
1040
1041
1042
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 1032

static VALUE
previous_sibling(VALUE self)
{
  xmlNodePtr node, sibling;
  Noko_Node_Get_Struct(self, xmlNode, node);

  sibling = node->prev;
  if (!sibling) { return Qnil; }

  return noko_xml_node_wrap(Qnil, sibling);
}
```

    
  

    
      
  
### 
  
    #**processing_instruction?**  ⇒ Boolean 
  

  

  

  
    

Returns true if this is a ProcessingInstruction node

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1234
1235
1236
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1234

def processing_instruction?
  type == PI_NODE
end
```

    
  

    
      
  
### 
  
    #**read_only?**  ⇒ Boolean 
  

  

  

  
    

Is this a read only node?

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1259
1260
1261
1262
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1259

def read_only?
  # According to gdome2, these are read-only node types
  [NOTATION_NODE, ENTITY_NODE, ENTITY_DECL].include?(type)
end
```

    
  

    
      
  
### 
  
    #**remove_attribute**(name)  ⇒ Object 
  

  
    Also known as:
    delete
    
  

  

  
    

Remove the attribute named `name`

  

  

  
    
      

```

718
719
720
721
722
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 718

def remove_attribute(name)
  attr = attributes[name].remove if key?(name)
  clear_xpath_context if Nokogiri.jruby?
  attr
end
```

    
  

    
      
  
### 
  
    #**remove_class**(names = nil)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
remove_class(css_classes) → self

```

Remove HTML CSS classes from this node. Any CSS class names in `css_classes` that exist in this node’s “class” attribute are removed, including any multiple entries.

If no CSS classes remain after this operation, or if `css_classes` is `nil`, the “class” attribute is deleted from the node.

This is a convenience function and is equivalent to:

```
node.kwattr_remove("class", css_classes)

```

Also see #kwattr_remove, #classes, #add_class, #append_class
Parameters

- 

`css_classes` (String, Array<String>)

CSS class names to be removed from the Node’s “class” attribute. May be a string containing whitespace-delimited names, or an Array of String names. Any class names already present will be removed. If no CSS classes remain, the “class” attribute is deleted.

Returns

`self` (Nokogiri::XML::Node) for ease of chaining method calls.

**Example**: Deleting a CSS class

Note that all instances of the class “section” are removed from the “class” attribute.

```
node                         # => <div class="section header section"></div>
node.remove_class("section") # => <div class="header"></div>

```

**Example**: Deleting the only remaining CSS class

Note that the attribute is removed once there are no remaining classes.

```
node                         # => <div class="section"></div>
node.remove_class("section") # => <div></div>

```

**Example**: Deleting multiple CSS classes

Note that the “class” attribute is deleted once it’s empty.

```
node                                    # => <div class="section header float"></div>
node.remove_class(["section", "float"]) # => <div class="header"></div>

```

  

  

  
    
      

```

884
885
886
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 884

def remove_class(names = nil)
  kwattr_remove("class", names)
end
```

    
  

    
      
  
### 
  
    #**replace**(node_or_tags)  ⇒ Object 
  

  

  

  
    

Replace this Node with `node_or_tags`.

`node_or_tags` can be a Nokogiri::XML::Node, a ::DocumentFragment, a ::NodeSet, or a String containing markup.

Returns the reparented node (if `node_or_tags` is a Node), or NodeSet (if `node_or_tags` is a DocumentFragment, NodeSet, or String).

Also see related method `swap`.

  

  

  
    
      

```

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
418
419
420
421
422
423
424
425
426
427
428
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 405

def replace(node_or_tags)
  raise("Cannot replace a node with no parent") unless parent

  # We cannot replace a text node directly, otherwise libxml will return
  # an internal error at parser.c:13031, I don't know exactly why
  # libxml is trying to find a parent node that is an element or document
  # so I can't tell if this is bug in libxml or not. issue #775.
  if text?
    replacee = Nokogiri::XML::Node.new("dummy", document)
    add_previous_sibling_node(replacee)
    unlink
    return replacee.replace(node_or_tags)
  end

  node_or_tags = parent.coerce(node_or_tags)

  if node_or_tags.is_a?(XML::NodeSet)
    node_or_tags.each { |n| add_previous_sibling(n) }
    unlink
  else
    replace_node(node_or_tags)
  end
  node_or_tags
end
```

    
  

    
      
  
### 
  
    #**serialize**(*args, &block)  ⇒ Object 
  

  

  

  
    

Serialize Node using `options`. Save options can also be set using a block.

See also Nokogiri::XML::Node::SaveOptions and Node@Serialization+and+Generating+Output.

These two statements are equivalent:

```
node.serialize(encoding: 'UTF-8', save_with: FORMAT | AS_XML)

```

or

```
node.serialize(encoding: 'UTF-8') do |config|
  config.format.as_xml
end

```

  

  

  
    
      

```

1364
1365
1366
1367
1368
1369
1370
1371
1372
1373
1374
1375
1376
1377
1378
1379
1380
1381
1382
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1364

def serialize(*args, &block)
  # TODO: deprecate non-hash options, see 46c68ed 2009-06-20 for context
  options = if args.first.is_a?(Hash)
    args.shift
  else
    {
      encoding: args[0],
      save_with: args[1],
    }
  end

  options[:encoding] ||= document.encoding
  encoding = Encoding.find(options[:encoding] || "UTF-8")

  io = StringIO.new(String.new(encoding: encoding))

  write_to(io, options, &block)
  io.string
end
```

    
  

    
      
  
### 
  
    #**swap**(node_or_tags)  ⇒ Object 
  

  

  

  
    

Swap this Node for `node_or_tags`

`node_or_tags` can be a Nokogiri::XML::Node, a ::DocumentFragment, a ::NodeSet, or a String Containing markup.

Returns self, to support chaining of calls.

Also see related method `replace`.

  

  

  
    
      

```

439
440
441
442
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 439

def swap(node_or_tags)
  replace(node_or_tags)
  self
end
```

    
  

    
      
  
### 
  
    #**text?**  ⇒ Boolean 
  

  

  

  
    

Returns true if this is a Text node

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1239
1240
1241
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1239

def text?
  type == TEXT_NODE
end
```

    
  

    
      
  
### 
  
    #**to_html**(options = {})  ⇒ Object 
  

  

  

  
    

Serialize this Node to HTML

```
doc.to_html

```

See Node#write_to for a list of `options`.  For formatted output, use Node#to_xhtml instead.

  

  

  
    
      

```

1391
1392
1393
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1391

def to_html(options = {})
  to_format(SaveOptions::DEFAULT_HTML, options)
end
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    

Turn this node in to a string.  If the document is HTML, this method returns html.  If the document is XML, this method returns XML.

  

  

  
    
      

```

1274
1275
1276
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1274

def to_s
  document.xml? ? to_xml : to_html
end
```

    
  

    
      
  
### 
  
    #**to_xhtml**(options = {})  ⇒ Object 
  

  

  

  
    

Serialize this Node to XHTML using `options`

```
doc.to_xhtml(indent: 5, encoding: 'UTF-8')

```

See Node#write_to for a list of `options`

  

  

  
    
      

```

1412
1413
1414
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1412

def to_xhtml(options = {})
  to_format(SaveOptions::DEFAULT_XHTML, options)
end
```

    
  

    
      
  
### 
  
    #**to_xml**(options = {})  ⇒ Object 
  

  

  

  
    

Serialize this Node to XML using `options`

```
doc.to_xml(indent: 5, encoding: 'UTF-8')

```

See Node#write_to for a list of `options`

  

  

  
    
      

```

1401
1402
1403
1404
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1401

def to_xml(options = {})
  options[:save_with] ||= SaveOptions::DEFAULT_XML
  serialize(options)
end
```

    
  

    
      
  
### 
  
    #**traverse** {|_self| ... } ⇒ Object 
  

  

  

  
    

Yields self and all children to `block` recursively.

  

  

Yields:

  
    
- 
      
      
        (_self)
      
      
      
    
  

Yield Parameters:

  
    
- 
      
        _self
      
      
        (Nokogiri::XML::Node)
      
      
      
        —
        

the object that the method was called on

      
    
  

  
    
      

```

1317
1318
1319
1320
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1317

def traverse(&block)
  children.each { |j| j.traverse(&block) }
  yield(self)
end
```

    
  

    
      
  
### 
  
    #**unlink**  ⇒ Object 
  

  
    Also known as:
    remove
    
  

  

  
    

:call-seq:

```
unlink() → self

```

Unlink this node from its current context.

  

  

  
    
      

```

997
998
999
1000
1001
1002
1003
1004
1005
```

    
    
      

```
# File 'ext/nokogiri/xml_node.c', line 997

static VALUE
unlink_node(VALUE self)
{
  xmlNodePtr node;
  Noko_Node_Get_Struct(self, xmlNode, node);
  xmlUnlinkNode(node);
  noko_xml_document_pin_node(node);
  return self;
}
```

    
  

    
      
  
### 
  
    #**value?**(value)  ⇒ Boolean 
  

  

  

  
    

Does this Node’s attributes include <value>

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

698
699
700
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 698

def value?(value)
  values.include?(value)
end
```

    
  

    
      
  
### 
  
    #**values**  ⇒ Object 
  

  

  

  
    

Get the attribute values for this Node.

  

  

  
    
      

```

692
693
694
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 692

def values
  attribute_nodes.map(&:value)
end
```

    
  

    
      
  
### 
  
    #**wrap**(node_or_tags)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
wrap(markup) -> self
wrap(node) -> self

```

Wrap this Node with the node parsed from `markup` or a dup of the `node`.
Parameters

- 

**markup** (String) Markup that is parsed and used as the wrapper. This node’s parent, if it exists, is used as the context node for parsing; otherwise the associated document is used. If the parsed fragment has multiple roots, the first root node is used as the wrapper.

- 

**node** (Nokogiri::XML::Node) An element that is ‘#dup`ed and used as the wrapper.

Returns

`self`, to support chaining.

Also see NodeSet#wrap

**Example** with a `String` argument:

```
doc = Nokogiri::HTML5(<<~HTML)
  <html><body>
    <a>asdf</a>
  </body></html>
HTML
doc.at_css("a").wrap("<div></div>")
doc.to_html
# => <html><head></head><body>
#      <div><a>asdf</a></div>
#    </body></html>

```

**Example** with a `Node` argument:

```
doc = Nokogiri::HTML5(<<~HTML)
  <html><body>
    <a>asdf</a>
  </body></html>
HTML
doc.at_css("a").wrap(doc.create_element("div"))
doc.to_html
# <html><head></head><body>
#   <div><a>asdf</a></div>
# </body></html>

```

  

  

  
    
      

```

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
269
270
271
272
273
274
275
276
277
278
279
280
281
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 259

def wrap(node_or_tags)
  case node_or_tags
  when String
    context_node = parent || document
    new_parent = context_node.coerce(node_or_tags).first
    if new_parent.nil?
      raise "Failed to parse '#{node_or_tags}' in the context of a '#{context_node.name}' element"
    end
  when Node
    new_parent = node_or_tags.dup
  else
    raise ArgumentError, "Requires a String or Node argument, and cannot accept a #{node_or_tags.class}"
  end

  if parent
    add_next_sibling(new_parent)
  else
    new_parent.unlink
  end
  new_parent.add_child(self)

  self
end
```

    
  

    
      
  
### 
  
    #**write_html_to**(io, options = {})  ⇒ Object 
  

  

  

  
    

Write Node as HTML to `io` with `options`

See Node#write_to for a list of `options`

  

  

  
    
      

```

1469
1470
1471
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1469

def write_html_to(io, options = {})
  write_format_to(SaveOptions::DEFAULT_HTML, io, options)
end
```

    
  

    
      
  
### 
  
    #**write_to**(io, *options) {|config| ... } ⇒ Object 
  

  

  

  
    

:call-seq:

```
write_to(io, *options)

```

Serialize this node or document to `io`.
Parameters

- 

`io` (IO) An IO-like object to which the serialized content will be written.

- 

`options` (Hash) See below

Options

- 

`:encoding` (String or Encoding) specify the encoding of the output (defaults to document encoding)

- 

`:indent_text` (String) the indentation text (defaults to `" "`)

- 

`:indent` (Integer) the number of `:indent_text` to use (defaults to `2`)

- 

`:save_with` (Integer) a combination of SaveOptions constants

To save with UTF-8 indented twice:

```
node.write_to(io, encoding: 'UTF-8', indent: 2)

```

To save indented with two dashes:

```
node.write_to(io, indent_text: '-', indent: 2)

```

  

  

Yields:

  
    
- 
      
      
        (config)
      
      
      
    
  

  
    
      

```

1440
1441
1442
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1440

def write_to(io, *options)
  options = options.first.is_a?(Hash) ? options.shift : {}
  encoding = options[:encoding] || options[0] || document.encoding
  if Nokogiri.jruby?
    save_options = options[:save_with] || options[1]
    indent_times = options[:indent] || 0
  else
    save_options = options[:save_with] || options[1] || SaveOptions::FORMAT
    indent_times = options[:indent] || 2
  end
  indent_text = options[:indent_text] || " "

  # Any string times 0 returns an empty string. Therefore, use the same
  # string instead of generating a new empty string for every node with
  # zero indentation.
  indentation = indent_times.zero? ? "" : (indent_text * indent_times)

  config = SaveOptions.new(save_options.to_i)
  yield config if block_given?

  encoding = encoding.is_a?(Encoding) ? encoding.name : encoding

  native_write_to(io, encoding, indentation, config.options)
end
```

    
  

    
      
  
### 
  
    #**write_xhtml_to**(io, options = {})  ⇒ Object 
  

  

  

  
    

Write Node as XHTML to `io` with `options`

See Node#write_to for a list of `options`

  

  

  
    
      

```

1477
1478
1479
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1477

def write_xhtml_to(io, options = {})
  write_format_to(SaveOptions::DEFAULT_XHTML, io, options)
end
```

    
  

    
      
  
### 
  
    #**write_xml_to**(io, options = {})  ⇒ Object 
  

  

  

  
    

Write Node as XML to `io` with `options`

```
doc.write_xml_to io, :encoding => 'UTF-8'

```

See Node#write_to for a list of options

  

  

  
    
      

```

1487
1488
1489
1490
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1487

def write_xml_to(io, options = {})
  options[:save_with] ||= SaveOptions::DEFAULT_XML
  write_to(io, options)
end
```

    
  

    
      
  
### 
  
    #**xml?**  ⇒ Boolean 
  

  

  

  
    

Returns true if this is an XML::Document node

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

1219
1220
1221
```

    
    
      

```
# File 'lib/nokogiri/xml/node.rb', line 1219

def xml?
  type == DOCUMENT_NODE
end
```