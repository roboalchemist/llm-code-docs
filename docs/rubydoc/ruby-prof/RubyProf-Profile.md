# Class: RubyProf::Profile
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RubyProf::Profile
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    ext/ruby_prof/rp_profile.c,

  lib/ruby-prof/profile.rb,
 ext/ruby_prof/rp_profile.c

  
  

## Overview

  
    

The Profile class represents a single profiling run and provides the main API for using ruby-prof.

```
After creating a Profile instance, start profiling code by calling the Profile#start method. To finish profiling,
call Profile#stop. Once profiling is completed, the Profile instance contains the results.

  profile = RubyProf::Profile.new
  profile.start
  ...
  result = profile.stop

Alternatively, you can use the block syntax:

  profile = RubyProf::Profile.profile do
    ...
  end

```

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**profile**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq:   profile(&block) -> RubyProf::Profile   profile(options, &block) -> RubyProf::Profile.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**_dump_data**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**_load_data**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**add_thread**(thread)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Adds the specified RubyProf thread to the profile.

  

      
        
- 
  
    
      #**exclude_common_methods!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Hides methods that, when represented as a call graph, have extremely large in and out degrees and make navigation impossible.

  

      
        
- 
  
    
      #**exclude_method!**  ⇒ self 
    

    
  
  
  
  
  
  
  
  

  
    

Excludes the method from profiling results.

  

      
        
- 
  
    
      #**exclude_methods!**(mod, *method_names)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**exclude_singleton_methods!**(mod, *method_names)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(*args)  ⇒ Object 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Returns a new profiler.

  

      
        
- 
  
    
      #**mode**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the measure mode used in this profile.

  

      
        
- 
  
    
      #**measure_mode_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**measure_mode_string**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**merge!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq: merge! -> self.

  

      
        
- 
  
    
      #**pause**  ⇒ self 
    

    
  
  
  
  
  
  
  
  

  
    

Pauses collecting profile data.

  

      
        
- 
  
    
      #**paused?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns whether a profile is currently paused.

  

      
        
- 
  
    
      #**profile**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

call-seq:   profile(&block) -> self.

  

      
        
- 
  
    
      #**remove_thread**(thread)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Removes the specified thread from the profile.

  

      
        
- 
  
    
      #**resume**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Resumes recording profile data.

  

      
        
- 
  
    
      #**running?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns whether a profile is currently running.

  

      
        
- 
  
    
      #**start**  ⇒ self 
    

    
  
  
  
  
  
  
  
  

  
    

Starts recording profile data.

  

      
        
- 
  
    
      #**stop**  ⇒ self 
    

    
  
  
  
  
  
  
  
  

  
    

Stops collecting profile data.

  

      
        
- 
  
    
      #**threads**  ⇒ Array of RubyProf::Thread 
    

    
  
  
  
  
  
  
  
  

  
    

Returns an array of RubyProf::Thread instances that were profiled.

  

      
        
- 
  
    
      #**track_allocations**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns if object allocations were tracked in this profile.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    
      #**new**  ⇒ Object 
    
      #**new**(keyword_args)  ⇒ Object 
    
  

  

  

  
    

Returns a new profiler. Possible keyword arguments include:

```
measure_mode:      Measure mode. Specifies the profile measure mode.
                   If not specified, defaults to RubyProf::WALL_TIME.
allow_exceptions:  Whether to raise exceptions encountered during profiling,
                   or to suppress all exceptions during profiling
track_allocations: Whether to track object allocations while profiling. True or false.
exclude_common:    Exclude common methods from the profile. True or false.
exclude_threads:   Threads to exclude from the profiling results.
include_threads:   Focus profiling on only the given threads. This will ignore
                   all other threads.

```

  

  

  
    
      

```

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
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 534

static VALUE prof_initialize(int argc, VALUE* argv, VALUE self)
{
    VALUE keywords;
    rb_scan_args_kw(RB_SCAN_ARGS_KEYWORDS, argc, argv, ":", &keywords);

    ID table[] = {rb_intern("measure_mode"),
                  rb_intern("track_allocations"),
                  rb_intern("allow_exceptions"),
                  rb_intern("exclude_common"),
                  rb_intern("exclude_threads"),
                  rb_intern("include_threads") };
    VALUE values[6];
    rb_get_kwargs(keywords, table, 0, 6, values);

    VALUE mode = values[0] == Qundef ? INT2NUM(MEASURE_WALL_TIME) : values[0];
    VALUE track_allocations = values[1] == Qtrue ? Qtrue : Qfalse;
    VALUE allow_exceptions = values[2] == Qtrue ? Qtrue : Qfalse;
    VALUE exclude_common = values[3] == Qtrue ? Qtrue : Qfalse;
    VALUE exclude_threads = values[4];
    VALUE include_threads = values[5];

    Check_Type(mode, T_FIXNUM);
    prof_profile_t* profile = prof_get_profile(self);
    profile->measurer = prof_measurer_create(NUM2INT(mode), RB_TEST(track_allocations));
    profile->allow_exceptions = RB_TEST(allow_exceptions);

    if (exclude_threads != Qundef)
    {
        Check_Type(exclude_threads, T_ARRAY);
        assert(profile->exclude_threads_tbl == NULL);
        profile->exclude_threads_tbl = threads_table_create();
        for (int i = 0; i < RARRAY_LEN(exclude_threads); i++)
        {
            VALUE thread = rb_ary_entry(exclude_threads, i);
            rb_st_insert(profile->exclude_threads_tbl, thread, Qtrue);
        }
    }

    if (include_threads != Qundef)
    {
        Check_Type(include_threads, T_ARRAY);
        assert(profile->include_threads_tbl == NULL);
        profile->include_threads_tbl = threads_table_create();
        for (int i = 0; i < RARRAY_LEN(include_threads); i++)
        {
            VALUE thread = rb_ary_entry(include_threads, i);
            rb_st_insert(profile->include_threads_tbl, thread, Qtrue);
        }
    }

    if (RB_TEST(exclude_common))
    {
        prof_exclude_common_methods(self);
    }

    return self;
}

```

    
  

  

  
    
## Class Method Details

    
      
  
### 
  
    .**profile**(*args)  ⇒ Object 
  

  

  

  
    

call-seq:

```
profile(&block) -> RubyProf::Profile
profile(options, &block) -> RubyProf::Profile

Profiles the specified block and returns a RubyProf::Profile
object. Arguments are passed to Profile initialize method.

  profile = RubyProf::Profile.profile do
    ..
  end

```

  

  

  
    
      

```

842
843
844
845
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 842

static VALUE prof_profile_class(int argc, VALUE* argv, VALUE klass)
{
    return prof_profile_instance(rb_class_new_instance(argc, argv, cProfile));
}

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**_dump_data**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

874
875
876
877
878
879
880
881
882
883
884
885
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 874

VALUE prof_profile_dump(VALUE self)
{
    prof_profile_t* profile = prof_get_profile(self);
  
    VALUE result = rb_hash_new();
    rb_hash_aset(result, ID2SYM(rb_intern("threads")), prof_threads(self));
    rb_hash_aset(result, ID2SYM(rb_intern("measurer_mode")), INT2NUM(profile->measurer->mode));
    rb_hash_aset(result, ID2SYM(rb_intern("measurer_track_allocations")), 
                 profile->measurer->track_allocations ? Qtrue : Qfalse);

    return result;
}

```

    
  

    
      
  
### 
  
    #**_load_data**(data)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 888

VALUE prof_profile_load(VALUE self, VALUE data)
{
    prof_profile_t* profile = prof_get_profile(self);

    VALUE measurer_mode = rb_hash_aref(data, ID2SYM(rb_intern("measurer_mode")));
    VALUE measurer_track_allocations = rb_hash_aref(data, ID2SYM(rb_intern("measurer_track_allocations")));
    profile->measurer = prof_measurer_create((prof_measure_mode_t)(NUM2INT(measurer_mode)),
                                              measurer_track_allocations == Qtrue ? true : false);

    VALUE threads = rb_hash_aref(data, ID2SYM(rb_intern("threads")));
    for (int i = 0; i < rb_array_len(threads); i++)
    {
        VALUE thread = rb_ary_entry(threads, i);
        thread_data_t* thread_data = prof_get_thread(thread);
        rb_st_insert(profile->threads_tbl, (st_data_t)thread_data->fiber_id, (st_data_t)thread_data);
    }

    return data;
}

```

    
  

    
      
  
### 
  
    #**add_thread**(thread)  ⇒ Object 
  

  

  

  
    

Adds the specified RubyProf thread to the profile.

  

  
  

  
    
      

```

771
772
773
774
775
776
777
778
779
780
781
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 771

static VALUE prof_add_thread(VALUE self, VALUE thread)
{
  prof_profile_t* profile_ptr = prof_get_profile(self);

  // This thread is now going to be owned by C
  thread_data_t* thread_ptr = prof_get_thread(thread);
  thread_ptr->owner = OWNER_C;

  rb_st_insert(profile_ptr->threads_tbl, thread_ptr->fiber_id, (st_data_t)thread_ptr);
  return thread;
}

```

    
  

    
      
  
### 
  
    #**exclude_common_methods!**  ⇒ Object 
  

  

  

  
    

Hides methods that, when represented as a call graph, have extremely large in and out degrees and make navigation impossible.

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/ruby-prof/profile.rb', line 35

def exclude_common_methods!
  ExcludeCommonMethods.apply!(self)
end

```

    
  

    
      
  
### 
  
    #**exclude_method!**  ⇒ self 
  

  

  

  
    

Excludes the method from profiling results.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (self)
      
      
      
    
  

  
    
      

```

852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 852

static VALUE prof_exclude_method(VALUE self, VALUE klass, VALUE msym)
{
    prof_profile_t* profile = prof_get_profile(self);

    if (profile->running == Qtrue)
    {
        rb_raise(rb_eRuntimeError, "RubyProf.start was already called");
    }

    st_data_t key = method_key(klass, msym);
    prof_method_t* method = method_table_lookup(profile->exclude_methods_tbl, key);

    if (!method)
    {
        method = prof_method_create(profile, klass, msym, Qnil, 0);
        method_table_insert(profile->exclude_methods_tbl, method->key, method);
    }

    return self;
}

```

    
  

    
      
  
### 
  
    #**exclude_methods!**(mod, *method_names)  ⇒ Object 
  

  

  

  
    
      

```

39
40
41
42
43
```

    
    
      

```
# File 'lib/ruby-prof/profile.rb', line 39

def exclude_methods!(mod, *method_names)
  [method_names].flatten.each do |method_name|
    exclude_method!(mod, method_name)
  end
end

```

    
  

    
      
  
### 
  
    #**exclude_singleton_methods!**(mod, *method_names)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/ruby-prof/profile.rb', line 45

def exclude_singleton_methods!(mod, *method_names)
  exclude_methods!(mod.singleton_class, *method_names)
end

```

    
  

    
      
  
### 
  
    #**mode**  ⇒ Object 
  

  

  

  
    

Returns the measure mode used in this profile.

  

  
  

  
    
      

```

617
618
619
620
621
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 617

static VALUE prof_profile_measure_mode(VALUE self)
{
    prof_profile_t* profile = prof_get_profile(self);
    return INT2NUM(profile->measurer->mode);
}

```

    
  

    
      
  
### 
  
    #**measure_mode_name**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
24
25
26
27
28
29
30
31
```

    
    
      

```
# File 'lib/ruby-prof/profile.rb', line 20

def measure_mode_name
  case self.measure_mode
    when WALL_TIME
      "Wall Time"
    when PROCESS_TIME
      "Process Time"
    when ALLOCATIONS
      "Allocations"
    when MEMORY
      "Memory"
  end
end

```

    
  

    
      
  
### 
  
    #**measure_mode_string**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
11
12
13
14
15
16
17
18
```

    
    
      

```
# File 'lib/ruby-prof/profile.rb', line 7

def measure_mode_string
  case self.measure_mode
    when WALL_TIME
      "wall_time"
    when PROCESS_TIME
      "process_time"
    when ALLOCATIONS
      "allocations"
    when MEMORY
      "memory"
  end
end

```

    
  

    
      
  
### 
  
    #**merge!**  ⇒ Object 
  

  

  

  
    

call-seq: merge! -> self

Merges RubyProf threads whose root call_trees reference the same target method. This is useful when profiling code that uses a main thread/fiber to distribute work to multiple workers. If there are tens or hundreds of workers, viewing results per worker thread/fiber can be overwhelming. Using `merge!` will combine the worker times together into one result.

Note the reported time will be much greater than the actual wall time. For example, if there are 10 workers that each run for 5 seconds, merged results will show one thread that ran for 50 seconds.

  

  

  
    
      

```

61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
```

    
    
      

```
# File 'lib/ruby-prof/profile.rb', line 61

def merge!
  # First group threads by their root call tree target (method). If the methods are
  # different than there is nothing to merge
  grouped = threads.group_by do |thread|
    thread.call_tree.target
  end

  # For each target, get the first thread. Then loop over the remaining threads,
  # and merge them into the first one and ten delete them. So we will be left with
  # one thread per target.
  grouped.each do |target, threads|
    thread = threads.shift
    threads.each do |other_thread|
      thread.merge!(other_thread)
      remove_thread(other_thread)
    end
    thread
  end

  self
end

```

    
  

    
      
  
### 
  
    #**pause**  ⇒ self 
  

  

  

  
    

Pauses collecting profile data.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (self)
      
      
      
    
  

  
    
      

```

679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 679

static VALUE prof_pause(VALUE self)
{
    prof_profile_t* profile = prof_get_profile(self);
    if (profile->running == Qfalse)
    {
        rb_raise(rb_eRuntimeError, "RubyProf is not running.");
    }

    if (profile->paused == Qfalse)
    {
        profile->paused = Qtrue;
        profile->measurement_at_pause_resume = prof_measure(profile->measurer, NULL);
        rb_st_foreach(profile->threads_tbl, pause_thread, (st_data_t)profile);
    }

    return self;
}

```

    
  

    
      
  
### 
  
    #**paused?**  ⇒ Boolean 
  

  

  

  
    

Returns whether a profile is currently paused.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

596
597
598
599
600
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 596

static VALUE prof_paused(VALUE self)
{
    prof_profile_t* profile = prof_get_profile(self);
    return profile->paused;
}

```

    
  

    
      
  
### 
  
    #**profile**  ⇒ Object 
  

  

  

  
    

call-seq:

```
profile(&block) -> self

Profiles the specified block.

  profile = RubyProf::Profile.new
  profile.profile do
    ..
  end

```

  

  

  
    
      

```

808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 808

static VALUE prof_profile_instance(VALUE self)
{
    int result;
    prof_profile_t* profile = prof_get_profile(self);

    if (!rb_block_given_p())
    {
        rb_raise(rb_eArgError, "A block must be provided to the profile method.");
    }

    prof_start(self);
    rb_protect(rb_yield, self, &result);
    self = prof_stop(self);

    if (profile->allow_exceptions && result != 0)
    {
        rb_jump_tag(result);
    }

    return self;
}

```

    
  

    
      
  
### 
  
    #**remove_thread**(thread)  ⇒ Object 
  

  

  

  
    

Removes the specified thread from the profile. This is used to remove threads after they have been merged togher. Retuns the removed thread.

  

  
  

  
    
      

```

788
789
790
791
792
793
794
795
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 788

static VALUE prof_remove_thread(VALUE self, VALUE thread)
{
  prof_profile_t* profile_ptr = prof_get_profile(self);
  thread_data_t* thread_ptr = prof_get_thread(thread);
  VALUE fiber_id = thread_ptr->fiber_id;
  rb_st_delete(profile_ptr->threads_tbl, (st_data_t*)&fiber_id, NULL);
  return thread;
}

```

    
  

    
      
  
### 
  
    
      #**resume**  ⇒ self 
    
      #**resume**(&block)  ⇒ self 
    
  

  

  

  
    

Resumes recording profile data.

  

  
  

Overloads:
  

    
      
      
- 
        #**resume**  ⇒ self 
        
  
    

  

  

Returns:

  
    
  - 
      
      
        (self)
      
      
      
    
  

      
    
      
      
- 
        #**resume**(&block)  ⇒ self 
        
  
    

  

  

Returns:

  
    
  - 
      
      
        (self)
      
      
      
    
  

      
    
  

  
    
      

```

702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 702

static VALUE prof_resume(VALUE self)
{
    prof_profile_t* profile = prof_get_profile(self);
    if (profile->running == Qfalse)
    {
        rb_raise(rb_eRuntimeError, "RubyProf is not running.");
    }

    if (profile->paused == Qtrue)
    {
        profile->paused = Qfalse;
        profile->measurement_at_pause_resume = prof_measure(profile->measurer, NULL);
        rb_st_foreach(profile->threads_tbl, unpause_thread, (st_data_t)profile);
    }

    return rb_block_given_p() ? rb_ensure(rb_yield, self, prof_pause, self) : self;
}

```

    
  

    
      
  
### 
  
    #**running?**  ⇒ Boolean 
  

  

  

  
    

Returns whether a profile is currently running.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

606
607
608
609
610
611
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 606

static VALUE
prof_running(VALUE self)
{
    prof_profile_t* profile = prof_get_profile(self);
    return profile->running;
}

```

    
  

    
      
  
### 
  
    #**start**  ⇒ self 
  

  

  

  
    

Starts recording profile data.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (self)
      
      
      
    
  

  
    
      

```

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
667
668
669
670
671
672
673
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 637

static VALUE prof_start(VALUE self)
{
    char* trace_file_name;

    prof_profile_t* profile = prof_get_profile(self);

    if (profile->running == Qtrue)
    {
        rb_raise(rb_eRuntimeError, "RubyProf.start was already called");
    }

    profile->running = Qtrue;
    profile->paused = Qfalse;
    profile->last_thread_data = threads_table_insert(profile, rb_fiber_current());

    /* open trace file if environment wants it */
    trace_file_name = getenv("RUBY_PROF_TRACE");

    if (trace_file_name != NULL)
    {
        if (strcmp(trace_file_name, "stdout") == 0)
        {
            trace_file = stdout;
        }
        else if (strcmp(trace_file_name, "stderr") == 0)
        {
            trace_file = stderr;
        }
        else
        {
            trace_file = fopen(trace_file_name, "w");
        }
    }

    prof_install_hook(self);
    return self;
}

```

    
  

    
      
  
### 
  
    #**stop**  ⇒ self 
  

  

  

  
    

Stops collecting profile data.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (self)
      
      
      
    
  

  
    
      

```

724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 724

static VALUE prof_stop(VALUE self)
{
    prof_profile_t* profile = prof_get_profile(self);

    if (profile->running == Qfalse)
    {
        rb_raise(rb_eRuntimeError, "RubyProf.start was not yet called");
    }

    prof_remove_hook(self);

    /* close trace file if open */
    if (trace_file != NULL)
    {
        if (trace_file != stderr && trace_file != stdout)
        {
            fclose(trace_file);
        }
        trace_file = NULL;
    }

    prof_stop_threads(profile);

    /* Unset the last_thread_data (very important!)
       and the threads table */
    profile->running = profile->paused = Qfalse;
    profile->last_thread_data = NULL;

    return self;
}

```

    
  

    
      
  
### 
  
    #**threads**  ⇒ Array of RubyProf::Thread 
  

  

  

  
    

Returns an array of RubyProf::Thread instances that were profiled.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Array of RubyProf::Thread)
      
      
      
    
  

  
    
      

```

759
760
761
762
763
764
765
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 759

static VALUE prof_threads(VALUE self)
{
    VALUE result = rb_ary_new();
    prof_profile_t* profile = prof_get_profile(self);
    rb_st_foreach(profile->threads_tbl, collect_threads, result);
    return result;
}

```

    
  

    
      
  
### 
  
    #**track_allocations**  ⇒ Boolean 
  

  

  

  
    

Returns if object allocations were tracked in this profile.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

627
628
629
630
631
```

    
    
      

```
# File 'ext/ruby_prof/rp_profile.c', line 627

static VALUE prof_profile_track_allocations(VALUE self)
{
    prof_profile_t* profile = prof_get_profile(self);
    return profile->measurer->track_allocations ? Qtrue : Qfalse;
}

```