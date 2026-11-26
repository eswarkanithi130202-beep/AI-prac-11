# Logical inference using propositional logic
# Facts
rain = True
cloudy = True

# Rules
if rain:
    road_wet = True
else:
    road_wet = False

if road_wet:
    drive_carefully = True
else:
    drive_carefully = False

if cloudy and rain:
    carry_umbrella = True
else:
    carry_umbrella = False

# Display facts and conclusions
print("AI Logical Reasoning System")
print("Rain:", rain)
print("Cloudy:", cloudy)
print("\nInferred Conclusions:")
print("Road is wet:", road_wet)
print("Drive carefully:", drive_carefully)
print("Carry umbrella:", carry_umbrella)
