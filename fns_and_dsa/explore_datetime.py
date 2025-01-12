from datetime import datetime, timedelta 

def display_current_datetime():
    #current_date = datetime.now().date()
    current_date_time = datetime.now()

    formatted_date = current_date_time.strftime('%Y-%m-%d %H:%M:%S')

    print("Current Date and Time: ",formatted_date)

display_current_datetime()


number_of_days = int(input("Enter the number of dates to add to the current date: "))

def calculate_future_date():
   #display_current_datetime()
   current_date = datetime.now().date()

   future_date = current_date + timedelta(days=number_of_days)
   print("Future date: ", future_date.strftime)

calculate_future_date()