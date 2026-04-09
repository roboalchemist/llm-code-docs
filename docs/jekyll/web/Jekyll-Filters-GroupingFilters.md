# Module: Jekyll::Filters::GroupingFilters
  
    Included in:
    Jekyll::Filters
  
  

  
  
    Defined in:
    lib/jekyll/filters/grouping_filters.rb
  
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**group_by**(input, property)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Group an array of items by a property.

-
  
      #**group_by_exp**(input, variable, expression)  ⇒ Object 

Group an array of items by an expression.

## Instance Method Details

###
  
    #**group_by**(input, property)  ⇒ Object 
  

  

  

  
    

Group an array of items by a property

input - the inputted Enumerable property - the property

Returns an array of Hashes, each looking something like this:

```
{"name"  => "larry"
 "items" => [...] } # all the items where `property` == "larry"

```

```

14
15
16
17
18
19
20
21
```

```
# File 'lib/jekyll/filters/grouping_filters.rb', line 14

def group_by(input, property)
  if groupable?(input)
    groups = input.group_by { |item| item_property(item, property).to_s }
    grouped_array(groups)
  else
    input
  end
end
```

###
  
    #**group_by_exp**(input, variable, expression)  ⇒ Object 
  

  

  

  
    

Group an array of items by an expression

input - the object array variable - the variable to assign each item to in the expression expression -a Liquid comparison expression passed in as a string

Returns the filtered array of objects

```

30
31
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
```

```
# File 'lib/jekyll/filters/grouping_filters.rb', line 30

def group_by_exp(input, variable, expression)
  return input unless groupable?(input)

  parsed_expr = parse_expression(expression)
  @context.stack do
    groups = input.group_by do |item|
      @context[variable] = item
      parsed_expr.render(@context)
    end
    grouped_array(groups)
  end
end
```
