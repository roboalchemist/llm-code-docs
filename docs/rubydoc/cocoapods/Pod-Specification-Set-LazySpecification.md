# Class: Pod::Specification::Set::LazySpecification
  
  
  

  
  
    Inherits:
    
      Pod::Specification
      
        

          
- Object
          
            
- Pod::Specification
          
            
- Pod::Specification::Set::LazySpecification
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/resolver/lazy_specification.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
      
- 
  
    
      #**spec_source**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute spec_source.

  

    
      
- 
  
    
      #**version**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute version.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(name, version, spec_source)  ⇒ LazySpecification 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of LazySpecification.

  

      
        
- 
  
    
      #**specification**  ⇒ Object 
    

    
      (also: #__getobj__)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**subspec_by_name**(name = nil, raise_if_missing = true, include_non_library_specifications = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, version, spec_source)  ⇒ LazySpecification 
  

  

  

  
    

Returns a new instance of LazySpecification.

  

  

  
    
      

```

18
19
20
21
22
```

    
    
      

```
# File 'lib/cocoapods/resolver/lazy_specification.rb', line 18

def initialize(name, version, spec_source)
  @name = name
  @version = version
  @spec_source = spec_source
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute name.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/cocoapods/resolver/lazy_specification.rb', line 16

def name
  @name
end
```

    
  

    
      
      
      
  
### 
  
    #**spec_source**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute spec_source.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/cocoapods/resolver/lazy_specification.rb', line 16

def spec_source
  @spec_source
end
```

    
  

    
      
      
      
  
### 
  
    #**version**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute version.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/cocoapods/resolver/lazy_specification.rb', line 16

def version
  @version
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**specification**  ⇒ Object 
  

  
    Also known as:
    __getobj__
    
  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/cocoapods/resolver/lazy_specification.rb', line 36

def specification
  @specification ||= spec_source.specification(name, version.version)
end
```

    
  

    
      
  
### 
  
    #**subspec_by_name**(name = nil, raise_if_missing = true, include_non_library_specifications = false)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
27
28
29
30
31
32
33
34
```

    
    
      

```
# File 'lib/cocoapods/resolver/lazy_specification.rb', line 24

def subspec_by_name(name = nil, raise_if_missing = true, include_non_library_specifications = false)
  subspec =
    if !name || name == self.name
      self
    else
      specification.subspec_by_name(name, raise_if_missing, include_non_library_specifications)
    end
  return unless subspec

  SpecWithSource.new subspec, spec_source
end
```