# Module: Conjur::HasAttributes
  
    Defined in:
    lib/conjur/has_attributes.rb
  
## Overview

Many Conjur assets have key-value attributes.  Although these should generally be accessed via
methods on specific asset classes (for example, Resource#owner), the are available as
a `Hash` on all types supporting attributes.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**annotations**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**as_json**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**attributes**  ⇒ Hash 
    

    
  
  
  
  
  
  
  
  

  
    

Get the attributes for this asset.

-
  
      #**invalidate**(&block)  

Call a block that will perform actions that might change the asset's attributes.

-
  
      #**to_s**  ⇒ Object 

## Instance Method Details

###
  
    #**annotations**  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
```

```
# File 'lib/conjur/has_attributes.rb', line 74

def annotations
  Hash[(attributes['annotations']||{}).collect {|e| [e['name'],e['value']]}]
end

```

###
  
    #**as_json**(options = {})  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
37
38
39
40
```

```
# File 'lib/conjur/has_attributes.rb', line 34

def as_json options={}
  result = super(options)
  if @attributes
    result.merge!(@attributes.as_json(options))
  end
  result
end

```

###
  
    #**attributes**  ⇒ Hash 
  

  

  

  
    

Get the attributes for this asset. This is an immutable Hash, unless the attributes
are changed via policy update.

Returns:

-

        (Hash)

        —
        

the asset's attributes.

```

56
57
58
59
```

```
# File 'lib/conjur/has_attributes.rb', line 56

def attributes
  return @attributes if @attributes
  fetch
end

```

###
  
    #**invalidate**(&block)  
  

  

  

  
    
  
    **Note:**
    

this is mainly used internally, but included in the public api for completeness.

This method returns an undefined value.

Call a block that will perform actions that might change the asset's attributes.
No matter what happens in the block, this method ensures that the cached attributes
will be invalidated.

```

68
69
70
71
72
```

```
# File 'lib/conjur/has_attributes.rb', line 68

def invalidate(&block)
  yield
ensure
  @attributes = nil
end

```

###
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

42
43
44
```

```
# File 'lib/conjur/has_attributes.rb', line 42

def to_s
  to_json.to_s
end

```
