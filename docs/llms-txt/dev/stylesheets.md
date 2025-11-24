# Source: https://dev.writer.com/framework/stylesheets.md

# Stylesheets

The appearance of your application can be fully customised via CSS stylesheets. These are dynamically linked during runtime and can be switched from the back-end, targeting all or specific sessions.

## Importing a stylesheet

Stylesheet imports are triggered via Framework's `mail`, similarly to other features discussed in [Backend-initiated actions](/framework/backend-initiated-actions). When the import is triggered, the front-end downloads the specified stylesheet and creates a `style` element with its contents.

The `import_stylesheet` method takes the `stylesheet_key` and `path` arguments. The first works as an identifier that will let you override the stylesheet later if needed. The second is the path to the CSS file.The path specified needs to be available to the front-end, so storing it in the `/static` folder of your app is recommended.

The following code imports a stylesheet when handling an event.

```py  theme={null}
def handle_click(state):
    state.import_stylesheet("theme", "/static/custom.css")
```

In many cases, you'll want to import a stylesheet during initialisation time, for all users. This is easily achievable via the initial state, as shown below.

```py  theme={null}
initial_state = wf.init_state({
    "counter": 1
})

initial_state.import_stylesheet("theme", "/static/custom.css")
```

<Tip>
  Use versions to avoid caching. During development time, stylesheets may be cached by your browser, preventing updates from being reflected. Append a querystring to bust the cache, e.g. use `/static/custom.css?3`.
</Tip>

## Applying CSS classes

You can use the property *Custom CSS classes* in the Builder's *Component Settings* to apply classes to a component, separated by spaces. Internally, this will apply the classes to the root HTML element of the rendered component.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.component-settings.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7bde5b1b655bc18d64c8fe53446cb7cb" alt="Stylesheets - Component Settings" data-og-width="1704" width="1704" data-og-height="346" height="346" data-path="framework/images/stylesheets.component-settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.component-settings.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=f7c8e67136955e17a4b761efa14c5389 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.component-settings.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=d4cdf0b6b22ddf396134346320c3ee85 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.component-settings.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=38078c3bf901999b1c5bad469d6e19dc 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.component-settings.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=7c14d29c9cb3f3d2d36ad0ccb55b9fd0 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.component-settings.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=3a8917d3978683898ed9276cdcbdf9b8 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.component-settings.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=82d19c3c2a0bb66e19334263b83e35b8 2500w" />

## Tips for effective stylesheets

The CSS code for the class used earlier, `bubblegum`, can be found below. Note how the `!important` flag is used when targetting style attributes that are configurable via the Builder. If the flag isn't included, these declarations will not work, because built-in Framework styling is of higher specificity.

```css  theme={null}
.bubblegum {
    background: #ff63ca !important;
    line-height: 1.5;
    transform: rotate(-5deg);
}

/* Targeting an element inside the component root element */
.bubblegum > h2 {
    color: #f9ff94 !important;
}
```

<Warning>
  Component structure may change. When targeting specific HTML elements inside components, take into account that the internal structure of components may change across Framework versions.
</Warning>

Alternatively, you can override Framework's style variables. This behaves slightly differently though; style variables are inherited by children components. For example, if a *Section* has been assigned the `bubblegum` class, its children will also have a pink background by default.

```css  theme={null}
.bubblegum {
    --containerBackgroundColor: #ff63ca;
    --primaryTextColor: #f9ff94;
    line-height: 1.5;	
    transform: rotate(-5deg);
}
```

The class can be used in *Component Settings*. If the stylesheet is imported, the effect will be immediate. In case the stylesheet has been modified since imported, it'll need to be imported again.

<img src="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.applied-classes.png?fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=65444dbafae3a638b47f484b9d04185f" alt="Stylesheets - Applied Classes" data-og-width="1686" width="1686" data-og-height="346" height="346" data-path="framework/images/stylesheets.applied-classes.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.applied-classes.png?w=280&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=449839ae5f1409c4342c0e8ff99f144c 280w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.applied-classes.png?w=560&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=aa26426ffebe72b2f2dc1ed6791cbae1 560w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.applied-classes.png?w=840&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=abb5349762ed4235873e3ab2ba43a4ac 840w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.applied-classes.png?w=1100&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=e4cd8049c49f3d97b749738eba914f52 1100w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.applied-classes.png?w=1650&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=f3a4a288941a0bcb911c558a7a8f68e7 1650w, https://mintcdn.com/writer/9jV0H_SSzBim4ReZ/framework/images/stylesheets.applied-classes.png?w=2500&fit=max&auto=format&n=9jV0H_SSzBim4ReZ&q=85&s=b0f46f5f93186668afd032d138b20e96 2500w" />

## Targeting component types

Framework components have root HTML elements with a class linked to their type. For example, *Dataframe* components use the class *CoreDataframe*. When writing a stylesheet, you can target all *Dataframe* components as shown below.

```css  theme={null}
.CoreDataframe {
    line-height: 2.0;
}
```

## Implementing themes

It's possible to switch stylesheets during runtime, by specifying the same `stylesheet_key` in subsequent calls. This allows you to implement a "theme" logic if desired, targeting the whole or a specific part of your app.

```py  theme={null}
def handle_cyberpunk(state):
    state.import_stylesheet("theme", "/static/cyberpunk_theme.css")

def handle_minimalist(state):
    state.import_stylesheet("theme", "/static/minimalist_theme.css")
```
