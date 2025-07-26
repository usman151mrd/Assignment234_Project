from resume_builder.models import Resume

def user_resume(request):
    """Add user's resume to template context"""
    if request.user.is_authenticated:
        user_resume = Resume.objects.filter(user=request.user).first()
        return {'user_resume': user_resume}
    return {'user_resume': None} 