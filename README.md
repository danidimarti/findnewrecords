# HOW TO FIND NEW RECORDS OF A LIST USING THIS SIMPLE PYTHON SCRIPT

#### 1. Download Python on your computer: https://www.python.org/downloads/
>The most recent versions of python already come with IDLE by default. IDLE is a simple file editor you can use to open and edit your script. 


#### 2. Now open the command prompt from your computer. 
> Tip: you can do this by pressing windows + R and writing cmd on the search field

#### 3. Install the Pandas package. 
> Pandas is a python library that allows you to do all sorts of data analysis. To do this write on the command line: *pip install pandas*

#### 4. Now open the script using IDLE or any editor of your choice to start adapting the script to your needs. 

## ADAPTING THE SCRIPT. 

#### 1. To run this script you need two files:
* **Base File**: this is your history file, that is, the file that you are going to base your research on. For example, if you want a “new donors 2020” list, your base file would be your entire list of donors, excluding the year of 2020. 
* **Comparison file**: this is the file you want to compare your list to. Following the same example, the comparison file will be the list of donations made in 2020. 

> IMPORTANT: if you add the script file in the same folder where both your base and your comparison lists are saved, you only need to add their name and extension in the script. Otherwise, you will need to add the entire path of where the csv are stored, like so: ‘C:\Users\Owner\Desktop\WORK\Python Analysis\hist-DonorsList.csv’ 

#### 2. Replace the files names marked in green with yours. Make sure you are using simple quotes: 

#### 3. Define what is going to be the unique identifier of each record in the files. The script will use this ID to find out which instances are new and which are known. The Unique ID can be email or Customer ID, for example. Change the name marked in green below with the correct header name. 

> IMPORTANT: Python is case sensitive. So if the header of your file says ‘Email’ and you write ‘email’ you are going to get an error. 


#### 4. Now it is time to select what columns you want to extract from the comparison to create your New Records List


#### 5. Define a name (e.g. ‘NewDonorsList.csv’) for the output file as well as it’s headers (e.g. firstname, email, country). Don’t forget to put the .CSV extension on the name of the file. 

> IMPORTANT: make sure to have as many headers as the number of columns you have selected on step 4. The script will also match them in the same order as they are listed. 


#### 6. Press F5 to run the script. 

#### 7. You will find the new records file on the same folder as your script is! :)









