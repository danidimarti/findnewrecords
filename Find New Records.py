import pandas as pd

# add the name of history file here: 
df1 = 'hist-DonorsList.csv'

#add the name of comparision file here:
df2 = '2020_list_unicode.csv'


# read the files. Setting low_memory to F to get rid of error
# SEP= in the paranthesis below specifies the separator of your csv file. 
base_file = pd.read_csv(df1, sep=',', header=0, low_memory=False)
comparison_file = pd.read_csv(df2, sep=',', header=0, low_memory=False)


#get email (unique identifier) from 'base' (old) and comparison (new) csv
#transform each csv to a list

emailList_base = base_file['email'].to_list()
emailList_comparison = comparison_file['Email'].to_list()


#crate empty range to store comparision (new) csv

list_20 = []


#iterate over rows of new csv
#get relevant columns for new csv
#append rows to empty range

for index, rows in comparison_file.iterrows():
    columns_20 = [
        rows['Firstname'],
        rows['Lastname'],
        rows['Gender'],
        rows['Email'],
        rows['Country'],
        rows['FormCode'],
        rows['Slug'],
        rows['UtmSource'],
        rows['UtmMedium'],
        rows['UtmCampaign'],
        rows['UtmTerm'],
        rows['DonationAmount'],
        rows['PaymentStatus'],
        rows['PaymentMethod'],
        rows['PaymentDate']
        ]

    list_20.append(columns_20)
    
#create empty range to store the comparison result
    
NewDonorsList = []


#define the length of the comparision file
length = len(emailList_comparison)

#iterate the new list (NOT RANGE)
#check records NOT in old list
#append results to empty range
for x in range(length):
    if emailList_comparison[x] not in emailList_base:
        NewDonorsList.append(list_20[x])

#transform range/list to dataframe
df = pd.DataFrame(NewDonorsList)

#transform data frame to csv
#export to csv
csv_newdonors = df.to_csv('NewDonorsList.csv', index=False, header=['Firstname',
'Lastname',
'Gender',
'Email', 
'Country',
'FormCode',
'Slug',
'UtmSource',
'UtmMedium',
'UtmCampaign',
'UtmTerm',
'DonationAmount',
'PaymentStatus',
'PaymentMethod',
'PaymentDate'
])


print(NewDonorsList)


