import Questions


if __name__ == '__main__':
    in_quiz = True  # while var is true, will loop through quiz questions

    while in_quiz:  # while quiz is active
        curr_quiz = Questions.Questions().start_quiz()  # starts quiz

        print("Try quiz again?")
        print("Yes (Y) or No (N)")

        while True:  # checks if user wants to play quiz again
            try:  # ensures valid input
                choice = input()

                if choice.upper() == "Y":
                    continue
                elif choice.upper() == "N":
                    in_quiz = False
                    break
                else:
                    print("Enter a valid choice: ")

            except ValueError:
                print("Enter a valid choice: ")

    print("Thank you for taking the Bend Your Footprint Quiz !!")
