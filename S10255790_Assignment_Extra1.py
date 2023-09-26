#Brandon Koh Ziheng S10255790 P17
#the additional feature added was using the data.gov.sg provided API to retrieve real time carpark availability whenever the user chooses [11]
#itemgetter module will be used in option 10

from operator import itemgetter

#requests module will be used later on to open the json file from data.gov.sg (need to install with pip install)

import requests

#defining option functions (3 and 10 i did inside the program because it involved opening files
def option1(length):
    #print option
    print("Option 1: Display Total Number of Carparks in 'carpark-information.csv'")
    #print total num of carparks
    print("Total Number of Carparks in 'carpark-information.csv':",length)
    
def option2(carparkinfo):
    #print option
    print("Option 2: Display All Basement Carparks in 'carpark-information.csv'")
    #print header
    print("{0:<15} {1:<15} {2:<15}".format("Carpark No", "Carpark Type", "Address"))
    #initialise counter
    basementcount = 0
    #loop through carpark
    for carpark in carparkinfo:
        #print basement carparks
        if carpark["Carpark Type"] == "BASEMENT CAR PARK":
            print("{0:<15} {1:<15} {2:<15}".format(carpark["Carpark Number"], carpark["Carpark Type"], carpark["Address"]))
            #add counter
            basementcount += 1
    #print the count of the basement carparks
    print("Total number:",basementcount)

def option3(availabilityfile):
    #print timestamp
    print(availabilityfile[0])
    #get the header of the file, split and strip it 
    keylist2 = availabilityfile.pop(1)
    keylist2 = keylist2.strip("\n") 
    keylist2 = keylist2.split(",")
    carpark = []
    #remove first line of the file because it is not carpark data
    availabilityfile.pop(0)
    for line in availabilityfile:
        #strip, replace the "" with nothing and split each line in the file (ensure split by only 3 commas, as some lines have commas in address)
        line = line.strip("\n")
        line = line.split(",",3)
        #make a dictionary with the values in the file
        carpark.append({keylist2[0]:line[0],keylist2[1]:line[1],keylist2[2]:line[2]})
    return carpark

def option4(length):
    #print option
    print("Option 4: Print Total Number of Carparks in the File Read in [3]")
    #print total carparks in file
    print("Total Number of Carparks in the File:",length)

def option5(carpark):
    #print option
    print("Option 5: Display Carparks without Available Lots")
    #initialise count
    emptycount = 0
    #loop through carpark list
    for line in carpark:
        #add counter whenever there are empty lots
        if int(line["Lots Available"]) == 0:
            emptycount+=1
            print("Carpark number:",line["Carpark Number"])
    #print how many empty lots
    print("Total number:",emptycount)

def option6(carpark):
    print("Option 6: Display Carparks With At Least x% Available Lots")
    #user input percent and validation
    try:
        percent = float(input("Enter the percentage required: "))
        #print header
        print("{0:<15} {1:<15} {2:<15} {3:<15}".format("Carpark No", "Total Lots", "Lots Available", "Percentage"))
        hitcount = 0
        #loop through every carpark's dictionary
        for line in carpark:
            #finding percentage
            if int(line["Lots Available"]) == int(line["Total Lots"]) and int(line["Total Lots"]) != 0:
                percentage = 100.0
            elif int(line["Total Lots"]) != 0:
                percentage = round((int(line["Lots Available"]) / (int(line["Total Lots"]))*100),1)
            #print if its at least user input
            if percentage >= percent:
                print("{0:<15} {1:<15} {2:<15} {3:<15}".format(line["Carpark Number"], line["Total Lots"], line["Lots Available"], percentage))
                hitcount+=1
        #print count
        print("Total number:",hitcount)
    except:
        print("Please enter a valid percentage.")

def option7(info,carpark):
    print("Option 7: Display Addresses of Carparks With At Least x% Available Lots")
    #user input percent and validation
    try:
        percent = float(input("Enter the percentage required: "))
        #print header
        print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}".format("Carpark No", "Total Lots", "Lots Available", "Percentage", "Address"))
        hitcount = 0
        #loop through every carpark's dictionary
        for line in carpark:
            #finding percentage
            if int(line["Lots Available"]) == int(line["Total Lots"]) and int(line["Total Lots"]) != 0:
                percentage = 100.0
            elif int(line["Total Lots"]) != 0:
                percentage = round((int(line["Lots Available"]) / (int(line["Total Lots"]))*100),1)
            #print if its at least user input
            if percentage >= percent:
                print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}".format(line["Carpark Number"], line["Total Lots"], line["Lots Available"], percentage, address))
                hitcount+=1
            #retrieving address
            for i in info:
                if line["Carpark Number"] == i["Carpark Number"]:
                    address = i["Address"]
        #print count
        print("Total number:",hitcount)
    except:
        print("Please enter a valid percentage.")
    
def option8(info,carpark):
    print("Option 8: Display All Carparks at a Given Location")
    #make a found variable to see if the location was found without getting errors
    found = 0
    count = 0
    #get location and capitalise it
    location = str(input("Enter location: ")).upper()
    for line in info:
        if location in line["Address"]:
            found = 1
                
    if found == 0:
        print("Location not found.")
        
    if found == 1:
        #print header
        print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}".format("Carpark No", "Total Lots", "Lots Available", "Percentage", "Address"))
        for line in info:
            #check if location in the address of that line, and then put the carpark number into a variable
            if location in line["Address"]:
                carparknum = line["Carpark Number"]
                for i in carpark:
                    #if both carpark numbers match up, they are the same carpark so the percentage will be accurate to that carpark
                    if carparknum == i["Carpark Number"]:
                        count+=1
                        #finding percentage, excluding the carparks with 0 total lots
                        if int(i["Lots Available"]) == int(i["Total Lots"]) and int(i["Total Lots"]) != 0:
                            percentage = 100.0
                        elif int(i["Total Lots"]) != 0:
                            percentage = round((int(i["Lots Available"]) / (int(i["Total Lots"]))*100),1)
                        #print each line
                        print("{0:<15} {1:<15} {2:<15} {3:<15} {4:<15}".format(line["Carpark Number"], i["Total Lots"], i["Lots Available"], percentage, line["Address"]))
        print("Number of carparks in this location:",count)
                        
def option9(info,carpark):
    #print option
    print("Option 9: Display Carpark with the Most Parking Lots")
    #initialise highest variable
    highest = 0
    for line in carpark:
        if int(line["Total Lots"]) > highest:
            #replace the variables if they are higher in the line
            highest = int(line["Total Lots"])
            highestnum = line["Carpark Number"]
            highestavail = line["Lots Available"]
            #finding percentage, exlcuding the carparks with 0 total lots
            if int(line["Lots Available"]) == int(line["Total Lots"]) and int(line["Total Lots"]) != 0:
                percentage = 100.0
            elif int(line["Total Lots"]) != 0:
                percentage = round((int(line["Lots Available"]) / (int(line["Total Lots"]))*100),1)
    for line in info:
        if line["Carpark Number"] == highestnum:
            #print header
            print("{0:<23} {1:<23} {2:<23} {3:<23} {4:<23} {5:<23} {6:<23}".format("Carpark No", "Carpark Type", "Type of Parking System","Total Lots", "Lots Available", "Percentage", "Address"))
            #print specific carpark info
            print("{0:<23} {1:<23} {2:<23} {3:<23} {4:<23} {5:<23} {6:<23}".format(highestnum, line["Carpark Type"], line["Type of Parking System"], highest, highestavail, percentage, line["Address"]))

def option10(info,carpark):
    addresscarpark = []
    for i in info:
        addinglist = []
        for line in carpark:
            #match up the two lists carpark number so it is the correct carpark info
            if line["Carpark Number"] == i["Carpark Number"]:
                #check if that carpark has been added
                if line["Carpark Number"] not in addinglist:
                    #if not added, add these few variables into the placeholder list 
                    addinglist.append(line["Carpark Number"])
                    addinglist.append(int(line["Total Lots"]))
                    addinglist.append(int(line["Lots Available"]))
                    addinglist.append(i["Address"] + "\n")
        #if placeholder list empty, dont append
        if addinglist == []:
            continue
        #if placeholder list not empty, append to the main carpark list
        else:
            addresscarpark.append(addinglist)
    #sort the addresscarpark nested list based on index 2 which is the lots available in each inner list
    addresscarpark = sorted(addresscarpark, key = itemgetter(2))
    for lst in range(len(addresscarpark)):
        for i in range(len(addresscarpark[lst])):
            #convert all elements to string so they can be joined
            addresscarpark[lst][i] = str(addresscarpark[lst][i])
        #join every list so it can be written to the csv by writelines()
        addresscarpark[lst] = ",".join(addresscarpark[lst])
        
        
    #insert the header in the first line
    addresscarpark.insert(0,"Carpark Number,Total Lots,Lots Available,Address\n")
    return addresscarpark


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
#read file at start of program
print(""" .----------------.  .----------------.  .----------------.   .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. | | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |   ______     | || |  _______     | || |    ______    | | | |      __      | || |    _______   | || |    _______   | || |    ______    | || |     __       | |
| |  |_   __ \   | || | |_   __ \    | || |  .' ___  |   | | | |     /  \     | || |   /  ___  |  | || |   /  ___  |  | || |  .' ___  |   | || |    /  |      | |
| |    | |__) |  | || |   | |__) |   | || | / .'   \_|   | | | |    / /\ \    | || |  |  (__ \_|  | || |  |  (__ \_|  | || | / .'   \_|   | || |    `| |      | |
| |    |  ___/   | || |   |  __ /    | || | | |    ____  | | | |   / ____ \   | || |   '.___`-.   | || |   '.___`-.   | || | | |    ____  | || |     | |      | |
| |   _| |_      | || |  _| |  \ \_  | || | \ `.___]  _| | | | | _/ /    \ \_ | || |  |`\____) |  | || |  |`\____) |  | || | \ `.___]  _| | || |    _| |_     | |
| |  |_____|     | || | |____| |___| | || |  `._____.'   | | | ||____|  |____|| || |  |_______.'  | || |  |_______.'  | || |  `._____.'   | || |   |_____|    | |
| |              | || |              | || |              | | | |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' | | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'   '----------------'  '----------------'  '----------------'  '----------------'  '----------------'""")
infoextension = "carpark-information.csv"
file = open(infoextension,'r')
file = file.readlines()
info = []
#pop first line, as it is the header
keylist = file.pop(0)
#strip the \n from line
keylist = keylist.strip("\n")
#split the header by the comma
keylist = keylist.split(",")
for line in file:
    #strip and split all the rest of the lines
    line = line.strip("\n")
    line = line.split(",",3)
    #append the dictionary for each line into the list
    info.append({keylist[0]:line[0],keylist[1]:line[1],keylist[2]:line[2],keylist[3]:line[3]})
#set a boolean variable later to see if option 3 has been done before
opt3 = False
#display main menu
while True:
    print("MENU\n====\n[1] Display Total Number of Carparks in 'carpark-information.csv'\n[2] Display All Basement Carparks in 'carpark-information.csv'\n[3] Read Carpark Availability Data File\n[4] Print Total Number of Carparks in the File Read in [3]/[11]")
    print("[5] Display Carparks Without Available Lots\n[6] Display Carparks With At Least x% Available Lots\n[7] Display Addresses of Carparks With At Least x% Available Lots\n[8] Display All Carparks at a Given Location")
    print("[9] Display Carpark with the Most Parking Lots\n[10] Create an Output File with Carpark Availability and Addresses\n[11] Get Most Recent Carpark Data from data.gov.sg\n[0] Exit")
    #user option input and validation
    try:
        user = int(input("Enter your option: "))
    except:
        print("Please enter a valid option.")
        continue

#option 1: Display Total Number of Carparks in 'carpark-information.csv'
    
    if user == 1:
        #print empty line
        print()
        option1(len(info))
        
#option 2: Display All Basement Carparks in 'carpark-information.csv'
        
    if user == 2:
        #print empty line
        print()
        option2(info)
        
#option 3: Read Carpark Availability Data File
        
    if user == 3:
        #print empty line
        print()
        #turn boolean true so other options can see that it is done
        opt3 = True
        #print option line
        print("Option 3: Read Carpark Availability Data File")
        #user input and validation
        try:
            filename = input("Enter the file name: ")
            availabilityfile = open(filename, 'r')
        except FileNotFoundError:
            print("Not a valid file name.")
            print()
            continue
        availabilityfile = availabilityfile.readlines()
        carpark = option3(availabilityfile)
            
#option 4: Print Total Number of Carparks in the File Read in [3]
            
    if user == 4:
        #print empty line
        print()
        #check if option 3 true before going on 
        if opt3 == True:
            option4(len(carpark))
        #print error message if option 3 false
        elif opt3 == False:
            print("Please choose [3]/[11] first to read Carpark Availability Data File")
            
#option 5: Display Carparks without Available Lots
            
    if user == 5:
        #print empty line
        print()
        #check if option 3 true before going on 
        if opt3 == True:
            option5(carpark)
        elif opt3 == False:
            print("Please choose [3]/[11] first to read Carpark Availability Data File")
            
#option 6: Display Carparks With At Least x% Available Lots
            
    if user == 6:
        #print empty line
        print()
        #check if option 3 true before going on 
        if opt3 == True:
            option6(carpark)
            
                
        #print error message if option 3 false
        elif opt3 == False:
            print("Please choose [3]/[11] first to read Carpark Availability Data File")

#option 7: Display Addresses of Carparks With At Least x% Available Lots

    if user == 7:
        #print empty line
        print()
        #check if option 3 true before going on 
        if opt3 == True:
            option7(info,carpark)     

        #print error message if option 3 false
        elif opt3 == False:
            print("Please choose [3]/[11] first to read Carpark Availability Data File")
            
#option 8 Display all carparks at a given location
            
    if user == 8:
        #print empty line
        print()
        #check if option 3 true before going on 
        if opt3 == True:
            option8(info,carpark)

        #print error message if option 3 false
        elif opt3 == False:
            print("Please choose [3]/[11] first to read Carpark Availability Data File")
            
#option 9: Display Carpark with the Most Parking Lots
            
    if user == 9:
        #print empty line
        print()
        #check if option 3 true before going on 
        if opt3 == True:
            option9(info,carpark)

    #print error message if option 3 false
        elif opt3 == False:
            print("Please choose [3]/[11] first to read Carpark Availability Data File")
        
#option 10: Create output file with addresses and sort by lots available
        
    if user == 10:
        #print empty line
        print()
        #check if option 3 true before going on 
        if opt3 == True:
            addresscarpark = option10(info,carpark)
            #open file
            with open("carpark-availability-with-addresses.csv","w") as newfile:
                #write to the file with writelines(), as it can write multiple lines at a time
                for i in range(len(addresscarpark)):
                    newfile.write(addresscarpark[i])
                print("carpark-availability-with-address.csv has been added to your directory.")

        #print error message if option 3 false
        elif opt3 == False:
            print("Please choose [3]/[11] first to read Carpark Availability Data File")

#option 11: Get Most Recent Carpark Data from data.gov.sg

    if user == 11:
        #this option is an alternative to option 3, so it should set opt3 = True
        opt3 = True
        #print empty line
        print()
        #fetch the realtime carpark data
        response = requests.get("https://api.data.gov.sg/v1/transport/carpark-availability")
        #empty carpark list to be replaced with current data
        carpark = []
        #check for status code, as API documentation says that 200 means success
        if response.status_code == 200:
            #returns a list/dict based on the structure of the json in the file
            data = response.json()
            #get carpark availability info from data (extract the value of the key 'items' in the data file)
            carpark_data = data.get("items", [])
            #items is where timestamp is stored, so go through items to find it
            for entry in carpark_data:
                #get timestamp or else put N/A
                timestamp = entry.get("timestamp", "N/A")
                carpark_info = entry.get("carpark_data", [])
                #loop through carpark_data which actually has the info of the carpark
                for cp in carpark_info:
                    #get carpark number, else put N/A
                    carpark_number = cp.get("carpark_number", "N/A")
                    #get carpark lot information
                    carpark_lots = cp.get("carpark_info", [])
                    for lot in carpark_lots:
                        #get total lots, else N/A
                        total_lots = lot.get("total_lots", "N/A")
                        #get available lots, else N/A
                        lots_available = lot.get("lots_available", "N/A")
                        #append the dictionary in the same format as option 3 into the 'carpark' list which is the same one that option 3 used
                        carpark.append({"Carpark Number":carpark_number,"Total Lots":total_lots,"Lots Available":lots_available})
            #insert the timestamp at the start, same as option 3 format
            print("Timestamp:",timestamp)
            print("Successfully obtained most recent carpark data from data.gov.sg.\n")
                        
        else:
            print("Failed to obtain data from data.gov.sg.")
            
          
#option 0: Exit
    if user == 0:
        break
    if opt3 == True or opt3 == False:
        continue
        
#print empty line before menu appears again
    print()
