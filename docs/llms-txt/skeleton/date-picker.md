# Source: https://www.skeleton.dev/docs/svelte/framework-components/date-picker.md

# Source: https://www.skeleton.dev/docs/react/framework-components/date-picker.md

# Date Picker

Select dates from a calendar interface.

```tsx
import { DatePicker, Portal } from '@skeletonlabs/skeleton-react';

export default function Default() {
	return (
		<DatePicker>
			<DatePicker.Label>Choose Date</DatePicker.Label>
			<DatePicker.Control>
				<DatePicker.Input placeholder="mm/dd/yyyy" />
				<DatePicker.Trigger />
			</DatePicker.Control>
			<Portal>
				<DatePicker.Positioner>
					<DatePicker.Content>
						<DatePicker.View view="day">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableHead>
												<DatePicker.TableRow>
													{datePicker.weekDays.map((weekDay, id) => (
														<DatePicker.TableHeader key={id}>{weekDay.short}</DatePicker.TableHeader>
													))}
												</DatePicker.TableRow>
											</DatePicker.TableHead>
											<DatePicker.TableBody>
												{datePicker.weeks.map((week, id) => (
													<DatePicker.TableRow key={id}>
														{week.map((day, id) => (
															<DatePicker.TableCell key={id} value={day}>
																<DatePicker.TableCellTrigger>{day.day}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="month">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getMonthsGrid({ columns: 4, format: 'short' }).map((months, id) => (
													<DatePicker.TableRow key={id}>
														{months.map((month, id) => (
															<DatePicker.TableCell key={id} value={month.value}>
																<DatePicker.TableCellTrigger>{month.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="year">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getYearsGrid({ columns: 4 }).map((years, id) => (
													<DatePicker.TableRow key={id}>
														{years.map((year, id) => (
															<DatePicker.TableCell key={id} value={year.value}>
																<DatePicker.TableCellTrigger>{year.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
					</DatePicker.Content>
				</DatePicker.Positioner>
			</Portal>
		</DatePicker>
	);
}

```

## Usage

Given the scale and scope of the Date Picker component, consider implementing within a local component to add a layer of abstraction. Then utlize the props and event handlers to pass data to and from the component respectively.

## Controlled

Manage the selected date value with controlled state.

```tsx
import { DatePicker, parseDate, Portal } from '@skeletonlabs/skeleton-react';
import { useState } from 'react';

export default function Controlled() {
	const [value, setValue] = useState([parseDate('2025-10-15')]);

	return (
		<DatePicker value={value} onValueChange={(e) => setValue(e.value)}>
			<DatePicker.Label>Picked date: {value.at(0)?.toString()}</DatePicker.Label>
			<DatePicker.Control>
				<DatePicker.Input placeholder="mm/dd/yyyy" />
				<DatePicker.Trigger />
			</DatePicker.Control>
			<Portal>
				<DatePicker.Positioner>
					<DatePicker.Content>
						<DatePicker.View view="day">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableHead>
												<DatePicker.TableRow>
													{datePicker.weekDays.map((weekDay, id) => (
														<DatePicker.TableHeader key={id}>{weekDay.short}</DatePicker.TableHeader>
													))}
												</DatePicker.TableRow>
											</DatePicker.TableHead>
											<DatePicker.TableBody>
												{datePicker.weeks.map((week, id) => (
													<DatePicker.TableRow key={id}>
														{week.map((day, id) => (
															<DatePicker.TableCell key={id} value={day}>
																<DatePicker.TableCellTrigger>{day.day}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="month">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getMonthsGrid({ columns: 4, format: 'short' }).map((months, id) => (
													<DatePicker.TableRow key={id}>
														{months.map((month, id) => (
															<DatePicker.TableCell key={id} value={month.value}>
																<DatePicker.TableCellTrigger>{month.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="year">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getYearsGrid({ columns: 4 }).map((years, id) => (
													<DatePicker.TableRow key={id}>
														{years.map((year, id) => (
															<DatePicker.TableCell key={id} value={year.value}>
																<DatePicker.TableCellTrigger>{year.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
					</DatePicker.Content>
				</DatePicker.Positioner>
			</Portal>
		</DatePicker>
	);
}

```

## Disabled

Disable the date picker to prevent user interaction.

```tsx
import { DatePicker, Portal } from '@skeletonlabs/skeleton-react';

export default function Disabled() {
	return (
		<DatePicker disabled>
			<DatePicker.Label>Choose Date</DatePicker.Label>
			<DatePicker.Control>
				<DatePicker.Input placeholder="mm/dd/yyyy" />
				<DatePicker.Trigger />
			</DatePicker.Control>
			<Portal>
				<DatePicker.Positioner>
					<DatePicker.Content>
						<DatePicker.View view="day">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableHead>
												<DatePicker.TableRow>
													{datePicker.weekDays.map((weekDay, id) => (
														<DatePicker.TableHeader key={id}>{weekDay.short}</DatePicker.TableHeader>
													))}
												</DatePicker.TableRow>
											</DatePicker.TableHead>
											<DatePicker.TableBody>
												{datePicker.weeks.map((week, id) => (
													<DatePicker.TableRow key={id}>
														{week.map((day, id) => (
															<DatePicker.TableCell key={id} value={day}>
																<DatePicker.TableCellTrigger>{day.day}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="month">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getMonthsGrid({ columns: 4, format: 'short' }).map((months, id) => (
													<DatePicker.TableRow key={id}>
														{months.map((month, id) => (
															<DatePicker.TableCell key={id} value={month.value}>
																<DatePicker.TableCellTrigger>{month.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="year">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getYearsGrid({ columns: 4 }).map((years, id) => (
													<DatePicker.TableRow key={id}>
														{years.map((year, id) => (
															<DatePicker.TableCell key={id} value={year.value}>
																<DatePicker.TableCellTrigger>{year.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
					</DatePicker.Content>
				</DatePicker.Positioner>
			</Portal>
		</DatePicker>
	);
}

```

## Minimum and Maximum

Restrict date selection to a specific range using the `min` and `max` props with the `parseDate` helper function.

```tsx
import { DatePicker, parseDate, Portal } from '@skeletonlabs/skeleton-react';

export default function MinMax() {
	const currentDate = new Date();
	const currentYear = currentDate.getFullYear();

	return (
		<DatePicker min={parseDate(`${currentYear}-01-01`)} max={parseDate(`${currentYear}-12-31`)}>
			<DatePicker.Label>Choose Date</DatePicker.Label>
			<DatePicker.Control>
				<DatePicker.Input placeholder="mm/dd/yyyy" />
				<DatePicker.Trigger />
			</DatePicker.Control>
			<Portal>
				<DatePicker.Positioner>
					<DatePicker.Content>
						<DatePicker.View view="day">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableHead>
												<DatePicker.TableRow>
													{datePicker.weekDays.map((weekDay, id) => (
														<DatePicker.TableHeader key={id}>{weekDay.short}</DatePicker.TableHeader>
													))}
												</DatePicker.TableRow>
											</DatePicker.TableHead>
											<DatePicker.TableBody>
												{datePicker.weeks.map((week, id) => (
													<DatePicker.TableRow key={id}>
														{week.map((day, id) => (
															<DatePicker.TableCell key={id} value={day}>
																<DatePicker.TableCellTrigger>{day.day}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="month">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getMonthsGrid({ columns: 4, format: 'short' }).map((months, id) => (
													<DatePicker.TableRow key={id}>
														{months.map((month, id) => (
															<DatePicker.TableCell key={id} value={month.value}>
																<DatePicker.TableCellTrigger>{month.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="year">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getYearsGrid({ columns: 4 }).map((years, id) => (
													<DatePicker.TableRow key={id}>
														{years.map((year, id) => (
															<DatePicker.TableCell key={id} value={year.value}>
																<DatePicker.TableCellTrigger>{year.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
					</DatePicker.Content>
				</DatePicker.Positioner>
			</Portal>
		</DatePicker>
	);
}

```

## Range Selection

Enable range selection by setting `selectionMode="range"` on the root component. Pair with two inputs fields:

* `index={0}` to represent the start dates.
* `index={1}` to represent the end dates.

```tsx
import { DatePicker, Portal } from '@skeletonlabs/skeleton-react';

export default function Range() {
	return (
		<DatePicker selectionMode="range">
			<DatePicker.Label>Select Date Range</DatePicker.Label>
			<DatePicker.Control>
				<DatePicker.Input index={0} placeholder="Start date..." />
				<DatePicker.Input index={1} placeholder="End date..." />
				<DatePicker.Trigger />
			</DatePicker.Control>
			<Portal>
				<DatePicker.Positioner>
					<DatePicker.Content>
						<DatePicker.View view="day">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableHead>
												<DatePicker.TableRow>
													{datePicker.weekDays.map((weekDay, id) => (
														<DatePicker.TableHeader key={id}>{weekDay.short}</DatePicker.TableHeader>
													))}
												</DatePicker.TableRow>
											</DatePicker.TableHead>
											<DatePicker.TableBody>
												{datePicker.weeks.map((week, id) => (
													<DatePicker.TableRow key={id}>
														{week.map((day, id) => (
															<DatePicker.TableCell key={id} value={day}>
																<DatePicker.TableCellTrigger>{day.day}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="month">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getMonthsGrid({ columns: 4, format: 'short' }).map((months, id) => (
													<DatePicker.TableRow key={id}>
														{months.map((month, id) => (
															<DatePicker.TableCell key={id} value={month.value}>
																<DatePicker.TableCellTrigger>{month.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="year">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getYearsGrid({ columns: 4 }).map((years, id) => (
													<DatePicker.TableRow key={id}>
														{years.map((year, id) => (
															<DatePicker.TableCell key={id} value={year.value}>
																<DatePicker.TableCellTrigger>{year.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
					</DatePicker.Content>
				</DatePicker.Positioner>
			</Portal>
		</DatePicker>
	);
}

```

### Presets

Use the `PresetTrigger` component to allow users to quickly select predefined date ranges.

```tsx
import { DatePicker, Portal } from '@skeletonlabs/skeleton-react';

export default function Presets() {
	return (
		<DatePicker selectionMode="range">
			<DatePicker.Label>Select Date Range</DatePicker.Label>
			<DatePicker.Control>
				<DatePicker.Input index={0} placeholder="Start date..." />
				<DatePicker.Input index={1} placeholder="End date..." />
				<DatePicker.Trigger />
			</DatePicker.Control>
			<Portal>
				<DatePicker.Positioner>
					<DatePicker.Content>
						<DatePicker.View view="day">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<div className="flex gap-2">
											<DatePicker.PresetTrigger value="last3Days">Last 3 Days</DatePicker.PresetTrigger>
											<DatePicker.PresetTrigger value="last7Days">Last 7 Days</DatePicker.PresetTrigger>
											<DatePicker.PresetTrigger value="last30Days">Last 30 Days</DatePicker.PresetTrigger>
										</div>
										<DatePicker.Table>
											<DatePicker.TableHead>
												<DatePicker.TableRow>
													{datePicker.weekDays.map((weekDay, id) => (
														<DatePicker.TableHeader key={id}>{weekDay.short}</DatePicker.TableHeader>
													))}
												</DatePicker.TableRow>
											</DatePicker.TableHead>
											<DatePicker.TableBody>
												{datePicker.weeks.map((week, id) => (
													<DatePicker.TableRow key={id}>
														{week.map((day, id) => (
															<DatePicker.TableCell key={id} value={day}>
																<DatePicker.TableCellTrigger>{day.day}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="month">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getMonthsGrid({ columns: 4, format: 'short' }).map((months, id) => (
													<DatePicker.TableRow key={id}>
														{months.map((month, id) => (
															<DatePicker.TableCell key={id} value={month.value}>
																<DatePicker.TableCellTrigger>{month.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="year">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getYearsGrid({ columns: 4 }).map((years, id) => (
													<DatePicker.TableRow key={id}>
														{years.map((year, id) => (
															<DatePicker.TableCell key={id} value={year.value}>
																<DatePicker.TableCellTrigger>{year.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
					</DatePicker.Content>
				</DatePicker.Positioner>
			</Portal>
		</DatePicker>
	);
}

```

## Inline calendar

Display the calendar inline without a popover by adding the `inline` prop to the root component. When using inline mode, omit the `Portal` and `Positioner` components.

```tsx
import { DatePicker } from '@skeletonlabs/skeleton-react';

export default function Inline() {
	return (
		<DatePicker inline>
			<DatePicker.Label>Choose Date</DatePicker.Label>
			<DatePicker.Content>
				<DatePicker.View view="day">
					<DatePicker.Context>
						{(datePicker) => (
							<>
								<DatePicker.ViewControl>
									<DatePicker.PrevTrigger />
									<DatePicker.ViewTrigger>
										<DatePicker.RangeText />
									</DatePicker.ViewTrigger>
									<DatePicker.NextTrigger />
								</DatePicker.ViewControl>
								<DatePicker.Table>
									<DatePicker.TableHead>
										<DatePicker.TableRow>
											{datePicker.weekDays.map((weekDay, id) => (
												<DatePicker.TableHeader key={id}>{weekDay.short}</DatePicker.TableHeader>
											))}
										</DatePicker.TableRow>
									</DatePicker.TableHead>
									<DatePicker.TableBody>
										{datePicker.weeks.map((week, id) => (
											<DatePicker.TableRow key={id}>
												{week.map((day, id) => (
													<DatePicker.TableCell key={id} value={day}>
														<DatePicker.TableCellTrigger>{day.day}</DatePicker.TableCellTrigger>
													</DatePicker.TableCell>
												))}
											</DatePicker.TableRow>
										))}
									</DatePicker.TableBody>
								</DatePicker.Table>
							</>
						)}
					</DatePicker.Context>
				</DatePicker.View>
				<DatePicker.View view="month">
					<DatePicker.Context>
						{(datePicker) => (
							<>
								<DatePicker.ViewControl>
									<DatePicker.PrevTrigger />
									<DatePicker.ViewTrigger>
										<DatePicker.RangeText />
									</DatePicker.ViewTrigger>
									<DatePicker.NextTrigger />
								</DatePicker.ViewControl>
								<DatePicker.Table>
									<DatePicker.TableBody>
										{datePicker.getMonthsGrid({ columns: 4, format: 'short' }).map((months, id) => (
											<DatePicker.TableRow key={id}>
												{months.map((month, id) => (
													<DatePicker.TableCell key={id} value={month.value}>
														<DatePicker.TableCellTrigger>{month.label}</DatePicker.TableCellTrigger>
													</DatePicker.TableCell>
												))}
											</DatePicker.TableRow>
										))}
									</DatePicker.TableBody>
								</DatePicker.Table>
							</>
						)}
					</DatePicker.Context>
				</DatePicker.View>
				<DatePicker.View view="year">
					<DatePicker.Context>
						{(datePicker) => (
							<>
								<DatePicker.ViewControl>
									<DatePicker.PrevTrigger />
									<DatePicker.ViewTrigger>
										<DatePicker.RangeText />
									</DatePicker.ViewTrigger>
									<DatePicker.NextTrigger />
								</DatePicker.ViewControl>
								<DatePicker.Table>
									<DatePicker.TableBody>
										{datePicker.getYearsGrid({ columns: 4 }).map((years, id) => (
											<DatePicker.TableRow key={id}>
												{years.map((year, id) => (
													<DatePicker.TableCell key={id} value={year.value}>
														<DatePicker.TableCellTrigger>{year.label}</DatePicker.TableCellTrigger>
													</DatePicker.TableCell>
												))}
											</DatePicker.TableRow>
										))}
									</DatePicker.TableBody>
								</DatePicker.Table>
							</>
						)}
					</DatePicker.Context>
				</DatePicker.View>
			</DatePicker.Content>
		</DatePicker>
	);
}

```

## Month and Year Selection

Add `MonthSelect` and `YearSelect` components to provide selectors for quickly changing the month and year.

```tsx
import { DatePicker, Portal } from '@skeletonlabs/skeleton-react';

export default function WithSelects() {
	return (
		<DatePicker>
			<DatePicker.Label>Choose Date</DatePicker.Label>
			<DatePicker.Control>
				<DatePicker.Input placeholder="mm/dd/yyyy" />
				<DatePicker.Trigger />
			</DatePicker.Control>
			<Portal>
				<DatePicker.Positioner>
					<DatePicker.Content>
						<DatePicker.YearSelect />
						<DatePicker.MonthSelect />
						<DatePicker.View view="day">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger disabled>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableHead>
												<DatePicker.TableRow>
													{datePicker.weekDays.map((weekDay, id) => (
														<DatePicker.TableHeader key={id}>{weekDay.short}</DatePicker.TableHeader>
													))}
												</DatePicker.TableRow>
											</DatePicker.TableHead>
											<DatePicker.TableBody>
												{datePicker.weeks.map((week, id) => (
													<DatePicker.TableRow key={id}>
														{week.map((day, id) => (
															<DatePicker.TableCell key={id} value={day}>
																<DatePicker.TableCellTrigger>{day.day}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="month">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getMonthsGrid({ columns: 4, format: 'short' }).map((months, id) => (
													<DatePicker.TableRow key={id}>
														{months.map((month, id) => (
															<DatePicker.TableCell key={id} value={month.value}>
																<DatePicker.TableCellTrigger>{month.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
						<DatePicker.View view="year">
							<DatePicker.Context>
								{(datePicker) => (
									<>
										<DatePicker.ViewControl>
											<DatePicker.PrevTrigger />
											<DatePicker.ViewTrigger>
												<DatePicker.RangeText />
											</DatePicker.ViewTrigger>
											<DatePicker.NextTrigger />
										</DatePicker.ViewControl>
										<DatePicker.Table>
											<DatePicker.TableBody>
												{datePicker.getYearsGrid({ columns: 4 }).map((years, id) => (
													<DatePicker.TableRow key={id}>
														{years.map((year, id) => (
															<DatePicker.TableCell key={id} value={year.value}>
																<DatePicker.TableCellTrigger>{year.label}</DatePicker.TableCellTrigger>
															</DatePicker.TableCell>
														))}
													</DatePicker.TableRow>
												))}
											</DatePicker.TableBody>
										</DatePicker.Table>
									</>
								)}
							</DatePicker.Context>
						</DatePicker.View>
					</DatePicker.Content>
				</DatePicker.Positioner>
			</Portal>
		</DatePicker>
	);
}

```

## Anatomy

Here's an overview of how the DatePicker component is structured in code:

```tsx
import { DatePicker, Portal } from '@skeletonlabs/skeleton-react';

export default function Anatomy() {
	return (
		<DatePicker>
			<DatePicker.Label />
			<DatePicker.Control>
				<DatePicker.Input />
				<DatePicker.Trigger />
			</DatePicker.Control>
			<Portal>
				<DatePicker.Positioner>
					<DatePicker.Content>
						<DatePicker.YearSelect />
						<DatePicker.MonthSelect />
						<DatePicker.View>
							<DatePicker.ViewControl>
								<DatePicker.PrevTrigger />
								<DatePicker.ViewTrigger>
									<DatePicker.RangeText />
								</DatePicker.ViewTrigger>
								<DatePicker.NextTrigger />
							</DatePicker.ViewControl>
							<DatePicker.Table>
								<DatePicker.TableHead>
									<DatePicker.TableRow>
										<DatePicker.TableHeader />
									</DatePicker.TableRow>
								</DatePicker.TableHead>
								<DatePicker.TableBody>
									<DatePicker.TableRow>
										<DatePicker.TableCell>
											<DatePicker.TableCellTrigger />
										</DatePicker.TableCell>
									</DatePicker.TableRow>
								</DatePicker.TableBody>
							</DatePicker.Table>
						</DatePicker.View>
					</DatePicker.Content>
				</DatePicker.Positioner>
			</Portal>
		</DatePicker>
	);
}
```

## API Reference

### Root

| Prop                 | Description                                                                                                                                                                                             | Type                                                                                                                                                                                                                                                      | Default  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| locale               | The locale (BCP 47 language tag) to use when formatting the date.                                                                                                                                       | string \| undefined                                                                                                                                                                                                                                       | "en-US"  |
| createCalendar       | A function that creates a Calendar object for a given calendar identifier.&#xA;Enables non-Gregorian calendar support (Persian, Buddhist, Islamic, etc.)&#xA;without bundling all calendars by default. | ((identifier: CalendarIdentifier) => Calendar) \| undefined                                                                                                                                                                                               | -        |
| translations         | The localized messages to use.                                                                                                                                                                          | IntlTranslations \| undefined                                                                                                                                                                                                                             | -        |
| ids                  | The ids of the elements in the date picker. Useful for composition.                                                                                                                                     | Partial\<\{ root: string; label: (index: number) => string; table: (id: string) => string; tableHeader: (id: string) => string; tableBody: (id: string) => string; tableRow: (id: string) => string; ... 11 more ...; positioner: string; }> \| undefined | -        |
| name                 | The \`name\` attribute of the input element.                                                                                                                                                            | string \| undefined                                                                                                                                                                                                                                       | -        |
| timeZone             | The time zone to use                                                                                                                                                                                    | string \| undefined                                                                                                                                                                                                                                       | "UTC"    |
| disabled             | Whether the calendar is disabled.                                                                                                                                                                       | boolean \| undefined                                                                                                                                                                                                                                      | -        |
| readOnly             | Whether the calendar is read-only.                                                                                                                                                                      | boolean \| undefined                                                                                                                                                                                                                                      | -        |
| required             | Whether the date picker is required                                                                                                                                                                     | boolean \| undefined                                                                                                                                                                                                                                      | -        |
| invalid              | Whether the date picker is invalid                                                                                                                                                                      | boolean \| undefined                                                                                                                                                                                                                                      | -        |
| outsideDaySelectable | Whether day outside the visible range can be selected.                                                                                                                                                  | boolean \| undefined                                                                                                                                                                                                                                      | false    |
| min                  | The minimum date that can be selected.                                                                                                                                                                  | DateValue \| undefined                                                                                                                                                                                                                                    | -        |
| max                  | The maximum date that can be selected.                                                                                                                                                                  | DateValue \| undefined                                                                                                                                                                                                                                    | -        |
| closeOnSelect        | Whether the calendar should close after the date selection is complete.&#xA;This is ignored when the selection mode is \`multiple\`.                                                                    | boolean \| undefined                                                                                                                                                                                                                                      | true     |
| openOnClick          | Whether to open the calendar when the input is clicked.                                                                                                                                                 | boolean \| undefined                                                                                                                                                                                                                                      | false    |
| value                | The controlled selected date(s).                                                                                                                                                                        | DateValue\[] \| undefined                                                                                                                                                                                                                                 | -        |
| defaultValue         | The initial selected date(s) when rendered.&#xA;Use when you don't need to control the selected date(s) of the date picker.                                                                             | DateValue\[] \| undefined                                                                                                                                                                                                                                 | -        |
| focusedValue         | The controlled focused date.                                                                                                                                                                            | DateValue \| undefined                                                                                                                                                                                                                                    | -        |
| defaultFocusedValue  | The initial focused date when rendered.&#xA;Use when you don't need to control the focused date of the date picker.                                                                                     | DateValue \| undefined                                                                                                                                                                                                                                    | -        |
| numOfMonths          | The number of months to display.                                                                                                                                                                        | number \| undefined                                                                                                                                                                                                                                       | -        |
| startOfWeek          | The first day of the week.&#xA; \`0\` - Sunday&#xA; \`1\` - Monday&#xA; \`2\` - Tuesday&#xA; \`3\` - Wednesday&#xA; \`4\` - Thursday&#xA; \`5\` - Friday&#xA; \`6\` - Saturday                          | number \| undefined                                                                                                                                                                                                                                       | -        |
| fixedWeeks           | Whether the calendar should have a fixed number of weeks.&#xA;This renders the calendar with 6 weeks instead of 5 or 6.                                                                                 | boolean \| undefined                                                                                                                                                                                                                                      | -        |
| showWeekNumbers      | Whether to show the week number column in the day view.                                                                                                                                                 | boolean \| undefined                                                                                                                                                                                                                                      | -        |
| onValueChange        | Function called when the value changes.                                                                                                                                                                 | ((details: ValueChangeDetails) => void) \| undefined                                                                                                                                                                                                      | -        |
| onFocusChange        | Function called when the focused date changes.                                                                                                                                                          | ((details: FocusChangeDetails) => void) \| undefined                                                                                                                                                                                                      | -        |
| onViewChange         | Function called when the view changes.                                                                                                                                                                  | ((details: ViewChangeDetails) => void) \| undefined                                                                                                                                                                                                       | -        |
| onVisibleRangeChange | Function called when the visible range changes.                                                                                                                                                         | ((details: VisibleRangeChangeDetails) => void) \| undefined                                                                                                                                                                                               | -        |
| onOpenChange         | Function called when the calendar opens or closes.                                                                                                                                                      | ((details: OpenChangeDetails) => void) \| undefined                                                                                                                                                                                                       | -        |
| isDateUnavailable    | Returns whether a date of the calendar is available.                                                                                                                                                    | ((date: DateValue, locale: string) => boolean) \| undefined                                                                                                                                                                                               | -        |
| selectionMode        | The selection mode of the calendar.&#xA;- \`single\` - only one date can be selected&#xA;- \`multiple\` - multiple dates can be selected&#xA;- \`range\` - a range of dates can be selected             | SelectionMode \| undefined                                                                                                                                                                                                                                | "single" |
| maxSelectedDates     | The maximum number of dates that can be selected.&#xA;This is only applicable when \`selectionMode\` is \`multiple\`.                                                                                   | number \| undefined                                                                                                                                                                                                                                       | -        |
| format               | The format of the date to display in the input.                                                                                                                                                         | ((date: DateValue, details: LocaleDetails) => string) \| undefined                                                                                                                                                                                        | -        |
| parse                | Function to parse the date from the input back to a DateValue.                                                                                                                                          | ((value: string, details: LocaleDetails) => DateValue \| undefined) \| undefined                                                                                                                                                                          | -        |
| placeholder          | The placeholder text to display in the input.                                                                                                                                                           | string \| undefined                                                                                                                                                                                                                                       | -        |
| view                 | The view of the calendar                                                                                                                                                                                | DateView \| undefined                                                                                                                                                                                                                                     | -        |
| defaultView          | The default view of the calendar                                                                                                                                                                        | DateView \| undefined                                                                                                                                                                                                                                     | "day"    |
| minView              | The minimum view of the calendar                                                                                                                                                                        | DateView \| undefined                                                                                                                                                                                                                                     | "day"    |
| maxView              | The maximum view of the calendar                                                                                                                                                                        | DateView \| undefined                                                                                                                                                                                                                                     | "year"   |
| positioning          | The user provided options used to position the date picker content                                                                                                                                      | PositioningOptions \| undefined                                                                                                                                                                                                                           | -        |
| open                 | The controlled open state of the date picker                                                                                                                                                            | boolean \| undefined                                                                                                                                                                                                                                      | -        |
| defaultOpen          | The initial open state of the date picker when rendered.&#xA;Use when you don't need to control the open state of the date picker.                                                                      | boolean \| undefined                                                                                                                                                                                                                                      | -        |
| inline               | Whether to render the date picker inline                                                                                                                                                                | boolean \| undefined                                                                                                                                                                                                                                      | -        |
| dir                  | The document's text/writing direction.                                                                                                                                                                  | "ltr" \| "rtl" \| undefined                                                                                                                                                                                                                               | "ltr"    |
| getRootNode          | A root node to correctly resolve document in custom environments. E.x.: Iframes, Electron.                                                                                                              | (() => ShadowRoot \| Node \| Document) \| undefined                                                                                                                                                                                                       | -        |
| element              | Render the element yourself                                                                                                                                                                             | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined                                                                                                                                                                                            | -        |

### Provider

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| value   | -                           | DatePickerApi\<PropTypes>                                      | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Context

| Prop     | Description | Type                                                 | Default |
| -------- | ----------- | ---------------------------------------------------- | ------- |
| children | -           | (datePicker: DatePickerApi\<PropTypes>) => ReactNode | -       |

### Label

| Prop    | Description                 | Type                                                             | Default |
| ------- | --------------------------- | ---------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"label">) => Element) \| undefined | -       |

### Control

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### PresetTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| value   | -                           | PresetTriggerValue                                                | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Input

| Prop      | Description                             | Type                                                             | Default |
| --------- | --------------------------------------- | ---------------------------------------------------------------- | ------- |
| index     | The index of the input to focus.        | number \| undefined                                              | -       |
| fixOnBlur | Whether to fix the input value on blur. | boolean \| undefined                                             | true    |
| element   | Render the element yourself             | ((attributes: HTMLAttributes\<"input">) => Element) \| undefined | -       |

### Trigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Positioner

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### Content

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### YearSelect

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"select">) => Element) \| undefined | -       |

### MonthSelect

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"select">) => Element) \| undefined | -       |

### View

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| view    | -                           | DateView \| undefined                                          | -       |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### ViewControl

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### PrevTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### ViewTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### RangeText

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |

### NextTrigger

| Prop    | Description                 | Type                                                              | Default |
| ------- | --------------------------- | ----------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"button">) => Element) \| undefined | -       |

### Table

| Prop    | Description                 | Type                                                             | Default |
| ------- | --------------------------- | ---------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"table">) => Element) \| undefined | -       |

### TableHead

| Prop    | Description                 | Type                                                             | Default |
| ------- | --------------------------- | ---------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"thead">) => Element) \| undefined | -       |

### TableRow

| Prop    | Description                 | Type                                                          | Default |
| ------- | --------------------------- | ------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"tr">) => Element) \| undefined | -       |

### TableHeader

| Prop    | Description                 | Type                                                          | Default |
| ------- | --------------------------- | ------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"th">) => Element) \| undefined | -       |

### TableBody

| Prop    | Description                 | Type                                                             | Default |
| ------- | --------------------------- | ---------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"tbody">) => Element) \| undefined | -       |

### TableCell

| Prop         | Description                 | Type                                                          | Default |
| ------------ | --------------------------- | ------------------------------------------------------------- | ------- |
| disabled     | -                           | boolean \| undefined                                          | -       |
| value        | -                           | number \| DateValue                                           | -       |
| columns      | -                           | number \| undefined                                           | -       |
| visibleRange | -                           | VisibleRange \| undefined                                     | -       |
| element      | Render the element yourself | ((attributes: HTMLAttributes\<"td">) => Element) \| undefined | -       |

### TableCellTrigger

| Prop    | Description                 | Type                                                           | Default |
| ------- | --------------------------- | -------------------------------------------------------------- | ------- |
| element | Render the element yourself | ((attributes: HTMLAttributes\<"div">) => Element) \| undefined | -       |
