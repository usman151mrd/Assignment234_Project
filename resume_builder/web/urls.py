from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from resume_builder.web.views import PersonalInformationCreateView
from .views import ResumeDynamicPreviewView

from . import views
from resume_builder.web.views import ResumePreviewView
from .views import select_template_view



from .views import (
    # Personal Info
    PersonalInformationListView, PersonalInformationCreateView, PersonalInformationUpdateView,
    PersonalInformationDeleteView, PersonalInformationDetailView,

    # Work Experience
    WorkExperienceListView, WorkExperienceCreateView, WorkExperienceUpdateView,
    WorkExperienceDeleteView, WorkExperienceDetailView,

    # Education
    EducationListView, EducationCreateView, EducationUpdateView,
    EducationDeleteView, EducationDetailView,

    # Projects
    ProjectListView, ProjectCreateView, ProjectUpdateView,
    ProjectDeleteView, ProjectDetailView,

    # Certifications
    CertificationListView, CertificationCreateView, CertificationUpdateView,
    CertificationDeleteView, CertificationDetailView,

    # Awards
    AwardListView, AwardCreateView, AwardUpdateView,
    AwardDeleteView, AwardDetailView,

    # Languages
    LanguageListView, LanguageCreateView, LanguageUpdateView,
    LanguageDeleteView, LanguageDetailView,

    # Technical Skills
    TechnicalSkillListView, TechnicalSkillCreateView, TechnicalSkillUpdateView,
    TechnicalSkillDeleteView, TechnicalSkillDetailView,

    # Resume Views
    ResumeListView, ResumeCreateView, ResumeDetailView, ResumeDeleteView,
    ResumeDownloadPDFView, ResumeDownloadDOCXView,

    # Previews

)

app_name = 'resume_builder_web'

urlpatterns = [
    # Personal Information
    path('personal-information/', PersonalInformationListView.as_view(), name='personal_information_list'),
    path('personal-information/add/', PersonalInformationCreateView.as_view(), name='personal_information_create'),
    path('personal-information/<int:pk>/edit/', PersonalInformationUpdateView.as_view(), name='personal_information_update'),
    path('personal-information/<int:pk>/delete/', PersonalInformationDeleteView.as_view(), name='personal_information_delete'),
    path('personal-information/<int:pk>/', PersonalInformationDetailView.as_view(), name='personal_information_detail'),

    # Work Experience
    path('work-experience/', WorkExperienceListView.as_view(), name='work_experience_list'),
    path('work-experience/add/', WorkExperienceCreateView.as_view(), name='work_experience_create'),
    path('work-experience/<int:pk>/edit/', WorkExperienceUpdateView.as_view(), name='work_experience_update'),
    path('work-experience/<int:pk>/delete/', WorkExperienceDeleteView.as_view(), name='work_experience_delete'),
    path('work-experience/<int:pk>/', WorkExperienceDetailView.as_view(), name='work_experience_detail'),

    # Education
    path('education/', EducationListView.as_view(), name='education_list'),
    path('education/add/', EducationCreateView.as_view(), name='education_create'),
    path('education/<int:pk>/edit/', EducationUpdateView.as_view(), name='education_update'),
    path('education/<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),
    path('education/<int:pk>/', EducationDetailView.as_view(), name='education_detail'),

    # Projects
    path('project/', ProjectListView.as_view(), name='project_list'),
    path('project/add/', ProjectCreateView.as_view(), name='project_create'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

    # Certifications
    path('certification/', CertificationListView.as_view(), name='certification_list'),
    path('certification/add/', CertificationCreateView.as_view(), name='certification_create'),
    path('certification/<int:pk>/edit/', CertificationUpdateView.as_view(), name='certification_update'),
    path('certification/<int:pk>/delete/', CertificationDeleteView.as_view(), name='certification_delete'),
    path('certification/<int:pk>/', CertificationDetailView.as_view(), name='certification_detail'),

    # Awards
    path('award/', AwardListView.as_view(), name='award_list'),
    path('award/add/', AwardCreateView.as_view(), name='award_create'),
    path('award/<int:pk>/edit/', AwardUpdateView.as_view(), name='award_update'),
    path('award/<int:pk>/delete/', AwardDeleteView.as_view(), name='award_delete'),
    path('award/<int:pk>/', AwardDetailView.as_view(), name='award_detail'),

    # Languages
    path('language/', LanguageListView.as_view(), name='language_list'),
    path('language/add/', LanguageCreateView.as_view(), name='language_create'),
    path('language/<int:pk>/edit/', LanguageUpdateView.as_view(), name='language_update'),
    path('language/<int:pk>/delete/', LanguageDeleteView.as_view(), name='language_delete'),
    path('language/<int:pk>/', LanguageDetailView.as_view(), name='language_detail'),

    # Technical Skills
    path('technical-skill/', TechnicalSkillListView.as_view(), name='technical_skill_list'),
    path('technical-skill/add/', TechnicalSkillCreateView.as_view(), name='technical_skill_create'),
    path('technical-skill/<int:pk>/edit/', TechnicalSkillUpdateView.as_view(), name='technical_skill_update'),
    path('technical-skill/<int:pk>/delete/', TechnicalSkillDeleteView.as_view(), name='technical_skill_delete'),
    path('technical-skill/<int:pk>/', TechnicalSkillDetailView.as_view(), name='technical_skill_detail'),

    # Resume Management
    path('resume/', ResumeListView.as_view(), name='resume_list'),
    path('resume/add/', ResumeCreateView.as_view(), name='resume_create'),
    path('resume/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),
    path('resume/<int:pk>/delete/', ResumeDeleteView.as_view(), name='resume_delete'),
    path('resume/<int:pk>/download/pdf/', ResumeDownloadPDFView.as_view(), name='resume_download_pdf'),
    path('resume/<int:pk>/download/docx/', ResumeDownloadDOCXView.as_view(), name='resume_download_docx'),

    # Resume Previews (recommended: use dynamic one)


    # Option A: session-based preview (after user selects a template)
    path('resume/preview/<int:resume_id>/', ResumePreviewView.as_view(), name='resume_preview'),

    # Option B: URL-based preview (e.g., /resume/23/preview/modern/)
    path('resume/<int:resume_id>/preview/<str:template_slug>/', ResumeDynamicPreviewView.as_view(), name='resume_dynamic_preview'),

    # View to save selected template in session
    path('select-template/', select_template_view, name='select_template'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
