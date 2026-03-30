# Module: Conjur::CIDR
  
    Defined in:
    lib/conjur/cidr.rb
  
## Overview

Utility methods for CIDR network addresses

## Defined Under Namespace

      **Classes:** InvalidCIDR
    
  
## Instance Attribute Summary collapse

-
  
      #**mask_addr**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute mask_addr.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**validate**(addr)  ⇒ IPAddr 
    

    
  
  
  
  
  
  
  
  

  
    

Parse addr into an IPAddr if it's not one already, then extend it with CIDR module.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**prefixlen**  ⇒ Fixnum 
    

    
  
  
  
  
  
  
  
  

  
    

The length of the network mask prefix.

-
  
      #**to_s**  ⇒ String 

The address as an "address/mask length" string.

## Instance Attribute Details

###
  
    #**mask_addr**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute mask_addr.

```

43
44
45
```

```
# File 'lib/conjur/cidr.rb', line 43

def mask_addr
  @mask_addr
end
```

## Class Method Details

###
  
    .**validate**(addr)  ⇒ IPAddr 
  

  

  

  
    

Parse addr into an IPAddr if it's not one already, then extend it with CIDR
module. This will force validation and will raise ArgumentError if invalid.

Returns:

-

        (IPAddr)

        —
        

the address (extended with CIDR module)

```

30
31
32
33
```

```
# File 'lib/conjur/cidr.rb', line 30

def self.validate addr
  addr = IPAddr.new addr unless addr.kind_of? IPAddr
  addr.extend self
end
```

## Instance Method Details

###
  
    #**prefixlen**  ⇒ Fixnum 
  

  

  

  
    

Returns the length of the network mask prefix.

Returns:

-

        (Fixnum)

        —
        

the length of the network mask prefix

```

53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
```

```
# File 'lib/conjur/cidr.rb', line 53

def prefixlen
  unless @prefixlen
    return @prefixlen = 0 if (mask = mask_addr) == 0

    @prefixlen = ipv4? ? 32 : 128

    while (mask & 1) == 0
      mask >>= 1
      @prefixlen -= 1
    end

    if mask != ((1 << @prefixlen) - 1)
      fail InvalidCIDR, "#{inspect} is not a valid CIDR network address"
    end
  end
  return @prefixlen
end
```

###
  
    #**to_s**  ⇒ String 
  

  

  

  
    

Returns the address as an "address/mask length" string.

#### Examples

```
IPAddr.new("192.0.2.0/255.255.255.0").extend(CIDR).to_s == "192.0.2.0/24"
```

Returns:

-

        (String)

        —
        

the address as an "address/mask length" string

```

48
49
50
```

```
# File 'lib/conjur/cidr.rb', line 48

def to_s
  [super, prefixlen].join '/'
end
```
