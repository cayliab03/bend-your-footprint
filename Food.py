class Food:
    """
    This class contains all questions related to food and calculates a score based on user inputs
    """

    def __init__(self):
        self.total_score = 0
        self.diet = ""
        self.purple_text = "\033[0;49;35m"
        self.green_text = "\033[0;49;32m"
        self.text_reset = "\033[0;49;38m"


    """
    calls call questions related to food in Food class

    :return double representing final food score
    """

    def call_food_questions(self):
        self.total_score += self.diet_category()
        self.total_score += self.fast_food_frequency()
        self.total_score -= self.has_personal_garden()
        return self.total_score


    """
    determines user's diet category and sets variable diet to user choice

    :return the user's primary transport score multiplied with a constant
    """

    def diet_category(self):
        print(self.purple_text, "\n\nWhat best describes your diet?", self.text_reset)
        print("\t1. Vegan \n\t2. Vegetarian \n\t3. Pescetarian \n\t4. Meat-lover")
        choice = self.check_user_input(1, 5)  # ensures user inputted valid int within given options

        if choice == 1:  # vegan
            self.diet = "vegan"
            return 2 + self.fresh_foods_consumption()
        elif choice == 2:  # vegetarian
            self.diet = "vegetarian"
            return 3 + self.fresh_foods_consumption()
        elif choice == 3:  # pescetarian
            self.diet = "pescetarian"
            return self.meat_consumption_frequency(4) + self.fresh_foods_consumption()
        elif choice == 4:  # meat-lover
            self.diet = "meat-lover"
            return self.meat_consumption_frequency(5) + self.fresh_foods_consumption()


    """
    determines user's meat consumption per week and passes on the current score to the red_meat_consumption method
    otherwise it returns the current score with an added value based on their input.

    :param temp_score 

    :return the user's food score multiplied by a constant
    """

    def meat_consumption_frequency(self, temp_score):
        print(self.purple_text, "\n\nHow often do you eat meat?", self.text_reset)
        print("\t1. 1-2 times a week \n\t2. 3-5 times a week \n\t3. Daily \n\t4. Multiple times a day")
        choice = self.check_user_input(1, 5)

        if choice == 1:  # 1-2 times a week
            return temp_score + 2 if self.diet_category == "pescetarian" else self.red_meat_consumption(temp_score + 2)
        elif choice == 2:  # 3-5 times a week
            return temp_score + 3 if self.diet_category == "pescetarian" else self.red_meat_consumption(temp_score + 3)
        elif choice == 3:  # daily
            return temp_score + 4 if self.diet_category == "pescetarian" else self.red_meat_consumption(temp_score + 4)
        elif choice == 4:  # multiple times a day
            return temp_score + 5 if self.diet_category == "pescetarian" else self.red_meat_consumption(temp_score + 5)


    """
    determines user's red meat consumption per week and returns the current score with an added value based on input.

    :param temp_score 

    :return the user's food score multiplied by a constant
    """

    def red_meat_consumption(self, temp_score):
        print(self.purple_text, "\n\nHow often do you eat red meat?", self.text_reset)
        print("\t1. Never \n\t2. 1-2 times a week \n\t3. 3-5 times day \n\t4. Every day \n\t5. Multiple times a day")
        choice = self.check_user_input(1, 6)
        if choice == 0:  # never
            return temp_score
        elif choice == 1:  # 1-2 times a week
            return temp_score * 1.2
        elif choice == 2:  # 3-5 times day
            return temp_score * 1.4
        elif choice == 3:  # every day
            return temp_score * 1.6
        else:  # multiple times a day
            return temp_score * 2


    """
    determines user's fresh food consumption per week and returns the current score with an added value based on input.

    :param temp_score 

    :return the user's food score multiplied by a constant
    """

    def fresh_foods_consumption(self):
        print(self.purple_text, "\n\nHow often do you eat fresh foods in your meals?", self.text_reset)
        print("\t1. Most meals \n\t2. A meal every day \n\t3. Few meals a week \n\t4. 1-2 meals a week "
              "\n\t5. Almost never")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # most meals
            return 1
        elif choice == 2:  # a meal every day
            return 1.5
        elif choice == 3:  # a few meals a week
            return 2
        elif choice == 4:  # 1-2 meals a week
            return 4
        else:  # almost never
            return 5


    """
    determines user's fast food consumption per week and returns the current score with an added value based on input
    
    :return the user's food score multiplied by a constant
    """

    def fast_food_frequency(self):
        print(self.purple_text, "\n\nHow often do you eat take-out?", self.text_reset)
        print("\t1. Almost never \n\t2. 1-2 times a week \n\t3. 3-5 times a week \n\t4. Everyday "
              "\n\t5. Multiple times a day")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # almost never
            return 0
        elif choice == 2:  # 1-2 times a week
            return 0.5
        elif choice == 3:  # 3-5 times a week
            return 1.5
        elif choice == 4:  # everyday
            return 2.5
        else:  # multiple times a day
            return 3


    """
    determines if a user grows fresh produce in their garden and returns the current score with an added value based on 
    their input

    :return the user's food score multiplied by a constant
    """

    def has_personal_garden(self):
        print(self.purple_text, "\n\nDo you grow food at home?", self.text_reset)
        print("\t1. No\n\t2. Yes")
        choice = self.check_user_input(1, 3)

        if choice == 1:  # no
            return 0
        else:
            return self.size_of_garden()  # yes


    """
    determines how large a user's personal garden is and returns the current score with an added value based on input.

    :return the user's food score multiplied by a constant
    """

    def size_of_garden(self):
        print(self.purple_text, "\n\nHow often do you eat take-out?", self.text_reset)
        print("\t1. Few plants around the house \n\t2. Small \n\t3. Medium-sized \n\t4. Sizeably large "
              "\n\t5. Very large")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # few plants around the house
            temp_score = 0.5
        elif choice == 2:  # small
            temp_score = 1.5
        elif choice == 3:  # medium-sized
            temp_score = 2.5
        elif choice == 4:  # sizeably large
            temp_score = 3
        else:
            temp_score = 4  # very large

        self.grows_food_at_home(temp_score)


    """
    determines how much the user grows fresh produce in their garden and returns the current score with an added value 
    based on their input.

    :return the user's food score multiplied by a constant
    """

    def grows_food_at_home(self, temp_score):
        print(self.purple_text, "\n\nDo you grow food at your home?", self.text_reset)
        print("\t1. Grows very little/no food \n\t2. Grows some food at home \n\t3. Grows sizeable amount of food "
              "\n\t4. Grows sizeable amount of food \n\t5. Grows most/all food")
        choice = self.check_user_input(1, 6)
        if choice == 1:  # grows very little / no food
            return temp_score
        elif choice == 2:  # grows some food at home
            return 1.5 * temp_score
        elif choice == 3:  # grows sizeable amount of food
            return 2.5 * temp_score
        else:  # grows most-to-all food
            return 5 * temp_score


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
