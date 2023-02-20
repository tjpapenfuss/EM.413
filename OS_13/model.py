import pandas as pd

#Import the csv files into pandas dataframes.
df = pd.read_csv("architectures.csv")
option_df = pd.read_csv("options.csv", index_col=0)
df_TradeSpace = df[['Cost', 'Utility']].copy()

# Set the global Variables. These metrics need to be updated in both architectures.csv and options.csv!
metric1 = "Frequency"
metric2 = "Data Accuracy"
metric3 = "Technical Maturity"
metric4 = "Setup time"
metric5 = "Safety"
metric6 = "Human Judgement"

for item in range(len(df)):
    # The following code gets the ID (Ie. A2.) for the 10 decisions of the system.
    # A1/2 are the options for the first architectural decision D1. 
    #print(a,b,c,d,e,f,g,h,j,k)
    a_val = df["A"][item]
    b_val = df["B"][item]
    c_val = df["C"][item]
    d_val = df["D"][item]
    e_val = df["E"][item]
    f_val = df["F"][item]
    g_val = df["G"][item]
    h_val = df["H"][item]
    j_val = df["J"][item]
    k_val = df["K"][item]

    ##############################################################################################################################
    # The following block of code is setting the utility values.
    # These utilities are calculated according to the following formulas:
    # U_f=  (2D1+D3+D5 )/4
    # U_A=  (D1+D2+D6+D8 )/4
    # U_M=  (D1+D2+D4+2D7+D9)/6
    # U_T=  (D1+D2+D4+3D6+2D7+2D10)/10
    # U_S=  (D1+D3+5D10 )/7
    # U_H=  (D1+D10 )/2
    # Where D is the decision identifier. Ie. D1 is Measurement collection architecture decision. 
    ##############################################################################################################################
    # A block of code
    # Set the Utility value for the Frequency.
    #df["Frequency"][item] = ((2*option_df.loc[a_val]["Frequency"]) + \
    #                        option_df.loc[c_val]["Frequency"] + \
    #                        option_df.loc[d_val]["Frequency"]) / 4
    df.at[item, metric1] = round(((2*option_df.loc[a_val][metric1]) + \
                            option_df.loc[c_val][metric1] + \
                            option_df.loc[e_val][metric1]) / 4, 2)

    # Set the Utility value for the Accuracy.
    df.at[item,metric2] = round((option_df.loc[a_val][metric2] + \
                            option_df.loc[b_val][metric2] + \
                            option_df.loc[f_val][metric2] + \
                            option_df.loc[h_val][metric2]) / 4, 2)

    # Set the Utility value for the Technical Maturity.
    df.at[item,metric3] = round((option_df.loc[a_val][metric3] + \
                            option_df.loc[b_val][metric3] + \
                            option_df.loc[d_val][metric3] + \
                            option_df.loc[j_val][metric3] + \
                            (2*option_df.loc[g_val][metric3])) / 6, 2)
    
    # Set the Utility value for the Setup time.
    df.at[item,metric4] = round((option_df.loc[a_val][metric4] + \
                            option_df.loc[b_val][metric4] + \
                            option_df.loc[d_val][metric4] + \
                            (3*option_df.loc[f_val][metric4]) + \
                            (2*option_df.loc[g_val][metric4]) + \
                            (2*option_df.loc[k_val][metric4])) / 10, 2)

    # Set the Utility value for the Safety.
    df.at[item,metric5] = round((option_df.loc[a_val][metric5] + \
                            option_df.loc[c_val][metric5] + \
                            (5*option_df.loc[k_val][metric5])) / 7, 2)

    # Set the Utility value for the Human judgement.
    df.at[item,metric6] = round((option_df.loc[a_val][metric6] + \
                            option_df.loc[k_val][metric6]) / 2, 2)

    # Generate value for the total Utility.
    # This is calculated using the following equation:
    # 0.15*U_f + 0.2*U_A + 0.15*U_M + 0.2*U_T + 0.15*U_S + 0.15*U_H
    df.at[item,"Utility"] = round((0.15*df.loc[item,metric1]) + \
                            (0.2*df.loc[item,metric2]) + \
                            (0.15*df.loc[item,metric3]) + \
                            (0.2*df.loc[item,metric4]) + \
                            (0.15*df.loc[item,metric5]) + \
                            (0.15*df.loc[item,metric6]), 2)
    
    # Set value for the Cost. 
    df.at[item,"Cost_norm"] = round((option_df.loc[a_val]["Cost_norm"] + \
                            option_df.loc[b_val]["Cost_norm"] + \
                            option_df.loc[c_val]["Cost_norm"] + \
                            option_df.loc[d_val]["Cost_norm"] + \
                            option_df.loc[e_val]["Cost_norm"] + \
                            option_df.loc[f_val]["Cost_norm"] + \
                            option_df.loc[g_val]["Cost_norm"] + \
                            option_df.loc[h_val]["Cost_norm"] + \
                            option_df.loc[j_val]["Cost_norm"] + \
                            option_df.loc[k_val]["Cost_norm"]) / 10, 2)

    df.at[item,"Cost"] =   round((option_df.loc[a_val]["Cost"] + \
                            option_df.loc[b_val]["Cost"] + \
                            option_df.loc[c_val]["Cost"] + \
                            option_df.loc[d_val]["Cost"] + \
                            option_df.loc[e_val]["Cost"] + \
                            option_df.loc[f_val]["Cost"] + \
                            option_df.loc[g_val]["Cost"] + \
                            option_df.loc[h_val]["Cost"] + \
                            option_df.loc[j_val]["Cost"] + \
                            option_df.loc[k_val]["Cost"]), 0)


    df_TradeSpace.at[item,"Cost"] = df.loc[item,"Cost"]
    df_TradeSpace.at[item,"Utility"] = df.loc[item,"Utility"]

df.to_csv("outputTesting.csv")

df_TradeSpace.to_csv("pythonTrade.csv")