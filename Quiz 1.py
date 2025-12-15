# question 1: Makola market inventory and sales system
inventory = {
    "Tomatoes" : {"stock": 150, 'price_per_unit': 5.0},
    "Onions" : {"stock": 80, 'price_per_unit': 3.5},
    "Garden Eggs" : {"stock": 200, 'price_per_unit': 1.0} 
}
while True: 
    item = input("Enter item name to purchase(Tomatoes, Onions, Garden Eggs) or 'exit': ")
    if item == "exit":
        print("Closing sales. Total transactions completed")
        break
    if item not in inventory:
        print(f"Item '{item}' not found in stock. Check spelling.")
    else:
        quantity = int(input("Enter quantity to buy: "))
        if quantity > inventory[item]["stock"]:
            print(f"Sorry, only {inventory[item]["stock"]} units of {item} remaining.")
        else: 
            cost = quantity * inventory[item]["price_per_unit"]
            inventory[item]["stock"] = inventory[item]["stock"] - quantity
            print(f"Sale successful! Cost: GHS {round(cost, 2)}. {inventory[item]["stock"]} remaining.")


# question 2: Ghana water company bill calculator
consumption = float(input("Total water consumption for the month(in cubic meters): "))
service_charge = 15.00
consumption_cost = 0
total_bill = service_charge
if consumption <= 15: 
    consumption_cost * 0.90
elif consumption <= 30: 
    consumption_cost = (15 * 0.90 ) + ((consumption -15) * 1.20 )
else:
    consumption_cost = (15 * 0.90) + (15 * 1.20) + ((consumption -30) * 1.80)
total_bill = service_charge + consumption_cost

print(f"Consumption: {consumption} m3")
print("Service charge: GHS 15.00")
print(f"Consumption cost: GHS{round(consumption_cost, 2)}")
print(f"Total bill: GHS {round(total_bill, 2)}")
    
    
#question 3: Traffic spped analyzer for road safety
recorded_speeds = [95, 110, 100, 85, 125, 90, 105, 115, 70, 130, 99, 101, 88]
speed_limit = 100

speeding_violations = []
total_speed = 0

for speed in recorded_speeds:
    total_speed += speed
    if speed > speed_limit:
        print(
            f"WARNING: Vehicle recorded at {speed} km/h. "
            f"Exceeded limit of {speed_limit} km/h."
        )
        speeding_violations.append(speed)

total_vehicles = len(recorded_speeds)
total_violations = len(speeding_violations)
percentage_speeding = (total_violations / total_vehicles) * 100
average_speed = total_speed / total_vehicles

print(f"Total vehicles recorded: {total_vehicles}")
print(f"Total speeding violations: {total_violations}")
print(f"Percentage speeding: {round(percentage_speeding, 2)}%")
print(f"Average speed: {round(average_speed, 2)} km/h")

focused_segment = recorded_speeds[2:8]
print(
    f"Speeds for focused inspection segment (3rd to 8th vehicle): {focused_segment}"
)
