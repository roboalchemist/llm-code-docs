# Class: Arcfour
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Arcfour
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/security/arcfour.rb
  
  

## Overview

  
    

Implementation of the “ARCFOUR” algorithm (“alleged RC4 (tm)”). Implemented as described at: www.mozilla.org/projects/security/pki/nss/draft-kaukonen-cipher-arcfour-03.txt

“RC4” is a trademark of RSA Data Security, Inc.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**encrypt**(string)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Encrypt string.

  

      
        
- 
  
    
      #**initialize**(key)  ⇒ Arcfour 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Arcfour.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(key)  ⇒ Arcfour 
  

  

  

  
    

Returns a new instance of Arcfour.

  

  

  
    
      

```

11
12
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
23
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
35
```

    
    
      

```
# File 'lib/prawn/security/arcfour.rb', line 11

def initialize(key)
  # Convert string key to Array of integers
  key = key.unpack('c*') if key.is_a?(String)

  # 1. Allocate an 256 element array of 8 bit bytes to be used as an S-box
  # 2. Initialize the S-box.  Fill each entry first with it's index
  @sbox = (0..255).to_a

  # 3. Fill another array of the same size (256) with the key, repeating
  #    bytes as necessary.
  s2 = []
  while s2.length < 256
    s2 += key
  end
  s2 = s2[0, 256]

  # 4. Set j to zero and initialize the S-box
  j = 0
  (0..255).each do |i|
    j = (j + @sbox[i] + s2[i]) % 256
    @sbox[i], @sbox[j] = @sbox[j], @sbox[i]
  end

  @i = @j = 0
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**encrypt**(string)  ⇒ String 
  

  

  

  
    

Encrypt string.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/prawn/security/arcfour.rb', line 41

def encrypt(string)
  string.unpack('c*').map { |byte| byte ^ key_byte }.pack('c*')
end

```