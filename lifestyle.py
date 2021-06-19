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

def lifestyle(update, context):

    chat_id = update.message.chat_id

    columns_check_c = ['lifestyle_status_ca', 'lifestyle_status_cb', 'lifestyle_status_cc']
    results_check_c = db.get_column_status(columns_check_c, chat_id)
    if 'INCOMPLETE' not in results_check_c:
        column_keys = ['lifestyle_status_c']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_d = ['lifestyle_status_da', 'lifestyle_status_db']
    results_check_d = db.get_column_status(columns_check_d, chat_id)
    if 'INCOMPLETE' not in results_check_d:
        column_keys = ['lifestyle_status_d']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns = ['lifestyle_status_a', 'lifestyle_status_b', 'lifestyle_status_c', 'lifestyle_status_d', 'lifestyle_status_e', 'lifestyle_status_f']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message = f"""Which scenario will you like to explore?
    \n1. Ask about smoking --- [{results[0]}]
    \n2. Ask about alcohol consumption --- [{results[1]}]
    \n3. Ask about diet --- [{results[2]}]
    \n4. Ask about physical activity --- [{results[3]}]
    \n5. Check on weight --- [{results[4]}]
    \n6. Ask about other lifestyle factors --- [{results[5]}]
    \n---
    \n7. Back to list of common factors affecting long-term BPV"""

    keyboard = [['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE

def lifestyle_a_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Indeed, {first_name}!
    \nTobacco smoking has an acute prolonged pressor effect that may raise daytime ambulatory BP [2]"""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient smokes?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_A_PART1

def lifestyle_a_part2(update, context):

    message_1 = """Advise patient to avoid smoking for at least 30 min before BP measurement [2]."""

    message_2 = """Also, recommend smoking cessation, supportive care, and referral to smoking cessation programs. History of tobacco use should be established at each patient visit [2]."""

    message_3 = """Click on the button below to find out why!"""

    keyboard = [['Why?']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return LIFESTYLE_A_PART2

def lifestyle_a_part3(update, context):

    chat_id = update.message.chat_id

    column_keys = ['lifestyle_status_a']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Cessation of tobacco smoking confers major benefit in terms of BP reduction, as well as avoiding coronary artery disease and other serious systemic disorder [7]."""

    message_2 = """Click on the button below to go back to list of common lifestyle factors affecting BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_RETURN

def lifestyle_b_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Indeed, {first_name}!
    \nThere is a long-established positive linear association between alcohol consumption and BP. Binge drinking can have a strong pressor effect that may cause BP elevation [2]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient consumes alcohol?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_B_PART1

def lifestyle_b_part2(update, context):

    message_1 = """Advise hypertensive men who drink alcohol to limit their consumption to 14 units per week and women to 8 units per week (1 unit is equal to 125 mL of wine or 250 mL of beer) [2]."""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_B_PART2

def lifestyle_b_part3(update, context):

    chat_id = update.message.chat_id

    column_keys = ['lifestyle_status_b']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Recommend alcohol-free days during the week and avoidance of binge drinking [2]."""

    message_2 = """Click on the button below to go back to list of common lifestyle factors affecting BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_RETURN

def lifestyle_c(update, context):

    chat_id = update.message.chat_id

    columns = ['lifestyle_status_ca', 'lifestyle_status_cb', 'lifestyle_status_cc']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message = f"""Which scenario will you like to explore?
    \n1. Ask about coffee consumption --- [{results[0]}]
    \n2. Ask about green or black tea consumption --- [{results[1]}]
    \n3. Ask about dietary sodium intake --- [{results[2]}]
    \n---
    \n4. Back to list of common lifestyle factors affecting BP"""

    keyboard = [['1'], ['2'], ['3'], ['4']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message, reply_markup = reply_markup)

    return LIFESTYLE_C

def lifestyle_ca_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Of course, {first_name}!
    \nCaffeine has been shown to have an acute pressor effect that may cause BP elevation [2]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient consumes coffee?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_CA_PART1

def lifestyle_ca_part2(update, context):

    chat_id = update.message.chat_id

    column_keys = ['lifestyle_status_ca']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Remind patient to avoid caffeine for at least 30 min before BP measurement [2]."""

    message_2 = """What will you like to do next?
    \n1. Back to list of other scenarios related to diet
    \n2. Back to list of common lifestyle factors affecting BP"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_RETURN_C

def lifestyle_cb(update, context):

    first_name = update.message.chat.first_name
    chat_id = update.message.chat_id

    column_keys = ['lifestyle_status_cb']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = f"""Of course, {first_name}!
    \nGreen or black tea consumption may also have a small but significant BP-lowering effect [2]."""

    message_2 = """What will you like to do next?
    \n1. Back to list of other scenarios related to diet
    \n2. Back to list of common lifestyle factors affecting BP"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_RETURN_C


def lifestyle_cc_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Of course, {first_name}!
    \nThere is evidence of a causal relationship between sodium intake and BP, and excessive sodium consumption (>5 g sodium per day, e.g. one small teaspoon of salt per day) has been shown to have a pressor effect and be associated with an increased prevalence of hypertension and the rise in SBP with age [2]."""

    message_2 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_CC_PART1

def lifestyle_cc_part2(update, context):

    message_1 = """Conversely, sodium restriction has been shown to have a BP-lowering effect in many trials [2]."""

    message_2 = """A recent meta-analysis of these trials showed that a reduction of ~1.75 g sodium per day (4.4 g salt/day) was associated with a mean 4.2/2.1 mmHg reduction in SBP/DBP, with a more pronounced effect (-5.4/ -2.8 mmHg) in people with hypertension [2]."""

    message_3 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return LIFESTYLE_CC_PART2

def lifestyle_cc_part3(update, context):

    message_1 = """The BP-lowering effect of sodium restriction is greater in black people, in older patients, and in patients with diabetes, metabolic syndrome, or CKD [2]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if the patient has an excessive sodium intake?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_CC_PART3

def lifestyle_cc_part4(update, context):

    chat_id = update.message.chat_id

    column_keys = ['lifestyle_status_cc']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Strongly recommend salt restriction of up to 5-6 g a day for patient with hypertension [7]."""

    message_2 = """What will you like to do next?
    \n1. Back to list of other scenarios related to diet
    \n2. Back to list of common lifestyle factors affecting BP"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_RETURN_C

def lifestyle_d(update, context):

    first_name = update.message.chat.first_name
    chat_id = update.message.chat_id

    columns = ['lifestyle_status_da', 'lifestyle_status_db']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message_1 = f"""Indeed, {first_name}!
    \nPhysical activity induces an acute rise in BP, especially SBP, followed by a short-lived decline in BP below baseline [2]."""

    message_2 = """A meta-analysis of RCTs has shown that aerobic endurance training, dynamic resistance training, and isometric training reduce resting SBP and DBP by 3.5/2.5, 1.8/3.2, and 10.9/6.2 mmHg, respectively, in general populations [2]."""

    message_3 = f"""Which scenario will you like to explore?
    \n1. What if patient starts exercising or exercises more often? --- [{results[0]}]
    \n2. What if patient stops exercising or exercises less often? --- [{results[1]}]
    \n---
    \n3. Back to list of common lifestyle factors affecting BP"""

    keyboard = [['1'], ['2'], ['3']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return LIFESTYLE_D

def lifestyle_da(update, context):

    chat_id = update.message.chat_id

    column_keys = ['lifestyle_status_da']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise patient to avoid exercise for at least 30 min before measurement [2]."""

    message_2 = """What will you like to do next?
    \n1. Back to list of other scenarios related to physical activity
    \n2. Back to list of common lifestyle factors affecting BP"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_RETURN_D

def lifestyle_db(update, context):

    chat_id = update.message.chat_id

    column_keys = ['lifestyle_status_db']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Recommend patient on regular dynamic (i.e. aerobic) exercise on at least 5 days a week, whether as single or interrupted episodes of 30 minutes or longer [7]."""

    message_2 = """What will you like to do next?
    \n1. Back to list of other scenarios related to physical activity
    \n2. Back to list of common lifestyle factors affecting BP"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_RETURN_D

def lifestyle_e_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Indeed, {first_name}!
    \nReducing weight towards an ideal body weight has been shown to reduce BP [2]."""

    message_2 = """In a meta-analysis, the mean SBP and DBP reductions associated with an average weight loss of 5.1 kg were 4.4 and 3.6 mmHg, respectively [2]."""

    message_3 = """Click on the button below to find out more!"""

    keyboard = [["What's More?"]]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return LIFESTYLE_E_PART1

def lifestyle_e_part2(update, context):

    message_1 = """Being overweight or obesity is associated with high BP, and weight gain is also associated with a rise in BP [4]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient gains weight and/or becomes overweight/obese?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_E_PART2

def lifestyle_e_part3(update, context):

    chat_id = update.message.chat_id

    column_keys = ['lifestyle_status_e']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Unless contraindicated, advise patients to reduce weight to a BMI below 23 kg/m2 and to a waist circumference below 90cm in men, and below 80cm in women (for Asians) [7]."""

    message_2 = """Click on the button below to go back to list of common lifestyle factors affecting BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_RETURN

def lifestyle_f_part1(update, context):

    first_name = update.message.chat.first_name

    message_1 = f"""Indeed, {first_name}!
    \nA rise in BP associated with lifestyle factors, such as a job change requiring travel and meals away from home [4].
    \nAlso, patients with acute pain or distress may experience an acute elevation in BP [2]."""

    message_2 = """Select the button below to explore the scenario:
    \n1. What if patient has other lifestyle factors that could cause BP elevation?"""

    keyboard = [['1']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_F_PART1

def lifestyle_f_part2(update, context):

    chat_id = update.message.chat_id

    column_keys = ['lifestyle_status_f']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Advise patient to mitigate the underlying cause if possible."""

    message_2 = """Click on the button below to go back to list of common lifestyle factors affecting BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return LIFESTYLE_RETURN
