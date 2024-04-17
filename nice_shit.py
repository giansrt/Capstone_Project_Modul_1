def is_valid_date_format(date_string):
    parts = date_string.split('/')
    if len(parts) != 3:
        print("Input the right format !!")
        return False
    
    day, month, year = parts
    if not (day.isdigit() and month.isdigit() and year.isdigit()):
        print("Dont input as a string !!")
        return False
    
    day = int(day)
    month = int(month)
    year = int(year)
    
    # Validasi bulan dan tahun
    if not (1 <= month <= 12):
        print("Input the right month !!")
        return False
    
    # Validasi hari berdasarkan bulan dan tahun (contoh sederhana)
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    elif month == 2:
        # Periksa tahun kabisat untuk Februari
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
        else:
            max_day = 28
    else:
        print("Input the right day !!")
        return False
    
    if not (1 <= day <= max_day):
        print(max_day)
        print("Input the right day 2 !!")
        return False
    
    return True
