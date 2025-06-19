# Assignment 3: Django Allauth Customization

## Objective

Complete the user authentication module by implementing and customizing all Django Allauth templates, including email templates for password reset and account activation. Test the full authentication flow.

---

## Tasks

### 1. Implement Allauth Templates

Create and customize the following templates in the `templates/account/` directory:

- `login.html`
- `logout.html`
- `logout_confirm.html`
- `signup.html`
- `password_reset.html`
- `password_reset_done.html`
- `password_reset_from_key.html`
- `password_reset_from_key_done.html`
- `password_change.html`
- `password_change_done.html`
- `email.html`
- `email_confirm.html`
- `confirm_email.html`
- `inactive.html`
- `verification_sent.html`

Each template should:
- Extend the appropriate base template.
- Use Bootstrap or your project’s CSS for styling.
- Provide a user-friendly interface.

---

### 2. Customize Email Templates

Implement custom HTML email templates for:

- Account activation (`email_confirm.html`)
- Password reset (`password_reset_email.html`)

Templates should:
- Be visually appealing and match your project branding.
- Include clear instructions and working action links.

---

### 3. Testing

- Register a new user and verify the account activation email.
- Test login, logout, and password reset flows.
- Ensure all templates render correctly and emails are sent with your custom design.

---

## Submission

- Push all template files to your repository.
- Include screenshots of each page and email received.
- Write a short report describing your testing process and any issues encountered.

---

**Deadline:** _[2025/06/28]_