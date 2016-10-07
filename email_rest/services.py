from .models import Email, Attachments
import requests

class Helper:

    def send_email(self, id):

        email = Email.objects.get(pk=id)
        attachments = Attachments.objects.all().filter(email=email)

        files = []
        for attachment in attachments:
            files.append( ("attachment", open(attachment.path)) )

        if (email.is_html == 1):

            return requests.post(
                "https://api.mailgun.net/v3/sandboxf6048140f8e4483b949a6c8ee8ef9d32.mailgun.org/messages",
                auth=("api", "key-218e1c8211e9166a3739b4fae4b9e3a2"),
                files=files,
                data={"from": "Mailgun Sandbox <postmaster@sandboxf6048140f8e4483b949a6c8ee8ef9d32.mailgun.org>",
                      "to": email.to,
                      "subject": email.subject,
                      "html": email.body,
                      "o:tag": email.tag })
        else:

            return requests.post(
                "https://api.mailgun.net/v3/sandboxf6048140f8e4483b949a6c8ee8ef9d32.mailgun.org/messages",
                auth=("api", "key-218e1c8211e9166a3739b4fae4b9e3a2"),
                files=files,
                data={"from": "Mailgun Sandbox <postmaster@sandboxf6048140f8e4483b949a6c8ee8ef9d32.mailgun.org>",
                      "to": email.to,
                      "subject": email.subject,
                      "text": email.body,
                      "o:tag": email.tag })

    def get_logs_events(self):
        return requests.get(
            "https://api.mailgun.net/v3/sandboxf6048140f8e4483b949a6c8ee8ef9d32.mailgun.org/events",
            auth=("api", "key-218e1c8211e9166a3739b4fae4b9e3a2"),
            params={"event" : "opened OR clicked"})

