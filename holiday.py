
#This programme calculates a user’s holiday cost including the plane cost, hotel cost, and car rental cost.

city_flight = input("Which city are you travelling to? (choose from London, Abuja, New York and Winchester): ")
num_nights = int(input("How many nights will you spend at a hotel?: "))
rental_days = int(input("How many days would you be hiring a car?: "))




def hotel_cost(num_nights):
    hotel_per_night = 65
    total_cost = hotel_per_night * num_nights
    return total_cost

def plane_cost(city_flight):

    if city_flight == "London":
       return 100
    
    elif city_flight == "Abuja":
        return 750
    
    elif city_flight == "New York":
        return 400
    
    elif city_flight == "Winchester":
        return 80
    
    elif city_flight == "Yaounde":
        return 870

    else:
        return 0

def car_rental(rental_days):
    car_daily_rental_cost = 40
    total_cost = rental_days * car_daily_rental_cost
    return total_cost

def holiday_cost(hotel_cost, plane_cost, car_rental):
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days) 
    total_cost = total_hotel_cost + total_plane_cost + total_car_rental_cost
    return total_cost


total_cost = holiday_cost(hotel_cost, plane_cost, car_rental)

print("Your holiday details are as follows: ")
print(f"You will be travelling to {city_flight} and it will cost you £{plane_cost(city_flight)}")
print(f"You will be staying at a hotel for {num_nights} nights and it will cost you £{hotel_cost(num_nights)}")
print(f"You will be hiring a car for {rental_days} days and it will cost you £{car_rental(rental_days)}")
print(f"Your total holiday cost is £{total_cost}")

