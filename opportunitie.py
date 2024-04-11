import psycopg2
import config


 
class Opportunities:
    def __init__(self,name):
        self.opp_name = name
    
    @classmethod    
    def add_item(self,opp_id, opp_name, opp_email,opp_description,region_id, shift_id, day_id, frequency_id, type_id, subtype_id):
        self.id = opp_id
        self.opp_name = opp_name
        self.opp_email = opp_email
        self.opp_description = opp_description
        self.region_id = region_id
        self.shift_id = shift_id
        self.day_id = day_id
        self.frequency_id = frequency_id
        self.type_id = type_id
        self.subtype_id = subtype_id


    # def __str__(self):
    #     return f"Opportunities: {self.opp_name}, Volunteers: {self.opp_email}"
      
    @classmethod
    def from_db(self,user_input_opp_name):
        try:
            conn = psycopg2.connect(
                dbname = config.DATABASE,
                user = config.USERNAME,
                password = config.PASSWORD,
                host = config.HOSTNAME,
                port = config.PORT)  
            cursor = conn.cursor() 
            
            query = f"""SELECT * FROM opportunities WHERE opp_name = '{user_input_opp_name}'"""
            
            cursor.execute(query)
            row = cursor.fetchone()
            row = [str(value) if value is not None else 'NULL' for value in row]
            opp_id, opp_name, opp_email, opp_description, region_id, shift_id, day_id, frequency_id, type_id, subtype_id = row

            item = Opportunities(opp_name)
            item.opp_email = opp_email
            item.opp_description = opp_description
            item.region_id = region_id
            item.shift_id = shift_id
            item.day_id = day_id
            item.frequency_id = frequency_id
            item.type_id = type_id
            item.subtype_id = subtype_id
            
            
            # print(self.opp_name)
            # print(self.opp_email)
            # print(self.opp_description)
            # print(self.region_id)
            # print(self.shift_id)
            # print(self.day_id)
            # print(self.frequency_id)
            # print(self.type_id)
            # print(self.subtype_id)
            # item = Opportunities()
            
            return item
        
        except psycopg2.Error as e:
            print('\n\tError conecting\n', e)
        finally:
            if conn:
                cursor.close()
                conn.close() 
                
       
    def create_list_volunteers1(self):
        try:
            conn = psycopg2.connect(
                dbname = config.DATABASE,
                user = config.USERNAME,
                password = config.PASSWORD,
                host = config.HOSTNAME,
                port = config.PORT)  
            cursor = conn.cursor() 
            query = f"""
                SELECT volunteer.v_first_name ||' '|| volunteer.v_last_name AS full_name, volunteer.v_email, volunteer.v_phone,
                region.region_name, work_day.day_name, work_shift.shift_name,frequency.frequency_rate,
                type_opp.type_name,subtype_opp.subtype_name
                FROM volunteer
                LEFT JOIN region ON volunteer.region_id = region.region_id
                LEFT JOIN work_shift ON volunteer.shift_id = work_shift.shift_id
                LEFT JOIN work_day ON volunteer.day_id = work_day.day_id
                LEFT JOIN frequency ON volunteer.frequency_id = frequency.frequency_id
                LEFT JOIN type_opp ON volunteer.type_id = type_opp.type_id
                LEFT JOIN subtype_opp ON volunteer.subtype_id = subtype_opp.subtype_id
                WHERE 
                (volunteer.region_id = {self.region_id} OR volunteer.region_id IS NULL)
                AND (volunteer.shift_id = {self.shift_id} OR volunteer.shift_id IS NULL)
                AND (volunteer.day_id = {self.day_id} OR volunteer.day_id IS NULL)
                AND (volunteer.frequency_id = {self.frequency_id} OR volunteer.frequency_id IS NULL)
                AND (volunteer.type_id = {self.type_id} OR volunteer.type_id IS NULL)
                AND (volunteer.subtype_id = {self.subtype_id} OR volunteer.subtype_id IS NULL)
                """
            cursor.execute(query)
            all_rows = cursor.fetchall()
            if len(all_rows) > 0:
                
                print('Here are the volonteers that are suitable for you:')
                for row in all_rows:
                    row = [str(value) if value is not None else 'NULL' for value in row]
                    full_name, email, phone, city,day, shift, frequency, opp_type, opp_subtype = row
                    volunteer = f"""
                        Volunteer personal information:
                        Name: {full_name}, Email: {email}, Phone number: {phone}
                        Volonteer preferences in work:
                        City: {city}, Days and Shifts: {day} - {shift} - {frequency}
                        Type of work: {opp_type}
                            Subtype: {opp_subtype}
                        """
                    print(volunteer)
            else:
                print('No volunteers found matching the criteria.')
        
        except psycopg2.Error as e:
            print('\n\tError conecting\n', e)
        finally:
            if conn:
                cursor.close()
                conn.close()
        
     
    def save(self):        

        try:
            conn = psycopg2.connect(
                dbname = config.DATABASE,
                user = config.USERNAME,
                password = config.PASSWORD,
                host = config.HOSTNAME,
                port = config.PORT)  
            cursor = conn.cursor() 
            
            if check_opp(self.opp_name):
                print('You have already published this opportunity before.')
                return
            else:
                query = f"""
                    INSERT INTO opportunities (opp_name, opp_email,opp_description, region_id, shift_id, day_id, frequency_id, type_id, subtype_id)
                    VALUES
                    ('{self.opp_name}', '{self.opp_email}','{self.opp_description}',
                    '{self.region_id}', {self.shift_id},{self.day_id},{self.frequency_id}, {self.type_id}, {self.subtype_id});"""

                cursor.execute(query)
                conn.commit()
                print('Your opportunitie was added successfully')
            
        except psycopg2.Error as e:
            print('\n\tError conecting\n', e)
        finally:
            if conn:
                cursor.close()
                conn.close()
                       
    def region_search(self):
        counter = 0
        while True:
            user_region = input('Where are you?\n').title()
            if check_of('region','region_name',user_region) > '0':
                self.region_id = check_of('region','region_name',user_region)
                break
            else:
                if counter < 3:
                    print('Invalid input. Try again')
                    print(f'You have {3-counter} more tries')
                    counter +=1
                elif counter == 3:
                    print('Invalid input. Try again')
                    print('This is your last try')
                    counter +=1
                else:
                    self.region_id = 'NULL'
                    break
      
    def shift_search(self):
        counter = 0
        while True:
            length = list_of('work_shift')
            user_shift = int(input('What shifts do you need a volunteer for?\n'))
            if user_shift <= length:
                self.shift_id = user_shift
                break
            else:
                if counter < 3:
                    print('Invalid input. Try again')
                    print(f'You have {3-counter} more tries')
                    counter +=1
                elif counter == 3:
                    print('Invalid input. Try again')
                    print('This is your last try')
                    counter +=1
                else:
                    self.shift_id = 'NULL'
                    break
         
    def day_search(self):
        counter = 0
        while True:
            length = list_of('work_day')
            user_day = int(input('What day of the week will volunteer work?\n'))
            if user_day <= length:
                self.day_id = user_day
                break
            else:
                if counter < 3:
                    print('Invalid input. Try again')
                    print(f'You have {3-counter} more tries')
                    counter +=1
                elif counter == 3:
                    print('Invalid input. Try again')
                    print('This is your last try')
                    counter +=1
                else:
                    self.frequency_id = 'NULL'
                    break   
                
    def rate_search(self):
        counter = 0
        while True:
            length = list_of('frequency')
            user_frequency = int(input('For how many weeks are you looking for a volunteer?\n'))
            if user_frequency <= length:
                self.frequency_id = user_frequency
                break
            else:
                if counter < 3:
                    print('Invalid input. Try again')
                    print(f'You have {3-counter} more tries')
                    counter +=1
                elif counter == 3:
                    print('Invalid input. Try again')
                    print('This is your last try')
                    counter +=1
                else:
                    self.frequency_id = 'NULL'
                    break
        
    def type_search(self):
        counter = 0
        while True:
            length = list_of('type_opp')
            user_type = int(input('What kind of work do you need a volunteer for?\n'))
            if user_type <= length:
                self.type_id = user_type
                break
            else:
                if counter < 3:
                    print('Invalid input. Try again')
                    print(f'You have {3-counter} more tries')
                    counter +=1
                elif counter == 3:
                    print('Invalid input. Try again')
                    print('This is your last try')
                    counter +=1
                else:
                    self.type_id = 'NULL'
                    break
    
    def subtype_search(self):
        counter = 0
        while True:
            
            length = list_of_subtype('subtype_opp',self.type_id)
            user_subtype = int(input('Please specify what kind of work do you need a volunteer for?\n'))
            if user_subtype <= (length * self.type_id) and user_subtype > (length * (self.type_id - 1)):
                self.subtype_id = user_subtype
                break
            else:
                if counter < 3:
                    print('Invalid input. Try again')
                    print(f'You have {3-counter} more tries')
                    counter +=1
                elif counter == 3:
                    print('Invalid input. Try again')
                    print('This is your last try')
                    counter +=1
                else:
                    self.type_id = 'NULL'
                    break

        
def check_opp(opp_name):
    
    try:
        
        conn = psycopg2.connect(
            dbname = config.DATABASE,
            user = config.USERNAME,
            password = config.PASSWORD,
            host = config.HOSTNAME,
            port = config.PORT)  
        cursor = conn.cursor() 
        
        
        query = f"SELECT * FROM opportunities WHERE opp_name = '{opp_name}';"
        

        cursor.execute(query)
        check = False
        all_rows = cursor.fetchall()
        if len(all_rows) > 0:
            check = True
        # for row in all_rows:
        #     print(row)
        return check
            
    except psycopg2.Error as e:
        print('Error conecting', e)
    finally:
        if conn:
            cursor.close()
            conn.close()

def list_of(table):
    try:
        
        conn = psycopg2.connect(
            dbname = config.DATABASE,
            user = config.USERNAME,
            password = config.PASSWORD,
            host = config.HOSTNAME,
            port = config.PORT)  
        cursor = conn.cursor() 
        
        
        query = f"SELECT * FROM {table};"
        cursor.execute(query)
        
        all_rows = cursor.fetchall()
        for row in all_rows:
                row = [str(value) if value is not None else 'NULL' for value in row]
                item_id, item_name = row
                item_list = f"""Name: {item_name}\t({item_id})\n"""
                print(item_list)
        return len(all_rows)
            
    except psycopg2.Error as e:
        print('Error conecting', e)
    finally:
        if conn:
            cursor.close()
            conn.close()


def list_of_subtype(table, user_input): #,column_name,item_name):
    try:
        
        conn = psycopg2.connect(
            dbname = config.DATABASE,
            user = config.USERNAME,
            password = config.PASSWORD,
            host = config.HOSTNAME,
            port = config.PORT)  
        cursor = conn.cursor() 
        
        
        query = f"SELECT subtype_id, subtype_name FROM {table} WHERE type_id = {user_input};" # WHERE {column_name} = '{item_name}';"
        cursor.execute(query)
        
        all_rows = cursor.fetchall()
        for row in all_rows:
                row = [str(value) if value is not None else 'NULL' for value in row]
                subitem_id, item_name = row
                item_list = f"""Name: {item_name}\t({subitem_id})\n"""
                print(item_list)
        return len(all_rows)
            
    except psycopg2.Error as e:
        print('Error conecting', e)
    finally:
        if conn:
            cursor.close()
            conn.close()



def check_of(table, column_name, item_name):
    
    try:
        
        conn = psycopg2.connect(
            dbname = config.DATABASE,
            user = config.USERNAME,
            password = config.PASSWORD,
            host = config.HOSTNAME,
            port = config.PORT)  
        cursor = conn.cursor() 
        
        
        query = f"SELECT * FROM {table} WHERE {column_name} = '{item_name}';"
        
        cursor.execute(query)
        all_rows = cursor.fetchall()
        if len(all_rows) > 0:
            for row in all_rows:
                row = [str(value) if value is not None else 'NULL' for value in row]
                item_id, item_name = row
                return item_id
        else:
            return '-1'
            
    except psycopg2.Error as e:
        print('Error conecting', e)
    finally:
        if conn:
            cursor.close()
            conn.close()

# opp = Opportunities.from_db('Animal Shelter Volunteer')
# opp.create_list_volunteers1()