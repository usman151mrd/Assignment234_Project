# resume_builder/forms.py
from django import forms
from .models import (
    ResumeTemplate, Resume, ResumeSection, WorkExperience,
    TechnicalSkill, Education, Technology, Project,
    Certification, Award, Language, PersonalInformation
)

class ResumeTemplateForm(forms.ModelForm):
    class Meta:
        model = ResumeTemplate
        fields = ['name', 'description', 'format_type', 'version']

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'slug', 'summary', 'tags', 'template', 'language', 'visibility']

class ResumeSectionForm(forms.ModelForm):
    class Meta:
        model = ResumeSection
        fields = ['section_type', 'title', 'content', 'order', 'is_visible']

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = [
            'first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country', 'postal_code',
            'linkedin_url', 'github_url', 'portfolio_url', 'profile_image',
            'date_of_birth', 'nationality', 'is_visible'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['resume', 'job_title', 'company', 'location', 'start_date', 'end_date', 'is_current', 'description', 'achievements', 'technologies']

class TechnicalSkillForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkill
        fields = ['resume', 'technology', 'proficiency', 'years_experience', 'last_used', 'project_count', 'is_visible']

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['resume', 'degree', 'institution', 'location', 'start_date', 'end_date', 'gpa', 'description', 'is_visible']

class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['name', 'category', 'icon']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['resume', 'title', 'role', 'start_date', 'end_date', 'description', 'technologies', 'outcomes', 'url', 'is_active']

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = [
            'resume', 'name', 'issuer', 'issue_date',
            'expiration_date', 'credential_id',
            'verification_url', 'skills'
        ]
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'skills': forms.SelectMultiple(attrs={'class': 'form-control'}),  # Fix for ManyToManyField
        }


class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['resume', 'title', 'issuer', 'issue_date', 'category', 'description', 'impact_metrics', 'is_visible']

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['resume', 'name', 'proficiency', 'certification', 'is_visible']