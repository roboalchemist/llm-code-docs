# Class: StackProf::Report
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- StackProf::Report
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/stackprof/report.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        MARSHAL_SIGNATURE =
          
        
        

```
"\x04\x08"
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**data**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute data.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**from_file**(file)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**from_json**(json)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**parse_json**(json)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**+**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**add_lines**(a, b)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_to_d3_flame_graph_format**(name, stacks, depth)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**files**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**flamegraph_row**(f, x, y, weight, addr)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**flamegraph_stacks**(raw)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**frames**(sort_by_total = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(data)  ⇒ Report 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Report.

  

      
        
- 
  
    
      #**max_samples**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**modeline**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**normalized_frames**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**overall_samples**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_alphabetical_flamegraph**(f = STDOUT, skip_common = true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_callgrind**(f = STDOUT)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_d3_flamegraph**(f = STDOUT, skip_common = true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_debug**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_dump**(f = STDOUT)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_file**(filter, f = STDOUT)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_files**(sort_by_total = false, limit = nil, f = STDOUT)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_flamegraph**(f, skip_common, alphabetical = false)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_graphviz**(options = {}, f = STDOUT)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_json**(f = STDOUT)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_method**(name, f = STDOUT)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_stackcollapse**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_text**(sort_by_total = false, limit = nil, select_files = nil, reject_files = nil, select_names = nil, reject_names = nil, f = STDOUT)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**print_timeline_flamegraph**(f = STDOUT, skip_common = true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**version**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**walk_method**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Walk up and down the stack from a given starting point (name).

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(data)  ⇒ Report 
  

  

  

  
    

Returns a new instance of Report.

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 46

def initialize(data)
  @data = data
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**data**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute data.

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 49

def data
  @data
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**from_file**(file)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
17
18
19
20
21
22
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 12

def from_file(file)
  File.open(file, 'rb') do |f|
    signature_bytes = f.read(2)
    f.rewind
    if signature_bytes == MARSHAL_SIGNATURE
      new(Marshal.load(f))
    else
      from_json(JSON.parse(f.read))
    end
  end
end
```

    
  

    
      
  
### 
  
    .**from_json**(json)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 24

def from_json(json)
  new(parse_json(json))
end
```

    
  

    
      
  
### 
  
    .**parse_json**(json)  ⇒ Object 
  

  

  

  
    
      

```

28
29
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
42
43
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 28

def parse_json(json)
  json.keys.each do |key|
    value = json.delete(key)
    from_json(value) if value.is_a?(Hash)

    new_key = case key
    when /\A[0-9]*\z/
      key.to_i
    else
      key.to_sym
    end

    json[new_key] = value
  end
  json
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**+**(other)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

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
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 622

def +(other)
  raise ArgumentError, "cannot combine #{other.class}" unless self.class == other.class
  raise ArgumentError, "cannot combine #{modeline} with #{other.modeline}" unless modeline == other.modeline
  raise ArgumentError, "cannot combine v#{version} with v#{other.version}" unless version == other.version

  f1, f2 = normalized_frames, other.normalized_frames
  frames = (f1.keys + f2.keys).uniq.inject(Hash.new) do |hash, id|
    if f1[id].nil?
      hash[id] = f2[id]
    elsif f2[id]
      hash[id] = f1[id]
      hash[id][:total_samples] += f2[id][:total_samples]
      hash[id][:samples] += f2[id][:samples]
      if f2[id][:edges]
        edges = hash[id][:edges] ||= {}
        f2[id][:edges].each do |edge, weight|
          edges[edge] ||= 0
          edges[edge] += weight
        end
      end
      if f2[id][:lines]
        lines = hash[id][:lines] ||= {}
        f2[id][:lines].each do |line, weight|
          lines[line] = add_lines(lines[line], weight)
        end
      end
    else
      hash[id] = f1[id]
    end
    hash
  end

  d1, d2 = data, other.data
  data = {
    version: version,
    mode: d1[:mode],
    interval: d1[:interval],
    samples: d1[:samples] + d2[:samples],
    gc_samples: d1[:gc_samples] + d2[:gc_samples],
    missed_samples: d1[:missed_samples] + d2[:missed_samples],
    frames: frames
  }

  self.class.new(data)
end
```

    
  

    
      
  
### 
  
    #**add_lines**(a, b)  ⇒ Object 
  

  

  

  
    
      

```

96
97
98
99
100
101
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 96

def add_lines(a, b)
  return b if a.nil?
  return a+b if a.is_a? Integer
  return [ a[0], a[1]+b ] if b.is_a? Integer
  [ a[0]+b[0], a[1]+b[1] ]
end
```

    
  

    
      
  
### 
  
    #**convert_to_d3_flame_graph_format**(name, stacks, depth)  ⇒ Object 
  

  

  

  
    
      

```

216
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
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 216

def convert_to_d3_flame_graph_format(name, stacks, depth)
  weight = 0
  children = []
  stacks.chunk do |stack|
    if depth == stack.length - 1
      :leaf
    else
      stack[depth]
    end
  end.each do |val, child_stacks|
    if val == :leaf
      child_stacks.each do |stack|
        weight += stack.last
      end
    else
      frame = @data[:frames][val]
      child_name = "#{ frame[:name] } : #{ frame[:file] } : #{ frame[:line] }"
      child_data = convert_to_d3_flame_graph_format(child_name, child_stacks, depth + 1)
      weight += child_data["value"]
      children << child_data
    end
  end

  {
    "name" => name,
    "value" => weight,
    "children" => children,
  }
end
```

    
  

    
      
  
### 
  
    #**files**  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/stackprof/report.rb', line 84

def files
  @data[:files] ||= @data[:frames].inject(Hash.new) do |hash, (addr, frame)|
    if file = frame[:file] and lines = frame[:lines]
      hash[file] ||= Hash.new
      lines.each do |line, weight|
        hash[file][line] = add_lines(hash[file][line], weight)
      end
    end
    hash
  end
end
```

    
  

    
      
  
### 
  
    #**flamegraph_row**(f, x, y, weight, addr)  ⇒ Object 
  

  

  

  
    
      

```

209
210
211
212
213
214
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 209

def flamegraph_row(f, x, y, weight, addr)
  frame = @data[:frames][addr]
  f.print ',' if @rows_started
  @rows_started = true
  f.puts %{{"x":#{x},"y":#{y},"width":#{weight},"frame_id":#{addr},"frame":#{frame[:name].dump},"file":#{frame[:file].dump}}}
end
```

    
  

    
      
  
### 
  
    #**flamegraph_stacks**(raw)  ⇒ Object 
  

  

  

  
    
      

```

191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 191

def flamegraph_stacks(raw)
  stacks = []
  max_x = 0
  max_y = 0
  idx = 0

  while len = raw[idx]
    idx += 1
    max_y = len if len > max_y
    stack = raw.slice(idx, len+1)
    idx += len+1
    stacks << stack
    max_x += stack.last
  end

  return stacks, max_x, max_y
end
```

    
  

    
      
  
### 
  
    #**frames**(sort_by_total = false)  ⇒ Object 
  

  

  

  
    
      

```

51
52
53
54
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 51

def frames(sort_by_total=false)
  @data[:"sorted_frames_#{sort_by_total}"] ||=
    @data[:frames].sort_by{ |iseq, stats| -stats[sort_by_total ? :total_samples : :samples] }.inject({}){|h, (k, v)| h[k] = v; h}
end
```

    
  

    
      
  
### 
  
    #**max_samples**  ⇒ Object 
  

  

  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 80

def max_samples
  @data[:max_samples] ||= @data[:frames].values.max_by{ |frame| frame[:samples] }[:samples]
end
```

    
  

    
      
  
### 
  
    #**modeline**  ⇒ Object 
  

  

  

  
    
      

```

72
73
74
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 72

def modeline
  "#{@data[:mode]}(#{@data[:interval]})"
end
```

    
  

    
      
  
### 
  
    #**normalized_frames**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 56

def normalized_frames
  id2hash = {}
  @data[:frames].each do |frame, info|
    id2hash[frame.to_s] = info[:hash] = Digest::SHA256.hexdigest("#{info[:name]}#{info[:file]}#{info[:line]}")
  end
  @data[:frames].inject(Hash.new) do |hash, (frame, info)|
    info = hash[id2hash[frame.to_s]] = info.dup
    info[:edges] = info[:edges].inject(Hash.new){ |edges, (edge, weight)| edges[id2hash[edge.to_s]] = weight; edges } if info[:edges]
    hash
  end
end
```

    
  

    
      
  
### 
  
    #**overall_samples**  ⇒ Object 
  

  

  

  
    
      

```

76
77
78
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 76

def overall_samples
  @data[:samples]
end
```

    
  

    
      
  
### 
  
    #**print_alphabetical_flamegraph**(f = STDOUT, skip_common = true)  ⇒ Object 
  

  

  

  
    
      

```

132
133
134
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 132

def print_alphabetical_flamegraph(f=STDOUT, skip_common=true)
  print_flamegraph(f, skip_common, true)
end
```

    
  

    
      
  
### 
  
    #**print_callgrind**(f = STDOUT)  ⇒ Object 
  

  

  

  
    
      

```

499
500
501
502
503
504
505
506
507
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
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 499

def print_callgrind(f = STDOUT)
  f.puts "version: 1"
  f.puts "creator: stackprof"
  f.puts "pid: 0"
  f.puts "cmd: ruby"
  f.puts "part: 1"
  f.puts "desc: mode: #{modeline}"
  f.puts "desc: missed: #{@data[:missed_samples]})"
  f.puts "positions: line"
  f.puts "events: Instructions"
  f.puts "summary: #{@data[:samples]}"

  list = frames
  list.each do |addr, frame|
    f.puts "fl=#{frame[:file]}"
    f.puts "fn=#{frame[:name]}"
    frame[:lines].each do |line, weight|
      f.puts "#{line} #{weight.is_a?(Array) ? weight[1] : weight}"
    end if frame[:lines]
    frame[:edges].each do |edge, weight|
      oframe = list[edge]
      f.puts "cfl=#{oframe[:file]}" unless oframe[:file] == frame[:file]
      f.puts "cfn=#{oframe[:name]}"
      f.puts "calls=#{weight} #{frame[:line] || 0}\n#{oframe[:line] || 0} #{weight}"
    end if frame[:edges]
    f.puts
  end

  f.puts "totals: #{@data[:samples]}"
end
```

    
  

    
      
  
### 
  
    #**print_d3_flamegraph**(f = STDOUT, skip_common = true)  ⇒ Object 
  

  

  

  
    
      

```

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
281
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
292
293
294
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
323
324
325
326
327
328
329
330
331
332
333
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
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
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
408
409
410
411
412
413
414
415
416
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 246

def print_d3_flamegraph(f=STDOUT, skip_common=true)
  raise "profile does not include raw samples (add `raw: true` to collecting StackProf.run)" unless raw = data[:raw]

  stacks, * = flamegraph_stacks(raw)

  # d3-flame-grpah supports only alphabetical flamegraph
  stacks.sort!

  require "json"
  json = JSON.generate(convert_to_d3_flame_graph_format("<root>", stacks, 0), max_nesting: false)

  # This html code is almost copied from d3-flame-graph sample code.
  # (Apache License 2.0)
  # https://github.com/spiermar/d3-flame-graph/blob/gh-pages/index.html

  f.print <<-END
<!DOCTYPE html>
<html lang="en">
  <head>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">

<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
<link rel="stylesheet" type="text/css" href="https://cdn.jsdelivr.net/gh/spiermar/[email protected]/dist/d3-flamegraph.css">

<style>

/* Space out content a bit */
body {
  padding-top: 20px;
  padding-bottom: 20px;
}

/* Custom page header */
.header {
  padding-bottom: 20px;
  padding-right: 15px;
  padding-left: 15px;
  border-bottom: 1px solid #e5e5e5;
}

/* Make the masthead heading the same height as the navigation */
.header h3 {
  margin-top: 0;
  margin-bottom: 0;
  line-height: 40px;
}

/* Customize container */
.container {
  max-width: 990px;
}

address {
  text-align: right;
}
</style>

<title>stackprof (mode: #{ data[:mode] })</title>

<!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
<!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
<![endif]-->
  </head>
  <body>
<div class="container">
  <div class="header clearfix">
    <nav>
      <div class="pull-right">
        <form class="form-inline" id="form">
          <a class="btn" href="javascript: resetZoom();">Reset zoom</a>
          <a class="btn" href="javascript: clear();">Clear</a>
          <div class="form-group">
            <input type="text" class="form-control" id="term">
          </div>
          <a class="btn btn-primary" href="javascript: search();">Search</a>
        </form>
      </div>
    </nav>
    <h3 class="text-muted">stackprof (mode: #{ data[:mode] })</h3>
  </div>
  <div id="chart">
  </div>
  <address>
    powered by <a href="https://github.com/spiermar/d3-flame-graph">d3-flame-graph</a>
  </address>
  <hr>
  <div id="details">
  </div>
</div>

<!-- D3.js -->
<script src="https://d3js.org/d3.v4.min.js" charset="utf-8"></script>

<!-- d3-tip -->
<script type="text/javascript" src=https://cdnjs.cloudflare.com/ajax/libs/d3-tip/0.9.1/d3-tip.min.js></script>

<!-- d3-flamegraph -->
<script type="text/javascript" src="https://cdn.jsdelivr.net/gh/spiermar/[email protected]/dist/d3-flamegraph.min.js"></script>

<script type="text/javascript">
var flameGraph = d3.flamegraph()
  .width(960)
  .cellHeight(18)
  .transitionDuration(750)
  .minFrameSize(5)
  .transitionEase(d3.easeCubic)
  .sort(true)
  //Example to sort in reverse order
  //.sort(function(a,b){ return d3.descending(a.name, b.name);})
  .title("")
  .onClick(onClick)
  .differential(false)
  .selfValue(false);

// Example on how to use custom tooltips using d3-tip.
// var tip = d3.tip()
//   .direction("s")
//   .offset([8, 0])
//   .attr('class', 'd3-flame-graph-tip')
//   .html(function(d) { return "name: " + d.data.name + ", value: " + d.data.value; });

// flameGraph.tooltip(tip);

var details = document.getElementById("details");
flameGraph.setDetailsElement(details);

// Example on how to use custom labels
// var label = function(d) {
//  return "name: " + d.name + ", value: " + d.value;
// }
// flameGraph.label(label);

// Example of how to set fixed chart height
// flameGraph.height(540);

d3.select("#chart")
    .datum(#{ json })
    .call(flameGraph);

document.getElementById("form").addEventListener("submit", function(event){
  event.preventDefault();
  search();
});

function search() {
  var term = document.getElementById("term").value;
  flameGraph.search(term);
}

function clear() {
  document.getElementById('term').value = '';
  flameGraph.clear();
}

function resetZoom() {
  flameGraph.resetZoom();
}

function onClick(d) {
  console.info("Clicked on " + d.data.name);
}
</script>
  </body>
</html>
  END
end
```

    
  

    
      
  
### 
  
    #**print_debug**  ⇒ Object 
  

  

  

  
    
      

```

103
104
105
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 103

def print_debug
  pp @data
end
```

    
  

    
      
  
### 
  
    #**print_dump**(f = STDOUT)  ⇒ Object 
  

  

  

  
    
      

```

107
108
109
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 107

def print_dump(f=STDOUT)
  f.puts Marshal.dump(@data.reject{|k,v| k == :files })
end
```

    
  

    
      
  
### 
  
    #**print_file**(filter, f = STDOUT)  ⇒ Object 
  

  

  

  
    
      

```

614
615
616
617
618
619
620
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 614

def print_file(filter, f = STDOUT)
  filter = /#{Regexp.escape filter}/ unless Regexp === filter
  list = files.select{ |name, lines| name =~ filter }
  list.sort_by{ |file, vals| -vals.values.inject(0){ |sum, n| sum + (n.is_a?(Array) ? n[1] : n) } }.each do |file, lines|
    source_display(f, file, lines)
  end
end
```

    
  

    
      
  
### 
  
    #**print_files**(sort_by_total = false, limit = nil, f = STDOUT)  ⇒ Object 
  

  

  

  
    
      

```

604
605
606
607
608
609
610
611
612
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 604

def print_files(sort_by_total=false, limit=nil, f = STDOUT)
  list = files.map{ |file, vals| [file, vals.values.inject([0,0]){ |sum, n| add_lines(sum, n) }] }
  list = list.sort_by{ |file, samples| -samples[1] }
  list = list.first(limit) if limit
  list.each do |file, vals|
    total_samples, samples = *vals
    f.printf "% 5d  (%5.1f%%) / % 5d  (%5.1f%%)   %s\n", total_samples, (100.0*total_samples/overall_samples), samples, (100.0*samples/overall_samples), file
  end
end
```

    
  

    
      
  
### 
  
    #**print_flamegraph**(f, skip_common, alphabetical = false)  ⇒ Object 
  

  

  

  
    
      

```

136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 136

def print_flamegraph(f, skip_common, alphabetical=false)
  raise "profile does not include raw samples (add `raw: true` to collecting StackProf.run)" unless raw = data[:raw]

  stacks, max_x, max_y = flamegraph_stacks(raw)

  stacks.sort! if alphabetical

  f.puts 'flamegraph(['
  max_y.times do |y|
    row_prev = nil
    row_width = 0
    x = 0

    stacks.each do |stack|
      weight = stack.last
      cell = stack[y] unless y == stack.length-1

      if cell.nil?
        if row_prev
          flamegraph_row(f, x - row_width, y, row_width, row_prev)
        end

        row_prev = nil
        x += weight
        next
      end

      if row_prev.nil?        # start new row with this cell
        row_width = weight
        row_prev = cell
        x += weight

      elsif row_prev == cell  # grow current row along x-axis
        row_width += weight
        x += weight

      else                    # end current row and start new row
        flamegraph_row(f, x - row_width, y, row_width, row_prev)
        x += weight
        row_prev = cell
        row_width = weight
      end

      row_prev = cell
    end

    if row_prev
      next if skip_common && row_width == max_x

      flamegraph_row(f, x - row_width, y, row_width, row_prev)
    end
  end
  f.puts '])'
end
```

    
  

    
      
  
### 
  
    #**print_graphviz**(options = {}, f = STDOUT)  ⇒ Object 
  

  

  

  
    
      

```

418
419
420
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
463
464
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
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 418

def print_graphviz(options = {}, f = STDOUT)
  if filter = options[:filter]
    mark_stack = []
    list = frames(true)
    list.each{ |addr, frame| mark_stack << addr if frame[:name] =~ filter }
    while addr = mark_stack.pop
      frame = list[addr]
      unless frame[:marked]
        mark_stack += frame[:edges].map{ |addr, weight| addr if list[addr][:total_samples] <= weight*1.2 }.compact if frame[:edges]
        frame[:marked] = true
      end
    end
    list = list.select{ |addr, frame| frame[:marked] }
    list.each{ |addr, frame| frame[:edges] && frame[:edges].delete_if{ |k,v| list[k].nil? } }
    list
  else
    list = frames(true)
  end

  limit = options[:limit]
  fraction = options[:node_fraction]

  included_nodes = {}
  node_minimum = fraction ? (fraction * overall_samples).ceil : 0

  f.puts "digraph profile {"
  f.puts "Legend [shape=box,fontsize=24,shape=plaintext,label=\""
  f.print "Total samples: #{overall_samples}\\l"
  f.print "Showing top #{limit} nodes\\l" if limit
  f.print "Dropped nodes with < #{node_minimum} samples\\l" if fraction
  f.puts "\"];"

  list.each_with_index do |(frame, info), index|
    call, total = info.values_at(:samples, :total_samples)
    break if total < node_minimum || (limit && index >= limit)

    sample = ''.dup
    sample << "#{call} (%2.1f%%)\\rof " % (call*100.0/overall_samples) if call < total
    sample << "#{total} (%2.1f%%)\\r" % (total*100.0/overall_samples)
    fontsize = (1.0 * call / max_samples) * 28 + 10
    size = (1.0 * total / overall_samples) * 2.0 + 0.5

    f.puts "  \"#{frame}\" [size=#{size}] [fontsize=#{fontsize}] [penwidth=\"#{size}\"] [shape=box] [label=\"#{info[:name]}\\n#{sample}\"];"
    included_nodes[frame] = true
  end

  list.each do |frame, info|
    next unless included_nodes[frame]

    if edges = info[:edges]
      edges.each do |edge, weight|
        next unless included_nodes[edge]

        size = (1.0 * weight / overall_samples) * 2.0 + 0.5
        f.puts "  \"#{frame}\" -> \"#{edge}\" [label=\"#{weight}\"] [weight=\"#{weight}\"] [penwidth=\"#{size}\"];"
      end
    end
  end
  f.puts "}"
end
```

    
  

    
      
  
### 
  
    #**print_json**(f = STDOUT)  ⇒ Object 
  

  

  

  
    
      

```

111
112
113
114
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 111

def print_json(f=STDOUT)
  require "json"
  f.puts JSON.generate(@data, max_nesting: false)
end
```

    
  

    
      
  
### 
  
    #**print_method**(name, f = STDOUT)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 530

def print_method(name, f = STDOUT)
  name = /#{name}/ unless Regexp === name
  frames.each do |frame, info|
    next unless info[:name] =~ name
    file, line = info.values_at(:file, :line)
    line ||= 1

    lines = info[:lines]
    maxline = lines ? lines.keys.max : line + 5
    f.printf "%s (%s:%d)\n", info[:name], file, line
    f.printf "  samples: % 5d self (%2.1f%%)  /  % 5d total (%2.1f%%)\n", info[:samples], 100.0*info[:samples]/overall_samples, info[:total_samples], 100.0*info[:total_samples]/overall_samples

    if (callers = callers_for(frame)).any?
      f.puts "  callers:"
      callers = callers.sort_by(&:last).reverse
      callers.each do |name, weight|
        f.printf "   % 5d  (% 8s)  %s\n", weight, "%3.1f%%" % (100.0*weight/info[:total_samples]), name
      end
    end

    if callees = info[:edges]
      f.printf "  callees (%d total):\n", info[:total_samples]-info[:samples]
      callees = callees.map{ |k, weight| [data[:frames][k][:name], weight] }.sort_by{ |k,v| -v }
      callees.each do |name, weight|
        f.printf "   % 5d  (% 8s)  %s\n", weight, "%3.1f%%" % (100.0*weight/(info[:total_samples]-info[:samples])), name
      end
    end

    f.puts "  code:"
    source_display(f, file, lines, line-1..maxline)
  end
end
```

    
  

    
      
  
### 
  
    #**print_stackcollapse**  ⇒ Object 
  

  

  

  
    
      

```

116
117
118
119
120
121
122
123
124
125
126
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 116

def print_stackcollapse
  raise "profile does not include raw samples (add `raw: true` to collecting StackProf.run)" unless raw = data[:raw]

  while len = raw.shift
    frames = raw.slice!(0, len)
    weight = raw.shift

    print frames.map{ |a| data[:frames][a][:name] }.join(';')
    puts " #{weight}"
  end
end
```

    
  

    
      
  
### 
  
    #**print_text**(sort_by_total = false, limit = nil, select_files = nil, reject_files = nil, select_names = nil, reject_names = nil, f = STDOUT)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 480

def print_text(sort_by_total=false, limit=nil, select_files= nil, reject_files=nil, select_names=nil, reject_names=nil, f = STDOUT)
  f.puts "=================================="
  f.printf "  Mode: #{modeline}\n"
  f.printf "  Samples: #{@data[:samples]} (%.2f%% miss rate)\n", 100.0*@data[:missed_samples]/(@data[:missed_samples]+@data[:samples])
  f.printf "  GC: #{@data[:gc_samples]} (%.2f%%)\n", 100.0*@data[:gc_samples]/@data[:samples]
  f.puts "=================================="
  f.printf "% 10s    (pct)  % 10s    (pct)     FRAME\n" % ["TOTAL", "SAMPLES"]
  list = frames(sort_by_total)
  list.select!{|_, info| select_files.any?{|path| info[:file].start_with?(path)}} if select_files
  list.select!{|_, info| select_names.any?{|reg| info[:name] =~ reg}} if select_names
  list.reject!{|_, info| reject_files.any?{|path| info[:file].start_with?(path)}} if reject_files
  list.reject!{|_, info| reject_names.any?{|reg| info[:name] =~ reg}} if reject_names
  list = list.first(limit) if limit
  list.each do |frame, info|
    call, total = info.values_at(:samples, :total_samples)
    f.printf "% 10d % 8s  % 10d % 8s     %s\n", total, "(%2.1f%%)" % (total*100.0/overall_samples), call, "(%2.1f%%)" % (call*100.0/overall_samples), info[:name]
  end
end
```

    
  

    
      
  
### 
  
    #**print_timeline_flamegraph**(f = STDOUT, skip_common = true)  ⇒ Object 
  

  

  

  
    
      

```

128
129
130
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 128

def print_timeline_flamegraph(f=STDOUT, skip_common=true)
  print_flamegraph(f, skip_common, false)
end
```

    
  

    
      
  
### 
  
    #**version**  ⇒ Object 
  

  

  

  
    
      

```

68
69
70
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 68

def version
  @data[:version]
end
```

    
  

    
      
  
### 
  
    #**walk_method**(name)  ⇒ Object 
  

  

  

  
    

Walk up and down the stack from a given starting point (name).  Loops until `:exit` is selected

  

  

  
    
      

```

565
566
567
568
569
570
571
572
573
574
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
589
590
591
592
593
594
595
596
597
598
599
600
601
602
```

    
    
      

```
# File 'lib/stackprof/report.rb', line 565

def walk_method(name)
  method_choice  = /#{Regexp.escape name}/
  invalid_choice = false

  # Continue walking up and down the stack until the users selects "exit"
  while method_choice != :exit
    print_method method_choice unless invalid_choice
    STDOUT.puts "\n\n"

    # Determine callers and callees for the current frame
    new_frames  = frames.select  {|_, info| info[:name] =~ method_choice }
    new_choices = new_frames.map {|frame, info| [
      callers_for(frame).sort_by(&:last).reverse.map(&:first),
      (info[:edges] || []).map{ |k, w| [data[:frames][k][:name], w] }.sort_by{ |k,v| -v }.map(&:first)
    ]}.flatten + [:exit]

    # Print callers and callees for selection
    STDOUT.puts "Select next method:"
    new_choices.each_with_index do |method, index|
      STDOUT.printf "%2d)  %s\n", index + 1, method.to_s
    end

    # Pick selection
    STDOUT.printf "> "
    selection = STDIN.gets.chomp.to_i - 1
    STDOUT.puts "\n\n\n"

    # Determine if it was a valid choice
    # (if not, don't re-run .print_method)
    if new_choice = new_choices[selection]
      invalid_choice = false
      method_choice = new_choice == :exit ? :exit : %r/^#{Regexp.escape new_choice}$/
    else
      invalid_choice = true
      STDOUT.puts "Invalid choice.  Please select again..."
    end
  end
end
```