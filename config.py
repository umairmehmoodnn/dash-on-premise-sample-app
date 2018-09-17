import os

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# This file only needs to be filled out if you wish to set                #
# DASH_APP_PRIVACY to 'private' or 'secret'                               #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Set to 'private' if you want to add a login screen to your app
# You can choose who can view the app in your list of files
# at <your-plotly-server>/organize.
# Set to 'public' if you want your app to be accessible to
# anyone who has access to your Plotly server on your network without
# a login screen.
# Set to 'secret' if you want to add a login screen, but allow it
# to be bypassed by using a secret "share_key" parameter.
DASH_APP_PRIVACY = 'public'

# Fill in with your Plotly On-Premise username
os.environ['PLOTLY_USERNAME'] = 'your-plotly-username'

# Fill in with your Plotly On-Premise API key
# See <your-plotly-server>/settings/api to generate a key
# If you have already created a key and saved it on your own machine
# (from the Plotly-Python library instructions at https://plot.ly/python/getting-started)
# then you can view that key in your ~/.plotly/.config file
# or inside a Python session with these commands:
# import plotly
# print(plotly.tools.get_config_file())
os.environ['PLOTLY_API_KEY'] = 'your-plotly-api-key'

# Fill in with your Plotly On-Premise domain
os.environ['PLOTLY_DOMAIN'] = 'https://your-plotly-domain.com'
os.environ['PLOTLY_API_DOMAIN'] = os.environ['PLOTLY_DOMAIN']

# Fill in with the domain of your Dash subdomain.
# This matches the domain of the Dash App Manager
PLOTLY_DASH_DOMAIN = 'https://your-dash-manager-plotly-domain.com'

# Keep as True if your SSL certificates are valid.
# If you are just trialing Plotly On-Premise with self signed certificates,
# then you can set this to False. Note that self-signed certificates are not
# safe for production.
os.environ['PLOTLY_SSL_VERIFICATION'] = 'True'
