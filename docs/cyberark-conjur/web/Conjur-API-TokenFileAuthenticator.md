# Class: Conjur::API::TokenFileAuthenticator
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::API::TokenFileAuthenticator

        show all
      

    Defined in:
    lib/conjur/base.rb
  
## Overview

Obtains fresh tokens by reading them from a file. Some other process is assumed
to be acquiring tokens and storing them to the file on a regular basis.

This authenticator assumes that the token was created immediately before
it was written to the file.

## Instance Attribute Summary collapse

-
  
      #**last_mtime**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute last_mtime.

-
  
      #**token_file**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute token_file.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(token_file)  ⇒ TokenFileAuthenticator 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of TokenFileAuthenticator.

-
  
      #**mtime**  ⇒ Object 

-
  
      #**needs_token_refresh?**  ⇒ Boolean 

-
  
      #**refresh_token**  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(token_file)  ⇒ TokenFileAuthenticator 
  

  

  

  
    

Returns a new instance of TokenFileAuthenticator.

```

270
271
272
```

```
# File 'lib/conjur/base.rb', line 270

def initialize token_file
  @token_file = token_file
end
```

## Instance Attribute Details

###
  
    #**last_mtime**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute last_mtime.

```

274
275
276
```

```
# File 'lib/conjur/base.rb', line 274

def last_mtime
  @last_mtime
end
```

###
  
    #**token_file**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute token_file.

```

268
269
270
```

```
# File 'lib/conjur/base.rb', line 268

def token_file
  @token_file
end
```

## Instance Method Details

###
  
    #**mtime**  ⇒ Object 
  

  

  

  
    
      

```

276
277
278
```

```
# File 'lib/conjur/base.rb', line 276

def mtime
  File.mtime token_file
end
```

###
  
    #**needs_token_refresh?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

290
291
292
```

```
# File 'lib/conjur/base.rb', line 290

def needs_token_refresh?
  mtime != last_mtime
end
```

###
  
    #**refresh_token**  ⇒ Object 
  

  

  

  
    
      

```

280
281
282
283
284
285
286
287
288
```

```
# File 'lib/conjur/base.rb', line 280

def refresh_token
  # There's a race condition here in which the file could be updated
  # after we read the mtime but before we read the file contents. So to be
  # conservative, use the oldest possible mtime.
  mtime = self.mtime
  File.open token_file, 'r' do |f|
    JSON.load(f.read).tap { @last_mtime = mtime }
  end
end
```
