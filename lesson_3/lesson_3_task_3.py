from address import Address
from mailing import Mailing

to_address = Address("112233", "Old_city", "Gogolya_Str.", "16", "10")
from_address = Address("445566", "New_city", "Shefchenko_Str.", "25", "5")

mailing = Mailing(to_address, from_address, 50, "TRACK112233")