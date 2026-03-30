# Markers and fixtures

There are some builtin markers and fixtures in `pytest-cov`.

## Markers

### `no_cover`

Eg:

```
@pytest.mark.no_cover
def test_foobar():
    # do some stuff that needs coverage disabled

```
