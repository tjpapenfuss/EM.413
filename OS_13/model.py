import pandas as pd

imported_df = pd.read_csv("architectures.csv")
df = imported_df.copy()
option_df = pd.read_csv("options.csv", index_col=0)
#print(df.iloc[1])
#print("A3"=="A5")
#p_count = 8
#integers = int(df["A"][1][1:2])

for item in range(len(df)):
    # The following code gets the numerical values for the 5 components of the system.
    a = int(df["A"][item][1:2])
    b = int(df["B"][item][1:2])
    c = int(df["C"][item][1:2])
    d = int(df["D"][item][1:2])
    e = int(df["E"][item][1:2])
    f = int(df["F"][item][1:2])
    g = int(df["G"][item][1:2])
    h = int(df["H"][item][1:2])
    j = int(df["J"][item][1:2])
    k = int(df["K"][item][1:2])
    print(a,b,c,d,e,f,g,h,j,k)
    a_val = df["A"][item]
    print(a_val)
    # The following variables are calcualted according to the following formulas:
    # Total Vehicle Cost [dollars] = Chassis Cost + Battery Cost + Charger Cost + Motor and inverter Cost + Autonomy system cost
    # Total Fleet Cost [dollars] = Vehicle Cost*Number of vehicles
    # Total Vehicle Weight [kg] = Chassis Weight + Battery Weight + Charger Weight + Motor and inverter Weight + Passengers Weight + Autonomy system Weight
    # Battery charge time [h] = Battery Capacity [kWh] / Charger Power [kW]
    # Power Consumption [Wh/km] = Nominal Power Consumption Chassis [Wh/km] + 0.1*(Total Weight [kg] - Chassis Weight [kg] ) + Added Power Consumption Autonomous System [Wh/km]
    # Range [km] = Battery Capacity [Wh] / Power Consumption [Wh/km]
    # Average Speed [km/h] = 700 * Motor Power [kW] / Total Weight [kg] 

    #initialize the variables. 
    df.loc[:, ("Frequency", item)] = 0
    df.loc[:, ("Accuracy",item)] = 0
    df.loc[:, ("Innovation",item)] = 0
    df.loc[:, ("Setup time",item)] = 0
    df.loc[:, ("Safety",item)] = 0
    df.loc[:, ("Judgement",item)] = 0
    df.loc[:, ("Cost",item)] = 0

    # A block of code
    #  Add to the total cost of vehicle P cost.
    df.loc[:, ("Frequency",item)] = \
        df.loc[:, ("Frequency",item)] + \
        option_df.loc[a_val]["Frequency"]
    print(df)
    print(option_df.loc[a_val]["Frequency"])
    # # Add to the total vehicle weight of P weights. 
    # df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)] = \
    #     df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)] + \
    #     df_battery_pack["Weight [kg]",p-1]
    # #Setting the initial Battery charge. 
    # df.loc[:, ("Battery charge time [h]",item)] = df.loc[:, ("Battery charge time [h]",item)] * df_battery_pack["Capacity [kWh]",p-1]
    # #Setting the initial Battery range. 
    # df.loc[:, ("Range [km]",item)] = df.loc[:, ("Range [km]",item)] * df_battery_pack["Capacity [kWh]",p-1]

    # # C block of code
    # # Add to the total cost of vehicle C cost.
    # df.loc[:, ("Total Vehicle Cost [$1000]",item)] = \
    #     df.loc[:, ("Total Vehicle Cost [$1000]",item)] + \
    #     df_chassis["Chassis Cost [$1000]",c-1]
    # # Add to the total vehicle weight of C weights. 
    # df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)] = \
    #     df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)] + \
    #     df_chassis["Weight chassis [kg]",c-1]
    # df.loc[:, ("Power Consumption [Wh/km]",item)] = \
    #     df.loc[:, ("Power Consumption [Wh/km]",item)] + \
    #     df_chassis["Nominal Power consumption [Wh/km]",c-1] - \
    #     (0.1 * df_chassis["Weight chassis [kg]",c-1])

    # # G block
    # # Add to the total cost of vehicle G cost.
    # df.loc[:, ("Total Vehicle Cost [$1000]",item)] = \
    #     df.loc[:, ("Total Vehicle Cost [$1000]",item)] + \
    #     df_battery_charger["Cost on vehicle [$1000]",g-1]
    # # Add to the total vehicle weight of G weights. 
    # df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)] = \
    #     df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)] + \
    #     df_battery_charger["Weight on vehicle [kg]",g-1]
    # # Dividing the calculated charge time by the charge power. 
    # df.loc[:, ("Battery charge time [h]",item)] = round(df.loc[:, ("Battery charge time [h]",item)] * \
    #     (1/df_battery_charger["Power [kW]",g-1]), 2)    

    # # M block
    # # Add to the total cost of vehicle M cost.
    # df.loc[:, ("Total Vehicle Cost [$1000]",item)] = \
    #     df.loc[:, ("Total Vehicle Cost [$1000]",item)] + \
    #     (df_motor["Cost [$]",m-1]/1000)    
    # # Add to the total vehicle weight of M weights. 
    # df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)] = \
    #     df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)] + \
    #     df_motor["Weight [kg]",m-1]    
    # df.loc[:, ("Average Speed [km/h]",item)] = df.loc[:, ("Average Speed [km/h]",item)] * \
    #     df_motor["Power [kW]",m-1]    

    # # A block
    # # Add to the total cost of vehicle A cost.
    # df.loc[:, ("Total Vehicle Cost [$1000]",item)] = \
    #     df.loc[:, ("Total Vehicle Cost [$1000]",item)] + \
    #     df_autonomy["Cost [$1000]",a-3]
    # # Add to the total vehicle weight of A weights. 
    # df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)] = \
    #     df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)] + \
    #     df_autonomy["Weight [kg]",a-3]
    # # Update power consumption with A consumption.
    # df.loc[:, ("Power Consumption [Wh/km]",item)] = \
    #     df.loc[:, ("Power Consumption [Wh/km]",item)] + \
    #     df_autonomy["Added Power Consumption [Wh/km]",a-3]

    # df.loc[:, ("Power Consumption [Wh/km]",item)] = \
    #     round(df.loc[:, ("Power Consumption [Wh/km]",item)] + \
    #     (0.1 * df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)]), 2)
    # #Setting the initial Battery range. 
    # df.loc[:, ("Range [km]",item)] = round(df.loc[:, ("Range [km]",item)] / df.loc[:, ("Power Consumption [Wh/km]",item)], 2)

    # df.loc[:, ("Average Speed [km/h]",item)] = round(df.loc[:, ("Average Speed [km/h]",item)] * \
    #     (1/df.loc[:, ("Total Vehicle Weight [kg] minus passengers",item)]), 2)

df.to_csv("outputTesting.csv")