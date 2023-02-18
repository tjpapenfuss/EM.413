import pandas as pd

#imported_df = pd.read_csv("architectures.csv")
df = pd.read_csv("architectures.csv")
#df = imported_df.copy()
option_df = pd.read_csv("options.csv", index_col=0)
#print(df.iloc[1])
#print("A3"=="A5")
#p_count = 8
#integers = int(df["A"][1][1:2])

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
    # U_I=  (D1+D2+D4+2D7+D9)/6
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
    df.at[item, "Frequency"] = round(((2*option_df.loc[a_val]["Frequency"]) + \
                            option_df.loc[c_val]["Frequency"] + \
                            option_df.loc[e_val]["Frequency"]) / 4, 2)

    # Set the Utility value for the Accuracy.
    df.at[item,"Accuracy"] = round((option_df.loc[a_val]["Accuracy"] + \
                            option_df.loc[b_val]["Accuracy"] + \
                            option_df.loc[f_val]["Accuracy"] + \
                            option_df.loc[h_val]["Accuracy"]) / 4, 2)
    #print(option_df.loc[a_val]["Accuracy"], option_df.loc[b_val]["Accuracy"], option_df.loc[f_val]["Accuracy"], option_df.loc[h_val]["Accuracy"])

    # Set the Utility value for the Innovation.
    df.at[item,"Innovation"] = round((option_df.loc[a_val]["Innovation"] + \
                            option_df.loc[b_val]["Innovation"] + \
                            option_df.loc[d_val]["Innovation"] + \
                            option_df.loc[j_val]["Innovation"] + \
                            (2*option_df.loc[g_val]["Innovation"])) / 6, 2)
    
    # Set the Utility value for the Setup time.
    df.at[item,"Setup time"] = round((option_df.loc[a_val]["Setup time"] + \
                            option_df.loc[b_val]["Setup time"] + \
                            option_df.loc[d_val]["Setup time"] + \
                            (3*option_df.loc[f_val]["Setup time"]) + \
                            (2*option_df.loc[g_val]["Setup time"]) + \
                            (2*option_df.loc[k_val]["Setup time"])) / 10, 2)

    # Set the Utility value for the Safety.
    df.at[item,"Safety"] = round((option_df.loc[a_val]["Safety"] + \
                            option_df.loc[c_val]["Safety"] + \
                            (5*option_df.loc[k_val]["Safety"])) / 7, 2)

    # Set the Utility value for the Judgement.
    df.at[item,"Judgement"] = round((option_df.loc[a_val]["Judgement"] + \
                            option_df.loc[k_val]["Judgement"]) / 2, 2)


    # Set value for the Cost. 
    df.at[item,"Cost"] = round((option_df.loc[a_val]["Cost"] + \
                            option_df.loc[b_val]["Cost"] + \
                            option_df.loc[c_val]["Cost"] + \
                            option_df.loc[d_val]["Cost"] + \
                            option_df.loc[e_val]["Cost"] + \
                            option_df.loc[f_val]["Cost"] + \
                            option_df.loc[g_val]["Cost"] + \
                            option_df.loc[h_val]["Cost"] + \
                            option_df.loc[j_val]["Cost"] + \
                            option_df.loc[k_val]["Cost"]) / 10, 2)
    

df.to_csv("outputTesting.csv")