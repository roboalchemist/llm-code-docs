# Class: RuboCop::RSpec::ExpectOffense::AnnotatedSource
  
    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::RSpec::ExpectOffense::AnnotatedSource

        show all
      

    Defined in:
    lib/rubocop/rspec/expect_offense.rb
  
## Overview

Parsed representation of code annotated with the ‘^^^ Message` style

##

      Constant Summary
      collapse
    

    
      
        ANNOTATION_PATTERN =
          
  
    

Ignore escaped carets, don’t treat as annotations

```
/\A\s*((?<!\\)\^+|\^{}) ?/.freeze
```

        ABBREV =
          
        
        

```
"[...]\n"
```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**parse**(annotated_source)  ⇒ AnnotatedSource 
    

    
  
  
  
  
  
  
  
  

  
    

Separates annotation lines from source lines.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**==**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**(lines, annotations)  ⇒ AnnotatedSource 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of AnnotatedSource.

-
  
      #**match_annotations?**(other)  ⇒ Boolean 

Dirty hack: expectations with […] are rewritten when they match This way the diff is clean.

-
  
      #**plain_source**  ⇒ String 

Return the plain source code without annotations.

-
  
      #**to_s**  ⇒ String 

      (also: #inspect)
    
  
  
  
  
  
  
  
  

  
    

Construct annotated source string (like what we parse).

-
  
      #**with_offense_annotations**(offenses)  ⇒ self 

Annotate the source code with the RuboCop offenses provided.

## Constructor Details

###
  
    #**initialize**(lines, annotations)  ⇒ AnnotatedSource 
  

  

  

  
    
  
    **Note:**
    

annotations are sorted so that reconstructing the annotation text via #to_s is deterministic

Returns a new instance of AnnotatedSource.

Parameters:

-

        lines

        (Array<String>)
      
      
      
    
  
    
-

        annotations
      
      
        (Array<(Integer, String)>)
      
      
      
        —
        

each entry is the annotated line number and the annotation text

```

265
266
267
268
```

```
# File 'lib/rubocop/rspec/expect_offense.rb', line 265

def initialize(lines, annotations)
  @lines       = lines.freeze
  @annotations = annotations.sort.freeze
end
```

## Class Method Details

###
  
    .**parse**(annotated_source)  ⇒ AnnotatedSource 
  

  

  

  
    

Separates annotation lines from source lines. Tracks the real source line number that each annotation corresponds to.

Parameters:

-

        annotated_source

        (String)
      
      
      
        —
        

string passed to the matchers

Returns:

-

        (AnnotatedSource)

```

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
```

```
# File 'lib/rubocop/rspec/expect_offense.rb', line 243

def self.parse(annotated_source)
  source      = []
  annotations = []

  annotated_source.each_line do |source_line|
    if ANNOTATION_PATTERN.match?(source_line)
      annotations << [source.size, source_line]
    else
      source << source_line
    end
  end
  annotations.each { |a| a[0] = 1 } if source.empty?

  new(source, annotations)
end
```

## Instance Method Details

###
  
    #**==**(other)  ⇒ Object 
  

  

  

  
    
      

```

270
271
272
```

```
# File 'lib/rubocop/rspec/expect_offense.rb', line 270

def ==(other)
  other.is_a?(self.class) && other.lines == lines && match_annotations?(other)
end
```

###
  
    #**match_annotations?**(other)  ⇒ Boolean 
  

  

  

  
    

Dirty hack: expectations with […] are rewritten when they match This way the diff is clean.

Returns:

-

        (Boolean)

```

276
277
278
279
280
281
282
283
284
285
286
287
```

```
# File 'lib/rubocop/rspec/expect_offense.rb', line 276

def match_annotations?(other)
  annotations.zip(other.annotations) do |(_actual_line, actual_annotation),
                                         (_expected_line, expected_annotation)|
    if expected_annotation&.end_with?(ABBREV) &&
       actual_annotation.start_with?(expected_annotation[0...-ABBREV.length])

      expected_annotation.replace(actual_annotation)
    end
  end

  annotations == other.annotations
end
```

###
  
    #**plain_source**  ⇒ String 
  

  

  

  
    

Return the plain source code without annotations

Returns:

-

        (String)

```

326
327
328
```

```
# File 'lib/rubocop/rspec/expect_offense.rb', line 326

def plain_source
  lines.join
end
```

###
  
    #**to_s**  ⇒ String 
  

  
    Also known as:
    inspect
    
  

  

  
    

Construct annotated source string (like what we parse)

Reconstruct a deterministic annotated source string. This is useful for eliminating semantically irrelevant annotation ordering differences.

#### Examples

#####

standardization

```

source1 = AnnotatedSource.parse(<<-RUBY)
line1
^ Annotation 1
 ^^ Annotation 2
RUBY

source2 = AnnotatedSource.parse(<<-RUBY)
line1
 ^^ Annotation 2
^ Annotation 1
RUBY

source1.to_s == source2.to_s # => true
```

Returns:

-

        (String)

```

312
313
314
315
316
317
318
319
320
```

```
# File 'lib/rubocop/rspec/expect_offense.rb', line 312

def to_s
  reconstructed = lines.dup

  annotations.reverse_each do |line_number, annotation|
    reconstructed.insert(line_number, annotation)
  end

  reconstructed.join
end
```

###
  
    #**with_offense_annotations**(offenses)  ⇒ self 
  

  

  

  
    

Annotate the source code with the RuboCop offenses provided

Parameters:

-

        offenses

        (Array<RuboCop::Cop::Offense>)
      
      
      
    
  
Returns:

-

        (self)

```

335
336
337
338
339
340
341
342
343
344
345
346
```

```
# File 'lib/rubocop/rspec/expect_offense.rb', line 335

def with_offense_annotations(offenses)
  offense_annotations =
    offenses.map do |offense|
      indent     = ' ' * offense.column
      carets     = '^' * offense.column_length
      carets     = '^{}' if offense.column_length.zero?

      [offense.line, "#{indent}#{carets} #{offense.message}\n"]
    end

  self.class.new(lines, offense_annotations)
end
```
