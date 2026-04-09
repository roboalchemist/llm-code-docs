# Module: Jekyll::Filters::DateFilters
  
    Included in:
    Jekyll::Filters
  
  

  
  
    Defined in:
    lib/jekyll/filters/date_filters.rb
  
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**date_to_long_string**(date, type = nil, style = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Format a date in long format e.g.

-
  
      #**date_to_rfc822**(date)  ⇒ Object 

Format a date according to RFC-822.

-
  
      #**date_to_string**(date, type = nil, style = nil)  ⇒ Object 

Format a date in short format e.g.

-
  
      #**date_to_xmlschema**(date)  ⇒ Object 

Format a date for use in XML.

## Instance Method Details

###
  
    #**date_to_long_string**(date, type = nil, style = nil)  ⇒ Object 
  

  

  

  
    

Format a date in long format e.g. “27 January 2011”. Ordinal format is also supported, in both the UK (e.g. “27th January 2011”) and US (“e.g. January 27th, 2011”) formats. UK format is the default.

date - the Time to format. type - if “ordinal” the returned String will be in ordinal format style - if “US” the returned String will be in US format.

```
Otherwise it will be in UK format.

```

Returns the formatted String.

```

32
33
34
```

```
# File 'lib/jekyll/filters/date_filters.rb', line 32

def date_to_long_string(date, type = nil, style = nil)
  stringify_date(date, "%B", type, style)
end

```

###
  
    #**date_to_rfc822**(date)  ⇒ Object 
  

  

  

  
    

Format a date according to RFC-822

date - The Time to format.

Examples

```
date_to_rfc822(Time.now)
# => "Sun, 24 Apr 2011 12:34:46 +0000"

```

Returns the formatted String.

```

62
63
64
65
66
```

```
# File 'lib/jekyll/filters/date_filters.rb', line 62

def date_to_rfc822(date)
  return date if date.to_s.empty?

  time(date).rfc822
end

```

###
  
    #**date_to_string**(date, type = nil, style = nil)  ⇒ Object 
  

  

  

  
    

Format a date in short format e.g. “27 Jan 2011”. Ordinal format is also supported, in both the UK (e.g. “27th Jan 2011”) and US (“e.g. Jan 27th, 2011”) formats. UK format is the default.

date - the Time to format. type - if “ordinal” the returned String will be in ordinal format style - if “US” the returned String will be in US format.

```
Otherwise it will be in UK format.

```

Returns the formatting String.

```

17
18
19
```

```
# File 'lib/jekyll/filters/date_filters.rb', line 17

def date_to_string(date, type = nil, style = nil)
  stringify_date(date, "%b", type, style)
end

```

###
  
    #**date_to_xmlschema**(date)  ⇒ Object 
  

  

  

  
    

Format a date for use in XML.

date - The Time to format.

Examples

```
date_to_xmlschema(Time.now)
# => "2011-04-24T20:34:46+08:00"

```

Returns the formatted String.

```

46
47
48
49
50
```

```
# File 'lib/jekyll/filters/date_filters.rb', line 46

def date_to_xmlschema(date)
  return date if date.to_s.empty?

  time(date).xmlschema
end

```
