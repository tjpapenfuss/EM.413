import pandas as pd
from sklearn import preprocessing

imported_df = pd.read_csv("Question2_bike.csv")
df = imported_df.copy()
df_battery_pack = pd.read_csv("bike_battery_pack.csv")
df_battery_charger = pd.read_csv("bike_battery_charger.csv")
df_motor = pd.read_csv("bike_motor.csv")
df_frame = pd.read_csv("bike_frame.csv")

for item in range(len(df)):
    # The following code gets the numerical values for the 5 components of the system.
    battery_pack        = int(df["E"][item][1:2]) # Battery Pack
    frame               = int(df["B"][item][1:2]) # Frame
    battery_charger     = int(df["G"][item][1:2]) # Battery charger
    motor               = int(df["K"][item][1:2]) # Motor and inverter module

    # The following variables are calcualted according to the following formulas:

    # Total Bike Cost [dollars] = Chassis Cost + Battery Cost + Charger Cost + Motor and inverter Cost
    df["Total Bike Cost [$1000]"][item] = df_battery_pack["Cost [$1000]"][battery_pack-1] + \
        df_frame["Frame Cost [$1000]"][frame-1] + \
        df_battery_charger["Cost on vehicle [$1000]"][battery_charger-1] + \
        (df_motor["Cost [$]"][motor-1]/1000)

    # Total Vehicle Weight [kg] = Chassis Weight + Battery Weight + Charger Weight + Motor and inverter Weight + Passengers Weight
    # Assumption is that there is just one rider.
    df["Total Bike Weight [kg]"][item] = 100 + df_battery_pack["Weight [kg]"][battery_pack-1] + \
        df_frame["Weight [kg]"][frame-1] + df_battery_charger["Weight on vehicle [kg]"][battery_charger-1] + \
        df_motor["Weight [kg]"][motor-1]
    
    # Battery charge time [h] = Battery Capacity [kWh] / Charger Power [kW]
    df["Battery charge time [h]"][item] = df_battery_pack["Capacity [kWh]"][battery_pack-1] / \
        df_battery_charger["Power [kW]"][battery_charger-1]
    
    # # Power Consumption [Wh/km] = Nominal Power Consumption Chassis [Wh/km] + 0.1*(Total Weight [kg] - Chassis Weight [kg] )
    df["Power Consumption [Wh/km]"][item] = round( df_frame["Nominal Power consumption [Wh/km]"][frame-1] + \
        (0.1 * (df["Total Bike Weight [kg]"][item] - df_frame["Weight [kg]"][frame-1])), 2)
    
    # # Range [km] = Battery Capacity [Wh] / Power Consumption [Wh/km]
    df["Range [km]"][item] = round(df_battery_pack["Capacity [kWh]"][battery_pack-1]*1000 / \
        df["Power Consumption [Wh/km]"][item], 2)

    # # Average Speed [km/h] = 700 * Motor Power [kW] / Total Weight [kg] 
    avg_speed = round(700 * df_motor["Power [kW]"][motor-1] / \
        df["Total Bike Weight [kg]"][item], 2)
    if(avg_speed > 30):
        df["Average Speed [km/h]"][item] = 30
    else:
        df["Average Speed [km/h]"][item] = avg_speed

    # Up-time [h] = Range [km] / Average Speed [km/h]
    df["Up-time [h]"][item] = round(df["Range [km]"][item] / df["Average Speed [km/h]"][item], 2)

    # Down-time [h] = Battery charge time [h] + 0.25
    df["Down-time [h]"][item] = round(df["Battery charge time [h]"][item] + 0.25, 2)

    # Availability [dml] = Up-time / (Up-time + Down-time) 
    df["Availability [dml]"][item] = round(df["Up-time [h]"][item] / (df["Up-time [h]"][item] + df["Down-time [h]"][item]), 2)


# bike_cost_normilization         = 0
# bike_weight_normilization       = (1/5)
# bike_charge_time_normilization  = (1/5)
# bike_power_normilization        = (1/5)
# bike_range_normilization        = (1/5)
# bike_speed_normilization        = (1/5)

# df_max_scaled = df.copy()
# df_max_scaled["Normalized utility"] = round( \
#     ((df_max_scaled["Total Bike Cost [$1000]"].abs().min()    /   df_max_scaled["Total Bike Cost [$1000]"]) * bike_cost_normilization + \
#     (df_max_scaled["Total Bike Weight [kg]"].abs().min()     /   df_max_scaled["Total Bike Weight [kg]"]) * bike_weight_normilization + \
#     (df_max_scaled["Battery charge time [h]"].abs().min()    /   df_max_scaled["Battery charge time [h]"]) * bike_charge_time_normilization + \
#     (df_max_scaled["Power Consumption [Wh/km]"].abs().min()  /   df_max_scaled["Power Consumption [Wh/km]"]) * bike_power_normilization + \
#     (df_max_scaled["Range [km]"]                             /   df_max_scaled["Range [km]"].abs().max()) * bike_range_normilization + \
#     (df_max_scaled["Average Speed [km/h]"]                   /   df_max_scaled["Average Speed [km/h]"].abs().max()) * bike_speed_normilization), 3)

#normalized_arr = preprocessing.normalize(df["Total Bike Cost [$1000]"])
# print(df_max_scaled["Normalized utility"])
df.to_csv("Q2_bike_output.csv")