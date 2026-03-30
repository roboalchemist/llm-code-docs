# _task Plugin Documentation

The _task plugin provides a framework for asynchronous task execution in ruTorrent.

## Overview

The _task plugin is a core infrastructure plugin that enables other plugins to run background tasks asynchronously.

## Features

- Background task execution
- Progress tracking
- Task cancellation support
- Error handling and reporting

## For Plugin Developers

### Creating a Task

```php
// In your plugin's init.php
$theTask = rTask::create($owner, [
    'callee'   => [$this, 'doWork'],
    'interval' => 1,
    'timeout'  => 60,
]);
```

### Task Lifecycle

| Phase | Description |
|-------|-------------|
| Created | Task instance created |
| Running | Task is executing |
| Completed | Task finished successfully |
| Failed | Task encountered an error |
| Cancelled | Task was manually cancelled |

## Configuration

Edit `plugins/_task/conf.php`:

```php
<?php
// Maximum concurrent tasks
$maxConcurrentTasks = 10;

// Task timeout (seconds)
$defaultTimeout = 300;
?>
```
