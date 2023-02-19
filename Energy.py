class Energy:

    """
    This class contains all questions related to transportation and calculates a score based on user inputs
    """

    def __init__(self):
        self.total_score = 0
        self.purple_text = "\033[0;49;35m"
        self.green_text = "\033[0;49;32m"
        self.text_reset = "\033[0;49;38m"


    """
    calls call questions related to energy in Energy class
    
    :return double representing final energy score
    """

    def call_energy_questions(self):
        self.total_score += self.house_to_family_ratio()
        self.total_score += self.dishwasher_usage()
        self.total_score += self.dryer_usage()
        self.total_score += self.gasoline_usage()
        self.total_score += self.has_led_lights()
        self.total_score += self.has_smart_thermostat()
        self.total_score += self.cooking_usage()
        self.renewable_energy_usage()
        return self.total_score


    """
    determines the size of the user's home 
    
    :return int representing their home size value
    """

    def home_size(self):
        print("\n\n", self.purple_text, "What best describes the size of your home?", self.text_reset)
        print("\t1. Apartment\n\t2. Small house\n\t3. Medium-sized house\n\t4. Large house")
        choice = self.check_user_input(1, 5)

        if choice == 1:  # apartment
            return 1
        elif choice == 2:  # small house
            return 2
        elif choice == 1:  # medium house
            return 3
        else:  # large house
            return 5


    """
    determines the size of the user's family
    
    :return the number the user inputs, which represents the number of people in their home
    """

    def family_size(self):
        print(self.purple_text, "\n\nHow many people live in your home?", self.text_reset)
        print("\t1. 1 person\n\t2. 2 people\n\t3. 3 people\n\t4. 4 people\n\t5. 5 people")
        choice = self.check_user_input(1, 6)

        return choice


    """
    determines the ratio of the user's house size to how many people live in their home
    the smaller houses with more people will have a better score than larger houses with more people
    
    :return integer representing the user's home-size to family-size ratio
    """

    def house_to_family_ratio(self):
        return self.home_size() - self.family_size()


    """
    determines if the user uses a dishwasher and how often they use it
    
    :returns double representing dishwasher score 
    """

    def dishwasher_usage(self):
        print(self.purple_text, "\n\nDo you use a dishwasher?", self.text_reset)
        print("\t1. Yes\n\t2. No")
        choice = self.check_user_input(1, 3)

        if choice == 2:  # no
            return 0

        print(self.purple_text, "\nHow many times a week do you use it", self.text_reset)
        print("\t1. Multiple times a day\n\t2. Once a day\n\t3. 4-6 times a week\n\t4. 1-3 times a week"
              "\n\t5. Not very often")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # multiple times a day
            return 4.5
        elif choice == 2:  # daily use
            return 3
        elif choice == 3:  # 3-5 times a week
            return 1.5
        elif choice == 4:  # 1-2 times a week
            return 1
        else:    # Not very often
            return 0.5


    """
    determines if the user uses a dryer and how often they use it
    
    :returns double representing dryer score
    """

    def dryer_usage(self):
        print(self.purple_text, "\n\nDo you use a dryer?", self.text_reset)
        print("\t1. Yes\n\t2. No")
        choice = self.check_user_input(1, 3)

        if choice == 2:  # no
            return 0

        print(self.purple_text, "\n\nHow many times a week do you use it?", self.text_reset)
        print("\t1. Once a day\n\t2. 5-6 times a week\n\t3. 3-4 times a week\n\t4. 1-2 times a week"
              "\n\t5. Not very often")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # daily
            return 4.5
        elif choice == 2:  # 5-6 times
            return 3
        elif choice == 3:  # 3-4 times a week
            return 2
        elif choice == 4:  # 1-2 times a week
            return 1.5
        else:  # Not very often
            return 0.5


    """
    determines how often a user's fills up their gas tank
    
    :returns double representing their gasoline usage score
    """

    def gasoline_usage(self):
        print(self.purple_text, "\n\nDo you own a car?", self.text_reset)
        print("\t1. Yes\n\t2. No")
        choice = self.check_user_input(1, 3)

        if choice == 2:
            return 0

        print(self.purple_text, "\n\nHow many times a week do you fill your gas tank?", self.text_reset)
        print("\t1. None (own electric car)\n\t2. Not very often\n\t3. 1-2 a week\n\t4. Couple times a week"
              "\n\t5. Almost everyday")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # none
            return 0
        elif choice == 2:  # not often
            return 1
        elif choice == 3:  # 1-2 times a week
            return 3
        elif choice == 4:  # couple times
            return 4
        else: # almost daily
            return 5


    '''
    determines if user has led lights in their home
    
    :return int representing their led light score
    '''

    def has_led_lights(self):
        print(self.purple_text, "\n\nDo you have LED lights?", self.text_reset)
        print("\t1. Yes\n\t2. No")
        choice = self.check_user_input(1, 3)

        if choice == 1:  # yes
            return 0
        else:  # no
            return 3


    '''
    determines if user has a smart thermostat in their home

    :return int representing their smart thermostat score
    '''

    def has_smart_thermostat(self):
        print(self.purple_text, "\n\nDo you have a smart thermostat?", self.text_reset)
        print("\t1. Yes\n\t2. No")
        choice = self.check_user_input(1, 3)

        if choice == 1:  # yes
            return 0
        else:  # no
            return 3


    """
    determines the user's electricity usage from cooking
    
    :return double representing the user's cooking usage score
    """

    def cooking_usage(self):
        print(self.purple_text, "\n\nDo you cook at home?", self.text_reset)
        print("\t1. Yes\n\t2. No")
        choice = self.check_user_input(1, 3)

        if choice == 2:  # no
            return 0

        print(self.purple_text, "\n\nHow often do you cook?", self.text_reset)
        print("\t1. Very rarely\n\t2. Few meals a week \n\t3. Many meals a week\n\t4. Most meals a week"
              "\n\t5. Almost all meals")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # very rarely
            temp_score = 0.5
        elif choice == 2:  # few meals
            temp_score = 1
        elif choice == 2:  # many meals
            temp_score = 1.5
        elif choice == 3:  # most meals
            temp_score = 2
        else:
            temp_score = 2.5

        print(self.purple_text, "\n\nWhen you cook, which appliance do you primarily use?", self.text_reset)
        print("\t1. Gas stove\n\t2. Electric stove\n\t3. Microwave\n\t4. Air Fryer\n\t5. None")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # gas stove
            return temp_score + 1
        elif choice == 2:  # electric stove
            return temp_score - 2
        elif choice == 3 or choice == 4:  # microwave or air fryer
            return temp_score - 0.5
        else:  # none
            return temp_score


    """
    determines how much renewable energy sources user has to power their home
    
    :returns double representing renewable energy usage
    """

    def renewable_energy_usage(self):
        print(self.purple_text, "\n\nHow much of your home's energy is from renewable resources?", self.text_reset)
        print("\t1. Very little/none\n\t2. Less than 25%\n\t3. Less then 50%\n\t4. Less than 75%"
              "\n\t5. Less than or equal to 100%")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # none
            return self.total_score
        elif choice == 2:  # <25
            return self.total_score * 0.9
        elif choice == 3:  # <50
            return self.total_score * 0.75
        elif choice == 4:  # <75
            return self.total_score * 0.6
        else:  # <= 100
            return self.total_score * 0.40


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
