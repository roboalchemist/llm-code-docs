# jsx_a11y/html-has-lang

## What it does

Ensures that every HTML document has a lang attribute

## Why is this bad?

If the language of a webpage is not specified,
the screen reader assumes the default language set by the user.
Language settings become an issue for users who speak multiple languages
and access website in more than one language.

## Examples

### Incorrect code for this rule:

```jsx
<html />
```

### Correct code for this rule:

```jsx
<html lang="en" />
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

```json [Config (.oxlintrc.json)]
{
  "plugins": ["jsx-a11y"],
  "rules": {
    "jsx-a11y/html-has-lang": "error"
  }
}
```

```bash [CLI]
oxlint --deny jsx-a11y/html-has-lang --jsx-a11y-plugin
```

## References

* Rule Source