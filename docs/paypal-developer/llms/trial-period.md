# Offer a Trial Period

Use a trial period to let subscribers try your product at a free or discounted price before regular billing cycles start. After the trial period ends, the regular billing period for the subscription begins. You can have up to 2 trial periods per plan.

The following sample requests show how to offer trial periods. Use these samples to adjust your code when you create a plan.

## Example: Music Service

The following example creates a trial period with the following characteristics:

- $0 for the first month.
- $15 per month following the trial period.

```bash
curl -v –X POST https://api-m.sandbox.paypal.com/v1/billing/plans \
-H "Accept: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN" \
-H "Content-Type: application/json" \
-H "PayPal-Request-Id: PLAN-18062020-002" \
-d '{"name": "Premium Music Plus", "description": "A premium plan with music download feature", "product_id": "PROD-5RN21878H3527870P", "billing_cycles": [{"frequency": {"interval_unit": "MONTH", "interval_count": 1}, "tenure_type": "TRIAL", "sequence": 1, "total_cycles": 1, "pricing_scheme": {"fixed_price": {"value": "0", "currency_code": "USD"}}}], "payment_preferences": {"auto_bill_outstanding": true, "payment_failure_threshold": 1}}'
```

## Example: Online Tutorial Service

The following example creates a trial period with the following characteristics:

- $0 free trial for the first week.
- $5 per week discounted trial for the next 3 weeks.
- $10 per week following the trial period.

```bash
curl -v –X POST https://api-m.sandbox.paypal.com/v1/billing/plans \
-H "Accept: application/json" \
-H "Authorization: Bearer ACCESS-TOKEN" \
-H "Content-Type: application/json" \
-H "PayPal-Request-Id: PLAN-18062020-003" \
-d '{"name": "Music Tutorial Premium Plus", "description": "Offering a premium music tutorial with download feature", "product_id": "PROD-5RN21878H3527870P", "billing_cycles": [{"frequency": {"interval_unit": "WEEK", "interval_count": 1}, "tenure_type": "TRIAL", "sequence": 1, "total_cycles": 1, "pricing_scheme": {"fixed_price": {"value": "0", "currency_code": "USD"}}}], "payment_preferences": {"auto_bill_outstanding": true, "payment_failure_threshold": 1}}'