""" Krunal Patel SDEV 300 voter_registration """

def voter_registration():
    """ Voter Registration Application  """
    print("****************************************************************")
    print("Welcome to the Python Voter Registration Application.")
    while True:
        # Ask if the user wants to continue with the voter registration
        proceed = input("Do you want to continue with Voter "
                        "Registration? (Yes/No): ").strip().lower()
        if proceed == 'no':
            print("Exiting the Voter Registration Application. Goodbye!")
            return
        if proceed != 'yes':
            print("Invalid input. Please enter 'Yes' or 'No'.")
            continue

    # Get and validate the first name
        first_name = input("What is your first name?: ").strip()
        if not first_name:
            print("First name cannot be empty.")
            continue

    # Get and validate the last name
        last_name = input("What is your last name?: ").strip()
        if not last_name:
            print("Last name cannot be empty.")
            continue

    # Get and validate the age
        try:
            age = int(input("What is your age?: ").strip())
            if age < 0 or age > 120:
                print("Please enter a reasonable age between 0 and 120.")
                continue
        except ValueError:
            print("Invalid age. Please enter a number.")
            continue

    # Check age eligibility
        if age < 18:
            print("You must be at least 18 years old to register to vote.")
            continue
    # Get and validate U.S. citizenship status
        citizenship = input("Are you a U.S. Citizen? (Yes/No): ").strip().lower()
        if citizenship == 'no':
            print("Only U.S. citizens can register to vote.")
            return
        if citizenship != 'yes':
            print("Invalid input. Please enter 'Yes' or 'No'.")
            continue

    # Get and validate the state of residence
        state = input("What state do you live in?").strip().upper()
        if not state :
            print("Please enter a 2-letter abbreviation for a valid U.S. state.")
            continue

    # Get and validate the zipcode
        zipcode = input("What is your zipcode?: ").strip()
        if not zipcode:
            print(" Please enter a 5-digit zipcode.")
            continue

    # Display the summary of the registration
        print("****************************************************************")
        print("Thanks for registering to vote. Here is the information we received:")
        print(f"Name (first last): {first_name} {last_name}")
        print(f"Age: {age}")
        print(f"U.S. Citizen: {citizenship.capitalize()}")
        print(f"State: {state}")
        print(f"Zipcode: {zipcode}")
        print("Thanks for trying the Voter Registration Application."
              "Your voter registration card should be shipped within 3 weeks.")
        print("****************************************************************")
        return
# run the voter_registration method
voter_registration()
