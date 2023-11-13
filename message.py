from django.conf import settings
from apps.utils.helpers.commons import DateTime


class MessageTemplates:
    @staticmethod
    def otp(name, otp):
        return f"""
        {name.title() + ', ' if name else ''}Your One-Time-Password is {otp}.
        """

    @staticmethod
    def password_reset_email(token: str, page_base_url=None):
        link = f"{page_base_url or settings.PASSWORD_RESET_PAGE}/{token}"
        buttonText = "Reset Password"

        message = f"""
            <p style="color: #fff">Kindly click the link below to continue in resetting your account password.</p>
            <p style="color: #fff"><a href="{page_base_url or settings.PASSWORD_RESET_PAGE}/{token}">{page_base_url or settings.PASSWORD_RESET_PAGE}/{token}</a></p>
            <p style="color: #fff"><b>The above link will expire in {DateTime.convert_seconds_to_hr_min(settings.PASSWORD_RESET_TOKEN_EXPIRATION_SECS)}.</b></p>
            """
        return message

    @staticmethod
    def email_verification_email(
        token: str, name, page_base_url=settings.ACCOUNT_VERIFY_ENDPOINT
    ):
        link = f"{page_base_url}?token={token}"

        email_template = """
            <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
            <html xmlns="http://www.w3.org/1999/xhtml">
                <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>{{ subject }}</title>
                </head>

                <body style="font-family: Helvetica, Arial, sans-serif; margin: 0px; padding: 0px; background-color: #ffffff;">
                    <table role="presentation"
                        style="width: 100%; border-collapse: collapse; border: 0px; border-spacing: 0px; font-family: Arial, Helvetica, sans-serif; background-color: rgb(239, 239, 239);">
                        <tbody>
                        <tr>
                            <td align="center" style="padding: 1rem 2rem; vertical-align: top; width: 100%;">
                            <table role="presentation" style="max-width: 600px; border-collapse: collapse; border: 0px; border-spacing: 0px; text-align: left;">
                                <tbody>
                                <tr>
                                    <td style="padding: 40px 0px 0px;">
                                        <div style="padding: 20px; background-color: rgb(255, 255, 255);">
                                            <div style="color: rgb(0, 0, 0); text-align: left;">
                                                <h1 style="margin: 1rem 0">Hi {name},</h1>
                                                <p style="padding-bottom: 16px">Follow this link to verify your account.</p>
                                                <p style="padding-bottom: 16px"><a href="{link}" target="_blank"
                                                    style="padding: 12px 24px; border-radius: 4px; color: #FFF; background: #2B52F5;display: inline-block;margin: 0.5rem 0;">Confirm
                                                    now</a></p>
                                                <p style="padding-bottom: 16px">If you didn’t ask to verify this address, you can ignore this email.</p>
                                                <p style="padding-bottom: 16px">Thanks! - <br>The Exam-Quest Team</p>
                                            </div>
                                        </div>

                                    </td>
                                </tr>
                                </tbody>
                            </table>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                    </body>
            </html>
        """.format(
            name=name, link=link
        )

        return email_template

    @staticmethod
    def email_verification_success():
        message = f"""
                <p style="color: #fff">Your email has been verified successfully.</p>
                """
        return message
