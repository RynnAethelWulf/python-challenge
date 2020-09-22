import csv
import os 

url_in = os.path.join("PyBank","Resources","budget_data.csv")
url_out = os.path.join("PyBank","Analysis","result.txt")

with open(url_in,'r') as data_file:
    data = csv.reader(data_file, delimiter = ',')
    
    header = next(data)
    months = []
    profit_loss = []
    for rows in data:
        months.append(rows[0])
        profit_loss.append(int(rows[1]))
#     print(len(months))
    
    change = []
    for i in range(1,len(profit_loss)):
        change.append(profit_loss[i]-profit_loss[i-1])
    average= sum(change)/len(change)    
    
    max_month = change.index(max(change))+1
    min_month = change.index(min(change))+1
#     print(months[value])




lines = ["Financial Analysis\n------------------------------\n",
                      f'Total months is {len(profit_loss)}\n',
                     f'Total net total  is ${sum(profit_loss)}\n',
                      f'Average  Change  is ${round(average,2)}\n',
                     f'Greatest Increase in Profits: {months[max_month]} (${max(change)})\n',
                     f'Greatest Decrease  in Profits: {months[min_month]} (${min(change)})']
                    
    


#     print(f'Total net total  is ${sum(profit_loss)}')    
#     print(f'Average  Change  is ${round(average,2)}')
#     print(f'Greatest Increase in Profits: {months[max_month]} (${max(change)})')
#     print(f'Greatest Decrease  in Profits: {months[min_month]} (${min(change)})')

with open(url_out,'w') as out_file:
    out_file.writelines(lines)