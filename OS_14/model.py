import pandas as pd

#Import the csv files into pandas dataframes.
df = pd.read_csv("architectures.csv")
option_setup = pd.read_csv("options_safety.csv", index_col=0)
option_reliability = pd.read_csv("options_reliability.csv", index_col=0)
#df_TradeSpace = df[['Cost', 'Utility']].copy()

for item in range(len(df)):
    # The following code gets the ID (Ie. A2.) for the 10 decisions of the system.
    # A1/2 are the options for the first architectural decision D1. 
    #print(a,b,c,d,e,f,g,h,j,k)
    a_val = df["A"][item] #1
    b_val = df["B"][item] #2
    c_val = df["C"][item] #3
    d_val = df["D"][item] #4
    e_val = df["E"][item] #5
    f_val = df["F"][item] #6
    g_val = df["G"][item] #7
    h_val = df["H"][item] #8
    j_val = df["J"][item] #9
    k_val = df["K"][item] #10
    metric_safety = "Safety"
    metric_reliability = "Reliability"

    ##############################################################################################################################
    # The following block of code is setting the utility values.
    # These utilities are calculated according to the following formulas:
    # U_Reliability =  ((D1+D2)/2)*D3*D4*D5*D7*D8*D9
    # U_Safety = (D1+D2) + D3 + D4 + (D6+D7) + (D8+D9) + D10
    # Where D is the decision identifier. Ie. D1 is Measurement collection architecture decision. 
    ##############################################################################################################################
    # A block of code
    # Set the Utility value for the Reliability.
    # df.at[item,metric_accuracy] = round(((option_accuracy.loc[a_val][metric_accuracy] + \
    #                         option_accuracy.loc[b_val][metric_accuracy])/2) * \
    #                         option_accuracy.loc[c_val][metric_accuracy] * \
    #                         option_accuracy.loc[d_val][metric_accuracy] * \
    #                         option_accuracy.loc[h_val][metric_accuracy], 2)
    df.at[item,metric_reliability] = round((5 * ((option_reliability.loc[a_val][metric_reliability] + \
                            option_reliability.loc[b_val][metric_reliability] + \
                            option_reliability.loc[c_val][metric_reliability] + \
                            option_reliability.loc[d_val][metric_reliability] + \
                            option_reliability.loc[e_val][metric_reliability] + \
                            option_reliability.loc[g_val][metric_reliability] + \
                            option_reliability.loc[h_val][metric_reliability] + \
                            option_reliability.loc[j_val][metric_reliability])/8)) - 4, 2)
    # Set the Utility value for the Safety.
    df.at[item,metric_safety] = round(1 + ((option_setup.loc[a_val][metric_safety] + \
                            option_setup.loc[b_val][metric_safety] + \
                            option_setup.loc[c_val][metric_safety] + \
                            option_setup.loc[f_val][metric_safety] + \
                            option_setup.loc[k_val][metric_safety]) * -0.0016), 2)

    # Set value for the Cost. 
    df.at[item,"Cost"] = (option_setup.loc[a_val]["Cost"] + \
                            option_setup.loc[b_val]["Cost"] + \
                            option_setup.loc[c_val]["Cost"] + \
                            option_setup.loc[d_val]["Cost"] + \
                            option_setup.loc[e_val]["Cost"] + \
                            option_setup.loc[f_val]["Cost"] + \
                            option_setup.loc[g_val]["Cost"] + \
                            option_setup.loc[h_val]["Cost"] + \
                            option_setup.loc[j_val]["Cost"] + \
                            option_setup.loc[k_val]["Cost"])


    #df_TradeSpace.at[item,"Cost"] = df.loc[item,"Cost"]
    #df_TradeSpace.at[item,"Utility"] = df.loc[item,"Utility"]

df.to_csv("outputTesting.csv")

#df_TradeSpace.to_csv("pythonTrade.csv")