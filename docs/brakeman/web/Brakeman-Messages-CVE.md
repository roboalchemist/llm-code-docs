# Class: Brakeman::Messages::CVE
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Brakeman::Messages::CVE
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/brakeman/messages.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(cve)  ⇒ CVE 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of CVE.

  

      
        
- 
  
    
      #**to_html**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(cve)  ⇒ CVE 
  

  

  

  
    

Returns a new instance of CVE.

  

  

  
    
      

```

118
119
120
```

    
    
      

```
# File 'lib/brakeman/messages.rb', line 118

def initialize cve
  @cve = cve
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**to_html**  ⇒ Object 
  

  

  

  
    
      

```

126
127
128
```

    
    
      

```
# File 'lib/brakeman/messages.rb', line 126

def to_html
  "(<a href=\"https://cve.mitre.org/cgi-bin/cvename.cgi?name=#{@cve}\" target=\"_blank\" rel=\"noreferrer\">#{@cve}</a>)"
end
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

122
123
124
```

    
    
      

```
# File 'lib/brakeman/messages.rb', line 122

def to_s
  "(#{@cve})"
end
```