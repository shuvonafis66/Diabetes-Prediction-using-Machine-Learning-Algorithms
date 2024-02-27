import streamlit as st

import pickle

st.set_option('deprecation.showfileUploaderEncoding', False)
model = pickle.load(open('diabetes_model.pkl', 'rb'))

st.markdown("<h1 style='text-align: center; color: #00afb9'>Diabetes Prediction</h1>"
                "<h6 style='text-align: center;color: #f7b538'>Supervised Machine Learning</h6>", unsafe_allow_html=True)


def main():



    # Custom style for rounded input boxes
    input_box_style = """
    <style>
        .stTextInput, .stNumberInput, .stSelectbox, .stSlider, .stDateInput {
            border-radius: 10px;
            padding: 4px;
        }
    </style>
    """
    st.markdown(input_box_style, unsafe_allow_html=True)





    # Custom style for slider color and team members
    custom_style = """
      <style>
          body {
              background-color: #e6f7ff;  /* Change this color to your desired color */
          }
          .team-members {
              background-color: #386641;
              border-radius: 10px;
              padding: 10px;
              margin-top: 20px;
          }
          .team-member {
              margin-bottom: 8px;
          }
          .custom-sidebar-title {
              background-color: #fca311;
              font-size: 24px;
              padding: 10px;
              text-align: center;
              border-radius: 10px;
              color: #2f3e46;  /* Change this color to your desired color */
              margin-top: 20px;
          }
          .result{
              background-color: #dc2f02;
              width: 33.33%;
              font-size: 24px;
              padding: 10px;
              text-align: center;
              margin: 0 auto;
              border-radius: 10px;
              color: #000000;  /* Change this color to your desired color */
              margin-top: 20px;
          }
          .good-result{
              background-color: #6a994e;
              font-size: 24px;
              padding: 10px;
              text-align: center;
              margin: 0 auto;
              border-radius: 10px;
              color: #000000;  /* Change this color to your desired color */
          }
          .head{
              background-color: #eda213;
              font-size: 24px;
              width: 70%;
              padding: 5px;
              text-align: center;
              margin: 0 auto;
              border-radius: 10px;
              color: #000000;  /* Change this color to your desired color */
          }
      </style>
      """
    st.markdown(custom_style, unsafe_allow_html=True)




    # Styled sidebar title
    st.sidebar.markdown("<div class='custom-sidebar-title'><b>Team Members</b></div>", unsafe_allow_html=True)
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")



    # Checkbox to toggle visibility
    collapse_checkbox = st.sidebar.checkbox("See Team Members")

    # Content to collapse
    team_members_content = """
    <p>Al Nafis Fuad Shuvo   20051717</p>
    <p>Ayman Bin Alam        20051719</p>
    <p>Ferdous Mahmud Fahad  20051727</p>
    <p>Md Roman Talukdar     20051734</p>
    <p>Prince Sarker Deganta 20051745</p>
    """



    # Show/hide content based on checkbox state
    if collapse_checkbox:
        st.sidebar.markdown("<div class='team-members'>" + team_members_content + "</div>", unsafe_allow_html=True)




    # st.sidebar.header("Logistic Regression  was used.")
    st.markdown("<div class='head'><b>JUST FILL IN THE INFORMATION BELOW</b></div>", unsafe_allow_html=True)

    # Customize background color for input elements
    st.markdown(
        """
        <style>
        div.stTextInput, div.stNumberInput, div.stSelectbox, div.stSlider, div.stDateInput {
            background-color: #0d1b2a !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )



    Pregnancies = st.slider("Input Your Number of Pregnancies", 0, 16)
    Glucose = st.slider("Input your Glucose", 74, 200)
    BloodPressure = st.slider("Input your Blood Pressure", 30, 180)
    SkinThickness = st.slider("Input your Skin thickness", 0, 100)
    Insulin = st.slider("Input your Insulin", 0, 250)
    BMI = st.slider("Input your BMI", 14.0, 60.0)
    DiabetesPedigreeFunction = st.slider("Input your Diabetes Pedigree Function", 0.0, 6.0)
    Age = st.slider("Input your Age", 0, 100)





    inputs = [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]




    if st.button('Predict'):
        result = model.predict(inputs)
        updated_res = result.flatten().astype(int)
        if updated_res == 0:
            st.markdown("<div class='good-result'><b>  Congratulation, You Dont have Diabetes </b></div>", unsafe_allow_html=True)
        else:
            st.write("I regret to inform you that you have been diagnosed with")
            st.markdown("<div class='result'><b>DIABETES</b></div>", unsafe_allow_html=True)




if __name__ == '__main__':
    main()