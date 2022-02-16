#
import time
from time import sleep
txts = "\033[1m"
txte = "\033[0;0m"
print(txts + "On the Subject of Memory" + txte)
sleep(1)
print("Version: 1")
print("Verification Code: 241")
sleep(1)
print(txts + "\nStep 1" + txte)
di = int(input("1-Display: "))
if di == 1:
    print("Press the button in the 2 position")
elif di == 2:
    print("Press the button in the 2 position")
elif di == 3:
    print("Press the button in the 3 position")
elif di == 4:
    print("Press the button in the 4 position")
else:
    print("Invalid input")
    quit()
ni = int(input("1-Number: "))
pi = int(input("1-Position: "))

print(txts + "\nStep 2" + txte)
dii = int(input("2-Display: "))
if dii == 1:
    print("Press the button with the number '4'")
elif dii == 2:
    print(f"Press the button in the {pi} position")
elif dii == 3:
    print("Press the button in the 1 position")
elif dii == 4:
    print(f"Press the button in the {pi} position")
else:
    print("Invalid input")
    quit()
nii = int(input("2-Number: "))
pii = int(input("2-Position: "))

print(txts + "\nStep 3" + txte)
diii = int(input("3-Display: "))
if diii == 1:
    print(f"Press the button with the number '{nii}'")
elif diii == 2:
    print(f"Press the button with the number '{ni}'")
elif diii == 3:
    print("Press the button in the 3 position")
elif diii == 4:
    print("Press the button with the number '4'")
else:
    print("Invalid input")
    quit()
niii = int(input("3-Number: "))
piii = int(input("3-Position: "))

print(txts + "\nStep 4" + txte)
div = int(input("4-Display: "))
if div == 1:
    print(f"Press the button in the {pi} position")
elif div == 2:
    print("Press the button in the 1 position")
elif div == 3:
    print(f"Press the button in the {pii} position")
elif div == 4:
    print(f"Press the button in the {pii} positions")
else:
    print("Invalid input")
    quit()
niv = int(input("4-Number: "))
piv = int(input("4-Position: "))

print(txts + "\nStep 5" + txte)
dv = int(input("5-Display: "))
if dv == 1:
    print(f"Press the button with the number {ni}")
elif dv ==2:
    print(f"Press the button with the number {nii}")
elif dv == 3:
    print(f"Press the button with the number {niv}")
elif dv == 4:
    print(f"Press the button with the number {niii}")
else:
    print("Invalid input")
    quit()
sleep(2.25)
print(txts + "Congratulations! You made it!" + txte)
print("Exiting the program...")
sleep(2)
quit()
