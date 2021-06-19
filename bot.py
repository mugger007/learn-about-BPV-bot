import os
import logging
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

from intro_ques import intro_ques, intro_end
from bpv_refresher import bpv_refresher_part1, bpv_refresher_part2, bpv_refresher_part3, bpv_refresher_part4
from fact_of_the_day import fact_of_the_day
from help import help, help_a_part1, help_a_part2, help_b_part1, help_b_part2, help_c

from bp_measuring_practices import bp_measuring_practices, bp_measuring_practices_1, bp_measuring_practices_2, bp_measuring_practices_2a, bp_measuring_practices_2aa_part1, bp_measuring_practices_2aa_part2, bp_measuring_practices_2aa_part3, bp_measuring_practices_2aaa, bp_measuring_practices_2aab, bp_measuring_practices_2aac, bp_measuring_practices_2ab_part1, bp_measuring_practices_2ab_part2, bp_measuring_practices_2b, bp_measuring_practices_2ba_part1, bp_measuring_practices_2ba_part2, bp_measuring_practices_2ba_part3, bp_measuring_practices_2bb_part1, bp_measuring_practices_2bb_part2, bp_measuring_practices_2bc_part1, bp_measuring_practices_2bc_part2, bp_measuring_practices_2c_part1, bp_measuring_practices_2c_part2, bp_measuring_practices_2d, bp_measuring_practices_2da_part1, bp_measuring_practices_2da_part2, bp_measuring_practices_2da_part3, bp_measuring_practices_2db_part1, bp_measuring_practices_2db_part2,  bp_measuring_practices_1a_part1, bp_measuring_practices_1a_part2, bp_measuring_practices_1aa, bp_measuring_practices_1ab, bp_measuring_practices_1b, bp_measuring_practices_1ba, bp_measuring_practices_1bb, bp_measuring_practices_1c_part1, bp_measuring_practices_1c_part2, bp_measuring_practices_1c_part3, bp_measuring_practices_1d_part1, bp_measuring_practices_1d_part2, bp_measuring_practices_1d_part3
from lifestyle import lifestyle, lifestyle_a_part1, lifestyle_a_part2, lifestyle_a_part3, lifestyle_b_part1, lifestyle_b_part2, lifestyle_b_part3, lifestyle_c, lifestyle_ca_part1, lifestyle_ca_part2, lifestyle_cb, lifestyle_cc_part1, lifestyle_cc_part2, lifestyle_cc_part3, lifestyle_cc_part4, lifestyle_d, lifestyle_da, lifestyle_db, lifestyle_e_part1, lifestyle_e_part2, lifestyle_e_part3, lifestyle_f_part1, lifestyle_f_part2
from medication_hist import medication_hist, medication_hist_a, medication_hist_b, medication_hist_c, medication_hist_d, medication_hist_e, medication_hist_f, medication_hist_g, medication_hist_h
from patient_obs import patient_obs, patient_obs_a, patient_obs_b, patient_obs_c, patient_obs_d, patient_obs_1, patient_obs_2, patient_obs_scenario
from patient_review import patient_review, patient_review_a, patient_review_b, patient_review_c, patient_review_d, patient_review_1, patient_review_2, patient_review_scenario
from treatment_adherence import treatment_adherence_part1, treatment_adherence_part2, treatment_adherence_a, treatment_adherence_b_part1, treatment_adherence_b_part2
from other_factors import other_factors, other_factors_a_part1, other_factors_a_part2, other_factors_a_part3, other_factors_b, other_factors_ba_part1, other_factors_ba_part2, other_factors_ba_part3, other_factors_ba_part4, other_factors_bb_part1, other_factors_bb_part2, other_factors_bb_part3, other_factors_bb_part4

from pre_quiz import pre_quiz_part1, pre_quiz_part2, pre_quiz_q1, pre_quiz_q2, pre_quiz_q3, pre_quiz_q4_intro1, pre_quiz_q4_intro2, pre_quiz_q4_intro3, pre_quiz_q4, pre_quiz_q5, pre_quiz_end
from post_quiz import post_quiz_part1, post_quiz_part2, post_quiz_q1, post_quiz_q2, post_quiz_q3, post_quiz_q4_intro1, post_quiz_q4_intro2, post_quiz_q4_intro3, post_quiz_q4, post_quiz_q5, post_quiz_end
from survey import survey, survey_q1, survey_q2, survey_q3a, survey_q3b, survey_q4a, survey_q4b, survey_q5a, survey_q5b, survey_q6, survey_q7a, survey_q7b, survey_q8, survey_end

# Stages
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

MODE = os.environ.get("MODE", "webhook")
PORT = int(os.environ.get('PORT', '8443'))

db = DBHelper()

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = '1809917012:AAEtugHYE2df2ttrfmeIzm4pahhMgoMsxk0' # CHANGE
HEROKU_URL = 'https://serene-sands-09412.herokuapp.com/'

def start(update, context):
    user = update.message.from_user
    first_name = update.message.chat.first_name
    chat_id = update.message.chat_id

    context.user_data['user_education'] = db.get_user_education(chat_id)

    logger.info("User %s started the conversation.", user.first_name)

    message_1 = """Good day to you! I am Dorcas, your personal buddy who will be assisting you throughout this supplementary education on identifying and managing factors affecting long-term blood pressure variability (BPV)!
    \nAs I am still in the prototype stage, please be patient with me!"""

    message_2 = """Thank you for participating in this evaluation of Dorcas."""

    message_3 = """Click on the button below to proceed!
    \nIf you wish to find out how this works or if you need further instructions, go to "Help" from the Main Menu, or type /help!"""

    keyboard = [['Next']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(message_1)
    update.message.reply_text(message_2)
    update.message.reply_text(message_3, reply_markup = reply_markup)

    if not context.user_data['user_education']:
        return START_NEW
    else:
        return START_EXISTING

def main_menu(update, context):

    chat_id = update.message.chat_id

    pre_quiz_status = db.check_pre_quiz(chat_id)
    print(pre_quiz_status)

    columns_check_all = ['bp_measuring_practices_status', 'treatment_adherence_status', 'lifestyle_status', 'medication_hist_status', 'patient_obs_status', 'patient_hist_status', 'other_factors_status']
    results_check_all = db.get_column_status(columns_check_all, chat_id)
    context.user_data['status_all'] = results_check_all

    message_1 = """Welcome to the Main Menu!
    \nWhat will you like to explore today?
    \n1. Learn more about long-term BPV
    \n2. Fact of the day
    \n3. Help"""

    message_2 = """Welcome to the Main Menu!
    \nWhat will you like to explore today? Psst... you have unlocked the virtual patient assessment feature!
    \n1. Learn more about long-term BPV
    \n2. Fact of the day
    \n3. Help
    \n4. Follow-up Knowledge Assessment
    \n5. Feedback on Dorcas"""

    keyboard_1 = [['1'], ['2'], ['3']]
    keyboard_2 = [['1'], ['2'], ['3'], ['4'], ['5']]

    reply_markup_1 = ReplyKeyboardMarkup(keyboard_1, one_time_keyboard = True, resize_keyboard = True)
    reply_markup_2 = ReplyKeyboardMarkup(keyboard_2, one_time_keyboard = True, resize_keyboard = True)

    if 'INCOMPLETE' in results_check_all:
        update.message.reply_text(message_1, reply_markup = reply_markup_1)
    else:
        update.message.reply_text(message_2, reply_markup = reply_markup_2)

    if pre_quiz_status is None:
        return MAIN_MENU_RETURN
    else:
        return MAIN_MENU


def learn_about_bpv_intro(update, context):

    chat_id = update.message.chat_id

    columns_check_1 = ['bp_measuring_practices_status_1', 'bp_measuring_practices_status_2']
    results_check_1 = db.get_column_status(columns_check_1, chat_id)
    if 'INCOMPLETE' not in results_check_1:
        column_keys = ['bp_measuring_practices_status']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_2 = ['treatment_adherence_status_a', 'treatment_adherence_status_b']
    results_check_2 = db.get_column_status(columns_check_2, chat_id)
    if 'INCOMPLETE' not in results_check_2:
        column_keys = ['treatment_adherence_status']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_3 = ['lifestyle_status_a', 'lifestyle_status_b', 'lifestyle_status_c', 'lifestyle_status_d', 'lifestyle_status_e', 'lifestyle_status_f']
    results_check_3 = db.get_column_status(columns_check_3, chat_id)
    if 'INCOMPLETE' not in results_check_3:
        column_keys = ['lifestyle_status']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_4 = ['medication_hist_status_a', 'medication_hist_status_b', 'medication_hist_status_c', 'medication_hist_status_d', 'medication_hist_status_e', 'medication_hist_status_f', 'medication_hist_status_g', 'medication_hist_status_h']
    results_check_4 = db.get_column_status(columns_check_4, chat_id)
    if 'INCOMPLETE' not in results_check_4:
        column_keys = ['medication_hist_status']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_5 = ['patient_obs_status_a', 'patient_obs_status_b', 'patient_obs_status_c', 'patient_obs_status_d']
    results_check_5 = db.get_column_status(columns_check_5, chat_id)
    if 'INCOMPLETE' not in results_check_5:
        column_keys = ['patient_obs_status']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_6 = ['patient_review_status_a', 'patient_review_status_b', 'patient_review_status_c', 'patient_review_status_d']
    results_check_6 = db.get_column_status(columns_check_6, chat_id)
    if 'INCOMPLETE' not in results_check_6:
        column_keys = ['patient_hist_status']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns_check_7 = ['other_factors_status_a', 'other_factors_status_b']
    results_check_7 = db.get_column_status(columns_check_7, chat_id)
    if 'INCOMPLETE' not in results_check_7:
        column_keys = ['other_factors_status']
        column_values = 'COMPLETED'
        column_values_dict = {}
        for i in column_keys:
                column_values_dict[i] = column_values
        db.update_column_status(column_values_dict, chat_id)

    columns = ['bp_measuring_practices_status', 'treatment_adherence_status', 'lifestyle_status', 'medication_hist_status', 'patient_obs_status', 'patient_hist_status', 'other_factors_status']

    results = db.get_column_status(columns, chat_id)
    #print("Result: ", results)

    message_1 = """By the way, you will see the list of modules below, with '[Incomplete]' tagged to each of them. This means that you have yet to complete the modules.
    \nAfter going through the minimum required amount of content in a module, it will be updated to '[Completed]'.
    \nOnce you have completed all the modules below, you will unlock the follow-up assessment feature!"""

    message_2 = """Looks like you have completed all the required modules! You can now return to Main Menu and do the virtual patient assessment!"""

    message_3 = f"""What will you like to do?
    \n1. Ask about BP measuring practices --- [{results[0]}]
    \n2. Ask about adherence to treatment --- [{results[1]}]
    \n3. Ask about lifestyle factors --- [{results[2]}]
    \n4. Ask about medication history --- [{results[3]}]
    \n5. Patient observation / physical examination --- [{results[4]}]
    \n6. Review patient history --- [{results[5]}]
    \n7. Consider other possibilities --- [{results[6]}]
    \n---
    \n8. Go through a BPV refresher
    \n9. Return to Main Menu"""

    keyboard = [['1'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    if 'INCOMPLETE' in context.user_data['status_all']:
        update.message.reply_text(message_3, reply_markup = reply_markup)
    else:
        update.message.reply_text(message_1)
        update.message.reply_text(message_2)
        update.message.reply_text(message_3, reply_markup = reply_markup)

    return LEARN_ABOUT_BPV

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():

    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points = [CommandHandler('start', start)],
        states = {
            START_EXISTING: [MessageHandler(Filters.regex(r'^.*Next.*$') & ~Filters.command, main_menu)],
            START_NEW: [MessageHandler(Filters.regex(r'^.*Next.*$') & ~Filters.command, intro_ques)],
            INTRO_QUES: [MessageHandler(Filters.regex(r'^.*\b(1|2|3)\b.*$') & ~Filters.command, intro_end)],
            MAIN_MENU: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, learn_about_bpv_intro),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, fact_of_the_day),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, help),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, post_quiz_part1),
                MessageHandler(Filters.regex(r'^.*5.*$') & ~Filters.command, survey),
                ],
            #fotd
            FACT_OF_THE_DAY: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, fact_of_the_day),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, main_menu),
                ],
            #help
            HELP_MENU: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, help_a_part1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, help_b_part1),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, help_c),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, main_menu),
                ],
            HELP_A_PART1: [MessageHandler(Filters.regex(r"^.*What's More?.*$") & ~Filters.command, help_a_part2)],
            HELP_B_PART1: [MessageHandler(Filters.regex(r"^.*What's More?.*$") & ~Filters.command, help_b_part2)],
            HELP_RETURN: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, help),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, main_menu),
                MessageHandler(Filters.regex(r'^.*Back to Help.*$') & ~Filters.command, help),
                MessageHandler(Filters.regex(r'^.*Main Menu.*$') & ~Filters.command, main_menu),
                ],
            #learn about bpv
            LEARN_ABOUT_BPV: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, treatment_adherence_part1),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, lifestyle),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, medication_hist),
                MessageHandler(Filters.regex(r'^.*5.*$') & ~Filters.command, patient_obs),
                MessageHandler(Filters.regex(r'^.*6.*$') & ~Filters.command, patient_review),
                MessageHandler(Filters.regex(r'^.*7.*$') & ~Filters.command, other_factors),
                MessageHandler(Filters.regex(r'^.*8.*$') & ~Filters.command, bpv_refresher_part1),
                MessageHandler(Filters.regex(r'^.*9.*$') & ~Filters.command, main_menu),
                ],
            #bpv refresher
            BPV_REFRESHER_PART1: [MessageHandler(Filters.regex(r'^.*Why Is It Important?.*$') & ~Filters.command, bpv_refresher_part2)],
            BPV_REFRESHER_PART2: [MessageHandler(Filters.regex(r"^.*What's More?.*$") & ~Filters.command, bpv_refresher_part3)],
            BPV_REFRESHER_PART3: [MessageHandler(Filters.regex(r'^.*Next.*$') & ~Filters.command, bpv_refresher_part2)],
            BPV_REFRESHER_PART4: [MessageHandler(Filters.regex(r'^.*Continue.*$') & ~Filters.command, learn_about_bpv_intro)],
            #bp measuring practices
            BP_MEASURING_PRACTICES: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_2),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, learn_about_bpv_intro),
                ],
            BP_MEASURING_PRACTICES_1: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_1a_part1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_1b),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, bp_measuring_practices_1c_part1),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, bp_measuring_practices_1d_part1),
                MessageHandler(Filters.regex(r'^.*5.*$') & ~Filters.command, bp_measuring_practices),
                ],
            BP_MEASURING_PRACTICES_2: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2a),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_2b),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, bp_measuring_practices_2c_part1),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, bp_measuring_practices_2d),
                MessageHandler(Filters.regex(r'^.*5.*$') & ~Filters.command, bp_measuring_practices),
                ],
            BP_MEASURING_PRACTICES_2A: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2aa_part1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_2ab_part1),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, bp_measuring_practices_2),
                ],
            BP_MEASURING_PRACTICES_2AA_PART1: [MessageHandler(Filters.regex(r'^.*What About Caffeine?.*$') & ~Filters.command, bp_measuring_practices_2aa_part2)],
            BP_MEASURING_PRACTICES_2AA_PART2: [MessageHandler(Filters.regex(r'^.*What About Exercise?.*$') & ~Filters.command, bp_measuring_practices_2aa_part3)],
            BP_MEASURING_PRACTICES_2AA_PART3: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2aaa),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_2aab),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, bp_measuring_practices_2aac),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, bp_measuring_practices_2a),
                MessageHandler(Filters.regex(r'^.*5.*$') & ~Filters.command, bp_measuring_practices_2),
                ],
            BP_MEASURING_PRACTICES_RETURN_2AA: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2aa_part3),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_2),
                ],
            BP_MEASURING_PRACTICES_2AB_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2ab_part2)],
            BP_MEASURING_PRACTICES_2AB_PART2: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2a),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_2),
                ],
            BP_MEASURING_PRACTICES_2B: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2ba_part1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_2bb_part1),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, bp_measuring_practices_2bc_part1),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, bp_measuring_practices_2),
                ],
            BP_MEASURING_PRACTICES_2BA_PART1: [MessageHandler(Filters.regex(r'^.*What About Supine?.*$') & ~Filters.command, bp_measuring_practices_2ba_part2)],
            BP_MEASURING_PRACTICES_2BA_PART2: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2ba_part3)],
            BP_MEASURING_PRACTICES_RETURN_2B: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2b),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_2),
                ],
            BP_MEASURING_PRACTICES_2BB_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2bb_part2)],
            BP_MEASURING_PRACTICES_2BC_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2bc_part2)],
            BP_MEASURING_PRACTICES_2C_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2c_part2)],
            BP_MEASURING_PRACTICES_2C_PART2: [MessageHandler(Filters.regex(r'^.*Back.*$') & ~Filters.command, bp_measuring_practices_2)],
            BP_MEASURING_PRACTICES_2D: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2da_part1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_2db_part1),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, bp_measuring_practices_2),
                ],
            BP_MEASURING_PRACTICES_2DA_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2da_part2)],
            BP_MEASURING_PRACTICES_2DA_PART2: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, bp_measuring_practices_2da_part3)],
            BP_MEASURING_PRACTICES_RETURN_2D: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2d),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_2),
                ],
            BP_MEASURING_PRACTICES_2DB_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_2db_part2)],
            BP_MEASURING_PRACTICES_1A_PART1: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, bp_measuring_practices_1a_part2)],
            BP_MEASURING_PRACTICES_1A_PART2: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_1aa),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_1ab),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, bp_measuring_practices_1),
                ],
            BP_MEASURING_PRACTICES_RETURN_1A: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_1a_part2),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_1),
                ],
            BP_MEASURING_PRACTICES_1B: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_1ba),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_1bb),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, bp_measuring_practices_1),
                ],
            BP_MEASURING_PRACTICES_RETURN_1B: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_1b),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, bp_measuring_practices_1),
                ],
            BP_MEASURING_PRACTICES_1C_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_1c_part2)],
            BP_MEASURING_PRACTICES_1C_PART2: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, bp_measuring_practices_1c_part3)],
            BP_MEASURING_PRACTICES_RETURN_1: [MessageHandler(Filters.regex(r'^.*Back.*$') & ~Filters.command, bp_measuring_practices_1)],
            BP_MEASURING_PRACTICES_1D_PART1: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, bp_measuring_practices_1d_part2)],
            BP_MEASURING_PRACTICES_1D_PART2: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, bp_measuring_practices_1d_part3)],
            # lifestyle
            LIFESTYLE: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_a_part1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, lifestyle_b_part1),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, lifestyle_c),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, lifestyle_d),
                MessageHandler(Filters.regex(r'^.*5.*$') & ~Filters.command, lifestyle_e_part1),
                MessageHandler(Filters.regex(r'^.*6.*$') & ~Filters.command, lifestyle_f_part1),
                MessageHandler(Filters.regex(r'^.*7.*$') & ~Filters.command, learn_about_bpv_intro),
                ],
            LIFESTYLE_A_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_a_part2)],
            LIFESTYLE_A_PART2: [MessageHandler(Filters.regex(r'^.*Why?.*$') & ~Filters.command, lifestyle_a_part3)],
            LIFESTYLE_RETURN: [MessageHandler(Filters.regex(r'^.*Back.*$') & ~Filters.command, lifestyle)],
            LIFESTYLE_B_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_b_part2)],
            LIFESTYLE_B_PART2: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, lifestyle_b_part3)],
            LIFESTYLE_C: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_ca_part1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, lifestyle_cb),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, lifestyle_cc_part1),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, lifestyle),
                ],
            LIFESTYLE_CA_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_ca_part2)],
            LIFESTYLE_RETURN_C: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_c),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, lifestyle),
                ],
            LIFESTYLE_CC_PART1: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, lifestyle_cc_part2)],
            LIFESTYLE_CC_PART2: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, lifestyle_cc_part3)],
            LIFESTYLE_CC_PART3: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_cc_part4)],
            LIFESTYLE_D: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_da),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, lifestyle_db),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, lifestyle),
                ],
            LIFESTYLE_RETURN_D: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_d),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, lifestyle),
                ],
            LIFESTYLE_E_PART1: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, lifestyle_e_part2)],
            LIFESTYLE_E_PART2: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_e_part3)],
            LIFESTYLE_F_PART1: [MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, lifestyle_f_part2)],
            #med hist
            MED_HIST: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, medication_hist_a),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, medication_hist_b),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, medication_hist_c),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, medication_hist_d),
                MessageHandler(Filters.regex(r'^.*5.*$') & ~Filters.command, medication_hist_e),
                MessageHandler(Filters.regex(r'^.*6.*$') & ~Filters.command, medication_hist_f),
                MessageHandler(Filters.regex(r'^.*7.*$') & ~Filters.command, medication_hist_g),
                MessageHandler(Filters.regex(r'^.*8.*$') & ~Filters.command, medication_hist_h),
                MessageHandler(Filters.regex(r'^.*9.*$') & ~Filters.command, learn_about_bpv_intro),
                MessageHandler(Filters.regex(r'^.*Back.*$') & ~Filters.command, medication_hist),
                ],
            #patient obs
            PATIENT_OBS: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, patient_obs_a),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, patient_obs_b),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, patient_obs_c),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, patient_obs_d),
                MessageHandler(Filters.regex(r'^.*5.*$') & ~Filters.command, learn_about_bpv_intro),
                ],
            PATIENT_OBS_NEXT: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, patient_obs_1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, patient_obs_2),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, patient_obs),
                ],
            PATIENT_OBS_RETURN: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, patient_obs_scenario),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, patient_obs),
                ],
            #patient review
            PATIENT_REVIEW: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, patient_review_a),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, patient_review_b),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, patient_review_c),
                MessageHandler(Filters.regex(r'^.*4.*$') & ~Filters.command, patient_review_d),
                MessageHandler(Filters.regex(r'^.*5.*$') & ~Filters.command, learn_about_bpv_intro),
                ],
            PATIENT_REVIEW_NEXT: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, patient_review_1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, patient_review_2),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, patient_review),
                ],
            PATIENT_REVIEW_RETURN: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, patient_review_scenario),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, patient_review),
                ],
            #treatment adherence
            TREATMENT_ADHERENCE_PART1: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, treatment_adherence_part2)],
            TREATMENT_ADHERENCE_PART2: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, treatment_adherence_a),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, treatment_adherence_b_part1),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, learn_about_bpv_intro),
                ],
            TREATMENT_ADHERENCE_RETURN: [MessageHandler(Filters.regex(r"^.*Back.*$") & ~Filters.command, treatment_adherence_part2)],
            TREATMENT_ADHERENCE_B_PART1: [MessageHandler(Filters.regex(r"^.*Find Out More.*$") & ~Filters.command, treatment_adherence_b_part2)],
            #other factors
            OTHER_FACTORS: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, other_factors_a_part1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, other_factors_b),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, learn_about_bpv_intro),
                ],
            OTHER_FACTORS_A_PART1: [MessageHandler(Filters.regex(r'^.*How to Manage?.*$') & ~Filters.command, other_factors_a_part2)],
            OTHER_FACTORS_A_PART2: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, other_factors_a_part3)],
            OTHER_FACTORS_RETURN: [MessageHandler(Filters.regex(r"^.*Back.*$") & ~Filters.command, other_factors)],
            OTHER_FACTORS_B: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, other_factors_ba_part1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, other_factors_bb_part1),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, learn_about_bpv_intro),
                ],
            OTHER_FACTORS_BA_PART1: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, other_factors_ba_part2)],
            OTHER_FACTORS_BA_PART2: [MessageHandler(Filters.regex(r'^.*How to Manage?.*$') & ~Filters.command, other_factors_ba_part3)],
            OTHER_FACTORS_BA_PART3: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, other_factors_ba_part4)],
            OTHER_FACTORS_RETURN_B: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, other_factors_b),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, other_factors),
                ],
            OTHER_FACTORS_BB_PART1: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, other_factors_bb_part2)],
            OTHER_FACTORS_BB_PART2: [MessageHandler(Filters.regex(r'^.*How to Manage?.*$') & ~Filters.command, other_factors_bb_part3)],
            OTHER_FACTORS_BB_PART3: [MessageHandler(Filters.regex(r"^.*What's More.*$") & ~Filters.command, other_factors_bb_part4)],
            #pre quiz
            PRE_QUIZ_PART1: [
                MessageHandler(Filters.regex(r'^.*Get Started.*$') & ~Filters.command, pre_quiz_part2),
                MessageHandler(Filters.regex(r'^.*Main Menu.*$') & ~Filters.command, main_menu),
                ],
            PRE_QUIZ_PART2: [MessageHandler(Filters.regex(r"^.*Let's Go!.*$") & ~Filters.command, pre_quiz_q1)],
            PRE_QUIZ_Q1: [MessageHandler(Filters.text & ~Filters.command, pre_quiz_q2)],
            PRE_QUIZ_Q2: [MessageHandler(Filters.text & ~Filters.command, pre_quiz_q3)],
            PRE_QUIZ_Q3: [MessageHandler(Filters.regex(r'^.*\b(a|b|c)\b.*$') & ~Filters.command, pre_quiz_q4_intro1)],
            PRE_QUIZ_Q4_INTRO1: [MessageHandler(Filters.regex(r'^.*Patient Information.*$') & ~Filters.command, pre_quiz_q4_intro2)],
            PRE_QUIZ_Q4_INTRO2: [MessageHandler(Filters.regex(r'^.*More Information.*$') & ~Filters.command, pre_quiz_q4_intro3)],
            PRE_QUIZ_Q4_INTRO3: [MessageHandler(Filters.regex(r'^.*Continue to Q4.*$') & ~Filters.command, pre_quiz_q4)],
            PRE_QUIZ_Q4: [MessageHandler(Filters.text & ~Filters.command, pre_quiz_q5)],
            PRE_QUIZ_Q5: [MessageHandler(Filters.text & ~Filters.command, pre_quiz_end)],
            #post quiz
            POST_QUIZ_PART1: [
                MessageHandler(Filters.regex(r'^.*Get Started.*$') & ~Filters.command, post_quiz_part2),
                MessageHandler(Filters.regex(r'^.*Main Menu.*$') & ~Filters.command, main_menu),
                ],
            POST_QUIZ_PART2: [MessageHandler(Filters.regex(r"^.*Let's Go!.*$") & ~Filters.command, post_quiz_q1)],
            POST_QUIZ_Q1: [MessageHandler(Filters.text & ~Filters.command, post_quiz_q2)],
            POST_QUIZ_Q2: [MessageHandler(Filters.text & ~Filters.command, post_quiz_q3)],
            POST_QUIZ_Q3: [MessageHandler(Filters.regex(r'^.*\b(a|b|c)\b.*$') & ~Filters.command, post_quiz_q4_intro1)],
            POST_QUIZ_Q4_INTRO1: [MessageHandler(Filters.regex(r'^.*Patient Information.*$') & ~Filters.command, post_quiz_q4_intro2)],
            POST_QUIZ_Q4_INTRO2: [MessageHandler(Filters.regex(r'^.*More Information.*$') & ~Filters.command, post_quiz_q4_intro3)],
            POST_QUIZ_Q4_INTRO3: [MessageHandler(Filters.regex(r'^.*Continue to Q4.*$') & ~Filters.command, post_quiz_q4)],
            POST_QUIZ_Q4: [MessageHandler(Filters.text & ~Filters.command, post_quiz_q5)],
            POST_QUIZ_Q5: [MessageHandler(Filters.text & ~Filters.command, post_quiz_end)],
            #survey
            SURVEY_START: [MessageHandler(Filters.regex(r'^.*Get Started.*$') & ~Filters.command, survey_q1)],
            SURVEY_Q1: [MessageHandler(Filters.regex(r'^.*\b(a|b|c)\b.*$') & ~Filters.command, survey_q2)],
            SURVEY_Q2: [MessageHandler(Filters.regex(r'^.*\b(a|b|c|d|e)\b.*$') & ~Filters.command, survey_q3a)],
            SURVEY_Q3A: [MessageHandler(Filters.regex(r'^.*\b(a|b|c|d|e)\b.*$') & ~Filters.command, survey_q3b)],
            SURVEY_Q3B: [MessageHandler(Filters.text & ~Filters.command, survey_q4a)],
            SURVEY_Q4A: [MessageHandler(Filters.regex(r'^.*\b(a|b|c|d|e)\b.*$') & ~Filters.command, survey_q4b)],
            SURVEY_Q4B: [MessageHandler(Filters.regex(r'^.*\b(a|b|c|d|e)\b.*$') & ~Filters.command, survey_q5a)],
            SURVEY_Q5A: [MessageHandler(Filters.regex(r'^.*\b(a|b|c|d|e)\b.*$') & ~Filters.command, survey_q5b)],
            SURVEY_Q5B: [MessageHandler(Filters.regex(r'^.*\b(a|b|c|d|e)\b.*$') & ~Filters.command, survey_q6)],
            SURVEY_Q6: [MessageHandler(Filters.text & ~Filters.command, survey_q7a)],
            SURVEY_Q7A: [MessageHandler(Filters.regex(r'^.*\b(a|b|c|d|e)\b.*$') & ~Filters.command, survey_q7b)],
            SURVEY_Q7B: [MessageHandler(Filters.text & ~Filters.command, survey_q8)],
            SURVEY_Q8: [MessageHandler(Filters.regex(r'^.*\b(a|b|c|d|e)\b.*$') & ~Filters.command, survey_end)],
            # return main menu
            MAIN_MENU_RETURN: [
                MessageHandler(Filters.regex(r'^.*1.*$') & ~Filters.command, pre_quiz_part1),
                MessageHandler(Filters.regex(r'^.*2.*$') & ~Filters.command, fact_of_the_day),
                MessageHandler(Filters.regex(r'^.*3.*$') & ~Filters.command, help),
                MessageHandler(Filters.regex(r'^.*Main Menu.*$') & ~Filters.command, main_menu),
                MessageHandler(Filters.regex(r'^.*Get Started.*$') & ~Filters.command, main_menu),
                ],
        },
        fallbacks = [
            CommandHandler('start', start),
            CommandHandler('help', help),
            ],
    )

    dp.add_handler(conv_handler)
    dp.add_error_handler(error)

    if MODE == 'webhook':
        # enable webhook
        updater.start_webhook(listen = "0.0.0.0",
                      port = PORT,
                      url_path = TOKEN,
                      webhook_url = HEROKU_URL + TOKEN)

    else:
        # enable polling
        updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
