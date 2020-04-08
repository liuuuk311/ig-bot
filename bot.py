# imports
import os
import random
from dotenv import load_dotenv

from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace

load_dotenv()

# login credentials
insta_username = os.environ.get('IG_BOT_USER')
insta_password = os.environ.get('IG_BOT_PASS')

assert insta_username is not None
assert insta_password is not None

set_workspace("./InstaPy")

# TARGET data
""" Set similar accounts and influencers from your niche to target...
"""
targets = [
    'davidefpv', 
    'milomilofpv', 
    'overvoltofficial', 
    'morollalessandro', 
    'frankcitrofpv', 
    'fpvmagazine', 
    'tattulipos', 
    'diatone.us', 
    'mgfpv', 
    'johnny_fpv',
    'iflightgo',
    'hqpropzhong',
    'ethixltd',
    'joshuabardwell',
    'mrsteelefpv',
    'airvuzfpv',
    'joe.fpv',
    ]


""" Skip all business accounts, except from list given...
"""
target_business_categories = ['Creators & Celebrities', 'Product/Service']

# COMMENT data
comments = []

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  want_check_browser=True,
                  headless_browser=False,
                  disable_image_load=True,
                  multi_logs=True)

with smart_run(session):
    session.set_simulation(enabled=True)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=7500,
                                    max_following=3000,
                                    min_followers=25,
                                    min_following=25,
                                    min_posts=3)

    session.set_skip_users(skip_private=True,
                           skip_no_profile_pic=True,
                           skip_business=True,
                           dont_skip_business_categories=[
                               target_business_categories])

    session.set_user_interact(amount=15, randomize=True, percentage=80)
    session.set_do_like(enabled=True, percentage=90)
    session.set_do_follow(enabled=True, percentage=40, times=1)


    # FOLLOW+INTERACTION on TARGETED accounts
    """ Select users form a list of a predefined targets...
    """
    number = random.randint(3, 5)
    random_targets = targets
    random_targets = random.sample(targets, number)

    """ Interact with the chosen targets...
    """
    session.follow_user_followers(random_targets,
                                  amount=random.randint(5, 15),
                                  randomize=True, sleep_delay=600,
                                  interact=True)

    """ Unfollow nonfollowers after two days...
    """
    session.unfollow_users(amount=random.randint(40, 60),
                           InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=48 * 60 * 60, sleep_delay=600)

    """ Unfollow all users followed by InstaPy after one week to keep the 
    following-level clean...
    """
    session.unfollow_users(amount=random.randint(60, 80),
                           InstapyFollowed=(True, "all"), style="FIFO",
                           unfollow_after=168 * 60 * 60, sleep_delay=600)

    """ Joining Engagement Pods...
    """
    session.join_pods()