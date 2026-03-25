# Class: Conjur::BaseObject
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::BaseObject

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      BuildObject, LogSource, Routing
  
    Defined in:
    lib/conjur/base_object.rb
  
## Direct Known Subclasses

Group, Host, HostFactory, Layer, Policy, Resource, Role, User, Variable, Webservice

## Instance Attribute Summary collapse

-
  
      #**credentials**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute credentials.

-
  
      #**id**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute id.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**account**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**as_json**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**identifier**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**(id, credentials)  ⇒ BaseObject 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of BaseObject.

-
  
      #**inspect**  ⇒ Object 

-
  
      #**kind**  ⇒ Object 

-
  
      #**username**  ⇒ Object 

### Methods included from Routing

# parser_for, #url_for

### Methods included from BuildObject

# build_object

### Methods included from LogSource

# log

## Constructor Details

###
  
    #**initialize**(id, credentials)  ⇒ BaseObject 
  

  

  

  
    

Returns a new instance of BaseObject.

```

26
27
28
29
```

```
# File 'lib/conjur/base_object.rb', line 26

def initialize id, credentials
  @id = Id.new id
  @credentials = credentials
end
```

## Instance Attribute Details

###
  
    #**credentials**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute credentials.

```

24
25
26
```

```
# File 'lib/conjur/base_object.rb', line 24

def credentials
  @credentials
end
```

###
  
    #**id**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute id.

```

24
25
26
```

```
# File 'lib/conjur/base_object.rb', line 24

def id
  @id
end
```

## Instance Method Details

###
  
    #**account**  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

```
# File 'lib/conjur/base_object.rb', line 37

def account
  id.account
end
```

###
  
    #**as_json**(options = {})  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
35
```

```
# File 'lib/conjur/base_object.rb', line 31

def as_json options={}
  {
    id: id.to_s
  }
end
```

###
  
    #**identifier**  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

```
# File 'lib/conjur/base_object.rb', line 45

def identifier
  id.identifier
end
```

###
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
```

```
# File 'lib/conjur/base_object.rb', line 53

def inspect
  "<#{self.class.name} id='#{id.to_s}'>"
end
```

###
  
    #**kind**  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

```
# File 'lib/conjur/base_object.rb', line 41

def kind
  id.kind
end
```

###
  
    #**username**  ⇒ Object 
  

  

  

  
    
      

```

49
50
51
```

```
# File 'lib/conjur/base_object.rb', line 49

def username
  credentials[:username] or raise "No username found in credentials"
end
```
