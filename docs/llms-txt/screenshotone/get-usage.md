# Source: https://screenshotone.com/docs/get-usage/

# Get Usage

You can get your current plan usage by:

```
GET https://api.screenshotone.com/usage?access_key=<YOUR ACCESS KEY>`

{
    "total": 10000, 
    "available: 950, 
    "used": 9050,
    "concurrency": {
        "limit":20,
        "remaining":20,
        "reset":1681646947775437264
    }
}
```

A bit of clarification: 

- `total` is the total number of requests allowed in the current billing plan period;
- `available` is the number of available requests until the end of the current period;
- `used` is the number of successfully executed requests.
- `concurrency.limit` is the total number of concurrent requests allowed per interval;
- `concurrency.remaining` is the number of available concurrent requests allowed per interval;
- `concurrency.reset` is the time when the limitation will be reset, in UNIX timestamp format in nanoseconds.