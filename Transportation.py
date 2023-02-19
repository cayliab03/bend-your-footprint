class Transportation:

    """
    This class contains all questions related to transportation and calculates a score based on user inputs
    """

    def __init__(self):
        self.total_score = 0
        self.primary_mode_of_transport = ""
        self.purple_text = "\033[0;49;35m"
        self.green_text = "\033[0;49;32m"
        self.text_reset = "\033[0;49;38m"


    """
    calls call questions related to transportation in Transportation class
    
    :return double representing final transportation score
    """

    def call_transport_questions(self):  # transportation-related questions master-list
        self.total_score += self.primary_mode_of_transportation()
        self.total_score += self.airplane_flight_frequency()
        return self.total_score


    """
    determines user's primary mode of transport and sets variable primary_mode_of_transport to user choice
    
    :return double of user's primary transport score 
    """

    def primary_mode_of_transportation(self):
        print(self.purple_text, "\n\nWhat is your primary mode of transportation?", self.text_reset)
        print("\t1. Car\n\t2. Public transport\n\t3. Bike\n\t4. Walking")

        choice = self.check_user_input(1, 5)  # ensures user inputted valid int within given options

        if choice == 1:  # choice 1 - car
            self.primary_mode_of_transport = "drive"
            return self.frequency_of_travelling(5)
        elif choice == 2:  # choice 2 - public transport
            self.primary_mode_of_transport = "commute"
            return self.frequency_of_travelling(2)
        elif choice == 3:  # choice 3 - bike
            self.primary_mode_of_transport = "bike"
            return 0
        else:  # choice 4 - walking
            self.primary_mode_of_transport = "walk"
            return 0


    """
    determines how often the user commutes using car or public transport and updates their current transport score
    then, calls method distance_of_travelling to finish transportation score of mode of choice
    
    :param double temp_score    current score of user's primary transportation mode
    :return double of result of method distance_from_travelling
    """

    def frequency_of_travelling(self, temp_score):
        print(self.purple_text, "\n\nHow many days do you " + self.primary_mode_of_transport + " each week?",
              self.text_reset)
        print("\t1. Over 5 days a week\n\t2. 4-5 days a week\n\t3. 2-3 times a week\n\t4. 1 or no days a week")
        choice = self.check_user_input(1, 5)

        # if primary mode of choice is car, temp_score is multiplied by a higher number
        if choice == 1:  # >5 days a week
            if self.primary_mode_of_transport == "commute":  # public transport
                temp_score = temp_score * 1.2
            else:  # car
                temp_score = temp_score * 3
        elif choice == 2:  # 4-5 times a week:
            if self.primary_mode_of_transport == "drive":
                temp_score = temp_score * 2.5
        elif choice == 1:  # 2-3 times a week
            if self.primary_mode_of_transport == "drive":
                temp_score = temp_score * 2
        # if <=1 day = temp_score unchanged
        return self.distance_of_travelling(temp_score)


    """
    determines how far the user commutes using car or public transportation and returns their final score of their 
    transportation mode of choice (if they use public transport) or passes on the current core to carpool method
    
    :param double temp_score    current score of user's primary transportation mode
    
    :return double of transportation score of primary mode of choice
    """

    def distance_of_travelling(self, temp_score):
        print(self.purple_text, "\n\nOn average, how far do you travel each day (includes both to destination "
                                "and return home?", self.text_reset)
        print("\t1. Over 40 km\n\t2. 20-40 km\n\t3.10-19 km\n\t4.>10 km")
        choice = self.check_user_input(1, 5)

        if choice == 4:  # >40 km
            return self.carpool(temp_score) * 1.25 if self.primary_mode_of_transport == "commute" \
                else self.carpool(temp_score * 2)
        elif choice == 3:  # 20<x<40 km
            return self.carpool(temp_score) * 1.15 if self.primary_mode_of_transport == "commute" \
                else self.carpool(temp_score * 1.75)
        elif choice == 2:  # 10<x<19 km
            return self.carpool(temp_score) if self.primary_mode_of_transport == "commute" \
                else self.carpool(temp_score * 1.5)
        elif choice == 1:  # <10 km
            return self.carpool(temp_score) if self.primary_mode_of_transport == "commute" \
                else self.carpool(temp_score * 1.25)


    """
    determines if user carpool (only is their primary mode is car) and adjusts their score 
    
    :param temp_score    
    :return double of transportation score of car users     
    """

    def carpool(self, temp_score):
        print(self.purple_text, "\n\nDo you carpool frequently?", self.text_reset)
        print("\t1. Yes\n\t2. No")
        choice = self.check_user_input(1, 3)

        return temp_score * 0.75 if choice == 1 else temp_score


    """
    calculates the frequency portion of user's flight score if they input that they fly by airplane
    
    :return 0 if user does not use airplanes or return value from method airplane_flight_distance
    """

    def airplane_flight_frequency(self):
        print("\n\n", self.purple_text, "How often do you fly every year?", self.text_reset)
        print("\t1. Every week\n\t2. Every month\n\t3. Every few months\n\t4. 1-2 times a year\n\t5. Almost never")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # flies every week
            return self.airplane_flight_distance(5)
        elif choice == 2:  # flies every month
            return self.airplane_flight_distance(4)
        elif choice == 3:   # flies every few months:
            return self.airplane_flight_distance(3)
        elif choice == 4:  # flies once or twice a year
            return self.airplane_flight_distance(2)
        else:  # never flies by airplane
            return 0


    """
    determines average length of user's flights and calculates flight score

    :param frequency                number of flights taken each year
    :return double of flight score
    """

    def airplane_flight_distance(self, frequency):  # measure by hours
        print(self.purple_text, "\n\nOn average, how long are your flights?", self.text_reset)
        print("\t1. Over 10 hours (long distance)\n\t2. Between 4-9 hours (medium distance)\n\t"
              "3. Less than 4 hours (short distance)")
        choice = self.check_user_input(1, 4)

        if choice == 1:  # long distance
            return frequency * 5
        elif choice == 2:  # medium distance
            return frequency * 3.5
        else:
            return frequency * 2  # short distance


    """
    ensures user inputted a valid integer to select an answer
    
    :param min_range                value of lowest-numbered option
    :param                          value of highest-numbered option
    
    :return int of user's choice
    """

    def check_user_input(self, min_range, max_range):
        while True:
            try:
                user_input = int(input())

                if user_input in range(min_range, max_range):
                    return user_input
                else:
                    print(self.green_text, "Enter a valid choice: ", self.text_reset)

            except ValueError:
                print(self.green_text, "Enter a valid choice: ", self.text_reset)
