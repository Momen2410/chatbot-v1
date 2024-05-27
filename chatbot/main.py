import streamlit as st
from PIL import Image
from Controller import classify_image, get_model_respose  # Ensure these functions are correctly imported

# Initialize session state variables
if 'classification_result' not in st.session_state:
    st.session_state.classification_result = None
if 'option1' not in st.session_state:
    st.session_state.option1 = None
if 'option2' not in st.session_state:
    st.session_state.option2 = None
if 'care_instructions' not in st.session_state:
    st.session_state.care_instructions = None

# Streamlit UI
st.title('Plant Classification')

# Step 1: Choose an option
option = st.radio("Choose an option:", ('Buy Plant', 'Have Plant'))

if option == 'Have Plant':
    # Step 2: Upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)

        # Step 3: Classify the image
        if st.button('Classify'):
            plant_name, plant_type, health_status = classify_image(image)
            st.session_state.classification_result = (plant_name, plant_type, health_status)
            
            # Reset session state for options and care instructions
            st.session_state.option1 = None
            st.session_state.option2 = None
            st.session_state.care_instructions = None

    # Check if classification result is available in session state
    if st.session_state.classification_result is not None:
        plant_name, plant_type, health_status = st.session_state.classification_result
        
        # Display classification results
        st.write('**Predicted Plant Name:**', plant_name)
        st.write('**Plant Type:**', plant_type)
        st.write('**Health Status:**', 'Healthy' if plant_type.strip('_') == 'healthy' else plant_type)
        
        # Step 4: Provide additional options based on health status
        if plant_type.strip('_') == 'healthy':
            st.session_state.option1 = st.radio("Choose an option:", ('You need good care', 'Thanks'))

            if st.session_state.option1 == 'You need good care':
                text = f''' 
                    Describe the best care for {plant_name}:
                    - Type of soil
                    - Ideal environment
                    - Ideal amount of water 
                    - Daily care
                    List potential diseases for a healthy {plant_name} in short sentences.
                '''
                if st.button('Get Care Instructions'):
                    st.session_state.care_instructions = get_model_respose(text)
            elif st.session_state.option1 == 'Thanks':
                st.write('See you later!')
        else:
            st.session_state.option2 = st.radio("Would you like to get care instructions?", ('Yes', 'No'))

            if st.session_state.option2 == 'Yes':
                text = f''' 
                    Describe the best care for {plant_name} with {plant_type}:
                    - Type of soil
                    - Ideal environment
                    - Ideal amount of water 
                    - Daily care
                    List potential diseases for {plant_name} with {plant_type} in short sentences.
                '''
                if st.button('Get Care Instructions'):
                    st.session_state.care_instructions = get_model_respose(text)
            elif st.session_state.option2 == 'No':
                st.write('See you later!')

    # Display care instructions if available
    if st.session_state.care_instructions:
        st.write(st.session_state.care_instructions)

else:
    st.write("Buy Plant Option Selected. UI for buying plant goes here.")
