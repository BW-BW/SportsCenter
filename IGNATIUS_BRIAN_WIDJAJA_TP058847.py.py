# IGNATIUS BRIAN WIDJAJA
# TP058847

# Function to Log in (Admin and Registered Student)
def login_function(txt, x, y):
    username = input("Please Enter Your Username: ")
    password = input("Please Enter Your Password: ")
    file = open(txt, "r").readlines()
    for line in file:
        info = line.split()  # Split any spacing or tab
        if username == info[x] and password == info[y]:  # match between data input and the .txt files
            print("Welcome to the system")
            return True
    print("Sorry, Wrong Username or Password")
    return False


# Function to find smallest alphabet
def minimum_function(_list):
    smallest = _list[0]
    for i in _list[0:]:  # [0:] is required to read all of the list(start point zero)
        if i < smallest:
            smallest = i
    return smallest


# Function to Sort Name in Ascending
def ascending_name_function(x):
    random_list = []
    coach_file = open("coach.txt", "r").readlines()
    for line in coach_file:
        line_name = (line.split())
        random_list.append(line_name[x])  # Append the number into a list

    alphabetical_list = []
    while random_list:
        mini = minimum_function(random_list)  # function calling
        smallest = mini
        alphabetical_list.append(smallest)  # Append smallest to new list
        random_list.pop(random_list.index(smallest))

    for i in alphabetical_list:  # Print the lines based list
        for line in coach_file:
            line_name = (line.split())
            if i == line_name[x]:
                print(line)


# Function to sort Numbers in Ascending
def ascending_number_function(x):
    str_random_list = []
    int_random_list = []
    ascend_list = []
    single_ascend_list = []
    coach_file = open("coach.txt", "r").readlines()
    for line in coach_file:
        line_name = (line.split())
        str_random_list.append(line_name[x])  # Append the number into a list

    for num in str_random_list:
        int_random_list.append(int(num))  # Change it from str into int

    smallest = int_random_list[0]
    while int_random_list:
        for item in int_random_list:
            if item < smallest:  # Find the smallest
                smallest = item

        ascend_list.append(smallest)  # Append the smallest
        int_random_list.pop(int_random_list.index(smallest))  # Delete the smallest from the list
        smallest = 9999999999

    for i in ascend_list:
        if i not in single_ascend_list:  # Delete all duplicate in ascend list
            single_ascend_list.append(i)

    for i in single_ascend_list:  # Print the lines based on non duplicated list
        for line in coach_file:
            line_name = (line.split())
            if str(i) == line_name[x]:
                print(line)


# Function to search Data based on Detail Given
def search_by_function(display, txt, x):
    search = input(display)
    coach_file = open(txt, "r").readlines()
    for line in coach_file:
        line_id = (line.split())
        if search == line_id[x]:  # Match between search and the lines position
            print(line)


# Function to Display All Data in a file
def display_all_record_function(txt):
    file = open(txt, "r")
    data = file.read()
    print(data)


# Function to Modify Data
def modify_function(txt, x1, x2, display1, display2, num1, num2):
    display_all_record_function(txt)  # function calling
    search1 = input(display1)
    search2 = input(display2)
    modify_list = []
    temp_list = []
    delete = ""
    main_file = open(txt, "r").readlines()
    for line in main_file:  # search the data
        line_id = (line.split())
        if search1 == line_id[x1] and search2 == line_id[x2]:
            delete = line  # delete will not be written in the new .txt
            for item in line_id:  # append to modify_list
                modify_list.append(item)
                temp_list.append(item)  # temp list used to calculate size of list
            break

    print("This is the data you can modify: ")
    print(modify_list[num1:num2])

    size = 0
    while temp_list:  # Find the list's size
        temp_list.pop()
        size = size+1

    mod = input("Which Data You Want to Change? You Need to Input the Exact Same Data: ")
    for i in range(size):
        if mod == modify_list[i]:
            modify_list[i] = input("Enter the New Data: ")

    lines = open(txt, "r").readlines()  # Re Write All lines except the modified one
    del_file = open(txt, "w")
    for line in lines:
        if line != delete:  # Write all except delete
            del_file.write(line)
    del_file.close()

    add_file = open(txt, "a")   # Write modified data to txt
    for element in modify_list:
        add_file.write(element)
        add_file.write('\t')
    add_file.write('\n')
    add_file.close()


# Function to View All Available Sport Center Codes
def place_code_function():
    file = open("location.txt", "r").readlines()
    for line in file:
        line_id = (line.split())
        print("Select " + str(line_id[0]) + " For " + str(line_id[1]))


# Function to View All Available Sport Codes
def sport_code_function():
    name1_list = [""]  # "" require for making it an empty list
    name2_list = []
    file = open("sport.txt", "r").readlines()
    for line in file:
        line_id = (line.split())
        for item in line_id:
            name2_list.append(item)
        if name2_list[0] != name1_list[0]:  # to avoid repetition of same name
            print("Select " + str(name2_list[0]) + " For " + str(name2_list[1]))
        name1_list = name2_list
        name2_list = []


# Function to Automatically Assign Sport Name Based on Number Chosen
def sport_name_function(txt, temp, _list):
    file = open(txt, "r").readlines()
    for line in file:
        line_id = (line.split())
        if temp == int(line_id[0]):  # it is int bcs the "temp" is also int
            data = str(line_id[1]) + "\t" + str(line_id[2])
            _list.append(data)
            break  # for avoiding multiple append


# Function to Automatically Assign Sport Center Name Based on Number Chosen
def sport_location_function(txt, temp, _list):
    file = open(txt, "r").readlines()
    for line in file:
        line_id = (line.split())
        if temp == int(line_id[0]):  # it is int bcs the "temp" is also int
            data = str(line_id[1])
            _list.append(data)


# Function to Add Coach Record
def add_coach_record_function():
    print("You Have Chosen Add Coach Record")
    coach_list = []
    flag = 1
    cnt = 1
    point = ""
    data = ""
    while flag == 1:
        while cnt <= 11:
            if cnt == 1:
                point = "Enter Coach Name(First Name Only!): "
            elif cnt == 2:
                point = "Enter Coach ID: "
            elif cnt == 3:
                point = "Enter Date Joined(DD/MM/YYYY): "
            elif cnt == 4:
                point = "Enter Date Terminated(type n/a if still working): "
            elif cnt == 5:
                point = "Enter Coach Phone Number: "
            elif cnt == 6:
                point = "Enter Coach Address(Don't put any space in address): "
            elif cnt == 7:
                place_code_function()  # function calling
                point = "Enter Coach Sport Center Code: "
            elif cnt == 8:
                temp = int(coach_list[6])
                sport_location_function("location.txt", temp, coach_list)  # function calling
            elif cnt == 9:
                sport_code_function()  # function calling
                point = "Enter Coach Sport Code: "
            elif cnt == 10:
                temp = int(coach_list[8])
                sport_name_function("sport.txt", temp, coach_list)  # function calling
            elif cnt == 11:
                point = "Enter Coach Rating(0 for starter): "

            if cnt != 8 and cnt != 10:
                data = input(point)
                coach_list.append(data)
            if data == "":
                print("You Must Fill This Part")
                continue  # make it go back to the empty entry
            cnt += 1
            flag = flag + 1
        flag = int(input("Do you want to continue? Press 1 to continue, press any other number to terminate"))
        if flag == 1:
            cnt = 1

        coach_file = open("coach.txt", "a")
        for element in coach_list:
            coach_file.write(element)
            coach_file.write('\t')
        coach_file.write('\n')
        coach_file.close()

        rating_file = open("rating.txt", "a")
        rating_file.write(coach_list[0])
        rating_file.write("\t")
        rating_file.write(coach_list[10])
        rating_file.write("\n")
        rating_file.close()

        for element in range(11):
            coach_list.pop()


# Function to Add Sport Center Record
def add_sport_location_function():
    print("You Have Chosen Add Sport Location Record")
    location_list = []
    flag = 1
    cnt = 1
    point = ""
    while flag == 1:
        while cnt <= 2:
            if cnt == 1:
                point = "Enter Location Code: "
            elif cnt == 2:
                point = "Enter Location Name: "
            data = input(point)
            if data == "":
                print("You Must Fill This Part")
                continue
            cnt += 1

            location_list.append(data)
            flag = flag + 1
        flag = int(input("Do you want to continue? Press 1 to continue, press any other number to terminate"))
        if flag == 1:
            cnt = 1

        location_file = open("location.txt", "a")
        for element in location_list:
            location_file.write(element)
            location_file.write('\t')
        location_file.write('\n')
        location_file.close()
        for element in range(2):
            location_list.pop()


# Function to Add Sport Record
def add_sport_record_function():
    print("You Have Chosen Add Sport Record")
    sport_list = []
    flag = 1
    cnt = 1
    data = ""
    point = ""
    while flag == 1:
        while cnt <= 5:
            if cnt == 1:
                point = "Enter Sport Code: "
            elif cnt == 2:
                point = "Enter Sport Name: "
            elif cnt == 3:
                point = "Enter Price per Hour: "
            elif cnt == 4:
                place_code_function()  # function calling
                point = "Enter Sport Center Code: "
            elif cnt == 5:
                temp = int(sport_list[3])
                sport_location_function("location.txt", temp, sport_list)  # function calling
            if cnt != 5:
                data = input(point)
                sport_list.append(data)
            if data == "":
                print("You Must Fill This Part")
                continue
            cnt += 1

            flag = flag + 1
        flag = int(input("Do you want to continue? Press 1 to continue, press any other number to terminate"))
        if flag == 1:
            cnt = 1

        sport_file = open("sport.txt", "a")
        for element in sport_list:
            sport_file.write(element)
            sport_file.write('\t')
        sport_file.write('\n')
        sport_file.close()
        for element in range(5):
            sport_list.pop()


# Function to Add Sport Schedule Record
def add_sport_schedule_record_function():
    print("You Have Chosen Add Sport Schedule Record")
    sport_schedule_list = []
    flag = 1
    cnt = 1
    data = ""
    point = ""
    while flag == 1:
        while cnt <= 6:
            if cnt == 1:
                sport_code_function()  # function calling
                point = "Enter Sport Code: "
            elif cnt == 2:
                temp = int(sport_schedule_list[0])
                sport_name_function("sport.txt", temp, sport_schedule_list)
            elif cnt == 3:
                place_code_function()  # function calling
                point = "Enter Sport Center Code: "
            elif cnt == 4:
                temp = int(sport_schedule_list[2])
                sport_location_function("location.txt", temp, sport_schedule_list)  # function calling
            elif cnt == 5:
                point = "Enter Day: "
            elif cnt == 6:
                point = "Enter Time (Hour:Minute): "
            if cnt != 2 and cnt != 4:
                data = input(point)
                sport_schedule_list.append(data)
            if data == "":
                print("You Must Fill This Part")
                continue
            cnt += 1

            flag = flag + 1
        flag = int(input("Do you want to continue? Press 1 to continue, press any other number to terminate"))
        if flag == 1:
            cnt = 1

        sport_schedule_file = open("sportschedule.txt", "a")
        for element in sport_schedule_list:
            sport_schedule_file.write(element)
            sport_schedule_file.write('\t')
        sport_schedule_file.write('\n')
        sport_schedule_file.close()
        for element in range(6):
            sport_schedule_list.pop()


# Function to Display All Coach Record
def display_all_coach_record_function():
    print("You Have Chosen Display All Coach Record\nThe order is:\n"
          "Name\tID\tDateJoined\tDateTerminated\tPhoneNumber\tAddress\tSportCenterCode"
          "\tSportCenterName\tSportCode\tSportName\tPayRate\tRating")
    display_all_record_function("coach.txt")  # function calling


# Function to Display All Sport Record
def display_all_sport_record_function():
    print("You Have Chosen Display All Sport Record\nThe order is:\n"
          "SportCode\tSportName\tPrice\tSportCenterCode\tSportCenterName")
    display_all_record_function("sport.txt")  # function calling


# Function to Display All Registered Student Record
def display_all_registered_student_record_function():
    print("You Have Chosen Display All Registered Student Record")
    display_all_record_function("student.txt")  # function calling


# Function to Search Coach Record by Coach ID
def coach_by_coach_id_record_function():
    print("You Have Chosen Display Coach by Coach ID Record")
    search_by_function("Enter Coach ID: ", "coach.txt", 1)  # function calling


# Function to Search Coach Record by Coach Rating
def coach_by_overall_rating_record_function():
    print("You Have Chosen Display Coach by Overall Rating Record")
    search_by_function("Enter Coach Rating: ", "coach.txt", 11)  # function calling


# Function to Search Sport Record by Sport ID
def sport_by_sport_id_record_function():
    print("You Have Chosen Display Sport by Sport ID Record")
    search_by_function("Enter Sport ID: ", "sport.txt", 0)  # function calling


# Function to Search Student Record by Student ID
def student_by_student_id_record_function():
    print("You Have Chosen Display Student by Student ID Record")
    search_by_function("Enter Student ID: ", "student.txt", 1)  # function calling


# Function to Sort Coach Record by Alphabetical Order
def coach_ascending_alphabetical_order_function():
    print("You Have Chosen Display Coach Ascending Alphabetical Order")
    ascending_name_function(0)  # function calling


# Function to Sort Coach Record by Pay Rate
def coach_ascending_hourly_pay_rate_order_function():
    print("You Have Chosen Display Coach Ascending Hourly Pay Rate Order")
    ascending_number_function(10)  # function calling


# Function to Sort Coach Record by Rating
def coach_ascending_overall_performance_order_function():
    print("You Have Chosen Display Coach Ascending Overall Performance Order")
    ascending_number_function(11)  # function calling


# Function to Modify Coach Record
def modify_coach_record_function():
    print("You Have Chosen Modify Coach Record\nThis is the Coach Record")
    modify_function("coach.txt", 1, 0, "Enter The Person's Coach ID: ", "Enter The Person's Name: ", 1, 6)


# Function to Modify Sport Record
def modify_sport_record_function():
    print("You Have Chosen Modify Sport Record")
    modify_function("sport.txt", 0, 3, "Enter The Sport's ID: ", "Enter The Location's ID: ", 0, 5)


# Function to Modify Sport Schedule Record
def modify_sport_schedule_record_function():
    print("You Have Chosen Modify Sport Schedule Record")
    modify_function("sportschedule.txt", 0, 3, "Enter The Sport's ID: ", "Enter The Location's ID: ", 5, 7)


# Function to Display Student's Self Record
def display_self_record_detail_function():
    print("You Have Chosen Display Self Record Detail\nPlease Re-Enter Your Username and Password")
    username = input("Please Enter Your Username: ")
    password = input("Please Enter Your Password: ")
    for line in open("student.txt", "r").readlines():  # Read the lines
        info = line.split()  # Split on spacing
        if username == info[12] and password == info[13]:
            print("The order is: "
                  "\nName, Number, BirthDate, JoinedDate, PhoneNumber, Email, Address, Sport Code, Sport Name"
                  ", Price, Sport Center Code, Sport Center Name, username, password")
            print(line)


# Function to Display Student's Registered Sport Schedule Record
def display_registered_sport_schedule_function():
    print("You Have Chosen Display Registered Sport Schedule Detail\nPlease Re-Enter Your Username and Password")
    username = input("Please Enter Your Username: ")
    password = input("Please Enter Your Password: ")
    for line in open("student.txt", "r").readlines():  # Read the lines
        info = line.split()  # Split on spacing
        if username == info[12] and password == info[13]:  # check credential
            for lines in open("sportschedule.txt", "r").readlines():  # to match between student's sport and schedule
                schedule_info = lines.split()
                if info[7] == schedule_info[0] and info[10] == schedule_info[3]:
                    print(schedule_info[1] + " " + schedule_info[5] + " " + schedule_info[6])


# Function to Display Sport Schedule Detail
def display_sport_schedule_detail_function():
    print("You Have Chosen Display Sport Schedule Detail\nThe order is:"
          "\nSportCode\tSportName\tPrice\tSportCenterCode\tSportCenterName\tDay\tTime")
    display_all_record_function("sportschedule.txt")  # function calling


# Function for Admin to Add Records
def add_records_function():
    print("You Have Chosen Add Records")
    print("Select options\n1.Add Coach Record\n2.Add Sport Record"
          "\n3.Add Sport Schedule Record\n4.Add Location")
    flag = 1
    while flag == 1:
        add_records_option = int(input("Enter your choice: "))
        if add_records_option == 1:
            add_coach_record_function()
            break
        elif add_records_option == 2:
            add_sport_record_function()
            break
        elif add_records_option == 3:
            add_sport_schedule_record_function()
            break
        elif add_records_option == 4:
            add_sport_location_function()
            break
        else:
            print("Wrong Choice, Try Again!")
            continue


# Function for Admin to Display All Records
def display_all_records_function():
    print("You Have Chosen Display All Records")
    print("Select options\n1.Display All Coach Record\n2.Display All Sport Record"
          "\n3.Display All Registered Student Record")
    flag = 1
    while flag == 1:
        display_all_records_option = int(input("Enter your choice: "))
        if display_all_records_option == 1:
            display_all_coach_record_function()
            break
        elif display_all_records_option == 2:
            display_all_sport_record_function()
            break
        elif display_all_records_option == 3:
            display_all_registered_student_record_function()
            break
        else:
            print("Wrong Choice, Try Again!")
            continue


# Function for Admin to Search Specific Records
def search_records_function():
    print("You Have Chosen Search Records")
    print("Select options\n1.Coach by Coach ID Record\n2.Coach by Overall Rating Record"
          "\n3.Sport by Sport ID Record\n4.Student by Student ID Record")
    flag = 1
    while flag == 1:
        search_records_option = int(input("Enter your choice: "))
        if search_records_option == 1:
            coach_by_coach_id_record_function()
            break
        elif search_records_option == 2:
            coach_by_overall_rating_record_function()
            break
        elif search_records_option == 3:
            sport_by_sport_id_record_function()
            break
        elif search_records_option == 4:
            student_by_student_id_record_function()
            break
        else:
            print("Wrong Choice, Try Again!")
            continue


# Function for Admin to Sort Records
def sort_records_function():
    print("You Have Chosen Sort Records")
    print("Select options\n1.Coach Ascending Alphabetical Order\n2.Coach Ascending Hourly Pay Rate Order"
          "\n3.Coach Ascending Overall Performance Order")
    flag = 1
    while flag == 1:
        sort_records_option = int(input("Enter your choice: "))
        if sort_records_option == 1:
            coach_ascending_alphabetical_order_function()
            break
        elif sort_records_option == 2:
            coach_ascending_hourly_pay_rate_order_function()
            break
        elif sort_records_option == 3:
            coach_ascending_overall_performance_order_function()
            break
        else:
            print("Wrong Choice, Try Again!")
            continue


# Function for Admin to Modify Records
def modify_record_function():
    print("You Have Chosen Modify Records")
    print("Select options\n1.Modify Coach Record\n2.Modify Sport Record\n3.Modify Sport Schedule Record")
    flag = 1
    while flag == 1:
        modify_records_option = int(input("Enter your choice: "))
        if modify_records_option == 1:
            modify_coach_record_function()
            break
        elif modify_records_option == 2:
            modify_sport_record_function()
            break
        elif modify_records_option == 3:
            modify_sport_schedule_record_function()
            break
        else:
            print("Wrong Choice, Try Again!")
            continue


# Function for Registered Student to Display Some Data
def display_details_function():
    print("You Have Chosen Display Details")
    print("Select options\n1.Display Coach Detail\n2.Display Self-Record Detail\n3.Display Registered Sport Schedule")
    flag = 1
    while flag == 1:
        display_detail_option = int(input("Enter your choice: "))
        if display_detail_option == 1:
            display_all_coach_record_function()
            break
        elif display_detail_option == 2:
            display_self_record_detail_function()
            break
        elif display_detail_option == 3:
            display_registered_sport_schedule_function()
            break
        else:
            print("Wrong Choice, Try Again!")
            continue


# Function for Registered Student to Modify Their Own Record
def modify_self_record_function():
    print("You Have Chosen Modify Self Records")
    modify_list = []
    temp_list = []
    print("Please Re-Enter Your Username and Password")
    username = input("Please Enter Your Username: ")
    password = input("Please Enter Your Password: ")
    for line in open("student.txt", "r").readlines():  # Read the lines
        info = line.split()  # Split on the space, and store the results in a list of two strings
        if username == info[12] and password == info[13]:
            delete = line
            for item in info:
                modify_list.append(item)
                temp_list.append(item)
            print(modify_list[0:7] + modify_list[12:14])  # they can only change this info

            size = 0
            while temp_list:
                temp_list.pop()
                size = size+1

            mod = input("Which Data You Want to Change? You Need to Input the Exact Same Data: ")
            for i in range(size):
                if mod == modify_list[i]:
                    modify_list[i] = input("Enter the New Data: ")

            del_file = open("student.txt", "r")      # Delete the data in txt
            lines = del_file.readlines()
            del_file = open("student.txt", "w")
            for lines in lines:
                if lines != delete:
                    del_file.write(lines)
            del_file.close()

            add_file = open("student.txt", "a")   # Append data to txt
            for element in modify_list:
                add_file.write(element)
                add_file.write('\t')
            add_file.write('\n')
            add_file.close()
            print("Your Record Has Been Updated")


# Function for Registered Student to Give Rating and Feedback
def provide_star_and_feedback_function():
    print("You Have Chosen Provide Star and Feedback\nPlease Re-Enter Your Username and Password")
    username = input("Please Enter Your Username: ")
    password = input("Please Enter Your Password: ")
    str_list = []
    int_list = []
    total = 0
    size = 0
    search = ""
    for line in open("student.txt", "r").readlines():  # Read the lines
        info = line.split()
        if username == info[12] and password == info[13]:  # check credential
            for lines in open("coach.txt", "r").readlines():
                coach_info = lines.split()
                if info[7] == coach_info[8] and info[10] == coach_info[6]:  # to find which coach
                    for liness in open("rating.txt", "r").readlines():
                        rating_info = liness.split()
                        if coach_info[0] == rating_info[0]:
                            file = open("rating.txt", "a")
                            rating = int(input("Enter The Rating (1-5) for Coach " + coach_info[0] + ": "))
                            search = coach_info[0]
                            if rating >= 1 and rating <= 5:
                                feedback = input("Enter Feedback for Coach " + coach_info[0] + ": ")
                                file.write(coach_info[0] + "\t" + str(rating) + "\t" + feedback)
                                file.write("\n")
                                file.close()
                                for x in open("rating.txt", "r").readlines():
                                    rating_info2 = x.split()
                                    if rating_info2[0] == coach_info[0]:
                                        str_list.append(rating_info2[1])
                            else:
                                print("Enter a single integer between 1 to 5")
                                continue
                            break  # to stop repeat inputting
                    break  # to stop from looping multiple times
            for num in str_list:
                int_list.append(int(num))  # TO MAKE THE LIST INTO INTEGER

            for cnt in int_list:
                total = total + cnt
                size = size + 1
            avg = total // (size-1)

            modify_list = []
            temp_list = []
            delete = ""
            main_file = open("coach.txt", "r").readlines()
            for line1 in main_file:  # search the data
                line_id = (line1.split())
                if search == line_id[0]:
                    delete = line1
                    for item in line_id:  # append to modify_list
                        modify_list.append(item)
                        temp_list.append(item)
                    break

            size = 0
            while temp_list:
                temp_list.pop()
                size = size+1

            mod = modify_list[11]
            for i in range(size):
                if mod == modify_list[i]:
                    modify_list[i] = str(avg)

            del_file = open("coach.txt", "r")      # Re Write All lines except the modified one
            lines = del_file.readlines()
            del_file = open("coach.txt", "w")
            for line2 in lines:
                if line2 != delete:
                    del_file.write(line2)
            del_file.close()

            add_file = open("coach.txt", "a")   # Write modified data to txt
            for element in modify_list:
                add_file.write(element)
                add_file.write('\t')
            add_file.write('\n')
            add_file.close()

            total = 0  # Needed if student has multiple coach
            size = 0
            str_list = []
            int_list = []


# Function for Public Student to Display Some Data
def display_sport_and_schedules_function():
    print("You Have Chosen Display Sport and Schedules")
    print("Select options\n1.Display Sport Detail\n2.Display Sport Schedule Detail")
    flag = 1
    while flag == 1:
        display_sport_and_schedule_option = int(input("Enter your choice: "))
        if display_sport_and_schedule_option == 1:
            display_all_sport_record_function()
            break
        elif display_sport_and_schedule_option == 2:
            display_sport_schedule_detail_function()
            break
        else:
            print("Wrong Choice, Try Again!")
            continue


# Function for Public Student to Register as a New Member
def register_as_a_new_student_function():
    print("You Have Chosen Register as a New Student\nEnter Your Personal Data")
    student_list = []
    flag = 1
    cnt = 1
    point = ""
    data = ""
    while flag == 1:
        while cnt <= 13:
            if cnt == 1:
                point = "Enter Your Name(First Name Only!): "
            elif cnt == 2:
                point = "Enter Your Student ID (TP123456): "
            elif cnt == 3:
                point = "Enter Your Date of Birth(DD/MM/YYYY): "
            elif cnt == 4:
                point = "Enter Date Joined(DD/MM/YYYY): "
            elif cnt == 5:
                point = "Enter Your Phone Number: "
            elif cnt == 6:
                point = "Enter Your Email: "
            elif cnt == 7:
                point = "Enter Your Address(Don't put any space in address): "
            elif cnt == 8:
                sport_code_function()  # function calling
                point = "Enter Sport Code You Want to Join: "
            elif cnt == 9:
                temp = int(student_list[7])
                sport_name_function("sport.txt", temp, student_list)  # function calling
            elif cnt == 10:
                place_code_function()  # function calling
                point = "Enter Which Sport Center You Want to Join: "
            elif cnt == 11:
                temp = int(student_list[9])
                sport_location_function("location.txt", temp, student_list)  # function calling
            elif cnt == 12:
                point = "Create New Username: "
            elif cnt == 13:
                point = "Create New Password: "

            if cnt != 9 and cnt != 11:
                data = input(point)
                student_list.append(data)
            if data == "":
                print("You Must Fill This Part")
                continue
            cnt += 1

        flag = int(input("Do you want to continue? Press 1 to continue, press any other number to terminate: "))
        if flag == 1:
            cnt = 1

        student_file = open("student.txt", "a")
        for element in student_list:
            student_file.write(element)
            student_file.write('\t')
        student_file.write('\n')
        student_file.close()
        for element in range(13):
            student_list.pop()


# Function to Show All Admin Options
def admin_function():
    print("Welcome to Admin. Enter your ID and Password")
    if login_function("admin_credential.txt", 0, 1):  # FUNCTION CALLING
        print("Welcome to Admin")
        print("Select options\n1.Add Records\n2.Display All Records\n3.Search Records"
              "\n4.Sort Records\n5.Modify Record\n6.Exit")
        flag = 1
        while flag == 1:
            admin_option = int(input("Enter your choice: "))
            if admin_option == 1:
                add_records_function()
                break
            elif admin_option == 2:
                display_all_records_function()
                break
            elif admin_option == 3:
                search_records_function()
                break
            elif admin_option == 4:
                sort_records_function()
                break
            elif admin_option == 5:
                modify_record_function()
                break
            elif admin_option == 6:
                main_menu_function()
                break
            else:
                print("Wrong Choice, Try Again!")
                continue


# Function to Show All Registered Student Options
def registered_student_function():
    print("Welcome to Registered Student. Enter your ID and Password")
    if login_function("student.txt", 12, 13):  # FUNCTION CALLING
        print("Welcome to Registered Student")
        print("Select options\n1.Display Details\n2.Modify Self Record\n3.Provide Star and Feedback\n4.Exit")
        flag = 1
        while flag == 1:
            reg_student_option = int(input("Enter your choice: "))
            if reg_student_option == 1:
                display_details_function()
                break
            elif reg_student_option == 2:
                modify_self_record_function()
                break
            elif reg_student_option == 3:
                provide_star_and_feedback_function()
                break
            elif reg_student_option == 4:
                main_menu_function()
                break
            else:
                print("Wrong Choice, Try Again!")
                continue


# Function to Show All Public Student Options
def public_student_function():
    print("Welcome to Public Student")
    print("Select options\n1.Display Sport and Schedules\n2.Register as a New Student\n3.Exit")
    flag = 1
    while flag == 1:
        pub_student_option = int(input("Enter your choice: "))
        if pub_student_option == 1:
            display_sport_and_schedules_function()
            break
        elif pub_student_option == 2:
            register_as_a_new_student_function()
            break
        elif pub_student_option == 3:
            main_menu_function()
            break
        else:
            print("Wrong Choice, Try Again!")
            continue


# Function to Show Options to User
def main_menu_function():
    print("----------Welcome to REAL CHAMPIONS SPORT ACADEMY----------")
    print("Select options\n1.Admin\n2.Registered Student\n3.Public Student\n4.Exit")

    flag = 1
    while flag == 1:
        option = int(input("Enter your choice: "))
        if option == 1:
            admin_function()
            break
        elif option == 2:
            registered_student_function()
            break
        elif option == 3:
            public_student_function()
            break
        elif option == 4:
            print("Goodbye")
            break
        else:
            print("Wrong Choice, Try Again!")
            continue


main_menu_function()
