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

def treatment_adherence_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Of course, {first_name}!
    \nPoor adherence to prescribed medicines can lead to clinically significant elevations in BP [16] and is a frequent cause of pseudo-resistant hypertension, occurring in ≤50% of patients assessed by therapeutic drug monitoring, and is directly related to the number of tablets prescribed [2]."""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return TREATMENT_ADHERENCE_PART1

def treatment_adherence_part2(update, context):

    chat_id = update.message.chat_id

    columns = ['treatment_adherence_status_a', 'treatment_adherence_status_b']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message_1 = """There is also growing evidence that it is the most important cause of poor BP control.
    \nNon-adherence to antihypertensive therapy correlates with higher risk of CV events [2]."""

    message_2 = """In any case, it is recommended to ensure medication adherence at every visit [7]."""

    message_3 = f"""What will you like to explore?
    \n1. Questions to ask patient on medication adherence --- [{results[0]}]
    \n2. Possible interventions to improve medication adherence --- [{results[1]}]
    \n---
    \n3. Back to list of common factors affecting long-term BPV."""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return TREATMENT_ADHERENCE_PART2

def treatment_adherence_a(update, context):

    chat_id = update.message.chat_id

    column_keys = ['treatment_adherence_status_a']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """These questions can include:
    \n- Do you have all of the medications you were prescribed? (and probe for barriers such as cost or confusion) [17]
    \n- Do you understand why you are taking them? [17]
    \n- How often do you miss a dose of the medication? [8]
    \n- Do any of your medications make you sick? [17]
    \n- If you feel worse, do you stop taking them? [17]
    \n- If you feel better, do you stop taking them? [17]"""

    message_2 = """Click on the button below to go back to list of content related to medication adherence."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return TREATMENT_ADHERENCE_RETURN

def treatment_adherence_b_part1(update, context):

    message_1 = """Do take note that it is important to provide first assess the barrier(s) to adherence and then provide the appropriate resolution to each barrier to adherence [2]."""

    message_2 = """Click on the button below to find out more about the possible interventions."""

    keyboard = [['Find Out More']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return TREATMENT_ADHERENCE_B_PART1

def treatment_adherence_b_part2(update, context):

    chat_id = update.message.chat_id

    column_keys = ['treatment_adherence_status_b']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """- Dosing of antihypertensive medication once daily rather than multiple times daily [4]
    \n- Use of combination pills rather than free individual components [4]
    \n- Taking into consideration the effect of treatment on a patient’s budget [2]
    \n- Link drug intake with habits [2]
    \n- Give adherence feedback to patients [2]
    \n- Empowerment of the patient by allowing self-monitoring of BP [2]
    \n- Use pill boxes and other special packaging [2]
    \n- Motivational interviewing [2]
    \n- Provide information on the risks of hypertension and the benefits of treatment, as well as agreeing a treatment strategy to achieve and maintain BP control [2]"""

    message_2 = """Click on the button below to go back to list of content related to medication adherence."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return TREATMENT_ADHERENCE_RETURN
