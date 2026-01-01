# Source: https://documentation.mailgun.com/docs/mailgun/user-manual/subaccounts/subaccounts-ip-pools.md

# Subaccounts and IP Pools

As a primary account admin you can manage the IP Pools that will be used by your subaccounts in one of three ways.

1. Define IP pool at send time - The primary account can use the header X-Mailgun-Sending-Ip-Pool and the pool ID of the IP pool contained on the primary account.
2. Delegate IP Pool to subaccount - During either the creation or later editing the details of the subaccount from the primary account UI, an admin can define a single IP pool for use by the subaccount. The IP pool can then be assigned to any sending domain contained on the subaccount.
3. Add DYIPP (Dynamic IP Pools) to their subaccount - The primary account admin has the option to enable and assign DYIPP for the entire subaccount or assign to individual domains within a subaccount.