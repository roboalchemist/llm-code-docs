# Type Alias: CustomIcon

```
type CustomIcon = string | ({ theme, iconSize }) => string;
```

Type representing a custom icon, which can be a string or a function.

*   If a string, it represents the name of the icon.
*   If a function, it takes an object with `theme` and `iconSize` properties and returns a string representing the icon.

---



[Source](https:/img.ly/docs/cesdk/sveltekit/api/cesdk-js/documentation/namespaces/userinterfaceelements/type-aliases/customcardimagebackground)