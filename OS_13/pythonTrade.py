import pandas as pd
import numpy as np
import matplotlib.pyplot as plt   

imported_df = pd.read_csv("pythonTrade.csv")

imported_df.plot(x="Utility", y="Cost", kind="scatter")

def pareto_frontier(Xs, Ys, maxX = True, maxY = True):
    # Sort the list in either ascending or descending order of X
    myList = sorted([[Xs[i], Ys[i]] for i in range(len(Xs))], reverse=maxX)
    print(myList[0])
    print(myList[1])
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

X_values, Y_values = pareto_frontier(imported_df["Utility"], imported_df["Cost"], maxX = False, maxY = True)
#pareto_pts = keep_efficient(np.array(imported_df[["Utility", "Cost"]]))
#bool_pareto = (is_pareto_efficient_simple(imported_df[["Utility", "Cost"]].to_numpy()))
#print(pareto_pts)
# print(bool_pareto)
print(X_values, Y_values)
#ax = plt.scatter(X_values, Y_values)
# ax = imported_df.plot(x="Cost", y="Utility", title="Cost vs Utility Use Case #1", color = bool_pareto, kind="scatter")
#fig = ax.get_figure()
#fig.savefig('figure.png')
plt.scatter(X_values, Y_values, c="red")
plt.title("Cost vs Utility Use Case #1")
# Then plot the Pareto frontier on top
# plt.plot(p_front[0], p_front[1])
plt.savefig('figure.png')
