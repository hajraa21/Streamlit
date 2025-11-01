import streamlit as st
st.title("General Knowledge Quiz🤓")
st.subheader("Test your general knowledge with this fun quiz!🧠")

st.text("Choose the correct answer for each question. Let's see how many you can get right!🎯")


# Initialize session state
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False

score = 0

# Quiz questions
st.radio("1. What is the capital of France?",('Berlin','Madrid','Paris','Rome'),index=None,key='q1')
if st.session_state.quiz_submitted:
    if st.session_state.q1=='Paris':
        score+=1
        st.success("Correct! Paris is such a beautiful city!")

    else:
        st.error("❌Wrong! Paris is the capital of France!")

st.radio("2. Which planet is known as the Red Planet?",('Earth','Mars','Jupiter','Venus'),index=None,key='q2')
if st.session_state.quiz_submitted:
    if st.session_state.q2=='Mars':
        score+=1
        st.success("Thats Right! Also, did you know Earth is known as the 'Green Planet'?")
    else:
        st.error("❌Wrong! Mars is the red planet!")

st.radio("3. Who painted the Mona Lisa?",('Vincent van Gogh','Pablo Picasso','Leonardo da Vinci', 'Michelangelo'),index=None,key='q3')
if st.session_state.quiz_submitted:
    if st.session_state.q3=='Leonardo da Vinci':
        score+=1
        st.success("Correct! He was such a great artist!")
    else:
        st.error("❌Wrong! Leonardo da vinci painted The Mona Lisa!")

st.radio("4. Which element has the chemical symbol 'Au'?",('Aluminium','Gold','Coppper','Silver'),index=None,key='q4')
if st.session_state.quiz_submitted:
    if st.session_state.q4=='Gold':
        score+=1
        st.success('Correct! Did you know Gold is also known as Aurum in science?')

    else:
        st.error("❌Wrong! Gold is represented as 'Au' in chemistry!")

st.radio("5. What is the largest mammal in the world?",('Elephant','Blue Whale','Giraffe', 'Polar Bear'),index=None,key='q5')
if st.session_state.quiz_submitted:
    if st.session_state.q5=='Blue Whale':
        score+=1
        st.success("Correct! Blue Whale is the largest mammal and can weigh upto 200 tons!")

    else:
        st.error("❌Wrong, Blue Whale is the largest mammal!")

st.radio("6. What is the largest ocean on Earth?", ('Atlantic','Indian', 'Arctic', 'Pacific'),index=None,key='q6')
if st.session_state.quiz_submitted:
    if st.session_state.q6=='Pacific':
        score+=1
        st.success("Correct! The Pacific Ocean covers more than 30% of the planet's surface!")

    else:
        st.error("❌Wrong! Pacific ocean is the largest ocean on Earth!")

st.radio(" What is the smallest prime number?",('1','2','5','9'),index=None,key='q7')
if st.session_state.quiz_submitted:
    if st.session_state.q7 == '2':
        score+=1
        st.success("Thats right! 2 is the first and only number that has exactly two factors: 1 and itself!")

    else:
        st.error("❌Wrong! 2 is the smallest prime number!")

st.radio("Who wrote 'Romeo and Juliet'?",('Charles Dickens', 'Jane Austen', 'William Shakespeare',  'Mark Twain'),index=None,key='q8')
if st.session_state.quiz_submitted:
    if st.session_state.q8=='William Shakespeare':
        score+=1
        st.success("Correct! Shakespeare is often called England's national poet and the 'Bard of Avon'.")

    else:
        st.error("❌Wrong! William Shakespear wrote 'Romeo and Juliet'!")

st.radio("What is the hardest natural substance on Earth?",('Gold','Iron','Diamond','Silver'),index=None,key='q9')
if st.session_state.quiz_submitted:
    if st.session_state.q9=='Diamond':
        score+=1
        st.success("Correct! Diamonds are formed under high-pressure, high-temperature conditions deep within the Earth's mantle.")

    else:
        st.error("❌Wrong! Diamonds are the hardest natural substance!")

st.radio("How many continents are there?",('5','6','7','8'),index=None,key='q10')
if st.session_state.quiz_submitted:
    if st.session_state.q10=='7':
        score+=1
        st.success("Correct! The seven continents are Asia, Africa, North America, South America, Antarctica, Europe, and Australia.")

    else:
        st.error("❌Wrong! There are 7 continents!")

st.divider()
# Submit button
if st.button('Submit Quiz'):
    if None in [st.session_state.q1, st.session_state.q2, st.session_state.q3, st.session_state.q4, st.session_state.q5, 
                st.session_state.q6, st.session_state.q7, st.session_state.q8, st.session_state.q9, st.session_state.q10]:
        st.warning("⚠️ Please answer all questions before submitting!")
    else:
        st.session_state.quiz_submitted = True
        st.rerun()  

 # Display score and feedback       
if st.session_state.quiz_submitted:
    st.write(f'🎯 You have successfully completed the quiz! Your score is **{score} out of 10**!🥳')
    
    if score == 10:
        st.balloons()
        st.success("🏆 Perfect score! You're a genius!")
        
    elif score >= 7:
        st.snow()
        st.info("🎉 Great job! You really know your stuff!")
        
    elif score >= 4:
        st.success("Good effort! Keep practicing to improve your score!")
    else:
        st.error("Try again and you'll do better next time!")
