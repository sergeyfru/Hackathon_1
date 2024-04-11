import psycopg2
import config

import volunteer_search_engine  

class Link_Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=config.DATABASE,
            user=config.USERNAME,
            password=config.PASSWORD,
            host=config.HOSTNAME,
            port=config.PORT
        )
        self.cursor = self.conn.cursor()

    def find_organizations(self, region_id, shift_id, day_id, frequency_id, type_id, subtype_id):
        query = '''
            SELECT *
            FROM opportunities
            WHERE region_id = %s
            AND shift_id = %s
            AND day_id = %s
            AND frequency_id = %s
            AND type_id = %s
            AND subtype_id = %s;
        '''
        self.cursor.execute(query, (region_id, shift_id, day_id, frequency_id, type_id, subtype_id))
        organizations = self.cursor.fetchall()
        return organizations

    

print('1 to find volunteer')
print('2 to find organisation')

choice = input('Enter your choice: ')

try:
    if choice == '1':
        volunteer_search_engine.volunteer_finder()
    
    elif choice == '2':
        # organization_finder = Link_Database()

        print('''               
                  1) Jerusalem 2) Tel aviv 3) Haifa 4) Rishon LeZion 5) Petakh Tikva \n
                  6) Ashdod 7) Netanya 8) Beer Sheva 9) Holon 10) Bnei Brak \n
                 11) Ramat Gan 12) Bat Yam 13) Ashkelon 14) Hertzliya 15) Kfar Saba\n
                 16) Modiin 17) Hadera 18) Raanana 19) Lod 20) Nahariya \n
                 21) Ramat HaSharon 22) Rehovot 23) Nazareth 24) Givatayim 25) Kiryat Ata \n
                 26) Eilat 27) Acre 28) Bet Shemesh 29) Lakhish 30) Dimona \n
                 31) Arad 32) Afula 33) Tiberias 34) Bet Shemesh 35) Kiryat Yam \n
                 36) Nahal Oz 37 ) Kiryat Malakhi 38) Yavne 39) Safed 40) Yehud-Monosson \n
                 41) Maalot-Tarshiha 43) Nesher
           ''')
        
        while True:
            try:
                region_id = int(input("Enter region id: "))
                if region_id < 1 or region_id > 43:
                    print('Invalid entry, region_id should be between 1 and 43')
                else:
                    break
            except ValueError:
                print('Invalid input.')

        print('''\n
                    1) Morning Shift
                    2) Afternoon Shift
                    3) Evening Shift
                    4) Full-day
                    ''')
        while True:
            try:
                shift_id = int(input("Enter shift id: "))
                if shift_id < 1 or shift_id > 4:
                    print('Invalid entry, shift id should be between 1 and 4')
                else:
                    break
            except ValueError:
                print('Invalid input')

        print('''
                1) Sunday 2) Monday 3) Tuesday
                4) Wednesday 5) Thursday 6) Friday
                7) Saturday

            ''')
        while True:
            try:
                day_id = int(input("Enter day id: "))
                if day_id < 1 or day_id > 7:
                    print('Invalid entry, day id should be between 1 and 7')
                else: 
                    break
            except ValueError:
                print('Invalid Input')
        print('''
                Number X of a Week
              1) 1 Week 2) 2 Week 3) 3 Week \n
              4) 4 Week 5) 5 Week 6) 6 Week 7) More than two month

            ''')
        while True:
            try:
                frequency_id = int(input("Enter frequency id: "))
                if frequency_id < 1 or frequency_id > 7:
                    print('Invalid frequency id, must be between 1 and 7')
                else: 
                    break
            except ValueError:
                print('Invalid input')
        print(''' Work Types:
              1)  Helping in Shelters for homeless animals
              2) Working in charity shop
              3) Assisting in nurshing
              4) Enviromental actions and projects
              5) Teaching children and teenagers
              6) Assisting in free clinics and hospitals
              7) Organizing local events and festivals
              8) Online volunteering
              9) Aiding local homeless people
              10) Helping people with disabilities
            ''')
        while True:
            try:
                type_id = int(input("Enter type id: "))
                if type_id < 1 or type_id > 10:
                    print('Invalid entry, must be between 1 and 10')
                else:
                    break
            except ValueError:
                print('Invalid input')
        print(
            '''
              1) Care for animals                                2) Walking dogs
              3) Cleaning facilities                             4) Assisting in adopting events
              5) Sorting and pricing items                       6) Assisting customers
              7) Sales support                                   8) Maintaining cleanliness and order
              9) Socializing with elderly residents              10) Helping with daily tasks
              11) Organizing recreational activities             12) Reading books and conversations
              13) Cleaning up litter in parks and beaches        14) Tree planting
              15) Teaching local residence about ecolog          16) Participating in enviromental events
              17) Assisting in schools and youth centers         18)Teaching specific subjects
              19) Helping with homework                          20) Organizing extracurricular activities
              21) Assisting visitors                             22) Supporting medical staff
              23) Helping with documentation                     24) Organizing events for patients
              25) Assisting in organizing and hosting events     26) Support during the event day
              27) Spreading information                          28) Participating in organizing relaxation and entertainment
              29) Translating texts for non-profit organizations 30) Assisting in web design
              31) Managing social media                          32) Online counselling and support
              33) Distributing food and essential items          34) Providing information on available services
              35) Assisting in accessing medical help            36) Organizing events for social support
              37) Assisting with daily tasks                     38) Accompanying to events
              39) Assisting with transportation                  40) Conductiong individual sessions
 

''')
        while True:
            try:
                subtype_id = int(input('Enter subtype id '))
                if subtype_id < 1 or subtype_id > 40:
                    print('Invalid entry, must be between 1 and 40')
                else:
                    break
            except ValueError:
                print('Invalid input')

        organizations = Link_Database().find_organizations(region_id, shift_id, day_id, frequency_id, type_id, subtype_id)

        if organizations:
            print("Organizations matching the criteria:")
            for org in organizations:
                # print(org)
                print(f"Organization name: {org[1]}")
                print(f"Organization email address: {org[2]}")
                print(f"Opportunity Description: {org[3]}")
        else:
            print("No organizations found matching the criteria.")


except psycopg2.Error as e:
    print("Error connecting to the database:", e)
