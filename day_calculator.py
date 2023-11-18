month_days={"january":31,"february":29,"march":31,"april":30,"may":31,"june":30,"july":31,"august":31,"september":30,"october":31,"november":30,"december":31}
month_num={"january":1,"february":2,"march":3,"april":4,"may":5,"june":6,"july":7,"august":8,"september":9,"october":10,"november":11,"december":12}
list_days=[31,29,31,30,31,30,31,31,30,31,30,31]
print("this program calculates the days which passed between two given dates")
count=1
total_days_new=0
total_days_older=0

year_older=int(input("enter the older year: "))
year_new=int(input("enter the more new year: "))
if year_older>year_new or year_new<=0 or year_older<=0:
    print("wrong years!")
else:
    day_older=int(input("enter the older day: "))


    day_new=int(input("enter the more new day: "))
    if 0<=day_new<=31 and 0<=day_older<=31:
        month_older=input("enter the older month: ")
        month_new=input("enterthe more new month: ")
        print(f"your older date is: {month_older} {day_older},{year_older}.")
        print(f"your newer date is: {month_new} {day_new},{year_new}.")

        for i in list_days:
            if month_num.get(month_new)==count:
                break
            count+=1
            total_days_new+=i 
        count=1    
        for i in list_days:
            if month_num.get(month_older)==count:
                break
            count+=1
            total_days_older+=i    




        days_passed_new=total_days_new+day_new
        days_passed_older=total_days_older+day_older


        if days_passed_new>=days_passed_older:


          days_passed=((year_new-year_older)*366)-(days_passed_older-days_passed_new)
          print(days_passed_new,days_passed_older)
          print(f"{days_passed} days are passed between the given dates")
        else:
          days_passed=((year_new-year_older)*366)-(days_passed_new-days_passed_older)
          print(f"{days_passed} days are passed between the given dates")






    else:
        print("wrong day!")    