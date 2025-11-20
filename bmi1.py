from langgraph.graph import StateGraph, START, END
from typing import TypedDict
import streamlit as st

# Page config
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")


#Define state
class BMI(TypedDict):
    weight: float
    height: float
    bmi: float
    category: str

#define functions
def calculate_bmi(state: BMI) -> BMI:
    weight = state['weight']
    height = state['height']
    bmi = weight / (height ** 2)
    state['bmi'] = round(bmi, 2)
    return state

def label(state: BMI) -> BMI:
    bmi = state['bmi']
    
    if bmi < 18.5:
        state['category'] = 'Underweight'
    elif 18.5 <= bmi < 25:
        state['category'] = 'Normal Weight'
    elif 25 <= bmi < 30:
        state['category'] = 'Overweight'
    elif 30 <= bmi < 35:
        state['category'] = 'Obesity Class I'
    elif 35 <= bmi < 40:
        state['category'] = 'Obesity Class II'
    else:
        state['category'] = 'Obesity Class III'
    
    return state

#define Graph
graph = StateGraph(BMI)
graph.add_node('calculate_bmi', calculate_bmi)
graph.add_node('label', label)
graph.add_edge(START, 'calculate_bmi')
graph.add_edge('calculate_bmi', 'label')
graph.add_edge('label', END)
wf = graph.compile()


st.title("💪 BMI Calculator")
st.markdown("### Track your health journey with ease!")


tab1, tab2 = st.tabs(["📊 Calculate", "ℹ️ About BMI"])

with tab1:
    st.markdown("#### Enter Your Details")
    
    # Input fields 
    col1, col2 = st.columns(2)
    
    with col1:
        weight = st.number_input(
            "Weight (kg)",
            min_value=20.0,
            max_value=300.0,
            value=60.0,
            step=0.5,   
        )
    
    with col2:
        height = st.number_input(
            "Height (m)",
            min_value=0.5,
            max_value=2.5,
            value=1.6,
            step=0.01,
        )
    
    st.markdown("---")
    
    # Calculate button
    if st.button("🔍 Calculate My BMI", type="primary"):
        # Execute workflow
        initial_state = {'weight': weight, 'height': height}
        final_state = wf.invoke(initial_state)
        
        # Display results
        
        st.markdown("### Your Results")
        
        # BMI display
        bmi_value = final_state['bmi']
        category = final_state['category']
        
        # Create metric display
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                label="Your BMI",
                value=bmi_value,
                delta=None
            )
        
        with col2:
            # Color code based on category
            if 'Normal' in category:
                st.success(f"**{category}** ✅")
                st.markdown("Great job! Keep it up! 🎉")
            elif 'Underweight' in category:
                st.warning(f"**{category}** ⚠️")
                st.markdown("Consider consulting a nutritionist.")
            else:
                st.error(f"**{category}** ⚠️")
                st.markdown("Consider consulting a healthcare professional.")
        
        # Visual BMI scale
        st.markdown("---")
        st.markdown("#### Where You Stand")
        
        # Progress bar showing position on BMI scale
        if bmi_value < 18.5:
            progress_val = (bmi_value / 18.5) * 0.2
        elif bmi_value < 25:
            progress_val = 0.2 + ((bmi_value - 18.5) / (25 - 18.5)) * 0.3
        elif bmi_value < 30:
            progress_val = 0.5 + ((bmi_value - 25) / (30 - 25)) * 0.2
        elif bmi_value < 40:
            progress_val = 0.7 + ((bmi_value - 30) / (40 - 30)) * 0.2
        else:
            progress_val = 0.9
        
        st.progress(min(progress_val, 1.0))

with tab2:
    st.markdown("### What is BMI?")
    st.info("""
    **Body Mass Index (BMI)** is a simple calculation using a person's height and weight. 
    It's a useful tool to assess whether an individual has a healthy body weight for a given height.
    """)
    
    st.markdown("### Formula")
    st.code("BMI = weight (kg) / (height (m))²", language="python")
    
    st.markdown("### BMI Categories")
    
    categories_data = {
        "Category": ["Underweight", "Normal Weight", "Overweight", "Obesity Class I", "Obesity Class II", "Obesity Class III"],
        "BMI Range": ["< 18.5", "18.5 - 24.9", "25.0 - 29.9", "30.0 - 34.9", "35.0 - 39.9", "≥ 40.0"],
        "Icon": ["⚠️", "✅", "⚠️", "⚠️", "⚠️", "⚠️"]
    }
    
    for i in range(len(categories_data["Category"])):
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.write(f"**{categories_data['Category'][i]}**")
        with col2:
            st.write(categories_data['BMI Range'][i])
        with col3:
            st.write(categories_data['Icon'][i])

    st.image('https://img.freepik.com/premium-vector/stick-figure-man-body-mass-index-formula-vector-illustration-set-person-bmi-infographic-chart-icon_654181-2713.jpg?semt=ais_incoming&w=740&q=80', caption="BMI Categories Overview")
    
    st.markdown("---")
    st.caption("💡 **Note:** BMI is a screening tool and not a diagnostic tool. Consult healthcare professionals for personalized advice.")

