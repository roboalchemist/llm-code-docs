# Module: Conjur::CertUtils
  
    Defined in:
    lib/conjur/cert_utils.rb
  
  

  
    
##

      Constant Summary
      collapse
    

    
      
        CERT_RE =
          
        
        

```
/-----BEGIN CERTIFICATE-----\n.*?\n-----END CERTIFICATE-----\n/m
```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**add_chained_cert**(store, chained_cert)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add a certificate to a given store.

-
  
      .**parse_certs**(certs)  ⇒ Array<OpenSSL::X509::Certificate> 

Parse X509 DER-encoded certificates from a string.

## Class Method Details

###
  
    .**add_chained_cert**(store, chained_cert)  ⇒ Object 
  

  

  

  
    

Add a certificate to a given store. If the certificate has more than
one certificate in its chain, it will be parsed and added to the store
one by one. This is done because `OpenSSL::X509::Store.new.add_cert`
adds only the intermediate certificate to the store.

```

52
53
54
55
56
57
58
59
60
```

```
# File 'lib/conjur/cert_utils.rb', line 52

def add_chained_cert store, chained_cert
  parse_certs(chained_cert).each do |cert|
    begin
      store.add_cert cert
    rescue OpenSSL::X509::StoreError => ex
      raise unless ex.message == 'cert already in hash table'
    end
  end
end
```

###
  
    .**parse_certs**(certs)  ⇒ Array<OpenSSL::X509::Certificate> 
  

  

  

  
    

Parse X509 DER-encoded certificates from a string

Parameters:

-

certificate(s) to parse in DER form

Returns:

-

certificates contained in the string

```

32
33
34
35
36
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
```

```
# File 'lib/conjur/cert_utils.rb', line 32

def parse_certs certs
  # fix any mangled namespace
  certs = certs.gsub /\s+/, "\n"
  certs.gsub! "-----BEGIN\nCERTIFICATE-----", '-----BEGIN CERTIFICATE-----'
  certs.gsub! "-----END\nCERTIFICATE-----", '-----END CERTIFICATE-----'
  certs += "\n" unless certs[-1] == "\n"

  certs.scan(CERT_RE).map do |cert|
    begin
      OpenSSL::X509::Certificate.new cert
    rescue OpenSSL::X509::CertificateError => exn
      raise exn, "Invalid certificate:\n#{cert} (#{exn.message})"
    end
  end
end
```
