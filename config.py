# ----------------------------------------------- #
# Plugin Name           : TradingView-Webhook-Bot #
# Author Name           : fabston                 #
# File Name             : config.py               #
# ----------------------------------------------- #

# TradingView Example Alert Message:
{
"key":"gundulPacul777", "telegram":"-1001672905672", "msg":"Long #{{ticker}} at `{{close}}`"
}

sec_key = (
    "gundulPacul777"  # Can be anything. Has to match with "key" in your TradingView alert message
)

# Telegram Settings
send_telegram_alerts = True
tg_token = "5056572283:AAF4xqvg_FIqqEw-U3feNW0rN4tYMRBC9gk"  # Bot token. Get it from @Botfather
channel = -1001672905672  # Channel ID (ex. -1001487568087)

# Discord Settings
send_discord_alerts = False
discord_webhook = ""  # Discord Webhook URL (https://support.discordapp.com/hc/de/articles/228383668-Webhooks-verwenden)

# Slack Settings
send_slack_alerts = False
slack_webhook = ""  # Slack Webhook URL (https://api.slack.com/messaging/webhooks)

# Twitter Settings
send_twitter_alerts = False
tw_ckey = ""
tw_csecret = ""
tw_atoken = ""
tw_asecret = ""

# Email Settings
send_email_alerts = False
email_sender = ""  # Your email address
email_receivers = ["", ""]  # Receivers, can be multiple
email_subject = "Trade Alert!"

email_port = 465  # SMTP SSL Port (ex. 465)
email_host = ""  # SMTP host (ex. smtp.gmail.com)
email_user = ""  # SMTP Login credentials
email_password = ""  # SMTP Login credentials
