# Each crop has 16 acres
area = 16

# Tomato: 30% @ 10t, 70% @ 12t, Rs. 7/kg
tomato_30 = 0.3 * area * 10 * 1000 * 7
tomato_70 = 0.7 * area * 12 * 1000 * 7
tomato = tomato_30 + tomato_70

# Potato: 10t/acre, Rs. 20/kg
potato = area * 10 * 1000 * 20

# Cabbage: 14t/acre, Rs. 24/kg
cabbage = area * 14 * 1000 * 24

# Sunflower: 0.7t/acre, Rs. 200/kg
sunflower = area * 0.7 * 1000 * 200

# Sugarcane: 45t/acre, Rs. 4000/t
sugarcane = area * 45 * 4000

# Total sales
total_sales = tomato + potato + cabbage + sunflower + sugarcane

# Chemical-free sales after 11 months: Tomato + Sunflower + Sugarcane
cf_sales = tomato + sunflower + sugarcane

# Output
print("\n--- Farmer Sales Report ---")
print("Total sales from all crops: ₹", total_sales)
print("Sales from chemical-free farming (after 11 months): ₹", cf_sales)
