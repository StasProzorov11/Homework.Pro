    
# 1. Користувач вводить із клавіатури номер дня тижня (1-7).
# Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1,
# на екрані напис понеділок, 2 — вівторок тощо.


try:

    day_of_the_week = int ( input ( "Enter day from 1 to 7  :  " ) )

    if day_of_the_week == 1:
        print ( "Monday" )

    elif day_of_the_week == 2:
        print ( "Tuesday" )

    elif day_of_the_week == 3:
        print ( "Wednesday" )

    elif day_of_the_week == 4:
        print ( "Thursday" )

    elif day_of_the_week == 5:
        print ( "Friday" )

    elif day_of_the_week == 6:
        print ( "Saturday" )

    elif day_of_the_week == 7:
        print ( "Sunday" )

    else:
        print ( "Not a good day, try again!" )

except ValueError:
 print ("It's not a number, try again!")

except Exception as error:
 print ( f"Error occurred: {error}" )