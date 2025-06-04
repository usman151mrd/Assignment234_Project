# Assignment: Resume Builder Web Application

## What Has Been Done For You

- **PostgreSQL Database Connection**  
  The project is already configured to use PostgreSQL as the database. This is set up in `core/settings.py` using environment variables for security and flexibility.

- **.env File Usage**  
  A `.env` file is used to store sensitive settings (like database credentials and secret keys) outside the codebase.  
  **Benefits:**  
  - Keeps secrets out of version control  
  - Makes it easy to change settings for different environments (development, production, etc.)  
  - Improves security and maintainability

- **NiceAdmin Template Setup**  
  The NiceAdmin Bootstrap 5 template is already integrated. Static files and `base.html` are set up for you. You can extend `base.html` in your templates.

---

## Assignment Instructions

### 1. User Authentication

#### 1.1. Login and Signup Pages
- Use **django-allauth** to implement user login and signup.
- Design the login and signup pages using the NiceAdmin template.
- Ensure the pages extend `base.html` and use static assets from the NiceAdmin theme.

---

### 2. CRUD Operations for Resume Builder Models

For each model in `resume_builder` (e\.g\., WorkExperience, Education, Project, Certification, Award, Language, TechnicalSkill):

#### 2.1. Create (Insert)
- Implement a form to add a new record for each model.
- Use Bootstrap 5 styling from NiceAdmin.
- Validate and save the form data.

#### 2.2. Read (List & Detail)
- Create a list view to display all records for the logged-in user.
- Add a detail view to show all information for a single record.

#### 2.3. Update
- Implement an edit form for each model.
- Pre-fill the form with existing data and allow updates.

#### 2.4. Delete
- Add a delete confirmation page for each model.
- Allow users to delete their own records.

---

### 3. Resume Template Selection and Download

#### 3.1. Template Selection
- Allow users to select a resume template from available options.
- Store the selected template for each user or resume.

#### 3.2. Resume Download
- Implement functionality to generate and download the resume in the selected template format (PDF or DOCX).
- Ensure the downloaded resume uses the chosen template design.

---

## Submission Guidelines

- All pages must extend `base.html` and use NiceAdmin styles.
- All CRUD operations must be available for each model in `resume_builder`.
- Login and signup must use allauth and be styled with NiceAdmin.
- Resume download must reflect the selected template.

---

**Good luck!**