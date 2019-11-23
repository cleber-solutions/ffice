# ffice

And Ice-like program to run webapps inside Firefox.

## Usage

    ffice https://example.org

This will create a new profile named `example.com`.

If you want to group some webapps under the same profile (if you intend to
use a common OAuth2 login, for instance), just name it this way:

    ffice https://gmail.com --profile google

If you just want to create all necessary files but **not** actually run
Firefox immediately, use the "show command" flag:

    ffice https://example.org --show-command
    firefox -profile /home/USER/.ffice/firefox/example.org -no-remote -new-instance "https://example.org"


## Environment variables

To change the configuration directory, export the `FFICE_CONFIG_DIR`
environment variable.
