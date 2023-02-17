import pandas as pd

imported_df = pd.read_csv("Question2.csv")
df = imported_df.copy()
df_battery_pack = pd.read_csv("battery_pack_car.csv")
df_chassis = pd.read_csv("chasis_car.csv")
df_battery_charger = pd.read_csv("battery_charger_car.csv")
df_motor = pd.read_csv("motor_inverter_car.csv")
df_autonomy = pd.read_csv("autonomous_car.csv")
#print(df.iloc[1])
print("A3"=="A5")
p_count = 8
for item in range(len(df)):
    #print(df.iloc[item]["A"])
    p = 1
    c = 1
    g = 1
    m = 1
    a = 3

    # The following variables are calcualted according to the following formulas:
    # Total Vehicle Cost [dollars] = Chassis Cost + Battery Cost + Charger Cost + Motor and inverter Cost + Autonomy system cost
    # Total Fleet Cost [dollars] = Vehicle Cost*Number of vehicles
    # Total Vehicle Weight [kg] = Chassis Weight + Battery Weight + Charger Weight + Motor and inverter Weight + Passengers Weight + Autonomy system Weight
    # Battery charge time [h] = Battery Capacity [kWh] / Charger Power [kW]
    # Power Consumption [Wh/km] = Nominal Power Consumption Chassis [Wh/km] + 0.1*(Total Weight [kg] - Chassis Weight [kg] ) + Added Power Consumption Autonomous System [Wh/km]
    # Range [km] = Battery Capacity [Wh] / Power Consumption [Wh/km]
    # Average Speed [km/h] = 700 * Motor Power [kW] / Total Weight [kg] 

    #initialize the variables. 
    df["Total Vehicle Cost [$1000]"][item] = 0
    df["Total Vehicle Weight [kg] minus passengers"][item] = 0
    df["Battery charge time [h]"][item] = 1
    df["Power Consumption [Wh/km]"][item] = 0
    df["Range [km]"][item] = 1
    df["Average Speed [km/h]"][item] = 700
    # Inside this while statement I go through and asses each of the components
    # and their corresponding additions to the entire system. 
    while(p <= p_count):
        # In this section of code we are going through each part.
        # We will add to each total value. 
        if (df.iloc[item]["P"].__eq__("P" + str(p))):
            # Add to the total cost of vehicle P cost.
            df["Total Vehicle Cost [$1000]"][item] = \
                df["Total Vehicle Cost [$1000]"][item] + \
                df_battery_pack["Cost [$1000]"][p-1]
            # Add to the total vehicle weight of P weights. 
            df["Total Vehicle Weight [kg] minus passengers"][item] = \
                df["Total Vehicle Weight [kg] minus passengers"][item] + \
                df_battery_pack["Weight [kg]"][p-1]
            #Setting the initial Battery charge. 
            df["Battery charge time [h]"][item] = df["Battery charge time [h]"][item] * df_battery_pack["Capacity [kWh]"][p-1]
            #Setting the initial Battery range. 
            df["Range [km]"][item] = df["Range [km]"][item] * df_battery_pack["Capacity [kWh]"][p-1]

        if(df.iloc[item]["C"].__eq__("C" + str(c))):
            # Add to the total cost of vehicle C cost.
            df["Total Vehicle Cost [$1000]"][item] = \
                df["Total Vehicle Cost [$1000]"][item] + \
                df_chassis["Chassis Cost [$1000]"][c-1]
            # Add to the total vehicle weight of C weights. 
            df["Total Vehicle Weight [kg] minus passengers"][item] = \
                df["Total Vehicle Weight [kg] minus passengers"][item] + \
                df_chassis["Weight chassis [kg]"][c-1]
            df["Power Consumption [Wh/km]"][item] = \
                df["Power Consumption [Wh/km]"][item] + \
                df_chassis["Nominal Power consumption [Wh/km]"][c-1] - \
                (0.1 * df_chassis["Weight chassis [kg]"][c-1])
        if(df.iloc[item]["G"].__eq__("G" + str(g))) and g <= 3:
            # Add to the total cost of vehicle G cost.
            df["Total Vehicle Cost [$1000]"][item] = \
                df["Total Vehicle Cost [$1000]"][item] + \
                df_battery_charger["Cost on vehicle [$1000]"][g-1]
            # Add to the total vehicle weight of G weights. 
            df["Total Vehicle Weight [kg] minus passengers"][item] = \
                df["Total Vehicle Weight [kg] minus passengers"][item] + \
                df_battery_charger["Weight on vehicle [kg]"][g-1]
            # Dividing the calculated charge time by the charge power. 
            df["Battery charge time [h]"][item] = round(df["Battery charge time [h]"][item] * \
                (1/df_battery_charger["Power [kW]"][g-1]), 2)
        if(df.iloc[item]["M"].__eq__("M" + str(m))) and m <= 4:
            # Add to the total cost of vehicle M cost.
            df["Total Vehicle Cost [$1000]"][item] = \
                df["Total Vehicle Cost [$1000]"][item] + \
                (df_motor["Cost [$]"][m-1]/1000)    
            # Add to the total vehicle weight of M weights. 
            df["Total Vehicle Weight [kg] minus passengers"][item] = \
                df["Total Vehicle Weight [kg] minus passengers"][item] + \
                df_motor["Weight [kg]"][m-1]    
            df["Average Speed [km/h]"][item] = df["Average Speed [km/h]"][item] * \
                df_motor["Power [kW]"][m-1]    
        if(df.iloc[item]["A"].__eq__("A" + str(a))) and a <= 5:
            # Add to the total cost of vehicle A cost.
            df["Total Vehicle Cost [$1000]"][item] = \
                df["Total Vehicle Cost [$1000]"][item] + \
                df_autonomy["Cost [$1000]"][p-1]
            # Add to the total vehicle weight of A weights. 
            df["Total Vehicle Weight [kg] minus passengers"][item] = \
                df["Total Vehicle Weight [kg] minus passengers"][item] + \
                df_autonomy["Weight [kg]"][p-1]
            # Update power consumption with A consumption.
            df["Power Consumption [Wh/km]"][item] = \
                df["Power Consumption [Wh/km]"][item] + \
                df_autonomy["Added Power Consumption [Wh/km]"][p-1]
        p+=1
        c+=1
        a+=1
        g+=1
        m+=1
        
    # The following will subtract the total weight of the vehicle for power consumption.
    df["Power Consumption [Wh/km]"][item] = \
        round(df["Power Consumption [Wh/km]"][item] + \
        (0.1 * df["Total Vehicle Weight [kg] minus passengers"][item]), 2)
    #Setting the initial Battery range. 
    df["Range [km]"][item] = round(df["Range [km]"][item] / df["Power Consumption [Wh/km]"][item], 2)

    df["Average Speed [km/h]"][item] = round(df["Average Speed [km/h]"][item] * \
        (1/df["Total Vehicle Weight [kg] minus passengers"][item]), 2)

    #print(df.iloc[item]["A"])
#print(df)
df.to_csv("outputTesting.csv")