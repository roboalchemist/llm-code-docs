# Source: https://koute.github.io/bytehound/memory_leak_analysis.html

Title: Case study: Memory leak analysis

URL Source: https://koute.github.io/bytehound/memory_leak_analysis.html

Markdown Content:
[Case study: Memory leak analysis](https://koute.github.io/bytehound/memory_leak_analysis.html#case-study-memory-leak-analysis)
-------------------------------------------------------------------------------------------------------------------------------

If you'd like to follow along this example check out the `simulation` directory in the root of the profiler's repository where you'll find the program being analyzed here.

We use the built-in scripting capabilities of the profiler for analysis here (which is available either through the `script` subcommand of the CLI, or through the scripting console in the GUI), however you can also use the built-in GUI to achieve roughly similar results. This example is more about demonstrating the mindset you need to have when analyzing the data in search of memory leaks as opposed to a step-by-step guide which you could apply everywhere.

### [Step one: let's take a look at the timeline](https://koute.github.io/bytehound/memory_leak_analysis.html#step-one-lets-take-a-look-at-the-timeline)

First let's try to graph all of the allocations:

```
graph()
    .add(allocations())
    .save();
```

[![Image 1](https://koute.github.io/bytehound/generated/de817a73106b6fcab6f673c2a11e379a.svg)](https://koute.github.io/bytehound/generated/de817a73106b6fcab6f673c2a11e379a.svg)

It definitely looks like we might have some sort of a memory leak here, but we can't see much on this graph alone due to all of the noise.

### [Step two: let's find all of the obvious memory leaks](https://koute.github.io/bytehound/memory_leak_analysis.html#step-two-lets-find-all-of-the-obvious-memory-leaks)

Let's try the simplest thing imaginable: graph only those allocations which were _never_ deallocated up until the very end:

```
graph()
    .add("Leaked", allocations().only_leaked())
    .add("Temporary", allocations())
    .save();
```

[![Image 2](https://koute.github.io/bytehound/generated/1129f4c245d59b852f156ad9c10af4f3.svg)](https://koute.github.io/bytehound/generated/1129f4c245d59b852f156ad9c10af4f3.svg)

Aha! We can see an obvious linear growth here! Let's try to split up the leaking part by backtrace:

```
let groups = allocations()
    .only_leaked()
    .group_by_backtrace()
        .sort_by_size();

graph().add(groups).save();
```

[![Image 3](https://koute.github.io/bytehound/generated/777abfc67d7d8df3b59279fd6a999059.svg)](https://koute.github.io/bytehound/generated/777abfc67d7d8df3b59279fd6a999059.svg)

Looks like we have a few potential leaks here. First, let's start will defining a small helper function which will graph _all_ of the allocations coming from that one single backtrace, and also print out that backtrace:

```
fn analyze_group(list) {
    let list_all = allocations().only_matching_backtraces(list);

    graph()
        .add("Leaked", list_all.only_leaked())
        .add("Temporary", list_all)
        .save();

    println("Total: {}", list_all.len());
    println("Leaked: {}", list_all.only_leaked().len());
    println();
    println("Backtrace:");
    println(list_all[0].backtrace().strip());
}
```

#### [Group #0](https://koute.github.io/bytehound/memory_leak_analysis.html#group-0)

So now let's start with the biggest one:

```
analyze_group(groups[0]);
```

[![Image 4](https://koute.github.io/bytehound/generated/32b3602d1807e04aacd0333ce20e8ba4.svg)](https://koute.github.io/bytehound/generated/32b3602d1807e04aacd0333ce20e8ba4.svg)

```
Total: 1646
Leaked: 1646

Backtrace:
#00 [simulation] _start [start.S:115]
#01 [libc.so.6] __libc_start_main
#02 [libc.so.6] 7f8bb4f5128f
#03 [simulation] main
#17 [simulation] simulation::main [main.rs:122]
#18 [simulation] simulation::allocate_linear_leak_never_deallocated [main.rs:32]
#19 [simulation] alloc::vec::Vec<T,A>::resize [mod.rs:2366]
```

We have a clear-cut memory leak here! Every allocation from this backtrace was leaked.

#### [Group #1](https://koute.github.io/bytehound/memory_leak_analysis.html#group-1)

Let's try yet another one:

```
analyze_group(groups[1]);
```

[![Image 5](https://koute.github.io/bytehound/generated/bc215d78c9605a87ec81c720db91eaa7.svg)](https://koute.github.io/bytehound/generated/bc215d78c9605a87ec81c720db91eaa7.svg)

```
Total: 1838
Leaked: 864

Backtrace:
#00 [simulation] _start [start.S:115]
#01 [libc.so.6] __libc_start_main
#02 [libc.so.6] 7f8bb4f5128f
#03 [simulation] main
#17 [simulation] simulation::main [main.rs:127]
#18 [simulation] simulation::allocate_bounded_leak [main.rs:72]
#19 [simulation] alloc::vec::Vec<T,A>::resize [mod.rs:2366]
```

Now this is interesting. If we only look at the supposedly leaked part it sure does look like it's an unbounded memory leak which grows linearly with time, but if we graph _every_ allocation from this backtrace we can see that its memory usage is actually bounded! The longer we would profile this program the more "flat" the leaked part would get.

So is this a problem? Usually not. If you have something like, say, an LRU cache, you might see this kind of allocation pattern.

#### [Group #2](https://koute.github.io/bytehound/memory_leak_analysis.html#group-2)

Let's look at the last group from our original leaked graph:

```
analyze_group(groups[2]);
```

[![Image 6](https://koute.github.io/bytehound/generated/10e11fbb3c386fc5867cf85ba6606662.svg)](https://koute.github.io/bytehound/generated/10e11fbb3c386fc5867cf85ba6606662.svg)

```
Total: 179391
Leaked: 183

Backtrace:
#00 [simulation] _start [start.S:115]
#01 [libc.so.6] __libc_start_main
#02 [libc.so.6] 7f8bb4f5128f
#03 [simulation] main
#17 [simulation] simulation::main [main.rs:132]
#18 [simulation] simulation::allocate_both_temporary_and_linear_leak [main.rs:96]
#19 [simulation] alloc::vec::Vec<T,A>::resize [mod.rs:2366]
```

This is the toughest case so far. Do we have a memory leak here on not? Well, it depends.

It could be a case of a bounded leak which hasn't yet reached a saturation point, or it could be simply a case of only some allocations ending up leaked. We'd either need to profile for a longer period of time, or analyze the code.

### [Step three: we need to go deeper](https://koute.github.io/bytehound/memory_leak_analysis.html#step-three-we-need-to-go-deeper)

So is this all? Did we actually find all of the memory leaks? Not necessarily.

What we did was that we only looked at those allocations which were **never** deallocated. So what about those allocations which _were_ deallocated, but _only_ at the very end when the program was shut down? Should we consider those allocations as leaks? Well, probably!

First, let's try to graph the memory usage again, but only including the allocations which _were_ deallocated before the program ended.

```
graph()
    .add(allocations().only_temporary())
    .save();
```

[![Image 7](https://koute.github.io/bytehound/generated/8d8466512d3936dac09187bdd5940975.svg)](https://koute.github.io/bytehound/generated/8d8466512d3936dac09187bdd5940975.svg)

Hmm... there might or might not be a leak here. We need a more powerful filter!

First, let's filter out all of the allocations from the previous section; we've already analyzed those so we don't want them here to confuse us:

```
let remaining = allocations().only_not_matching_backtraces(groups);
```

And now, we want a list of allocations which weren't deallocated _right until the end_, right? Well, we can do that!

```
let leaked_until_end = remaining
    .only_leaked_or_deallocated_after(data().runtime() * 0.98);

graph().add(leaked_until_end).save();
```

[![Image 8](https://koute.github.io/bytehound/generated/ec65f23a32addbcc21d7c644e7ee3579.svg)](https://koute.github.io/bytehound/generated/ec65f23a32addbcc21d7c644e7ee3579.svg)

This indeed looks promising. But let's clean in up a little first.

What's with the peak right at the end? Well, we asked for allocations which were _only leaked or deallocated after 98% of the runtime has elapsed_, so naturally those short lived allocations from near the end which were also deallocated after that time will still be included.

Let's get rid of them:

```
let leaked_until_end = remaining
    .only_leaked_or_deallocated_after(data().runtime() * 0.98)
    .only_alive_for_at_least(data().runtime() * 0.02);

graph().add(leaked_until_end).save();
```

[![Image 9](https://koute.github.io/bytehound/generated/fb135c686185b44eb2060786d25f76ee.svg)](https://koute.github.io/bytehound/generated/fb135c686185b44eb2060786d25f76ee.svg)

Much better!

Now let's graph those by backtrace:

```
let groups = leaked_until_end.group_by_backtrace().sort_by_size();
graph().add(groups).save();
```

[![Image 10](https://koute.github.io/bytehound/generated/95bef5b76accb344e7f68b007d10320c.svg)](https://koute.github.io/bytehound/generated/95bef5b76accb344e7f68b007d10320c.svg)

Bingo! There _was_ something hidden in all of those temporary allocations after all!

Let's define another helper function to help us with our analysis:

```
fn analyze_group(list) {
    let list_all = allocations().only_matching_backtraces(list);
    let list_selected = list_all
        .only_deallocated_after_at_least(data().runtime() * 0.98);

    graph()
        .add("Deallocated after 98%", list_selected)
        .add("Deallocated before 98%", list_all)
        .save();

    println("Total: {}", list_all.len());
    println("Deallocated after 98%: {}", list_selected.len());
    println();
    println("Backtrace:");
    println(list_all[0].backtrace().strip());
}
```

Let's try to use it!

#### [Group #0](https://koute.github.io/bytehound/memory_leak_analysis.html#group-0-1)

```
analyze_group(groups[0]);
```

[![Image 11](https://koute.github.io/bytehound/generated/1414653361c213f4cdf3130c906d010d.svg)](https://koute.github.io/bytehound/generated/1414653361c213f4cdf3130c906d010d.svg)

```
Total: 1710
Deallocated after 98%: 1710

Backtrace:
#00 [simulation] _start [start.S:115]
#01 [libc.so.6] __libc_start_main
#02 [libc.so.6] 7f8bb4f5128f
#03 [simulation] main
#17 [simulation] simulation::main [main.rs:123]
#18 [simulation] simulation::allocate_linear_leak_deallocated_at_the_end [main.rs:44]
#19 [simulation] alloc::vec::Vec<T,A>::resize [mod.rs:2366]
```

We have a winner! This definitely looks like a leak.

#### [Group #1](https://koute.github.io/bytehound/memory_leak_analysis.html#group-1-1)

```
analyze_group(groups[1]);
```

[![Image 12](https://koute.github.io/bytehound/generated/def851f48671c55a4e4c2703390b5586.svg)](https://koute.github.io/bytehound/generated/def851f48671c55a4e4c2703390b5586.svg)

```
Total: 9
Deallocated after 98%: 1

Backtrace:
#00 [simulation] _start [start.S:115]
#01 [libc.so.6] __libc_start_main
#02 [libc.so.6] 7f8bb4f5128f
#03 [simulation] main
#17 [simulation] simulation::main [main.rs:123]
#18 [simulation] simulation::allocate_linear_leak_deallocated_at_the_end [main.rs:45]
#19 [simulation] alloc::vec::Vec<T,A>::push [mod.rs:1833]
#20 [simulation] alloc::raw_vec::RawVec<T,A>::reserve_for_push [raw_vec.rs:298]
#21 [simulation] alloc::raw_vec::RawVec<T,A>::grow_amortized [raw_vec.rs:400]
#22 [simulation] alloc::raw_vec::finish_grow [raw_vec.rs:466]
#23 [simulation] <alloc::alloc::Global as core::alloc::Allocator>::grow [alloc.rs:266]
#24 [simulation] alloc::alloc::Global::grow_impl [alloc.rs:213]
#25 [simulation] alloc::alloc::realloc [alloc.rs:213]
#26 [libbytehound.so] realloc [api.rs:377]
```

This is `Vec` that, from the look of it, is just growing in size.

It probably _contains_ whatever is leaking (and if you read the backtrace it actualy _does_), but it's not what we're looking for.

In fact, if we look at the original graph most of what we have remaining are probably cases like this. Let's double-check by filtering out the leak we've already found and graph everything again:

```
let group = groups
    .ungroup()
    .only_not_matching_backtraces(groups[0])
    .group_by_backtrace();

graph().add(group).save();
```

[![Image 13](https://koute.github.io/bytehound/generated/6af338c92abba6952fa8272c4b9e1e3b.svg)](https://koute.github.io/bytehound/generated/6af338c92abba6952fa8272c4b9e1e3b.svg)

This does indeed look like all of the long lived allocations here might have been just `Vec`s.

Let's verify that hypothesis:

```
graph()
    .add("Vecs", group.ungroup().only_passing_through_function("raw_vec::finish_grow"))
    .add("Remaining", group.ungroup())
    .save();
```

[![Image 14](https://koute.github.io/bytehound/generated/9e5779aa236836da6faf6b71b475eb15.svg)](https://koute.github.io/bytehound/generated/9e5779aa236836da6faf6b71b475eb15.svg)

Indeed we were right!

[](https://koute.github.io/bytehound/getting_started.html "Previous chapter")[](https://koute.github.io/bytehound/common_issues.html "Next chapter")

[](https://koute.github.io/bytehound/getting_started.html "Previous chapter")[](https://koute.github.io/bytehound/common_issues.html "Next chapter")
