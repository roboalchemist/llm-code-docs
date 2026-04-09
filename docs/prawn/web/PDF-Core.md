# Module: PDF::Core
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/security.rb
  
  

## Overview

  
    

rubocop: disable Style/Documentation

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Reference, Stream
    
  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      .**encrypted_pdf_object**(obj, key, id, gen, in_content_stream = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Like pdf_object, but returns an encrypted result if required.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**encrypted_pdf_object**(obj, key, id, gen, in_content_stream = false)  ⇒ Object 
  

  

  

  
    

Like pdf_object, but returns an encrypted result if required. For direct objects, requires the object identifier and generation number from the indirect object referencing obj.

  

  

  
    
      

```

217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
```

    
    
      

```
# File 'lib/prawn/security.rb', line 217

def encrypted_pdf_object(obj, key, id, gen, in_content_stream = false)
  case obj
  when Array
    array_content = obj.map { |e|
      encrypted_pdf_object(e, key, id, gen, in_content_stream)
    }.join(' ')
    "[#{array_content}]"
  when LiteralString
    obj =
      ByteString.new(
        Prawn::Document::Security.encrypt_string(obj, key, id, gen),
      ).gsub(/[\\\r()]/, STRING_ESCAPE_MAP)
    "(#{obj})"
  when Time
    obj = "#{obj.strftime('D:%Y%m%d%H%M%S%z').chop.chop}'00'"
    obj =
      ByteString.new(
        Prawn::Document::Security.encrypt_string(obj, key, id, gen),
      ).gsub(/[\\\r()]/, STRING_ESCAPE_MAP)
    "(#{obj})"
  when String
    pdf_object(
      ByteString.new(
        Prawn::Document::Security.encrypt_string(obj, key, id, gen),
      ),
      in_content_stream,
    )
  when ::Hash
    hash_content = obj.map { |k, v|
      unless k.is_a?(String) || k.is_a?(Symbol)
        raise PDF::Core::Errors::FailedObjectConversion,
          'A PDF Dictionary must be keyed by names'
      end
      "#{pdf_object(k.to_sym, in_content_stream)} #{encrypted_pdf_object(v, key, id, gen, in_content_stream)}\n"
    }.join('')
    "<< #{hash_content}>>"
  when NameTree::Value
    "#{pdf_object(obj.name)} #{encrypted_pdf_object(obj.value, key, id, gen, in_content_stream)}"
  when PDF::Core::OutlineRoot, PDF::Core::OutlineItem
    encrypted_pdf_object(obj.to_hash, key, id, gen, in_content_stream)
  else # delegate back to pdf_object
    pdf_object(obj, in_content_stream)
  end
end

```