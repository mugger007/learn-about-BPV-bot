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

def pre_quiz_part1(update, context):

    first_name = update.message.chat.first_name

    message = f"""Awesome {first_name}! Before we get started, allow me to find out more about your current knowledge on this subject. Not to worry, it is just a few multiple-choice questions. Click on the button below when you are ready to start the assessment!"""

    keyboard = [['Get Started'], ['Main Menu']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return PRE_QUIZ_PART1

def pre_quiz_part2(update, context):

    message_1 = f"""As this will be an assessment of what your baseline knowledge, do complete it to the best of your abilities!"""

    message_2 = """Before you look at the patient case, let us start off with some general questions on factors affecting long-term BPV."""

    message_3 = """Dorcas wishes you all the best!"""

    keyboard = [["Let's Go!"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return PRE_QUIZ_PART2

def pre_quiz_q1(update, context):

    message_1 = """1. Which factor(s) can affect a patient's long-term BPV?
    \na. BP measurement errors
    \nb. Lifestyle factors such as dietary sodium intake
    \nc. Activation of sympathetic nervous system
    \nd. Poor adherence to antihypertensive therapy"""

    message_2 = """Type in your answer below (e.g. “a, b, d”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return PRE_QUIZ_Q1

def pre_quiz_q2(update, context):

    pre_quiz_q1 = update.message.text
    chat_id = update.message.chat_id
    pre_quiz_dict = {'pre_quiz_q1': pre_quiz_q1}
    db.update_quiz(pre_quiz_dict, chat_id)

    message_1 = """2. For a hypertensive patient who has an elevated BP after starting a treatment regimen on antidepressants (specifically MAOIs), what would be the appropriate management plan(s)?
    \na. Consider switching to an alternative agent (e.g., SSRIs) depending on indication
    \nb. Encourage patient to consume tyramine-containing foods
    \nc. Consider increasing the dosage of the patient's antihypertensive(s)
    \nd. Do nothing, as this is only a transient BP elevation"""

    message_2 = """Type in your answer below (e.g. “a, b, d”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return PRE_QUIZ_Q2

def pre_quiz_q3(update, context):

    pre_quiz_q2 = update.message.text
    chat_id = update.message.chat_id
    pre_quiz_dict = {'pre_quiz_q2': pre_quiz_q2}
    db.update_quiz(pre_quiz_dict, chat_id)

    message = """3. When a patient has his/her ankle crossed over the knee while taking BP measurement, how would that affect his BP readings? Select your answer below .
    \na. It could lead to an underestimation of BP (i.e. lower than actual BP)
    \nb. It could lead to an overestimation of BP (i.e. higher than actual BP)
    \nc. It does not affect the BP readings"""

    keyboard = [['a'], ['b'], ['c']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return PRE_QUIZ_Q3

def pre_quiz_q4_intro1(update, context):

    first_name = update.message.chat.first_name
    pre_quiz_q3 = update.message.text
    chat_id = update.message.chat_id
    pre_quiz_dict = {'pre_quiz_q3': pre_quiz_q3}
    db.update_quiz(pre_quiz_dict, chat_id)

    message = f"""Thank you, {first_name}, for completing the general questions, now let us look at the patient information."""

    keyboard = [['Patient Information']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return PRE_QUIZ_Q4_INTRO1

def pre_quiz_q4_intro2(update, context):

    message = """Mary is a 65-year-old Chinese female diagnosed with hypertension. She also has type 2 diabetes. Her office/clinic BP today is 124/72 mmHg. Mary feels well, except for the occasional headaches at work that she has been experiencing since her last visit. Her average home BP monitoring (HBPM) readings for the past week was 136/88 mmHg. She has been exercising less and put on a significant amount of weight since the last visit."""

    keyboard = [['More Information']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return PRE_QUIZ_Q4_INTRO2

def pre_quiz_q4_intro3(update, context):

    message = """Social History (SH):
    \n- Works as a cashier in NTUC
    \nPast Medical History (PMH):
    \n- T2DM x 2 years
    \n- HTN x 1 month
    \nMedication History:
    \n- Amlodipine 5 mg OD
    \n- Glipizide 20 mg BD (increased from 10 mg BD one year ago)
    \n- Metformin 850 mg TDS
    \n- Ibuprofen 400 mg PRN, max 1.2 g a day
    \nAllergies:
    \n- Penicillin (rashes)
    \nG6PD status:
    \n- Not deficient"""

    keyboard = [['Continue to Q4']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return PRE_QUIZ_Q4_INTRO3

def pre_quiz_q4(update, context):

    message_1 = """1. Which factor(s) could have caused the significant BP variability in Mary?
    \na. Less exercise
    \nb. Weight gain
    \nc. Increased dosage of Glipizide
    \nd. Taking Ibuprofen"""

    message_2 = """Type in your answer below (e.g. “a, b, d”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return PRE_QUIZ_Q4

def pre_quiz_q5(update, context):

    pre_quiz_q4 = update.message.text
    chat_id = update.message.chat_id
    pre_quiz_dict = {'pre_quiz_q4': pre_quiz_q4}
    db.update_quiz(pre_quiz_dict, chat_id)

    message_1 = """2. Based on your answer for Q4, what is/are the appropriate management plan(s) for Mary's long-term BPV?
    \na. Encourage more exercise and a healthier diet
    \nb. Increased dosage of Amlodipine
    \nc. Switch to a non-NSAID analgesic
    \nd. Continue to monitor BP"""

    message_2 = """Type in your answer below (e.g. “a, b, d”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return PRE_QUIZ_Q5

def pre_quiz_end(update, context):

    first_name = update.message.chat.first_name
    pre_quiz_q5 = update.message.text
    chat_id = update.message.chat_id
    pre_quiz_dict = {'pre_quiz_q5': pre_quiz_q5}
    db.update_quiz(pre_quiz_dict, chat_id)

    message = f"""That is all {first_name}! Thank you for completing the baseline knowledge assessment. I am sure that I can help you to build on your existing knowledge on long-term BPV. Let's get started! """

    keyboard = [['Get Started']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return MAIN_MENU_RETURN
