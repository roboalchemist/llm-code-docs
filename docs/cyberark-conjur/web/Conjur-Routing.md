# Module: Conjur::Routing
  
    Included in:
    API, API, BaseObject
  
  

  
  
    Defined in:
    lib/conjur/routing.rb
  
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**parser_for**(method, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**url_for**(method, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**parser_for**(method, *args)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

```
# File 'lib/conjur/routing.rb', line 7

def parser_for method, *args
  router.send "parse_#{method}", *args
end
```

###
  
    #**url_for**(method, *args)  ⇒ Object 
  

  

  

  
    
      

```

3
4
5
```

```
# File 'lib/conjur/routing.rb', line 3

def url_for method, *args
  router.send method, *args
end
```
