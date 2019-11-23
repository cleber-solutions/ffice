def generate_user_chrome(chromepath):
    user_chrome_path = chromepath / 'userChrome.css'
    if user_chrome_path.exists():
        return

    user_chrome = (
        '#nav-bar { '
        'max-height: 0 !important; margin-bottom: -20px '
        '!important; opacity: 0; } '
        '#identity-box, #navigator-toolbox::after, #tabbrowser-tabs '
        '{  --tab-min-height: 0px !important;  margin-left: 0px !important; '
        'height: 0px !important; }'
    )
    with user_chrome_path.open('w') as file_obj:
        file_obj.write(user_chrome)
