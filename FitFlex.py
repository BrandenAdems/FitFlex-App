"""



TITLE: FITFLEX APP
AUTHOR: BRANDEN ADEMS ANAK KIETHSON



"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This section is to import library
import streamlit as st
import json
import openai
from dotenv import load_dotenv
import os
from datetime import date

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This section is to load the key from load_dotenv()
load_dotenv()

#%%
# This section is to call the OPENAI API KEY
openai.api_key = os.getenv('OPENAI_API_KEY')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Streamlit Web Design

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This section is for prompt Example
example1 = """
Give me a recommendation exercise to lose belly fat? Give me in the form of pin points.
"""

answer1 = """
To lose belly fat effectively, here are some key exercise recommendations:

1. High-Intensity Interval Training (HIIT): Incorporate HIIT workouts into your routine, which involve short bursts of intense exercises followed by brief recovery periods. This can include exercises like burpees, mountain climbers, high knees, or jumping jacks. HIIT helps burn calories, boosts metabolism, and promotes overall fat loss, including belly fat.

2. Cardiovascular Exercises: Engage in cardio activities that elevate your heart rate and burn calories. Options include running, cycling, swimming, brisk walking, or using cardio machines like the elliptical or rowing machine. Aim for at least 150 minutes of moderate-intensity cardio or 75 minutes of vigorous-intensity cardio per week.

3. Core-Strengthening Exercises: Focus on exercises that target the core muscles, including the abdominals and obliques. Examples include planks, Russian twists, bicycle crunches, reverse crunches, and stability ball exercises. Strengthening your core helps tone and define the abdominal muscles while contributing to overall stability.

4. Resistance Training: Include resistance exercises in your routine to build lean muscle mass. This can be done with free weights, weight machines, resistance bands, or bodyweight exercises like squats, lunges, push-ups, and tricep dips. Building muscle helps increase your metabolism and burn more calories throughout the day.

5. Pilates or Yoga: Consider incorporating Pilates or yoga into your fitness regimen. These practices focus on core strength, flexibility, and overall body awareness. They can help improve posture, tone the abdominal muscles, and reduce stress levels, which may contribute to belly fat accumulation.

6. Full-Body Workouts: Engage in full-body workouts that target multiple muscle groups simultaneously. Compound exercises like deadlifts, kettlebell swings, or thrusters engage the core while working other major muscle groups, helping to burn calories and promote overall fat loss.

"""

example2 = """
what is the perfect diet to lose belly fat? Give me in the form of pin points.
"""

answer2 = """

To support your efforts in losing belly fat, here are some key dietary recommendations:

1. Caloric Deficit: Create a calorie deficit by consuming fewer calories than your body needs for weight maintenance. Calculate your daily calorie needs based on your age, gender, weight, height, and activity level. Aim for a moderate caloric deficit of around 500-750 calories per day to promote gradual and sustainable weight loss.

2. Balanced Macronutrients: Focus on a balanced intake of macronutrients, including proteins, carbohydrates, and healthy fats:

    a. Proteins: Include lean protein sources such as chicken breast, turkey, fish, tofu, legumes, and Greek yogurt. Protein helps promote satiety, preserves lean muscle mass, and supports fat burning.

    b. Complex Carbohydrates: Opt for high-fiber, unprocessed carbohydrates like whole grains, fruits, vegetables, and legumes. These provide sustained energy, fiber for digestion, and essential nutrients.

    c. Healthy Fats: Consume sources of healthy fats like avocados, nuts, seeds, olive oil, and fatty fish (e.g., salmon). Healthy fats aid in hormone regulation, provide satiety, and support overall health.

3. Portion Control: Practice portion control to avoid overeating. Use smaller plates, measure your servings, and be mindful of portion sizes. Pay attention to hunger and fullness cues to avoid unnecessary calorie intake.

4. Reduced Added Sugars: Minimize your intake of added sugars found in sugary drinks, sweets, processed snacks, and desserts. These contribute to belly fat accumulation and provide empty calories. Opt for natural sweeteners like fruits or small amounts of honey or maple syrup if needed.

5. Increased Fiber Intake: Consume fiber-rich foods to promote satiety and improve digestion. Include sources like vegetables, fruits, whole grains, legumes, and nuts. Fiber helps regulate blood sugar levels and promotes a healthy gut.

6. Hydration: Stay adequately hydrated by drinking water throughout the day. Hydration supports overall bodily functions, aids digestion, and may help reduce overeating. Limit sugary beverages, sodas, and excessive alcohol intake, as they contribute to calorie intake.

7. Mindful Eating: Practice mindful eating by paying attention to your food choices, eating slowly, and savoring each bite. This can help you recognize hunger and fullness cues, prevent overeating, and promote a healthier relationship with food.

8. Consistency and Sustainability: Focus on adopting a balanced and sustainable eating pattern that you can maintain in the long term. Avoid quick-fix diets or extreme restrictions that are difficult to sustain, as they often lead to weight regain.

"""


example3 = """

give me at least 3 exercise i can do for cardiovascular exercises. give me in the form of pin points.

"""

answer3 = """

Certainly! Here are three cardiovascular exercises you can incorporate into your routine:

1. Exercise: Running
    a. Find a suitable location, such as a park or treadmill, and start with a brisk walk to warm up.
    b. Gradually increase your pace to a comfortable jogging or running speed.
    c. Maintain proper running form with an upright posture, relaxed shoulders, and a slight forward lean.
    d. Swing your arms naturally and land on the midfoot, rolling through to the toes.
    e. Start with a duration that suits your fitness level, such as 10-15 minutes, and gradually increase it over time.
    f. To challenge yourself, you can incorporate intervals of faster running or uphill sprints.
2. Exercise: Cycling
    a. Choose a stationary bike or ride outdoors on a bicycle.
    b. Adjust the seat height and position for proper alignment and comfort.
    c. Begin pedaling at a moderate pace, gradually increasing the resistance or speed.
    d. Maintain a steady pedaling rhythm and engage your core for stability.
    e. Aim for a duration of 20-30 minutes or more, depending on your fitness level.
    f. You can vary the intensity by incorporating intervals of increased resistance or alternating between seated and standing positions.
3. Exercise: Jumping Jacks
    a. Stand with your feet together and arms by your sides.
    b. Jump explosively, spreading your legs wider than shoulder-width apart and simultaneously raising your arms overhead.
    c. As you land, quickly return to the starting position by jumping back with your feet together and lowering your arms.
    d. Repeat the movement in a continuous, rhythmic fashion.
    e. Start with a set duration, such as 30 seconds, and gradually increase it as you improve.
    f. To make it more challenging, you can increase the speed or incorporate variations like squat jacks or cross jacks.

"""

example4 = """"

can you plan me an exercise to lose belly fat for a week and a diet plan for a week. i would love it to be in pinpoint form.

"""

answer4 = """

Certainly! Here's a weekly exercise plan and a sample diet plan to help you lose belly fat:

Weekly Exercise Plan:

1. Day 1: HIIT Workout

    a. Perform a 10-minute warm-up with dynamic stretches.
    b. Complete a 20-minute HIIT workout consisting of exercises like burpees, mountain climbers, high knees, and jumping jacks. Perform each exercise for 30 seconds with a 15-second rest in between. Repeat for four rounds.
    c. Finish with a 10-minute cooldown and static stretching.

2. Day 2: Cardiovascular Exercise

    a. Engage in 30 minutes of moderate-intensity cardio, such as running, cycling, or using a cardio machine.
    b. Aim for a steady pace that elevates your heart rate and makes you break a sweat.
    c. Cool down with a 5-minute walk and static stretches.

3. Day 3: Core-Strengthening Workout

    a. Perform a 10-minute warm-up with light cardio exercises like jogging in place or jumping rope.
    b. Complete a 15-minute core workout consisting of exercises like planks, Russian twists, reverse crunches, and stability ball exercises. Perform each exercise for 30 seconds with a 15-second rest in between. Repeat for three rounds.
    c. Finish with a 10-minute cooldown and static stretching.

4. Day 4: Rest or Active Rest

    a. Take a day of rest to allow your body to recover and repair. Alternatively, engage in light activities like walking, yoga, or stretching to promote active recovery.

5. Day 5: Full-Body Strength Training

    a. Perform a 10-minute warm-up with dynamic stretches.
    b. Complete a 30-minute full-body strength training session using exercises like squats, lunges, push-ups, rows, and shoulder presses. Perform 2-3 sets of 10-15 reps for each exercise.
    c. Finish with a 10-minute cooldown and static stretching.

6. Day 6: Cardiovascular Exercise

    a. Engage in 45 minutes of moderate-intensity cardio, such as swimming, brisk walking, or cycling.
    b. Vary the intensity throughout the session with intervals of higher intensity or incline if using a machine.
    c. Cool down with a 5-minute walk and static stretches.

7. Day 7: Active Rest or Flexibility Training

    a. Take another day of rest or focus on flexibility training with activities like yoga, Pilates, or stretching exercises.
    b. Relax and allow your body to recover from the week's workouts.

Note: Feel free to adjust the duration and intensity of the exercises based on your fitness level and preferences. Incorporate rest days and listen to your body to prevent overexertion or injury.

Sample Diet Plan:

1. Day 1:

    a. Breakfast: Greek yogurt with berries and a sprinkle of granola.
    b. Snack: A small handful of almonds.
    c. Lunch: Grilled chicken breast with mixed greens, cherry tomatoes, cucumbers, and balsamic vinaigrette.
    d. Snack: Carrot sticks with hummus.
    e. Dinner: Baked salmon with roasted vegetables (broccoli, bell peppers, and zucchini).
    f. Evening Snack: Sliced apples with a tablespoon of almond butter.

2. Day 2:

    a. Breakfast: Oatmeal topped with sliced bananas and a drizzle of honey.
    b. Snack: A protein smoothie with spinach, banana, almond milk, and a scoop of protein powder.
    c. Lunch: Quinoa salad with grilled vegetables (eggplant, peppers, and onions) and feta cheese.
    d. Snack: Greek yogurt with a teaspoon of chia seeds.
    e. Dinner: Stir-fried tofu with mixed vegetables (snap peas, carrots, and mushrooms) served over brown rice.
    f. Evening Snack: Celery sticks with peanut butter.

3. Day 3:

    a. Breakfast: Scrambled eggs with spinach, tomatoes, and whole wheat toast.
    b. Snack: A handful of grapes.
    c. Lunch: Turkey wrap with whole wheat tortilla, lettuce, tomato, and mustard.
    d. Snack: Cottage cheese with pineapple chunks.
    e. Dinner: Grilled shrimp skewers with roasted sweet potatoes and steamed asparagus.
    f. Evening Snack: A small bowl of mixed berries.

"""

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#This is section is the GPT code

def fitness_ai(text_input):
    fitness_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages=[
                {"role":"system",
                "content":""" 
                You are the best fitness trainer and planner. you are tasked with conceptualizing a cutting-edge fitness planner that combines advanced technology, innovative features, and user-friendly design.
                Your goal is to create a planner that not only helps individuals monitor their progress but also provides personalized recommendations and
                motivation to keep them engaged and on track with their fitness journey.

                """
                },

                {
                "role":"user",
                "content" : example1
                },

                {"role":"assistant",
                "content":answer1
                },

                {
                "role":"user",
                "content" : example2
                },

                {"role":"assistant",
                "content":answer2
                },

                {
                "role":"user",
                "content" : example3
                },

                {"role":"assistant",
                "content":answer3
                },

                {
                "role":"user",
                "content" : example4
                },

                {"role":"assistant",
                "content":answer4
                },

                {
                "role":"user",
                "content" : text_input
                }
            ],
            max_tokens = 1000,
            temperature = 1
    )
        
    fitness = fitness_response['choices'][0]['message']['content']
    return fitness

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# This section is for the process when the button is press

def main():

    st.set_page_config(
    page_title="FitFlex",
    page_icon="🏋️‍♂️",
    )

    
    header = st.container()
    description = st.container()

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # This section is for the background picture
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
    background-image: url("https://i.shgcdn.com/1e124b0b-7f01-435a-8812-ddb9c0bbe1bc/-/format/auto/-/preview/3000x3000/-/quality/lighter/");

    }
    </style>

    <style>
    [data-testid="stHeader"] {
    background-image: url("https://i.shgcdn.com/1e124b0b-7f01-435a-8812-ddb9c0bbe1bc/-/format/auto/-/preview/3000x3000/-/quality/lighter/");
    }
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)



    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # This section is for the header

    with header:
        st.markdown("""<h1 style='text-align: center; color: white;'>🏋️‍♂️ Welcome to FitFlex! 🏋️‍♂️ </h1>""", unsafe_allow_html=True)


    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # This section is for the description
    with description:
        st.markdown("""<h4 style='text-align: center; color: white;'>Where planning is easy with the help of AI. 
                    Plan the right exercise for you stay in shape and motivated! </h4>""", unsafe_allow_html=True)


    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # This section is for the sidebar (title)

    # st.sidebar.title("Navigation Bar")

    sidebar_style = """

    <style>
    .css-1cypcdb {
    background-color: rgba(255, 255, 255, 0.2);
    }
    </style>

    <style>
    .css-k7vsyb {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100px;
    }
    </style>

    """
    st.markdown(sidebar_style, unsafe_allow_html=True)

    #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # This section is for Text input
    with st.form('input_form'):
        text_input = st.text_area("Tell Us What is your plan for your fitness exercise (Example: I wish to train my muscle, give me a week worth of training with diet plans to increase my muscle mass): ")
        process = st.form_submit_button('Process')

    text_inputs = [text_input]


    if process:
        fitness = fitness_ai(text_input)
        text = st.text_area("Generated Plan", fitness, height= 500)
    
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
