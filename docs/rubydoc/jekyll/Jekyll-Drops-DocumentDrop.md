# Class: Jekyll::Drops::DocumentDrop
  
    Inherits:
    
      Drop
      
        

          
- Object

- Liquid::Drop

- Drop

- Jekyll::Drops::DocumentDrop

        show all
      
    
  
  

  
  
  
      Extended by:
      Forwardable
  
    Defined in:
    lib/jekyll/drops/document_drop.rb
  
## Direct Known Subclasses

ExcerptDrop

##

      Constant Summary
      collapse
    

    
      
        NESTED_OBJECT_FIELD_BLACKLIST =
          
        
        

```
%w(
  content output excerpt next previous
).freeze
```

### Constants inherited

     from Drop

Jekyll::Drops::Drop::NON_CONTENT_METHODS

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**<=>**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**collapse_document**(doc)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Generate a Hash which breaks the recursive chain.

-
  
      #**collection**  ⇒ Object 

-
  
      #**excerpt**  ⇒ Object 

-
  
      #**hash_for_json**(state = nil)  ⇒ Object 

Generate a Hash for use in generating JSON.

-
  
      #**name**  ⇒ Object 

-
  
      #**next**  ⇒ Object 

-
  
      #**previous**  ⇒ Object 

### Methods inherited from Drop

# [], #[]=, #content_methods, data_delegator, data_delegators, delegate_method, delegate_method_as, delegate_methods, #each, #each_key, #fetch, getter_method_names, #initialize, #inspect, #key?, #keys, #merge, #merge!, mutable, mutable?, private_delegate_methods, #to_h, #to_json

## Constructor Details

This class inherits a constructor from Jekyll::Drops::Drop
  
## Instance Method Details

###
  
    #**<=>**(other)  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
35
36
37
38
```

```
# File 'lib/jekyll/drops/document_drop.rb', line 32

def <=>(other)
  return nil unless other.is_a? DocumentDrop

  cmp = self["date"] <=> other["date"]
  cmp = self["path"] <=> other["path"] if cmp.nil? || cmp.zero?
  cmp
end
```

###
  
    #**collapse_document**(doc)  ⇒ Object 
  

  

  

  
    

Generate a Hash which breaks the recursive chain. Certain fields which are normally available are omitted.

Returns a Hash with only non-recursive fields present.

```

67
68
69
70
71
```

```
# File 'lib/jekyll/drops/document_drop.rb', line 67

def collapse_document(doc)
  doc.keys.each_with_object({}) do |(key, _), result|
    result[key] = doc[key] unless NESTED_OBJECT_FIELD_BLACKLIST.include?(key)
  end
end
```

###
  
    #**collection**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

```
# File 'lib/jekyll/drops/document_drop.rb', line 20

def collection
  @obj.collection.label
end
```

###
  
    #**excerpt**  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

```
# File 'lib/jekyll/drops/document_drop.rb', line 24

def excerpt
  fallback_data["excerpt"].to_s
end
```

###
  
    #**hash_for_json**(state = nil)  ⇒ Object 
  

  

  

  
    

Generate a Hash for use in generating JSON. This is useful if fields need to be cleared before the JSON can generate.

state - the JSON::State object which determines the state of current processing.

Returns a Hash ready for JSON generation.

```

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
# File 'lib/jekyll/drops/document_drop.rb', line 54

def hash_for_json(state = nil)
  to_h.tap do |hash|
    if state && state.depth >= 2
      hash["previous"] = collapse_document(hash["previous"]) if hash["previous"]
      hash["next"]     = collapse_document(hash["next"]) if hash["next"]
    end
  end
end
```

###
  
    #**name**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

```
# File 'lib/jekyll/drops/document_drop.rb', line 28

def name
  fallback_data["name"] || @obj.basename
end
```

###
  
    #**next**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

```
# File 'lib/jekyll/drops/document_drop.rb', line 44

def next
  @obj.next_doc.to_liquid
end
```

###
  
    #**previous**  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
```

```
# File 'lib/jekyll/drops/document_drop.rb', line 40

def previous
  @obj.previous_doc.to_liquid
end
```
