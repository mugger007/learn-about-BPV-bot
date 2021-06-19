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

def patient_review(update, context):

    first_name = update.message.chat.first_name
    chat_id = update.message.chat_id

    columns = ['patient_review_status_a', 'patient_review_status_b', 'patient_review_status_c', 'patient_review_status_d']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message_1 = f"""Of course, {first_name}!
    \nThis could help to check if patient has been diagnosed with a common cause of secondary hypertension or to identify symptoms indicative of a common cause of secondary hypertension [2]."""

    message_2 = f"""Which common cause of secondary hypertension will you like to explore?
    \n1. Obstructive sleep apnea --- [{results[0]}]
    \n2. Renal parenchymal disease --- [{results[1]}]
    \n3. Primary aldosteronism [Endocrine] --- [{results[2]}]
    \n4. Atherosclerotic renovascular disease [Renovascular] --- [{results[3]}]
    \n---
    \n5. Back to list of common factors affecting long-term BPV."""

    keyboard = [['1'], ['2'], ['3'], ['4'], ['5']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return PATIENT_REVIEW

def patient_review_a(update, context):

    chat_id = update.message.chat_id

    columns = ['patient_review_status_1', 'patient_review_status_2']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    column_keys = ['patient_review_status_a']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """The symptoms of obstructive sleep apnea include [4]:
    \n- Snoring
    \n- Fitful sleep
    \n- Breathing pauses during sleep"""

    message_2 = f"""Which scenario will you like to explore?
    \n1. What if patient is not diagnosed but has signs and symptoms of a secondary cause of hypertension? --- [{results[0]}]
    \n2. What if patient is diagnosed with a secondary cause of hypertension, or has a positive screening test? --- [{results[1]}]
    \n---
    \n3. Back to list of other causes of secondary hypertension"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return PATIENT_REVIEW_NEXT

def patient_review_b(update, context):

    chat_id = update.message.chat_id

    columns = ['patient_review_status_1', 'patient_review_status_2']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    column_keys = ['patient_review_status_b']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """The signs of renal parenchymal disease include [2, 4]:
    \n- Diabetes
    \n- Hematuria
    \n- Proteinuria
    \n- Nocturia
    \n- Anemia
    \n- Renal mass in adult polycystic CKD"""

    message_2 = f"""Which scenario will you like to explore?
    \n1. What if patient is not diagnosed but has signs and symptoms of a secondary cause of hypertension? --- [{results[0]}]
    \n2. What if patient is diagnosed with a secondary cause of hypertension, or has a positive screening test? --- [{results[1]}]
    \n---
    \n3. Back to list of other causes of secondary hypertension"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return PATIENT_REVIEW_NEXT

def patient_review_c(update, context):

    chat_id = update.message.chat_id

    columns = ['patient_review_status_1', 'patient_review_status_2']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    column_keys = ['patient_review_status_c']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """The symptoms of primary aldosteronism include [4]:
    \n- Hypokalemia (spontaneous or diuretic induced)
    \n- Arrhythmias (with hypokalemia); especially atrial fibrillation"""

    message_2 = f"""Which scenario will you like to explore?
    \n1. What if patient is not diagnosed but has signs and symptoms of a secondary cause of hypertension? --- [{results[0]}]
    \n2. What if patient is diagnosed with a secondary cause of hypertension, or has a positive screening test? --- [{results[1]}]
    \n---
    \n3. Back to list of other causes of secondary hypertension"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return PATIENT_REVIEW_NEXT

def patient_review_d(update, context):

    chat_id = update.message.chat_id

    columns = ['patient_review_status_1', 'patient_review_status_2']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    column_keys = ['patient_review_status_d']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """The symptoms of atherosclerotic renovascular disease include [2]:
    \n- Widespread atherosclerosis (especially PAD)
    \n- Diabetes
    \n- Smoking
    \n- Recurrent flash pulmonary edema"""

    message_2 = f"""Which scenario will you like to explore?
    \n1. What if patient is not diagnosed but has signs and symptoms of a secondary cause of hypertension? --- [{results[0]}]
    \n2. What if patient is diagnosed with a secondary cause of hypertension, or has a positive screening test? --- [{results[1]}]
    \n---
    \n3. Back to list of other causes of secondary hypertension"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return PATIENT_REVIEW_NEXT

def patient_review_scenario(update, context):

    chat_id = update.message.chat_id

    columns = ['patient_review_status_1', 'patient_review_status_2']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)
    message = f"""Which scenario will you like to explore?
    \n1. What if patient is not diagnosed but has signs and symptoms of a secondary cause of hypertension? --- [{results[0]}]
    \n2. What if patient is diagnosed with a secondary cause of hypertension, or has a positive screening test? --- [{results[1]}]
    \n---
    \n3. Back to list of other causes of secondary hypertension"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return PATIENT_REVIEW_NEXT

def patient_review_1(update, context):

    chat_id = update.message.chat_id

    column_keys = ['patient_review_status_1']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Screening should be considered after confirming that BP is elevated with ABPM [2]."""

    message_2 = """What will you like to do next?
    \n1. Back to list of other scenarios related to a secondary cause of hypertension
    \n2. Back to list of other causes of secondary hypertension"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return PATIENT_REVIEW_RETURN

def patient_review_2(update, context):

    chat_id = update.message.chat_id

    column_keys = ['patient_review_status_2']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Patient should be referred for specialist evaluation as intervention is still important because it will often result in much better BP control with less medication [2]."""

    message_2 = """What will you like to do next?
    \n1. Back to list of other scenarios related to a secondary cause of hypertension
    \n2. Back to list of other causes of secondary hypertension"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return PATIENT_REVIEW_RETURN
