import random
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

def fact_of_the_day(update, context):

    message_1 = [
    """Dynamic and static exercise can cause BP increases, and that the increase is more pronounced for SBP than for DBP [2].""",
    """Tobacco smoking has an acute prolonged pressor effect that may cause BP elevation [2]""",
    """Caffeine has been shown to have an acute pressor effect that may cause BP elevation [2]""",
    """If the cuffs used in BP measurement are too small relative to the arm circumference, it can result in a spurious elevation of BP [2]""",
    """There could be a difference in BP between arms, ideally established by simultaneous measurement. The arm with the higher BP values should be used for all subsequent measurements [2]""",
    ]

    message_2 = """What will you like to do next?
    \n1. Tell me another Fact of the Day
    \n2. Return to Main Menu"""

    keyboard = [['1'], ['2']]

    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)

    update.message.reply_text(random.choice(message_1))
    update.message.reply_text(message_2, reply_markup = reply_markup)

    return FACT_OF_THE_DAY
