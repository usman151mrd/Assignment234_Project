from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404 , FileResponse
from django.template.loader import render_to_string
from io import BytesIO
from docx import Document
from docx.shared import Inches
import json
from resume_builder.models import (
    ResumeTemplate, Resume, ResumeSection, WorkExperience,
    TechnicalSkill, Education, Technology, Project,
    Certification, Award, Language
)
from resume_builder.forms import (
    ResumeTemplateForm, ResumeForm, ResumeSectionForm, WorkExperienceForm,
    TechnicalSkillForm, EducationForm, TechnologyForm, ProjectForm,
    CertificationForm, AwardForm, LanguageForm, EmptyForm
)

class OwnerRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        if isinstance(obj, Resume):
            return obj.user == self.request.user
        return obj.resume.user == self.request.user
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if 'user' not in kwargs:
            kwargs['user'] = self.request.user
        return kwargs

class BaseResumeFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if 'resume' in form.fields:
            form.fields['resume'].queryset = Resume.objects.filter(user=self.request.user)
        return form

class RelatedObjectCreateView(CreateView):
    def get_initial(self):
        initial = super().get_initial()
        resume_pk = self.kwargs.get('resume_pk')
        if resume_pk:
            resume = get_object_or_404(Resume, pk=resume_pk, user=self.request.user)
            initial['resume'] = resume
        return initial
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user

        resume_pk = self.kwargs.get('resume_pk')
        if resume_pk:
            kwargs['resume_instance'] = get_object_or_404(Resume, pk=resume_pk, user=self.request.user)
        return kwargs

    def form_valid(self, form):
        if not form.instance.resume_id:
            resume_pk = self.kwargs.get('resume_pk')
            form.instance.resume = get_object_or_404(Resume, pk=resume_pk, user=self.request.user)
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume_pk = self.kwargs.get('resume_pk')
        if resume_pk:
            try:
                context['resume'] = get_object_or_404(Resume, pk=resume_pk, user=self.request.user)
            except Exception as e:
                pass
        return context

    def get_success_url(self):
            resume_pk = self.kwargs.get('resume_pk')
            return reverse_lazy('web:resume_detail', kwargs={'pk': resume_pk})
class RelatedObjectListView(LoginRequiredMixin, ListView):
    context_object_name = 'objects'

    def get_queryset(self):
        resume_pk = self.kwargs.get('resume_pk')
        self.resume = get_object_or_404(Resume, pk=resume_pk, user=self.request.user)
        return self.model.objects.filter(resume=self.resume)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume'] = self.resume
        return context

class WorkExperienceListView(RelatedObjectListView):
    model = WorkExperience
    template_name = 'resume_builder/work_experience/work_experience_list.html'
    context_object_name = 'work_experiences'

class WorkExperienceCreateView(RelatedObjectCreateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = 'resume_builder/work_experience/work_experience_form.html'

class WorkExperienceUpdateView(BaseResumeFormMixin, OwnerRequiredMixin, UpdateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = 'resume_builder/work_experience/work_experience_form.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})

class WorkExperienceDeleteView(OwnerRequiredMixin, DeleteView):
    model = WorkExperience
    template_name = 'resume_builder/work_experience/work_experience_confirm_delete.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})
    form_class = EmptyForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('user', None)
        return kwargs

class WorkExperienceDetailView(OwnerRequiredMixin, DetailView):
    model = WorkExperience
    template_name = 'resume_builder/work_experience/work_experience_detail.html'
    context_object_name = 'experience'

class EducationListView(RelatedObjectListView):
    model = Education
    template_name = 'resume_builder/education/education_list.html'
    context_object_name = 'educations'

class EducationCreateView(RelatedObjectCreateView):
    model = Education
    form_class = EducationForm
    template_name = 'resume_builder/education/education_form.html'

class EducationUpdateView(BaseResumeFormMixin, OwnerRequiredMixin, UpdateView):
    model = Education
    form_class = EducationForm
    template_name = 'resume_builder/education/education_form.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})

class EducationDeleteView(OwnerRequiredMixin, DeleteView):
    model = Education
    template_name = 'resume_builder/education/education_confirm_delete.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})
    form_class = EmptyForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('user', None)
        return kwargs

class EducationDetailView(OwnerRequiredMixin, DetailView):
    model = Education
    template_name = 'resume_builder/education/education_detail.html'
    context_object_name = 'education'

class ProjectListView(RelatedObjectListView):
    model = Project
    template_name = 'resume_builder/project/project_list.html'
    context_object_name = 'projects'

class ProjectCreateView(RelatedObjectCreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'resume_builder/project/project_form.html'

class ProjectUpdateView(BaseResumeFormMixin, OwnerRequiredMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'resume_builder/project/project_form.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})

class ProjectDeleteView(OwnerRequiredMixin, DeleteView):
    model = Project
    template_name = 'resume_builder/project/project_confirm_delete.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})
    form_class = EmptyForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('user', None)
        return kwargs

class ProjectDetailView(OwnerRequiredMixin, DetailView):
    model = Project
    template_name = 'resume_builder/project/project_detail.html'
    context_object_name = 'project'

class CertificationListView(RelatedObjectListView):
    model = Certification
    template_name = 'resume_builder/certification/certification_list.html'
    context_object_name = 'certifications'

class CertificationCreateView(RelatedObjectCreateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'resume_builder/certification/certification_form.html'

class CertificationUpdateView(BaseResumeFormMixin, OwnerRequiredMixin, UpdateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'resume_builder/certification/certification_form.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})

class CertificationDeleteView(OwnerRequiredMixin, DeleteView):
    model = Certification
    template_name = 'resume_builder/certification/certification_confirm_delete.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})
    form_class = EmptyForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('user', None)
        return kwargs

class CertificationDetailView(OwnerRequiredMixin, DetailView):
    model = Certification
    template_name = 'resume_builder/certification/certification_detail.html'
    context_object_name = 'certification'

class AwardListView(RelatedObjectListView):
    model = Award
    template_name = 'resume_builder/award/award_list.html'
    context_object_name = 'awards'

class AwardCreateView(RelatedObjectCreateView):
    model = Award
    form_class = AwardForm
    template_name = 'resume_builder/award/award_form.html'

class AwardUpdateView(BaseResumeFormMixin, OwnerRequiredMixin, UpdateView):
    model = Award
    form_class = AwardForm
    template_name = 'resume_builder/award/award_form.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})

class AwardDeleteView(OwnerRequiredMixin, DeleteView):
    model = Award
    template_name = 'resume_builder/award/award_confirm_delete.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})
    form_class = EmptyForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('user', None)
        return kwargs

class AwardDetailView(OwnerRequiredMixin, DetailView):
    model = Award
    template_name = 'resume_builder/award/award_detail.html'
    context_object_name = 'award'

class LanguageListView(RelatedObjectListView):
    model = Language
    template_name = 'resume_builder/language/language_list.html'
    context_object_name = 'languages'

class LanguageCreateView(RelatedObjectCreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'resume_builder/language/language_form.html'

class LanguageUpdateView(BaseResumeFormMixin, OwnerRequiredMixin, UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = 'resume_builder/language/language_form.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})

class LanguageDeleteView(OwnerRequiredMixin, DeleteView):
    model = Language
    template_name = 'resume_builder/language/language_confirm_delete.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})
    form_class = EmptyForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('user', None)
        return kwargs

class LanguageDetailView(OwnerRequiredMixin, DetailView):
    model = Language
    template_name = 'resume_builder/language/language_detail.html'
    context_object_name = 'language'

class TechnicalSkillListView(RelatedObjectListView):
    model = TechnicalSkill
    template_name = 'resume_builder/technical_skill/technical_skill_list.html'
    context_object_name = 'technical_skills'

class TechnicalSkillCreateView(RelatedObjectCreateView):
    model = TechnicalSkill
    form_class = TechnicalSkillForm
    template_name = 'resume_builder/technical_skill/technical_skill_form.html'

class TechnicalSkillUpdateView(BaseResumeFormMixin, OwnerRequiredMixin, UpdateView):
    model = TechnicalSkill
    form_class = TechnicalSkillForm
    template_name = 'resume_builder/technical_skill/technical_skill_form.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})

class TechnicalSkillDeleteView(OwnerRequiredMixin, DeleteView):
    model = TechnicalSkill
    template_name = 'resume_builder/technical_skill/technical_skill_confirm_delete.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.resume.pk})
    form_class = EmptyForm
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('user', None)
        return kwargs

class TechnicalSkillDetailView(OwnerRequiredMixin, DetailView):
    model = TechnicalSkill
    template_name = 'resume_builder/technical_skill/technical_skill_detail.html'
    context_object_name = 'technical_skill'

class ResumeListView(LoginRequiredMixin, ListView):
    model = Resume
    template_name = 'resume_builder/resume_list.html'
    context_object_name = 'resumes'

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

class ResumeDetailView(OwnerRequiredMixin, DetailView):
    model = Resume
    template_name = 'resume_builder/resume_detail.html'
    context_object_name = 'resume_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume = self.get_object()
        context['work_experiences'] = resume.work_experiences.all()
        context['educations'] = resume.educations.all()
        context['projects'] = resume.projects.all()
        context['certifications'] = resume.certifications.all()
        context['awards'] = resume.awards.all()
        context['languages'] = resume.languages.all()
        context['technical_skills'] = resume.technical_skills.all()
        return context

class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume_builder/resume_form.html'
    success_url = reverse_lazy('web:resume_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ResumeUpdateView(OwnerRequiredMixin, UpdateView):
    model = Resume
    form_class = ResumeForm
    template_name = 'resume_builder/resume_form.html'
    def get_success_url(self):
        return reverse_lazy('web:resume_detail', kwargs={'pk': self.object.pk})
class ResumeDeleteView(OwnerRequiredMixin, DeleteView):
    model = Resume
    template_name = 'resume_builder/resume_confirm_delete.html'
    success_url = reverse_lazy('web:resume_list')
    form_class = EmptyForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.pop('user', None)
        return kwargs
class ResumeTemplateSelectionView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        resume_id = request.GET.get('resume_id')
        if not resume_id:
            return redirect('web:resume_list')

        resume = get_object_or_404(Resume, pk=resume_id, user=request.user)
        templates = ResumeTemplate.objects.filter(is_active=True).order_by('name')

        context = {
            'resume': resume,
            'templates': templates
        }
        return render(request, 'resume_builder/resume_template_selection.html', context)

    def post(self, request, *args, **kwargs):
        resume_id = request.POST.get('resume_id')
        template_id = request.POST.get('template_id')

        if not resume_id or not template_id:
            return redirect('web:resume_list')

        resume = get_object_or_404(Resume, pk=resume_id, user=request.user)
        template = get_object_or_404(ResumeTemplate, pk=template_id)

        resume.template = template
        resume.save()

        return redirect('web:resume_detail', pk=resume.pk)

class ResumeDownloadView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        file_type = kwargs.get('file_type')

        resume = get_object_or_404(Resume, pk=pk, user=request.user)

        if file_type != 'docx':
            raise Http404("Only DOCX file type is supported for download.")

        response = HttpResponse()
        filename = f"{getattr(resume, 'title', 'untitled_resume').replace(' ', '_').lower()}_docx"

        document = Document()

        document.sections[0].left_margin = Inches(1)
        document.sections[0].right_margin = Inches(1)
        document.sections[0].top_margin = Inches(0.75)
        document.sections[0].bottom_margin = Inches(0.75)

        first_name = getattr(resume, 'first_name', '')
        last_name = getattr(resume, 'last_name', '')
        email = getattr(resume, 'email', '')
        phone = getattr(resume, 'phone', '')
        linkedin_url = getattr(resume, 'linkedin_url', '')
        portfolio_url = getattr(resume, 'portfolio_url', '')
        summary = getattr(resume, 'summary', '')

        if first_name or last_name:
            document.add_heading(f"{first_name} {last_name}".strip(), level=1)

        contact_info_parts = []
        if email:
            contact_info_parts.append(f"Email: {email}")
        if phone:
            contact_info_parts.append(f"Phone: {phone}")
        if contact_info_parts:
            document.add_paragraph(" | ".join(contact_info_parts))

        if linkedin_url:
            document.add_paragraph(f"LinkedIn: {linkedin_url}")
        if portfolio_url:
            document.add_paragraph(f"Portfolio: {portfolio_url}")

        if first_name or last_name or email or phone or linkedin_url or portfolio_url:
            document.add_paragraph("\n")

        if summary:
            document.add_heading('Summary', level=2)
            document.add_paragraph(summary)
            document.add_paragraph("\n")

        if hasattr(resume, 'work_experiences') and resume.work_experiences.exists():
            document.add_heading('Work Experience', level=2)
            for exp in resume.work_experiences.all().order_by('-start_date'):
                document.add_paragraph(f"Job Title: {exp.job_title}")
                document.add_paragraph(f"Company: {exp.company}, {exp.location}")
                document.add_paragraph(f"Dates: {exp.start_date.strftime('%b %Y')} - "
                                        f"{exp.end_date.strftime('%b %Y') if not exp.is_current else 'Current'}")
                if exp.description:
                    document.add_paragraph(exp.description)
                if exp.achievements:
                    try:
                        achievements_list = json.loads(exp.achievements)
                        if achievements_list:
                            document.add_paragraph("Achievements:")
                            for achievement in achievements_list:
                                document.add_paragraph(f"- {achievement}", style='List Bullet')
                    except (json.JSONDecodeError, TypeError):
                        document.add_paragraph(f"Achievements: {exp.achievements}")

                document.add_paragraph("\n")

        if hasattr(resume, 'education_set') and resume.education_set.exists():
            document.add_heading('Education', level=2)
            for edu in resume.education_set.all().order_by('-end_date'):
                document.add_paragraph(f"Degree: {edu.degree}")
                document.add_paragraph(f"Field: {edu.field_of_study}")
                document.add_paragraph(f"Institution: {edu.institution}, {edu.location}")
                document.add_paragraph(f"Dates: {edu.start_date.strftime('%Y')} - {edu.end_date.strftime('%Y')}")
                if edu.description:
                    document.add_paragraph(edu.description)
                document.add_paragraph("\n")

        if hasattr(resume, 'projects') and resume.projects.exists():
            document.add_heading('Projects', level=2)
            for proj in resume.projects.all().order_by('-start_date'):
                document.add_paragraph(f"Project: {proj.title}")
                document.add_paragraph(f"URL: {proj.url if proj.url else 'N/A'}")
                document.add_paragraph(f"Dates: {proj.start_date.strftime('%b %Y')} - "
                                        f"{proj.end_date.strftime('%b %Y') if not proj.is_current else 'Current'}")
                if proj.description:
                    document.add_paragraph(proj.description)
                document.add_paragraph("\n")

        if hasattr(resume, 'technical_skills') and resume.technical_skills.exists():
            document.add_heading('Technical Skills', level=2)
            for skill in resume.technical_skills.all().order_by('technology__name'):
                document.add_paragraph(f"- {skill.technology.name} ({skill.proficiency}, {skill.years_experience} years experience, Last Used: {skill.last_used if skill.last_used else 'N/A'})")
            document.add_paragraph("\n")

        if hasattr(resume, 'certifications') and resume.certifications.exists():
            document.add_heading('Certifications', level=2)
            for cert in resume.certifications.all().order_by('-issue_date'):
                document.add_paragraph(f"- {cert.name} from {cert.issuing_organization} (Issued: {cert.issue_date.strftime('%b %Y')})")
            document.add_paragraph("\n")

        if hasattr(resume, 'awards') and resume.awards.exists():
            document.add_heading('Awards', level=2)
            for award in resume.awards.all().order_by('-date'):
                document.add_paragraph(f"- {award.name} from {award.organizer} (Date: {award.date.strftime('%b %Y')})")
            document.add_paragraph("\n")

        if hasattr(resume, 'languages') and resume.languages.exists():
            document.add_heading('Languages', level=2)
            for lang in resume.languages.all().order_by('name'):
                document.add_paragraph(f"- {lang.name} ({lang.proficiency})")
            document.add_paragraph("\n")

        doc_io = BytesIO()
        document.save(doc_io)
        doc_io.seek(0)

        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
        response['Content-Disposition'] = f'attachment; filename="{filename}.docx"'
        response.write(doc_io.getvalue())

        return response