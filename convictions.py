

## Convictions App

convictions = int(input("How many convictions do you have? "))
# same_day = Yes or No1


if convictions == 1:
    print("Proceed to the clinic to get an expunction!")
elif convictions > 1:
    same_day = input("Were your convictions on the same day of Court? (Yes/No)" )
    if same_day == "Yes":
        print("Proceed to the clinic to get an expunction!")
else:
    print("Sorry, you don't qualify")