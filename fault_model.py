import random
import datetime


MAX_INT = 2147483647
MAX_FLOAT = 1.7976931348623157e+308
MAX_STR = 1000
# complex: 1.7976931348623157e+308 + 1.7976931348623157e+308j

##### ARRAY FAULTS ######

def A_Duplicate(array): # Duplicate random elements in the array
    index = random.randint(0, len(array) - 1)
    array.insert(index + 1, array[index])
    return array

def A_RemoveOne(array): # Remove random element from the array
    index = random.randint(0, len(array) - 1)
    array.pop(index)
    return array

def A_RemoveAll(array): # Remove all elements in the array
    array.clear()
    return array

def A_RemoveAllButFirst(array): # Remove all elements in the array except the first 
    new_array = array[0]
    return new_array

##### NUMBER FAULTS ######

def N_Any_Empty(value):
    return ""

def N_Any_Null(value):
    return None

def N_Add1(number):
    number = number + 1
    return number

def N_Sub1(number):
    number = number - 1
    return number

def N_ReplacePositive(number):
    number = random.randint(1,1000)
    return number

def N_ReplaceNegative(number):
    number = random.randint(1,1000)*(-1)
    return number

def N_Replace0(number):
    number = 0
    return number

def N_Replace1(number):
    number = 1
    return number

def N_Replace_minus_1(number):
    number = -1
    return number

def N_ReplaceTypeMax(number):
    if (type(number)==int):
        number = MAX_INT
    elif (type(number)==float):
        number = MAX_FLOAT
    return number

def N_ReplaceTypeMin(number):
    if (type(number)==int):
        number = -MAX_INT
    elif (type(number)==float):
        number = -MAX_FLOAT
    return number

def N_ReplaceTypeMax_plus1(number):
    if (type(number)==int):
        number = MAX_INT + 1
    elif (type(number)==float):
        number = MAX_FLOAT + 1
    return number

def N_ReplaceTypeMin_minus1(number):
    if (type(number)==int):
        number = -MAX_INT - 1
    elif (type(number)==float):
        number = -MAX_FLOAT - 1
    return number

##### BOOLEAN FAULTS ######
def B_Any_Empty(value):
    return ""

def B_Any_Null(value):
    return None

def B_Negate(value):
    bvalue = value
    if (value == "True") or (value == "TRUE") or (value == "true"):
        bvalue = True
    elif (value == "False") or (value == "FALSE") or (value == "false"):
        bvalue = False
    bvalue = not bvalue
    return bvalue

boolean_faults = {
    "B_Negate": B_Negate
}

##### STRING FAULTS #####

def S_Any_Empty(value):
    return ""

def S_Any_Null(value):
    return None

def S_AppendPrintable(text):
    random_number = random.randint(32, 127)
    text += chr(random_number)*MAX_STR
    return text #É NECESSÁRIO ADICIONAR CARACTERES ATÉ OVERFLOW?
    
def S_ReplacePrintable(text):
    random_index = random.randint(0, len(text))
    random_number = random.randint(32, 127)
    random_character = chr(random_number)
    text = text[:random_index] + random_character + text[random_index + 1:]
    return text #É NECESSÁRIO SUBSTITUIR TODOS OS CARACTERES DA STRING?

def S_ReplaceAlphanumeric(text):
    alphanumeric_characters=[]
    for i in range(48, 58):
        alphanumeric_characters.append(chr(i))
    for i in range(65, 91):
        alphanumeric_characters.append(chr(i))
    for i in range(97, 123):
        alphanumeric_characters.append(chr(i))
    new_string = ""
    for character in text:
        new_character = random.choice(alphanumeric_characters)
        new_string += new_character
    return new_string

def S_AppendNonPrintable(text):
    random_number = random.randint(0, 31)
    # print(chr(random_number).isprintable())
    text += chr(random_number)
    return text

def S_InsertNonPrintable(text):
    random_index = random.randint(0, len(text))
    non_printable_character = chr(random.randint(0, 31))
    text = text[:random_index] + non_printable_character + text[random_index + 1:]
    return text

def S_ReplaceNonPrintable(text):
    non_printable_characters=[]
    for i in range(0, 31):
        non_printable_characters.append(chr(i))
    new_string = ""
    for character in text:
        new_character = random.choice(non_printable_characters)
        new_string += new_character
    return new_string

def S_Malicious(text):
    sql_injection_code = "' OR 1=1"
    text += sql_injection_code
    return text

# def Byte_Duplicate(text): IT DEPENDS OF THE DOMAIN. 
#     return text

# def By_Swap(text):
#     return text

##### DATE FAULTS #####

def D_Any_Empty(value):
    return ""

def D_Any_Null(value):
    return None

def D_Add100Years(text):
    date = datetime.datetime.strptime(text, "%d/%m/%Y")
    new_date = date + datetime.timedelta(days=365.25 * 100)
    text = new_date.strftime("%d/%m/%Y")
    return text

def D_Sub100Years(text):
    date = datetime.datetime.strptime(text, "%d/%m/%Y")
    if (date.year > 100):
        new_date = date - datetime.timedelta(days=365.25 * 100 - 1)
        text = new_date.strftime("%d/%m/%Y")
    return text

def D_LastDayPreviousMil(text): #Replace with last day of the previous millennium
    date = datetime.datetime.strptime(text, "%d/%m/%Y")
    year = date.year - 1000
    if (year > 0):
        text = "31/12/{:04d}".format(year)
    return text

def D_FirstDayCurrentMil(text): #Replace with first day of the current millennium
    date = datetime.datetime.strptime(text, "%d/%m/%Y")
    year = "{:04d}".format(date.year)
    year = year[0]+"000"
    if (int(year) > 0):
        text = "01/01/{}".format(year)
    else:
        text = "01/01/0000"
    return text
    
def D_Replace1985_2_29(text): #Replace with invalid date 1985-2-29
    text = "29/02/1985"
    return text

def D_Replace1998_4_31(text): #Replace with invalid date 1998-4-31
    text = "31/04/1998"
    return text

def D_Replace1997_13_1(text): #Replace with invalid date 1997-13-01
    text = "01/13/1997"
    return text

def D_Replace1994_12_0(text): #Replace with invalid date 1994-12-0
    text = "00/12/1994"
    return text

def D_Replace1993_8_32(text): #Replace with invalid date 1993-8-32
    text = "32/08/1993"
    return text

##### DATETIME FAULTS #####

def T_Any_Empty(value):
    return ""

def T_Any_Null(value):
    return None

def T_Add100Years(text):
    date = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    new_date = date + datetime.timedelta(days=365.25 * 100)
    text = new_date.strftime("%d/%m/%Y %H:%M:%S")
    return text

def T_Sub100Years(text):
    date = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    if (date.year > 100):
        new_date = date - datetime.timedelta(days=365.25 * 100 - 1)
        text = new_date.strftime("%d/%m/%Y %H:%M:%S")
    return text

def T_LastDayPreviousMil(text): #Replace with last day of the previous millennium
    date = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    hour = date.hour
    minute = date.minute
    second = date.second
    year = date.year - 1000
    if (year > 0):
        text = "31/12/{:04d} {}:{}:{:02d}".format(year, hour, minute, second)
    return text

def T_FirstDayCurrentMil(text): #Replace with first day of the current millennium
    date = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    year = "{:04d}".format(date.year)
    year = year[0]+"000"
    if (int(year) > 0):
        text = "01/01/{} 00:00:00".format(year)
    else:
        text = "01/01/0000 00:00:00"
    return text
    
def T_Replace1985_2_29(text): #Replace with invalid date 1985-2-29
    text = "29/02/1985 00:00:00"
    return text

def T_Replace1998_4_31(text): #Replace with invalid date 1998-4-31
    text = "31/04/1998 00:00:00"
    return text

def T_Replace1997_13_1(text): #Replace with invalid date 1997-13-01
    text = "01/13/1997 00:00:00"
    return text

def T_Replace1994_12_0(text): #Replace with invalid date 1994-12-0
    text = "00/12/1994 00:00:00"
    return text

def T_Replace1993_8_32(text): #Replace with invalid date 1993-8-32
    text = "32/08/1993 00:00:00"
    return text

def T_Add24Hours(text): #Add 24 hours to the time
    date_time = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    hour = date_time.hour + 24
    minute = date_time.minute
    second = date_time.second
    day = date_time.day
    month = date_time.month
    year = date_time.year
    text = "{}/{}/{} {}:{}:{}".format(day, month, year, hour, minute, second)
    return text

def T_Sub24Hours(text): #Subtract 24 hours from the time
    date_time = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    hour = date_time.hour - 24
    minute = date_time.minute
    second = date_time.second
    day = date_time.day
    month = date_time.month
    year = date_time.year
    text = "{}/{}/{} {}:{}:{}".format(day, month, year, hour, minute, second)
    return text

def T_Replace13_00_61(text): #Replace with invalid time 13:00:61
    date_time = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    day = date_time.day
    month = date_time.month
    year = date_time.year
    text = "{}/{}/{} 13:00:61".format(day, month, year)
    return text

def T_Replace10_73_02(text): #Replace with invalid time 10:73:02
    date_time = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    day = date_time.day
    month = date_time.month
    year = date_time.year
    text = "{}/{}/{} 10:73:02".format(day, month, year)
    return text

def T_Replace25_28_04(text): #Replace with invalid time 25:28:04
    date_time = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    day = date_time.day
    month = date_time.month
    year = date_time.year
    text = "{}/{}/{} 25:28:04".format(day, month, year)
    return text

def T_Replace04_03_60(text): #Replace with invalid time 04:03:60
    date_time = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    day = date_time.day
    month = date_time.month
    year = date_time.year
    text = "{}/{}/{} 04:03:60".format(day, month, year)
    return text

def T_Replace07_60_15(text): #Replace with invalid time 07:60:15
    date_time = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    day = date_time.day
    month = date_time.month
    year = date_time.year
    text = "{}/{}/{} 07:60:15".format(day, month, year)
    return text

def T_Replace24_05_01(text): #Replace with invalid time 24:05:01
    date_time = datetime.datetime.strptime(text, "%d/%m/%Y %H:%M:%S")
    day = date_time.day
    month = date_time.month
    year = date_time.year
    text = "{}/{}/{} 24:05:01".format(day, month, year)
    return text

array_faults = {
    "A_Duplicate": A_Duplicate, 
    "A_RemoveOne": A_RemoveOne, 
    "A_RemoveAll": A_RemoveAll, 
    "A_RemoveAllButFirst": A_RemoveAllButFirst,
}

number_faults = {
    "N_Any_Empty": N_Any_Empty,
    "N_Any_Null": N_Any_Null,
    "N_Add1": N_Add1,
    "N_Sub1": N_Sub1,
    "N_ReplacePositive": N_ReplacePositive,
    "N_ReplaceNegative": N_ReplaceNegative,
    "N_Replace0": N_Replace0,
    "N_Replace1": N_Replace1,
    "N_Replace-1": N_Replace_minus_1,
    "N_ReplaceTypeMax": N_ReplaceTypeMax,
    "N_ReplaceTypeMin": N_ReplaceTypeMin,
    "N_ReplaceTypeMax+1": N_ReplaceTypeMax_plus1,
    "N_ReplaceTypeMin-1": N_ReplaceTypeMin_minus1   
}
    
string_faults = {
    "S_Any_Empty": S_Any_Empty,
    "S_Any_Null": S_Any_Null,
    "S_AppendPrintable": S_AppendPrintable,
    "S_ReplacePrintable": S_ReplacePrintable,
    "S_ReplaceAlphanumeric": S_ReplaceAlphanumeric,
    "S_AppendNonPrintable": S_AppendNonPrintable,
    "S_InsertNonPrintable": S_InsertNonPrintable,
    "S_ReplaceNonPrintable": S_ReplaceNonPrintable,
    "S_Malicious": S_Malicious,
}

date_faults = {
    "D_Any_Empty": D_Any_Empty,
    "D_Any_Null": D_Any_Null,
    "D_Add100Years": D_Add100Years,
    "D_Sub100Years": D_Sub100Years,
    "D_LastDayPreviousMil": D_LastDayPreviousMil,
    "D_FirstDayCurrentMil": D_FirstDayCurrentMil,
    "D_Replace1985-2-29": D_Replace1985_2_29,
    "D_Replace1998-4-31": D_Replace1998_4_31,
    "D_Replace1997-13-1": D_Replace1997_13_1,
    "D_Replace1994-12-0": D_Replace1994_12_0,
    "D_Replace1993-8-32": D_Replace1993_8_32,
}

datetime_faults = {
    "T_Any_Empty": T_Any_Empty,
    "T_Any_Null": T_Any_Null,
    "T_Add100Years": T_Add100Years,
    "T_Sub100Years": T_Sub100Years,
    "T_LastDayPreviousMil": T_LastDayPreviousMil,
    "T_FirstDayCurrentMil": T_FirstDayCurrentMil,
    "T_Replace1985-2-29": T_Replace1985_2_29,
    "T_Replace1998-4-31": T_Replace1998_4_31,
    "T_Replace1997-13-1": T_Replace1997_13_1,
    "T_Replace1994-12-0": T_Replace1994_12_0,
    "T_Replace1993-8-32": T_Replace1993_8_32,
    "T_Add24Hours": T_Add24Hours,
    "T_Sub24Hours": T_Sub24Hours,
    "T_Replace13_00_61": T_Replace13_00_61,
    "T_Replace10_73_02": T_Replace10_73_02,
    "T_Replace25_28_04": T_Replace25_28_04,
    "T_Replace04_03_60": T_Replace04_03_60,
    "T_Replace07_60_15": T_Replace07_60_15,
    "T_Replace24_05_01": T_Replace24_05_01   
}

