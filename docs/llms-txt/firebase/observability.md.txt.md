# Source: https://firebase.google.com/docs/phone-number-verification/observability.md.txt

<br />

Firebase PNV integrates with Cloud Monitoring.

## Google Cloud Monitoring

Firebase PNV exports a single metric, `fpnv.googleapis.com/verification_count`, with
the labels `method`, `outcome`, `region_code`, and `platform`:

| Metric type ^Launch stage^ *(Resource hierarchy levels)* Display name ||
| Kind, Type, Unit Monitored resources | *Description* Labels |
|---|---|
| `fpnv.googleapis.com/verification_count` ^BETA^  ***(project)*** Firebase Phone Number Verification Metrics ||
| `DELTA`, `INT64`, `1` **fpnv.googleapis.com/Project** | *Number of phone number verification attempts.* `method`: Verification method used. Always `API`. `outcome`: The outcome of the verification attempt (`SUCCESS`, `FAILURE`, `QUOTA_EXCEEDED`, `BACKEND_ERROR`). `region_code`: The two-letter region code for the phone number. `platform`: The platform where verification was requested. |