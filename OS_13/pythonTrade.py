import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   

imported_df = pd.read_csv("pythonTrade.csv")

imported_df.plot(x="Cost", y="Utility", kind="scatter")

def pareto_frontier(Xs, Ys, maxX = True, maxY = True):
    # Sort the list in either ascending or descending order of X
    myList = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxX)
    #print(myList[0])
    #print(myList[1])
    # Start the Pareto frontier with the first value in the sorted list
    p_front = [myList[0]]    
    # Loop through the sorted list
    for pair in myList[1:]:
        if maxY: 
            if pair[1] >= p_front[-1][1]: # Look for higher values of Y…
                p_front.append(pair) # … and add them to the Pareto frontier
        else:
            if pair[1] <= p_front[-1][1]: # Look for lower values of Y…
                p_front.append(pair) # … and add them to the Pareto frontier
    # Turn resulting pairs back into a list of Xs and Ys
    p_frontX = [pair[0] for pair in p_front]
    p_frontY = [pair[1] for pair in p_front]
    return p_frontX, p_frontY

X_values, Y_values = pareto_frontier(imported_df["Cost"], imported_df["Utility"], maxX = False, maxY = True)
#pareto_pts = keep_efficient(np.array(imported_df[["Utility", "Cost"]]))
#bool_pareto = (is_pareto_efficient_simple(imported_df[["Utility", "Cost"]].to_numpy()))
#print(pareto_pts)
# print(bool_pareto)
print(X_values, Y_values)
#ax = plt.scatter(X_values, Y_values)
# ax = imported_df.plot(x="Cost", y="Utility", title="Cost vs Utility Use Case #1", color = bool_pareto, kind="scatter")
#fig = ax.get_figure()
#fig.savefig('figure.png')
ax = plt.gca()
ax.set_ylim([0, 1])
plt.scatter(X_values, Y_values, c="red")
plt.plot(X_values, Y_values, 'red', linestyle="--")
plt.title("Cost vs Utility - OS-13")
plt.xlabel("Cost ($ Millions)")
plt.text(300000, 0.9, "Utopia", color="gold")
plt.plot(100000, 0.90, marker='*', markersize=30, color="gold")

# Plot some reference architectures
#First Architecture, Semi-Automated Records
plt.plot(imported_df["Cost"][0], imported_df["Utility"][0], marker='s', markersize=8, color="purple")
plt.plot(2900000, 0.915, marker='s', markersize=8, color="purple")
plt.text(1300000, 0.90, "Ref #1: Semi-Automated Records", color="purple")

#Second Architecture, IoT Dashboard Monitoring
plt.plot(imported_df["Cost"][1], imported_df["Utility"][1], marker='s', markersize=8, color="green")
plt.plot(2900000, 0.865, marker='s', markersize=8, color="green")
plt.text(1300000, 0.85, "Ref #2: IoT Dashboard Monitoring", color="green")

#Third Architecture, VR Equipment Inspection
plt.plot(imported_df["Cost"][2], imported_df["Utility"][2], marker='s', markersize=8, color="darkblue")
plt.plot(2900000, 0.815, marker='s', markersize=8, color="darkblue")
plt.text(1300000, 0.80, "Ref #3: VR Equipment Inspection", color="darkblue")
# Then plot the Pareto frontier on top
# plt.plot(p_front[0], p_front[1])
plt.savefig('figure.png')
