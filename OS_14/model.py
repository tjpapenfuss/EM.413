import pandas as pd

#Import the csv files into pandas dataframes.
df = pd.read_csv("architectures.csv")
option_setup = pd.read_csv("options_setup_time.csv", index_col=0)
option_accuracy = pd.read_csv("options_accuracy.csv", index_col=0)
#df_TradeSpace = df[['Cost', 'Utility']].copy()

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
    metric_setup = "setup_time"
    metric_accuracy = "Accuracy"

    ##############################################################################################################################
    # The following block of code is setting the utility values.
    # These utilities are calculated according to the following formulas:
    # U_Accuracy =  ((D1+D2)/2)*D3*D4*D8
    # U_Setup_Time = (D1+D2) + D3 + D4 + (D6+D7) + (D8+D9) + D10
    # Where D is the decision identifier. Ie. D1 is Measurement collection architecture decision. 
    ##############################################################################################################################
    # A block of code
    # Set the Utility value for the Accuracy.
    df.at[item,metric_accuracy] = round(((option_accuracy.loc[a_val][metric_accuracy] + \
                            option_accuracy.loc[b_val][metric_accuracy])/2) * \
                            option_accuracy.loc[c_val][metric_accuracy] * \
                            option_accuracy.loc[d_val][metric_accuracy] * \
                            option_accuracy.loc[h_val][metric_accuracy], 2)
    
    # Set the Utility value for the Setup time.
    df.at[item,metric_setup] = (option_setup.loc[a_val][metric_setup] + \
                            option_setup.loc[b_val][metric_setup] + \
                            option_setup.loc[c_val][metric_setup] + \
                            option_setup.loc[d_val][metric_setup] + \
                            option_setup.loc[f_val][metric_setup] + \
                            option_setup.loc[g_val][metric_setup] + \
                            option_setup.loc[h_val][metric_setup] + \
                            option_setup.loc[j_val][metric_setup] + \
                            option_setup.loc[k_val][metric_setup])
    
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