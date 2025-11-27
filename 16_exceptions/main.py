## Exception = An Event that interrupts the flow of a program.

## Ex. ZeroDivisionError, ValueError, TypeError

## try.. catch... finally...


try:
    number = int(input("Enter a number:"))
    print(1/number)

except ZeroDivisionError:
    print("You cannot divide by zero IDIOT!")
except ValueError:
    print("Enter only Numbers please!")
except Exception:
    print("Something went wrong!")
finally:
    print("Do some cleanup here")