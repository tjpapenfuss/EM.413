import pandas as pd

MAX_SPEED = 20

imported_df = pd.read_csv("Question2.csv")
df = imported_df.copy()
df_battery_pack = pd.read_csv("battery_pack_car.csv")
df_chassis = pd.read_csv("chasis_car.csv")
df_battery_charger = pd.read_csv("battery_charger_car.csv")
df_motor = pd.read_csv("motor_inverter_car.csv")
df_autonomy = pd.read_csv("autonomous_car.csv")

# We will probably need to update this number. Not sure what number to put here
number_of_passengers = 2

# For loop to iterate through all combinations that are possible.
for item in range(len(df)):
    # The following code gets the numerical values for the 5 components of the system.
    # I.e. if we have 'A3' it will drop the A and just get the value 3. 
    battery_pack        = int(df["P"][item][1:2]) # Battery Pack
    chassis             = int(df["C"][item][1:2]) # Chassis
    battery_charger     = int(df["G"][item][1:2]) # Battery charger
    motor               = int(df["M"][item][1:2]) # Motor and inverter module
    autonomous_sys      = int(df["A"][item][1:2]) # Autonomous System

    match chassis:
        case 1:
            number_of_passengers = 2
        case 2:
            number_of_passengers = 4
        case 3:
            number_of_passengers = 6
        case 4:
            number_of_passengers = 8
        case 5:
            number_of_passengers = 10
        case 6:
            number_of_passengers = 16
        case 7:
            number_of_passengers = 20
        case 8:
            number_of_passengers = 30

    # Total Vehicle Cost [dollars] = Chassis Cost + Battery Cost + Charger Cost + Motor and inverter Cost + Autonomy system cost
    df["Total Vehicle Cost [$1000]"][item] = df_battery_pack["Cost [$1000]"][battery_pack-1] + \
        df_chassis["Chassis Cost [$1000]"][chassis-1] + df_battery_charger["Cost on vehicle [$1000]"][battery_charger-1] + \
        df_autonomy["Cost [$1000]"][autonomous_sys-3] + (df_motor["Cost [$]"][motor-1]/1000)   
    
    # Total Vehicle Weight [kg] = Chassis Weight + Battery Weight + Charger Weight + Motor and inverter Weight + Passengers Weight + Autonomy system Weight
    df["Total Vehicle Weight [kg]"][item] = round(df_battery_pack["Weight [kg]"][battery_pack-1] + \
        df_chassis["Weight chassis [kg]"][chassis-1] + df_battery_charger["Weight on vehicle [kg]"][battery_charger-1] + \
        df_autonomy["Weight [kg]"][autonomous_sys-3] + df_motor["Weight [kg]"][motor-1] + \
        number_of_passengers * 100, 2)
    
    # Battery charge time [h] = Battery Capacity [kWh] / Charger Power [kW]
    df["Battery charge time [h]"][item] = \
        round(df_battery_pack["Capacity [kWh]"][battery_pack-1] / df_battery_charger["Power [kW]"][battery_charger-1], 2)   
    
    # Power Consumption [Wh/km] = Nominal Power Consumption Chassis [Wh/km] + 0.1*(Total Weight [kg] - Chassis Weight [kg] ) + Added Power Consumption Autonomous System [Wh/km]
    df["Power Consumption [Wh/km]"][item] = round(df_chassis["Nominal Power consumption [Wh/km]"][chassis-1] + \
        (0.1 * (df["Total Vehicle Weight [kg]"][item] - df_chassis["Weight chassis [kg]"][chassis-1])) + \
        df_autonomy["Added Power Consumption [Wh/km]"][autonomous_sys-3], 2)

    # Range [km] = Battery Capacity [Wh] / Power Consumption [Wh/km]
    df["Range [km]"][item] = round(df_battery_pack["Capacity [kWh]"][battery_pack-1] * 1000 / \
        df["Power Consumption [Wh/km]"][item], 2)

    # Average Speed [km/h] = 700 * Motor Power [kW] / Total Weight [kg] 
    avg_speed = round(700 * df_motor["Power [kW]"][motor-1] / \
        df["Total Vehicle Weight [kg]"][item], 2)
    if(avg_speed > MAX_SPEED):
        df["Average Speed [km/h]"][item] = MAX_SPEED
    else:
        df["Average Speed [km/h]"][item] = avg_speed

    # Up-time [h] = Range [km] / Average Speed [km/h]
    df["Up-time [h]"][item] = round(df["Range [km]"][item] / df["Average Speed [km/h]"][item], 2)

    # Down-time [h] = Battery charge time [h] + 0.25
    df["Down-time [h]"][item] = round(df["Battery charge time [h]"][item] + 0.25, 2)

    # Availability [dml] = Up-time / (Up-time + Down-time) 
    df["Availability [dml]"][item] = round(df["Up-time [h]"][item] / (df["Up-time [h]"][item] + df["Down-time [h]"][item]), 2)

df.to_csv("Q2_output.csv")