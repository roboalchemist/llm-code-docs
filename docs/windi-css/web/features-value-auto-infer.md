# Source: https://windicss.org/features/value-auto-infer

Title: Windi CSS

URL Source: https://windicss.org/features/value-auto-infer

Markdown Content:
Value Auto-infer
----------------

Since Windi CSS will only generate the CSS utilities you use, it enables you to use arbitrary values in your classes and generate corresponding styles based on the appropriate semantics.

```
<!-- sizes and positions -->
<div class="p-5px mt-[0.3px]"></div>

<!-- colors -->
<button class="bg-hex-b2a8bb"></button>
<button class="bg-[#b2a8bb]"></button>
<button class="bg-[hsl(211.7,81.9%,69.6%)]"></button>

<!-- grid template -->
<div class="grid-cols-[auto,1fr,30px]"></div>
```

This is useful when you want to opt-out of your design system and have some fine-grain controls over some specific components. Both direct `p-5px` and explicitly escaping `p-[5px]` are supported.

We also provided [an visual analyser](https://windicss.org/features/analyzer) to give you an overview of all the utility usages in your project and to spot unwanted value escaping of your design system with ease.

Numbers
-------

```
p-{float} -> padding: {float/4}rem;
```

CSS

.p-2\.5 {
  padding: 0.625rem;
}
.p-3\.2 {
  padding: 0.8rem;
}

Sizes
-----

```
// {size} should be end with rem|em|px|vh|vw|ch|ex
p-{size} -> padding: {size};
```

CSS

.p-3px {
  padding: 3px;
}
.p-4rem {
  padding: 4rem;
}

Fractions
---------

```
w-{fraction} -> width: {fraction -> percent};
```

CSS

.w-9\/12 {
  width: 75%;
}

Colors
------

```
text-{color} -> color: rgba(...);

border-hex-{hex} -> border-color: rgba(...);
```

CSS

.border-hex-6dd1c7 {
  --tw-border-opacity: 1;
  border-color: rgba(109, 209, 199, var(--tw-border-opacity));
}
.text-cyan-400 {
  --tw-text-opacity: 1;
  color: rgba(34, 211, 238, var(--tw-text-opacity));
}

Variables
---------

You can even pass variable names, which is very useful in combination with CSS variables.

```
bg-${variableName}
```

CSS

.bg-\$test-variable {
  background-color: var(--test-variable);
}

Grid Templates
--------------

```
grid-cols-[auto,1fr,30px]
```

CSS

.grid-cols-\[auto\2c 1fr\2c 30px\] {
  grid-template-columns: auto 1fr 30px;
}
