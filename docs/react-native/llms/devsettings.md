# Source: https://reactnative.dev/docs/devsettings.md

# DevSettings

The `DevSettings` module exposes methods for customizing settings for developers in development.

***

# Reference

## Methods[​](#methods "Direct link to Methods")

### `addMenuItem()`[​](#addmenuitem "Direct link to addmenuitem")

tsx

```
static addMenuItem(title: string, handler: () => any);
```

Add a custom menu item to the Dev Menu.

**Parameters:**

| Name            | Type     |
| --------------- | -------- |
| titleRequired   | string   |
| handlerRequired | function |

**Example:**

tsx

```
DevSettings.addMenuItem('Show Secret Dev Screen', () => {
  Alert.alert('Showing secret dev screen!');
});
```

***

### `reload()`[​](#reload "Direct link to reload")

tsx

```
static reload(reason?: string): void;
```

Reload the application. Can be invoked directly or on user interaction.

**Example:**

tsx

```
<Button title="Reload" onPress={() => DevSettings.reload()} />
```
