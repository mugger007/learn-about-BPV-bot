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

def post_quiz_part1(update, context):

    first_name = update.message.chat.first_name

    message = f"""Awesome, {first_name}, you can now put your knowledge to the test! You will be identifying what are the factors affecting the patient's long-term BPV and then managing for these factors."""

    keyboard = [['Get Started'], ['Main Menu']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return POST_QUIZ_PART1

def post_quiz_part2(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Awesome, {first_name}!
    \nAs this will be an assessment of what you have learned using Dorcas, do complete it to the best of your abilities!"""

    message_2 = """Before you look at the patient case, let us start off with some general questions on factors affecting long-term BPV."""

    message_3 = """Dorcas wishes you all the best!"""

    keyboard = [["Let's Go!"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return POST_QUIZ_PART2

def post_quiz_q1(update, context):

    message_1 = """1. Which factor(s) can affect a patient's long-term BPV?
    \na: Smoking 15 minutes before taking BP measurement
    \nb: Binge drinking alcohol
    \nc: Change in chemoreceptive/cardiopulmonary reflexes
    \nd: Taking NSAIDs"""

    message_2 = """Type in your answer below (e.g. “a, b, d”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return POST_QUIZ_Q1

def post_quiz_q2(update, context):

    post_quiz_q1 = update.message.text
    chat_id = update.message.chat_id
    post_quiz_dict = {'post_quiz_q1': post_quiz_q1}
    db.update_quiz(post_quiz_dict, chat_id)

    message_1 = """2. For a hypertensive patient who has an elevated BP after starting a treatment regimen on NSAIDs for frequent headache, what would be the appropriate management plan(s)?
    \na. Avoid excessive use of NSAID
    \nb. Consider increasing the dosage of the patient's antihypertensive(s)
    \nc. Consider well-tolerated therapeutic alternatives (e.g., simple analgesics, physical therapy)
    \nd. Continue monitoring BP"""

    message_2 = """Type in your answer below (e.g. “a, b, d”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return POST_QUIZ_Q2

def post_quiz_q3(update, context):

    post_quiz_q2 = update.message.text
    chat_id = update.message.chat_id
    post_quiz_dict = {'post_quiz_q2': post_quiz_q2}
    db.update_quiz(post_quiz_dict, chat_id)

    message = """3. When a patient has his/her ankle crossed over the knee while taking BP measurement, how would that affect his BP readings? Select your answer below .
    \na. It could lead to an underestimation of BP (i.e. lower than actual BP)
    \nb. It could lead to an overestimation of BP (i.e. higher than actual BP)
    \nc. It does not affect the BP readings"""

    keyboard = [['a'], ['b'], ['c']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return POST_QUIZ_Q3

def post_quiz_q4_intro1(update, context):

    first_name = update.message.chat.first_name
    post_quiz_q3 = update.message.text
    chat_id = update.message.chat_id
    post_quiz_dict = {'post_quiz_q3': post_quiz_q3}
    db.update_quiz(post_quiz_dict, chat_id)

    message = f"""Thank you, {first_name}, for completing the general questions, now let us look at the patient information."""

    keyboard = [['Patient Information']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return POST_QUIZ_Q4_INTRO1

def post_quiz_q4_intro2(update, context):

    message = """Kent is a 45-year-old male diagnosed with hypertension. He also has hyperlipidaemia and type 2 diabetes. His office/clinic BP today is 124/72 mmHg. Kent feels well, except for the occasional runny and blocked nose that he has been experiencing since his last visit. He also reports that he has been experiencing some trouble falling asleep, likely due to the increase in workload recently. As a result of the increased workload, he has also been drinking more often, including up to 6 cans of beer a day for several days in a week. His average HPBM readings for the past week was 136/88 mmHg."""

    keyboard = [['More Information']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return POST_QUIZ_Q4_INTRO2

def post_quiz_q4_intro3(update, context):

    message = """Social History (SH):
    \n- Works as an engineer in a MNC
    \nPast Medical History (PMH):
    \n- T2DM x 2 years
    \n- HLD x 2 years
    \n- HTN x 1 month
    \nMedication History:
    \n- Amlodipine 5 mg OD
    \n- Atorvastatin 20 mg OD (increased from 10 mg OD one year ago)
    \n- Glipizide 20 mg BD (increased from 10 mg BD one year ago)
    \n- Metformin 850 mg TDS
    \n- Clarityn-D 24 Hour 1 tab OD PRN
    \nAllergies:
    \n- Aspirin (nausea)"""

    keyboard = [['Continue to Q4']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return POST_QUIZ_Q4_INTRO3

def post_quiz_q4(update, context):

    message_1 = """1. Which factor(s) could have caused the significant BP variability in Kent?
    \na. Insomnia
    \nb. Increased dosage of Atorvastatin
    \nc. Binge drinking
    \nd. Taking Clarityn-D"""

    message_2 = """Type in your answer below (e.g. “a, b, d”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return POST_QUIZ_Q4

def post_quiz_q5(update, context):

    post_quiz_q4 = update.message.text
    chat_id = update.message.chat_id
    post_quiz_dict = {'post_quiz_q4': post_quiz_q4}
    db.update_quiz(post_quiz_dict, chat_id)

    message_1 = """2. Based on your answer for Q4, what is/are the appropriate management plan(s) for Kent’s long-term BPV?
    \na. Advise limiting alcohol consumption to 14 units per week and recommend alcohol-free days
    \nb. Increased dosage of Amlodipine
    \nc. Switch to an alternative therapy (e.g., nasal saline) for nasal congestion
    \nd. Refer for sleep disorder therapy
    \ne. Continue to monitor BP"""

    message_2 = """Type in your answer below (e.g. “a, b, d”)"""

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)

    return POST_QUIZ_Q5

def post_quiz_end(update, context):

    post_quiz_q5 = update.message.text
    chat_id = update.message.chat_id
    post_quiz_dict = {'post_quiz_q5': post_quiz_q5}
    db.update_quiz(post_quiz_dict, chat_id)

    #message = f"""Wonder what happens to Kent next?
    #\nClick on the button below to find out!"""

    #keyboard = [['Yes']]"""

    message = f"""Good job on completing the assessment!"""

    keyboard = [['Main Menu']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return MAIN_MENU_RETURN
