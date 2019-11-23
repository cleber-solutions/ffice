# ffice

And Ice-like program to run webapps inside Firefox.

## Motivations

### Ice is a really interesting tool

But its code is not the best Python possible. Besides, it embeds some
Peppermint's things...

### I don't trust Chrome/Chromium

Yeah, but when a company that earns from advertising is your main sponsor
I doubt you'd put that much effort into protecting your users privacy.

## Install

    pip install 'git+https://github.com/cleber-solutions/ffice.git'

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
