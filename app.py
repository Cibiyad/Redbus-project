import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(page_title="Bus Ride Dashboard", page_icon="🚍", layout="wide")
st.subheader("🚍📁 Bus Ride Information")

# Database connection function that accepts query parameters
def fetch_data(query, params=None):
    try:
        con = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="Cibiya_1279",
            database="redbus"
        )
        cursor = con.cursor()
        cursor.execute(query, params)
        data = cursor.fetchall()
        column_names = [i[0] for i in cursor.description]
        cursor.close()
        con.close()
        return data, column_names
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")
        return None, None

st.sidebar.header("Please filter here")

# Sidebar for selecting the state transport corporation
state_transport_corp = st.sidebar.selectbox(
    'Select the State Transport Corporation:',
    ['Kerala (KSRTC)', 'Kadamba (KTCL)', 'WBTC (CTC)', 'North Bengal(NBSTC)', 'Punjab (PEPSU)', 
     'Bihar (BSRTC)', 'Meghalaya Transport Corporation(MTC)', 'Sikkim Nationalised Transport (SNT)', 
     'Chandigarh (CTU)', 'KAAC TRANSPORT']
)

# Fetch the routes based on the selected state transport corporation
def fetch_routes(state_corp):
    query = f"""
        SELECT DISTINCT route_name 
        FROM finalbusdata 
        WHERE busname LIKE %s
    """
    busname_filter = f"%{state_corp.split()[0]}%"
    routes, _ = fetch_data(query, (busname_filter,))
    return [r[0] for r in routes] if routes else []

routes = fetch_routes(state_transport_corp)
if routes:
    selected_route = st.sidebar.selectbox("Select Route", routes)
else:
    st.write(f"No routes available for {state_transport_corp}.")

# Other filters
bus_type = st.sidebar.selectbox('Select the bus type:', ['Sleeper', 'Seater'])
air_con = st.sidebar.selectbox('Select A/C or Non A/C:', ['A/C', 'Non A/C'])
ratings = st.sidebar.selectbox('Select the ratings:', ['4 to 5', '3 to 4', '2 to 3', '1 to 2', '0 to 1', 'unrated'])
price_option = st.sidebar.selectbox('Select the bus fare:', ['upto ₹200', 'upto ₹400', 'upto ₹600', 'upto ₹800', 'upto ₹1000', '₹1000+'])

# Date and time inputs
travel_date = st.sidebar.date_input('Select the Date of Travel:')
starting_time = st.sidebar.time_input('Select the Starting Time:')

# Map price options to numeric ranges
price_map = {
    'upto ₹200': (0, 200),
    'upto ₹400': (0, 400),
    'upto ₹600': (0, 600),
    'upto ₹800': (0, 800),
    'upto ₹1000': (0, 1000),
    '₹1000+': (1000, float('inf'))
}

min_price, max_price = price_map[price_option]

# Constructing dynamic query conditions
bustype_query = ""
if bus_type == 'Sleeper' and air_con == 'A/C':
     bustype_query = """bustype LIKE '%Sleeper%' AND bustype LIKE '%A/C%'"""
elif bus_type == 'Seater' and air_con == 'A/C':
     bustype_query = """bustype LIKE '%Seater%' AND bustype LIKE '%A/C%'"""
elif bus_type == 'Sleeper' and air_con == 'Non A/C':
     bustype_query = """bustype LIKE '%Sleeper%' AND bustype LIKE '%Non A/C%'"""
elif bus_type == 'Seater' and air_con == 'Non A/C':
     bustype_query = """bustype LIKE '%Seater%' AND bustype LIKE '%Non A/C%'"""

rating_query = ""
if ratings == '4 to 5':
    rating_query = "star_rating BETWEEN 4 AND 5"
elif ratings == '3 to 4':
    rating_query = "star_rating BETWEEN 3 AND 4"
elif ratings == '2 to 3':
    rating_query = "star_rating BETWEEN 2 AND 3"
elif ratings == '1 to 2':
    rating_query = "star_rating BETWEEN 1 AND 2"
elif ratings == '0 to 1':
    rating_query = "star_rating BETWEEN 0 AND 1"
elif ratings == 'unrated':
    rating_query = "star_rating = 0"

time_query = f"""departing_time >= '{starting_time.strftime('%H:%M:%S')}'"""

price_query = f"price BETWEEN {min_price} AND {max_price}"

# Handle button click to trigger the search
if st.sidebar.button("Search"):
    formatted_date = travel_date.strftime('%Y-%m-%d')

    query = f"""
        SELECT route_name, busname, bustype, departing_time, duration, reaching_time, star_rating, seats_available, price
        FROM finalbusdata
        WHERE route_name = %s AND 
              {bustype_query} AND 
              {rating_query} AND 
              {time_query} AND 
              {price_query}
    """
    
    params = (selected_route,)
    # st.write(f"Executing query with parameters: {params}")
    
    data, column_names = fetch_data(query, params)
    
    # Display the fetched data
    if data:
        df = pd.DataFrame(data, columns=column_names)
        st.subheader(f"Bus Details for Route: {selected_route}")
        st.table(df)
    else:
        st.write("No buses available for the selected route with the given filters.")
