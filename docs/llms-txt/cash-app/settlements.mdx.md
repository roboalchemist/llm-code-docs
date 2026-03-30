# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/resources/frequently-asked-questions/settlements.mdx

***

## stoplight-id: 3375bd393e73a

# FAQ: Settlements

**Q: When are settlement reports uploaded?**

**A:** Our settlement jobs start running at 23:00 UTC. This is done via a SFTP file upload.

***

**Q: Do settlements include payments, refunds, and disputes?**

**A:** Yes, Cash App provides a net settlement process, deducting refund and dispute amounts from captured payment amounts.
Each net settlement will have a corresponding reconciliation report showing the amount of each payment, applicable fees, refunds, and dispute-related adjustments used in the calculation of the settlement amount. This report is delivered daily via SFTP to the PSP.
