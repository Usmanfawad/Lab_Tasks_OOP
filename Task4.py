#Task4
#USMAN FAWAD 18B-069-CS(A)
import datetime

class toyota:
    def __init__(self,name,chasisno,model,price,color,manufacturedate,registered,seatingcapacity,transmissiontype,batterytype):
        self.name = name
        self.chasisno=chasisno
        self.model=model
        self.price=price
        self.color=color
        self.manufacturedate=manufacturedate
        self.registered=registered
        self.seatingcapacity=seatingcapacity
        self.transmissiontype=transmissiontype
        self.batterytype=batterytype

    # repairance Cost
    head_light = 400
    rear_light = 500
    bumper = 1000

    def desciption_car(self):
        print("\n\nCar Description:")
        print("Car Model Name: {:<30}\nCar Chasis No: {:<30}\nCar Model: {:<30}\nCar Price: {:<30}\nCar Type: {:<30}\nCar Color: {:<30}\nCar Manufacture Date: {:<30}\nCar Register Date: {:<30}\nCar Seating Capacity: {:<30}\nCar transmission type: {:<30}\nCar Battery type: {:<30}".format(self.name,self.chasisno,self.model,self.price,self.__class__.__name__,self.color,self.manufacturedate,self.registered,self.seatingcapacity,self.transmissiontype,self.batterytype))

    def car_maintenance(self,option):
        print("\n<<<<Car Maintainance>>>>\n")
        if option.lower()=='yes' or option.lower()=='Y':
            print("Car Maintained")
        else:
            print("Maintainance not required")

    def change_car_oil(self,option_1):
        print("\n<<<<Car Oil change>>>>\n")
        if option_1.lower()=='yes' or option.lower()=='Y':
            print("Car oil changed.")
        else:
            print("No oil change required.")

    def car_repair(self,parttorepair):
        print("\n<<<<Toyota Repair Center>>>>\n")
        if self.__class__.__name__ == "mvp":
            if parttorepair.lower()== "Head Light":
                print("Headlight repaired for: $",head_light)
            elif parttorepair.lower()== "Rear Light":
                print("Rear Light repaired for: $",rear_light)
            elif parttorepair.lower()== "Bumper":
                print("Bumper repaired for: $",bumper)
            else:
                print("Part Not Available")

    def car_insure(self,renew):
        print("\n<<<Car Insurance>>>\n")
        if renew.lower()=='y' or renew.lower()=='Yes':
            print("Insurance renewed at: ",datetime.datetime.today().strftime('%Y-%m-%d'))
        else:
            print("Not Insured")

    def car_wash(self,option_2):
        print("\n<<<Car Wash>>>\n")
        if option_2.lower()=='y' or option_2.lower()=='Yes':
            print("Car Washed")

    def car_sell(self):
        print("\n<<<<Selling Car>>>>\n")
        print("Your ",self.name," has been sold for: $",self.price)

class mvp(toyota):
    def __init__(self,name,chasisno,model,price,color,manufacturedate,registered,seatingcapacity,transmissiontype,batterytype,fueltype,maxspeed,speakers,powerwindows,abs):
        super().__init__(name,chasisno,model,price,color,manufacturedate,registered,seatingcapacity,transmissiontype,batterytype)
        self.fuel_type=fueltype
        self.max_speed=maxspeed
        self.speakers= speakers
        self.power_windows=powerwindows
        self.abs=abs


    def desciption_car(self):
        super().desciption_car()
        print('{}: {}\n{}: {}\n{}: {}\n{}: {}\n{}: {}'.format("Fuel Type",self.fuel_type,"Max Speed",self.max_speed,"Speakers",self.speakers,"Power Windows",self.power_windows,"ABS",self.abs))


class busses(toyota):
    def __init__(self,name, chasisno, model, price, color, manufacturedate, registered, seatingcapacity, transmissiontype,batterytype,centrallocking,musicsystem,backdoor):
        super().__init__(name,chasisno, model, price, color, manufacturedate, registered, seatingcapacity, transmissiontype,batterytype)
        self.central_locking=centrallocking
        self.music_system=musicsystem
        self.back_door=backdoor

class suv(toyota):
    def __init__(self,name, chasisno, model, price, color, manufacturedate, registered, seatingcapacity, transmissiontype,batterytype,minturningradius,smartentry,climatecontrol):
        super().__init__(name,chasisno, model, price, color, manufacturedate, registered, seatingcapacity, transmissiontype,batterytype)
        self.min_turning_radius=minturningradius
        self.smart_entry=smartentry
        self.climate_control=climatecontrol




car_1=mvp('Hilux',4194891,2018,14300000,'red',2019,'yes',5,'auto','dry','petrol','125kmh','yes','yes','yes')
car_1.desciption_car()

car_1.car_repair('no')
car_1.car_maintenance("Bumper")
car_1.car_insure('y')
car_1.car_wash('y')
car_1.car_sell()