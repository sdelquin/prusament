import re
from pathlib import Path

import jinja2
import logzero
from sendgrify import SendGrid

import settings


def init_logger():
    console_logformat = (
        '%(asctime)s '
        '%(color)s'
        '[%(levelname)-8s] '
        '%(end_color)s '
        '%(message)s '
        '%(color)s'
        '(%(filename)s:%(lineno)d)'
        '%(end_color)s'
    )
    # remove colors on logfile
    file_logformat = re.sub(r'%\((end_)?color\)s', '', console_logformat)

    console_formatter = logzero.LogFormatter(fmt=console_logformat)
    file_formatter = logzero.LogFormatter(fmt=file_logformat)
    logzero.setup_default_logger(formatter=console_formatter)
    logzero.logfile(
        settings.LOGFILE,
        maxBytes=settings.LOGFILE_SIZE,
        backupCount=settings.LOGFILE_BACKUP_COUNT,
        formatter=file_formatter,
    )
    return logzero.logger


def init_jinja():
    loader = jinja2.FileSystemLoader(settings.EMAIL_TEMPLATES_DIR)
    env = jinja2.Environment(loader=loader)
    return env


def render_message(args: dict, template_name: Path) -> str:
    jinja_env = init_jinja()
    template = jinja_env.get_template(template_name)
    return template.render(**args)


def init_sendgrid(
    apikey=settings.SENDGRID_APIKEY,
    from_email=settings.SENDGRID_FROM_EMAIL,
    from_name=settings.SENDGRID_FROM_NAME,
):
    return SendGrid(apikey, from_email, from_name)
