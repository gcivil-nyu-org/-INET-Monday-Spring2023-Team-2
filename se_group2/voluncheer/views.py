from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

# ======================== Job Board ============================
test_jobs = [
#     Job(job_title="We Speak NYC", \
#         job_discription="We Speak NYC (formerly We Are New York) is the City’s Free Supplemental English Language Learning Program. We Speak NYC organizes conversation groups that meet in 7-10-week conversation classes in all five boroughs and online. We aim to create a positive experience for all learners, utilizing community building and speaking to practical needs.", \
#         job_location="New York, NY", \
#         job_worktime="Full-Time", \
#         job_image="images/volunteer_job_1.png", \
#     ),
#     Job(
#         job_title="Habitat for Humanity NYC and Westchester: Site Leaders for Construction and Painting",\
#         job_discription=\
#         """
#             Habitat NYC and Westchester is looking for Volunteer Site Leaders who can manage a small group of volunteers (of up to five people) on our construction and community painting sites as they go through their activities. We are currently demolishing/building or doing gut-and-rehab projects on future single-family homes in southeastern Queens (around Jamaica), and we are currently painting community space in the Bronx. \
#             """,\
#         job_location="New York, NY",\
#         job_worktime="Part-Time",\
#         job_image="images/volunteer_job_2.png",\
#         job_pubdate=timezone.now().date(),\
#     ),
    Job(
        job_organization=Organization.objects.get(pk=5),
        job_title="Pancreatic Cancer Action Network",
        job_discription=
        """
            Our mission is to take bold action to improve the lives of everyone impacted by pancreatic cancer by advancing scientific research, building community, sharing knowledge and advocating for patients.
            """,
        job_location="New York, NY",
        job_worktime="Part-Time",
        job_image="images/volunteer_job_3.png",
        job_pubdate=timezone.now().date(),
    ),
    Job(
        job_organization=Organization.objects.get(pk=5),
        job_title="Serve Lunch To The Homeless",
        job_discription=
        """
            Are you looking to help those who are homeless in NYC? At The Bowery Mission, we serve anyone looking for a warm meal to eat. We rely on our volunteers to provide critical services to New Yorkers in need. Help our chefs serve lunch to the community. Tasks may also include limited meal prep, clearing tables, and helping with washing dishes. We serve our guests with food prepared in-house and occasionally donated meals from vendors. Thank you so much for serving!!
            """,
        job_location="New York, NY",
        job_worktime="Part-Time",
        job_image="images/volunteer_job_4.png",
        job_pubdate=timezone.now().date(),
    ),
]


def jobboard(request):
    job_lists = Job.objects.order_by('-job_pubdate'[:20])
    context = {'job_lists': job_lists}
    return render(request, 'voluncheer/jobboard.html', context)


def jobboard_select(request):
    job_lists = Job.objects.order_by('-job_pubdate'[:20])
    context = {'job_lists': job_lists}
    return render(request, 'voluncheer/jobboard.html', context)


# ======================== User Profile ============================

def user_profile(request, user_id):
    user_profile = get_object_or_404(User, pk=user_id)
    badge_urls = []
    badge_list = user_profile.user_badges.split(",")
    for badge in badge_list:
        try:
            badge_urls.append(GLOBAL_BADGES[badge])
        except:
            pass
    context = {'user_profile': user_profile, 'badge_urls': badge_urls}
    return render(request, 'voluncheer/user_profile.html', context)


# ==================== Organization Profile =========================

def organization_profile(request, organ_id):
    organ_profile = get_object_or_404(Organization, pk=organ_id)
    job_lists = organ_profile.job_set.all()
    context = {'organ_profile': organ_profile, 'job_lists': job_lists}
    return render(request, 'voluncheer/organization_profile.html', context)


# ========================== Chatroom ================================

def chatroom_user(request, user_id):
    context = {}
    return render(request, 'voluncheer/chatroom.html', context)

def chatroom_organ(request, organ_id):
    context = {}
    return render(request, 'voluncheer/chatroom.html', context)

# ============================= Map ==================================

def map(request):
    context = {}
    return render(request, 'voluncheer/map.html', context)


def temp(request):
    return
