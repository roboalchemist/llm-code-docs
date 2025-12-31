# Source: https://docs.intelligems.io/performance-optimization/edgemesh.md

# Edgemesh

Each time you make a change in Intelligems (for example, starting or ending an experiment), Intelligems updates a portion of the script that loads on your site in order to effect the change. If you use Edgemesh, they may cache Intelligems' configuration, preventing these changes from taking effect.

The most effective way to work around that is to add: `data-em-disable` to the Intelligems script tag to prevent this caching.

Example:

```html
<script>
    window.Shopify = window.Shopify || {theme: {id: {{ theme.id }}, role: '{{ theme.role }}' } };
    window._template = {
        directory: "{{ template.directory }}",
        name: "{{ template.name }}",
        suffix: "{{ template.suffix }}"
    };
</script>
<script type="module" blocking="render" fetchpriority="high" src="https://cdn.intelligems.io/esm/<customer_id>/bundle.js" data-em-disable></script>
```

Copy this script and replace `<customer_id>` with your actual unique ID, which can be found on the Settings page of the Intelligems app. Alternatively, you can add `data-em-disable` to the Intelligems script tag so that it matches the above.
