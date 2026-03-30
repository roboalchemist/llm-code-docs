# Source: https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html

Title: Multitasking and Background Operations | Terminal.Gui v2

URL Source: https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html

Markdown Content:
_See also [Cross-platform Driver Model](https://gui-cs.github.io/Terminal.Gui/docs/drivers.html)_

Terminal.Gui applications run on a single main thread with an event loop that processes keyboard, mouse, and system events. This document explains how to properly handle background work, timers, and asynchronous operations while keeping your UI responsive.

Threading Model[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#threading-model)
-----------------------------------------------------------------------------------------------

Terminal.Gui follows the standard UI toolkit pattern where **all UI operations must happen on the main thread**. Attempting to modify views or their properties from background threads will result in undefined behavior and potential crashes.

### The Golden Rule[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#the-golden-rule)

> Always use `App?.Invoke()` (from within a View) or `app.Invoke()` (with an IApplication instance) to update the UI from background threads.

Background Operations[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#background-operations)
-----------------------------------------------------------------------------------------------------------

### Using async/await (Recommended)[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#using-asyncawait-recommended)

The preferred way to handle background work is using C#'s async/await pattern:

```
private async void LoadDataButton_Clicked()
{
    loadButton.Enabled = false;
    statusLabel.Text = "Loading...";
    
    try
    {
        // This runs on a background thread
        var data = await FetchDataFromApiAsync();
        
        // This automatically returns to the main thread
        dataView.LoadData(data);
        statusLabel.Text = $"Loaded {data.Count} items";
    }
    catch (Exception ex)
    {
        statusLabel.Text = $"Error: {ex.Message}";
    }
    finally
    {
        loadButton.Enabled = true;
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")

### Using Application.Invoke()[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#using-applicationinvoke)

When working with traditional threading APIs or when async/await isn't suitable:

**From within a View (recommended):**

```
private void StartBackgroundWork()
{
    Task.Run(() =>
    {
        // This code runs on a background thread
        for (int i = 0; i <= 100; i++)
        {
            Thread.Sleep(50); // Simulate work
            
            // Marshal back to main thread for UI updates
            App?.Invoke(() =>
            {
                progressBar.Fraction = i / 100f;
                statusLabel.Text = $"Progress: {i}%";
            });
        }
        
        App?.Invoke(() =>
        {
            statusLabel.Text = "Complete!";
        });
    });
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")
**Using IApplication instance:**

```
private void StartBackgroundWork(IApplication app)
{
    Task.Run(() =>
    {
        // This code runs on a background thread
        for (int i = 0; i <= 100; i++)
        {
            Thread.Sleep(50); // Simulate work
            
            // Marshal back to main thread for UI updates
            app.Invoke(() =>
            {
                progressBar.Fraction = i / 100f;
                statusLabel.Text = $"Progress: {i}%";
            });
        }
        
        app.Invoke(() =>
        {
            statusLabel.Text = "Complete!";
        });
    });
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")
Timers[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#timers)
-----------------------------------------------------------------------------

Use timers for periodic updates like clocks, status refreshes, or animations:

```
public class ClockView : View
{
    private Label timeLabel;
    private object timerToken;
    
    public ClockView()
    {
        timeLabel = new Label { Text = DateTime.Now.ToString("HH:mm:ss") };
        Add(timeLabel);
        
        // Update every second using the View's App property
        timerToken = App?.AddTimeout(
            TimeSpan.FromSeconds(1), 
            UpdateTime
        );
    }
    
    private bool UpdateTime()
    {
        timeLabel.Text = DateTime.Now.ToString("HH:mm:ss");
        return true; // Continue timer
    }
    
    protected override void Dispose(bool disposing)
    {
        if (disposing && timerToken != null)
        {
            App?.RemoveTimeout(timerToken);
        }
        base.Dispose(disposing);
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")

### Timer Best Practices[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#timer-best-practices)

* **Always remove timers** when disposing views to prevent memory leaks
* **Return `true`** from timer callbacks to continue, `false` to stop
* **Keep timer callbacks fast** - they run on the main thread
* **Use appropriate intervals** - too frequent updates can impact performance

Common Patterns[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#common-patterns)
-----------------------------------------------------------------------------------------------

### Progress Reporting[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#progress-reporting)

```
private async void ProcessFiles()
{
    var files = Directory.GetFiles(folderPath);
    progressBar.Fraction = 0;
    
    for (int i = 0; i < files.Length; i++)
    {
        await ProcessFileAsync(files[i]);
        
        // Update progress on main thread
        progressBar.Fraction = (float)(i + 1) / files.Length;
        statusLabel.Text = $"Processed {i + 1} of {files.Length} files";
        
        // Allow UI to update
        await Task.Yield();
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")

### Cancellation Support[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#cancellation-support)

```
private CancellationTokenSource cancellationSource;

private async void StartLongOperation()
{
    cancellationSource = new CancellationTokenSource();
    cancelButton.Enabled = true;
    
    try
    {
        await LongRunningOperationAsync(cancellationSource.Token);
        statusLabel.Text = "Operation completed";
    }
    catch (OperationCanceledException)
    {
        statusLabel.Text = "Operation cancelled";
    }
    finally
    {
        cancelButton.Enabled = false;
    }
}

private void CancelButton_Clicked()
{
    cancellationSource?.Cancel();
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")

### Responsive UI During Blocking Operations[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#responsive-ui-during-blocking-operations)

```
private async void ProcessLargeDataset()
{
    var data = GetLargeDataset();
    var batchSize = 100;
    
    for (int i = 0; i < data.Count; i += batchSize)
    {
        // Process a batch
        var batch = data.Skip(i).Take(batchSize);
        ProcessBatch(batch);
        
        // Update UI and yield control
        progressBar.Fraction = (float)i / data.Count;
        await Task.Yield(); // Allows UI events to process
    }
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")
Common Mistakes to Avoid[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#common-mistakes-to-avoid)
-----------------------------------------------------------------------------------------------------------------

### ❌ Don't: Update UI from background threads[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#-dont-update-ui-from-background-threads)

```
Task.Run(() =>
{
    label.Text = "This will crash!"; // Wrong!
});
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")

### ✅ Do: Use App.Invoke() or app.Invoke()[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#-do-use-appinvoke-or-appinvoke)

```
Task.Run(() =>
{
    // From within a View:
    App?.Invoke(() =>
    {
        label.Text = "This is safe!"; // Correct!
    });
    
    // Or with IApplication instance:
    // app.Invoke(() => { label.Text = "This is safe!"; });
});
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")

### ❌ Don't: Forget to clean up timers[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#-dont-forget-to-clean-up-timers)

```
// Memory leak - timer keeps running after view is disposed
// From within a View:
App?.AddTimeout(TimeSpan.FromSeconds(1), UpdateStatus);

// Or with IApplication instance:
app.AddTimeout(TimeSpan.FromSeconds(1), UpdateStatus);
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")

### ✅ Do: Remove timers in Dispose[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#-do-remove-timers-in-dispose)

```
protected override void Dispose(bool disposing)
{
    if (disposing && timerToken != null)
    {
        // From within a View, use App property
        App?.RemoveTimeout(timerToken);
        
        // Or with IApplication instance:
        // app.RemoveTimeout(timerToken);
    }
    base.Dispose(disposing);
}
```

[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html# "Copy")
Performance Considerations[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#performance-considerations)
---------------------------------------------------------------------------------------------------------------------

* **Batch UI updates** when possible instead of updating individual elements
* **Use appropriate timer intervals** - 100ms is usually the maximum useful rate
* **Yield control** in long-running operations with `await Task.Yield()`
* **Consider using `ConfigureAwait(false)`** for non-UI async operations
* **Profile your application** to identify performance bottlenecks

See Also[](https://gui-cs.github.io/Terminal.Gui/docs/multitasking.html#see-also)
---------------------------------------------------------------------------------

* [Events](https://gui-cs.github.io/Terminal.Gui/docs/events.html) - Event handling patterns
* [Keyboard Input](https://gui-cs.github.io/Terminal.Gui/docs/keyboard.html) - Keyboard event processing
* [Mouse Input](https://gui-cs.github.io/Terminal.Gui/docs/mouse.html) - Mouse event handling
* [Configuration Management](https://gui-cs.github.io/Terminal.Gui/docs/config.html) - Application settings and state
