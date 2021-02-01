name = input("Please enter your name: ")
number = int(input("Please enter a number: "))
print(name)
print(number)
is_fizz = ("is a Fizz number.")
is_buzz = ("is a Buzz number.")
is_fizz_buzz = ("is a FizzBuzz number.")

if number % 3==0 and number % 5 ==0:
  print(is_fizz_buzz)
elif number % 3==0:
  print(is_fizz)
elif number % 5 == 0:
  print(is_buzz)
else:
  print("is neither a fizzy or a buzzy number.")