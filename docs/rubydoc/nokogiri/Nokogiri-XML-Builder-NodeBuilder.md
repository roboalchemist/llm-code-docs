# Class: Nokogiri::XML::Builder::NodeBuilder
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::Builder::NodeBuilder
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/builder.rb
  
  

## Overview

  
    

:nodoc:

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**[]**(k)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**[]=**(k, v)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(node, doc_builder)  ⇒ NodeBuilder 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of NodeBuilder.

  

      
        
- 
  
    
      #**method_missing**(method, *args, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(node, doc_builder)  ⇒ NodeBuilder 
  

  

  

  
    

Returns a new instance of NodeBuilder.

  

  

  
    
      

```

443
444
445
446
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 443

def initialize(node, doc_builder)
  @node = node
  @doc_builder = doc_builder
end
```

    
  

  

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
### 
  
    #**method_missing**(method, *args, &block)  ⇒ Object 
  

  

  

  
    
      

```

456
457
458
459
460
461
462
463
464
465
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
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 456

def method_missing(method, *args, &block)
  opts = args.last.is_a?(Hash) ? args.pop : {}
  case method.to_s
  when /^(.*)!$/
    @node["id"] = Regexp.last_match(1)
    @node.content = args.first if args.first
  when /^(.*)=/
    @node[Regexp.last_match(1)] = args.first
  else
    @node["class"] =
      ((@node["class"] || "").split(/\s/) + [method.to_s]).join(" ")
    @node.content = args.first if args.first
  end

  # Assign any extra options
  opts.each do |k, v|
    @node[k.to_s] = ((@node[k.to_s] || "").split(/\s/) + [v]).join(" ")
  end

  if block
    old_parent = @doc_builder.parent
    @doc_builder.parent = @node

    arity = @doc_builder.arity || block.arity
    value = if arity <= 0
      @doc_builder.instance_eval(&block)
    else
      yield(@doc_builder)
    end

    @doc_builder.parent = old_parent
    return value
  end
  self
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]**(k)  ⇒ Object 
  

  

  

  
    
      

```

452
453
454
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 452

def [](k)
  @node[k]
end
```

    
  

    
      
  
### 
  
    #**[]=**(k, v)  ⇒ Object 
  

  

  

  
    
      

```

448
449
450
```

    
    
      

```
# File 'lib/nokogiri/xml/builder.rb', line 448

def []=(k, v)
  @node[k] = v
end
```