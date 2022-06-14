# ------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# ------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []


class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """
    # TODO Add Code to the CD class
    cd_id = 0
    cd_title = ''
    cd_artist = ''
    pass


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """

    # TODO Add code to process data from a file
    @staticmethod
    def load_inventory(file_name):
        # artist, title, id
        cd_list = []
        cd_Inventory = open(file_name, "r")
        for line in cd_Inventory:
            data = line.strip().split(',')
            cd_object = CD()
            cd_object.cd_artist = data[0]
            cd_object.cd_title = data[1]
            cd_object.cd_id = int(data[2])
            cd_list.append(cd_object)
        cd_Inventory.close()
        return cd_list

    # TODO Add code to process data to a file
    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        objFile = open(file_name, 'w')
        for cd in lst_Inventory:
            objFile.write(cd.cd_artist + ',' + cd.cd_title + ',' + str(cd.cd_id) + '\n')
        objFile.close()

    pass


# -- PRESENTATION (Input/Output) -- #
class IO:
    # TODO add docstring
    """Handling Input / Output

       properties:

       methods:
       def show_menu(self):
       def get_choice(self):
       def display_data(cd_list):
       def add_cd(self):
       """

    # TODO add code to show menu to user
    @staticmethod
    def show_menu():
        print("\n --------- Menu ---------"
              "\n1. See current inventory "
              "\n2. Add data to the inventory "
              "\n3. Save inventory to file "
              "\n4. Load inventory from file "
              "\n5. Exit program")

    # TODO add code to captures user's choice
    @staticmethod
    def get_choice():
        choice = input('Which option do you want: ')
        return int(choice)

    # TODO add code to display the current data on screen
    @staticmethod
    def display_data(cd_list):
        print('Current Inventory\n')
        for cd in cd_list:
            print("Id: " + str(cd.cd_id) + " Artist: " + cd.cd_artist + " Title: " + cd.cd_title)

    # TODO add code to get CD data from user
    @staticmethod
    def add_cd():
        cd_object = CD()
        print("\nAdding a CD")
        cd_object.cd_artist = input("Enter an Artist name: ")
        cd_object.cd_title = input("Enter an Title name: ")
        cd_object.cd_id = int(input("Enter an ID: "))
        return cd_object

    pass


# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
lstOfCDObjects = lstOfCDObjects + (FileIO.load_inventory(strFileName))
# Display menu to user
while True:
    IO.show_menu()
    option = IO.get_choice()
    if option == 1:
        IO.display_data(lstOfCDObjects)
    elif option == 2:
        lstOfCDObjects.append(IO.add_cd())
    elif option == 3:
        FileIO.save_inventory(strFileName, lstOfCDObjects)
    elif option == 4:
        FileIO.load_inventory(strFileName)
    elif option == 5:
        break

# show user current inventory
# let user add data to the inventory
# let user save inventory to file
# let user load inventory from file
# let user exit program
