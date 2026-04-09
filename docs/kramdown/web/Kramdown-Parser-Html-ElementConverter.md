# Class: Kramdown::Parser::Html::ElementConverter
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Kramdown::Parser::Html::ElementConverter
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Constants, Utils::Entities
  
  
  

  

  
  
    Defined in:
    lib/kramdown/parser/html.rb
  
  

## Overview

  
    

Converts HTML elements to native elements if possible.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        REMOVE_TEXT_CHILDREN =
          
        
        

```
%w[html head hgroup ol ul dl table colgroup tbody thead tfoot tr
select optgroup]

```

      
        WRAP_TEXT_CHILDREN =
          
        
        

```
%w[body section nav article aside header footer address div li dd
blockquote figure figcaption fieldset form]

```

      
        REMOVE_WHITESPACE_CHILDREN =
          
        
        

```
%w[body section nav article aside header footer address
div li dd blockquote figure figcaption td th fieldset form]

```

      
        STRIP_WHITESPACE =
          
        
        

```
%w[address article aside blockquote body caption dd div dl dt fieldset
figcaption form footer header h1 h2 h3 h4 h5 h6 legend li nav p
section td th]

```

      
        SIMPLE_ELEMENTS =
          
        
        

```
%w[em strong blockquote hr br img p thead tbody tfoot tr td th ul ol dl
li dl dt dd]

```

      
        EMPHASIS_TYPE_MAP =
          
        
        

```
{'em' => :em, 'i' => :em, 'strong' => :strong, 'b' => :strong}

```

      
    
  

  
  
  
### Constants included
     from Utils::Entities

  

Utils::Entities::ENTITY_MAP, Utils::Entities::ENTITY_TABLE

  
  
  
### Constants included
     from Constants

  

Constants::HTML_ATTRIBUTE_RE, Constants::HTML_BLOCK_ELEMENTS, Constants::HTML_CDATA_RE, Constants::HTML_COMMENT_RE, Constants::HTML_CONTENT_MODEL, Constants::HTML_CONTENT_MODEL_BLOCK, Constants::HTML_CONTENT_MODEL_RAW, Constants::HTML_CONTENT_MODEL_SPAN, Constants::HTML_DOCTYPE_RE, Constants::HTML_ELEMENT, Constants::HTML_ELEMENTS_WITHOUT_BODY, Constants::HTML_ENTITY_RE, Constants::HTML_INSTRUCTION_RE, Constants::HTML_SPAN_ELEMENTS, Constants::HTML_TAG_CLOSE_RE, Constants::HTML_TAG_RE

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**convert**(root, el = root)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**convert_a**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_code**(el)  ⇒ Object 
    

    
      (also: #convert_pre)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_em**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_h1**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_script**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_table**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_textarea**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**extract_text**(el, raw)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**handle_math_tag**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(root)  ⇒ ElementConverter 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ElementConverter.

  

      
        
- 
  
    
      #**is_math_tag?**(el)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**is_simple_table?**(el)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process**(el, do_conversion = true, preserve_text = false, parent = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert the element `el` and its children.

  

      
        
- 
  
    
      #**process_children**(el, do_conversion = true, preserve_text = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_html_element**(el, do_conversion = true, preserve_text = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_text**(raw, preserve = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process the HTML text `raw`: compress whitespace (if `preserve` is `false`) and convert entities in entity elements.

  

      
        
- 
  
    
      #**remove_text_children**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_whitespace_children**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**set_basics**(el, type, opts = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**strip_whitespace**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrap_text_children**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Utils::Entities

  

entity

  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(root)  ⇒ ElementConverter 
  

  

  

  
    

Returns a new instance of ElementConverter.

  

  

  
    
      

```

219
220
221
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 219

def initialize(root)
  @root = root
end

```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**convert**(root, el = root)  ⇒ Object 
  

  

  

  
    
      

```

223
224
225
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 223

def self.convert(root, el = root)
  new(root).process(el)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**convert_a**(el)  ⇒ Object 
  

  

  

  
    
      

```

388
389
390
391
392
393
394
395
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 388

def convert_a(el)
  if el.attr['href']
    set_basics(el, :a)
    process_children(el)
  else
    process_html_element(el, false)
  end
end

```

    
  

    
      
  
### 
  
    #**convert_code**(el)  ⇒ Object 
  

  
    Also known as:
    convert_pre
    
  

  

  
    
      

```

421
422
423
424
425
426
427
428
429
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
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 421

def convert_code(el)
  raw = +''
  extract_text(el, raw)
  result = process_text(raw, true)
  begin
    str = result.inject(+'') do |mem, c|
      case c.type
      when :text
        mem << c.value
      when :entity
        mem << if [60, 62, 34, 38].include?(c.value.code_point)
                 c.value.code_point.chr
               else
                 c.value.char
               end
      when :smart_quote, :typographic_sym
        mem << entity(c.value.to_s).char
      else
        raise "Bug - please report"
      end
    end
    result.clear
    result << Element.new(:text, str)
  rescue StandardError
  end
  if result.length > 1 || result.first.type != :text
    process_html_element(el, false, true)
  else
    if el.value == 'code'
      set_basics(el, :codespan)
      el.attr['class']&.gsub!(/\s+\bhighlighter-\w+\b|\bhighlighter-\w+\b\s*/, '')
    else
      set_basics(el, :codeblock)
      if el.children.size == 1 && el.children.first.value == 'code'
        value = (el.children.first.attr['class'] || '').scan(/\blanguage-\S+/).first
        el.attr['class'] = "#{value} #{el.attr['class']}".rstrip if value
      end
    end
    el.value = result.first.value
    el.children.clear
  end
end

```

    
  

    
      
  
### 
  
    #**convert_em**(el)  ⇒ Object 
  

  

  

  
    
      

```

398
399
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
# File 'lib/kramdown/parser/html.rb', line 398

def convert_em(el)
  text = +''
  extract_text(el, text)
  if text =~ /\A\s/ || text =~ /\s\z/
    process_html_element(el, false)
  else
    set_basics(el, EMPHASIS_TYPE_MAP[el.value])
    process_children(el)
  end
end

```

    
  

    
      
  
### 
  
    #**convert_h1**(el)  ⇒ Object 
  

  

  

  
    
      

```

412
413
414
415
416
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 412

def convert_h1(el)
  set_basics(el, :header, level: el.value[1..1].to_i)
  extract_text(el, el.options[:raw_text] = +'')
  process_children(el)
end

```

    
  

    
      
  
### 
  
    #**convert_script**(el)  ⇒ Object 
  

  

  

  
    
      

```

570
571
572
573
574
575
576
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 570

def convert_script(el)
  if is_math_tag?(el)
    handle_math_tag(el)
  else
    process_html_element(el)
  end
end

```

    
  

    
      
  
### 
  
    #**convert_table**(el)  ⇒ Object 
  

  

  

  
    
      

```

465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 465

def convert_table(el)
  unless is_simple_table?(el)
    process_html_element(el, false)
    return
  end
  remove_text_children(el)
  process_children(el)
  set_basics(el, :table)

  calc_alignment = lambda do |c|
    if c.type == :tr
      el.options[:alignment] = c.children.map do |td|
        if td.attr['style']
          td.attr['style'].slice!(/(?:;\s*)?text-align:\s+(center|left|right)/)
          td.attr.delete('style') if td.attr['style'].strip.empty?
          $1 ? $1.to_sym : :default
        else
          :default
        end
      end
    else
      c.children.each {|cc| calc_alignment.call(cc) }
    end
  end
  calc_alignment.call(el)
  el.children.delete_if {|c| c.type == :html_element }

  change_th_type = lambda do |c|
    if c.type == :th
      c.type = :td
    else
      c.children.each {|cc| change_th_type.call(cc) }
    end
  end
  change_th_type.call(el)

  if el.children.first.type == :tr
    tbody = Element.new(:tbody)
    tbody.children = el.children
    el.children = [tbody]
  end
end

```

    
  

    
      
  
### 
  
    #**convert_textarea**(el)  ⇒ Object 
  

  

  

  
    
      

```

384
385
386
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 384

def convert_textarea(el)
  process_html_element(el, true, true)
end

```

    
  

    
      
  
### 
  
    #**extract_text**(el, raw)  ⇒ Object 
  

  

  

  
    
      

```

379
380
381
382
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 379

def extract_text(el, raw)
  raw << el.value.to_s if el.type == :text
  el.children.each {|c| extract_text(c, raw) }
end

```

    
  

    
      
  
### 
  
    #**handle_math_tag**(el)  ⇒ Object 
  

  

  

  
    
      

```

582
583
584
585
586
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 582

def handle_math_tag(el)
  set_basics(el, :math, category: (el.attr['type'].include?("mode=display") ? :block : :span))
  el.value = el.children.shift.value.sub(/\A(?:%\s*)?<!\[CDATA\[\n?(.*?)(?:\s%)?\]\]>\z/m, '\1')
  el.attr.delete('type')
end

```

    
  

    
      
  
### 
  
    #**is_math_tag?**(el)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

578
579
580
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 578

def is_math_tag?(el)
  el.attr['type'].to_s =~ /\bmath\/tex\b/
end

```

    
  

    
      
  
### 
  
    #**is_simple_table?**(el)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 508

def is_simple_table?(el)
  only_phrasing_content = lambda do |c|
    c.children.all? do |cc|
      (cc.type == :text || !HTML_BLOCK_ELEMENTS.include?(cc.value)) && only_phrasing_content.call(cc)
    end
  end
  check_cells = proc do |c|
    if c.value == 'th' || c.value == 'td'
      return false unless only_phrasing_content.call(c)
    else
      c.children.each {|cc| check_cells.call(cc) }
    end
  end
  check_cells.call(el)

  nr_cells = 0
  check_nr_cells = lambda do |t|
    if t.value == 'tr'
      count = t.children.count {|cc| cc.value == 'th' || cc.value == 'td' }
      if count != nr_cells
        if nr_cells == 0
          nr_cells = count
        else
          nr_cells = -1
          break
        end
      end
    else
      t.children.each {|cc| check_nr_cells.call(cc) }
    end
  end
  check_nr_cells.call(el)
  return false if nr_cells == -1 || nr_cells == 0

  alignment = nil
  check_alignment = proc do |t|
    if t.value == 'tr'
      cur_alignment = t.children.select {|cc| cc.value == 'th' || cc.value == 'td' }.map do |cell|
        md = /text-align:\s+(center|left|right|justify|inherit)/.match(cell.attr['style'].to_s)
        return false if md && (md[1] == 'justify' || md[1] == 'inherit')
        md.nil? ? :default : md[1]
      end
      alignment = cur_alignment if alignment.nil?
      return false if alignment != cur_alignment
    else
      t.children.each {|cc| check_alignment.call(cc) }
    end
  end
  check_alignment.call(el)

  check_rows = lambda do |t, type|
    t.children.all? do |r|
      (r.value == 'tr' || r.type == :text) && r.children.all? {|c| c.value == type || c.type == :text }
    end
  end
  check_rows.call(el, 'td') ||
    (el.children.all? do |t|
       t.type == :text || (t.value == 'thead' && check_rows.call(t, 'th')) ||
         ((t.value == 'tfoot' || t.value == 'tbody') && check_rows.call(t, 'td'))
     end && el.children.any? {|t| t.value == 'tbody' })
end

```

    
  

    
      
  
### 
  
    #**process**(el, do_conversion = true, preserve_text = false, parent = nil)  ⇒ Object 
  

  

  

  
    

Convert the element `el` and its children.

  

  

  
    
      

```

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
261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 228

def process(el, do_conversion = true, preserve_text = false, parent = nil)
  case el.type
  when :xml_comment, :xml_pi
    ptype = if parent.nil?
              'div'
            else
              case parent.type
              when :html_element then parent.value
              when :code_span then 'code'
              when :code_block then 'pre'
              when :header then 'h1'
              else parent.type.to_s
              end
            end
    el.options.replace(category: (HTML_CONTENT_MODEL[ptype] == :span ? :span : :block))
    return
  when :html_element
    # do nothing
  when :root
    el.children.map! do |c|
      if c.type == :text
        process_text(c.value, !do_conversion)
      else
        process(c)
        c
      end
    end.flatten!
    remove_whitespace_children(el)
    return
  else return
  end

  mname = "convert_#{el.value}"
  if do_conversion && self.class.method_defined?(mname)
    send(mname, el)
  else
    type = el.value
    remove_text_children(el) if do_conversion && REMOVE_TEXT_CHILDREN.include?(type)

    if do_conversion && SIMPLE_ELEMENTS.include?(type)
      set_basics(el, type.intern)
      process_children(el, do_conversion, preserve_text)
    else
      process_html_element(el, do_conversion, preserve_text)
    end

    if do_conversion
      strip_whitespace(el) if STRIP_WHITESPACE.include?(type)
      remove_whitespace_children(el) if REMOVE_WHITESPACE_CHILDREN.include?(type)
      wrap_text_children(el) if WRAP_TEXT_CHILDREN.include?(type)
    end
  end
end

```

    
  

    
      
  
### 
  
    #**process_children**(el, do_conversion = true, preserve_text = false)  ⇒ Object 
  

  

  

  
    
      

```

282
283
284
285
286
287
288
289
290
291
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 282

def process_children(el, do_conversion = true, preserve_text = false)
  el.children.map! do |c|
    if c.type == :text
      process_text(c.value, preserve_text || !do_conversion)
    else
      process(c, do_conversion, preserve_text, el)
      c
    end
  end.flatten!
end

```

    
  

    
      
  
### 
  
    #**process_html_element**(el, do_conversion = true, preserve_text = false)  ⇒ Object 
  

  

  

  
    
      

```

324
325
326
327
328
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 324

def process_html_element(el, do_conversion = true, preserve_text = false)
  el.options.replace(category: HTML_SPAN_ELEMENTS.include?(el.value) ? :span : :block,
                     content_model: (do_conversion ? HTML_CONTENT_MODEL[el.value] : :raw))
  process_children(el, do_conversion, preserve_text)
end

```

    
  

    
      
  
### 
  
    #**process_text**(raw, preserve = false)  ⇒ Object 
  

  

  

  
    

Process the HTML text `raw`: compress whitespace (if `preserve` is `false`) and convert entities in entity elements.

  

  

  
    
      

```

295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 295

def process_text(raw, preserve = false)
  raw.gsub!(/\s+/, ' ') unless preserve
  src = Kramdown::Utils::StringScanner.new(raw)
  result = []
  until src.eos?
    if (tmp = src.scan_until(/(?=#{HTML_ENTITY_RE})/o))
      result << Element.new(:text, tmp)
      src.scan(HTML_ENTITY_RE)
      val = src[1] || src[2]&.to_i || src[3].hex
      result << if %w[lsquo rsquo ldquo rdquo].include?(val)
                  Element.new(:smart_quote, val.intern)
                elsif %w[mdash ndash hellip laquo raquo].include?(val)
                  Element.new(:typographic_sym, val.intern)
                else
                  begin
                    Element.new(:entity, entity(val), nil, original: src.matched)
                  rescue ::Kramdown::Error
                    src.pos -= src.matched_size - 1
                    Element.new(:entity, ::Kramdown::Utils::Entities.entity('amp'))
                  end
                end
    else
      result << Element.new(:text, src.rest)
      src.terminate
    end
  end
  result
end

```

    
  

    
      
  
### 
  
    #**remove_text_children**(el)  ⇒ Object 
  

  

  

  
    
      

```

330
331
332
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 330

def remove_text_children(el)
  el.children.delete_if {|c| c.type == :text }
end

```

    
  

    
      
  
### 
  
    #**remove_whitespace_children**(el)  ⇒ Object 
  

  

  

  
    
      

```

363
364
365
366
367
368
369
370
371
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 363

def remove_whitespace_children(el)
  i = -1
  el.children = el.children.reject do |c|
    i += 1
    c.type == :text && c.value.strip.empty? &&
      (i == 0 || i == el.children.length - 1 || (el.children[i - 1].block? &&
                                                 el.children[i + 1].block?))
  end
end

```

    
  

    
      
  
### 
  
    #**set_basics**(el, type, opts = {})  ⇒ Object 
  

  

  

  
    
      

```

373
374
375
376
377
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 373

def set_basics(el, type, opts = {})
  el.type = type
  el.options.replace(opts)
  el.value = nil
end

```

    
  

    
      
  
### 
  
    #**strip_whitespace**(el)  ⇒ Object 
  

  

  

  
    
      

```

353
354
355
356
357
358
359
360
361
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 353

def strip_whitespace(el)
  return if el.children.empty?
  if el.children.first.type == :text
    el.children.first.value.lstrip!
  end
  if el.children.last.type == :text
    el.children.last.value.rstrip!
  end
end

```

    
  

    
      
  
### 
  
    #**wrap_text_children**(el)  ⇒ Object 
  

  

  

  
    
      

```

334
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
347
348
349
350
351
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 334

def wrap_text_children(el)
  tmp = []
  last_is_p = false
  el.children.each do |c|
    if !c.block? || c.type == :text
      unless last_is_p
        tmp << Element.new(:p, nil, nil, transparent: true)
        last_is_p = true
      end
      tmp.last.children << c
      tmp
    else
      tmp << c
      last_is_p = false
    end
  end
  el.children = tmp
end

```