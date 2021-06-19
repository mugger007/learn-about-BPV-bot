from telegram.ext import (
    Updater,
    CallbackContext,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    Filters,
)
from telegram import ReplyKeyboardMarkup
from dbhelper import DBHelper

(START_EXISTING,
START_NEW,
INTRO_QUES,
MAIN_MENU,
FACT_OF_THE_DAY,
HELP_MENU,
HELP_A_PART1,
HELP_B_PART1,
HELP_RETURN,
LEARN_ABOUT_BPV,
BPV_REFRESHER_PART1,
BPV_REFRESHER_PART2,
BPV_REFRESHER_PART3,
BPV_REFRESHER_PART4,
BP_MEASURING_PRACTICES,
BP_MEASURING_PRACTICES_1,
BP_MEASURING_PRACTICES_2,
BP_MEASURING_PRACTICES_2A,
BP_MEASURING_PRACTICES_2AA_PART1,
BP_MEASURING_PRACTICES_2AA_PART2,
BP_MEASURING_PRACTICES_2AA_PART3,
BP_MEASURING_PRACTICES_RETURN_2AA,
BP_MEASURING_PRACTICES_2AB_PART1,
BP_MEASURING_PRACTICES_2AB_PART2,
BP_MEASURING_PRACTICES_2B,
BP_MEASURING_PRACTICES_2BA_PART1,
BP_MEASURING_PRACTICES_2BA_PART2,
BP_MEASURING_PRACTICES_RETURN_2B,
BP_MEASURING_PRACTICES_2BB_PART1,
BP_MEASURING_PRACTICES_2BC_PART1,
BP_MEASURING_PRACTICES_2C_PART1,
BP_MEASURING_PRACTICES_2C_PART2,
BP_MEASURING_PRACTICES_2D,
BP_MEASURING_PRACTICES_2DA_PART1,
BP_MEASURING_PRACTICES_2DA_PART2,
BP_MEASURING_PRACTICES_RETURN_2D,
BP_MEASURING_PRACTICES_2DB_PART1,
BP_MEASURING_PRACTICES_1A_PART1,
BP_MEASURING_PRACTICES_1A_PART2,
BP_MEASURING_PRACTICES_RETURN_1A,
BP_MEASURING_PRACTICES_1B,
BP_MEASURING_PRACTICES_RETURN_1B,
BP_MEASURING_PRACTICES_1C_PART1,
BP_MEASURING_PRACTICES_1C_PART2,
BP_MEASURING_PRACTICES_RETURN_1,
BP_MEASURING_PRACTICES_1D_PART1,
BP_MEASURING_PRACTICES_1D_PART2,
LIFESTYLE,
LIFESTYLE_A_PART1,
LIFESTYLE_A_PART2,
LIFESTYLE_RETURN,
LIFESTYLE_B_PART1,
LIFESTYLE_B_PART2,
LIFESTYLE_C,
LIFESTYLE_CA_PART1,
LIFESTYLE_RETURN_C,
LIFESTYLE_CC_PART1,
LIFESTYLE_CC_PART2,
LIFESTYLE_CC_PART3,
LIFESTYLE_D,
LIFESTYLE_RETURN_D,
LIFESTYLE_E_PART1,
LIFESTYLE_E_PART2,
LIFESTYLE_F_PART1,
MED_HIST,
PATIENT_OBS,
PATIENT_OBS_NEXT,
PATIENT_OBS_RETURN,
PATIENT_REVIEW,
PATIENT_REVIEW_NEXT,
PATIENT_REVIEW_RETURN,
TREATMENT_ADHERENCE_PART1,
TREATMENT_ADHERENCE_PART2,
TREATMENT_ADHERENCE_RETURN,
TREATMENT_ADHERENCE_B_PART1,
OTHER_FACTORS,
OTHER_FACTORS_A_PART1,
OTHER_FACTORS_A_PART2,
OTHER_FACTORS_RETURN,
OTHER_FACTORS_B,
OTHER_FACTORS_BA_PART1,
OTHER_FACTORS_BA_PART2,
OTHER_FACTORS_BA_PART3,
OTHER_FACTORS_RETURN_B,
OTHER_FACTORS_BB_PART1,
OTHER_FACTORS_BB_PART2,
OTHER_FACTORS_BB_PART3,
PRE_QUIZ_PART1,
PRE_QUIZ_PART2,
PRE_QUIZ_Q1,
PRE_QUIZ_Q2,
PRE_QUIZ_Q3,
PRE_QUIZ_Q4_INTRO1,
PRE_QUIZ_Q4_INTRO2,
PRE_QUIZ_Q4_INTRO3,
PRE_QUIZ_Q4,
PRE_QUIZ_Q5,
POST_QUIZ_PART1,
POST_QUIZ_PART2,
POST_QUIZ_Q1,
POST_QUIZ_Q2,
POST_QUIZ_Q3,
POST_QUIZ_Q4_INTRO1,
POST_QUIZ_Q4_INTRO2,
POST_QUIZ_Q4_INTRO3,
POST_QUIZ_Q4,
POST_QUIZ_Q5,
SURVEY_START,
SURVEY_Q1,
SURVEY_Q2,
SURVEY_Q3A,
SURVEY_Q3B,
SURVEY_Q4A,
SURVEY_Q4B,
SURVEY_Q5A,
SURVEY_Q5B,
SURVEY_Q6,
SURVEY_Q7A,
SURVEY_Q7B,
SURVEY_Q8,
MAIN_MENU_RETURN) = range(121)

db = DBHelper()

def survey(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Awesome, {first_name}!
    \nThank you for taking the time to answer some of my questions regarding... myself. Your feedback will help me to get better at what I am doing!"""

    message_2 = """You can simply navigate around by selecting a button when provided with the options - there is no need for you to type anything at all (except when asked for it)!"""

    keyboard = [['Get Started']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return SURVEY_START

def survey_q1(update, context):

    message = """1. How quickly were you be able to learn to use this chatbot?
    \na. Almost instantly
    \nb. After some time
    \nc. Still learning how to use it"""

    keyboard = [['a'], ['b'], ['c']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return SURVEY_Q1

def survey_q2(update, context):

    survey_q1 = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q1': survey_q1}
    db.update_survey(survey_dict, chat_id)

    message = """2. How easy was it to use the chatbot?
    \na. Very easy
    \nb. Easy
    \nc. Neutral
    \nd. Difficult
    \ne. Very difficult"""

    keyboard = [['a'], ['b'], ['c'], ['d'], ['e']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return SURVEY_Q2

def survey_q3a(update, context):

    survey_q2 = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q2': survey_q2}
    db.update_survey(survey_dict, chat_id)

    message = """3a. The chatbot provides me with a personalized learning experience.
    \na. Strongly agree
    \nb. Agree
    \nc. Neutral
    \nd. Disagree
    \ne. Strongly disagree"""

    keyboard = [['a'], ['b'], ['c'], ['d'], ['e']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return SURVEY_Q3A

def survey_q3b(update, context):

    survey_q3a = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q3a': survey_q3a}
    db.update_survey(survey_dict, chat_id)

    message_1 = """3b. Rank the chatbot features from most relevant to least relevant in providing a personalized learning experience.
    \na. Addressing you by name
    \nb. Navigating through the educational modules at your own time
    \nc. Tracking your progress in the educational modules
    \nd. Choosing your preferred virtual patient to apply your knowledge
    \ne. Providing feedback on your virtual patient assessment"""

    message_2 = """Type in your ranking below (e.g. if you think that feature B is more relevant than feature A, and feature A more relevant than feature C, type in “B, A, C”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return SURVEY_Q3B

def survey_q4a(update, context):

    survey_q3b = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q3b': survey_q3b}
    db.update_survey(survey_dict, chat_id)

    message = """4a. What best describes your level of knowledge on identifying the factors affecting long-term BPV, BEFORE using the chatbot?
    \na. Excellent
    \nb. Very good
    \nc. Good
    \nd. Fair
    \ne. Poor"""

    keyboard = [['a'], ['b'], ['c'], ['d'], ['e']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return SURVEY_Q4A

def survey_q4b(update, context):

    survey_q4a = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q4a': survey_q4a}
    db.update_survey(survey_dict, chat_id)

    message = """4b. What best describes your level of knowledge on identifying the factors affecting long-term BPV, AFTER using the chatbot?
    \na. Excellent
    \nb. Very good
    \nc. Good
    \nd. Fair
    \ne. Poor"""

    keyboard = [['a'], ['b'], ['c'], ['d'], ['e']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return SURVEY_Q4B

def survey_q5a(update, context):

    survey_q4b = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q4b': survey_q4b}
    db.update_survey(survey_dict, chat_id)

    message = """5a. What best describes your level of knowledge on managing the factors affecting long-term BPV, BEFORE using the chatbot?
    \na. Excellent
    \nb. Very good
    \nc. Good
    \nd. Fair
    \ne. Poor"""

    keyboard = [['a'], ['b'], ['c'], ['d'], ['e']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return SURVEY_Q5A

def survey_q5b(update, context):

    survey_q5a = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q5a': survey_q5a}
    db.update_survey(survey_dict, chat_id)

    message = """5b. What best describes your level of knowledge on managing the factors affecting long-term BPV, AFTER using the chatbot?
    \na. Excellent
    \nb. Very good
    \nc. Good
    \nd. Fair
    \ne. Poor"""

    keyboard = [['a'], ['b'], ['c'], ['d'], ['e']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return SURVEY_Q5B

def survey_q6(update, context):

    survey_q5b = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q5b': survey_q5b}
    db.update_survey(survey_dict, chat_id)


    message_1 = """6. Rank the chatbot features from most liked to most disliked.
    \na. Accessing via messaging app (i.e. Telegram)
    \nb. Having a persona for the chatbot (i.e. Dorcas)
    \nc. Navigating by buttons only
    \nd. Having a “Help” section
    \ne. Having a “Fact of the day” section
    \nf. Having well-segregated educational modules
    \ng. Providing links to content resources (i.e. articles from scientific journals)
    \nh. Having virtual patient assessment
    \ni. Providing feedback on your virtual patient assessment"""

    message_2 = """Type in your ranking below (e.g. if you think that feature B is more relevant than feature A, and feature A more relevant than feature C, type in “B, A, C”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return SURVEY_Q6

def survey_q7a(update, context):

    survey_q6 = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q6': survey_q6}
    db.update_survey(survey_dict, chat_id)

    message = f"""7a. How relevant is the chatbot content for your stage of education?
    \na. Extremely relevant
    \nb. Very relevant
    \nc. Moderately relevant
    \nd. Slightly relevant
    \ne. Not relevant at all"""

    keyboard = [['a'], ['b'], ['c'], ['d'], ['e']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return SURVEY_Q7A

def survey_q7b(update, context):

    survey_q7a = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q7a': survey_q7a}
    db.update_survey(survey_dict, chat_id)

    message_1 = f"""7b. Rank the educational content from most relevant to least relevant to your stage of education.
    \na. Common factors that affect long-term BPV
    \nb. How the factors affect long-term BPV
    \nc. Appropriate questions to probe the patients to identify the factors affecting their long-term BPV
    \nd. Management plan(s) for the factors affecting long-term BPV"""

    message_2 = """Type in your ranking below (e.g. if you think that feature B is more relevant than feature A, and feature A more relevant than feature C, type in “B, A, C”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return SURVEY_Q7B

def survey_q8(update, context):

    survey_q7b = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q7b': survey_q7b}
    db.update_survey(survey_dict, chat_id)

    message = f"""8. How frequent would you be using this chatbot during your stage of education?
    \na. More than once a day
    \nb. Once a day
    \nc. Once a week
    \nd. Once a month
    \ne. Less than once a month"""

    keyboard = [['a'], ['b'], ['c'], ['d'], ['e']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return SURVEY_Q8

def survey_end(update, context):

    first_name = update.message.chat.first_name
    survey_q8 = update.message.text
    chat_id = update.message.chat_id
    survey_dict = {'survey_q8': survey_q8}
    db.update_survey(survey_dict, chat_id)

    message = f"""That's all! Thank you so much for your feedback, {first_name}! With your feedback, I will surely improve!"""

    keyboard = [['Main Menu']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return MAIN_MENU_RETURN
