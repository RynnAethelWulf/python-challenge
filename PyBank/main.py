import csv
url = "./PyBank/Resources/PyBank_Resources.csv"
def read():
     with open(url,mode='r') as datafile:
        data =csv.DictReader(datafile, delimiter=',')
        
        for values in data:
            print(values['Date'],int(values['Profit/Losses']))
            if(max(int(values['Profit/Losses']))):
                G_profit =  values    
        
        data_lines = [lines for lines in data]
        Total_votes = len(data_lines)
        return(data_lines,Total_votes)
get_data,Tot_votes = read()
# print(get_data)


total  = [int(sum_data['Profit/Losses']) for sum_data in get_data]

print(Tot_votes)
print(sum(total))
print((sum(total)/len(total)))
print(max(total))
print(min(total))
print(data)
