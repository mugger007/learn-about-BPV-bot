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

def bp_measuring_practices(update, context):

    first_name = update.message.chat.first_name
    chat_id = update.message.chat_id

    columns_check_1 = ['bp_measuring_practices_status_1a', 'bp_measuring_practices_status_1b', 'bp_measuring_practices_status_1c', 'bp_measuring_practices_status_1d']
    results_check_1 = db.get_column_status(columns_check_1, chat_id)
    if 'INCOMPLETE' not in results_check_1:
        column_keys = ['bp_measuring_practices_status_1']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_2 = ['bp_measuring_practices_status_2a', 'bp_measuring_practices_status_2b', 'bp_measuring_practices_status_2c', 'bp_measuring_practices_status_2d']
    results_check_2 = db.get_column_status(columns_check_2, chat_id)
    if 'INCOMPLETE' not in results_check_2:
        column_keys = ['bp_measuring_practices_status_2']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns = ['bp_measuring_practices_status_1', 'bp_measuring_practices_status_2']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message_1 = f"""Indeed {first_name}, BP measurement errors are considered as a factor affecting long-term BPV.
    \nThis is especially so, as home BP monitoring (HBPM) is often a more practical approach in clinical practice [4] and increasingly used as an out-of-office measurement method in Singapore [5]."""

    message_2 = """Hence, it is important to check if the patient is
    \n(i) using the appropriate HBPM device, and
    \n(ii) familiar with the instructions on HBPM procedures"""

    message_3 = f"""Which scenario will you like to explore?
    \n1. Ask about the HBPM device used --- [{results[0]}]
    \n2. Ask about the HBPM procedures --- [{results[1]}]
    \n---
    \n3. Back to list of common factors affecting long-term BPV"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES

def bp_measuring_practices_1(update, context):

    chat_id = update.message.chat_id

    columns_check_1a = ['bp_measuring_practices_1aa_status', 'bp_measuring_practices_1ab_status']
    results_check_1a = db.get_column_status(columns_check_1a, chat_id)
    if 'INCOMPLETE' not in results_check_1a:
        column_keys = ['bp_measuring_practices_status_1a']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_1b = ['bp_measuring_practices_1ba_status', 'bp_measuring_practices_1bb_status']
    results_check_1b = db.get_column_status(columns_check_1b, chat_id)
    if 'INCOMPLETE' not in results_check_1b:
        column_keys = ['bp_measuring_practices_status_1b']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns = ['bp_measuring_practices_status_1a', 'bp_measuring_practices_status_1b', 'bp_measuring_practices_status_1c', 'bp_measuring_practices_status_1d']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message = f"""Which scenario will you like to explore?
    \n1. Verify the use of automated validated device --- [{results[0]}]
    \n2. Verify if patient is using a monitor that has automated storage of readings in memory --- [{results[1]}]
    \n3. Verify use of appropriate cuff size to fit the arm --- [{results[2]}]
    \n4. Verify that patient is measuring BPs on the same arm --- [{results[3]}]
    \n---
    \n5. Back to key categories of BP measurement errors"""

    keyboard = [['1'], ['2'], ['3'], ['4'], ['5']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_1

def bp_measuring_practices_2(update, context):

    chat_id = update.message.chat_id

    columns_check_2a = ['bp_measuring_practices_status_2aa', 'bp_measuring_practices_status_2ab']
    results_check_2a = db.get_column_status(columns_check_2a, chat_id)
    if 'INCOMPLETE' not in results_check_2a:
        column_keys = ['bp_measuring_practices_status_2a']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_2b = ['bp_measuring_practices_status_2ba', 'bp_measuring_practices_status_2bb', 'bp_measuring_practices_status_2bc']
    results_check_2b = db.get_column_status(columns_check_2b, chat_id)
    if 'INCOMPLETE' not in results_check_2b:
        column_keys = ['bp_measuring_practices_status_2b']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_2d = ['bp_measuring_practices_status_2da', 'bp_measuring_practices_status_2db']
    results_check_2d = db.get_column_status(columns_check_2d, chat_id)
    if 'INCOMPLETE' not in results_check_2d:
        column_keys = ['bp_measuring_practices_status_2d']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns = ['bp_measuring_practices_status_2a', 'bp_measuring_practices_status_2b', 'bp_measuring_practices_status_2c', 'bp_measuring_practices_status_2d']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message = f"""Which scenario will you like to explore?
    \n1. Verify that patient remains still before BP measurements --- [{results[0]}]
    \n2. Verify that patient sits correctly --- [{results[1]}]
    \n3. Verify that patient has the bottom of the cuff placed directly above the antecubital fossa (bend of the elbow) --- [{results[2]}]
    \n4. Verify that patient takes multiple readings and records all readings accurately --- [{results[3]}]
    \n---
    \n5. Back to key categories of BP measurement errors"""

    keyboard = [['1'], ['2'], ['3'], ['4'], ['5']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2

def bp_measuring_practices_2a(update, context):

    chat_id = update.message.chat_id

    columns_check_2aa = ['bp_measuring_practices_status_2aaa', 'bp_measuring_practices_status_2aab', 'bp_measuring_practices_status_2aac']
    results_check_2aa = db.get_column_status(columns_check_2aa, chat_id)
    if 'INCOMPLETE' not in results_check_2aa:
        column_keys = ['bp_measuring_practices_status_2aa']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns = ['bp_measuring_practices_status_2aa', 'bp_measuring_practices_status_2ab']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message = f"""Which scenario will you like to explore?
    \n1. Verify that patient avoids smoking, caffeinated beverages, or exercise within 30 min before BP measurements --- [{results[0]}]
    \n2. Verify that patient has at least 5 min of quiet rest before BP measurements --- [{results[1]}]
    \n---
    \n3. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2A

def bp_measuring_practices_2aa_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Of course, {first_name}!
    \nWhen it comes to smoking, tobacco smoking has an acute prolonged pressor effect that may cause BP elevation [2]."""

    message_2 = """Click on to find out more about the effects of caffeine!"""

    keyboard = [['What About Caffeine?']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2AA_PART1

def bp_measuring_practices_2aa_part2(update, context):

    message_1 = """For caffeinated beverages, caffeine has been shown to have an acute pressor effect that may cause BP elevation [2]."""

    message_2 = """Click on to find out more about the effects of physical exercise!"""

    keyboard = [['What About Exercise?']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2AA_PART2

def bp_measuring_practices_2aa_part3(update, context):

    chat_id = update.message.chat_id

    columns = ['bp_measuring_practices_status_2aaa', 'bp_measuring_practices_status_2aab', 'bp_measuring_practices_status_2aac']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message_1 = """When it comes to exercise, BP increases during dynamic and static exercise, and that the increase is more pronounced for SBP than for DBP [2]."""

    message_2 = f"""Which scenario will you like to explore?
    \nWhat if patient has been
    \n1. Smoking --- [{results[0]}]
    \n2. Drinking caffeinated beverage --- [{results[1]}]
    \n3. Exercising --- [{results[2]}]
    \nwithin 30 minutes before BP measurements?
    \n---
    \n4. Back to list of other scenarios related to remaining still before BP measurements
    \n5. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2'], ['3'], ['4'], ['5']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2AA_PART3

def bp_measuring_practices_2aaa(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_2aaa']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise patient to avoid smoking for at least 30 min before measurement [2]."""

    message_2 = """Also, recommend smoking cessation, supportive care, and referral to smoking cessation programs. History of tobacco use should be established at each patient visit[2]."""

    message_3 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to patient activities within 30 minutes before BP measurement
    \n2. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_2AA

def bp_measuring_practices_2aab(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_2aab']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise patient to avoid caffeine for at least 30 min before measurement [2]."""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to patient activities within 30 minutes before BP measurement
    \n2. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_2AA

def bp_measuring_practices_2aac(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_2aac']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise patient to avoid exercise for at least 30 min before measurement [2]."""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to patient activities within 30 minutes before BP measurement
    \n2. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_2AA

def bp_measuring_practices_2ab_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Of course, {first_name}!
    \nDaytime ambulatory SBP is significantly higher that that obtained after 5 min of seated rest [13]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient has less than 5 min of quiet rest before BP measurement?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2AB_PART1

def bp_measuring_practices_2ab_part2(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_2ab']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise patient to have at least 5 min of quiet rest before BP measurements [4]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. Back to list of other scenarios related to remaining still before BP measurements
    \n2. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2AB_PART2

def bp_measuring_practices_2b(update, context):

    chat_id = update.message.chat_id

    columns = ['bp_measuring_practices_status_2ba', 'bp_measuring_practices_status_2bb', 'bp_measuring_practices_status_2bc']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message = f"""Which scenario will you like to explore?
    \n1. Verify that patient sits with back straight and supported (e.g. on a straight-backed dining chair, rather than a sofa) --- [{results[0]}]
    \n2. Verify that patient sits with feet flat on the floor and legs uncrossed --- [{results[1]}]
    \n3. Verify that patient keeps arm supported on a flat surface (such as a table), with the upper arm at heart level --- [{results[2]}]
    \n---
    \n4. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2'], ['3'], ['4']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2B

def bp_measuring_practices_2ba_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Good call, {first_name}!
    \nIf the patient is standing while taking BP measurement, BP could be significantly lower than that in the sitting position [9].
    \nIt could also lead to orthostatic hypotension - defined as a reduction in SBP of ≥20 mmHg or in DBP of ≥10 mmHg within 3 min of standing [4]."""

    message_2 = """Click on the button below to find out more about the effects of being in a supine position while taking BP measurement!"""

    keyboard = [['What About Supine?']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2BA_PART1

def bp_measuring_practices_2ba_part2(update, context):

    message_1 = """If the patient is in a supine position while taking BP measurement, BP could be significantly higher than that in the sitting position [9]."""

    message_2 = f"""Select the button below to explore the scenario:
    \n1. What if patient has been in an inappropriate position while taking BP measurements?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2BA_PART2

def bp_measuring_practices_2ba_part3(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_2ba']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise and demonstrate to patient on sitting with back straight and supported when taking BP measurements [4]."""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to sitting posture for BP measurement
    \n2. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_2B

def bp_measuring_practices_2bb_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Good call, {first_name}!
    \nIf the patient has the legs crossed or ankle crossed over the knee while taking BP measurement, BP could be significantly higher than that if the patient has the legs flat on the floor [10, 11]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient's legs are in an inappropriate position while taking BP measurements?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2BB_PART1

def bp_measuring_practices_2bb_part2(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_2bb']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise and demonstrate to patient on sitting with feet flat on the floor and legs uncrossed [4]."""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to sitting posture for BP measurement
    \n2. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_2B

def bp_measuring_practices_2bc_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Good call, {first_name}!
    \nIf the patient's upper arm is raised above the heart level, it can lead to an underestimation of BP.
    \nIf the patient's upper arm is below the heart level, it could lead to an overestimation of BP. The magnitude of this error can be as great as 10 mm Hg for SBP and DBP [12]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient's upper arm is in an inappropriate position while taking BP measurements?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2BC_PART1

def bp_measuring_practices_2bc_part2(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_2bc']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise and demonstrate to patient on keeping arm supported on a flat surface, with the upper arm at heart level [4]."""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to sitting posture for BP measurement
    \n2. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_2B

def bp_measuring_practices_2c_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Good call, {first_name}!
    \nIncorrect cuff positioning can lead to a systematic overestimation of BP when the cuff is too small in relation to arm circumference [15]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient's cuff positioning is incorrect?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2C_PART1

def bp_measuring_practices_2c_part2(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_2c']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise and demonstrate to patient to place the bottom of the cuff directly above the antecubital fossa (bend of the elbow) [4]."""

    message_2 = """Click on the button below to go back to list of common HBPM procedure related factors affecting BP measurement."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2C_PART2

def bp_measuring_practices_2d(update, context):

    chat_id = update.message.chat_id

    columns = ['bp_measuring_practices_status_2da', 'bp_measuring_practices_status_2db']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message = f"""Which scenario would you like to explore?
    \n1. Verify that patient takes at least 2 readings 1 min apart in morning before taking medications and in evening before supper --- [{results[0]}]
    \n2. Verify that patient has brought along the monitor with built-in memory for their clinic appointments --- [{results[1]}]
    \n---
    \n3. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2D

def bp_measuring_practices_2da_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Indeed, {first_name}!
    \nThe 1 min interval between home BP readings gives a closer agreement with the daytime average BP than that of a shorter interval [14]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient does not take BP readings at least 1 min apart at the recommended timings?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2DA_PART1

def bp_measuring_practices_2da_part2(update, context):

    message_1 = """Advise patient to takes at least 2 readings 1 min apart in morning before taking medications and in evening before supper [4]."""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2DA_PART2

def bp_measuring_practices_2da_part3(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_2da']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Optimally, the patient should measure and record BP daily.
    \nIdeally, obtain weekly BP readings in the first 2 weeks after a change in the treatment regimen and during the week before a clinic visit [4]."""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to taking multiple BP readings and recording accurately
    \n2. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_2D

def bp_measuring_practices_2db_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Indeed, {first_name}!
    \nThe measurements tend to have lower accuracy if values are recorded manually than stored electronically [7], especially if patient is an elderly or cognitively impaired [8]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient has not brought along the BP monitor?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_2DB_PART1

def bp_measuring_practices_2db_part2(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_2db']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Request patient to bring the BP monitor to the clinic before further assessment.
    \nBP should be based on an average of readings on at least 2 occasions for clinical decision making [4]"""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to taking multiple BP readings and recording accurately
    \n2. Back to list of common HBPM procedure related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_2D

def bp_measuring_practices_1a_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Indeed, {first_name}!
    \nUse of auscultatory devices (mercury, aneroid, or other) is not generally useful for HBPM because patients rarely master the technique required for measurement of BP with auscultatory devices, hence leading to inaccurate measurements [4]"""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_1A_PART1

def bp_measuring_practices_1a_part2(update, context):

    chat_id = update.message.chat_id

    columns = ['bp_measuring_practices_1aa_status', 'bp_measuring_practices_1ab_status']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message_1 = """Patients are advised to only use BP devices that have been confirmed to be validated for accuracy, otherwise measurements might be inaccurate [6]."""

    message_2 = f"""Which scenario will you like to explore?
    \n1. What if patient is not using an automated validated device? --- [{results[0]}]
    \n2. What if I cannot verify the use of automated validated device? --- [{results[1]}]
    \n---
    \n3. Back to list of common HBPM device related factors affecting BP measurement"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_1A_PART2

def bp_measuring_practices_1aa(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_1aa']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise patient to switch to an automated validated device [4]."""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to the use of an automated validated device
    \n2. Back to list of common HBPM device related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_1A

def bp_measuring_practices_1ab(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_1ab']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Request patient to bring the BP monitor to the clinic before further assessment."""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to the use of an automated validated device
    \n2. Back to list of common HBPM device related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_1A

def bp_measuring_practices_1b(update, context):

    first_name = update.message.chat.first_name
    chat_id = update.message.chat_id

    columns = ['bp_measuring_practices_1ba_status', 'bp_measuring_practices_1bb_status']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message_1 = f"""Indeed, {first_name}!
    \nThe measurements tend to have a greater accuracy if values are stored electronically than recorded manually [7], especially if patient is an elderly or cognitively impaired [8]."""

    message_2 = f"""Which scenario will you like to explore?
    \n1. What if patient is using a monitor that has automated storage of readings in memory? --- [{results[0]}]
    \n2. What if patient is not using a monitor that has automated storage of readings in memory? --- [{results[1]}]
    \n---
    \n3. Back to list of common HBPM device related factors affecting BP measurement"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_1B

def bp_measuring_practices_1ba(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_1ba']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Request patient to bring the HBPM monitor to the clinic to verify the readings in the memory before further assessment."""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to a monitor with automated storage of readings
    \n2. Back to list of common HBPM device related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_1B

def bp_measuring_practices_1bb(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_1bb']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise patient to switch to a monitor that has automated storage of readings in memory [4]."""

    message_2 = f"""What will you like to do next?
    \n1. Back to list of other scenarios related to a monitor with automated storage of readings
    \n2. Back to list of common HBPM device related factors affecting BP measurement"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_1B

def bp_measuring_practices_1c_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Indeed, {first_name}!
    \nIf the cuffs used are too small relative to the arm circumference, it can result in a spurious elevation of BP [2]."""

    message_2 = f"""Click the button below to explore the scenario:
    \n1. What if patient is using a monitor that has automated storage of readings in memory?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_1C_PART1

def bp_measuring_practices_1c_part2(update, context):

    message_1 = """Advise patient to use an appropriate cuff size for the arm circumference - use a standard bladder cuff (12-13 cm wide and 35 cm long) for most patients, but larger and smaller cuffs are available for larger (arm circumference >32 cm) and thinner arms, respectively [2]."""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_1C_PART2

def bp_measuring_practices_1c_part3(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_1c']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """A thigh cuff should be used for extremely large arms [7]."""

    message_2 = """Click on the button below to go back to list of common HBPM device related factors affecting BP measurement."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_1

def bp_measuring_practices_1d_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Indeed, {first_name}!
    \nThere could be a difference in BP between arms, ideally established by simultaneous measurement. The arm with the higher BP values should be used for all subsequent measurements [2]."""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_1D_PART1

def bp_measuring_practices_1d_part2(update, context):

    message_1 = """Also, between-arm SBP difference of >15 mmHg is suggestive of atheromatous disease and is associated with an increased CV risk [2]."""

    message_2 = f"""Select the button below to explore the scenario:
    \n1. What if patient is not measuring BP on same arm?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_1D_PART2

def bp_measuring_practices_1d_part3(update, context):

    chat_id = update.message.chat_id

    column_keys = ['bp_measuring_practices_status_1d']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise patient to measure all subsequent BP using the arm with the higher BP values [2]."""

    message_2 = """Click on the button below to go back to list of common HBPM device related factors affecting BP measurement."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return BP_MEASURING_PRACTICES_RETURN_1
