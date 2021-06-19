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

column_keys = ['bp_measuring_practices_status', 'treatment_adherence_status', 'lifestyle_status', 'medication_hist_status', 'patient_obs_status', 'patient_hist_status', 'other_factors_status', 'bp_measuring_practices_status_1', 'bp_measuring_practices_status_2', 'bp_measuring_practices_status_1a', 'bp_measuring_practices_status_1b', 'bp_measuring_practices_status_1c', 'bp_measuring_practices_status_1d', 'bp_measuring_practices_status_2a', 'bp_measuring_practices_status_2b', 'bp_measuring_practices_status_2c', 'bp_measuring_practices_status_2d', 'bp_measuring_practices_status_2aa', 'bp_measuring_practices_status_2ab', 'bp_measuring_practices_status_2aa', 'bp_measuring_practices_status_2ab', 'bp_measuring_practices_status_2aaa', 'bp_measuring_practices_status_2aab', 'bp_measuring_practices_status_2aac', 'bp_measuring_practices_status_2ba', 'bp_measuring_practices_status_2bb', 'bp_measuring_practices_status_2bc', 'bp_measuring_practices_status_2da', 'bp_measuring_practices_status_2db', 'bp_measuring_practices_1aa_status', 'bp_measuring_practices_1ab_status', 'bp_measuring_practices_1ba_status', 'bp_measuring_practices_1bb_status', 'lifestyle_status_a', 'lifestyle_status_b', 'lifestyle_status_c', 'lifestyle_status_d', 'lifestyle_status_e', 'lifestyle_status_f', 'lifestyle_status_ca', 'lifestyle_status_cb', 'lifestyle_status_cc', 'lifestyle_status_da', 'lifestyle_status_db', 'treatment_adherence_status_a', 'treatment_adherence_status_b', 'medication_hist_status_a', 'medication_hist_status_b', 'medication_hist_status_c', 'medication_hist_status_d', 'medication_hist_status_e', 'medication_hist_status_f', 'medication_hist_status_g', 'medication_hist_status_h', 'other_factors_status_a', 'other_factors_status_b', 'other_factors_status_ba', 'other_factors_status_bb', 'patient_obs_status_a', 'patient_obs_status_b', 'patient_obs_status_c', 'patient_obs_status_d', 'patient_obs_status_1', 'patient_obs_status_2', 'patient_review_status_a', 'patient_review_status_b', 'patient_review_status_c', 'patient_review_status_d', 'patient_review_status_1', 'patient_review_status_2']

column_values = 'INCOMPLETE'

column_values_dict = {}
for i in column_keys:
        column_values_dict[i] = column_values

db = DBHelper()

def intro_ques(update, context):

    first_name = update.message.chat.first_name
    chat_id = update.message.chat_id
    try:
        db.add_user(chat_id)
        db.update_column_status(column_values_dict, chat_id)
    except Exception as e:
        print("User %s is already created.", user.first_name)

    message = f"""Hi {first_name}, it is great to have you around!
    \nJust to know you better, which stage of your pharmacy education are you currently at?
    \n1. Completed pre-registration training
    \n2. Completed community rotation but not industry rotation of PECT
    \n3. Completed industry rotation but not community rotation of PECT"""

    keyboard = [['1'], ['2'], ['3']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)
    update.message.reply_text(message, reply_markup = reply_markup)

    return INTRO_QUES

def intro_end(update, context):

    user_education = update.message.text
    chat_id = update.message.chat_id
    db.add_user_education(user_education, chat_id)

    message_1 = """Since you are new here, I would recommend you to start with '1. Learn more about long-term BPV'.
    \nEven if you are confident of your knowledge, it will definitely be a great refresher!"""

    message_2 = """Welcome to the Main Menu!
    \nWhat will you like to explore today?
    \n1. Learn more about long-term BPV
    \n2. Fact of the day
    \n3. Help"""

    keyboard = [['1'], ['2'], ['3']]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return MAIN_MENU
