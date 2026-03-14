# Source: https://koute.github.io/bytehound/configuration.html

Title: Configuring the profiler - Memory profiling for fun and profit

URL Source: https://koute.github.io/bytehound/configuration.html

Markdown Content:
Configuring the profiler - Memory profiling for fun and profit
===============

1.   [**1.** Introduction](https://koute.github.io/bytehound/introduction.html)
2.   [**2.** Getting started](https://koute.github.io/bytehound/getting_started.html)
3.   [**3.** Case study: Memory leak analysis](https://koute.github.io/bytehound/memory_leak_analysis.html)
4.   [**4.** Common issues](https://koute.github.io/bytehound/common_issues.html)
5.   [**5.** Configuring the profiler](https://koute.github.io/bytehound/configuration.html)
6.   [**6.** API reference](https://koute.github.io/bytehound/api_reference.html)
7.       1.   [**6.1.** Globally available functions](https://koute.github.io/bytehound/api_reference/globals.html)
    2.           1.   [**6.1.1.** allocations](https://koute.github.io/bytehound/api_reference/globals/allocations.html)
        2.   [**6.1.2.** maps](https://koute.github.io/bytehound/api_reference/globals/maps.html)
        3.   [**6.1.3.** data](https://koute.github.io/bytehound/api_reference/globals/data.html)
        4.   [**6.1.4.** graph](https://koute.github.io/bytehound/api_reference/globals/graph.html)
        5.   [**6.1.5.** info](https://koute.github.io/bytehound/api_reference/globals/info.html)
        6.   [**6.1.6.** load](https://koute.github.io/bytehound/api_reference/globals/load.html)
        7.   [**6.1.7.** println](https://koute.github.io/bytehound/api_reference/globals/println.html)
        8.   [**6.1.8.** h](https://koute.github.io/bytehound/api_reference/globals/h.html)
        9.   [**6.1.9.** m](https://koute.github.io/bytehound/api_reference/globals/m.html)
        10.   [**6.1.10.** s](https://koute.github.io/bytehound/api_reference/globals/s.html)
        11.   [**6.1.11.** ms](https://koute.github.io/bytehound/api_reference/globals/ms.html)
        12.   [**6.1.12.** us](https://koute.github.io/bytehound/api_reference/globals/us.html)
        13.   [**6.1.13.** kb](https://koute.github.io/bytehound/api_reference/globals/kb.html)
        14.   [**6.1.14.** mb](https://koute.github.io/bytehound/api_reference/globals/mb.html)
        15.   [**6.1.15.** gb](https://koute.github.io/bytehound/api_reference/globals/gb.html)
        16.   [**6.1.16.** argv](https://koute.github.io/bytehound/api_reference/globals/argv.html)
        17.   [**6.1.17.** chdir](https://koute.github.io/bytehound/api_reference/globals/chdir.html)
        18.   [**6.1.18.** dirname](https://koute.github.io/bytehound/api_reference/globals/dirname.html)
        19.   [**6.1.19.** exit](https://koute.github.io/bytehound/api_reference/globals/exit.html)
        20.   [**6.1.20.** mkdir_p](https://koute.github.io/bytehound/api_reference/globals/mkdir_p.html)

    3.   [**6.2.** Allocation](https://koute.github.io/bytehound/api_reference/Allocation.html)
    4.           1.   [**6.2.1.** allocated_at](https://koute.github.io/bytehound/api_reference/Allocation/allocated_at.html)
        2.   [**6.2.2.** backtrace](https://koute.github.io/bytehound/api_reference/Allocation/backtrace.html)
        3.   [**6.2.3.** deallocated_at](https://koute.github.io/bytehound/api_reference/Allocation/deallocated_at.html)

    5.   [**6.3.** AllocationList](https://koute.github.io/bytehound/api_reference/AllocationList.html)
    6.           1.   [**6.3.1.** - (operator)](https://koute.github.io/bytehound/api_reference/AllocationList/op_minus.html)
        2.   [**6.3.2.** + (operator)](https://koute.github.io/bytehound/api_reference/AllocationList/op_plus.html)
        3.   [**6.3.3.**& (operator)](https://koute.github.io/bytehound/api_reference/AllocationList/op_and.html)
        4.   [**6.3.4.** [] (operator)](https://koute.github.io/bytehound/api_reference/AllocationList/op_square_brackets.html)
        5.   [**6.3.5.** group_by_backtrace](https://koute.github.io/bytehound/api_reference/AllocationList/group_by_backtrace.html)
        6.   [**6.3.6.** len](https://koute.github.io/bytehound/api_reference/AllocationList/len.html)
        7.   [**6.3.7.** only_address_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_address_at_least.html)
        8.   [**6.3.8.** only_address_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_address_at_most.html)
        9.   [**6.3.9.** only_alive_at](https://koute.github.io/bytehound/api_reference/AllocationList/only_alive_at.html)
        10.   [**6.3.10.** only_alive_for_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_alive_for_at_least.html)
        11.   [**6.3.11.** only_alive_for_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_alive_for_at_most.html)
        12.   [**6.3.12.** only_allocated_after_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_allocated_after_at_least.html)
        13.   [**6.3.13.** only_allocated_until_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_allocated_until_at_most.html)
        14.   [**6.3.14.** only_backtrace_length_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_backtrace_length_at_least.html)
        15.   [**6.3.15.** only_backtrace_length_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_backtrace_length_at_most.html)
        16.   [**6.3.16.** only_chain_alive_for_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_chain_alive_for_at_least.html)
        17.   [**6.3.17.** only_chain_alive_for_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_chain_alive_for_at_most.html)
        18.   [**6.3.18.** only_chain_length_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_chain_length_at_least.html)
        19.   [**6.3.19.** only_chain_length_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_chain_length_at_most.html)
        20.   [**6.3.20.** only_deallocated_after_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_deallocated_after_at_least.html)
        21.   [**6.3.21.** only_deallocated_until_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_deallocated_until_at_most.html)
        22.   [**6.3.22.** only_first_size_larger_or_equal](https://koute.github.io/bytehound/api_reference/AllocationList/only_first_size_larger_or_equal.html)
        23.   [**6.3.23.** only_first_size_larger](https://koute.github.io/bytehound/api_reference/AllocationList/only_first_size_larger.html)
        24.   [**6.3.24.** only_first_size_smaller_or_equal](https://koute.github.io/bytehound/api_reference/AllocationList/only_first_size_smaller_or_equal.html)
        25.   [**6.3.25.** only_first_size_smaller](https://koute.github.io/bytehound/api_reference/AllocationList/only_first_size_smaller.html)
        26.   [**6.3.26.** only_from_maps](https://koute.github.io/bytehound/api_reference/AllocationList/only_from_maps.html)
        27.   [**6.3.27.** only_group_allocations_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_group_allocations_at_least.html)
        28.   [**6.3.28.** only_group_allocations_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_group_allocations_at_most.html)
        29.   [**6.3.29.** only_group_interval_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_group_interval_at_least.html)
        30.   [**6.3.30.** only_group_interval_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_group_interval_at_most.html)
        31.   [**6.3.31.** only_group_leaked_allocations_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_group_leaked_allocations_at_least.html)
        32.   [**6.3.32.** only_group_leaked_allocations_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_group_leaked_allocations_at_most.html)
        33.   [**6.3.33.** only_group_max_total_usage_first_seen_at_least](https://koute.github.io/bytehound/api_reference/AllocationList/only_group_max_total_usage_first_seen_at_least.html)
        34.   [**6.3.34.** only_group_max_total_usage_first_seen_at_most](https://koute.github.io/bytehound/api_reference/AllocationList/only_group_max_total_usage_first_seen_at_most.html)
        35.   [**6.3.35.** only_jemalloc](https://koute.github.io/bytehound/api_reference/AllocationList/only_jemalloc.html)
        36.   [**6.3.36.** only_larger_or_equal](https://koute.github.io/bytehound/api_reference/AllocationList/only_larger_or_equal.html)
        37.   [**6.3.37.** only_larger](https://koute.github.io/bytehound/api_reference/AllocationList/only_larger.html)
        38.   [**6.3.38.** only_last_size_larger_or_equal](https://koute.github.io/bytehound/api_reference/AllocationList/only_last_size_larger_or_equal.html)
        39.   [**6.3.39.** only_last_size_larger](https://koute.github.io/bytehound/api_reference/AllocationList/only_last_size_larger.html)
        40.   [**6.3.40.** only_last_size_smaller_or_equal](https://koute.github.io/bytehound/api_reference/AllocationList/only_last_size_smaller_or_equal.html)
        41.   [**6.3.41.** only_last_size_smaller](https://koute.github.io/bytehound/api_reference/AllocationList/only_last_size_smaller.html)
        42.   [**6.3.42.** only_leaked_or_deallocated_after](https://koute.github.io/bytehound/api_reference/AllocationList/only_leaked_or_deallocated_after.html)
        43.   [**6.3.43.** only_leaked](https://koute.github.io/bytehound/api_reference/AllocationList/only_leaked.html)
        44.   [**6.3.44.** only_matching_backtraces](https://koute.github.io/bytehound/api_reference/AllocationList/only_matching_backtraces.html)
        45.   [**6.3.45.** only_not_jemalloc](https://koute.github.io/bytehound/api_reference/AllocationList/only_not_jemalloc.html)
        46.   [**6.3.46.** only_not_matching_backtraces](https://koute.github.io/bytehound/api_reference/AllocationList/only_not_matching_backtraces.html)
        47.   [**6.3.47.** only_not_passing_through_function](https://koute.github.io/bytehound/api_reference/AllocationList/only_not_passing_through_function.html)
        48.   [**6.3.48.** only_not_passing_through_source](https://koute.github.io/bytehound/api_reference/AllocationList/only_not_passing_through_source.html)
        49.   [**6.3.49.** only_passing_through_function](https://koute.github.io/bytehound/api_reference/AllocationList/only_passing_through_function.html)
        50.   [**6.3.50.** only_passing_through_source](https://koute.github.io/bytehound/api_reference/AllocationList/only_passing_through_source.html)
        51.   [**6.3.51.** only_ptmalloc_from_main_arena](https://koute.github.io/bytehound/api_reference/AllocationList/only_ptmalloc_from_main_arena.html)
        52.   [**6.3.52.** only_ptmalloc_mmaped](https://koute.github.io/bytehound/api_reference/AllocationList/only_ptmalloc_mmaped.html)
        53.   [**6.3.53.** only_ptmalloc_not_from_main_arena](https://koute.github.io/bytehound/api_reference/AllocationList/only_ptmalloc_not_from_main_arena.html)
        54.   [**6.3.54.** only_ptmalloc_not_mmaped](https://koute.github.io/bytehound/api_reference/AllocationList/only_ptmalloc_not_mmaped.html)
        55.   [**6.3.55.** only_smaller_or_equal](https://koute.github.io/bytehound/api_reference/AllocationList/only_smaller_or_equal.html)
        56.   [**6.3.56.** only_smaller](https://koute.github.io/bytehound/api_reference/AllocationList/only_smaller.html)
        57.   [**6.3.57.** only_temporary](https://koute.github.io/bytehound/api_reference/AllocationList/only_temporary.html)
        58.   [**6.3.58.** save_as_flamegraph](https://koute.github.io/bytehound/api_reference/AllocationList/save_as_flamegraph.html)
        59.   [**6.3.59.** save_as_graph](https://koute.github.io/bytehound/api_reference/AllocationList/save_as_graph.html)

    7.   [**6.4.** AllocationGroupList](https://koute.github.io/bytehound/api_reference/AllocationGroupList.html)
    8.           1.   [**6.4.1.** (iterator)](https://koute.github.io/bytehound/api_reference/AllocationGroupList/op_iterator.html)
        2.   [**6.4.2.** [] (operator)](https://koute.github.io/bytehound/api_reference/AllocationGroupList/op_square_brackets.html)
        3.   [**6.4.3.** len](https://koute.github.io/bytehound/api_reference/AllocationGroupList/len.html)
        4.   [**6.4.4.** only_all_leaked](https://koute.github.io/bytehound/api_reference/AllocationGroupList/only_all_leaked.html)
        5.   [**6.4.5.** only_count_at_least](https://koute.github.io/bytehound/api_reference/AllocationGroupList/only_count_at_least.html)
        6.   [**6.4.6.** sort_by_count_ascending](https://koute.github.io/bytehound/api_reference/AllocationGroupList/sort_by_count_ascending.html)
        7.   [**6.4.7.** sort_by_count_descending](https://koute.github.io/bytehound/api_reference/AllocationGroupList/sort_by_count_descending.html)
        8.   [**6.4.8.** sort_by_count](https://koute.github.io/bytehound/api_reference/AllocationGroupList/sort_by_count.html)
        9.   [**6.4.9.** sort_by_size_ascending](https://koute.github.io/bytehound/api_reference/AllocationGroupList/sort_by_size_ascending.html)
        10.   [**6.4.10.** sort_by_size_descending](https://koute.github.io/bytehound/api_reference/AllocationGroupList/sort_by_size_descending.html)
        11.   [**6.4.11.** sort_by_size](https://koute.github.io/bytehound/api_reference/AllocationGroupList/sort_by_size.html)
        12.   [**6.4.12.** take](https://koute.github.io/bytehound/api_reference/AllocationGroupList/take.html)
        13.   [**6.4.13.** ungroup](https://koute.github.io/bytehound/api_reference/AllocationGroupList/ungroup.html)

    9.   [**6.5.** Backtrace](https://koute.github.io/bytehound/api_reference/Backtrace.html)
    10.           1.   [**6.5.1.** strip](https://koute.github.io/bytehound/api_reference/Backtrace/strip.html)

    11.   [**6.6.** Data](https://koute.github.io/bytehound/api_reference/Data.html)
    12.           1.   [**6.6.1.** allocations](https://koute.github.io/bytehound/api_reference/Data/allocations.html)
        2.   [**6.6.2.** runtime](https://koute.github.io/bytehound/api_reference/Data/runtime.html)

    13.   [**6.7.** Duration](https://koute.github.io/bytehound/api_reference/Duration.html)
    14.           1.   [**6.7.1.** + (operator)](https://koute.github.io/bytehound/api_reference/Duration/op_plus.html)
        2.   [**6.7.2.** - (operator)](https://koute.github.io/bytehound/api_reference/Duration/op_minus.html)
        3.   [**6.7.3.** * (operator)](https://koute.github.io/bytehound/api_reference/Duration/op_multiply.html)

    15.   [**6.8.** Graph](https://koute.github.io/bytehound/api_reference/Graph.html)
    16.           1.   [**6.8.1.** add](https://koute.github.io/bytehound/api_reference/Graph/add.html)
        2.   [**6.8.2.** only_non_empty_series](https://koute.github.io/bytehound/api_reference/Graph/only_non_empty_series.html)
        3.   [**6.8.3.** save_each_series_as_flamegraph](https://koute.github.io/bytehound/api_reference/Graph/save_each_series_as_flamegraph.html)
        4.   [**6.8.4.** save_each_series_as_graph](https://koute.github.io/bytehound/api_reference/Graph/save_each_series_as_graph.html)
        5.   [**6.8.5.** save](https://koute.github.io/bytehound/api_reference/Graph/save.html)
        6.   [**6.8.6.** show_address_space](https://koute.github.io/bytehound/api_reference/Graph/show_address_space.html)
        7.   [**6.8.7.** show_deallocations](https://koute.github.io/bytehound/api_reference/Graph/show_deallocations.html)
        8.   [**6.8.8.** show_live_allocations](https://koute.github.io/bytehound/api_reference/Graph/show_live_allocations.html)
        9.   [**6.8.9.** show_memory_usage](https://koute.github.io/bytehound/api_reference/Graph/show_memory_usage.html)
        10.   [**6.8.10.** show_new_allocations](https://koute.github.io/bytehound/api_reference/Graph/show_new_allocations.html)
        11.   [**6.8.11.** show_rss](https://koute.github.io/bytehound/api_reference/Graph/show_rss.html)
        12.   [**6.8.12.** trim_left](https://koute.github.io/bytehound/api_reference/Graph/trim_left.html)
        13.   [**6.8.13.** trim_right](https://koute.github.io/bytehound/api_reference/Graph/trim_right.html)
        14.   [**6.8.14.** trim](https://koute.github.io/bytehound/api_reference/Graph/trim.html)
        15.   [**6.8.15.** start_at](https://koute.github.io/bytehound/api_reference/Graph/start_at.html)
        16.   [**6.8.16.** end_at](https://koute.github.io/bytehound/api_reference/Graph/end_at.html)
        17.   [**6.8.17.** with_gradient_color_scheme](https://koute.github.io/bytehound/api_reference/Graph/with_gradient_color_scheme.html)
        18.   [**6.8.18.** without_axes](https://koute.github.io/bytehound/api_reference/Graph/without_axes.html)
        19.   [**6.8.19.** without_grid](https://koute.github.io/bytehound/api_reference/Graph/without_grid.html)
        20.   [**6.8.20.** without_legend](https://koute.github.io/bytehound/api_reference/Graph/without_legend.html)

    17.   [**6.9.** Map](https://koute.github.io/bytehound/api_reference/Map.html)
    18.           1.   [**6.9.1.** allocated_at](https://koute.github.io/bytehound/api_reference/Map/allocated_at.html)
        2.   [**6.9.2.** backtrace](https://koute.github.io/bytehound/api_reference/Map/backtrace.html)
        3.   [**6.9.3.** deallocated_at](https://koute.github.io/bytehound/api_reference/Map/deallocated_at.html)

    19.   [**6.10.** MapList](https://koute.github.io/bytehound/api_reference/MapList.html)
    20.           1.   [**6.10.1.** len](https://koute.github.io/bytehound/api_reference/MapList/len.html)
        2.   [**6.10.2.** only_address_at_least](https://koute.github.io/bytehound/api_reference/MapList/only_address_at_least.html)
        3.   [**6.10.3.** only_address_at_most](https://koute.github.io/bytehound/api_reference/MapList/only_address_at_most.html)
        4.   [**6.10.4.** only_alive_at](https://koute.github.io/bytehound/api_reference/MapList/only_alive_at.html)
        5.   [**6.10.5.** only_alive_for_at_least](https://koute.github.io/bytehound/api_reference/MapList/only_alive_for_at_least.html)
        6.   [**6.10.6.** only_alive_for_at_most](https://koute.github.io/bytehound/api_reference/MapList/only_alive_for_at_most.html)
        7.   [**6.10.7.** only_allocated_after_at_least](https://koute.github.io/bytehound/api_reference/MapList/only_allocated_after_at_least.html)
        8.   [**6.10.8.** only_allocated_until_at_most](https://koute.github.io/bytehound/api_reference/MapList/only_allocated_until_at_most.html)
        9.   [**6.10.9.** only_backtrace_length_at_least](https://koute.github.io/bytehound/api_reference/MapList/only_backtrace_length_at_least.html)
        10.   [**6.10.10.** only_backtrace_length_at_most](https://koute.github.io/bytehound/api_reference/MapList/only_backtrace_length_at_most.html)
        11.   [**6.10.11.** only_bytehound](https://koute.github.io/bytehound/api_reference/MapList/only_bytehound.html)
        12.   [**6.10.12.** only_deallocated_after_at_least](https://koute.github.io/bytehound/api_reference/MapList/only_deallocated_after_at_least.html)
        13.   [**6.10.13.** only_deallocated_until_at_most](https://koute.github.io/bytehound/api_reference/MapList/only_deallocated_until_at_most.html)
        14.   [**6.10.14.** only_executable](https://koute.github.io/bytehound/api_reference/MapList/only_executable.html)
        15.   [**6.10.15.** only_jemalloc](https://koute.github.io/bytehound/api_reference/MapList/only_jemalloc.html)
        16.   [**6.10.16.** only_larger](https://koute.github.io/bytehound/api_reference/MapList/only_larger.html)
        17.   [**6.10.17.** only_larger_or_equal](https://koute.github.io/bytehound/api_reference/MapList/only_larger_or_equal.html)
        18.   [**6.10.18.** only_leaked](https://koute.github.io/bytehound/api_reference/MapList/only_leaked.html)
        19.   [**6.10.19.** only_leaked_or_deallocated_after](https://koute.github.io/bytehound/api_reference/MapList/only_leaked_or_deallocated_after.html)
        20.   [**6.10.20.** only_matching_backtraces](https://koute.github.io/bytehound/api_reference/MapList/only_matching_backtraces.html)
        21.   [**6.10.21.** only_matching_deallocation_backtraces](https://koute.github.io/bytehound/api_reference/MapList/only_matching_deallocation_backtraces.html)
        22.   [**6.10.22.** only_not_bytehound](https://koute.github.io/bytehound/api_reference/MapList/only_not_bytehound.html)
        23.   [**6.10.23.** only_not_executable](https://koute.github.io/bytehound/api_reference/MapList/only_not_executable.html)
        24.   [**6.10.24.** only_not_jemalloc](https://koute.github.io/bytehound/api_reference/MapList/only_not_jemalloc.html)
        25.   [**6.10.25.** only_not_matching_backtraces](https://koute.github.io/bytehound/api_reference/MapList/only_not_matching_backtraces.html)
        26.   [**6.10.26.** only_not_matching_deallocation_backtraces](https://koute.github.io/bytehound/api_reference/MapList/only_not_matching_deallocation_backtraces.html)
        27.   [**6.10.27.** only_not_passing_through_function](https://koute.github.io/bytehound/api_reference/MapList/only_not_passing_through_function.html)
        28.   [**6.10.28.** only_not_passing_through_source](https://koute.github.io/bytehound/api_reference/MapList/only_not_passing_through_source.html)
        29.   [**6.10.29.** only_not_readable](https://koute.github.io/bytehound/api_reference/MapList/only_not_readable.html)
        30.   [**6.10.30.** only_not_writable](https://koute.github.io/bytehound/api_reference/MapList/only_not_writable.html)
        31.   [**6.10.31.** only_passing_through_function](https://koute.github.io/bytehound/api_reference/MapList/only_passing_through_function.html)
        32.   [**6.10.32.** only_passing_through_source](https://koute.github.io/bytehound/api_reference/MapList/only_passing_through_source.html)
        33.   [**6.10.33.** only_peak_rss_at_least](https://koute.github.io/bytehound/api_reference/MapList/only_peak_rss_at_least.html)
        34.   [**6.10.34.** only_peak_rss_at_most](https://koute.github.io/bytehound/api_reference/MapList/only_peak_rss_at_most.html)
        35.   [**6.10.35.** only_readable](https://koute.github.io/bytehound/api_reference/MapList/only_readable.html)
        36.   [**6.10.36.** only_smaller](https://koute.github.io/bytehound/api_reference/MapList/only_smaller.html)
        37.   [**6.10.37.** only_smaller_or_equal](https://koute.github.io/bytehound/api_reference/MapList/only_smaller_or_equal.html)
        38.   [**6.10.38.** only_temporary](https://koute.github.io/bytehound/api_reference/MapList/only_temporary.html)
        39.   [**6.10.39.** only_writable](https://koute.github.io/bytehound/api_reference/MapList/only_writable.html)
        40.   [**6.10.40.** - (operator)](https://koute.github.io/bytehound/api_reference/MapList/op_minus.html)
        41.   [**6.10.41.** + (operator)](https://koute.github.io/bytehound/api_reference/MapList/op_plus.html)
        42.   [**6.10.42.**& (operator)](https://koute.github.io/bytehound/api_reference/MapList/op_and.html)
        43.   [**6.10.43.** [] (operator)](https://koute.github.io/bytehound/api_reference/MapList/op_square_brackets.html)

*   Light (default)
*   Rust
*   Coal
*   Navy
*   Ayu

Memory profiling for fun and profit
===================================

[](https://koute.github.io/bytehound/print.html "Print this book")

[Configuring the profiler](https://koute.github.io/bytehound/configuration.html#configuring-the-profiler)
=========================================================================================================

The profiler is configured through environment variables; here's a list of all of the supported environment variables that you can set.

### [`MEMORY_PROFILER_OUTPUT`](https://koute.github.io/bytehound/configuration.html#memory_profiler_output)

_Default: `memory-profiling\_%e\_%t\_%p.dat`_

A path to a file to which the data will be written to.

This environment variable supports placeholders which will be replaced at runtime with the following:

*   `%p` -> PID of the process
*   `%t` -> number of seconds since UNIX epoch
*   `%e` -> name of the executable
*   `%n` -> auto-incrementing counter (0, 1, .., 9, 10, etc.)

### [`MEMORY_PROFILER_LOG`](https://koute.github.io/bytehound/configuration.html#memory_profiler_log)

_Default: unset_

The log level to use; possible values:

*   `trace`
*   `debug`
*   `info`
*   `warn`
*   `error`

Unset by default, which disables logging altogether.

### [`MEMORY_PROFILER_LOGFILE`](https://koute.github.io/bytehound/configuration.html#memory_profiler_logfile)

_Default: unset_

Path to the file to which the logs will be written to; if unset the logs will be emitted to stderr (if they're enabled with `MEMORY_PROFILER_LOG`).

This supports placeholders similar to `MEMORY_PROFILER_OUTPUT` (except `%n`).

### [`MEMORY_PROFILER_CULL_TEMPORARY_ALLOCATIONS`](https://koute.github.io/bytehound/configuration.html#memory_profiler_cull_temporary_allocations)

_Default: `0`_

When set to `1` the profiler will cull temporary allocations and omit them from the output.

Use this if you only care about memory leaks or you want to do long term profiling over several days.

### [`MEMORY_PROFILER_TEMPORARY_ALLOCATION_LIFETIME_THRESHOLD`](https://koute.github.io/bytehound/configuration.html#memory_profiler_temporary_allocation_lifetime_threshold)

_Default: `10000`_

The minimum lifetime of an allocation, in milliseconds, to **not** be considered a temporary allocation, and hence not get culled.

Only makes sense when `MEMORY_PROFILER_CULL_TEMPORARY_ALLOCATIONS` is turned on.

### [`MEMORY_PROFILER_TEMPORARY_ALLOCATION_PENDING_THRESHOLD`](https://koute.github.io/bytehound/configuration.html#memory_profiler_temporary_allocation_pending_threshold)

_Default: None_

The maximum number of allocations to be kept in memory when tracking which allocations are temporary and which are not.

Every allocation whose lifetime hasn't yet crossed the temporary allocation interval will be temporarily kept in a buffer, and removed from it once it either gets deallocated or its lifetime crosses the temporary allocation interval.

If the number of allocations stored in this buffer exceeds the value set here the buffer will be cleared and all of the allocations contained within will be written to disk, regardless of their lifetime.

Only makes sense when `MEMORY_PROFILER_CULL_TEMPORARY_ALLOCATIONS` is turned on.

### [`MEMORY_PROFILER_GRAB_BACKTRACES_ON_FREE`](https://koute.github.io/bytehound/configuration.html#memory_profiler_grab_backtraces_on_free)

_Default: `1`_

When set to `1` the backtraces will be also be gathered when the memory is freed.

### [`MEMORY_PROFILER_DISABLE_BY_DEFAULT`](https://koute.github.io/bytehound/configuration.html#memory_profiler_disable_by_default)

_Default: `0`_

When set to `1` the tracing will be disabled be default at startup.

### [`MEMORY_PROFILER_REGISTER_SIGUSR1`](https://koute.github.io/bytehound/configuration.html#memory_profiler_register_sigusr1)

_Default: `1`_

When set to `1` the profiler will register a `SIGUSR1` signal handler which can be used to toggle (enable or disable) profiling.

### [`MEMORY_PROFILER_REGISTER_SIGUSR2`](https://koute.github.io/bytehound/configuration.html#memory_profiler_register_sigusr2)

_Default: `1`_

When set to `1` the profiler will register a `SIGUSR2` signal handler which can be used to toggle (enable or disable) profiling.

### [`MEMORY_PROFILER_ENABLE_SERVER`](https://koute.github.io/bytehound/configuration.html#memory_profiler_enable_server)

_Default: `0`_

When set to `1` the profiled process will start an embedded server which can be used to stream the profiling data through TCP using `bytehound gather` and `bytehound-gather`.

This server will only be started when profiling is first enabled.

### [`MEMORY_PROFILER_BASE_SERVER_PORT`](https://koute.github.io/bytehound/configuration.html#memory_profiler_base_server_port)

_Default: `8100`_

TCP port of the embedded server on which the profiler will listen on.

If the profiler won't be able to bind a socket to this port it will try to find the next free port to bind to. It will succesively probe the ports in a linear fashion, e.g. 8100, 8101, 8102, etc., up to 100 times before giving up.

Requires `MEMORY_PROFILER_ENABLE_SERVER` to be set to `1`.

### [`MEMORY_PROFILER_ENABLE_BROADCAST`](https://koute.github.io/bytehound/configuration.html#memory_profiler_enable_broadcast)

_Default: `0`_

When set to `1` the profiled process will send UDP broadcasts announcing that it's being profiled. This is used by `bytehound gather` and `bytehound-gather` to automatically discover `bytehound` instances to which to connect.

Requires `MEMORY_PROFILER_ENABLE_SERVER` to be set to `1`.

### [`MEMORY_PROFILER_WRITE_BINARIES_TO_OUTPUT`](https://koute.github.io/bytehound/configuration.html#memory_profiler_write_binaries_to_output)

_Default: `1`_

Controls whenever the profiler will embed the profiled application (and all of the libraries used by the application) inside of the profiling data it writes to disk.

This makes it possible to later decode the profiling data without having to manually hunt down the original binaries.

### [`MEMORY_PROFILER_ZERO_MEMORY`](https://koute.github.io/bytehound/configuration.html#memory_profiler_zero_memory)

_Default: `0`_

Decides whenever `malloc` will behave like `calloc` and fill the memory it returns with zeros.

### [`MEMORY_PROFILER_BACKTRACE_CACHE_SIZE_LEVEL_1`](https://koute.github.io/bytehound/configuration.html#memory_profiler_backtrace_cache_size_level_1)

_Default: `16384`_

Controls the size of the internal backtrace cache used to deduplicate emitted stack traces.

This is the size of the per-thread cache.

### [`MEMORY_PROFILER_BACKTRACE_CACHE_SIZE_LEVEL_2`](https://koute.github.io/bytehound/configuration.html#memory_profiler_backtrace_cache_size_level_2)

_Default: `327680`_

Controls the size of the internal backtrace cache used to deduplicate emitted stack traces.

This is the size of the global cache.

### [`MEMORY_PROFILER_GATHER_MMAP_CALLS`](https://koute.github.io/bytehound/configuration.html#memory_profiler_gather_mmap_calls)

_Default: `0`_

Controls whenever the profiler will also gather calls to `mmap` and `munmap`.

(Those are _not_ treated as allocations and are only available under the `/mmaps` API endpoint.)

### [`MEMORY_PROFILER_USE_SHADOW_STACK`](https://koute.github.io/bytehound/configuration.html#memory_profiler_use_shadow_stack)

_Default: `1`_

Whenever to use a more intrusive, faster unwinding algorithm; enabled by default.

Setting it to `0` will on average significantly slow down unwinding. This option is provided only for debugging purposes.

### [`MEMORY_PROFILER_TRACK_CHILD_PROCESSES`](https://koute.github.io/bytehound/configuration.html#memory_profiler_track_child_processes)

_Default: `0`_

If set to `1`, bytehound will also track the memory allocations of child processes spawned by the profiled process. This only applies to child processes spawned by the common `fork()` + `exec()` combination.

Note that if you enable this, you should use a value with appropriates placeholders (like PID) in `MEMORY_PROFILER_OUTPUT`, so that the output filenames for the parent and child processes are different. Otherwise, they would overwrite each other's data.

[](https://koute.github.io/bytehound/common_issues.html "Previous chapter")[](https://koute.github.io/bytehound/api_reference.html "Next chapter")

[](https://koute.github.io/bytehound/common_issues.html "Previous chapter")[](https://koute.github.io/bytehound/api_reference.html "Next chapter")
