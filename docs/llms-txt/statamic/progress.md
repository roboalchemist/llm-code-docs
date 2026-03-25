# Source: https://statamic.dev/vue-components/progress.md

# Progress

Control the magic progress bar at the top of the page.


You can control the progress bar at the top of the page through the `$progress` instance method.

This progress bar will get a little further in small intervals automatically but will never reach 100% until it's told to.

The component can track the progress from multiple places, and will only be considered complete once all of them are complete.

``` js
import { progress } from '@statamic/cms/api';

progress.start($name); // Starts the progress bar
progress.complete($name); // Instantly progress to 100% and disappear

progress.loading($name, true); // Alias of .start() - Useful for passing a boolean
progress.loading($name, false); // Alias of complete()

progress.names(); // The names of the items that are being tracked.
progress.count(); // How many are being tracked.
progress.isComplete(); // Whether all the items that were being tracked have completed.
```

:::tip
If you have a component that may appear multiple times on one page (like a Fieldtype), make sure the name is unique. You could use the browser's crypto API for this:

``` js
const uniqueId = crypto.randomUUID();

progress.start(`things-${uniqueId}`);
```
:::
