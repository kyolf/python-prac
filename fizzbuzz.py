import sys

my_input = 0;

def fizzbuzz(num):
  for i in range(0,num +1):
    if i % 5 == 0 and i % 3 == 0:
      print('FizzBuzz')
    elif i % 5 == 0:
      print('Buzz')
    elif i % 3 == 0:
      print('Fizz')
    else:
      print(i)

if len(sys.argv) == 0:
  my_input = int(input('ENTER A NUMBER!: '))
  print(type(my_input))
  fizzbuzz(my_input)
else:
  fizzbuzz(int(sys.argv[1]))