import csv
import os


url = os.path.join("PyPoll", "Resources","election_data.csv")

def read():
     with open(url,mode='r') as datafile:
        data =csv.DictReader(datafile, delimiter=',')
        data_lines = [lines for lines in data]
        Total_votes = len(data_lines)
        return(data_lines,Total_votes)
get_data,Tot_votes = read()
winner_dict = {}
def check_data(data,names):
    count = 0
    for lines in data:
        if(lines["Candidate"] == names):
            count += 1
            winner_dict[names] = count
    avg = round(count/Tot_votes*100,2)
    return lambda name: print(f"{name}: {avg}% ({count})")



def display_res():
    print(f"Total Votes: {Tot_votes}")
    Result_Khan = check_data(get_data,"Khan")("Khan")
    Result_Correy = check_data(get_data,"Correy")("Correy")
    Result_Correy = check_data(get_data,"Li")("Li")
    Result_Correy = check_data(get_data,"O'Tooley")("O'Tooley")
    max_key = max(winner_dict, key=winner_dict.get)
    print(f"Winner: {max_key}")

if __name__ == "__main__":
    display_res()

