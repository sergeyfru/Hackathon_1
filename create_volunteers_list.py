import config
import psycopg2
from faker import Faker
import random


def create_volunteer():
    
    try:
        
        conn = psycopg2.connect(
            dbname = config.DATABASE,
            user = config.USERNAME,
            password = config.PASSWORD,
            host = config.HOSTNAME,
            port = config.PORT)  
        cursor = conn.cursor() 
        
        for i in range(150):
            faker = Faker()
            full = faker.name()
            first_name, last_name = full.split(' ',1)
            query = f"""
            INSERT INTO volunteer(v_first_name, v_last_name, v_email, v_phone, region_id, shift_id, day_id, frequency_id, type_id)
            VALUES
            ('{first_name}','{last_name}','{faker.email()}', {random.randint(100000000,1779999999)},
            {random.randint(1,42)},{random.randint(1,4)},{random.randint(1,7)},{random.randint(1,7)},{random.randint(1,10)});"""
            
            cursor.execute(query)
            conn.commit()
        print('finish')   
    except psycopg2.Error as e:
        print('Error conecting', e)
    finally:
        if conn:
            cursor.close()
            conn.close()
            
            
# create_volunteer() 
      