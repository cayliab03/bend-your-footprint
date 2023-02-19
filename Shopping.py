class Shopping:

    """
    This class contains all questions related to transportation and calculates a score based on user inputs
    """

    def __init__(self):
        self.total_score = 0
        self.purple_text = "\033[0;49;35m"
        self.green_text = "\033[0;49;32m"
        self.text_reset = "\033[0;49;38m"


    """
    calls call questions related to shopping in Shopping class

    :return double representing final shopping score
    """

    def call_shopping_questions(self):
        self.total_score += self.trash_count()
        self.total_score += self.recycle_count()
        self.total_score += self.purchasing_new_clothing()
        self.total_score += self.store_purchasing()
        self.total_score += self.rent_clothing()
        self.total_score += self.repair_items()
        self.total_score += self.throw_away_items()
        return self.total_score


    """
    determines amount of trash user throws away each week
    
    :return int representing trash score    
    """

    def trash_count(self):
        print(self.purple_text, "\n\nHow often do throw out a garbage bags every week?", self.text_reset)
        print("\t1. Once a week \n\t2. 2 times a week \n\t3. 3 times a week \n\t4. 4 times a week"
              "\n\t5. 5 or more times a week ")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # 1 time
            return 1
        elif choice == 2:  # 2 times
            return 2
        elif choice == 3:  # 3 times
            return 3
        elif choice == 4:  # 4 times
            return 4
        else:
            return 5  # 5 times


    """
    determines how often user recycles
    
    :return int representing user's recycling score
    """

    def recycle_count(self):
        print(self.purple_text, "\n\nHow often do you recycle items?", self.text_reset)
        print("\t1. Regularly \n\t2. Most of the time \n\t3. Sometimes \n\t4. Rarely "
              "\n\t5. Almost never ")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # regularly
            return 0.5
        elif choice == 2:  # mostly
            return 1.5
        elif choice == 3:  # sometimes
            return 2.5
        elif choice == 4:  # rarely
            return 3.5
        else:
            return 4.5  # never


    """
    determines how often user buys clothing
    
    :return int representing user's clothing shopping score 
    """

    def purchasing_new_clothing(self):
        print(self.purple_text, "\n\nHow often do you purchase new clothing?", self.text_reset)
        print("\t1. Every week \n\t2. Every 2 weeks or so \n\t3. Every month \n\t4. Every few months"
              "\n\t5. Few times a year")
        choice = self.check_user_input(1, 6)

        if choice == 1:  # every week
            return 1
        elif choice == 2:  # 2 weeks
            return 2
        elif choice == 3:  # monthly
            return 3
        elif choice == 4:  # few months
            return 4
        else:  # year
            return 5


    """
    determines where user primarily purchases clothing
    
    :return int representing user's clothing store score
    """

    def store_purchasing(self):
        print(self.purple_text, "\n\nWhere to you get new clothes primarily?", self.text_reset)
        print("\t1. Upcycling existing clothes and/or secondhand stores \n\t2. Fast-fashion brands (online & in-person)"
              "\n\t3. Sustainable brands")
        choice = self.check_user_input(1, 4)
        if choice == 1:  # secondhand
            return -4
        elif choice == 2:  # fast-fashion
            return 4
        else:  # sustainable
            return 1


    """
    determines if user rents clothing pieces or not
    
    :return int representing if user rents clothing
    """

    def rent_clothing(self):
        print(self.purple_text, "\n\nDo you rent clothing (fancy dresses, tuxedos, etc", self.text_reset)
        print("\t1. Yes\n\t2. No")
        choice = self.check_user_input(1, 3)

        if choice == 1:  # yes
            return -2
        else:  # no
            return 0


    """
    determines how frequently user's repairs items
    
    :return int representing user's item repair score
    """

    def repair_items(self):
        print(self.purple_text, "\n\nHow often do you repair items?", self.text_reset)
        print("\t1. Whenever possible\n\t2. Occasionally\n\t3. Rarely\n\t4. Never")
        choice = self.check_user_input(1, 5)

        if choice == 1:  # whenever possible
            return -5
        elif choice == 2:  # occasionally
            return -2
        elif choice == 2:  # rarely
            return 2
        else:  # never
            return 4


    """
    determines how user gets rid of unwanted, but functional items like clothing
    
    :return int representing how user disposes of items
    """

    def throw_away_items(self):
        print(self.purple_text, "\n\nHow do you get rid of (non-trash, relatively functional) items? "
              "For example, furniture and clothing", self.text_reset)
        print("\t1. Selling and/or donating\n\t2. Garbage or recycle")

        choice = self.check_user_input(1, 3)

        if choice == 1:  # selling
            return -5
        else:
            return 4  # garbage


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
