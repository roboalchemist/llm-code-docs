# Class: Conjur::Configuration
  
    Inherits:
    
      Object
      
        

          
- Object

- Conjur::Configuration

        show all
      

    Defined in:
    lib/conjur/configuration.rb
  
## Overview

Stores a configuration for the Conjur API client.  This class provides *global* and *thread local* storage
for common options used by the Conjur API.  Most importantly, it specifies the

- REST endpoints, derived from the #appliance_url and #account options

- The certificate used for secure connections to the Conjur appliance (#cert_file)

### Environment Variables

Option values used by Conjur can be given by environment variables, using a standard naming scheme. Specifically,
an environment variable named `CONJUR_ACCOUNT` will be used to provide a default value for the #account
option.

### Required Options

The #account and #appliance_url are always required.  Except in
special cases, the #cert_file is also required, but you may omit it if your Conjur root
certificate is in the OpenSSl default certificate store.

### Thread Local Configuration

While using a globally available configuration is convenient for most applications, sometimes you will need to
use different configurations in different threads.  This is supported by  returning a thread local version from configuration
if one has been set by with_configuration.

#### Examples

#####

Basic Configuration

```
Conjur.configure do |c|
  c.account = 'the-account'
  c.cert_file = find_conjur_cert_file
end

```

#####

Setting the appliance_url from an environment variable

```
ENV['CONJUR_APPLIANCE_URL'] = 'https://some-host.com/api'
Conjur::Configuration.new.appliance_url # => 'https://some-host.com/api'

```

#####

Using thread local configuration in a web application request handler

```
# Assume that we're in a request handler thread in a multithreaded web server.

requested_appliance_url = request.header 'X-Conjur-Appliance-Url'

with_configuration Conjur.config.clone(appliance_url: requested_appliance_url) do
  # `api` is an instance attribute.  Note that we can use an api that was created
  # before we modified the thread local configuration.

  # 404 if the user doesn't exist

  user = api.user request.header('X-Conjur-Login')
  raise HttpError, 404, "User #{user.login} does not exist" unless user.exists?
  # ... finish the request
end

```

See Also:
  
- configuration

- configure

- with_configuration

## Instance Attribute Summary collapse

-
  
      #**account**  ⇒ String 

The organizational account used by Conjur.

-
  
      #**appliance_url**  ⇒ String 

The url for your Conjur appliance.

-
  
      #**authn_local_socket**  ⇒ Object 

File path to the Unix socket used for local authentication.

-
  
      #**authn_url**  ⇒ String 

The url for the Conjur authentication service.

-
  
      #**cert_file**  ⇒ String? 

Path to the certificate file to use when making secure connections to your Conjur appliance.

-
  
      #**core_url**  ⇒ String 

The url for the core Conjur services.

-
  
      #**rest_client_options**  ⇒ Object 

Custom options for the underlying RestClient Requests.

-
  
      #**ssl_certificate**  ⇒ Object 

Contents of a certificate file.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**apply_cert_config!**(store = OpenSSL::SSL::SSLContext::DEFAULT_CERT_STORE)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Add the certificate configured by the #ssl_certificate and #cert_file options to the certificate store used by Conjur clients.

-
  
      #**clone**(override_options = {})  ⇒ Conjur::Configuration 

Return a copy of this Configuration instance, optionally updating the copy with options from the `override_options` hash.

-
  
      #**create_rest_client_options**(options)  ⇒ Object 

Create rest_client_options by merging the input with the rest_client_options present on the configuration object.

-
  
      #**initialize**(options = {})  ⇒ Configuration 

    constructor
  
  
  
  
  
  

  
    

Create a new Configuration, setting initial values from `options`.

## Constructor Details

###
  
    #**initialize**(options = {})  ⇒ Configuration 
  

  

  

  
    
  
    **Note:**
    

`options` must use symbols for keys.

Create a new Conjur::Configuration, setting initial values from
`options`.

#### Examples

```
Conjur.config = Conjur::Configuration.new account: 'companyname'
Conjur.config.account # => 'companyname'

```

Parameters:

-

        options

        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

hash of options to set on the new instance.

```

190
191
192
193
194
```

```
# File 'lib/conjur/configuration.rb', line 190

def initialize options = {}
  @explicit = options.dup
  @supplied = options.dup
  @computed = Hash.new
end

```

## Instance Attribute Details

###
  
    #**account**  ⇒ String 
  

  

  

  
    
  
    **Note:**
    

this option is **required**, and attempting to make any api calls prior to setting it (either
explicitly or with the `"CONJUR_ACCOUNT"` environment variable) will raise an exception.

The organizational account used by Conjur.

On Conjur appliances, this option will be set once when the appliance is first configured.  You can get the
value for the acccount option from your conjur administrator, or if you have installed
the Conjur command line tools by running
conjur authn whoami,
or examining your .conjurrc file.

Returns:

-

        (String)

```

348
```

```
# File 'lib/conjur/configuration.rb', line 348

add_option :account, required: true

```

###
  
    #**appliance_url**  ⇒ String 
  

  

  

  
    
  
    **Note:**
    

If you are using an appliance (if you're not sure, you probably are), this option is *required*.

The url for your Conjur appliance.

If your appliance's hostname is `'conjur.companyname.com'`, then your `appliance_url` will
be `'https://conjur.companyname.com/api'`.

Returns:

-

        (String)

        —
        

the appliance URL

```

325
```

```
# File 'lib/conjur/configuration.rb', line 325

add_option :appliance_url

```

###
  
    #**authn_local_socket**  ⇒ Object 
  

  

  

  
    

File path to the Unix socket used for local authentication.
This is only available when the API client is running on the Conjur server.

```

413
```

```
# File 'lib/conjur/configuration.rb', line 413

add_option :authn_local_socket, default: "/run/authn-local/.socket"

```

###
  
    #**authn_url**  ⇒ String 
  

  

  

  
    

The url for the Conjur authentication service.

By default, this will be built from the +appliance_url+. To use a custom authenticator,
set this option in code or set `CONJUR_AUTHN_URL`.

Returns:

-

        (String)

        —
        

the authentication service url

```

299
300
301
```

```
# File 'lib/conjur/configuration.rb', line 299

add_option :authn_url do
  global_service_url 0, service_name: 'authn'
end

```

###
  
    #**cert_file**  ⇒ String? 
  

  

  

  
    

Path to the certificate file to use when making secure connections to your Conjur appliance.

This should be the path to the root Conjur SSL certificate in PEM format. You will normally get the
certificate file using the conjur init command.
This option is not required if the certificate or its root is in the OpenSSL default cert store.
If your program throws an error indicating that SSL verification has failed, you probably need
to set or fix this option.

Returns:

-

        (String, nil)

        —
        

path to the certificate file, or nil if you aren't using one.

```

361
```

```
# File 'lib/conjur/configuration.rb', line 361

add_option :cert_file

```

###
  
    #**core_url**  ⇒ String 
  

  

  

  
    
  
    **Note:**
    

You should not generally set this value.  Instead, Conjur will derive it from the
# account and #appliance_url
properties.

The url for the core Conjur services.

Returns:

-

        (String)

        —
        

the base service url

```

312
313
314
```

```
# File 'lib/conjur/configuration.rb', line 312

add_option :core_url do
  global_service_url 0
end

```

###
  
    #**rest_client_options**  ⇒ Object 
  

  

  

  
    

Custom options for the underlying RestClient Requests. This defaults to:

```
{
  ssl_cert_store: OpenSSL::SSL::SSLContext::DEFAULT_CERT_STORE
}
``

The `ssl_cert_store` value aligns with the default certificate store used by
{#apply_cert_config!}.

NOTE: When setting the value of rest_client_options the defaults are not retained,
you must manually set them on the value you provide.

```

```

400
401
402
403
404
405
406
407
```

```
# File 'lib/conjur/configuration.rb', line 400

add_option :rest_client_options do
  {
    ssl_cert_store: OpenSSL::SSL::SSLContext::DEFAULT_CERT_STORE,
    headers: { 
      'x-cybr-telemetry': get_telemetry_header
    }
  }
end

```

###
  
    #**ssl_certificate**  ⇒ Object 
  

  

  

  
    

Contents of a certificate file.  This can be used instead of :cert_file in environments like Heroku where  you
can't use a certificate file.

This option overrides the value of #cert_file if both are given, and issues a warning.

See Also:
  
- #cert_file

```

371
```

```
# File 'lib/conjur/configuration.rb', line 371

add_option :ssl_certificate

```

## Instance Method Details

###
  
    #**apply_cert_config!**(store = OpenSSL::SSL::SSLContext::DEFAULT_CERT_STORE)  ⇒ Boolean 
  

  

  

  
    

Add the certificate configured by the #ssl_certificate and #cert_file options to the certificate
store used by Conjur clients.

NOTE: If you specify a non-default `store` value, you must manually set the
`ssl_cert_store` value on #rest_client_options to the same value.

Parameters:

-

        store

        (OpenSSL::X509::Store)
      
      
        *(defaults to: OpenSSL::SSL::SSLContext::DEFAULT_CERT_STORE)*
      
      
        —
        

the certificate store that the certificate will be installed in.

Returns:

-

        (Boolean)

        —
        

whether a certificate was added to the store.

```

430
431
432
433
434
435
436
437
438
439
440
```

```
# File 'lib/conjur/configuration.rb', line 430

def apply_cert_config! store=OpenSSL::SSL::SSLContext::DEFAULT_CERT_STORE
  if ssl_certificate
    CertUtils.add_chained_cert(store, ssl_certificate)
  elsif cert_file
    ensure_cert_readable!(cert_file)
    store.add_file cert_file
  else
    return false
  end
  true
end

```

###
  
    #**clone**(override_options = {})  ⇒ Conjur::Configuration 
  

  

  

  
    

Return a copy of this Conjur::Configuration instance, optionally
updating the copy with options from the `override_options` hash.

#### Examples

```
original = Conjur.configuration
original.account  # => 'conjur'
copy = original.clone account: 'some-other-account'
copy.account    # => 'some-other-account'
original.account # => 'conjur'

```

Parameters:

-

        override_options

        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

options to set on the new instance

Returns:

-

        (Conjur::Configuration)

        —
        

a copy of this configuration

```

273
274
275
```

```
# File 'lib/conjur/configuration.rb', line 273

def clone override_options = {}
  self.class.new self.explicit.dup.merge(override_options)
end

```

###
  
    #**create_rest_client_options**(options)  ⇒ Object 
  

  

  

  
    

Create rest_client_options by merging the input with the
rest_client_options present on the configuration object.

```

417
418
419
420
```

```
# File 'lib/conjur/configuration.rb', line 417

def create_rest_client_options options
  options ||= {}
  rest_client_options.merge(options) { |key, left, right| left.merge(right) }
end

```
