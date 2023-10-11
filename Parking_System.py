#We make a Class for Parking
class Parking:
    def __init__(self):
        #Here we use to Two Data Structures, list and Dictionary as adding and removing element
        #from Both of operation average is O(1)
        #Below list is consisting list of all 20 slots in parking
        self.Empty_Slots_Parking_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 18, 19, 20]
        #Below Dictionary is for keeping the Record of all Vehicle (Vehicle Number = Key) and (Slot as Value)
        self.Dictionary_list_Car_and_Slot = {}

    def Adding_Vehicle_in_Slots(self, New_Vehicle_Number):
        if len(self.Empty_Slots_Parking_list) != 0: #Checking for Any slot is Available or not
            try:
                slot = self.Empty_Slots_Parking_list[0] #Taking First Slot available in Parking
                self.Empty_Slots_Parking_list.pop(0) #Removing the slot from list 
                self.Dictionary_list_Car_and_Slot[New_Vehicle_Number] = slot #Adding Key: Value pair of Vehicle Number and Slot
                return f"{New_Vehicle_Number} Got the Slot {slot}"
            except Exception as e:
                return e
        else:
            print("Slots are Full Please check, any other Parking Area") 

    def Retrieving_Slots_for_Vehicle(self, G_Vehicle_Number):
        slot_found = self.Dictionary_list_Car_and_Slot.get(G_Vehicle_Number, 'Vehicle Not Found') # Using get method for dict to get Value
        if slot_found != 'Vehicle Not Found': #If slot is found for Given Vehicle, the it will giive output regardinng level and Slot
            if slot_found > 0 and slot_found < 11:
                return {"level": "A", "spot": slot_found}  
            else:
                return {"level": "B", "spot": slot_found}
                
        return f"{G_Vehicle_Number}  {slot_found}"

    def Removing_Vehicle_in_Slots(self, R_Vehicle_Number):
        if R_Vehicle_Number in self.Dictionary_list_Car_and_Slot: #checks if the Vehicle is available
            removed_vehicle = self.Dictionary_list_Car_and_Slot.pop(R_Vehicle_Number) #removes the Vehicle data and gives the slot value to variable assigned to it
            self.Empty_Slots_Parking_list.append(removed_vehicle) #Add the empty slot again to list
            self.Empty_Slots_Parking_list.sort() # Sort the List for Optimized Parking
            return f"{R_Vehicle_Number} Has Exited"
        else:
            return f"{R_Vehicle_Number} was Not Found"

def main():
    obj = Parking()

    while True:
        print("******Welcome to Parking******, \n Enter the Action for your Task \n -> Adding New Vehicle: 1 \n -> Checking for Vehicle: 2 \n -> Exiting From Parking: 3 \n -> Exit the Program: 4")
        Action = int(input("==> Enter the Number of Action: "))
        if Action == 1:
            New_Vehicle_Number = input("TAKING SLOT --> Enter the Vehicle Number: ")
            print(obj.Adding_Vehicle_in_Slots(New_Vehicle_Number))

        elif Action == 2:
            G_Vehicle_Number = input("VEHICLE EXISTING SLOT --> Enter the Vehicle Number: ")
            print(obj.Retrieving_Slots_for_Vehicle(G_Vehicle_Number))

        elif Action == 3:
            R_Vehicle_Number = input("RELEASING SLOT--> Enter the Vehicle Number: ")
            print(obj.Removing_Vehicle_in_Slots(R_Vehicle_Number))

        elif Action == 4:
            print("Exiting the Program")
            break

        else:
            print("Invalid Entry")

if __name__ == "__main__":
    main()
