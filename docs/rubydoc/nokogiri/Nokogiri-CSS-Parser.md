# Class: Nokogiri::CSS::Parser
  
  
  

  
  
    Inherits:
    
      Racc::Parser
      
        

          
- Object
          
            
- Racc::Parser
          
            
- Nokogiri::CSS::Parser
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/css/parser.rb,

  lib/nokogiri/css/parser.rb,
 lib/nokogiri/css/parser_extras.rb

  
  

## Overview

  
    

:nodoc:

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        Racc_arg =
          
        
        

```
[
racc_action_table,
racc_action_check,
racc_action_default,
racc_action_pointer,
racc_goto_table,
racc_goto_check,
racc_goto_default,
racc_goto_pointer,
racc_nt_base,
racc_reduce_table,
racc_token_table,
racc_shift_n,
racc_reduce_n,
racc_use_result_var ]

```

      
        Racc_token_to_s_table =
          
        
        

```
[
"$end",
"error",
"FUNCTION",
"INCLUDES",
"DASHMATCH",
"LBRACE",
"HASH",
"PLUS",
"GREATER",
"S",
"STRING",
"IDENT",
"COMMA",
"NUMBER",
"PREFIXMATCH",
"SUFFIXMATCH",
"SUBSTRINGMATCH",
"TILDE",
"NOT_EQUAL",
"SLASH",
"DOUBLESLASH",
"NOT",
"EQUAL",
"RPAREN",
"LSQUARE",
"RSQUARE",
"HAS",
"\"@\"",
"\".\"",
"\"*\"",
"\"|\"",
"\":\"",
"$start",
"selector",
"simple_selector_1toN",
"prefixless_combinator_selector",
"optional_S",
"combinator",
"xpath_attribute_name",
"xpath_attribute",
"simple_selector",
"element_name",
"hcap_0toN",
"function",
"pseudo",
"attrib",
"hcap_1toN",
"class",
"namespaced_ident",
"namespace",
"attrib_name",
"attrib_val_0or1",
"expr",
"nth",
"attribute_id",
"negation",
"eql_incl_dash",
"negation_arg" ]

```

      
        Racc_debug_parser =
          
        
        

```
false

```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**_reduce_1**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 0 omitted.

  

      
        
- 
  
    
      #**_reduce_10**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_11**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_13**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 12 omitted.

  

      
        
- 
  
    
      #**_reduce_14**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_15**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_17**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 16 omitted.

  

      
        
- 
  
    
      #**_reduce_18**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_19**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_2**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_21**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 20 omitted.

  

      
        
- 
  
    
      #**_reduce_23**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 22 omitted.

  

      
        
- 
  
    
      #**_reduce_24**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_25**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_26**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_28**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 27 omitted.

  

      
        
- 
  
    
      #**_reduce_29**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_3**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_30**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_31**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_32**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_34**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 33 omitted.

  

      
        
- 
  
    
      #**_reduce_35**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_36**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_37**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_38**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_39**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_4**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_40**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_41**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_42**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_45**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 44 omitted.

  

      
        
- 
  
    
      #**_reduce_47**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 46 omitted.

  

      
        
- 
  
    
      #**_reduce_48**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_49**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_5**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_50**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_51**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_54**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 53 omitted.

  

      
        
- 
  
    
      #**_reduce_55**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_56**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_57**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_58**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_6**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_64**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 63 omitted.

  

      
        
- 
  
    
      #**_reduce_65**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_66**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_67**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_69**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 68 omitted.

  

      
        
- 
  
    
      #**_reduce_7**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_70**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_71**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_72**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_73**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_74**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_75**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_76**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_8**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_9**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**_reduce_none**(val, _values, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

reduce 81 omitted.

  

      
        
- 
  
    
      #**initialize**  ⇒ Parser 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Parser.

  

      
        
- 
  
    
      #**next_token**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**on_error**(error_token_id, error_value, value_stack)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

On CSS parser error, raise an exception.

  

      
        
- 
  
    
      #**parse**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unescape_css_identifier**(identifier)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unescape_css_string**(str)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**xpath_for**(selector, visitor)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the xpath for `selector` using `visitor`.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ Parser 
  

  

  

  
    

Returns a new instance of Parser.

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/nokogiri/css/parser_extras.rb', line 8

def initialize
  @tokenizer = Tokenizer.new
  super
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**_reduce_1**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 0 omitted

  

  

  
    
      

```

363
364
365
366
367
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 363

def _reduce_1(val, _values, result)
      result = [val[0], val[2]].flatten

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_10**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

409
410
411
412
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 409

def _reduce_10(val, _values, result)
 result = Node.new(:ATTRIB_NAME, [val[0]])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_11**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

414
415
416
417
418
419
420
421
422
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 414

def _reduce_11(val, _values, result)
      result =  if val[1].nil?
                  val[0]
                else
                  Node.new(:CONDITIONAL_SELECTOR, [val[0], val[1]])
                end

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_13**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 12 omitted

  

  

  
    
      

```

426
427
428
429
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 426

def _reduce_13(val, _values, result)
 result = Node.new(:CONDITIONAL_SELECTOR, val)
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_14**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

431
432
433
434
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 431

def _reduce_14(val, _values, result)
 result = Node.new(:CONDITIONAL_SELECTOR, val)
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_15**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

436
437
438
439
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 436

def _reduce_15(val, _values, result)
 result = Node.new(:CONDITIONAL_SELECTOR, [Node.new(:ELEMENT_NAME, ['*']), val[0]])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_17**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 16 omitted

  

  

  
    
      

```

443
444
445
446
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 443

def _reduce_17(val, _values, result)
 result = Node.new(val[0], [nil, val[1]])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_18**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

448
449
450
451
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 448

def _reduce_18(val, _values, result)
 result = Node.new(val[1], [val[0], val[2]])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_19**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

453
454
455
456
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 453

def _reduce_19(val, _values, result)
 result = Node.new(:DESCENDANT_SELECTOR, [val[0], val[2]])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_2**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

369
370
371
372
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 369

def _reduce_2(val, _values, result)
 result = val.flatten
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_21**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 20 omitted

  

  

  
    
      

```

460
461
462
463
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 460

def _reduce_21(val, _values, result)
 result = Node.new(:CLASS_CONDITION, [unescape_css_identifier(val[1])])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_23**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 22 omitted

  

  

  
    
      

```

467
468
469
470
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 467

def _reduce_23(val, _values, result)
 result = Node.new(:ELEMENT_NAME, val)
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_24**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

472
473
474
475
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 472

def _reduce_24(val, _values, result)
 result = Node.new(:ELEMENT_NAME, [val[0], val[2]])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_25**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

477
478
479
480
481
482
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 477

def _reduce_25(val, _values, result)
      name = val[0]
      result = Node.new(:ELEMENT_NAME, [name])

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_26**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

484
485
486
487
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 484

def _reduce_26(val, _values, result)
 result = val[0]
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_28**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 27 omitted

  

  

  
    
      

```

491
492
493
494
495
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 491

def _reduce_28(val, _values, result)
      result = Node.new(:ATTRIBUTE_CONDITION, [val[1]] + (val[2] || []))

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_29**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

497
498
499
500
501
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 497

def _reduce_29(val, _values, result)
      result = Node.new(:ATTRIBUTE_CONDITION, [val[1]] + (val[2] || []))

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_3**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

374
375
376
377
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 374

def _reduce_3(val, _values, result)
 result = [val[1]].flatten
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_30**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

503
504
505
506
507
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 503

def _reduce_30(val, _values, result)
      result = Node.new(:PSEUDO_CLASS, [Node.new(:FUNCTION, ['nth-child(', val[1]])])

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_31**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

509
510
511
512
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 509

def _reduce_31(val, _values, result)
 result = Node.new(:ATTRIB_NAME, [[val[0], val[2]].compact.join(':')])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_32**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

514
515
516
517
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 514

def _reduce_32(val, _values, result)
 result = Node.new(:ATTRIB_NAME, [val[0]])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_34**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 33 omitted

  

  

  
    
      

```

521
522
523
524
525
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 521

def _reduce_34(val, _values, result)
      result = Node.new(:FUNCTION, [val[0].strip])

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_35**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

527
528
529
530
531
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 527

def _reduce_35(val, _values, result)
      result = Node.new(:FUNCTION, [val[0].strip, val[1]].flatten)

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_36**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

533
534
535
536
537
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 533

def _reduce_36(val, _values, result)
      result = Node.new(:FUNCTION, [val[0].strip, val[1]].flatten)

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_37**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

539
540
541
542
543
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 539

def _reduce_37(val, _values, result)
      result = Node.new(:FUNCTION, [val[0].strip, val[1]].flatten)

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_38**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

545
546
547
548
549
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 545

def _reduce_38(val, _values, result)
      result = Node.new(:FUNCTION, [val[0].strip, val[1]].flatten)

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_39**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

551
552
553
554
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 551

def _reduce_39(val, _values, result)
 result = [val[0], val[2]]
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_4**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

379
380
381
382
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 379

def _reduce_4(val, _values, result)
 result = :DIRECT_ADJACENT_SELECTOR
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_40**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

556
557
558
559
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 556

def _reduce_40(val, _values, result)
 result = [val[0], val[2]]
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_41**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

561
562
563
564
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 561

def _reduce_41(val, _values, result)
 result = [val[0], val[2]]
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_42**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

566
567
568
569
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 566

def _reduce_42(val, _values, result)
 result = [val[0], val[2]]
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_45**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 44 omitted

  

  

  
    
      

```

575
576
577
578
579
580
581
582
583
584
585
586
587
588
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 575

def _reduce_45(val, _values, result)
      case val[0]
      when 'even'
        result = Node.new(:NTH, ['2','n','+','0'])
      when 'odd'
        result = Node.new(:NTH, ['2','n','+','1'])
      when 'n'
        result = Node.new(:NTH, ['1','n','+','0'])
      else
        result = val
      end

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_47**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 46 omitted

  

  

  
    
      

```

592
593
594
595
596
597
598
599
600
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 592

def _reduce_47(val, _values, result)
      if val[1] == 'n'
        result = Node.new(:NTH, val)
      else
        raise Racc::ParseError, "parse error on IDENT '#{val[1]}'"
      end

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_48**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 602

def _reduce_48(val, _values, result)
               # n+3, -n+3
      if val[0] == 'n'
        val.unshift("1")
        result = Node.new(:NTH, val)
      elsif val[0] == '-n'
        val[0] = 'n'
        val.unshift("-1")
        result = Node.new(:NTH, val)
      else
        raise Racc::ParseError, "parse error on IDENT '#{val[1]}'"
      end

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_49**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 618

def _reduce_49(val, _values, result)
                    # 5n, -5n, 10n-1
      n = val[1]
      if n[0, 2] == 'n-'
        val[1] = 'n'
        val << "-"
        # b is contained in n as n is the string "n-b"
        val << n[2, n.size]
        result = Node.new(:NTH, val)
      elsif n == 'n'
        val << "+"
        val << "0"
        result = Node.new(:NTH, val)
      else
        raise Racc::ParseError, "parse error on IDENT '#{val[1]}'"
      end

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_5**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

384
385
386
387
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 384

def _reduce_5(val, _values, result)
 result = :CHILD_SELECTOR
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_50**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

638
639
640
641
642
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 638

def _reduce_50(val, _values, result)
      result = Node.new(:PSEUDO_CLASS, [val[1]])

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_51**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

644
645
646
647
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 644

def _reduce_51(val, _values, result)
 result = Node.new(:PSEUDO_CLASS, [val[1]])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_54**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 53 omitted

  

  

  
    
      

```

653
654
655
656
657
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 653

def _reduce_54(val, _values, result)
      result = Node.new(:COMBINATOR, val)

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_55**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

659
660
661
662
663
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 659

def _reduce_55(val, _values, result)
      result = Node.new(:COMBINATOR, val)

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_56**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

665
666
667
668
669
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 665

def _reduce_56(val, _values, result)
      result = Node.new(:COMBINATOR, val)

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_57**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

671
672
673
674
675
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 671

def _reduce_57(val, _values, result)
      result = Node.new(:COMBINATOR, val)

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_58**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

677
678
679
680
681
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 677

def _reduce_58(val, _values, result)
      result = Node.new(:COMBINATOR, val)

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_6**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

389
390
391
392
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 389

def _reduce_6(val, _values, result)
 result = :FOLLOWING_SELECTOR
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_64**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 63 omitted

  

  

  
    
      

```

693
694
695
696
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 693

def _reduce_64(val, _values, result)
 result = Node.new(:ID, [unescape_css_identifier(val[0])])
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_65**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

698
699
700
701
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 698

def _reduce_65(val, _values, result)
 result = [val[0], unescape_css_identifier(val[1])]
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_66**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

703
704
705
706
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 703

def _reduce_66(val, _values, result)
 result = [val[0], unescape_css_string(val[1])]
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_67**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

708
709
710
711
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 708

def _reduce_67(val, _values, result)
 result = [val[0], val[1]]
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_69**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 68 omitted

  

  

  
    
      

```

715
716
717
718
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 715

def _reduce_69(val, _values, result)
 result = :equal
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_7**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

394
395
396
397
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 394

def _reduce_7(val, _values, result)
 result = :DESCENDANT_SELECTOR
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_70**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

720
721
722
723
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 720

def _reduce_70(val, _values, result)
 result = :prefix_match
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_71**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

725
726
727
728
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 725

def _reduce_71(val, _values, result)
 result = :suffix_match
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_72**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

730
731
732
733
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 730

def _reduce_72(val, _values, result)
 result = :substring_match
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_73**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

735
736
737
738
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 735

def _reduce_73(val, _values, result)
 result = :not_equal
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_74**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

740
741
742
743
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 740

def _reduce_74(val, _values, result)
 result = :includes
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_75**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

745
746
747
748
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 745

def _reduce_75(val, _values, result)
 result = :dash_match
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_76**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

750
751
752
753
754
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 750

def _reduce_76(val, _values, result)
      result = Node.new(:NOT, [val[1]])

    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_8**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

399
400
401
402
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 399

def _reduce_8(val, _values, result)
 result = :CHILD_SELECTOR
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_9**(val, _values, result)  ⇒ Object 
  

  

  

  
    
      

```

404
405
406
407
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 404

def _reduce_9(val, _values, result)
 result = val[1]
    result
end

```

    
  

    
      
  
### 
  
    #**_reduce_none**(val, _values, result)  ⇒ Object 
  

  

  

  
    

reduce 81 omitted

  

  

  
    
      

```

766
767
768
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 766

def _reduce_none(val, _values, result)
  val[0]
end

```

    
  

    
      
  
### 
  
    #**next_token**  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/nokogiri/css/parser_extras.rb', line 18

def next_token
  @tokenizer.next_token
end

```

    
  

    
      
  
### 
  
    #**on_error**(error_token_id, error_value, value_stack)  ⇒ Object 
  

  

  

  
    

On CSS parser error, raise an exception

  

  

Raises:

  
    
- 
      
      
        (SyntaxError)
      
      
      
    
  

  
    
      

```

30
31
32
33
```

    
    
      

```
# File 'lib/nokogiri/css/parser_extras.rb', line 30

def on_error(error_token_id, error_value, value_stack)
  after = value_stack.compact.last
  raise SyntaxError, "unexpected '#{error_value}' after '#{after}'"
end

```

    
  

    
      
  
### 
  
    #**parse**(string)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
```

    
    
      

```
# File 'lib/nokogiri/css/parser_extras.rb', line 13

def parse(string)
  @tokenizer.scan_setup(string)
  do_parse
end

```

    
  

    
      
  
### 
  
    #**unescape_css_identifier**(identifier)  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 26

def unescape_css_identifier(identifier)
  identifier.gsub(/\\(?:([^0-9a-fA-F])|([0-9a-fA-F]{1,6})\s?)/){ |m| $1 || [$2.hex].pack('U') }
end

```

    
  

    
      
  
### 
  
    #**unescape_css_string**(str)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/nokogiri/css/parser.rb', line 30

def unescape_css_string(str)
  str.gsub(/\\(?:([^0-9a-fA-F])|([0-9a-fA-F]{1,6})\s?)/) do |m|
    if $1=="\n"
      ''
    else
      $1 || [$2.hex].pack('U')
    end
  end
end

```

    
  

    
      
  
### 
  
    #**xpath_for**(selector, visitor)  ⇒ Object 
  

  

  

  
    

Get the xpath for `selector` using `visitor`

  

  

  
    
      

```

23
24
25
26
27
```

    
    
      

```
# File 'lib/nokogiri/css/parser_extras.rb', line 23

def xpath_for(selector, visitor)
  parse(selector).map do |ast|
    ast.to_xpath(visitor)
  end
end

```