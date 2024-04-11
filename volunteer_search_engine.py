import psycopg2
import config
import opportunitie


def volunteer_finder():
    counter = 0
    while True:
        print('Do you already have a request for volonteers?')
        user_input = input('Yes, We do (Y) \nNo, we have new request (N)\n').capitalize()
        if user_input =='Y':
            #finder of volonteer
            search_volunteers()
            break
        elif user_input == 'N':
            print('Let`s create a request')
            create_request()
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
                break
    
    
def search_volunteers():    #option (Y) - they have request
    print('Let`s find you file')
    user_input_opp_name = input('What is the name of your organization?\n').title()
    try:
        conn = psycopg2.connect(
            dbname = config.DATABASE,
            user = config.USERNAME,
            password = config.PASSWORD,
            host = config.HOSTNAME,
            port = config.PORT)  
        cursor = conn.cursor() 
        
        if opportunitie.check_opp(user_input_opp_name):       
            opp = opportunitie.Opportunities.from_db(user_input_opp_name)
            opp.create_list_volunteers1()
        else:
            print('You don`t have a requst')
            user_input = input('Do you want to create a new reqest?\n (Y) / (N)\n').capitalize()
            if user_input == 'Y':
                create_request()
                return
            else:
                return
            
            
        
    except psycopg2.Error as e:
        print('\n\tError conecting\n', e)
    finally:
        if conn:
            cursor.close()
            conn.close()


def create_request():  # option (N) - they want to create new request
    user_input_name = input('What name of your organization?\n').title()
    if opportunitie.check_opp(user_input_name):
        print('You already have a request')
        return
    else:
        opp = opportunitie.Opportunities(user_input_name)
        opp.opp_email = input('What is your email?\n')
        counter = 0
        while True:
            user_description = input('Do you want add description of your organization?\n (Y) / (N)\n').capitalize()
            if user_description == 'Y':
                opp.opp_description = input('Type your description:\n').capitalize()
                break
            elif user_description == 'N':
                opp.opp_description = 'NULL'
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
                    opp.opp_description = 'NULL'
                    break
        opp.region_search()
        
        opp.shift_search()
        
        opp.day_search()
        
        opp.rate_search()
        
        opp.type_search()
        
        opp.subtype_search()
        
        # opp.save()
    
        
        opp.create_list_volunteers1()
        





# volunteer_finder()
# search_volunteers()
    
    
    
    
    
    
    
    
    