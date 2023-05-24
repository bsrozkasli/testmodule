import pyttsx3
import random
import time
engine = pyttsx3.init()
questions=(
"Are you an organised person? How do you plan your schedule?",
"How do you overcome your fears? Explain.",
"What kind of books/movies do you like? Explain why.",
"Is there any activity you haven’t tried but would like to do? Explain.",
"Think of three jobs that you cannot do. Why do you think you cannot do them?",
"Which jobs do you think will be more popular in the future? Why?",
"Is there any book or movie that affected your life? Explain how.",
"How do you think a healthy life style should be like? Explain.",
"How do you choose your clothes? Explain.",
"Do you like making plans before your trips? Why or why not?",
"Do you think how you look is important? Why or why not?",
"Which places do you like visiting most when you travel to a new city? Explain why.",
"What are the best activities you can do in your hometown? Explain.",
"Do you think people will change their fashion style in the future? Why or why not?",
"What do you think is the easiest job? Explain why.",
"What would you like to do after you graduate from university? Explain.",
"Who has the most difficult job in your family? Explain why.",
"Which are the most popular jobs in the world nowadays? Explain why.",
"What can be the worst problem in work place? Explain.",
"Have you ever experienced a frightening situation? What happened? How did you react?",
"Are you good at giving advice to people? Why or why not?",
"Have you learnt something from a difficult situation? Explain.",
"Why do you think some life events change people’s lives? Explain.",
"How do you think people’s life styles changed? Compare the past and present time.",
"Have you ever changed anything about your life style? Explain why and how?",
"What is the best day you have ever had? Explain why.",
"Which activities do you like to do in your free time? Why?",
"What kind of art do you like most? Why?",
"What kind of books/movies are more popular today? Explain why.",
"Do you like doing or watching sports? Why or why not?"

)
# "You will have 15 seconds to think of two questions to ask. Let's begin"


def speaking():
    engine.setProperty('rate', 175)
    # voices = engine.getProperty('voices')
    # preferred_voice = random.randint(0,-1)
    # engine.setProperty('voice', voices[1].id)


    engine.say(questions[random.randint(0,len(questions))])
    engine.runAndWait()
    return timer(times)
def timer(times):
    for remainder in range(times,0,-1):
        print("remaining time",remainder,"second")
        time.sleep(1)
    engine.say("time is up","I ask you second question.")
    engine.runAndWait()
    return speaking()
times=45

print(speaking())
