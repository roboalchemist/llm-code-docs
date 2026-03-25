# Module: Prawn::Document::Security
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Prawn::Document
  
  

  
  
    Defined in:
    lib/prawn/security.rb
  
  

## Overview

  
    

Implements PDF encryption (password protection and permissions) as specified in the PDF Reference, version 1.3, section 3.5 “Encryption”.

  

  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      .**encrypt_string**(str, key, id, gen)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Encrypts the given string under the given key, also requiring the object ID and generation number of the reference.

  

      
        
- 
  
    
      #**encrypt_document**(options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Encrypts the document, to protect confidential data or control modifications to the document.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**encrypt_string**(str, key, id, gen)  ⇒ String 
  

  

  

  
    

Encrypts the given string under the given key, also requiring the object ID and generation number of the reference.

See Algorithm 3.1.

  

  

Parameters:

  
    
- 
      
        str
      
      
        (String)
      
      
      
    
  
    
- 
      
        key
      
      
        (String)
      
      
      
    
  
    
- 
      
        id
      
      
        (Integer)
      
      
      
    
  
    
- 
      
        gen
      
      
        (Integer)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

106
107
108
109
110
111
112
113
114
115
```

    
    
      

```
# File 'lib/prawn/security.rb', line 106

def self.encrypt_string(str, key, id, gen)
  # Convert ID and Gen number into little-endian truncated byte strings
  id = [id].pack('V')[0, 3]
  gen = [gen].pack('V')[0, 2]
  extended_key = "#{key}#{id}#{gen}"

  # Compute the RC4 key from the extended key and perform the encryption
  rc4_key = Digest::MD5.digest(extended_key)[0, 10]
  Arcfour.new(rc4_key).encrypt(str)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**encrypt_document**(options = {})  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Encrypts the document, to protect confidential data or control modifications to the document. The encryption algorithm used is detailed in the PDF Reference 1.3, section 3.5 “Encryption”, and it is implemented by all major PDF readers.

#### Examples

Deny printing to everyone, but allow anyone to open without a password:

“‘ruby encrypt_document permissions: { print_document: false },

```
owner_password: :random

```

“‘

Set a user and owner password on the document, with full permissions for both the user and the owner:

“‘ruby encrypt_document user_password: ’foo’, owner_password: ‘bar’ “‘

Set no passwords, grant all permissions (This is useful because the default in some readers, if no permissions are specified, is “deny”):

“‘ruby encrypt_document “`

#### Caveats

- 

The encryption used is weak; the key is password-derived and is limited to 40 bits, due to US export controls in effect at the time the PDF standard was written.

- 

There is nothing technologically requiring PDF readers to respect the permissions embedded in a document. Many PDF readers do not.

- 

In short, you have **no security at all** against a moderately motivated person. Don’t use this for anything super-serious. This is not a limitation of Prawn, but is rather a built-in limitation of the PDF format.

  

  

Parameters:

  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    

Options Hash (options):
    

      
        
- 
          :user_password
          (String)
          
            
          
          
            — 

Password required to open the document. If this is omitted or empty, no password will be required. The document will still be encrypted, but anyone can read it.

          
        
      
        
- 
          :owner_password
          (String, :random)
          
            
          
          
            — 

Password required to make modifications to the document or change or override its permissions. If this is set to `:random`, a random password will be used; this can be useful if you never want users to be able to override the document permissions.

          
        
      
        
- 
          :permissions
          (Hash{Symbol => Boolean})
          
            
          
          
            — 

A hash mapping permission symbols (see below) to `true` or `false`. `true` means “permitted”, and `false` means “not permitted”. All permissions default to `true`.

The following permissions can be specified:

  - 

`:print_document` – Print document.

  - 

`:modify_contents` – Modify contents of document (other than text annotations and interactive form fields).

  - 

`:copy_contents` – Copy text and graphics from document.

  - 

`:modify_annotations` – Add or modify text annotations and interactive form fields.

          
        
      
    

  

  
    
      

```

78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
```

    
    
      

```
# File 'lib/prawn/security.rb', line 78

def encrypt_document(options = {})
  Prawn.verify_options(i[user_password owner_password permissions], options)
  @user_password = options.delete(:user_password) || ''

  @owner_password = options.delete(:owner_password) || @user_password
  if @owner_password == :random
    # Generate a completely ridiculous password
    @owner_password = (1..32).map { rand(256) }.pack('c*')
  end

  self.permissions = options.delete(:permissions) || {}

  # Shove the necessary entries in the trailer and enable encryption.
  state.trailer[:Encrypt] = encryption_dictionary
  state.encrypt = true
  state.encryption_key = user_encryption_key
end

```