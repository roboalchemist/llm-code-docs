- 

    Libraries »
    wdm (0.2.0)

    »
    Index (M) »
    WDM
     » 
    Monitor

# 

    Inherits:

      Object

          Object

- WDM::Monitor

        show all

    Defined in:
    ext/wdm/rb_monitor.c

## 

- 

      #**run!**  ⇒ Object 

- 

      #**stop**  ⇒ Object 

- 

      #**watch**(*args)  ⇒ Object 

- 

      #**watch_recursively**(*args)  ⇒ Object 

## 

### 

```

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
529
530
531
532
533
534
535
```

```
# File 'ext/wdm/rb_monitor.c', line 471

static VALUE
rb_monitor_run_bang(VALUE self)
{
    BOOL already_running,
         waiting_succeeded;
    WDM_PMonitor monitor;

    WDM_DEBUG("Running the monitor!");

    TypedData_Get_Struct(self, WDM_Monitor, &monitor_data_type, monitor);
    already_running = FALSE;

    EnterCriticalSection(&monitor->lock);
        if ( monitor->running ) {
            already_running = TRUE;
        }
        else {
            monitor->running = TRUE;
        }
    LeaveCriticalSection(&monitor->lock);

    if (already_running) {
        WDM_DEBUG("Not doing anything because the monitor is already running!");
        return Qnil;
    }

    // Reset events
    ResetEvent(monitor->process_event);
    ResetEvent(monitor->stop_event);

    monitor->monitoring_thread = CreateThread(
        NULL,                     // default security attributes
        0,                        // use default stack size
        start_monitoring,         // thread function name
        monitor,                  // argument to thread function
        0,                        // use default creation flags
        NULL                      // Ignore thread identifier
    );

    if ( monitor->monitoring_thread == NULL ) {
        rb_raise(eWDM_Error, "Can't create a thread for the monitor!");
    }

    while ( monitor->running ) {

        waiting_succeeded = (VALUE)rb_thread_call_without_gvl(wait_for_changes, monitor->process_event, stop_monitoring, monitor);

        if ( waiting_succeeded == Qfalse ) {
            rb_raise(eWDM_Error, "Failed while waiting for a change in the watched directories!");
        }

        if ( ! monitor->running ) {
            wdm_queue_empty(monitor->changes);
            return Qnil;
        }

        process_changes(monitor->changes);

        if ( ! ResetEvent(monitor->process_event) ) {
            rb_raise(eWDM_Error, "Couldn't reset system events to watch for changes!");
        }
    }

    return Qnil;
}

```

### 

```

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
```

```
# File 'ext/wdm/rb_monitor.c', line 537

static VALUE
rb_monitor_stop(VALUE self)
{
    WDM_PMonitor monitor;

    TypedData_Get_Struct(self, WDM_Monitor, &monitor_data_type, monitor);

    stop_monitoring(monitor);

    WDM_DEBUG("Stopped the monitor!");

    return Qnil;
}

```

### 

```

252
253
254
255
256
```

```
# File 'ext/wdm/rb_monitor.c', line 252

static VALUE
rb_monitor_watch(int argc, VALUE *argv, VALUE self)
{
    return combined_watch(FALSE, argc, argv, self);
}

```

### 

```

258
259
260
261
262
```

```
# File 'ext/wdm/rb_monitor.c', line 258

static VALUE
rb_monitor_watch_recursively(int argc, VALUE *argv, VALUE self)
{
    return combined_watch(TRUE, argc, argv, self);
}

```

  Generated on Fri Apr  3 08:38:54 2026 by
  yard
  0.9.38 (ruby-3.4.3).