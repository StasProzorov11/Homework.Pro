# 2. Користувач вводить два числа.
# Визначити, чи рівні ці числа, і, якщо ні,
# вивести їх на екран у порядку зростання
try :
 first_number = int(input("Enter first number : "))
 second_number = int(input("Enter second number : "))

 if first_number > second_number :

  print(f"second_number : {second_number} < first_number : {first_number}")

 elif first_number < second_number :

  print(f"first_number : {first_number} < second_number : {second_number}")

 else :

  print(f"first_number : {first_number} = second_number : {second_number}")


except ValueError:
 print ("It's not a number, try again!")

except Exception as error:
 print ( f"Error occurred: {error}" )