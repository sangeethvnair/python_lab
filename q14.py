import matplotlib.pyplot as plt
 def plot_profits(): 
    months = list(range(1, 13))
    profits = []
    print("Enter the profits for each of the 12 months:") 
    for i in range(1, 13): 
        profit = float(input(f"Profit for month {i}: ")) 
        profits.append(profit)  
        plt.figure(figsize=(10, 5)) 
        plt.plot(months, profits, marker='o', linestyle='-', color='blue')  
        plt.xlabel("Month Number") 
        plt.ylabel("Total Profit") 
        plt.title("Monthly Profit of Company ABC") 
        plt.grid(True)  
        plt.xticks(months)  
        plt.show() 
        plot_profits()