<!-- Source: https://namespace.so/docs/reference/cli/auth-check-login -->

# nsc auth check-login

Return a successful exit code if the caller is still authenticated to Namespace.

`nsc auth check-login` verifies that you are currently authenticated and that your session is still valid.
When everything is valid, it exits with code 0. When there is a problem it will exit with a non-zero exit code.

This is useful for scripts that need to check for a valid login.

## Usage

```
nsc auth check-login [--duration duration]
```

### Examples

#### Logged in:

```
$ nsc auth check-login
# Exit code 0
```

#### Not logged in:

```
$ nsc auth check-login
Failed:
Jul  8 11:48:14.098 UTC nsc.fetch-token waited=3us
not logged in
 
please run `nsc login`
 
# Exit code 1
```

## Options

### --duration

Fail if the current session does not last at least this much more time. Defaults to 5 minutes.

Last updated July 8, 2025
