# Source: https://statamic.dev/control-panel/toast-notifications.md

# Toast Notifications

Simple notification messages that "pop" into the screen like toast popping out of a toaster.

You may display simple toast notifications through the `$toast` instance method.

``` js
this.$toast.info('message');    // Basic message
this.$toast.success('message'); // Green success
this.$toast.error('message');   // Red error
this.$toast.success('message', { duration: 3000 }); // Auto-disappear after this many milliseconds
```

You may also trigger these from the server using the `Toast` facade.

```php
use Statamic\Facades\CP\Toast;

Toast::info('message');
Toast::success('message');
Toast::error('message');

Toast::info('message')->duration(3000);
```

You don't have to return them to a response. Simply calling them is enough. They will automatically routed through the response into JavaScript.
