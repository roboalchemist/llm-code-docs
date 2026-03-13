# Class: Jekyll::Drops::ExcerptDrop
  
    Inherits:
    
      DocumentDrop
      
        

          
- Object

- Liquid::Drop

- Drop

- DocumentDrop

- Jekyll::Drops::ExcerptDrop

        show all
      

    Defined in:
    lib/jekyll/drops/excerpt_drop.rb
  
## Constant Summary

### Constants inherited

     from DocumentDrop

DocumentDrop::NESTED_OBJECT_FIELD_BLACKLIST

### Constants inherited

     from Drop

Drop::NON_CONTENT_METHODS

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**date**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**excerpt**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**layout**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

### Methods inherited from DocumentDrop

# <=>, #collapse_document, #collection, #hash_for_json, #next, #previous

### Methods inherited from Drop

# [], #[]=, #content_methods, data_delegator, data_delegators, delegate_method, delegate_method_as, delegate_methods, #each, #each_key, #fetch, getter_method_names, #hash_for_json, #initialize, #inspect, #key?, #keys, #merge, #merge!, mutable, mutable?, private_delegate_methods, #to_h, #to_json

## Constructor Details

This class inherits a constructor from Jekyll::Drops::Drop
  
## Instance Method Details

###
  
    #**date**  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

```
# File 'lib/jekyll/drops/excerpt_drop.rb', line 10

def date
  @obj.doc.date
end

```

###
  
    #**excerpt**  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
```

```
# File 'lib/jekyll/drops/excerpt_drop.rb', line 14

def excerpt
  nil
end

```

###
  
    #**layout**  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
```

```
# File 'lib/jekyll/drops/excerpt_drop.rb', line 6

def layout
  @obj.doc.data["layout"]
end

```

###
  
    #**name**  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
```

```
# File 'lib/jekyll/drops/excerpt_drop.rb', line 18

def name
  @obj.doc.data["name"] || @obj.doc.basename
end

```
