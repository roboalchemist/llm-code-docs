# Source: https://python.useinstructor.com/concepts/enums/index.md

To prevent data misalignment, we can use Enums for standardized fields. Always include an "Other" option as a fallback so the model can signal uncertainty.

```python
from pydantic import BaseModel, Field
from enum import Enum


class Role(Enum):
    PRINCIPAL = "PRINCIPAL"
    TEACHER = "TEACHER"
    STUDENT = "STUDENT"
    OTHER = "OTHER"


class UserDetail(BaseModel):
    age: int
    name: str
    role: Role = Field(
        description="Correctly assign one of the predefined roles to the user."
    )
```

If you're having a hard time with `Enum` an alternative is to use `Literal` instead.

```python
from typing import Literal
from pydantic import BaseModel


class UserDetail(BaseModel):
    age: int
    name: str
    role: Literal["PRINCIPAL", "TEACHER", "STUDENT", "OTHER"]
```

## See Also

- [Types](https://python.useinstructor.com/concepts/types/index.md) - Working with different data types including Literal
- [Union Types](https://python.useinstructor.com/concepts/unions/index.md) - Using unions with enums for multiple choices
- [Response Models](https://python.useinstructor.com/concepts/models/index.md) - Using enums in Pydantic models
- [Fields](https://python.useinstructor.com/concepts/fields/index.md) - Customizing enum fields with Field metadata
