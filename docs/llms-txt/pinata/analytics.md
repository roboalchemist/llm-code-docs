# Source: https://docs.pinata.cloud/sdk/types/analytics.md

# Analytics

### AnalyticsQuery

```typescript  theme={null}
export type AnalyticsQuery = {
	gateway_domain: string;
	start_date: string;
	end_date: string;
	cid?: string;
	file_name?: string;
	user_agent?: string;
	country?: string;
	region?: string;
	referer?: string;
	limit?: number;
	sort_order?: "asc" | "desc";
};
```

### TopAnalyticsQuery

```typescript  theme={null}
export type TopAnalyticsQuery = AnalyticsQuery & {
	sort_by: "requests" | "bandwidth";
	attribute:
		| "cid"
		| "country"
		| "region"
		| "user_agent"
		| "referer"
		| "file_name";
};
```

### TopAnalyticsResponse

```typescript  theme={null}
export type TopAnalyticsResponse = {
	data: TopAnalyticsItem[];
};
```

### TopAnalyticsItem

```typescript  theme={null}
export type TopAnalyticsItem = {
	value: string;
	requests: number;
	bandwidth: number;
};
```

### TimeIntervalAnalyticsQuery

```typescript  theme={null}
export type TimeIntervalAnalyticsQuery = AnalyticsQuery & {
	sort_by?: "requests" | "bandwidth";
	date_interval: "day" | "week";
};
```

### TimePeriodItem

```typescript  theme={null}
export type TimePeriodItem = {
	period_start_time: string;
	requests: number;
	bandwidth: number;
};
```

### TimeIntervalAnalyticsResponse

```typescript  theme={null}
export type TimeIntervalAnalyticsResponse = {
	total_requests: number;
	total_bandwidth: number;
	time_periods: TimePeriodItem[];
};
```

### UserPinnedDataResponse

```typescript  theme={null}
export type UserPinnedDataResponse = {
	pin_count: number;
	pin_size_total: number;
	pin_size_with_replications_total: number;
};
```
