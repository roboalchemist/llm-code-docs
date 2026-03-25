# Module: Fabrication::Syntax::Make
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/fabrication/syntax/make.rb
  
  

## Overview

  
    

Extends Fabrication to provide make/make! class methods, which are shortcuts for Fabricate.build/Fabricate.

Usage:

require ‘fabrication/syntax/make’

User.make(:name => ‘Johnny’)

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**make**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**make!**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**make**(*args)  ⇒ Object 
  

  

  

  
    
      

```

14
15
16
17
18
19
```

    
    
      

```
# File 'lib/fabrication/syntax/make.rb', line 14

def make(*args, &)
  overrides = Fabrication::Support.extract_options!(args)
  klass = Fabrication::Support.underscore(name).to_sym
  fabricator_name = args.first.is_a?(Symbol) ? "#{klass}_#{args.first}" : klass
  Fabricate.build(fabricator_name, overrides, &)
end
```

    
  

    
      
  
### 
  
    #**make!**(*args)  ⇒ Object 
  

  

  

  
    
      

```

21
22
23
24
25
26
```

    
    
      

```
# File 'lib/fabrication/syntax/make.rb', line 21

def make!(*args, &)
  overrides = Fabrication::Support.extract_options!(args)
  klass = Fabrication::Support.underscore(name).to_sym
  fabricator_name = args.first.is_a?(Symbol) ? "#{klass}_#{args.first}" : klass
  Fabricate(fabricator_name, overrides, &)
end
```