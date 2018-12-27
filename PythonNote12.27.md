# sending emails
```
def send_email(email):
    from django.core.mail import EmailMultiAlternatives
    subject, from_email = 'Test email from MySite', 'xxxx@sina.com'
    text_content = 'This is an important message.'
    html_content = '<p>This is an <strong>important</strong> message.</p>'
    msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
```
There should be text content in the email content, cuz some customer's email may not support html content.
