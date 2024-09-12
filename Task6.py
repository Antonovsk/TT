a = int(input ("Введите шестизначный номер билета: "))

# Преобразование числа в строку
digits = str(a)

if int(digits[0]) + int(digits[1]) + int(digits[2]) == int(digits[3]) + int(digits[4]) + int(digits[5]):
    print("Билет счастливый")
    
else:
    print("Билет не счастливый")
    
