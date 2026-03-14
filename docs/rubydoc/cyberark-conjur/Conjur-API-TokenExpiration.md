# Module: Conjur::API::TokenExpiration
  
    Included in:
    APIKeyAuthenticator, LocalAuthenticator
  
  

  
  
    Defined in:
    lib/conjur/base.rb
  
  

  
    
##

      Constant Summary
      collapse
    

    
      
        TOKEN_STALE =
          
  
    

The four minutes is to work around a bug in Conjur < 4.7 causing a 404 on
long-running operations (when the token is used right around the 5 minute mark).

```
4.minutes

```

## Instance Attribute Summary collapse

-
  
      #**token_born**  ⇒ Object 

Returns the value of attribute token_born.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**gettime**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**needs_token_refresh?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**token_age**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**update_token_born**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Attribute Details

###
  
    #**token_born**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute token_born.

```

184
185
186
```

```
# File 'lib/conjur/base.rb', line 184

def token_born
  @token_born
end

```

## Instance Method Details

###
  
    #**gettime**  ⇒ Object 
  

  

  

  
    
      

```

198
199
200
201
202
203
```

```
# File 'lib/conjur/base.rb', line 198

def gettime
  Process.clock_gettime Process::CLOCK_MONOTONIC
rescue
  # fall back to normal clock if there's no CLOCK_MONOTONIC
  Time.now.to_f
end

```

###
  
    #**needs_token_refresh?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

186
187
188
```

```
# File 'lib/conjur/base.rb', line 186

def needs_token_refresh?
  token_age > TOKEN_STALE
end

```

###
  
    #**token_age**  ⇒ Object 
  

  

  

  
    
      

```

194
195
196
```

```
# File 'lib/conjur/base.rb', line 194

def token_age
  gettime - token_born
end

```

###
  
    #**update_token_born**  ⇒ Object 
  

  

  

  
    
      

```

190
191
192
```

```
# File 'lib/conjur/base.rb', line 190

def update_token_born
  self.token_born = gettime
end

```
