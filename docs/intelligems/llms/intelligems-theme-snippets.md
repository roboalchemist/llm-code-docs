# Source: https://docs.intelligems.io/developer-resources/intelligems-theme-snippets.md

# Intelligems Theme Snippets

### Template Testing Snippet

If you would like to run template tests, add the following JavaScript snippet to your `theme.liquid` file **above** the standard Intelligems script:

```html
  <script>
    window._template = {
        directory: "{{ template.directory }}",
        name: "{{ template.name }}",
        suffix: "{{ template.suffix }}"
    }
    window.Shopify = window.Shopify || {theme: {id: {{ theme.id }}, role: '{{ theme.role }}' } };
  </script> 
```

If you are using the Intelligems Theme Block extension, the snippet will be automatically included for you.
