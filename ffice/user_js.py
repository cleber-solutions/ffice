def generate_user_js(profilepath):
    user_js_path = profilepath / 'user.js'
    if user_js_path.exists():
        return

    user_js = (
        'user_pref("browser.cache.disk.enable", false);\n'
        'user_pref("browser.cache.disk.capacity", 0);\n'
        'user_pref("browser.cache.disk.filesystem_reported", 1);\n'
        'user_pref("browser.cache.disk.smart_size.enabled", false);\n'
        'user_pref("browser.cache.disk.smart_size.first_run", false);\n'
        'user_pref("browser.cache.disk.smart_size.use_old_max", false);\n'
        'user_pref("browser.ctrlTab.previews", true);\n'
        'user_pref("browser.tabs.warnOnClose", false);\n'
        'user_pref("plugin.state.flash", 2);\n'
        'user_pref('
        '"toolkit.legacyUserProfileCustomizations.stylesheets", true'
        ');'
    )
    with user_js_path.open('w') as file_obj:
        file_obj.write(user_js)
