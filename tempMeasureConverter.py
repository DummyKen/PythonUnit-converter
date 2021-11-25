# A program to convert some measurement units including temperatures(F/C)
import time
print('''Welcome to my unit converter:
Here you can convert many units including Farenheit,Celsius,meters,inch,etc
-----------------------------------------------------------------------
Instructions:
1/Enter your input
2/Enter your input's category(weight,length,temperature)
3/Enter your input's unit:
(Available Conversions:
    Weight: (k)g to (l)bs/(l)bs to (k)g
            
    Length: (i)nch to (m)eter/(m)eter to (i)nch
            (i)nch to (f)eet/(f)eet to (i)nch
    
    Temperature:    (C)elsius to Kel(v)in/Kel(v)in to (C)elsius
                    (C)elsius to (F)arenheit/(F)arenheit to (C)elsius
            
~~Have fun converting stuff!~~
            ''')

#empty string to put the choice when converting 
choice = ''
#input
try:
    number = int(input("Enter your number to be converted.\n(You will get humiliated if you enter an unacceptable input. Take care :):"))
    print('Acceptable Input!')
    unit = input('''Enter your unit
    Available Units:
    Weight: (k)ilogram,(l)bs
    Length: (i)nch, (m)eter, (f)eet
    Temperature: (C)elsius, Kel(v)in, (F)arenheit
    
    ----Characters inside ( ) are the unit keywords----: :''')
    if unit().lower() == 'k':
        print('You asked to convert the number form kilogram to lbs:The only possible conversion!')
        print('Converting.......')
        time.sleep(2)
        print("The number in lbs:", lbs)
    elif unit().lower() == 'l':
        print('You asked to convert the number form lbs to kilogram:The only possible conversion!')
        print('Converting.......')
        time.sleep(2)
        print("The number in kilo:", kilo)
    elif unit().lower() == 'i':
        choice = input('To which do you want to convert--(m)eter or (f)eet--:')
            if choice == 'm':
                print('Converting to meter')
                time.sleep(2)
                print('The number in meters:', meters)
            elif choice == 'f':
                print('Converting to feet....')
                time.sleep(2)
                print('The number in feet:', feet)
    elif unit().lower() == 'm':
        blah blah
    
