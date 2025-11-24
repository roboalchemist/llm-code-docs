# Source: https://dev.writer.com/agent-builder/component-styles.md

# Add styling to the agent UI

You can style an agent's interface in two ways:

1. [Using component configuration menus](#component-configuration-menu) to adjust styling such as colors, backgrounds, shadows, and text alignment.

2. [Using CSS](#style-agent-builder-components-with-css) to target specific components, apply more advanced styling not available in the configuration menu, and create reusable styles across multiple components.

The configuration menu provides a convenient interface for common styling needs, while CSS gives you complete control over the agent's appearance.

## Component configuration menu

The component's configuration menu provides an interface for common styling needs such as colors, backgrounds, and text alignment. Each interface component has a different set of configurable attributes, which you can access via the configuration menu.

There are three styling options for each configurable attribute:

* **Default**: the default styling for the attribute.
* **CSS**: provide a CSS rule to apply to the attribute. For example, if the attribute is font color, you can set a CSS value such as `red`, a hex code, or an RGB value to apply to the attribute.
* **Pick**: define a value from a visual picker. For example, you can select a color from a color picker or control a shadow from a set of slider controls.

<Tabs>
  <Tab title="Default">
    Revert to the default styling for the attribute.
    <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/default-styling.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5877d1641997671c54dab544f4871114" alt="" data-og-width="2876" width="2876" data-og-height="860" height="860" data-path="images/agent-builder/default-styling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/default-styling.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4be13d1f7f4631e2b50d5c896dd0ed19 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/default-styling.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=0813c379b509c2033b8419e1866878f5 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/default-styling.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=a85037279618f18af556bd5149d2855d 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/default-styling.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=b52b7630b2b03b52e69b7044b4d894ba 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/default-styling.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=0a7105770d618ce2981cdbf711266acc 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/default-styling.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=ac392fb2142604ee5ca6a4d75adcc37e 2500w" />
  </Tab>

  <Tab title="CSS">
    Provide a CSS rule to apply to the attribute.

    For example, if the attribute is font color, you can set a [CSS value](https://www.w3schools.com/cssref/css_colors.php) such as `red`, a hex code, or an RGB value to apply to the attribute.

    For shadow attributes, you can remove a component's shadow with `none` or update the shadow with [`box-shadow` CSS rules](https://www.w3schools.com/cssref/css3_pr_box-shadow.php).

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/css-styling.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=07c97a999bdb875ca9fd49fc4c977991" alt="" data-og-width="2876" width="2876" data-og-height="838" height="838" data-path="images/agent-builder/css-styling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/css-styling.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=4531ca1ab1bedf0ef8ced72ee6718bd0 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/css-styling.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=b7e94ab9ec627d31f875770c2e980622 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/css-styling.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=33dc8263ab8b69012a2675f9fc55e979 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/css-styling.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=b5142d85d6c43e6e827394edeaac5f4f 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/css-styling.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=9081660132e6cc95863908777737a1fd 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/css-styling.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=12e08d0308a7d52216ef5684340a8339 2500w" />
  </Tab>

  <Tab title="Pick">
    Define a value from a visual picker. For example, you can select a color from a color picker.
    <img src="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/pick-styling.png?fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=b59b72907c383f82a3f0efcf9066e5e0" alt="" data-og-width="2872" width="2872" data-og-height="850" height="850" data-path="images/agent-builder/pick-styling.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/pick-styling.png?w=280&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=9e833daf5d74bbf43dc6b1251c45f494 280w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/pick-styling.png?w=560&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=d13d65629148b72bdff3d946bcbae532 560w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/pick-styling.png?w=840&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=6d56291411c8cd67478ac3940fbb27e1 840w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/pick-styling.png?w=1100&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=e48a5566d59a3f745e10406261143b28 1100w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/pick-styling.png?w=1650&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=11f10e4e3a62e722228abcb95281e90d 1650w, https://mintcdn.com/writer/nTMyJEeQXE_UTdYX/images/agent-builder/pick-styling.png?w=2500&fit=max&auto=format&n=nTMyJEeQXE_UTdYX&q=85&s=cbe11353f977870ce08e4ebcb14a0a67 2500w" />
  </Tab>
</Tabs>

## Add a CSS stylesheet

To add more specific and detailed styling for your agent's UI, you can add CSS stylesheets.

To style your agent's UI with CSS, follow these steps:

1. Add a CSS file to your project via the **Code** tab
2. Load the stylesheet into the agent's state
3. Apply CSS classes to components via the component's configuration menu

The example below creates a `bubblegum` class to make a pink, rotated component and makes the header font color for `CoreSection h3` elements yellow.

<Steps>
  <Step title="Add the `.css` file to your project">
    Create a new `.css` file in your project or upload an existing one via the **Code** tab.

    This example creates a new file named `theme.css` in the `static` directory with the following content:

    ```css  theme={null}
    .bubblegum {
        background: #ff63ca !important;
        line-height: 1.5;
        transform: rotate(-5deg);
    }

    .CoreSection h3 {
        color: #f9ff94 !important;
    }
    ```

    <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-file.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=e195f460e11ddfb726f82b23f4ab6ef0" alt="" data-og-width="2862" width="2862" data-og-height="838" height="838" data-path="images/agent-builder/add-css-file.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-file.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=a04e45a7dd6a78474ecd18ea87193af9 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-file.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=33a8907b8b5e31ea8ad6baa5ecd9e5b0 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-file.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=43400ca456ca5d31c102dfe5d39c0567 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-file.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=af2f40ab9b44e7df0a5a9636084a3360 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-file.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=07f78171f71abaeb5b4c8b37ce9029a3 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-file.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=63670d1c6aff6f3e46a2f406147f5afc 2500w" />
    See [Style Agent Builder components with CSS](#style-agent-builder-components-with-css) for more information about specifically styling Agent Builder components.

    <Note>
      To move a file into a directory such as `static`, prepend the directory name to the beginning of the filename. For example, `static/theme.css`.
    </Note>
  </Step>

  <Step title="Import the CSS file in your agent's code">
    To load the stylesheet when the agent starts, import the CSS file using the state's `import_stylesheet` method in `main.py`. The code below imports the stylesheet named `theme` from the `static` directory.

    ```python  theme={null}
    initial_state.import_stylesheet("theme", "static/theme.css")
    ```

        <img src="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/import-css-file.png?fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=75d53eca11d82dfd47d5237b513ab442" alt="" data-og-width="2856" width="2856" data-og-height="834" height="834" data-path="images/agent-builder/import-css-file.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/import-css-file.png?w=280&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=0dbfbfefa5325f22507a9e18b7ca5c54 280w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/import-css-file.png?w=560&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=04d57b4a7435fd277d19bcc1e17b4f36 560w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/import-css-file.png?w=840&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=cb775459e906cf0e1dab6b91550bb4fa 840w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/import-css-file.png?w=1100&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=bceb747032908dba7f8605ac5898a494 1100w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/import-css-file.png?w=1650&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=52f8a5d5d5cde076d2b1327d6e4c4905 1650w, https://mintcdn.com/writer/pM8WhgC5nDcujQ4i/images/agent-builder/import-css-file.png?w=2500&fit=max&auto=format&n=pM8WhgC5nDcujQ4i&q=85&s=5cecd4e236210879079e7a5b6729812c 2500w" />

    The first argument is the name you want to give to the stylesheet, which you can reference if there are multiple stylesheets. The second argument is the path to the CSS file.

    You can also import stylesheets during runtime by calling the `import_stylesheet` method from the `state` object. See [Switch stylesheets during runtime](#switch-stylesheets-during-runtime) for more information.
  </Step>

  <Step title="Apply CSS classes to components">
    In the component's configuration menu, add a CSS class to the component under **Custom CSS classes**. Separate multiple classes with a space.

    This example adds the `bubblegum` class to a `Section` component so that the component's background is pink and rotated 5 degrees. The `CoreSection h3` styling applies to the header for any `Section` components, making the header text yellow.
    <img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-class.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c2938f3eb534c78bd4a64ef1d436b218" alt="" data-og-width="2866" width="2866" data-og-height="826" height="826" data-path="images/agent-builder/add-css-class.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-class.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=669f8669fdd655f29e5cc01f9ae540c8 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-class.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=6d9755f51ccef4b6f71a2acb8ff415f7 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-class.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=c4af83f37fa48f327c8c5b1b37582076 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-class.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=1447e6dc9d660c6c01b99ba30a44e87a 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-class.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=6f718d0d664c477c37184ce0211a70ab 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/images/agent-builder/add-css-class.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=4fd955df06124d9331509fb66aa2e8e1 2500w" />
  </Step>
</Steps>

<Warning>
  **CSS changes may not appear immediately due to browser caching.** When you modify a CSS file and refresh the page, you may experience a delay before the changes apply. This is expected behavior caused by browser caching.

  To see your CSS changes immediately during development, append a version querystring to your stylesheet path. This works because browsers cache CSS files based on their URL. By changing the querystring parameter, you force the browser to treat it as a new file and download a fresh copy. Increment the version number each time you update the CSS file to see changes immediately:

  ```python  theme={null}
  initial_state.import_stylesheet("theme", "static/theme.css?v=1")
  # After making changes, update to:
  initial_state.import_stylesheet("theme", "static/theme.css?v=2")
  ```
</Warning>

### Style Agent Builder components with CSS

Agent Builder components each have a class name starting with `Core` that you can use when defining CSS rules.

For example, the `Text` component has the class name `CoreText`. You can use this class name to style all `Text` components with the following CSS rule:

```css  theme={null}
.CoreText {
  color: red !important;
}
```

<Tip>
  The `!important` flag is essential when targeting attributes that are configurable via the component's configuration menu, such as text and background colors. Without the `!important` flag, the styles you define in CSS will be overridden by the component's configuration menu styling, because the configuration menu styling is of higher specificity.
</Tip>

### Switch stylesheets during runtime

You can switch stylesheets during runtime by calling the `import_stylesheet` method. To replace the current stylesheet with a new one, use the same stylesheet name but a different path to a new stylesheet.

The example below switches the stylesheet named `theme` to a different file when the `handle_cyberpunk` or `handle_minimalist` functions are called.

```python  theme={null}
def handle_cyberpunk(state):
    state.import_stylesheet("theme", "static/cyberpunk_theme.css")

def handle_minimalist(state):
    state.import_stylesheet("theme", "static/minimalist_theme.css")
```

<feedback />
