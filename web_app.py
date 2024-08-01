import streamlit as st
import mysql.connector
import pandas as pd
from datetime import time

# Database connection
def fetch_data(query):
    con = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Cibiya_1279",
        database="redbus"
    )
    cursor = con.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    # Get column names
    column_names = [column[0] for column in cursor.description]
    con.close()
    return rows,column_names

with st.sidebar:
    state_transport_corp = st.selectbox('Select the State Transport Corporation:',
    ['Kerala (KSRTC)', 'Kadamba (KTCL)', 'WBTC (CTC)','North Bengal(NBSTC)','Punjab (PEPSU)','Bihar (BSRTC)',
     'Meghalaya Transport Corporation(MTC)','Sikkim Nationalised Transport (SNT)','Chandigarh (CTU)','KAAC TRANSPORT'])
if state_transport_corp == 'Kerala (KSRTC)':
        route = ['Bangalore to Kozhikode', 'Kozhikode to Ernakulam', 'Kozhikode to Bangalore', 
                 'Ernakulam to Kozhikode', 'Kozhikode to Mysore', 'Kozhikode to Thiruvananthapuram', 
                 'Bangalore to Kalpetta (kerala)', 'Mysore to Kozhikode', 'Kalpetta (kerala) to Bangalore', 
                 'Kozhikode to Thrissur', 'Thiruvananthapuram to Kozhikode', 'Bangalore to Kannur', 
                 'Kozhikode to Kottayam', 'Kannur to Bangalore', 'Kottayam to Kozhikode', 
                 'Thrissur to Kozhikode', 'Kozhikode to Kalpetta (kerala)', 'Coimbatore to Ooty', 
                 'Kalpetta (kerala) to Kozhikode']
elif state_transport_corp == 'Kadamba (KTCL)':
        route = ['Pune to Goa', 'Goa to Pune', 'Mumbai to Goa', 'Goa to Mumbai', 'Pandharpur to Goa', 
                 'Bangalore to Goa', 'Goa to Pandharpur', 'Belagavi to Goa', 'Goa to Bangalore', 
                 'Solapur to Goa', 'Goa to Kolhapur(Maharashtra)', 'Goa to Solapur', 'Goa to Sangola (Solapur)', 
                 'Sangola (Solapur) to Goa', 'Calangute (goa) to Goa Airport', 'Goa to Sangli', 'Calangute (goa) to Mopa Airport', 
                 'Mopa Airport to Calangute (goa)', 'Ponda to Belagavi', 'Goa to Miraj', 'Goa Airport to Calangute (goa)', 
                 'Marcel to Belagavi', 'Shivamogga to Goa', 'Goa to Mopa Airport', 'Goa to Satara', 'Belagavi to Marcel', 
                 'Mopa Airport to Goa', 'Shirdi to Goa', 'Goa to Shivamogga', 'Goa to Shirdi', 'Goa to Goa Airport', 
                 'Margao to Mopa Airport', 'Goa Airport to Goa', 'Mopa Airport to Margao', 'Belagavi to Saquelim', 
                 'Panaji to Mopa Airport', 'Saquelim to Belagavi', 'Calangute (goa) to Goa', 'Calangute (goa) to Panaji', 
                 'Goa Airport to Panaji']
elif state_transport_corp == 'WBTC(CTC)':
        route =['Durgapur (West Bengal) to Kolkata','Digha to Barasat (West Bengal)','Barasat (West Bengal) to Digha', 'Suri to Kolkata',
                'Kolkata to Digha', 'Bolpur (West Bengal) to Kolkata', 'Kolkata to Suri', 'Digha to Kolkata', 'Kolkata to Durgapur (West Bengal)', 
                'Habra to Digha', 'Barasat (West Bengal) to Nandakumar (West Bengal)', 'Asansol (West Bengal) to Kolkata', 'Barasat (West Bengal) to Contai (Kanthi)', 
                'Siliguri to Kolkata', 'Kolkata to Bolpur (West Bengal)', 'Barasat (West Bengal) to Kolaghat', 'Barasat (West Bengal) to Heria', 'Digha to Habra', 
                'Midnapore to Barasat (West Bengal)', 'Haldia to Barasat (West Bengal)', 'Midnapore to Kolkata', 'Durgapur (West Bengal) to Purulia', 
                'Kolkata to Siliguri', 'Durgapur (West Bengal) to Barasat (West Bengal)', 'Haldia to Kolkata', 'Kolkata to Purulia', 'Kolkata to Asansol (West Bengal)', 
                'Barasat (West Bengal) to Nimtouri', 'Habra to Kolaghat', 'Habra to Contai (Kanthi)']
elif state_transport_corp == 'Punjab (PEPSU)':
        route = ['Patiala to Delhi', 'Delhi to Patiala', 'Ludhiana to Delhi', 'Delhi to Ludhiana', 'Phagwara to Delhi', 
                 'Jalandhar to Delhi', 'Delhi to Jalandhar', 'Patiala to Delhi Airport', 'Jalandhar to Delhi Airport', 
                 'Ludhiana to Delhi Airport', 'Phagwara to Delhi Airport', 'Delhi Airport to Ludhiana', 'Delhi to Phagwara', 
                 'Delhi to Amritsar', 'Amritsar to Delhi', 'Delhi Airport to Patiala', 'Amritsar to Delhi Airport', 
                 'Kapurthala to Delhi', 'Delhi Airport to Jalandhar', 'Chandigarh to Bathinda', 'Chandigarh to Faridkot', 
                 'Chandigarh to Patiala']
elif state_transport_corp == 'Bihar (BSRTC)':
        route = ['Patna (Bihar) to Bettiah', 'Gopalganj (Bihar) to Delhi', 'Patna (Bihar) to Motihari', 
                 'Delhi to Motihari', 'Bettiah to Patna (Bihar)', 'Motihari to Delhi', 'Patna (Bihar) to Balmiki Nagar (bihar)', 
                 'Balmiki Nagar (bihar) to Patna (Bihar)', 'Patna (Bihar) to Kathmandu', 'Patna (Bihar) to Katihar', 
                 'Patna (Bihar) to Purnea', 'Patna (Bihar) to Hazaribagh', 'Ranchi to Patna (Bihar)', 'Hazaribagh to Patna (Bihar)', 
                 'Patna (Bihar) to Raxaul', 'Muzaffarpur (Bihar) to Kathmandu', 'Patna (Bihar) to Ranchi', 'Muzaffarpur (Bihar) to Ranchi', 
                 'Kathmandu to Patna (Bihar)', 'Ranchi to Muzaffarpur (Bihar)', 'Motihari to Lucknow', 'Lucknow to Motihari', 
                 'Motihari to Kathmandu', 'Agra to Motihari', 'Patna (Bihar) to Janakpur (Nepal)', 'Muzaffarpur (Bihar) to Hazaribagh', 
                 'Purnea to Patna (Bihar)', 'Patna (Bihar) to Araria (Bihar)', 'Darbhanga to Patna (Bihar)', 
                 'Patna (Bihar) to Saharsa', 'Motihari to Agra', 'Hajipur (Bihar) to Kathmandu', 
                 'Kathmandu to Motihari', 'Patna (Bihar) to Forbesganj', 'Ranchi to Hajipur (Bihar)', 
                 'Lucknow to Gopalganj (Bihar)']
elif state_transport_corp == 'Chandigarh (CTU)':        
            route = ['Chandigarh to Delhi', 'Delhi to Chandigarh', 'Yamuna Nagar to Chandigarh', 
                     'Chandigarh to Shimla', 'Chandigarh to Vrindavan', 'Chandigarh to Yamuna Nagar', 
                     'Chandigarh to Sujanpur (himachal pradesh)', 'Ludhiana to Chandigarh', 'Hamirpur (Himachal Pradesh) to Chandigarh', 
                     'Vrindavan to Chandigarh', 'Chandigarh to Hamirpur (Himachal Pradesh)', 'Sujanpur (himachal pradesh) to Chandigarh', 
                     'Shimla to Chandigarh', 'Chandigarh to Ludhiana', 'Chandigarh to Dharamshala (Himachal Pradesh)', 
                     'Chandigarh to Dehradun', 'Chandigarh to Baijnath', 'Pathankot to Chandigarh', 'Chandigarh to Haridwar', 
                     'Chandigarh to Pathankot', 'Talwara to Chandigarh', 'Dehradun to Chandigarh', 'Amritsar to Chandigarh', 
                     'Chandigarh to Rishikesh', 'Chandigarh to Talwara', 'Chandigarh to Dinanagar (punjab)', 'Dinanagar (punjab) to Chandigarh', 
                     'Rishikesh to Chandigarh', 'Chandigarh to Amritsar', 'Chandigarh to Agra', 'Dharamshala (Himachal Pradesh) to Chandigarh', 
                     'Chandigarh to Katra (jammu and kashmir)', 'Hisar (Haryana) to Chandigarh', 'Rohtak to Chandigarh', 
                     'Chandigarh to Una (Himachal Pradesh)', 'Chandigarh to Jammu (j and k)', 'Chandigarh to Rohtak', 
                     'Chandigarh to Manali', 'Chandigarh to Haldwani', 'Jawala Ji to Chandigarh', 'Agra to Chandigarh', 
                     'Jammu (j and k) to Chandigarh', 'Chandigarh to Hisar (Haryana)', 'Chandigarh to Kathgodam', 'Haridwar to Chandigarh', 
                     'Katra (jammu and kashmir) to Chandigarh', 'Baijnath to Chandigarh', 'Narnaul to Chandigarh', 'Chandigarh to Jawala Ji']
elif state_transport_corp == 'NORTH BENGAL STATE TRANSPORT CORPORATION':
            route = ['Kolkata to Siliguri', 'Siliguri to Kolkata', 'Kolkata to Raiganj', 'Raiganj to Kolkata', 'Kolkata to Malda', 
                     'Cooch Behar (West Bengal) to Berhampore (West Bengal)', 'Kolkata to Cooch Behar (West Bengal)', 'Malda to Kolkata', 'Berhampore (West Bengal) to Cooch Behar (West Bengal)', 
                     'Kolkata to Balurghat', 'Berhampore (West Bengal) to Siliguri', 'Siliguri to Berhampore (West Bengal)', 'Kolkata to Gangarampur', 
                     'Cooch Behar (West Bengal) to Malda', 'Malda to Cooch Behar (West Bengal)', 'Balurghat to Kolkata', 'Kolkata to Jalpaiguri', 'Kolkata to Islampur (West Bengal)', 
                     'Falakata (West Bengal) to Berhampore (West Bengal)', 'Kolkata to Falakata (West Bengal)', 'Cooch Behar (West Bengal) to Raiganj', 'Siliguri to Cooch Behar (West Bengal)', 
                     'Raiganj to Krishnanagar (West Bengal)', 'Raiganj to Siliguri', 'Kolkata to Buniadpur', 'Gangarampur to Kolkata', 'Siliguri to Ranaghat', 'Siliguri to Krishnanagar (West Bengal)', 
                     'Falakata (West Bengal) to Kolkata', 'Kolkata to Farakka', 'Siliguri to Raiganj', 'Kolkata to Dhupguri (West Bengal)', 'Falakata (West Bengal) to Malda', 'Kolkata to Gazole', 
                     'Berhampore (West Bengal) to Falakata (West Bengal)', 'Balurghat to Siliguri', 'Siliguri to Barasat (West Bengal)', 'Kolkata to Maynaguri (West Bengal)', 'Kolkata to Itahar (West Bengal)', 
                     'Cooch Behar (West Bengal) to Krishnanagar (West Bengal)', 'Cooch Behar (West Bengal) to Omarpur (West Bengal)', 'Berhampore (West Bengal) to Jalpaiguri', 'Malda to Siliguri', 'Raiganj to Ranaghat', 
                     'Cooch Behar (West Bengal) to Farakka', 'Cooch Behar (West Bengal) to Siliguri']
elif state_transport_corp == 'KAAC TRANSPORT':
            route = ['Guwahati to Diphu', 'Dokmoka to Guwahati', 'Guwahati to Dokmoka', 'Guwahati to Bokolia (Assam)', 'Diphu to Hamren']
elif state_transport_corp == 'Meghalaya Transport Corporation(MTC)':
            route = ['Guwahati to Shillong', 'Shillong to Tura (Meghalaya)', 'Shillong to Guwahati', 'Tura (Meghalaya) to Shillong',
                      'Shillong to Silchar', 'Silchar to Shillong', 'Shillong to Karimganj', 'Shillong to Williamnagar (Meghalaya)',
                      'Williamnagar (Meghalaya) to Shillong', 'Hailakandi to Shillong']
elif state_transport_corp == 'Sikkim Nationalised Transport (SNT)':
            route =['Gangtok to Siliguri', 'Siliguri to Gangtok', 'Siliguri to Melli (Sikkim)']

bus_route = st.selectbox('Select the route:',route)
bus_type = st.selectbox('Select the bus type:',['Sleeper','Seater'])

air_con = st.selectbox('Select A/C or Non A/C:',['A/C', 'Non A/C'])

ratings = st.selectbox('Select the ratings:',['4 to 5','3 to 4','2 to 3','1 to 2','0 to 1','unrated'])

starting_time = st.selectbox('Select the starting time:',['00:00 to 06:00','06:00 to 12:00','12:00 to 18:00','18:00 to 24:00'])

price_option = ['upto ₹200','upto ₹400','upto ₹600','upto ₹800','upto ₹1000', '₹1000+']
price = st.select_slider('Select the bus fare:',price_option)
    

click_button = st.button('search')

if bus_type == 'Sleeper' and air_con == 'A/C':
     bustype_query = """bustype LIKE '%Sleeper%'
                    AND (bustype LIKE '%A/C%' OR
                        bustype LIKE 'A/C%')
                    AND (bustype NOT LIKE '%Non%' OR
                        bustype NOT LIKE 'Non%' OR
                        bustype NOT LIKE 'NON%')"""
elif bus_type == 'Seater' and air_con == 'A/C':
     bustype_query = """bustype LIKE '%Seater%'
                    AND (bustype LIKE '%A/C%' OR
                        bustype LIKE 'A/C%')
                    AND bustype LIKE '%MULTI AXLE'
                    And (bustype NOT LIKE '%Non%' OR
                        bustype NOT LIKE 'Non%' OR
                        bustype NOT LIKE 'NON%')"""
elif bus_type == 'Sleeper' and air_con == 'Non A/C':
     bustype_query = """bustype LIKE '%Sleeper%'
                    AND (bustype LIKE '%Non%' OR
                        bustype LIKE 'Non%' OR
                        bustype LIKE 'NON%')"""  
elif bus_type == 'Seater' and air_con == 'Non A/C':
     bustype_query = """bustype LIKE '%Seater%'
                    AND (bustype LIKE '%Non%' OR
                        bustype LIKE 'Non%' OR
                        bustype LIKE 'NON%')"""         

if ratings == '4 to 5':
     rating_query = """star_rating >= 4 AND
                        star_rating <= 5"""
elif ratings == '3 to 4':
     rating_query = """star_rating >= 3 AND
                        star_rating <= 4"""
elif ratings == '2 to 3':
     rating_query = """star_rating >= 2 AND
                        star_rating <= 3"""
elif ratings == '1 to 2':
     rating_query = """star_rating >= 1 AND
                        star_rating <= 2"""
elif ratings == '0 to 1':
     rating_query = """star_rating > 0 AND
                        star_rating <= 1"""
elif ratings == 'unrated':
     rating_query = "star_rating = 0"

if starting_time == '00:00 to 06:00':
     time_query = f"""departing_time >= '{starting_time[:6]}' AND 
                    departing_time <= '{starting_time[-5:]}'"""
elif starting_time == '06:00 to 12:00':
     time_query = f"""departing_time >= '{starting_time[:6]}' AND 
                    departing_time <= '{starting_time[-5:]}'"""
elif starting_time == '12:00 to 18:00':
     time_query = f"""departing_time >= '{starting_time[:6]}' AND 
                    departing_time <= '{starting_time[-5:]}'"""
elif starting_time == '18:00 to 24:00':
     time_query = f"""departing_time >= '{starting_time[:6]}' AND 
                    departing_time <= '{starting_time[-5:]}'"""


if price == 'upto ₹200':
     price_query = "price <= 200"
elif price == 'upto ₹400':
     price_query = "price <= 400"
elif price == 'upto ₹600':
     price_query = "price <= 600"
elif price == 'upto ₹800':
     price_query = "price <= 800"
elif price == 'upto ₹1000':
     price_query = "price <= 1000"
elif price == '₹1000+':
     price_query = "price >= 1000"

st.title(':blue[Bus information for the route]')
query = f"""SELECT * FROM finalbusdata WHERE
            route_name = '{bus_route}' AND 
            {bustype_query} AND
            {rating_query} AND
            {time_query} AND
            {price_query};"""

if click_button:
        # Fetch data from the database
        data, columns = fetch_data(query)
        # Convert to a DataFrame
        df = pd.DataFrame(data, columns=columns)
        # Convert time columns to appropriate format
        # time_columns = ['departing_time', 'reaching_time']  # time column names
        # for col in time_columns:
        #     if col in df.columns:
        #         df[col] = pd.to_datetime(df[col], format='%H:%M').dt.time
        # df['departing_time'] = pd.to_datetime(df['departing_time'], format='%H:%M').dt.time
        # df['reaching_time'] = pd.to_datetime(df['reaching_time'], format='%H:%M').dt.time

        df['departing_time'] = df['departing_time'].apply(lambda x: (pd.Timestamp('1970-01-01') + x).time() if pd.notna(x) else None)
        df['reaching_time'] = df['reaching_time'].apply(lambda x: (pd.Timestamp('1970-01-01') + x).time() if pd.notna(x) else None)
        # Display the data
        st.write(df)
            