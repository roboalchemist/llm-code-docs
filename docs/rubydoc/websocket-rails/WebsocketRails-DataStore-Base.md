# Class: WebsocketRails::DataStore::Base
  
  
  

  
  
    Inherits:
    
      ActiveSupport::HashWithIndifferentAccess
      
        

          
- Object
          
            
- ActiveSupport::HashWithIndifferentAccess
          
            
- WebsocketRails::DataStore::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/data_store.rb
  
  

  
## Direct Known Subclasses

  

Connection, Controller

  
    
## 
      Constant Summary
      collapse
    

    
      
        @@all_instances =
          
        
        

```
Hash.new { |h,k| h[k] = [] }
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**clear_all_instances**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**collect_all**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**destroy!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**instances**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/websocket_rails/data_store.rb', line 29

def initialize
  instances << self
end
```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**clear_all_instances**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/websocket_rails/data_store.rb', line 25

def self.clear_all_instances
  @@all_instances = Hash.new { |h,k| h[k] = [] }
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**collect_all**(key)  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
40
41
42
43
44
45
46
47
48
49
```

    
    
      

```
# File 'lib/websocket_rails/data_store.rb', line 37

def collect_all(key)
  collection = instances.each_with_object([]) do |instance, array|
    array << instance[key]
  end

  if block_given?
    collection.each do |item|
      yield(item)
    end
  else
    collection
  end
end
```

    
  

    
      
  
### 
  
    #**destroy!**  ⇒ Object 
  

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/websocket_rails/data_store.rb', line 51

def destroy!
  instances.delete_if {|store| store.object_id == self.object_id }
end
```

    
  

    
      
  
### 
  
    #**instances**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/websocket_rails/data_store.rb', line 33

def instances
  all_instances[self.class]
end
```