import Questions


if __name__ == '__main__':
    print("\033[0;49;31m AAAAAAAAAAAAAAAA\t\033[0;49;91m AAAAAAAAAAAAAAAA\n"
          "\033[0;49;32m AAAAAAAAAAAAAAAA\t\033[0;49;92m AAAAAAAAAAAAAAAA\n"
          "\033[0;49;33m AAAAAAAAAAAAAAAA\t\033[0;49;93m AAAAAAAAAAAAAAAA\n"
          "\033[0;49;34m AAAAAAAAAAAAAAAA\t\033[0;49;94m AAAAAAAAAAAAAAAA\n"
          "\033[0;49;35m AAAAAAAAAAAAAAAA\t\033[0;49;95m AAAAAAAAAAAAAAAA\n"
          "\033[0;49;36m AAAAAAAAAAAAAAAA\t\033[0;49;96m AAAAAAAAAAAAAAAA\n"
          "\033[0;49;37m AAAAAAAAAAAAAAAA\t\033[0;49;97m AAAAAAAAAAAAAAAA\n"
          "\033[0;49;38m AAAAAAAAAAAAAAAA\t\033[0;49;98m AAAAAAAAAAAAAAAA\n")


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
