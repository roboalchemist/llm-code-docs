# Class: Pod::Generator::DummySource
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Pod::Generator::DummySource
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/dummy_source.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**class_name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute class_name.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The string contents of the dummy source file.

  

      
        
- 
  
    
      #**initialize**(class_name_identifier)  ⇒ DummySource 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of DummySource.

  

      
        
- 
  
    
      #**save_as**(pathname)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(class_name_identifier)  ⇒ DummySource 
  

  

  

  
    

Returns a new instance of DummySource.

  

  

  
    
      

```

6
7
8
9
```

    
    
      

```
# File 'lib/cocoapods/generator/dummy_source.rb', line 6

def initialize(class_name_identifier)
  validated_class_name_identifier = class_name_identifier.gsub(/[^0-9a-z_]/i, '_')
  @class_name = "PodsDummy_#{validated_class_name_identifier}"
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**class_name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute class_name.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/cocoapods/generator/dummy_source.rb', line 4

def class_name
  @class_name
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    

Returns the string contents of the dummy source file.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

the string contents of the dummy source file.

      
    
  

  
    
      

```

13
14
15
16
17
18
19
20
21
22
```

    
    
      

```
# File 'lib/cocoapods/generator/dummy_source.rb', line 13

def generate
  result = "    #import <Foundation/Foundation.h>\n    @interface \#{class_name} : NSObject\n    @end\n    @implementation \#{class_name}\n    @end\n  source\n  result\nend\n".strip_heredoc

```

    
  

    
      
  
### 
  
    #**save_as**(pathname)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
27
28
```

    
    
      

```
# File 'lib/cocoapods/generator/dummy_source.rb', line 24

def save_as(pathname)
  pathname.open('w') do |source|
    source.write(generate)
  end
end

```