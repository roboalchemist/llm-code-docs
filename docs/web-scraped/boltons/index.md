# Source: https://boltons.readthedocs.io/

Title: boltons — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/

Markdown Content:
_boltons should be builtins._

[![Image 1: release](https://img.shields.io/pypi/v/boltons.svg)](https://pypi.python.org/pypi/boltons)[![Image 2: calver](https://img.shields.io/badge/calver-YY.MINOR.MICRO-22bfda.svg)](http://calver.org/)[![Image 3: changelog](https://img.shields.io/badge/CHANGELOG-UPDATED-b84ad6.svg)](https://github.com/mahmoud/boltons/blob/master/CHANGELOG.md)

**Boltons** is a set of pure-Python utilities in the same spirit as — and yet conspicuously missing from — [the standard library](https://docs.python.org/3/library/index.html), including:

> *   [`Atomic file saving`](https://boltons.readthedocs.io/en/latest/fileutils.html#boltons.fileutils.atomic_save "boltons.fileutils.atomic_save"), bolted on with [`fileutils`](https://boltons.readthedocs.io/en/latest/fileutils.html#module-boltons.fileutils "boltons.fileutils")
> 
> *   A highly-optimized [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict "boltons.dictutils.OrderedMultiDict"), in [`dictutils`](https://boltons.readthedocs.io/en/latest/dictutils.html#module-boltons.dictutils "boltons.dictutils")
> 
> *   Two types of [`PriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.PriorityQueue "boltons.queueutils.PriorityQueue"), in [`queueutils`](https://boltons.readthedocs.io/en/latest/queueutils.html#module-boltons.queueutils "boltons.queueutils")
> 
> *   [`Chunked`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.chunked "boltons.iterutils.chunked") and [`windowed`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.windowed "boltons.iterutils.windowed") iteration, in [`iterutils`](https://boltons.readthedocs.io/en/latest/iterutils.html#module-boltons.iterutils "boltons.iterutils")
> 
> *   A full-featured [`TracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo "boltons.tbutils.TracebackInfo") type, for representing stack traces, in [`tbutils`](https://boltons.readthedocs.io/en/latest/tbutils.html#module-boltons.tbutils "boltons.tbutils")
> 
> *   A lightweight [`UTC timezone`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.UTC "boltons.timeutils.UTC") available in [`timeutils`](https://boltons.readthedocs.io/en/latest/timeutils.html#module-boltons.timeutils "boltons.timeutils").
> 
> *   Recursive mapping for nested data transforms, with [`remap`](https://boltons.readthedocs.io/en/latest/iterutils.html#boltons.iterutils.remap "boltons.iterutils.remap")

And that’s just a small selection. As of March 06, 2026, `boltons` is 87 types and 172 functions, spread across 29 modules. See them all in the [Index](https://boltons.readthedocs.io/en/latest/genindex.html), and see what’s new by [checking the CHANGELOG](https://github.com/mahmoud/boltons/blob/master/CHANGELOG.md).

Installation and Integration[](https://boltons.readthedocs.io/#installation-and-integration "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

Boltons can be added to a project in a few ways. There’s the obvious one:

pip install boltons

On macOS, it can also be installed via [MacPorts](https://ports.macports.org/port/py-boltons/summary):

sudo port install py-boltons

Then dozens of boltons are just an import away:

from boltons.cacheutils import LRU
lru_cache = LRU()
lru_cache['result'] = 'success'

Due to the nature of utilities, application developers might want to consider other integration options. See the [Integration](https://boltons.readthedocs.io/en/latest/architecture.html#arch-integration) section of the architecture document for more details.

Boltons is tested against Python 3.7-3.13, as well as PyPy3.

Third-party packages[](https://boltons.readthedocs.io/#third-party-packages "Link to this heading")
----------------------------------------------------------------------------------------------------

The majority of boltons strive to be “good enough” for a wide range of basic uses, leaving advanced use cases to Python’s [myriad specialized 3rd-party libraries](https://pypi.python.org/pypi). In many cases the respective `boltons` module will describe 3rd-party alternatives worth investigating when use cases outgrow `boltons`. If you’ve found a natural “next-step” library worth mentioning, [consider filing an issue](https://boltons.readthedocs.io/#gaps)!

Gaps[](https://boltons.readthedocs.io/#gaps "Link to this heading")
--------------------------------------------------------------------

Found something missing in the standard library that should be in `boltons`? Found something missing in `boltons`? First, take a moment to read the very brief [Architecture](https://boltons.readthedocs.io/en/latest/architecture.html) statement to make sure the functionality would be a good fit.

Then, if you are very motivated, submit [a Pull Request](https://github.com/mahmoud/boltons/pulls). Otherwise, submit a short feature request on [the Issues page](https://github.com/mahmoud/boltons/issues), and we will figure something out.

Section listing[](https://boltons.readthedocs.io/#section-listing "Link to this heading")
------------------------------------------------------------------------------------------

*   [Architecture](https://boltons.readthedocs.io/en/latest/architecture.html)
    *   [Integration](https://boltons.readthedocs.io/en/latest/architecture.html#integration)
    *   [Design of a `bolton`](https://boltons.readthedocs.io/en/latest/architecture.html#design-of-a-bolton)
    *   [Themes of `boltons`](https://boltons.readthedocs.io/en/latest/architecture.html#themes-of-boltons)

*   [`cacheutils` - Caches and caching](https://boltons.readthedocs.io/en/latest/cacheutils.html)
    *   [Least-Recently Inserted (LRI)](https://boltons.readthedocs.io/en/latest/cacheutils.html#least-recently-inserted-lri)
    *   [Least-Recently Used (LRU)](https://boltons.readthedocs.io/en/latest/cacheutils.html#least-recently-used-lru)
    *   [Automatic function caching](https://boltons.readthedocs.io/en/latest/cacheutils.html#automatic-function-caching)
    *   [Threshold-bounded Counting](https://boltons.readthedocs.io/en/latest/cacheutils.html#threshold-bounded-counting)

*   [`debugutils` - Debugging utilities](https://boltons.readthedocs.io/en/latest/debugutils.html)
    *   [`pdb_on_exception()`](https://boltons.readthedocs.io/en/latest/debugutils.html#boltons.debugutils.pdb_on_exception)
    *   [`pdb_on_signal()`](https://boltons.readthedocs.io/en/latest/debugutils.html#boltons.debugutils.pdb_on_signal)
    *   [`wrap_trace()`](https://boltons.readthedocs.io/en/latest/debugutils.html#boltons.debugutils.wrap_trace)

*   [`dictutils` - Mapping types (OMD)](https://boltons.readthedocs.io/en/latest/dictutils.html)
    *   [`FrozenDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.FrozenDict)
    *   [`ManyToMany`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.ManyToMany)
    *   [`MultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.MultiDict)
    *   [`OMD`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OMD)
    *   [`OneToOne`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OneToOne)
    *   [`OrderedMultiDict`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.OrderedMultiDict)
    *   [`subdict()`](https://boltons.readthedocs.io/en/latest/dictutils.html#boltons.dictutils.subdict)

*   [`ecoutils` - Ecosystem analytics](https://boltons.readthedocs.io/en/latest/ecoutils.html)
    *   [Transmission and collection](https://boltons.readthedocs.io/en/latest/ecoutils.html#transmission-and-collection)
    *   [Notable omissions](https://boltons.readthedocs.io/en/latest/ecoutils.html#notable-omissions)
    *   [Compatibility](https://boltons.readthedocs.io/en/latest/ecoutils.html#compatibility)
    *   [Profile generation](https://boltons.readthedocs.io/en/latest/ecoutils.html#profile-generation)
    *   [`get_profile()`](https://boltons.readthedocs.io/en/latest/ecoutils.html#boltons.ecoutils.get_profile)

*   [`fileutils` - Filesystem helpers](https://boltons.readthedocs.io/en/latest/fileutils.html)
    *   [Creating, Finding, and Copying](https://boltons.readthedocs.io/en/latest/fileutils.html#creating-finding-and-copying)
    *   [Atomic File Saving](https://boltons.readthedocs.io/en/latest/fileutils.html#atomic-file-saving)
    *   [File Permissions](https://boltons.readthedocs.io/en/latest/fileutils.html#file-permissions)
    *   [Miscellaneous](https://boltons.readthedocs.io/en/latest/fileutils.html#miscellaneous)

*   [`formatutils` - `str.format()` toolbox](https://boltons.readthedocs.io/en/latest/formatutils.html)
    *   [`BaseFormatField`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.BaseFormatField)
    *   [`DeferredValue`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.DeferredValue)
    *   [`construct_format_field_str()`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.construct_format_field_str)
    *   [`get_format_args()`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.get_format_args)
    *   [`infer_positional_format_args()`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.infer_positional_format_args)
    *   [`tokenize_format_str()`](https://boltons.readthedocs.io/en/latest/formatutils.html#boltons.formatutils.tokenize_format_str)

*   [`funcutils` - `functools` fixes](https://boltons.readthedocs.io/en/latest/funcutils.html)
    *   [Decoration](https://boltons.readthedocs.io/en/latest/funcutils.html#decoration)
    *   [Function construction](https://boltons.readthedocs.io/en/latest/funcutils.html#function-construction)
    *   [Improved `partial`](https://boltons.readthedocs.io/en/latest/funcutils.html#improved-partial)
    *   [Miscellaneous metaprogramming](https://boltons.readthedocs.io/en/latest/funcutils.html#miscellaneous-metaprogramming)

*   [`gcutils` - Garbage collecting tools](https://boltons.readthedocs.io/en/latest/gcutils.html)
    *   [`GCToggler`](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.GCToggler)
    *   [`get_all()`](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.get_all)
    *   [`toggle_gc`](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.toggle_gc)
    *   [`toggle_gc_postcollect`](https://boltons.readthedocs.io/en/latest/gcutils.html#boltons.gcutils.toggle_gc_postcollect)

*   [`ioutils` - Input/output enhancements](https://boltons.readthedocs.io/en/latest/ioutils.html)
    *   [Spooled Temporary Files](https://boltons.readthedocs.io/en/latest/ioutils.html#spooled-temporary-files)
    *   [Examples](https://boltons.readthedocs.io/en/latest/ioutils.html#examples)
    *   [Multiple Files](https://boltons.readthedocs.io/en/latest/ioutils.html#multiple-files)

*   [`iterutils` - `itertools` improvements](https://boltons.readthedocs.io/en/latest/iterutils.html)
    *   [Iteration](https://boltons.readthedocs.io/en/latest/iterutils.html#iteration)
    *   [Stripping and splitting](https://boltons.readthedocs.io/en/latest/iterutils.html#stripping-and-splitting)
    *   [Nested](https://boltons.readthedocs.io/en/latest/iterutils.html#nested)
    *   [Numeric](https://boltons.readthedocs.io/en/latest/iterutils.html#numeric)
    *   [Categorization](https://boltons.readthedocs.io/en/latest/iterutils.html#categorization)
    *   [Sorting](https://boltons.readthedocs.io/en/latest/iterutils.html#sorting)
    *   [Reduction](https://boltons.readthedocs.io/en/latest/iterutils.html#reduction)
    *   [Type Checks](https://boltons.readthedocs.io/en/latest/iterutils.html#type-checks)

*   [`jsonutils` - JSON interactions](https://boltons.readthedocs.io/en/latest/jsonutils.html)
    *   [`JSONLIterator`](https://boltons.readthedocs.io/en/latest/jsonutils.html#boltons.jsonutils.JSONLIterator)
    *   [`reverse_iter_lines()`](https://boltons.readthedocs.io/en/latest/jsonutils.html#boltons.jsonutils.reverse_iter_lines)

*   [`listutils` - `list` derivatives](https://boltons.readthedocs.io/en/latest/listutils.html)
    *   [`BList`](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BList)
    *   [`BarrelList`](https://boltons.readthedocs.io/en/latest/listutils.html#boltons.listutils.BarrelList)

*   [`mathutils` - Mathematical functions](https://boltons.readthedocs.io/en/latest/mathutils.html)
    *   [`Bits`](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits)
    *   [Alternative Rounding Functions](https://boltons.readthedocs.io/en/latest/mathutils.html#alternative-rounding-functions)

*   [`mboxutils` - Unix mailbox utilities](https://boltons.readthedocs.io/en/latest/mboxutils.html)
    *   [`mbox_readonlydir`](https://boltons.readthedocs.io/en/latest/mboxutils.html#boltons.mboxutils.mbox_readonlydir)

*   [`namedutils` - Lightweight containers](https://boltons.readthedocs.io/en/latest/namedutils.html)
    *   [`namedlist()`](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedlist)
    *   [`namedtuple()`](https://boltons.readthedocs.io/en/latest/namedutils.html#boltons.namedutils.namedtuple)

*   [`pathutils` - Filesystem fun](https://boltons.readthedocs.io/en/latest/pathutils.html)
    *   [`augpath()`](https://boltons.readthedocs.io/en/latest/pathutils.html#boltons.pathutils.augpath)
    *   [`expandpath()`](https://boltons.readthedocs.io/en/latest/pathutils.html#boltons.pathutils.expandpath)
    *   [`shrinkuser()`](https://boltons.readthedocs.io/en/latest/pathutils.html#boltons.pathutils.shrinkuser)

*   [`queueutils` - Priority queues](https://boltons.readthedocs.io/en/latest/queueutils.html)
    *   [`BasePriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.BasePriorityQueue)
    *   [`HeapPriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.HeapPriorityQueue)
    *   [`PriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.PriorityQueue)
    *   [`SortedPriorityQueue`](https://boltons.readthedocs.io/en/latest/queueutils.html#boltons.queueutils.SortedPriorityQueue)

*   [`setutils` - `IndexedSet` type](https://boltons.readthedocs.io/en/latest/setutils.html)
    *   [`IndexedSet`](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.IndexedSet)
    *   [`complement()`](https://boltons.readthedocs.io/en/latest/setutils.html#boltons.setutils.complement)

*   [`socketutils` - `socket` wrappers](https://boltons.readthedocs.io/en/latest/socketutils.html)
    *   [BufferedSocket](https://boltons.readthedocs.io/en/latest/socketutils.html#bufferedsocket)
    *   [Netstring](https://boltons.readthedocs.io/en/latest/socketutils.html#id1)

*   [`statsutils` - Statistics fundamentals](https://boltons.readthedocs.io/en/latest/statsutils.html)
    *   [Statistical moments](https://boltons.readthedocs.io/en/latest/statsutils.html#statistical-moments)
    *   [Robust statistics](https://boltons.readthedocs.io/en/latest/statsutils.html#robust-statistics)
    *   [Online and Offline Statistics](https://boltons.readthedocs.io/en/latest/statsutils.html#online-and-offline-statistics)
    *   [`Stats`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.Stats)
    *   [`describe()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.describe)
    *   [`format_histogram_counts()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.format_histogram_counts)
    *   [`iqr()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.iqr)
    *   [`kurtosis()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.kurtosis)
    *   [`mean()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.mean)
    *   [`median()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.median)
    *   [`median_abs_dev()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.median_abs_dev)
    *   [`pearson_type()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.pearson_type)
    *   [`rel_std_dev()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.rel_std_dev)
    *   [`skewness()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.skewness)
    *   [`std_dev()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.std_dev)
    *   [`trimean()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.trimean)
    *   [`variance()`](https://boltons.readthedocs.io/en/latest/statsutils.html#boltons.statsutils.variance)

*   [`strutils` - Text manipulation](https://boltons.readthedocs.io/en/latest/strutils.html)
    *   [`MultiReplace`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.MultiReplace)
    *   [`a10n()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.a10n)
    *   [`args2cmd()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.args2cmd)
    *   [`args2sh()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.args2sh)
    *   [`asciify()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.asciify)
    *   [`bytes2human()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.bytes2human)
    *   [`camel2under()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.camel2under)
    *   [`cardinalize()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.cardinalize)
    *   [`complement_int_list()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.complement_int_list)
    *   [`escape_shell_args()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.escape_shell_args)
    *   [`find_hashtags()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.find_hashtags)
    *   [`format_int_list()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.format_int_list)
    *   [`gunzip_bytes()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.gunzip_bytes)
    *   [`gzip_bytes()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.gzip_bytes)
    *   [`html2text()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.html2text)
    *   [`human_readable_list()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.human_readable_list)
    *   [`indent()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.indent)
    *   [`int_ranges_from_int_list()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.int_ranges_from_int_list)
    *   [`is_ascii()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.is_ascii)
    *   [`is_uuid()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.is_uuid)
    *   [`iter_splitlines()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.iter_splitlines)
    *   [`multi_replace()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.multi_replace)
    *   [`ordinalize()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.ordinalize)
    *   [`parse_int_list()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.parse_int_list)
    *   [`pluralize()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.pluralize)
    *   [`removeprefix()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.removeprefix)
    *   [`singularize()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.singularize)
    *   [`slugify()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.slugify)
    *   [`split_punct_ws()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.split_punct_ws)
    *   [`strip_ansi()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.strip_ansi)
    *   [`under2camel()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.under2camel)
    *   [`unit_len()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.unit_len)
    *   [`unwrap_text()`](https://boltons.readthedocs.io/en/latest/strutils.html#boltons.strutils.unwrap_text)

*   [`tableutils` - 2D data structure](https://boltons.readthedocs.io/en/latest/tableutils.html)
    *   [`Table`](https://boltons.readthedocs.io/en/latest/tableutils.html#boltons.tableutils.Table)

*   [`tbutils` - Tracebacks and call stacks](https://boltons.readthedocs.io/en/latest/tbutils.html)
    *   [`Callpoint`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.Callpoint)
    *   [`ContextualCallpoint`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualCallpoint)
    *   [`ContextualExceptionInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualExceptionInfo)
    *   [`ContextualTracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ContextualTracebackInfo)
    *   [`ExceptionInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ExceptionInfo)
    *   [`ParsedException`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.ParsedException)
    *   [`TracebackInfo`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.TracebackInfo)
    *   [`print_exception()`](https://boltons.readthedocs.io/en/latest/tbutils.html#boltons.tbutils.print_exception)

*   [`timeutils` - `datetime` additions](https://boltons.readthedocs.io/en/latest/timeutils.html)
    *   [`daterange()`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.daterange)
    *   [`isoparse()`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.isoparse)
    *   [`parse_timedelta()`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.parse_timedelta)
    *   [`strpdate()`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.strpdate)
    *   [`total_seconds()`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.total_seconds)
    *   [`dt_to_timestamp()`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.dt_to_timestamp)
    *   [`relative_time()`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.relative_time)
    *   [`decimal_relative_time()`](https://boltons.readthedocs.io/en/latest/timeutils.html#boltons.timeutils.decimal_relative_time)
    *   [General timezones](https://boltons.readthedocs.io/en/latest/timeutils.html#general-timezones)
    *   [US timezones](https://boltons.readthedocs.io/en/latest/timeutils.html#us-timezones)

*   [`typeutils` - Type handling](https://boltons.readthedocs.io/en/latest/typeutils.html)
    *   [`classproperty`](https://boltons.readthedocs.io/en/latest/typeutils.html#boltons.typeutils.classproperty)
    *   [`get_all_subclasses()`](https://boltons.readthedocs.io/en/latest/typeutils.html#boltons.typeutils.get_all_subclasses)
    *   [`issubclass()`](https://boltons.readthedocs.io/en/latest/typeutils.html#boltons.typeutils.issubclass)
    *   [`make_sentinel()`](https://boltons.readthedocs.io/en/latest/typeutils.html#boltons.typeutils.make_sentinel)

*   [`urlutils` - Structured URL](https://boltons.readthedocs.io/en/latest/urlutils.html)
    *   [The URL type](https://boltons.readthedocs.io/en/latest/urlutils.html#the-url-type)
    *   [Low-level functions](https://boltons.readthedocs.io/en/latest/urlutils.html#low-level-functions)
    *   [Useful constants](https://boltons.readthedocs.io/en/latest/urlutils.html#useful-constants)

(For a quick reference you can ctrl-F, see the [Index](https://boltons.readthedocs.io/en/latest/genindex.html).)
