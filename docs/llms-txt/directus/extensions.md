# Source: https://directus.io/docs/raw/tutorials/extensions.md

# Source: https://directus.io/docs/raw/configuration/extensions.md

# Extensions

> Configuration for extensions and the Directus Marketplace.

<partial content="config-env-vars">



</partial>

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        EXTENSIONS_PATH
      </code>
      
      <sup>
        <span>
          1
        </span>
      </sup>
    </td>
    
    <td>
      Path to your local extensions directory, or subdirectory within the configured storage location when <code>
        EXTENSIONS_LOCATION
      </code>
      
       is set.
    </td>
    
    <td>
      <code>
        ./extensions
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EXTENSIONS_MUST_LOAD
      </code>
    </td>
    
    <td>
      Exit the server when any API extension fails to load.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EXTENSIONS_AUTO_RELOAD
      </code>
      
      <sup>
        <span>
          2
        </span>
        
        , <span>
          3
        </span>
      </sup>
    </td>
    
    <td>
      Automatically reload extensions when they have changed.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EXTENSIONS_CACHE_TTL
      </code>
      
      <sup>
        <span>
          4
        </span>
      </sup>
    </td>
    
    <td>
      How long custom app Extensions get cached by browsers.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EXTENSIONS_LOCATION
      </code>
      
      <sup>
        <span>
          5
        </span>
        
        , <span>
          6
        </span>
      </sup>
    </td>
    
    <td>
      Key of the configured <a href="/configuration/files">
        storage locations
      </a>
      
       to load extensions from a specific storage location.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EXTENSIONS_LIMIT
      </code>
    </td>
    
    <td>
      Maximum number of extensions you allow to be installed through the Marketplace.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        EXTENSIONS_ROLLDOWN
      </code>
    </td>
    
    <td>
      Enable use of <a href="https://rolldown.rs/" rel="nofollow">
        Rolldown
      </a>
      
       to optimize extensions bundling.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

 When `EXTENSIONS_LOCATION` is set, this defines the path inside the selected storage location where extensions reside.

<sup>
<span>

2

</span>
</sup>

 `EXTENSIONS_AUTO_RELOAD` will not work when the `EXTENSIONS_LOCATION` environment variable is set.

<sup>
<span>

3

</span>
</sup>

 `EXTENSIONS_AUTO_RELOAD` will likely not work on Windows machines without also setting the `CHOKIDAR_USEPOLLING` environment variable to `true`.

<sup>
<span>

4

</span>
</sup>

 The `EXTENSIONS_CACHE_TTL` environment variable controls how long [app extensions](/guides/extensions/app-extensions) are cached by browsers. By default, extensions are not cached.

<sup>
<span>

5

</span>
</sup>

 By default extensions are loaded from the local file system. `EXTENSIONS_LOCATION` can be used to load extensions from a storage location instead.

<sup>
<span>

6

</span>
</sup>

 The value of `EXTENSIONS_LOCATION` must correspond to a key defined in your `STORAGE_LOCATIONS` environment variable.

## Marketplace

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default Value
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        MARKETPLACE_TRUST
      </code>
    </td>
    
    <td>
      One of <code>
        sandbox
      </code>
      
      , <code>
        all
      </code>
    </td>
    
    <td>
      <code>
        sandbox
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        MARKETPLACE_REGISTRY
      </code>
    </td>
    
    <td>
      The registry to use for the Directus Marketplace.
    </td>
    
    <td>
      <code>
        https://registry.directus.io
      </code>
    </td>
  </tr>
</tbody>
</table>

<callout icon="material-symbols:info-outline">

**Sandbox**<br />


By default, the Directus Marketplace will allow installation of all [App extension types](/guides/extensions/app-extensions) and only [API extension types](/guides/extensions/api-extensions) that use our secure sandbox.

</callout>
