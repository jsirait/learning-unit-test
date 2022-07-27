# task 1
laps = 45
FuelRequirement = 2.25 * laps
print("fuel req: " + str(FuelRequirement))

qualifying = 80.45
additional_time = (FuelRequirement + 0.5*FuelRequirement - 5) * (0.35/10)
first_lap_time = qualifying + additional_time
print(first_lap_time)
