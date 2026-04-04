# Source: https://code.kx.com/q/learn/tour/tables/

Title: Tables in kdb+ | A whirlwind tour of kdb+ and q | Documentation for kdb+ and the q programming language

URL Source: https://code.kx.com/q/learn/tour/tables/

Published Time: Tue, 03 Mar 2026 17:25:01 GMT

Markdown Content:
Tables in kdb+ | A whirlwind tour of kdb+ and q | Documentation for kdb+ and the q programming language - kdb+ and q documentation
===============

- [x] - [x]

[Skip to content](https://code.kx.com/q/learn/tour/tables/#tables)

[![Image 1: logo](https://code.kx.com/q/local/img/kx.svg)](https://code.kx.com/ "code.kx.com")

 kdb+ and q documentation

 Tables in kdb+ | A whirlwind tour of kdb+ and q | Documentation for kdb+ and the q programming language

 Initializing search

Ask a question

- [Home](https://code.kx.com/home)
- [kdb+ and q](https://code.kx.com/q/)
- [kdb Insights SDK](https://code.kx.com/insights)
- [kdb Insights Enterprise](https://code.kx.com/insights/enterprise)
- [KDB.AI](https://code.kx.com/kdbai)
- [PyKX](https://code.kx.com/pykx)
- [APIs](https://code.kx.com/insights/api)
- [Help](https://code.kx.com/home/support.html)

[![Image 2: logo](https://code.kx.com/q/local/img/kx.svg)](https://code.kx.com/q/ "kdb+ and q documentation") kdb+ and q documentation  
- [Home](https://code.kx.com/home)
- - [x]  kdb+ and q   kdb+ and q  
  - [About](https://code.kx.com/q/)
  - - [x]  Getting Started   Getting Started  
    - [Install](https://code.kx.com/q/learn/install/)
    - [Licenses](https://code.kx.com/q/learn/licensing/)

  - - [x]  Learn   Learn  
    - [Overview](https://code.kx.com/q/learn/)
    - - [x]  Mountain tour   Mountain tour  
      - [Overview](https://code.kx.com/q/learn/tour/overview/)
      - [Begin here](https://code.kx.com/q/learn/tour/)
      - [The q session](https://code.kx.com/q/learn/tour/session/)
      - - [x]  Tables  [Tables](https://code.kx.com/q/learn/tour/tables/) On this page  
        - [Construct](https://code.kx.com/q/learn/tour/tables/#construct)
        - [Work](https://code.kx.com/q/learn/tour/tables/#work)
        - [Keys](https://code.kx.com/q/learn/tour/tables/#keys)
        - [Persist](https://code.kx.com/q/learn/tour/tables/#persist)
        - [Go large](https://code.kx.com/q/learn/tour/tables/#go-large)

      - [CSVs](https://code.kx.com/q/learn/tour/csvs/)
      - [Datatypes](https://code.kx.com/q/learn/tour/datatypes/)
      - [Scripts](https://code.kx.com/q/learn/tour/scripts/)
      - [IDE](https://code.kx.com/q/learn/tour/ide/)

    - [Q for quants](https://code.kx.com/q/learn/brief-introduction/)
    - [Q by Examples](https://code.kx.com/q/learn/q-by-examples/)
    - [Q for All (video)](https://code.kx.com/q/learn/q-for-all/)
    - - [x]  Examples from Python   Examples from Python  
      - [Basic](https://code.kx.com/q/learn/python/examples/)
      - [Array](https://code.kx.com/q/learn/python/examples/array/)
      - [List](https://code.kx.com/q/learn/python/examples/list/)
      - [Strings](https://code.kx.com/q/learn/python/examples/string/)
      - [Dictionaries](https://code.kx.com/q/learn/python/examples/dict/)

    - [Q for Mortals 3](https://code.kx.com/q4m3/)
    - - [x]  Q by Puzzles   Q by Puzzles  
      - [About](https://code.kx.com/q/learn/pb/)
      - [12 Days of Xmas](https://code.kx.com/q/learn/pb/xmas-days/)
      - [ABC problem](https://code.kx.com/q/learn/pb/abc-problem/)
      - [Abundant odds](https://code.kx.com/q/learn/pb/abundant-odds/)
      - [Four is magic](https://code.kx.com/q/learn/pb/four-magic/)
      - [Name Game](https://code.kx.com/q/learn/pb/name-game/)
      - [Summarize and Say](https://code.kx.com/q/learn/pb/sum-say/)
      - [Word wheel](https://code.kx.com/q/learn/pb/word-wheel/)

    - - [x]  Reading room   Reading room  
      - [Information desk](https://code.kx.com/q/learn/reading/)
      - [Boggle](https://code.kx.com/q/learn/reading/boggle/)
      - [Cats cradle](https://code.kx.com/q/learn/reading/strings/)
      - [Fizz buzz](https://code.kx.com/q/learn/reading/fizzbuzz/)
      - [Klondike](https://code.kx.com/q/learn/reading/klondike/)
      - [Phrasebook](https://code.kx.com/phrases/)
      - [Scrabble](https://code.kx.com/q/learn/reading/scrabble/)

    - - [x]  Application examples   Application examples  
      - [Astronomy](https://code.kx.com/q/wp/astronomy/)
      - [Detecting card counters](https://code.kx.com/q/wp/card-counters/)
      - [Corporate actions](https://code.kx.com/q/wp/corporate-actions/)
      - [Disaster management](https://code.kx.com/q/wp/disaster-management/)
      - [Exoplanets](https://code.kx.com/q/wp/exoplanets/)
      - [Market depth](https://code.kx.com/q/wp/market-depth/)
      - [Market fragmentation](https://code.kx.com/q/wp/market-fragmentation/)
      - [Option pricing](https://code.kx.com/q/wp/option-pricing/)
      - [Predicting floods](https://code.kx.com/q/wp/disaster-floods/)
      - [Signal processing](https://code.kx.com/q/wp/signal-processing/)
      - [Space weather](https://code.kx.com/q/wp/space-weather/)
      - [Trading surveillance](https://code.kx.com/q/wp/surveillance/)
      - [Transaction-cost analysis](https://code.kx.com/q/wp/transaction-cost/)
      - [Trend indicators](https://code.kx.com/q/wp/trend-indicators/)

    - - [x]  Advanced q   Advanced q  
      - [Remarks on Style](https://github.com/qbists/style)
      - [Shifts & scans](https://code.kx.com/q/learn/shifts-scans/)
      - [Technical articles](https://code.kx.com/q/learn/blogs/)
      - [Views](https://code.kx.com/q/learn/views/)
      - [Origins](https://code.kx.com/q/learn/archive/)
      - [Terminology](https://code.kx.com/q/about/terminology/)

    - - [x]  Starting kdb+   Starting kdb+  
      - [Overview](https://code.kx.com/q/learn/startingkdb/)
      - [The q language](https://code.kx.com/q/learn/startingkdb/language/)
      - [IPC](https://code.kx.com/q/learn/startingkdb/ipc/)
      - [Tables](https://code.kx.com/q/learn/startingkdb/tables/)
      - [Historical database](https://code.kx.com/q/learn/startingkdb/hdb/)
      - [Realtime database](https://code.kx.com/q/learn/startingkdb/tick/)

  - - [x]  Language   Language  
    - [Reference card](https://code.kx.com/q/ref/)
    - [By topic](https://code.kx.com/q/basics/by-topic/)
    - - [x]  Iteration   Iteration  
      - [Overview](https://code.kx.com/q/basics/iteration/)
      - [Implicit iteration](https://code.kx.com/q/basics/implicit-iteration/)
      - [Iterators](https://code.kx.com/q/ref/iterators/)
      - [Maps](https://code.kx.com/q/ref/maps/)
      - [Accumulators](https://code.kx.com/q/ref/accumulators/)
      - [Guide to iterators](https://code.kx.com/q/wp/iterators/)

    - - [x]  Keywords   Keywords  
      - [abs](https://code.kx.com/q/ref/abs/)
      - [aj, aj0, ajf, ajf0](https://code.kx.com/q/ref/aj/)
      - [all, any](https://code.kx.com/q/ref/all-any/)
      - [and](https://code.kx.com/q/ref/and/)
      - [asc, iasc, xasc](https://code.kx.com/q/ref/asc/)
      - [asof](https://code.kx.com/q/ref/asof/)
      - [attr](https://code.kx.com/q/ref/attr/)
      - [avg, avgs, mavg, wavg](https://code.kx.com/q/ref/avg/)
      - [bin, binr](https://code.kx.com/q/ref/bin/)
      - [ceiling](https://code.kx.com/q/ref/ceiling/)
      - [count, mcount](https://code.kx.com/q/ref/count/)
      - [cols, xcol, xcols](https://code.kx.com/q/ref/cols/)
      - [cor](https://code.kx.com/q/ref/cor/)
      - [cos, acos](https://code.kx.com/q/ref/cos/)
      - [cov, scov](https://code.kx.com/q/ref/cov/)
      - [cross](https://code.kx.com/q/ref/cross/)
      - [csv](https://code.kx.com/q/ref/csv/)
      - [cut](https://code.kx.com/q/ref/cut/)
      - [delete](https://code.kx.com/q/ref/delete/)
      - [deltas](https://code.kx.com/q/ref/deltas/)
      - [desc, idesc, xdesc](https://code.kx.com/q/ref/desc/)
      - [dev, mdev, sdev](https://code.kx.com/q/ref/dev/)
      - [differ](https://code.kx.com/q/ref/differ/)
      - [distinct](https://code.kx.com/q/ref/distinct/)
      - [div](https://code.kx.com/q/ref/div/)
      - [dsave](https://code.kx.com/q/ref/dsave/)
      - [each, peach](https://code.kx.com/q/ref/each/)
      - [ej](https://code.kx.com/q/ref/ej/)
      - [ema](https://code.kx.com/q/ref/ema/)
      - [enlist](https://code.kx.com/q/ref/enlist/)
      - [eval, reval](https://code.kx.com/q/ref/eval/)
      - [except](https://code.kx.com/q/ref/except/)
      - [exec](https://code.kx.com/q/ref/exec/)
      - [exit](https://code.kx.com/q/ref/exit/)
      - [exp, xexp](https://code.kx.com/q/ref/exp/)
      - [fby](https://code.kx.com/q/ref/fby/)
      - [fills](https://code.kx.com/q/ref/fill/)
      - [first, last](https://code.kx.com/q/ref/first/)
      - [fkeys](https://code.kx.com/q/ref/fkeys/)
      - [flip](https://code.kx.com/q/ref/flip/)
      - [floor](https://code.kx.com/q/ref/floor/)
      - [get, set](https://code.kx.com/q/ref/get/)
      - [getenv, setenv](https://code.kx.com/q/ref/getenv/)
      - [group](https://code.kx.com/q/ref/group/)
      - [gtime, ltime](https://code.kx.com/q/ref/gtime/)
      - [hcount](https://code.kx.com/q/ref/hcount/)
      - [hdel](https://code.kx.com/q/ref/hdel/)
      - [hopen, hclose](https://code.kx.com/q/ref/hopen/)
      - [hsym](https://code.kx.com/q/ref/hsym/)
      - [ij, ijf](https://code.kx.com/q/ref/ij/)
      - [in](https://code.kx.com/q/ref/in/)
      - [insert](https://code.kx.com/q/ref/insert/)
      - [inter](https://code.kx.com/q/ref/inter/)
      - [inv](https://code.kx.com/q/ref/inv/)
      - [key](https://code.kx.com/q/ref/key/)
      - [keys, xkey](https://code.kx.com/q/ref/keys/)
      - [like](https://code.kx.com/q/ref/like/)
      - [lj, ljf](https://code.kx.com/q/ref/lj/)
      - [load, rload](https://code.kx.com/q/ref/load/)
      - [log, xlog](https://code.kx.com/q/ref/log/)
      - [lower, upper](https://code.kx.com/q/ref/lower/)
      - [lsq](https://code.kx.com/q/ref/lsq/)
      - [max, maxs, mmax](https://code.kx.com/q/ref/max/)
      - [md5](https://code.kx.com/q/ref/md5/)
      - [med](https://code.kx.com/q/ref/med/)
      - [meta](https://code.kx.com/q/ref/meta/)
      - [min, mins, mmin](https://code.kx.com/q/ref/min/)
      - [mmu](https://code.kx.com/q/ref/mmu/)
      - [mod](https://code.kx.com/q/ref/mod/)
      - [neg](https://code.kx.com/q/ref/neg/)
      - [next, prev, xprev](https://code.kx.com/q/ref/next/)
      - [not](https://code.kx.com/q/ref/not/)
      - [null](https://code.kx.com/q/ref/null/)
      - [or](https://code.kx.com/q/ref/or/)
      - [over, scan](https://code.kx.com/q/ref/over/)
      - [parse](https://code.kx.com/q/ref/parse/)
      - [pj](https://code.kx.com/q/ref/pj/)
      - [prd, prds](https://code.kx.com/q/ref/prd/)
      - [prior](https://code.kx.com/q/ref/prior/)
      - [rand](https://code.kx.com/q/ref/rand/)
      - [rank](https://code.kx.com/q/ref/rank/)
      - [ratios](https://code.kx.com/q/ref/ratios/)
      - [raze](https://code.kx.com/q/ref/raze/)
      - [read0](https://code.kx.com/q/ref/read0/)
      - [read1](https://code.kx.com/q/ref/read1/)
      - [reciprocal](https://code.kx.com/q/ref/reciprocal/)
      - [reverse](https://code.kx.com/q/ref/reverse/)
      - [rotate](https://code.kx.com/q/ref/rotate/)
      - [save, rsave](https://code.kx.com/q/ref/save/)
      - [select](https://code.kx.com/q/ref/select/)
      - [show](https://code.kx.com/q/ref/show/)
      - [signum](https://code.kx.com/q/ref/signum/)
      - [sin, asin](https://code.kx.com/q/ref/sin/)
      - [sqrt](https://code.kx.com/q/ref/sqrt/)
      - [ss, ssr](https://code.kx.com/q/ref/ss/)
      - [string](https://code.kx.com/q/ref/string/)
      - [sublist](https://code.kx.com/q/ref/sublist/)
      - [sum, sums, msum, wsum](https://code.kx.com/q/ref/sum/)
      - [sv](https://code.kx.com/q/ref/sv/)
      - [system](https://code.kx.com/q/ref/system/)
      - [tables](https://code.kx.com/q/ref/tables/)
      - [tan, atan](https://code.kx.com/q/ref/tan/)
      - [til](https://code.kx.com/q/ref/til/)
      - [trim, ltrim, rtrim](https://code.kx.com/q/ref/trim/)
      - [type](https://code.kx.com/q/ref/type/)
      - [uj, ujf](https://code.kx.com/q/ref/uj/)
      - [union](https://code.kx.com/q/ref/union/)
      - [ungroup](https://code.kx.com/q/ref/ungroup/)
      - [update](https://code.kx.com/q/ref/update/)
      - [upsert](https://code.kx.com/q/ref/upsert/)
      - [value](https://code.kx.com/q/ref/value/)
      - [var, svar](https://code.kx.com/q/ref/var/)
      - [view, views](https://code.kx.com/q/ref/view/)
      - [vs](https://code.kx.com/q/ref/vs/)
      - [where](https://code.kx.com/q/ref/where/)
      - [within](https://code.kx.com/q/ref/within/)
      - [wj, wj1](https://code.kx.com/q/ref/wj/)
      - [xbar](https://code.kx.com/q/ref/xbar/)
      - [xgroup](https://code.kx.com/q/ref/xgroup/)
      - [xrank](https://code.kx.com/q/ref/xrank/)

    - [Overloaded glyphs](https://code.kx.com/q/ref/overloads/)
    - - [x]  Operators   Operators  
      - [Add](https://code.kx.com/q/ref/add/)
      - [Amend](https://code.kx.com/q/ref/amend/)
      - [Apply, Index, Trap](https://code.kx.com/q/ref/apply/)
      - [Assign](https://code.kx.com/q/ref/assign/)
      - [Cast](https://code.kx.com/q/ref/cast/)
      - [Coalesce](https://code.kx.com/q/ref/coalesce/)
      - [Compose](https://code.kx.com/q/ref/compose/)
      - [Cut](https://code.kx.com/q/ref/cut/)
      - [Deal, Roll, Permute](https://code.kx.com/q/ref/deal/)
      - [Delete](https://code.kx.com/q/ref/delete/)
      - [Display](https://code.kx.com/q/ref/display/)
      - [Dict](https://code.kx.com/q/ref/dict/)
      - [Divide](https://code.kx.com/q/ref/divide/)
      - [Dynamic Load](https://code.kx.com/q/ref/dynamic-load/)
      - [Drop](https://code.kx.com/q/ref/drop/)
      - [Enkey, Unkey](https://code.kx.com/q/ref/enkey/)
      - [Enumerate](https://code.kx.com/q/ref/enumerate/)
      - [Enumeration](https://code.kx.com/q/ref/enumeration/)
      - [Enum Extend](https://code.kx.com/q/ref/enum-extend/)
      - [Equal](https://code.kx.com/q/ref/equal/)
      - [Exec](https://code.kx.com/q/ref/exec/)
      - [File Binary](https://code.kx.com/q/ref/file-binary/)
      - [File Text](https://code.kx.com/q/ref/file-text/)
      - [Fill](https://code.kx.com/q/ref/fill/)
      - [Find](https://code.kx.com/q/ref/find/)
      - [Flip Splayed](https://code.kx.com/q/ref/flip-splayed/)
      - [Greater](https://code.kx.com/q/ref/greater/)
      - [Greater Than](https://code.kx.com/q/ref/greater-than/)
      - [Identity, Null](https://code.kx.com/q/ref/identity/)
      - [Join](https://code.kx.com/q/ref/join/)
      - [Less Than](https://code.kx.com/q/ref/less-than/)
      - [Lesser](https://code.kx.com/q/ref/lesser/)
      - [Match](https://code.kx.com/q/ref/match/)
      - [Matrix Multiply](https://code.kx.com/q/ref/mmu/)
      - [Multiply](https://code.kx.com/q/ref/multiply/)
      - [Not Equal](https://code.kx.com/q/ref/not-equal/)
      - [Pad](https://code.kx.com/q/ref/pad/)
      - [Select](https://code.kx.com/q/ref/select/)
      - [Set Attribute](https://code.kx.com/q/ref/set-attribute/)
      - [Simple Exec](https://code.kx.com/q/ref/simple-exec/)
      - [Signal](https://code.kx.com/q/ref/signal/)
      - [Subtract](https://code.kx.com/q/ref/subtract/)
      - [Take](https://code.kx.com/q/ref/take/)
      - [Tok](https://code.kx.com/q/ref/tok/)
      - [Update](https://code.kx.com/q/ref/update/)
      - [Vector Conditional](https://code.kx.com/q/ref/vector-conditional/)

    - - [x]  Control constructs   Control constructs  
      - [Cond](https://code.kx.com/q/ref/cond/)
      - [do](https://code.kx.com/q/ref/do/)
      - [if](https://code.kx.com/q/ref/if/)
      - [while](https://code.kx.com/q/ref/while/)

    - - [x]  Namespaces   Namespaces  
      - [.h (markup)](https://code.kx.com/q/ref/doth/)
      - [.j (JSON)](https://code.kx.com/q/ref/dotj/)
      - [.m (memory backed files)](https://code.kx.com/q/ref/dotm/)
      - [.Q (utils)](https://code.kx.com/q/ref/dotq/)
      - [.z (env, callbacks)](https://code.kx.com/q/ref/dotz/)

    - [Application](https://code.kx.com/q/basics/application/)
    - [Atomic functions](https://code.kx.com/q/basics/atomic/)
    - [Comparison](https://code.kx.com/q/basics/comparison/)
    - [Conformability](https://code.kx.com/q/basics/conformable/)
    - [Connection handles](https://code.kx.com/q/basics/handles/)
    - [Command-line options](https://code.kx.com/q/basics/cmdline/)
    - [Datatypes](https://code.kx.com/q/basics/datatypes/)
    - [Dictionaries](https://code.kx.com/q/basics/dictsandtables/)
    - [Enumerations](https://code.kx.com/q/basics/enumerations/)
    - [Evaluation control](https://code.kx.com/q/basics/control/)
    - [Exposed infrastructure](https://code.kx.com/q/basics/exposed-infrastructure/)
    - [File system](https://code.kx.com/q/basics/files/)
    - [Function notation](https://code.kx.com/q/basics/function-notation/)
    - [Glossary](https://code.kx.com/q/basics/glossary/)
    - [Internal functions](https://code.kx.com/q/basics/internal/)
    - [Joins](https://code.kx.com/q/basics/joins/)
    - [Mathematics](https://code.kx.com/q/basics/math/)
    - [Metadata](https://code.kx.com/q/basics/metadata/)
    - [Namespaces](https://code.kx.com/q/basics/namespaces/)
    - [Pattern matching](https://code.kx.com/q/basics/pattern/)
    - [Parse trees](https://code.kx.com/q/basics/parsetrees/)
    - - [x]  qSQL   qSQL  
      - [qSQL queries](https://code.kx.com/q/basics/qsql/)
      - [Functional qSQL](https://code.kx.com/q/basics/funsql/)

    - [Regular Expressions](https://code.kx.com/q/basics/regex/)
    - [Syntax](https://code.kx.com/q/basics/syntax/)
    - [System commands](https://code.kx.com/q/basics/syscmds/)
    - [Tables](https://code.kx.com/q/kb/faq/)
    - [Variadic syntax](https://code.kx.com/q/basics/variadic/)

  - - [x]  Database   Database  
    - [Tables in the filesystem](https://code.kx.com/q/database/)
    - - [x]  Populating tables   Populating tables  
      - [Loading from large files](https://code.kx.com/q/kb/loading-from-large-files/)
      - [Foreign keys](https://code.kx.com/q/wp/foreign-keys/)
      - [Linking columns](https://code.kx.com/q/kb/linking-columns/)
      - [Data loaders](https://code.kx.com/q/wp/data-loaders/)
      - [From MDB via ODBC](https://code.kx.com/q/database/mdb-odbc/)

    - - [x]  Persisting tables   Persisting tables  
      - [Serializing an object](https://code.kx.com/q/database/object/)
      - [Splayed tables](https://code.kx.com/q/kb/splayed-tables/)
      - [Partitioned tables](https://code.kx.com/q/kb/partition/)
      - [Segmented databases](https://code.kx.com/q/database/segment/)
      - [Multiple partitions](https://code.kx.com/q/wp/multi-partitioned-dbs/)

    - - [x]  Maintenance   Maintenance  
      - [Data management](https://code.kx.com/q/wp/data-management/)
      - [Data-At-Rest Encryption](https://code.kx.com/q/kb/dare/)
      - - [x]  Compression   Compression  
        - [File compression](https://code.kx.com/q/kb/file-compression/)
        - [Compression examples](https://code.kx.com/q/wp/compress/)
        - [FSI case study](https://code.kx.com/q/kb/compression/fsicasestudy/)

      - [Permissions](https://code.kx.com/q/wp/permissions/)
      - [Query optimization](https://code.kx.com/q/wp/columnar-database/)
      - [Query scaling](https://code.kx.com/q/wp/query-scaling/)
      - [Time-series simplification](https://code.kx.com/q/wp/ts-shrink/)
      - [Compacting HDB sym](https://code.kx.com/q/kb/compacting-hdb-sym/)
      - [Working with sym files](https://code.kx.com/q/wp/symfiles/)

  - - [x]  Developing   Developing  
    - - [x]  IPC   IPC  
      - [Overview](https://code.kx.com/q/basics/ipc/)
      - [Listening port](https://code.kx.com/q/basics/listening-port/)
      - [Deferred response](https://code.kx.com/q/kb/deferred-response/)
      - [Async callbacks](https://code.kx.com/q/kb/callbacks/)
      - [Named pipes](https://code.kx.com/q/kb/named-pipes/)
      - [Serialization examples](https://code.kx.com/q/kb/serialization/)
      - [Socket sharding](https://code.kx.com/q/wp/socket-sharding/)
      - [SSL/TLS](https://code.kx.com/q/kb/ssl/)
      - [HTTP](https://code.kx.com/q/kb/http/)
      - [WebSockets](https://code.kx.com/q/kb/websockets/)

    - - [x]  Tools   Tools  
      - [Code profiler](https://code.kx.com/q/kb/profiler/)
      - [Debugging](https://code.kx.com/q/basics/debug/)
      - [Errors](https://code.kx.com/q/basics/errors/)
      - [man.q](https://code.kx.com/q/about/man/)
      - [Unit tests](https://code.kx.com/q/kb/unit-tests/)
      - [Monitor & control execution](https://code.kx.com/q/kb/using-dotz/)

    - - [x]  Coding   Coding  
      - [Geospatial indexing](https://code.kx.com/q/kb/geospatial/)
      - [Linear programming](https://code.kx.com/q/kb/lp/)
      - [Multithreaded primitives](https://code.kx.com/q/kb/mt-primitives/)
      - [Pivoting tables](https://code.kx.com/q/kb/pivoting-tables/)
      - [Precision](https://code.kx.com/q/basics/precision/)
      - [Programming examples](https://code.kx.com/q/kb/programming-examples/)
      - [Programming idioms](https://code.kx.com/q/kb/programming-idioms/)
      - [Temporal data](https://code.kx.com/q/kb/temporal-data/)
      - [Timezones](https://code.kx.com/q/kb/timezones/)
      - [Unicode](https://code.kx.com/q/kb/unicode/)

    - - [x]  DevOps   DevOps  
      - [CPU affinity](https://code.kx.com/q/kb/cpu-affinity/)
      - [Daemon](https://code.kx.com/q/kb/daemon/)
      - [Firewalling](https://code.kx.com/q/kb/firewalling/)
      - [inetd, xinetd](https://code.kx.com/q/kb/inetd/)
      - [Linux production notes](https://code.kx.com/q/kb/linux-production/)
      - [File system comparison](https://code.kx.com/q/kb/filesystemTestByNano/)
      - [Log Files](https://code.kx.com/q/kb/logging/)
      - [Multi-threading](https://code.kx.com/q/wp/multi-thread/)
      - [Multiple versions](https://code.kx.com/q/kb/versions/)
      - [Parallel processing](https://code.kx.com/q/basics/peach/)
      - [Performance tips](https://code.kx.com/q/kb/performance-tips/)
      - [Shebang script](https://code.kx.com/q/develop/shebang/)
      - [Surveillance latency](https://code.kx.com/q/wp/surveillance-latency/)
      - [Windows service](https://code.kx.com/q/kb/windows-service/)
      - - [x]  Optane Memory   Optane Memory  
        - [Optane Memory and kdb+](https://code.kx.com/q/kb/optane/)
        - [Performance tests](https://code.kx.com/q/architecture/optane-tests/)

    - - [x]  Release notes   Release notes  
      - [History](https://code.kx.com/q/releases/)
      - [Changes in 4.1](https://code.kx.com/q/releases/ChangesIn4.1/)
      - [Changes in 4.0](https://code.kx.com/q/releases/ChangesIn4.0/)
      - [Changes in 3.6](https://code.kx.com/q/releases/ChangesIn3.6/)
      - [Changes in 3.5](https://code.kx.com/q/releases/ChangesIn3.5/)
      - [Changes in 3.4](https://code.kx.com/q/releases/ChangesIn3.4/)
      - [Changes in 3.3](https://code.kx.com/q/releases/ChangesIn3.3/)
      - [Changes in 3.2](https://code.kx.com/q/releases/ChangesIn3.2/)
      - [Changes in 3.1](https://code.kx.com/q/releases/ChangesIn3.1/)
      - [Changes in 3.0](https://code.kx.com/q/releases/ChangesIn3.0/)
      - [Changes in 2.8](https://code.kx.com/q/releases/ChangesIn2.8/)
      - [Changes in 2.7](https://code.kx.com/q/releases/ChangesIn2.7/)
      - [Changes in 2.6](https://code.kx.com/q/releases/ChangesIn2.6/)
      - [Changes in 2.5](https://code.kx.com/q/releases/ChangesIn2.5/)
      - [Changes in 2.4](https://code.kx.com/q/releases/ChangesIn2.4/)
      - [Withdrawn](https://code.kx.com/q/releases/withdrawn/)

    - [Developer tools](https://code.kx.com/q/devtools/)
    - [FAQ](https://code.kx.com/q/kb/faq-listbox/)

  - - [x]  Streaming   Streaming  
    - - [x]  General architecture   General architecture  
      - [Overview](https://code.kx.com/q/architecture/)
      - - [x]  kdb+tick   kdb+tick  
        - [Tickerplant (tick.q)](https://code.kx.com/q/architecture/tickq/)
        - [Tickerplant pub/sub (u.q)](https://code.kx.com/q/architecture/uq/)
        - [RDB (r.q)](https://code.kx.com/q/architecture/rq/)

    - [Alternative architecture](https://code.kx.com/q/kb/kdb-tick/)
    - [TP Log (data recovery)](https://code.kx.com/q/wp/data-recovery/)
    - [RTEs (real-time engines)](https://code.kx.com/q/wp/rt-tick/)
    - [Gateway design](https://code.kx.com/q/wp/gateway-design/)
    - [Query routing](https://code.kx.com/q/wp/query-routing/)
    - [Load balancing](https://code.kx.com/q/kb/load-balancing/)
    - [Profiling](https://code.kx.com/q/wp/tick-profiling/)
    - [Disaster recovery](https://code.kx.com/q/wp/disaster-recovery/)
    - [Kubernetes](https://youtu.be/jqtkkCqBvr4)
    - [Order Book](https://code.kx.com/q/wp/order-book/)
    - [Alternative in-memory layouts](https://code.kx.com/q/kb/alternative-in-memory-layouts/)
    - [Corporate actions](https://code.kx.com/q/kb/corporate-actions/)
    - - [x]  Advanced   Advanced  
      - [Distributed systems](https://code.kx.com/q/wp/query-interface/)
      - [RDB intraday writedown](https://code.kx.com/q/wp/intraday-writedown/)

  - - [x]  Interfaces   Interfaces  
    - - [x]  Languages   Languages  
      - - [x]  C/C++   C/C++  
        - [Quick guide](https://code.kx.com/q/interfaces/c-client-for-q/)
        - [API reference](https://code.kx.com/q/interfaces/capiref/)
        - [C API for kdb+](https://code.kx.com/q/wp/capi/)
        - [Extending q with C/C++](https://code.kx.com/q/interfaces/using-c-functions/)
        - [Async callbacks (C client)](https://code.kx.com/q/kb/server-calling-client/)

      - [C#](https://code.kx.com/q/interfaces/csharp/)
      - [Foreign Function Interface (FFI)](https://code.kx.com/q/interfaces/ffi/)
      - [Java](https://code.kx.com/q/interfaces/java/)
      - [Python](https://code.kx.com/q/interfaces/python/)
      - [R](https://code.kx.com/q/interfaces/r/)
      - [Rust](https://code.kx.com/q/interfaces/rust/)
      - [Scala](https://code.kx.com/q/interfaces/scala-client-for-q/)

    - [KX libraries](https://code.kx.com/q/interfaces/)
    - [Bloomberg](https://code.kx.com/q/interfaces/q-client-for-bloomberg/)
    - [Excel](https://code.kx.com/q/interfaces/excel-client-for-q/)
    - [FIX messaging](https://code.kx.com/q/wp/fix-messaging/)
    - [GPUs](https://code.kx.com/q/interfaces/gpus/)
    - [Matlab](https://code.kx.com/q/interfaces/matlab-client-for-q/)
    - - [x]  ODBC   ODBC  
      - [ODBC client](https://code.kx.com/q/interfaces/q-client-for-odbc/)
      - [ODBC3 server](https://code.kx.com/q/interfaces/q-server-for-odbc3/)
      - [ODBC3 and Tableau](https://code.kx.com/q/wp/data-visualization/)

    - [Solace pub/sub](https://code.kx.com/q/wp/solace/)
    - [Open source](https://code.kx.com/q/github/)
    - [Machine learning](https://code.kx.com/q/ml/)

  - - [x]  Using kdb+ in the cloud   Using kdb+ in the cloud  
    - [About](https://code.kx.com/q/cloud/)
    - - [x]  Amazon Web Services   Amazon Web Services  
      - [Reference architecture](https://code.kx.com/q/cloud/aws/)
      - - [x]  Amazon EC2 & Storage Services   Amazon EC2 & Storage Services  
        - [Migrating a kdb+ HDB to Amazon EC2](https://code.kx.com/q/cloud/aws/migration/)
        - [Elastic Block Store (EBS)](https://code.kx.com/q/cloud/aws/app-a-ebs/)
        - [EFS (NFS)](https://code.kx.com/q/cloud/aws/app-b-efs-nfs/)
        - [Amazon Storage Gateway](https://code.kx.com/q/cloud/aws/app-c-asg/)
        - [FSx for Lustre](https://code.kx.com/q/cloud/aws/lustre/)

      - [AWS Lambda](https://code.kx.com/q/cloud/aws-lambda/)

    - - [x]  Microsoft Azure   Microsoft Azure  
      - [Reference architecture](https://code.kx.com/q/cloud/azure/architecture/)

    - - [x]  Google Cloud   Google Cloud  
      - [Reference architecture](https://code.kx.com/q/cloud/gcpm/architecture/)

    - - [x]  Auto Scaling   Auto Scaling  
      - [About](https://code.kx.com/q/cloud/autoscale/)
      - [Amazon Web Services](https://code.kx.com/q/cloud/autoscale/aws/)
      - [Realtime data cluster](https://code.kx.com/q/cloud/autoscale/rdc/)
      - [Costs and risks](https://code.kx.com/q/cloud/autoscale/cost-risk/)

    - - [x]  Other file systems   Other file systems  
      - [MapR-FS](https://code.kx.com/q/cloud/otherfs/mapr/)
      - [Goofys](https://code.kx.com/q/cloud/otherfs/goofys/)
      - [S3FS](https://code.kx.com/q/cloud/otherfs/s3fs/)
      - [S3QL](https://code.kx.com/q/cloud/otherfs/s3ql/)
      - [ObjectiveFS](https://code.kx.com/q/cloud/otherfs/objectivefs/)
      - [WekaIO Matrix](https://code.kx.com/q/cloud/otherfs/wekaio-matrix/)
      - [Quobyte](https://code.kx.com/q/cloud/otherfs/quobyte/)

  - [Academy](https://learninghub.kx.com/)
  - [Discussion Forum](https://learninghub.kx.com/forums/forum/kdb)
  - [White papers](https://code.kx.com/q/wp/)
  - [About this site](https://code.kx.com/q/about/thissite/)

- [kdb Insights SDK](https://code.kx.com/insights)
- [kdb Insights Enterprise](https://code.kx.com/insights/enterprise)
- [KDB.AI](https://code.kx.com/kdbai)
- [PyKX](https://code.kx.com/pykx)
- [APIs](https://code.kx.com/insights/api)
- [Help](https://code.kx.com/home/support.html)

 On this page  
- [Construct](https://code.kx.com/q/learn/tour/tables/#construct)
- [Work](https://code.kx.com/q/learn/tour/tables/#work)
- [Keys](https://code.kx.com/q/learn/tour/tables/#keys)
- [Persist](https://code.kx.com/q/learn/tour/tables/#persist)
- [Go large](https://code.kx.com/q/learn/tour/tables/#go-large)

Tables[¶](https://code.kx.com/q/learn/tour/tables/#tables "Permanent link")
===========================================================================

Tables are first-class objects in q.

Construct[¶](https://code.kx.com/q/learn/tour/tables/#construct "Permanent link")
---------------------------------------------------------------------------------

Construct a small table using table notation.

```q
q)ec1:([]city:`Istanbul`Moscow`London`StPetersburg;country:`Turkey`Russia`UK`Russia;pop:15067724 12615279 9126366 5383890)
q)ec1
city         country pop
-----------------------------
Istanbul     Turkey  15067724
Moscow       Russia  12615279
London       UK      9126366
StPetersburg Russia  5383890
```

Equals means equals

In q names are assigned values with the colon. The equals sign `=` is the Equals operator. It returns a boolean.

```q
q)a:5
q)a+2   / a gets 5
7
q)a=2   / no, it is not
0b
```

Unlike classical relational databases, q tables are ordered. You can index them. A table is a list of dictionaries. Any single row is a dictionary.

```q
q)ec1 2
city   | `London
country| `UK
pop    | 9126366
```

And a list of dictionaries with the same keys is – a table.

```q
q)ec1 2 0
city     country pop
-------------------------
London   UK      9126366
Istanbul Turkey  15067724
```

Flipping a table gets you its columns as a dictionary of vectors.

```q
q)flip ec1
city   | Istanbul Moscow   London  StPetersburg
country| Turkey   Russia   UK      Russia
pop    | 15067724 12615279 9126366 5383890
```

Flipping it again puts you back where you started.

```q
q)flip flip ec1
city         country pop
-----------------------------
Istanbul     Turkey  15067724
Moscow       Russia  12615279
London       UK      9126366
StPetersburg Russia  5383890
```

So another way to construct a table:

```q
q)ec2:flip`city`country`pop!(`Berlin`Kyiv`Madrid;`Germany`Ukraine`Spain;3748148 3703100 3223334)
q)ec2
city   country pop
----------------------
Berlin Germany 3748148
Kyiv   Ukraine 3703100
Madrid Spain   3223334
```

CSVs are a common source of tables.

[CSVs](https://code.kx.com/q/learn/tour/csvs/)

Work[¶](https://code.kx.com/q/learn/tour/tables/#work "Permanent link")
-----------------------------------------------------------------------

There are two ways to work with tables and you can mix them to suit yourself.

QSQL queries are very like SQL. (Perhaps a little less verbose.)

```q
q)select city,pop from ec2 upsert ec1
city         pop
---------------------
Berlin       3748148
Kyiv         3703100
Madrid       3223334
Istanbul     15067724
Moscow       12615279
London       9126366
StPetersburg 5383890
```

Or you can think in terms of the underlying q objects.

The [Join](https://code.kx.com/q/ref/join/) operator `,` catenates lists.

```q
q)1 2 3,10 20
1 2 3 10 20
q)"abc","def"
"abcdef"
```

Two tables are two lists of dictionaries.

```q
q)ec2,ec1
city         country pop
-----------------------------
Berlin       Germany 3748148
Kyiv         Ukraine 3703100
Madrid       Spain   3223334
Istanbul     Turkey  15067724
Moscow       Russia  12615279
London       UK      9126366
StPetersburg Russia  5383890
```

Keys[¶](https://code.kx.com/q/learn/tour/tables/#keys "Permanent link")
-----------------------------------------------------------------------

Setting one or more columns of a table as its key divides it into two tables (the keyed and non-keyed columns) and from them makes a dictionary.

The dictionary’s key is the key column/s of the table. Its value is the unkeyed column/s. Both key and value are tables.

Persist[¶](https://code.kx.com/q/learn/tour/tables/#persist "Permanent link")
-----------------------------------------------------------------------------

Any object can be persisted to a file.

```q
q)conts:`Africa`Asia`Australia`Europe`NorthAmerica`SouthAmerica
q)`:path/to/continents set conts
`:path/to/continents
q)get `:path/to/continents
`Africa`Asia`Australia`Europe`NorthAmerica`SouthAmerica

q)`:path/to/ec set ec
`:path/to/ec
q)select from `:path/to/ec where pop>5000000
city         country pop
-----------------------------
Istanbul     Turkey  15067724
Moscow       Russia  12615279
London       UK      9126366
StPetersburg Russia  5383890
```

Go large[¶](https://code.kx.com/q/learn/tour/tables/#go-large "Permanent link")
-------------------------------------------------------------------------------

Flat tables are limited by the absolute maximum size of a vector in kdb+.

Tables up to 100 million rows can be _splayed_ (one file for each column) across directories.

If your table is larger – or grows – you can _partition_ it;usually by time period.

If your table exceeds disk size, you can _segment_ it. (This can also improve I/O performance of a partitioned table.)

[`get`, `set`](https://code.kx.com/q/ref/get/), [`save`](https://code.kx.com/q/ref/save/)

[Splayed tables](https://code.kx.com/q/kb/splayed-tables/), [Partitioned tables](https://code.kx.com/q/kb/partition/)

_Q for Mortals_[§8. Tables](https://code.kx.com/q4m3/8_Tables/), [§14. Introduction to kdb+](https://code.kx.com/q4m3/14_Introduction_to_Kdb%2B)

 Back to top

 This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).

Kx and kdb+ are registered trademarks of [Kx Systems, Inc.](https://kx.com/), a subsidiary of [FD Technologies plc](https://www.fdtechnologies.com/).

 Made with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)

![Image 3](https://id.rlcdn.com/464526.gif)
