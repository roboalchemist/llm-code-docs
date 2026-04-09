# Class: Nokogiri::XML::Node::SaveOptions
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::Node::SaveOptions
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/node/save_options.rb
  
  

## Overview

  
    

Save options for serializing nodes. See the method group entitled Node@Serialization+and+Generating+Output for usage.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        FORMAT =
          
  
    

Format serialized xml

  

  

        
        

```
1

```

      
        NO_DECLARATION =
          
  
    

Do not include declarations

  

  

        
        

```
2

```

      
        NO_EMPTY_TAGS =
          
  
    

Do not include empty tags

  

  

        
        

```
4

```

      
        NO_XHTML =
          
  
    

Do not save XHTML

  

  

        
        

```
8

```

      
        AS_XHTML =
          
  
    

Save as XHTML

  

  

        
        

```
16

```

      
        AS_XML =
          
  
    

Save as XML

  

  

        
        

```
32

```

      
        AS_HTML =
          
  
    

Save as HTML

  

  

        
        

```
64

```

      
        AS_BUILDER =
          
  
    

Save builder created document

  

  

        
        

```
128

```

      
        DEFAULT_XML =
          
  
    

the default for XML documents

  

  

        
        

```
FORMAT | AS_XML

```

      
        DEFAULT_HTML =
          
  
    

the default for HTML document

  

  

        
        

```
FORMAT | NO_DECLARATION | NO_EMPTY_TAGS | AS_HTML

```

      
        DEFAULT_XHTML =
          
  
    

the default for XHTML document

  

  

        
        

```
FORMAT | NO_DECLARATION | AS_XHTML

```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
      (also: #to_i)
    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Integer representation of the SaveOptions.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(options = 0)  ⇒ SaveOptions 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Create a new SaveOptions object with `options`.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(options = 0)  ⇒ SaveOptions 
  

  

  

  
    

Create a new SaveOptions object with `options`

  

  

  
    
      

```

47
48
49
```

    
    
      

```
# File 'lib/nokogiri/xml/node/save_options.rb', line 47

def initialize(options = 0)
  @options = options
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  
    Also known as:
    to_i
    
  

  

  
    

Integer representation of the SaveOptions

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/nokogiri/xml/node/save_options.rb', line 44

def options
  @options
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

66
67
68
69
70
71
72
```

    
    
      

```
# File 'lib/nokogiri/xml/node/save_options.rb', line 66

def inspect
  options = []
  self.class.constants.each do |k|
    options << k.downcase if send(:"#{k.downcase}?")
  end
  super.sub(/>$/, " " + options.join(", ") + ">")
end

```