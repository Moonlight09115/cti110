#To make a sale prediction program
#17 February 2019
#CT1-110 P2T1-Sales Prediction
#Noah Knight

# Get the projected total sales.
total_sales = float(input('Enter the projected sales: '))
# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23
# Display the profit.
print('The profit is $', format(profit, ',.2f'))
