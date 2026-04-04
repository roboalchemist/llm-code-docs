# @angular-eslint/eslint-plugin

Source: https://github.com/angular-eslint/angular-eslint

## Overview

@angular-eslint/eslint-plugin is an ESLint plugin that contains rules specific to Angular projects. It provides linting rules designed to enforce Angular style guide best practices and prevent common mistakes in Angular component, directive, service, and module code. The plugin works seamlessly with TypeScript ESLint to analyze Angular TypeScript source code.

**Package Information:**
- **Name:** @angular-eslint/eslint-plugin
- **Version:** 21.1.0+ (aligns with Angular CLI versions)
- **License:** MIT
- **Repository:** https://github.com/angular-eslint/angular-eslint
- **NPM:** https://www.npmjs.com/package/@angular-eslint/eslint-plugin

## Key Features

- **Angular-Specific Rules:** 40+ rules designed for Angular projects covering components, directives, services, pipes, and lifecycle management
- **Best Practices Enforcement:** Rules enforce Angular style guide recommendations from https://angular.dev/style-guide
- **Multiple Rule Categories:** Rules organized by type - possible problems, suggestions, and deprecated rules
- **Auto-fix Support:** Many rules support ESLint's `--fix` flag for automatic code correction
- **Rule Suggestions:** Some rules provide suggestions for fixing issues beyond automatic fixes
- **Modern Angular Support:** Rules for both traditional decorators (@Input, @Output, etc.) and modern Angular signals API
- **Lifecycle Management:** Rules for proper lifecycle hook usage and ordering
- **TypeScript Integration:** Works with @typescript-eslint/utils for full TypeScript support

## Installation

Install the plugin alongside ESLint and TypeScript ESLint:

```bash
npm install --save-dev @angular-eslint/eslint-plugin @typescript-eslint/eslint-plugin @typescript-eslint/parser eslint typescript
```

Or using the Angular CLI schematics:

```bash
ng add angular-eslint
```

## Configuration

### Using Flat Config (ESLint v9+, Recommended)

Create `eslint.config.js`:

```javascript
const tsPlugin = require('@typescript-eslint/eslint-plugin');
const angularPlugin = require('@angular-eslint/eslint-plugin');
const tsParser = require('@typescript-eslint/parser');

module.exports = [
  {
    files: ['**/*.ts'],
    languageOptions: {
      parser: tsParser,
      parserOptions: {
        project: './tsconfig.json',
        sourceType: 'module'
      }
    },
    plugins: {
      '@typescript-eslint': tsPlugin,
      '@angular-eslint': angularPlugin
    },
    rules: {
      '@angular-eslint/directive-selector': [
        'error',
        {
          type: 'attribute',
          prefix: 'app',
          style: 'camelCase'
        }
      ],
      '@angular-eslint/component-selector': [
        'error',
        {
          type: 'element',
          prefix: 'app',
          style: 'kebab-case'
        }
      ],
      '@angular-eslint/prefer-inject': 'error',
      '@angular-eslint/no-input-rename': 'error',
      '@angular-eslint/no-output-rename': 'error'
    }
  }
];
```

### Using ESLintrc Config (Deprecated but Still Supported)

Create `.eslintrc.json`:

```json
{
  "root": true,
  "ignorePatterns": ["projects/**/*"],
  "overrides": [
    {
      "files": ["*.ts"],
      "parserOptions": {
        "project": ["tsconfig.json"],
        "createDefaultProgram": true
      },
      "extends": [
        "plugin:@angular-eslint/recommended",
        "plugin:@angular-eslint/template/recommended"
      ],
      "rules": {
        "@angular-eslint/directive-selector": [
          "error",
          {
            "type": "attribute",
            "prefix": "app",
            "style": "camelCase"
          }
        ],
        "@angular-eslint/component-selector": [
          "error",
          {
            "type": "element",
            "prefix": "app",
            "style": "kebab-case"
          }
        ]
      }
    }
  ]
}
```

## Premade Configurations

The plugin provides ready-to-use configurations that can be extended:

- Recommended rules for safe, well-established practices
- Angular style guide compliant defaults
- Different strictness levels available

## Rule Categories

### Possible Problems (8 Rules)

Rules that detect potential bugs and common mistakes:

| Rule | Purpose |
|------|---------|
| `contextual-lifecycle` | Ensures lifecycle methods are used in correct context |
| `no-async-lifecycle-method` | Prevents async lifecycle hooks (Angular doesn't wait for them) |
| `no-attribute-decorator` | Disallows @Attribute decorator to prevent confusion with @Input |
| `no-developer-preview` | Prevents use of APIs marked as developer preview |
| `no-experimental` | Prevents use of experimental APIs |
| `no-implicit-take-until-destroyed` | Ensures takeUntilDestroyed() called with explicit DestroyRef outside injection context |
| `require-lifecycle-on-prototype` | Lifecycle methods must be on prototype, not instance |
| `sort-lifecycle-methods` | Ensures lifecycle methods declared in execution order |

### Suggestions (33 Rules)

Rules providing guidance on code improvements and modern patterns:

| Rule | Purpose | Fixable |
|------|---------|---------|
| `component-class-suffix` | Component classes should have "Component" suffix (deprecated in v20) | |
| `component-max-inline-declarations` | Limits inline template/styles/animation lines | |
| `component-selector` | Enforces component selector naming conventions | |
| `consistent-component-styles` | Ensures consistent styles/styleUrls/styleUrl usage | Yes |
| `contextual-decorator` | Classes must use appropriate decorators | |
| `directive-class-suffix` | Directive classes should have "Directive" suffix (deprecated in v20) | |
| `directive-selector` | Enforces directive selector naming conventions | |
| `no-duplicates-in-metadata-arrays` | Prevents duplicate entries in metadata arrays | |
| `no-empty-lifecycle-method` | Disallows declaring empty lifecycle methods | |
| `no-forward-ref` | Disallows forwardRef() for dependency injection | |
| `no-input-prefix` | Input names should not use disallowed prefixes | |
| `no-input-rename` | Input bindings should not be aliased | Yes |
| `no-inputs-metadata-property` | Disallows old inputs metadata property | |
| `no-lifecycle-call` | Prevents explicit calls to lifecycle methods | |
| `no-output-native` | Output names should not match DOM events | |
| `no-output-on-prefix` | Output names should not be "on" or start with "on" | |
| `no-output-rename` | Output bindings should not be aliased | Yes |
| `no-outputs-metadata-property` | Disallows old outputs metadata property | |
| `no-pipe-impure` | Disallows impure pipe declarations | |
| `no-queries-metadata-property` | Disallows old queries metadata property | |
| `no-uncalled-signals` | Warns about unintentional signal logic instead of signal value | |
| `pipe-prefix` | Enforces consistent pipe naming prefixes | |
| `prefer-host-metadata-property` | Use host metadata instead of @HostBinding/@HostListener | |
| `prefer-inject` | Prefer inject() over constructor parameter injection | |
| `prefer-on-push-component-change-detection` | Recommends OnPush change detection | |
| `prefer-output-emitter-ref` | Use OutputEmitterRef instead of @Output() | |
| `prefer-output-readonly` | @Output/@OutputEmitterRef/@OutputRef should be readonly | |
| `prefer-signal-model` | Use model() instead of input/output for two-way bindings | Yes |
| `prefer-signals` | Use signals instead of @Input/@ViewChild/etc | Yes |
| `prefer-standalone` | Components/Directives/Pipes should be standalone | |
| `relative-url-prefix` | Enforce ./ and ../ prefixes in relative URLs | |
| `require-localize-metadata` | $localize messages should have translation metadata | |
| `runtime-localize` | $localize messages must support runtime-loaded translations | |
| `sort-keys-in-type-decorator` | Sort keys in type decorators consistently | Yes |
| `use-component-selector` | Component must declare selector | |
| `use-component-view-encapsulation` | Disallows ViewEncapsulation.None | |
| `use-injectable-provided-in` | Use providedIn for tree-shakeable Injectables | |
| `use-lifecycle-interface` | Implement lifecycle interfaces for declared hooks | Yes |
| `use-pipe-transform-interface` | Pipes must implement PipeTransform interface | Yes |

### Deprecated (1 Rule)

| Rule | Status |
|------|--------|
| `no-conflicting-lifecycle` | Deprecated, replaced by improved validation |

## Common Rules Explained

### prefer-inject

Recommends using Angular's modern `inject()` function over constructor parameter injection:

```typescript
// Bad - Constructor parameter injection
@Injectable()
class UserService {
  constructor(private http: HttpClient) {}
}

// Good - Modern inject() function
@Injectable()
class UserService {
  private http = inject(HttpClient);
}
```

**Benefits:**
- Enables dependency injection outside constructors
- More concise and less boilerplate
- Works with modern Angular features (signals, functional guards)
- Better tree-shaking

### no-input-rename

Prevents aliasing of @Input bindings to avoid confusion:

```typescript
// Bad - Dual naming is confusing
@Component({})
class MyComponent {
  @Input('userName') name: string;  // Access as 'this.name' but bind as '[userName]'
}

// Good - Same name internally and externally
@Component({})
class MyComponent {
  @Input() name: string;  // Consistent naming
}

// Good - Modern signals approach
@Component({})
class MyComponent {
  name = input<string>();
}
```

### directive-selector and component-selector

Enforces consistent naming for selectors following Angular style guide:

```typescript
// Directive: attribute selectors, camelCase prefix
@Directive({
  selector: '[appHighlight]'  // attr selector, 'app' prefix
})
class HighlightDirective {}

// Component: element selectors, kebab-case prefix
@Component({
  selector: 'app-hero-list'  // element selector, 'app' prefix
})
class HeroListComponent {}
```

### prefer-standalone

Encourages standalone components and directives:

```typescript
// Bad - Module-based approach (legacy)
@Component({
  selector: 'app-hero',
  standalone: false  // or omitted
})
class HeroComponent {}

// Good - Standalone (modern)
@Component({
  selector: 'app-hero',
  standalone: true,
  imports: [CommonModule]
})
class HeroComponent {}
```

### no-output-rename

Prevents aliasing of @Output bindings:

```typescript
// Bad
@Component({})
class MyComponent {
  @Output('customEvent') event = new EventEmitter<any>();
}

// Good
@Component({})
class MyComponent {
  @Output() event = new EventEmitter<any>();
}
```

### use-lifecycle-interface

Ensures lifecycle interface implementation:

```typescript
// Bad - Declares hook without implementing interface
@Component({})
class MyComponent {
  ngOnInit() {
    console.log('initialized');
  }
}

// Good - Implements corresponding interface
@Component({})
class MyComponent implements OnInit {
  ngOnInit() {
    console.log('initialized');
  }
}
```

## Peer Dependencies

- **@typescript-eslint/utils:** ^7.11.0 || ^8.0.0
- **eslint:** ^8.57.0 || ^9.0.0
- **typescript:** * (any version)

## Version Alignment

@angular-eslint packages align major versions with Angular CLI:

- @angular-eslint v18.x.x works with @angular/cli@18.x.x
- @angular-eslint v19.x.x works with @angular/cli@19.x.x
- @angular-eslint v20.x.x works with @angular/cli@20.x.x
- @angular-eslint v21.x.x works with @angular/cli@21.x.x

Minor and patch versions don't need to match exactly.

## Using with Angular CLI

The Angular CLI builder (`@angular-eslint/builder`) automatically executes linting:

```bash
ng lint
```

Or lint a specific project:

```bash
ng lint my-app
```

## Writing Custom Rules

The plugin provides utilities for creating custom rules:

```typescript
import { RuleContext } from '@typescript-eslint/utils/dist/ts-eslint';
import { createESLintRule } from '@angular-eslint/utils';

export const rule = createESLintRule({
  name: 'custom-rule',
  meta: {
    type: 'suggestion',
    docs: {
      description: 'My custom Angular rule',
      recommended: false
    },
    schema: []
  },
  defaultOptions: [],
  create(context: RuleContext<'error', []>) {
    return {
      // Rule implementation
    };
  }
});
```

See `@angular-eslint/utils` and `@angular-eslint/test-utils` for detailed guidance.

## Performance Considerations

- **Type-Aware Rules:** Some rules require TypeScript type information, which adds linting time
- **Configuration:** For best performance in v15+, use the auto-generated configuration
- **Optimization:** See the RULES_REQUIRING_TYPE_INFORMATION guide in the official repository

## Performance Tips

1. Use ESLint v9+ and flat config for better performance
2. Avoid enabling all type-aware rules unless necessary
3. Configure parserOptions.project selectively
4. Use file-level ignores to exclude unnecessary directories

## Related Packages

- **@angular-eslint/eslint-plugin-template:** Rules for Angular HTML templates
- **@angular-eslint/template-parser:** Parser for Angular templates
- **@angular-eslint/builder:** Angular CLI builder for ESLint
- **@angular-eslint/schematics:** Schematics for configuration generation
- **@angular-eslint/utils:** Utilities for rule development
- **@angular-eslint/test-utils:** Testing utilities for custom rules

## Version Support

- **Angular CLI:** v12.0.0 and above (major version alignment as of v12)
- **ESLint:** v8.57.0 or v9.0.0+
- **TypeScript ESLint:** v7.11.0 or v8.0.0+
- **TypeScript:** Any version

## Features Summary

The plugin enforces:
- **Component best practices:** Selector conventions, change detection, view encapsulation
- **Directive best practices:** Selector naming, proper decorator usage
- **Service/Injectable best practices:** Proper providedIn configuration
- **Lifecycle management:** Hook ordering, proper interface implementation, avoiding async hooks
- **Dependency injection:** Preferring inject() over constructor parameters
- **Modern Angular:** Signals, standalone components, model two-way binding
- **Template integration:** When used with @angular-eslint/eslint-plugin-template

## Resources

- **Official Documentation:** https://github.com/angular-eslint/angular-eslint
- **Angular Style Guide:** https://angular.dev/style-guide
- **NPM Package:** https://www.npmjs.com/package/@angular-eslint/eslint-plugin
- **Rules Reference:** Individual rule documentation in the repository
- **Migration Guide:** From Codelyzer and TSLint to Angular ESLint

## License

MIT - See repository for full license
