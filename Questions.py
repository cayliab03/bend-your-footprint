import Transportation
import Food
import Energy
import Shopping


class Questions:

    """
    This class contain the quiz's introduction and results, score calculations, and calls each question
    """


    """
    :var weakest_element              string of element (category) which the user scored the worst in
    :var weakest_ele_score            double score of the user's weakest element
    :var total_green_score            double of sum of user's scores from 4 elements (categories)
    :var yellow_text                  ASNI colour code for yellow   
    :var text_reset                   ANSI colour code for white             
    """

    def __init__(self):
        self.weakest_element = ""
        self.weakest_ele_score = 0
        self.total_green_score = 0
        self.yellow_text = "\033[0;49;93m"
        self.text_reset = "\033[0;49;38m"


    """
    runs quiz; displays introduction and conclusion, call questions and loads scores into dictionary to be used for 
    final result calculation
    """

    def start_quiz(self):
        self.introduction()
        score_dict = self.all_questions()
        self.element_score_calculator(score_dict)
        self.results()


    """
    displays introduction and instructions to user
    """

    def introduction(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\nThis is the Bend Your Footprint sustainability quiz!")
        print("\nThis program will ask a series of questions and you will pick the answer that best applies to you.")
        print("\nAt the end, the program will calculate your sustainability score and which are you are weakest in.")
        print("\nLet's begin!!\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


    """
    call questions of classes Transportation, Energy, Shopping, and Food and stores results into a dictionary
    the keys of the dictionary are the elements (air represents transportation questions, earth with energy, fire with
    shopping, water with food) and its associated values are the results of each Class
    
    :return dictionary with element and associated score
    """

    def all_questions(self):
        earth_score = Energy.Energy().call_energy_questions()
        air_score = Transportation.Transportation().call_transport_questions()
        fire_score = Shopping.Shopping().call_shopping_questions()
        water_score = Food.Food().call_food_questions()

        # total = 125.75
        scores = {"AIR": air_score, "EARTH": earth_score, "FIRE": fire_score, "WATER": water_score}

        return scores


    """
    calculates user's total score across 4 categories and identifies their weakest area (and its associated score
    """

    def element_score_calculator(self, score_dict):

        for x in score_dict:
            self.total_green_score += score_dict[x]

            if self.weakest_ele_score < score_dict[x]:
                self.weakest_ele_score = score_dict[x]
                self.weakest_element = x


    """
    calculates sustainability percentage and prints messages based on result
    
    for calculation, first calculates how many points they had (as a percentage of the max points possible). worse 
    sustainable answers leads to higher percentages at this step
    then, subtracts that percentage from 100 (%). the higher the score, the lower their sustainability percentage is    
    """

    def green_percentage_calculator(self):
        green_percent = round(100 - (self.total_green_score / 125.75) * 100, 2)

        print("Your total sustainability percentage is...")
        print(self.yellow_text, green_percent, "% !!", self.text_reset)

        if green_percent < 20:
            print("It looks like we have a long and fun path ahead of us !")
        elif green_percent < 40:
            print("We're off to a good start !")
        elif green_percent < 60:
            print("Awesome progress ! Keep up the good work !")
        elif green_percent < 80:
            print("Amazing ! Looks like your hard work is starting to pay off !")
        else:
            print("Incredible job ! It must feel great to make such a hugh impact !")


    """
    displays user's results
    """

    def results(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("\n~~End of quiz~~\n")
        self.green_percentage_calculator()
        print("\nYour weakest element is....")
        print(self.yellow_text, self.weakest_element, self.text_reset)
        print("\nPlease head to our website at "
              "https://bendyourfootprint.website/ "
              "to what this means and more sustainable strategies to increase your "
              "score and help care for the planet.\n")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
