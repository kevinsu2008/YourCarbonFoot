import streamlit as st
import openai
from openai import OpenAI
from PIL import Image

# import datasets
# from datasets import dataset
# Assuming 'dataset' is the list of dictionaries you've provided

# Example: Print each country's name and its per capita CO2 emissions


# for record in dataset:
#     entity = record["Entity"]
#     emissions = record["Per capita consumption-based CO₂ emissions"]
#     print(f"{entity}: {emissions} kg CO2e")

# Example: Find and print the country with the highest per capita CO2 emissions


# max_emissions = max(dataset, key=lambda x: x["Per capita consumption-based CO₂ emissions"])
# print(f"Country with the highest per capita CO2 emissions: {max_emissions['Entity']}, {max_emissions['Per capita consumption-based CO₂ emissions']} kg CO2e")

# def fcc(emission_input):
#     # Find the closest country above the input's emissions amount
#     closest_country = None
#     for country in dataset:
#         if country["Per capita consumption-based CO₂ emissions"] >= emission_input:
#             closest_country = country
#             break

    # Calculate percentage of the average citizen in the found country
    # percentage = (emission_input / closest_country["Per capita consumption-based CO₂ emissions"]) * 100

    # Format the output string
    # output = f"You emit {percentage:.2f}% of the average citizen in {closest_country['Entity']}"

    # return output

st.set_page_config(page_title='Your Carbon Footprint')
# Set streamlit columns
col1, col2, col3 = st.columns([1,2,1])
with col1:
    st.image('/Users/Kevin/Downloads/Your-Carbon-Foot-main/Your-Carbon-Foot-main/hackathon/image.png')
    st.image('/Users/Kevin/Downloads/Your-Carbon-Foot-main/Your-Carbon-Foot-main/hackathon/image.png')
    st.image('/Users/Kevin/Downloads/Your-Carbon-Foot-main/Your-Carbon-Foot-main/hackathon/image.png')

with col3:
    st.image('/Users/Kevin/Downloads/Your-Carbon-Foot-main/Your-Carbon-Foot-main/hackathon/image1.png')
    st.image('/Users/Kevin/Downloads/Your-Carbon-Foot-main/Your-Carbon-Foot-main/hackathon/image1.png')
    st.image('/Users/Kevin/Downloads/Your-Carbon-Foot-main/Your-Carbon-Foot-main/hackathon/image1.png')
# Function to generate OpenAI prompt and process response
def analyze_activities(openai_api_key, activities_description):
    openai.api_key = openai_api_key
    client = OpenAI(api_key="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")
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0.5,
        messages=
        [
            {"role": "system", "content": "NOTE ALL CALCULATIONS MUST BE EMISSIONS PER DAY NOT YEAR and DO NOT GENERATE ADDITIONAL INFORMATION THAT IS NOT STATED, SPECIFICALLY FOR TRANSPORT, You will give SPECIFIC NUMBERS AND METRICS for each category along with a specific bolded grand total before going into the individual components; (add brief explanations for how each factor is important and calculated, bold each factor). When giving answers, strongly consider the vehicles used and hours of heating when providing feedback. If the user provides additional information not related to transportation, heating, and home metrics, after you have addressed the 3 main categories, briefly address whether or not their information releases a significant amount of carbon and perform a calculation of daily carbon emissions if necessary. (Create a percentile based YourCarbonFootprint score from 1-100 to encapsulate emissions as compared to average individual. A high score means low carbon emissions and a low score means high carbon emissions) PLEASE DONT MAKE MISTAKES WITH HOME HEATING, TRANSPORTATION, HOME ENERGY, or ANYTHING ELSE DIRECTLY AFTER THE YOURCARBONFOOTPRINT SCORE, CALCULATE THE PERCENTILE OF CARBON EMISSIONS THE USER HAS IN COMPARISON TO TAYLOR SWIFT, WHO EMITS 8300 TONNES PER YEAR. FORMAT IT IN THE FOLLOWING MANNER 'Overall, your carbon emissions are (x) percent of Taylor Swift's daily emissions! Way to go!' where you calculate x/227340. THE YOURCARBONFOOTPRINT SCORE AND PERCENTILE OF TAYLOR SWIFT SHOULD GO AT THE END OF THE RESPONSE. THE YOURCARBONFOOTPRINT SCORE AND PERCENTILE OF TAYLOR SWIFT ARE VERY IMPORTANT AND SHOULD BOTH BE INCLUDED AT THE VERY END, WITH BOTH BOLDED. PUT THE bolded GRAND TOTAL IN THE BEGINNING OF THE RESPONSE PLEASE ALSO WRITE A BRIEF BULLETED LIST FORMATTED WITH AT LEAST 4 SPECIFIC SUGGESTIONS FOR THE USER TO OFFSET EMISSIONS WITH NUMERICAL ESTIMATES OF IMPACT"+str(activities_description)},
            # {"role": "user", "content": f"Given the following list of daily activities, estimate the total carbon emissions in kg CO2e. Use common emission factors for average circumstances. Also give numerous actionable steps the user can take to reduce their emissions in the future, and provide specific amounts plus make sure to bold each factor and structure just like the calculations. \n\nActivities:\n{activities_description}\n\nEstimate:"}
        ]    
    )        
     
    return completion.choices[0].message.content

# API Key input
# openai_api_key = st.text_input('Enter OpenAI API Key', type='password')
openai_api_key = "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"


# Streamlit UI
with col2:
    # st.write('<h1 style="text-align: center;"><marquee>Your Carbon Footprint</marquee></h1>', unsafe_allow_html=True)
    st.write('<h1 style="text-align: center;">Your Carbon Foot</h1>', unsafe_allow_html=True)

    # Activity inputs
    transportList = ['Car','Bus','Walk', 'Bike']
    st.write('<h6 style="text-align: center;"></h6>', unsafe_allow_html=True)
    st.write('<h6 style="text-align: center;">Transportation Metrics</h6>', unsafe_allow_html=True)
    transport_mode = st.selectbox('What is your usual mode of transportation?:', transportList)
    driving_miles = st.number_input('Driving distance in miles:', min_value=0.0, value=0.0, step=1.0)
    car_type = st.text_input('Vehicle Brand and model (For Car/Bus Only):', '')
    st.write('<h6 style="text-align: center;">Temperature/Heating Metrics</h6>', unsafe_allow_html=True)
    heating_temp = st.number_input('Average daily home heat temperature in Fahrenheit:', min_value=0.0, value=0.0, step=1.0)
    heat_time = st.number_input('Average hours per day spent with heating on:', min_value=0.0, value=0.0, step=0.5)
    elecList = ['Apartment','Townhouse','Single Family Home', 'Shared Home','Dorm/Shared Apartment']
    st.write('<h6 style="text-align: center;">Home Metrics</h6>', unsafe_allow_html=True)
    elecSelect = st.selectbox('What type of home do you live in?:', elecList)
    # Free text input for other activities
    other_activities = st.text_area("Describe any other daily activities:", height=100)
    # Construct the activities description
    
    #totalEmissions = f"Driving daily for {driving_km} km, vehicle used to drive is {car_type}, Heating daily set at {heating_temp} Fahrenheit for {heat_time} hours per day, Using {elecSelect} with the average kwh from every housing type. Set the output to a SINGLE NUMBER - the amount of total emissions NO UNITS"

    #countryMetric = st.number_input(fcc(totalEmissions))


    activities_description = f"Going daily for {driving_miles} miles 0 if indicated walking or biking, using a {transport_mode} mode of transport, {car_type}, Heating daily set at {heating_temp} Fahrenheit for {heat_time} hours per day, Using {elecSelect} with the average kwh from every housing type. Please list a couple other factors in the same format as the aforementioned factors"
    if other_activities:
        activities_description += f" Other activities: {other_activities}"
    # Button to calculate emissions

if st.button('Calculate Emissions'):
    if openai_api_key:
        with st.spinner('Analyzing activities...'):
            emissions_estimate = analyze_activities(openai_api_key, activities_description)
            totalEmissions = (analyze_activities(openai_api_key, activities_description + " ONLY GIVE SINGLE FLOAT VALUE NO WORDS"))
            # displayEmissions = st.number_input(fcc(totalEmissions))
            st.success(f"{emissions_estimate}")

    else:
        st.error('Please enter a valid OpenAI API Key')



# Streamlit UI
    
st.markdown("""
        <style>
            body {
                background-color: #25b509;
            }
            h1 {
                color: #25b509;
                font-family: "Roboto", sans-serif;
            }
            h6 {
                color: #25b509;
                font-family: "Roboto", sans-serif;
            }
            h3 {
                color: #25b509;
                text-decoration: underline;
                text-align: center;
            }
            p {
                color: #000000;
                text-align: left;
                font-family: "Roboto", sans-serif;
                font-size: 16px;
            # }
            # img {
            #     height: 350px;
            #     width: 240px;
            #     float: right;
            }
            .floatright {
                float: right;
            }
            li {
                color: #000000;
            }
        </style>
    """, unsafe_allow_html=True)
    
    
st.write('<h3 style=>Why Does It Matter?</h3>', unsafe_allow_html=True)
st.write("""
        Tracking your carbon emissions is absolutely essential in today's world. It's not just about being environmentally conscious; it's about taking charge of your impact on the planet and making a real difference in the fight against climate change. Imagine being able to see, in vivid detail, the exact ways your daily activities are affecting the environment. With the carbon calculator we've created, you have the power to do just that. This tool isn't just useful; it's revolutionary. It empowers you to uncover the hidden environmental costs of your lifestyle and discover simple yet impactful ways to reduce your carbon footprint. By using this calculator, you're not just making a change – you're joining a global movement towards a greener, more sustainable future. So why wait? Start tracking your carbon emissions today and be a part of the solution.
    """)
image = Image.open('/Users/Kevin/Downloads/Your-Carbon-Foot-main/Your-Carbon-Foot-main/hackathon/environment.jpg')
image.resize((200,125))
st.image("/Users/Kevin/Downloads/Your-Carbon-Foot-main/Your-Carbon-Foot-main/hackathon/environment.jpg", use_column_width=True)
st.write('<h3 style=>What Does My Carbon Footprint Score Mean?</h3>', unsafe_allow_html=True)
st.write("""
        Your Carbon Footprint Score allows you to guage how carbon-efficient you are through analyzing your day-to-day activities in an unbiased manner. A higher score is considered better for the climate, and we strongly encourage striving to achieve a Carbon Footprint Score of 90 or above!
    """)