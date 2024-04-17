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
    
    if not (1 <= day <= 31):
        print("Input the right day  !!")
        return False
    
    return True

if not is_valid_date_format(date_start) or not is_valid_date_format(date_end):
    print("Invalid input date. Please enter the date in the format dd/mm/yyyy correctly !!!")
    # Lakukan tindakan lanjutan jika input tanggal tidak valid
    continue
else:
    day, month, year = map(int, date_start.split('/'))
    day_end, month_end, year_end = map(int, date_end.split('/'))