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

def other_factors(update, context):

    first_name = update.message.chat.first_name
    chat_id = update.message.chat_id

    #check if other_factors_status_b is COMPLETED
    columns_check = ['other_factors_status_ba', 'other_factors_status_bb']
    results_check = db.get_column_status(columns_check, chat_id)
    if 'INCOMPLETE' not in results_check:
        column_keys = ['other_factors_status_b']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns = ['other_factors_status_a', 'other_factors_status_b']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message_1 = f"""Of course, {first_name}!
    \nIf all the other factors (e.g. secondary causes of hypertension, poor adherence to treatment) have been excluded, some other factors can be considered."""

    message_2 = f"""Which scenario will you like to explore?
    \n1. Which scenario will you like to explore? --- [{results[0]}]
    \n2. Between the HBPM readings and the office/clinic BP --- [{results[1]}]
    \n---
    \n3. Back to list of common factors affecting long-term BPV."""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return OTHER_FACTORS

def other_factors_a_part1(update, context):

    message_1 = """The elevated BP could be related to an increasing risk of cardiovascular disease [7]."""

    message_2 = """Click on the button below to find out how to manage it!"""

    keyboard = [['How to Manage?']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return OTHER_FACTORS_A_PART1

def other_factors_a_part2(update, context):

    message_1 = """It is recommended that the patient has a routine clinical evaluation which includes the following [7]:
    \n1. Clinical and family history
    \n2. Full standard physical examination
    \n3. Laboratory investigations, including:
    \na) Urine analysis: Dipstick for hematuria/albumin, microscopic examination, and test for albuminuria
    \nb) Measurement of serum concentrations of electrolytes, creatinine, urea, fasting glucose and fasting lipids
    \nc) Computation of eGFR
    \n4. ECG"""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return OTHER_FACTORS_A_PART2

def other_factors_a_part3(update, context):

    chat_id = update.message.chat_id

    column_keys = ['other_factors_status_a']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Also consider the diagnosis of hypertension, but it should only be based on multiple BP measurements taken on several separate occasions [7]."""

    message_2 = """Click on the button below to go back to list of other factors affecting BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return OTHER_FACTORS_RETURN

def other_factors_b(update, context):

    chat_id = update.message.chat_id

    columns = ['other_factors_status_ba', 'other_factors_status_bb']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message = f"""Which scenario will you like to explore?
    \nThe current office/clinic BP readings are significantly:
    \n1. Higher --- [{results[0]}]
    \n2. Lower --- [{results[1]}]
    \n---
    \n3. Back to list of common factors affecting long-term BPV."""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return OTHER_FACTORS_B

def other_factors_ba_part1(update, context):

    message_1 = """Consider the white coat effect, which is characterized by elevated office BP but normal readings when measured outside the office with HBPM [4].
    \nWhen measured in clinic or office, the alerting response in about 1 in 4 patients can result in exaggerated BP [6].
    \nIt is usually considered clinically significant when office SBP/DBPs are >20/10 mm Hg higher than home SBP/DBPs) [4]."""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return OTHER_FACTORS_BA_PART1

def other_factors_ba_part2(update, context):

    message_1 = """It is more common with increasing age, in women, and in non-smokers [4]."""

    message_2 = """It has been implicated in 'pseudo-resistant hypertension' and results in an underestimation of office BP control rates [4]."""

    message_3 = """Click on the button below to find out how to manage the white coat effect!"""

    keyboard = [['How to Manage?']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return OTHER_FACTORS_BA_PART2

def other_factors_ba_part3(update, context):

    message_1 = """Because a diagnosis of white coat hypertension may result in a decision not to treat or intensify treatment in patients with elevated office BP readings, confirmation of BP control by HBPM provides added support for this decision [4]."""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return OTHER_FACTORS_BA_PART3

def other_factors_ba_part4(update, context):

    chat_id = update.message.chat_id

    column_keys = ['other_factors_status_ba']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """In white coat hypertensive patients, it is recommended to implement lifestyle changes aimed at reducing CV risk as well as regular follow-up with periodic out-of-office (e.g. HBPM, ABPM) BP monitoring [2]."""

    message_2 = """What will you like to do next?
    \n1. Back to list of other scenarios related to office/clinic BP
    \n2. Back to list of other factors affecting BP"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return OTHER_FACTORS_RETURN_B

def other_factors_bb_part1(update, context):

    message_1 = """Consider masked hypertension, which is characterized by office readings suggesting normal BP but out-of-office (e.g. HBPM) readings that are consistently above normal [4]."""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return OTHER_FACTORS_BB_PART1

def other_factors_bb_part2(update, context):

    message_1 = """Prevalence is greater in younger people, men, smokers, and those with higher levels of physical activity, alcohol consumption, anxiety, and job stress [4]."""

    message_2 = """The risk of CVD and all-cause mortality in persons with masked hypertension is similar to that noted in those with sustained hypertension and about twice as high as the corresponding risk in their normotensive counterparts.
    \nThe prevalence of masked hypertension increases with higher office BP readings [4]."""

    message_3 = """Click on the button below to find out how to manage masked hypertension!"""

    keyboard = [['How to Manage?']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return OTHER_FACTORS_BB_PART2

def other_factors_bb_part3(update, context):

    message_1 = """In adults being treated for hypertension with elevated HBPM readings suggestive of masked uncontrolled hypertension, confirmation of the diagnosis by ABPM might be reasonable before intensification of antihypertensive drug treatment [4]."""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return OTHER_FACTORS_BB_PART3

def other_factors_bb_part4(update, context):
    
    chat_id = update.message.chat_id

    column_keys = ['other_factors_status_bb']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """In masked hypertension, lifestyle changes are recommended to reduce CV risk, with regular follow-up, including periodic out-of-office (e.g. HBPM, ABPM) BP monitoring [2]."""

    message_2 = """What will you like to do next?
    \n1. Back to list of other scenarios related to office/clinic BP
    \n2. Back to list of other factors affecting BP"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return OTHER_FACTORS_RETURN_B
