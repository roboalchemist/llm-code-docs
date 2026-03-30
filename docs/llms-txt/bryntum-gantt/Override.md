# Source: https://bryntum.com/products/gantt/docs-llm/api/Core/mixin/Override.md

# [Override](https://bryntum.com/docs/gantt/api/Core/mixin/Override)

Simplifies overriding class methods by allowing methods from another class to be used as overrides. Overrides are defined as own classes. They must at a minimum contain a static getter named \`target´, which should return an object with the class to override. Apply the override by calling [apply()](https://bryntum.com/docs/gantt/api/#Core/mixin/Override#function-apply-static).

Versions can be specified in the override target config to only apply the override for specific product versions. Both `minVersion` and `maxVersion` are **inclusive** - the override will be applied when the current product version falls within the range `[minVersion, maxVersion]`.

```
class TemplateColumnOverride {
    static get target() {
        return {
            class      : TemplateColumn,
            product    : 'grid',
            minVersion : '1.0',
            maxVersion : '1.5'
        }
    }

    renderer(renderData) {
        // call overridden function (optional)
        const value = this._overridden.renderer.call(this, renderData);

        return 'HELLO' + value;
    }
}
Override.apply(TemplateColumnOverride);
```

## Functions

Functions are methods available for calling on the class

[apply](https://bryntum.com/docs/gantt/api/Core/mixin/Override#function-apply-static)
Apply override. We strongly suggest that you at least specify `maxVersion` for your overrides.

Both `minVersion` and `maxVersion` are **inclusive** - the override will be applied when the current product version falls within the range `[minVersion, maxVersion]`.

```
class OriginalOverride {
    static get target() {
        return {
            class      : Original,
            product    : 'grid',
            minVersion : '1.0',
            maxVersion : '1.5'
        }
    }
}
```

[shouldApplyOverride](https://bryntum.com/docs/gantt/api/Core/mixin/Override#function-shouldApplyOverride-static)
Checks versions if an override should be applied. Specify version in your overrides target config.

Both `minVersion` and `maxVersion` are **inclusive** - the override will be applied when the current product version falls within the range `[minVersion, maxVersion]`.

```
class OriginalOverride {
    static get target() {
        return {
            class      : Original,
            product    : 'grid',
            minVersion : '1.0',  // inclusive: override applies to 1.0 and newer
            maxVersion : '1.5'   // inclusive: override applies to 1.5 and older
        }
    }
}
```
