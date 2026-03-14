# Module: Jekyll::Utils::Internet
  
    Defined in:
    lib/jekyll/utils/internet.rb
  
  

  
    
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**connected?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**dns**(domain)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

###
  
    .**connected?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

23
24
25
```

```
# File 'lib/jekyll/utils/internet.rb', line 23

def connected?
  !dns("example.com").nil?
end
```

###
  
    .**dns**(domain)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/jekyll/utils/internet.rb', line 27

def dns(domain)
  require "resolv"
  Resolv::DNS.open do |resolver|
    resolver.getaddress(domain)
  end
rescue Resolv::ResolvError, Resolv::ResolvTimeout
  nil
end
```
