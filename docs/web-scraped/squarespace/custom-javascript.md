# Custom JavaScript

## Overview

Squarespace allows developers to incorporate custom JavaScript files and libraries within templates. The platform offers two approaches: using Squarespace's built-in script loader or implementing your own preprocessor.

## Script Loader Method

Squarespace provides a dedicated script loader that minifies code and consolidates multiple JavaScript files into a single resource, reducing HTTP requests.

### Syntax

```html
<squarespace:script src="plugin.js" combo="true" />
<squarespace:script src="site.js" combo="true" />
```

### Attributes

- **src** - References file paths relative to the template's `/scripts` directory
- **combo** - Boolean that determines whether to combine multiple scripts into a single HTTP request (recommended for performance)

### Benefits

- Automatic minification of JavaScript code
- Consolidation of multiple files into single HTTP request
- Optimized performance for production environments

## Custom Preprocessor Approach

Developers can utilize alternative JavaScript workflow tools such as:
- NPM
- Gulp
- Browserify
- Webpack

Compiled code should be placed in the `/scripts` folder and linked using standard HTML script tags or Squarespace's script tag syntax.

### Example with Webpack

```bash
# Install webpack and dependencies
npm install --save-dev webpack webpack-cli

# Build your JavaScript
webpack

# Output goes to /scripts/bundle.js
```

Then reference in your template:
```html
<squarespace:script src="bundle.js" combo="true" />
```

## External Third-Party Libraries

You can load libraries from external servers or CDN networks. However, implementing a local fallback ensures functionality if the external source becomes unavailable.

### CDN with Local Fallback Pattern

```html
<script src="//code.jquery.com/jquery-2.2.1.min.js"></script>
<script>
   window.jQuery || document.write('<script src="scripts/jquery-2.2.1.min.js"><\/script>')
</script>
```

This pattern:
1. Attempts to load jQuery from the CDN
2. Checks if jQuery loaded successfully
3. References a locally-hosted version if the CDN fails

### Why Local Fallbacks Matter

- External CDN services may experience downtime
- Network connectivity issues could block CDN access
- Local fallback ensures site functionality is not dependent on external services

### Common Libraries

Popular libraries commonly included via CDN:
- jQuery
- Bootstrap
- D3.js
- Moment.js
- Lodash

Always include a local fallback for mission-critical libraries.

## Script Execution Context

### Squarespace Template Object

Access Squarespace-specific functionality through the Template object:

```javascript
// Get a tweak value
Y.Squarespace.Template.getTweakValue('variableName')

// Listen for tweak changes
Y.Global.on('tweak:change', function(e) {
  // Handle change
});
```

### YUI Framework

Squarespace uses the YUI (Yahoo User Interface) framework for core functionality. Your custom scripts can integrate with YUI:

```javascript
// YUI is available as Y
Y.one('.selector').addClass('class-name');
Y.all('.items').each(function(item) {
  // Process each item
});
```

## Best Practices

### Performance Optimization

1. **Minify scripts** - Remove unnecessary characters
2. **Combine files** - Use `combo="true"` to consolidate requests
3. **Lazy load** - Load non-critical scripts asynchronously
4. **Defer execution** - Load scripts after DOM is ready

### Code Organization

```
/scripts/
  ├── site.js          (main site functionality)
  ├── plugins.js       (third-party plugins)
  ├── vendor.js        (external libraries)
  └── utils.js         (utility functions)
```

### Initialization

Ensure scripts run after the DOM is loaded:

```javascript
Y.on('domready', function() {
  // Your code here - safe to manipulate DOM
  initializeMyComponent();
});
```

## Accessing Squarespace Data

Your custom JavaScript can access site data through Squarespace's API:

```javascript
// Get current page data
var pageData = Y.Squarespace.page;

// Access site configuration
var siteConfig = Y.Squarespace.siteConfig;

// Get item data in collection contexts
if (Y.Squarespace.item) {
  var itemData = Y.Squarespace.item;
}
```

## Event Handling

Listen for Squarespace events in your custom scripts:

```javascript
// Page changed
Y.Global.on('sqsp:page:changed', function(e) {
  console.log('Page changed:', e);
});

// Page scrolled
Y.one(window).on('scroll', function(e) {
  console.log('Scrolled to:', window.scrollY);
});
```

## Debugging

### Browser Console

Use the browser developer console to test and debug:

```javascript
// Check if your code is loaded
console.log(typeof myFunction);

// Monitor Squarespace events
Y.Global.on('*:*', function(e) {
  console.log('Event:', e.type);
});
```

### Debug Mode

Enable verbose logging in the local development server:

```bash
squarespace-server https://site-name.squarespace.com --verbose
```

This helps identify script loading issues and execution errors.

## Common Patterns

### Form Submission Handler

```javascript
Y.one('form').on('submit', function(e) {
  e.preventDefault();
  // Handle form submission
});
```

### DOM Manipulation

```javascript
// Add class to element
Y.one('.target').addClass('active');

// Create and append element
var newEl = Y.Node.create('<div class="new">Content</div>');
Y.one('body').append(newEl);
```

### AJAX Request

```javascript
Y.io('/api/endpoint', {
  method: 'GET',
  on: {
    success: function(id, o) {
      console.log('Response:', o.responseText);
    },
    failure: function(id, o) {
      console.log('Error:', o.statusText);
    }
  }
});
```

## Security Considerations

- **Validate user input** - Always sanitize data from forms
- **Use HTTPS** - Ensure external scripts are loaded over HTTPS
- **Content Security Policy** - Be aware of CSP headers that may restrict inline scripts
- **XSS Prevention** - Don't use innerHTML with user-provided data

## Support

For issues with custom JavaScript in Squarespace templates, consult the [Squarespace Developer Documentation](https://developers.squarespace.com/) or reach out to [Squarespace support](https://support.squarespace.com/).
