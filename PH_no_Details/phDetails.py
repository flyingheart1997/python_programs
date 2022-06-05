import phonenumbers
from phonenumbers import timezone, geocoder, carrier

number = input("Enter Your No : ")
ph = phonenumbers.parse('+91'+number)
time = timezone.time_zones_for_number(ph)
car = carrier.name_for_number(ph, 'en')
region = geocoder.description_for_number(ph, 'en')
print(ph)
print(time)
print(car)
print(region)
