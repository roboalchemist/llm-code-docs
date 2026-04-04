# Source: https://developers.cloudflare.com/sandbox/guides/file-watching/index.md

---

title: Watch filesystem changes · Cloudflare Sandbox SDK docs
description: Monitor files and directories in real-time to build responsive
  development tools and automation workflows.
lastUpdated: 2026-02-06T17:10:29.000Z
chatbotDeprioritize: false
source_url:
  html: https://developers.cloudflare.com/sandbox/guides/file-watching/
  md: https://developers.cloudflare.com/sandbox/guides/file-watching/index.md
---

This guide shows you how to monitor filesystem changes in real-time using the Sandbox SDK's file watching capabilities. File watching is essential for building development tools, automated workflows, and responsive applications that react to file system changes.

## Basic file watching

Start by watching a directory for any changes:

* JavaScript

  ```js
  const watcher = await sandbox.watch("/workspace/src", {
    onEvent: (event) => {
      console.log(`${event.type} event: ${event.path}`);
      console.log(`Is directory: ${event.isDirectory}`);
    },
    onError: (error) => {
      console.error("Watch failed:", error.message);
    },
  });


  // Always clean up when done
  process.on("exit", () => watcher.stop());
  ```

* TypeScript

  ```ts
  const watcher = await sandbox.watch('/workspace/src', {
    onEvent: (event) => {
      console.log(`${event.type} event: ${event.path}`);
      console.log(`Is directory: ${event.isDirectory}`);
    },
    onError: (error) => {
      console.error('Watch failed:', error.message);
    }
  });


  // Always clean up when done
  process.on('exit', () => watcher.stop());
  ```

The watcher will detect four types of events:

* **create** - Files or directories created
* **modify** - File content or attributes changed
* **delete** - Files or directories removed
* **rename** - Files or directories moved/renamed

## Filter by file type

Use `include` patterns to watch only specific file types:

* JavaScript

  ```js
  // Only watch TypeScript and JavaScript files
  const watcher = await sandbox.watch("/workspace/src", {
    include: ["*.ts", "*.tsx", "*.js", "*.jsx"],
    onEvent: (event) => {
      console.log(`${event.type}: ${event.path}`);
    },
  });
  ```

* TypeScript

  ```ts
  // Only watch TypeScript and JavaScript files
  const watcher = await sandbox.watch('/workspace/src', {
    include: ['*.ts', '*.tsx', '*.js', '*.jsx'],
    onEvent: (event) => {
      console.log(`${event.type}: ${event.path}`);
    }
  });
  ```

Common include patterns:

* `*.ts` - TypeScript files
* `*.js` - JavaScript files
* `*.json` - JSON configuration files
* `*.md` - Markdown documentation
* `package*.json` - Package files specifically

## Exclude directories

Use `exclude` patterns to ignore certain directories or files:

* JavaScript

  ```js
  const watcher = await sandbox.watch("/workspace", {
    exclude: [
      "node_modules", // Dependencies
      "dist", // Build output
      "*.log", // Log files
      ".git", // Git metadata (excluded by default)
      "*.tmp", // Temporary files
    ],
    onEvent: (event) => {
      console.log(`Change detected: ${event.path}`);
    },
  });
  ```

* TypeScript

  ```ts
  const watcher = await sandbox.watch('/workspace', {
    exclude: [
      'node_modules',    // Dependencies
      'dist',           // Build output
      '*.log',          // Log files
      '.git',           // Git metadata (excluded by default)
      '*.tmp'           // Temporary files
    ],
    onEvent: (event) => {
      console.log(`Change detected: ${event.path}`);
    }
  });
  ```

Default exclusions

The following patterns are excluded by default: `.git`, `node_modules`, `.DS_Store`. You can override this by providing your own `exclude` array.

## Build responsive development tools

### Auto-restarting development server

Build a development server that automatically restarts when source files change:

* JavaScript

  ```js
  let serverProcess = null;


  async function startServer() {
    if (serverProcess) {
      await serverProcess.stop();
    }


    console.log("Starting development server...");
    serverProcess = await sandbox.startProcess("npm run dev", {
      onOutput: (stream, data) => {
        console.log(`[server] ${data}`);
      },
    });
  }


  const watcher = await sandbox.watch("/workspace/src", {
    include: ["*.ts", "*.js", "*.json"],
    onEvent: async (event) => {
      if (event.type === "modify") {
        console.log(`Detected change in ${event.path}, restarting server...`);
        await startServer();
      }
    },
  });


  // Initial server start
  await startServer();
  ```

* TypeScript

  ```ts
  let serverProcess: { stop: () => Promise<void> } | null = null;


  async function startServer() {
    if (serverProcess) {
      await serverProcess.stop();
    }


    console.log('Starting development server...');
    serverProcess = await sandbox.startProcess('npm run dev', {
      onOutput: (stream, data) => {
        console.log(`[server] ${data}`);
      }
    });
  }


  const watcher = await sandbox.watch('/workspace/src', {
    include: ['*.ts', '*.js', '*.json'],
    onEvent: async (event) => {
      if (event.type === 'modify') {
        console.log(`Detected change in ${event.path}, restarting server...`);
        await startServer();
      }
    }
  });


  // Initial server start
  await startServer();
  ```

### Auto-building on changes

Trigger builds automatically when source files are modified:

* JavaScript

  ```js
  let buildInProgress = false;


  const watcher = await sandbox.watch("/workspace/src", {
    include: ["*.ts", "*.tsx"],
    onEvent: async (event) => {
      if (event.type === "modify" && !buildInProgress) {
        buildInProgress = true;
        console.log("Building TypeScript project...");


        try {
          const result = await sandbox.exec("npm run build");
          if (result.success) {
            console.log("Build completed successfully");
          } else {
            console.error("Build failed:", result.stderr);
          }
        } catch (error) {
          console.error("Build error:", error);
        } finally {
          buildInProgress = false;
        }
      }
    },
  });
  ```

* TypeScript

  ```ts
  let buildInProgress = false;


  const watcher = await sandbox.watch('/workspace/src', {
    include: ['*.ts', '*.tsx'],
    onEvent: async (event) => {
      if (event.type === 'modify' && !buildInProgress) {
        buildInProgress = true;
        console.log('Building TypeScript project...');


        try {
          const result = await sandbox.exec('npm run build');
          if (result.success) {
            console.log('Build completed successfully');
          } else {
            console.error('Build failed:', result.stderr);
          }
        } catch (error) {
          console.error('Build error:', error);
        } finally {
          buildInProgress = false;
        }
      }
    }
  });
  ```

### Live documentation updates

Watch documentation files and rebuild docs when they change:

* JavaScript

  ```js
  const watcher = await sandbox.watch("/workspace/docs", {
    include: ["*.md", "*.mdx"],
    onEvent: async (event) => {
      if (event.type === "modify") {
        console.log(`Documentation updated: ${event.path}`);


        // Rebuild documentation site
        const result = await sandbox.exec("npm run build:docs");
        if (result.success) {
          console.log("Documentation rebuilt");
        }
      }
    },
  });
  ```

* TypeScript

  ```ts
  const watcher = await sandbox.watch('/workspace/docs', {
    include: ['*.md', '*.mdx'],
    onEvent: async (event) => {
      if (event.type === 'modify') {
        console.log(`Documentation updated: ${event.path}`);


        // Rebuild documentation site
        const result = await sandbox.exec('npm run build:docs');
        if (result.success) {
          console.log('Documentation rebuilt');
        }
      }
    }
  });
  ```

## Advanced patterns

### Debounced file operations

Avoid excessive operations by debouncing rapid file changes:

* JavaScript

  ```js
  let debounceTimeout = null;
  const changedFiles = new Set();


  const watcher = await sandbox.watch("/workspace/src", {
    onEvent: (event) => {
      changedFiles.add(event.path);


      // Clear existing timeout
      if (debounceTimeout) {
        clearTimeout(debounceTimeout);
      }


      // Set new timeout to process changes
      debounceTimeout = setTimeout(async () => {
        console.log(`Processing ${changedFiles.size} changed files...`);


        // Process all accumulated changes
        for (const filePath of changedFiles) {
          await processFile(filePath);
        }


        changedFiles.clear();
        debounceTimeout = null;
      }, 1000); // Wait 1 second after last change
    },
  });


  async function processFile(filePath) {
    // Your file processing logic
    console.log(`Processing ${filePath}`);
  }
  ```

* TypeScript

  ```ts
  let debounceTimeout: NodeJS.Timeout | null = null;
  const changedFiles = new Set<string>();


  const watcher = await sandbox.watch('/workspace/src', {
    onEvent: (event) => {
      changedFiles.add(event.path);


      // Clear existing timeout
      if (debounceTimeout) {
        clearTimeout(debounceTimeout);
      }


      // Set new timeout to process changes
      debounceTimeout = setTimeout(async () => {
        console.log(`Processing ${changedFiles.size} changed files...`);


        // Process all accumulated changes
        for (const filePath of changedFiles) {
          await processFile(filePath);
        }


        changedFiles.clear();
        debounceTimeout = null;
      }, 1000); // Wait 1 second after last change
    }
  });


  async function processFile(filePath: string) {
    // Your file processing logic
    console.log(`Processing ${filePath}`);
  }
  ```

### Multi-directory watching

Watch multiple directories with different configurations:

* JavaScript

  ```js
  // Watch source code for builds
  const srcWatcher = await sandbox.watch("/workspace/src", {
    include: ["*.ts", "*.tsx"],
    onEvent: async (event) => {
      if (event.type === "modify") {
        await sandbox.exec("npm run build:src");
      }
    },
  });


  // Watch tests for test runs
  const testWatcher = await sandbox.watch("/workspace/tests", {
    include: ["*.test.ts", "*.spec.ts"],
    onEvent: async (event) => {
      if (event.type === "modify") {
        await sandbox.exec(`npm test -- ${event.path}`);
      }
    },
  });


  // Watch config files for full rebuilds
  const configWatcher = await sandbox.watch("/workspace", {
    include: ["package.json", "tsconfig.json", "vite.config.ts"],
    recursive: false, // Only watch root level
    onEvent: async (event) => {
      console.log("Configuration changed, rebuilding project...");
      await sandbox.exec("npm run build");
    },
  });
  ```

* TypeScript

  ```ts
  // Watch source code for builds
  const srcWatcher = await sandbox.watch('/workspace/src', {
    include: ['*.ts', '*.tsx'],
    onEvent: async (event) => {
      if (event.type === 'modify') {
        await sandbox.exec('npm run build:src');
      }
    }
  });


  // Watch tests for test runs
  const testWatcher = await sandbox.watch('/workspace/tests', {
    include: ['*.test.ts', '*.spec.ts'],
    onEvent: async (event) => {
      if (event.type === 'modify') {
        await sandbox.exec(`npm test -- ${event.path}`);
      }
    }
  });


  // Watch config files for full rebuilds
  const configWatcher = await sandbox.watch('/workspace', {
    include: ['package.json', 'tsconfig.json', 'vite.config.ts'],
    recursive: false, // Only watch root level
    onEvent: async (event) => {
      console.log('Configuration changed, rebuilding project...');
      await sandbox.exec('npm run build');
    }
  });
  ```

### Graceful shutdown

Use AbortSignal for clean shutdown handling:

* JavaScript

  ```js
  const controller = new AbortController();


  const watcher = await sandbox.watch("/workspace/src", {
    signal: controller.signal,
    onEvent: (event) => {
      console.log(`Event: ${event.type} - ${event.path}`);
    },
    onError: (error) => {
      if (error.name === "AbortError") {
        console.log("Watch cancelled gracefully");
      } else {
        console.error("Watch error:", error);
      }
    },
  });


  // Handle shutdown signals
  process.on("SIGINT", () => {
    console.log("Shutting down file watcher...");
    controller.abort();
  });
  ```

* TypeScript

  ```ts
  const controller = new AbortController();


  const watcher = await sandbox.watch('/workspace/src', {
    signal: controller.signal,
    onEvent: (event) => {
      console.log(`Event: ${event.type} - ${event.path}`);
    },
    onError: (error) => {
      if (error.name === 'AbortError') {
        console.log('Watch cancelled gracefully');
      } else {
        console.error('Watch error:', error);
      }
    }
  });


  // Handle shutdown signals
  process.on('SIGINT', () => {
    console.log('Shutting down file watcher...');
    controller.abort();
  });
  ```

## Best practices

### Resource management

Always stop watchers to prevent resource leaks:

* JavaScript

  ```js
  const watchers = [];


  // Create watchers
  const srcWatcher = await sandbox.watch("/workspace/src", options);
  const testWatcher = await sandbox.watch("/workspace/tests", options);
  watchers.push(srcWatcher, testWatcher);


  // Clean shutdown
  async function shutdown() {
    console.log("Stopping all watchers...");
    await Promise.all(watchers.map((w) => w.stop()));
    console.log("All watchers stopped");
  }


  process.on("exit", shutdown);
  process.on("SIGINT", shutdown);
  process.on("SIGTERM", shutdown);
  ```

* TypeScript

  ```ts
  const watchers: Array<{ stop: () => Promise<void> }> = [];


  // Create watchers
  const srcWatcher = await sandbox.watch('/workspace/src', options);
  const testWatcher = await sandbox.watch('/workspace/tests', options);
  watchers.push(srcWatcher, testWatcher);


  // Clean shutdown
  async function shutdown() {
    console.log('Stopping all watchers...');
    await Promise.all(watchers.map(w => w.stop()));
    console.log('All watchers stopped');
  }


  process.on('exit', shutdown);
  process.on('SIGINT', shutdown);
  process.on('SIGTERM', shutdown);
  ```

### Error handling

Implement robust error handling for production use:

* JavaScript

  ```js
  const watcher = await sandbox.watch("/workspace/src", {
    onEvent: async (event) => {
      try {
        await handleFileChange(event);
      } catch (error) {
        console.error(
          `Failed to handle ${event.type} event for ${event.path}:`,
          error,
        );
        // Don't let errors stop the watcher
      }
    },
    onError: async (error) => {
      console.error("Watch system error:", error);


      // Attempt to restart watcher on critical errors
      if (error.message.includes("inotify")) {
        console.log("Attempting to restart file watcher...");
        await watcher.stop();
        // Recreate watcher with same options
      }
    },
  });
  ```

* TypeScript

  ```ts
  const watcher = await sandbox.watch('/workspace/src', {
    onEvent: async (event) => {
      try {
        await handleFileChange(event);
      } catch (error) {
        console.error(`Failed to handle ${event.type} event for ${event.path}:`, error);
        // Don't let errors stop the watcher
      }
    },
    onError: async (error) => {
      console.error('Watch system error:', error);


      // Attempt to restart watcher on critical errors
      if (error.message.includes('inotify')) {
        console.log('Attempting to restart file watcher...');
        await watcher.stop();
        // Recreate watcher with same options
      }
    }
  });
  ```

### Performance optimization

For high-frequency changes, use server-side filtering:

* JavaScript

  ```js
  // Efficient - filtering happens at kernel/inotify level
  const watcher = await sandbox.watch("/workspace", {
    include: ["*.ts"], // Only TypeScript files
    exclude: ["node_modules"], // Skip dependencies
  });


  // Less efficient - all events sent to JavaScript
  const watcher2 = await sandbox.watch("/workspace", {
    onEvent: (event) => {
      if (!event.path.endsWith(".ts")) return;
      if (event.path.includes("node_modules")) return;
      // Handle event
    },
  });
  ```

* TypeScript

  ```ts
  // Efficient - filtering happens at kernel/inotify level
  const watcher = await sandbox.watch('/workspace', {
    include: ['*.ts'],           // Only TypeScript files
    exclude: ['node_modules']    // Skip dependencies
  });


  // Less efficient - all events sent to JavaScript
  const watcher2 = await sandbox.watch('/workspace', {
    onEvent: (event) => {
      if (!event.path.endsWith('.ts')) return;
      if (event.path.includes('node_modules')) return;
      // Handle event
    }
  });
  ```

## Troubleshooting

### Path not found errors

Ensure directories exist before watching them:

* JavaScript

  ```js
  const watchPath = "/workspace/src";


  // Check if path exists first
  try {
    const exists = await sandbox.readDir(watchPath);
    const watcher = await sandbox.watch(watchPath, options);
  } catch (error) {
    if (error.message.includes("not found")) {
      console.log(`Creating directory ${watchPath}...`);
      await sandbox.exec(`mkdir -p ${watchPath}`);
      // Now start watching
      const watcher = await sandbox.watch(watchPath, options);
    }
  }
  ```

* TypeScript

  ```ts
  const watchPath = '/workspace/src';


  // Check if path exists first
  try {
    const exists = await sandbox.readDir(watchPath);
    const watcher = await sandbox.watch(watchPath, options);
  } catch (error) {
    if (error.message.includes('not found')) {
      console.log(`Creating directory ${watchPath}...`);
      await sandbox.exec(`mkdir -p ${watchPath}`);
      // Now start watching
      const watcher = await sandbox.watch(watchPath, options);
    }
  }
  ```

### High CPU usage

If watching large directories causes performance issues:

1. Use specific `include` patterns instead of watching everything
2. Exclude large directories like `node_modules` and `dist`
3. Watch specific subdirectories instead of the entire project
4. Use non-recursive watching for shallow monitoring

Container lifecycle

File watchers are automatically stopped when the sandbox sleeps or shuts down. They will restart when the sandbox wakes up, but you may need to re-establish them in your application logic.

## Related resources

* [File Watching API reference](https://developers.cloudflare.com/sandbox/api/file-watching/) - Complete API documentation
* [Manage files guide](https://developers.cloudflare.com/sandbox/guides/manage-files/) - File operations
* [Background processes guide](https://developers.cloudflare.com/sandbox/guides/background-processes/) - Long-running processes
