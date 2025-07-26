from django.shortcuts import render
from allauth.account.models import EmailAddress
from django.contrib.auth.decorators import login_required
from resume_builder.models import (
    PersonalInformation, WorkExperience, Education, Project,
    Certification, Award, Language, TechnicalSkill, Resume
)

@login_required
def dashboard(request):
    # Check if user's email is verified
    is_verified = EmailAddress.objects.filter(user=request.user, verified=True).exists()

    # Get user's resume
    user_resume = Resume.objects.filter(user=request.user).first()

    # Get counts for each model
    context = {
        'personal_info_count': PersonalInformation.objects.filter(resume__user=request.user).count(),
        'work_experience_count': WorkExperience.objects.filter(resume__user=request.user).count(),
        'education_count': Education.objects.filter(resume__user=request.user).count(),
        'project_count': Project.objects.filter(resume__user=request.user).count(),
        'certification_count': Certification.objects.filter(resume__user=request.user).count(),
        'award_count': Award.objects.filter(resume__user=request.user).count(),
        'language_count': Language.objects.filter(resume__user=request.user).count(),
        'technical_skill_count': TechnicalSkill.objects.filter(resume__user=request.user).count(),
        'resume_count': Resume.objects.filter(user=request.user).count(),
        'user_resume': user_resume,
        'is_verified': is_verified,
        # Recent entries
        'recent_work_experience': WorkExperience.objects.filter(resume__user=request.user).order_by('-created_at')[:3],
        'recent_education': Education.objects.filter(resume__user=request.user).order_by('-end_date')[:3],
        'recent_projects': Project.objects.filter(resume__user=request.user).order_by('-start_date')[:3],
        'recent_certifications': Certification.objects.filter(resume__user=request.user).order_by('-issue_date')[:3],
    }
    
    return render(request, 'dashboard/dashboard.html', context)