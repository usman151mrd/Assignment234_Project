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

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['resume', 'job_title', 'company', 'location', 'start_date', 'end_date', 'is_current', 'description', 'achievements', 'technologies']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'achievements': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['resume'].queryset = Resume.objects.filter(user=user)
            self.fields['technologies'].queryset = Technology.objects.all()

class TechnicalSkillForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkill
        fields = ['resume', 'technology', 'proficiency', 'years_experience', 'last_used', 'project_count', 'is_visible']
        widgets = {
            'last_used': forms.DateInput(attrs={'type': 'date'}),
            'proficiency': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['resume'].queryset = Resume.objects.filter(user=user)
            self.fields['technology'].queryset = Technology.objects.all()

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['resume', 'degree', 'institution', 'location', 'start_date', 'end_date', 'gpa', 'description', 'is_visible']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'gpa': forms.NumberInput(attrs={'step': '0.1', 'min': '0', 'max': '4'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['resume'].queryset = Resume.objects.filter(user=user)

class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['name', 'category', 'icon']

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['resume', 'title', 'role', 'start_date', 'end_date', 'description', 'technologies', 'outcomes', 'url', 'is_active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'outcomes': forms.Textarea(attrs={'rows': 3}),
            'url': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['resume'].queryset = Resume.objects.filter(user=user)
            self.fields['technologies'].queryset = Technology.objects.all()

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['resume', 'name', 'issuer', 'issue_date', 'expiration_date', 'credential_id', 'verification_url', 'skills']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
            'verification_url': forms.URLInput(attrs={'placeholder': 'https://example.com'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['resume'].queryset = Resume.objects.filter(user=user)
            self.fields['skills'].queryset = Technology.objects.all()

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['resume', 'title', 'issuer', 'issue_date', 'category', 'description', 'impact_metrics', 'is_visible']
        widgets = {
            'issue_date': forms.DateInput(attrs={'type': 'date'}),
            'description': forms.Textarea(attrs={'rows': 4}),
            'impact_metrics': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['resume'].queryset = Resume.objects.filter(user=user)

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['resume', 'name', 'proficiency', 'certification', 'is_visible']
        widgets = {
            'proficiency': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['resume'].queryset = Resume.objects.filter(user=user)

class PersonalInformationForm(forms.ModelForm):
    class Meta:
        model = PersonalInformation
        fields = ['resume', 'full_name', 'email', 'phone', 'address', 'date_of_birth', 'profile_photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['resume'].queryset = Resume.objects.filter(user=user)