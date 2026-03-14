# Module: Dry::Validation::Hints
  
    Defined in:
    lib/dry/validation/extensions/hints.rb
  
## Overview

Hints extension

#### Examples

```
Dry::Validation.load_extensions(:hints)

contract = Dry::Validation::Contract.build do
  schema do
    required(:name).filled(:string, min_size?: 2..4)
  end
end

contract.call(name: "fo").hints
# {:name=>["size must be within 2 - 4"]}

contract.call(name: "").messages
# {:name=>["must be filled", "size must be within 2 - 4"]}
```

## Defined Under Namespace

      **Modules:** ResultExtensions
