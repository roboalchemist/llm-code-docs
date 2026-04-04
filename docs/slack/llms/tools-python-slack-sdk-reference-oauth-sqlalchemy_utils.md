Source: https://docs.slack.dev/tools/python-slack-sdk/reference/oauth/sqlalchemy_utils

# Module slack_sdk.oauth.sqlalchemy_utils

## Functions

`def normalize_datetime_for_db(dt: datetime.datetime | None) ‑> datetime.datetime | None`

Expand source code

```python
def normalize_datetime_for_db(dt: Optional[datetime]) -> Optional[datetime]:
    """
    Normalize timezone-aware datetime to naive UTC datetime for database storage.

    Ensures compatibility with existing databases using TIMESTAMP WITHOUT TIME ZONE.
    SQLAlchemy DateTime columns without timezone=True create naive timestamp columns
    in databases like PostgreSQL. This function strips timezone information from
    timezone-aware datetimes (which are already in UTC) to enable safe comparisons.

    Args:
        dt: A timezone-aware or naive datetime object, or None

    Returns:
        A naive datetime in UTC, or None if input is None

    Example:
        >>> from datetime import datetime, timezone
        >>> aware_dt = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
        >>> naive_dt = normalize_datetime_for_db(aware_dt)
        >>> naive_dt.tzinfo is None
        True
    """
    if dt is None:
        return None
    if dt.tzinfo is not None:
        return dt.replace(tzinfo=None)
    return dt
```

Normalize timezone-aware datetime to naive UTC datetime for database storage.

Ensures compatibility with existing databases using TIMESTAMP WITHOUT TIME ZONE. SQLAlchemy DateTime columns without timezone=True create naive timestamp columns in databases like PostgreSQL. This function strips timezone information from timezone-aware datetimes (which are already in UTC) to enable safe comparisons.

## Args

**`dt`**

A timezone-aware or naive datetime object, or None

## Returns

A naive datetime in UTC, or None if input is None

## Example

```python-repl
>>> from datetime import datetime, timezone
>>> aware_dt = datetime(2024, 1, 1, 12, 0, 0, tzinfo=timezone.utc)
>>> naive_dt = normalize_datetime_for_db(aware_dt)
>>> naive_dt.tzinfo is None
True
```
