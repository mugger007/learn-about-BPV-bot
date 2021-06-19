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

def medication_hist(update, context):

    first_name = update.message.chat.first_name
    chat_id = update.message.chat_id

    columns = ['medication_hist_status_a', 'medication_hist_status_b', 'medication_hist_status_c', 'medication_hist_status_d', 'medication_hist_status_e', 'medication_hist_status_f', 'medication_hist_status_g', 'medication_hist_status_h']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message_1 = f"""Of course, {first_name}!
    \nThis is to look out for frequently used medications which may cause elevated BP [2, 4]:"""

    message_2 = f"""Which medication will like to find out about its possible management strategy?
    \n1. Antidepressants --- [{results[0]}]
    \n2. Decongestants --- [{results[1]}]
    \n3. NSAIDs --- [{results[2]}]
    \n4. Oral contraceptives --- [{results[3]}]
    \n5. Immunosuppressants --- [{results[4]}]
    \n6. Stimulant drugs --- [{results[5]}]
    \n7. Atypical antipsychotics --- [{results[6]}]
    \n8. Herbal supplements --- [{results[7]}]
    \n---
    \n9. Back to list of common factors affecting long-term BPV."""

    keyboard = [['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return MED_HIST

def medication_hist_a(update, context):

    chat_id = update.message.chat_id

    column_keys = ['medication_hist_status_a']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Examples include: MAOIs, SNRIs, TCAs"""

    message_2 = """Consider alternative agents (e.g., SSRIs) depending on indication.
    \nAvoid tyramine-containing foods with MAOIs [4]."""

    message_3 = """Click on the button below to go back to list of frequently used medications which may cause elevated BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return MED_HIST

def medication_hist_b(update, context):

    chat_id = update.message.chat_id

    column_keys = ['medication_hist_status_b']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Examples include: phenylephrine, pseudoephedrine"""

    message_2 = """Use for shortest duration possible, and avoid in severe or uncontrolled hypertension.
    \nConsider alternative therapies (e.g. nasal saline, intranasal corticosteroids, antihistamines) as appropriate [4]."""

    message_3 = """Click on the button below to go back to list of frequently used medications which may cause elevated BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return MED_HIST

def medication_hist_c(update, context):

    chat_id = update.message.chat_id

    column_keys = ['medication_hist_status_c']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Examples include: indomethacin, naproxen, piroxicam"""

    message_2 = """Avoid excessive use of NSAID treatment and consider well-tolerated therapeutic alternatives, including simple analgesics and physical therapy.
    \nThe progress of each patient should be monitored by careful BP measurement, particularly during the period of initiation of NSAID therapy [18]."""

    message_3 = """Click on the button below to go back to list of frequently used medications which may cause elevated BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return MED_HIST

def medication_hist_d(update, context):

    chat_id = update.message.chat_id

    column_keys = ['medication_hist_status_d']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Use low-dose (e.g. 20-30 mcg ethinyl estradiol) agents or a progestin-only form of contraception, or consider alternative forms of birth control where appropriate (e.g. barrier, abstinence, IUD).
    \nAvoid use in women with uncontrolled hypertension [4]."""

    message_2 = """Click on the button below to go back to list of frequently used medications which may cause elevated BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return MED_HIST

def medication_hist_e(update, context):

    chat_id = update.message.chat_id

    column_keys = ['medication_hist_status_e']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Examples include: cyclosporine, steroids"""

    message_2 = """Consider converting to tacrolimus, which may be associated with fewer effects on BP, or rapamycin, which has almost no effect on BP [4]."""

    message_3 = """Click on the button below to go back to list of frequently used medications which may cause elevated BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return MED_HIST

def medication_hist_f(update, context):

    chat_id = update.message.chat_id

    column_keys = ['medication_hist_status_f']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Examples include: amphetamine, cocaine, ecstasy"""

    message_2 = """Discontinue, or (only for amphetamines) decrease dose [4]."""

    message_3 = """Click on the button below to go back to list of frequently used medications which may cause elevated BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return MED_HIST

def medication_hist_g(update, context):

    chat_id = update.message.chat_id

    column_keys = ['medication_hist_status_g']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Examples include: clozapine, olanzapine"""

    message_2 = """Discontinue or limit use when possible.
    \nConsider behavior therapy where appropriate.
    \nRecommend lifestyle modification.
    \nConsider alternative agents associated with lower risk of weight gain, diabetes mellitus, and dyslipidemia (e.g. aripiprazole, ziprasidone) [4]."""

    message_3 = """Click on the button below to go back to list of frequently used medications which may cause elevated BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return MED_HIST

def medication_hist_h(update, context):

    chat_id = update.message.chat_id

    column_keys = ['medication_hist_status_h']
    column_values = 'COMPLETED'
    column_values_dict = {}
    for i in column_keys:
            column_values_dict[i] = column_values
    db.update_column_status(column_values_dict, chat_id)

    message_1 = """Examples include: Ma Huang (ephedra), St. John’s wort (with MAO inhibitors, yohimbine)"""

    message_2 = """Avoid use [4]."""

    message_3 = """Click on the button below to go back to list of frequently used medications which may cause elevated BP."""

    keyboard = [['Back']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    return MED_HIST
