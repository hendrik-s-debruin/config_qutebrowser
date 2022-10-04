from os.path import expanduser

config.load_autoconfig(False)

# ==============================================================================
# Global Vars
# ==============================================================================
js_scripts_directory = expanduser("~") + "/.config/qutebrowser/js"

# ==============================================================================
# Command Aliases
# ==============================================================================
c.aliases = {'w': 'session-save',
    'q':      'quit',
    'wq':     'quit --save',
    'v':      'spawn --userscript ~/.config/qutebrowser/myscripts/zathura.sh',
    'bmark':  'bookmark-add',
    'rebash': 'config-source',
    'blank':  'open about:blank',
    }

# ==============================================================================
# Theme
# ==============================================================================
background   = "#32302f"
foreground   = "#ebdbb2"
highlight    = "#3c3836"
black        = "#282828"
gray         = "#928374"
lightgray    = "#202020"
white        = "#a89984"
red          = "#cc241d"
lightred     = "#fb4934"
green        = "#98971a"
lightgreen   = "#b8bb26"
orange       = "#d79921"
yellow       = "#fabd2f"
blue         = "#458588"
lightblue    = "#83a598"
magenta      = "#b16286"
lightmagenta = "#d3869b"
cyan         = "#689d6a"
lightcyan    = "#8ec07c"

# ==================================== Fonts ===================================
c.fonts.default_family = "Source Code Pro"

# ============================== Completion Widget =============================
c.colors.completion.category.bg                 = background
c.colors.completion.category.border.bottom      = background
c.colors.completion.category.border.top         = gray
c.colors.completion.category.fg                 = foreground
c.colors.completion.even.bg                     = background
c.colors.completion.odd.bg                      = background
c.colors.completion.fg                          = [foreground, foreground, foreground]
c.colors.completion.item.selected.bg            = background
c.colors.completion.item.selected.border.bottom = background
c.colors.completion.item.selected.border.top    = background
c.colors.completion.item.selected.fg            = yellow
c.colors.completion.match.fg                    = yellow
c.colors.completion.scrollbar.bg                = background
c.colors.completion.scrollbar.fg                = foreground

# ================================ Download Bar ================================
c.colors.downloads.bar.bg                       = background
c.colors.downloads.error.bg                     = red
c.colors.downloads.error.fg                     = foreground
c.colors.downloads.start.bg                     = blue
c.colors.downloads.start.fg                     = foreground
c.colors.downloads.stop.bg                      = green
c.colors.downloads.stop.fg                      = foreground

# =================================== Hinting ==================================
c.colors.hints.bg                               = background
c.colors.hints.fg                               = foreground
c.colors.hints.match.fg                         = green

# ================================== Keyhings ==================================
c.colors.keyhint.bg                             = 'rgba(0, 0, 0, 80%)'
c.colors.keyhint.fg                             = foreground
c.colors.keyhint.suffix.fg                      = yellow

# ================================== Messages ==================================
# ----------------------------------- Errors -----------------------------------
c.colors.messages.error.bg                      = red
c.colors.messages.error.border                  = red
c.colors.messages.error.fg                      = foreground

# ------------------------------------ Info ------------------------------------
c.colors.messages.info.bg                       = background
c.colors.messages.info.border                   = background
c.colors.messages.info.fg                       = foreground

# ---------------------------------- Warnings ----------------------------------
c.colors.messages.warning.bg                    = background
c.colors.messages.warning.border                = background
c.colors.messages.warning.fg                    = yellow

# =================================== Prompts ==================================
c.colors.prompts.bg                             = background
c.colors.prompts.border                         = '3px solid ' + background
c.colors.prompts.fg                             = foreground
c.colors.prompts.selected.bg                    = yellow

# ==================================== Modes ===================================
# -------------------------------- Command Mode --------------------------------
c.colors.statusbar.command.bg                   = background
c.colors.statusbar.command.fg                   = foreground
c.colors.statusbar.command.private.bg           = background
c.colors.statusbar.command.private.fg           = foreground

# --------------------------------- Insert Mode --------------------------------
c.colors.statusbar.insert.bg                    = blue
c.colors.statusbar.insert.fg                    = foreground

# --------------------------------- Normal Mode --------------------------------
c.colors.statusbar.normal.bg                    = background
c.colors.statusbar.normal.fg                    = foreground

# ------------------------------ Passthrough Mode ------------------------------
c.colors.statusbar.passthrough.bg               = magenta
c.colors.statusbar.passthrough.fg               = foreground

# -------------------------------- Private Mode --------------------------------
c.colors.statusbar.private.bg                   = background
c.colors.statusbar.private.fg                   = yellow

# ==================================== URLs ====================================
c.colors.statusbar.url.error.fg                 = orange
c.colors.statusbar.url.fg                       = foreground
c.colors.statusbar.url.hover.fg                 = foreground
c.colors.statusbar.url.success.http.fg          = foreground
c.colors.statusbar.url.success.https.fg         = 'lime'
c.colors.statusbar.url.warn.fg                  = yellow

# ==================================== Tabs ====================================
c.colors.tabs.selected.odd.bg                   = background
c.colors.tabs.selected.odd.fg                   = foreground

# ==============================================================================
# Behaviour
# ==============================================================================
c.confirm_quit              = ['downloads']
c.content.cookies.accept    = 'no-3rdparty'
c.content.pdfjs             = False
c.content.fullscreen.window = True
c.spellcheck.languages      = ["af-ZA", "de-DE", "en-GB", "it-IT", "es-ES", "fr-FR", "ru-RU"]
c.tabs.show                 = 'never'
c.tabs.tabs_are_windows     = True
c.url.default_page          = 'about:blank'
c.url.start_pages           = ['about:blank']

# ==============================================================================
# Bindings
# ==============================================================================
# ================================= Normal Mode ================================
config.bind('<Ctrl-e>', 'scroll down')
config.bind('<Ctrl-y>', 'scroll up')
config.bind('E', 'open-editor')
config.bind('zi', 'zoom-in')
config.bind('zo', 'zoom-out')
config.bind('zz', 'zoom 100')
config.bind('J', 'scroll-page 0 1')
config.bind('K', 'scroll-page 0 -1')
config.bind('c', 'tab-clone')
config.bind("s", "jseval --file " + js_scripts_directory + "/scroll.js")
config.bind("S", "jseval --file " + js_scripts_directory + "/noscroll.js")
config.bind('w', 'jseval document.body.style.backgroundColor = "white";')
config.unbind("d") # do not close window

# ==============================================================================
# Search Engines
# ==============================================================================
c.url.searchengines = {
    # ================================= General ================================
    # DuckDuckGO
    'DEFAULT': 'https://duckduckgo.com/?q={}',
    'd':       'https://duckduckgo.com/?q={}',
    # Google
    'g':       'http://www.google.com/search?q={}',
    # Youtube
    'y':       'https://www.youtube.com/results?search_query={}',
    # google scholar
    's':       'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q={}',

    # ================================ Reference ===============================
    # CPPreference
    'std':     'https://en.cppreference.com/mwiki/index.php?title=Special%3ASearch&search={}&button=',
    # StackOverflow
    'so':      'https://stackoverflow.com/search?q={}',
    # Python
    'py':      'https://docs.python.org/3.8/search.html?q={}&check_keywords=yes&area=default',
    # Rust
    'rstd' : 'https://doc.rust-lang.org/std/?search={}',
    'rdoc': 'https://docs.rs/releases/search?query={}',

    # ============================== Dictionaries ==============================
    'enit':    'http://www.wordreference.com/enit/{}',
    'iten':    'http://www.wordreference.com/iten/{}',
    'conjit':  'http://www.wordreference.com/conj/ItVerbs.aspx?v={}',

    # Spanish
    'enes':    'http://www.wordreference.com/enes/{}',
    'esen':    'http://www.wordreference.com/esen/{}',
    'conjes':  'http://www.wordreference.com/conj/EsVerbs.aspx?v={}',

    # German
    'ende':    'http://www.wordreference.com/ende/{}',
    'deen':    'http://www.wordreference.com/deen/{}',
    'conjde':  'http://www.verbix.com/webverbix/German/{}.html',

    # French
    'enfr':    'http://www.wordreference.com/enfr/{}',
    'fren':    'http://www.wordreference.com/fren/{}',
    'conjfr':  'http://www.wordreference.com/conj/FrVerbs.aspx?v={}',

    # Russian
    'enru':    'http://www.wordreference.com/enru/{}',
    'ruen':    'http://www.wordreference.com/ruen/{}',
    'руан':    'http://www.wordreference.com/ruen/{}',

    # Czech
    'encz':    'https://slovnik.seznam.cz/preklad/anglicky_cesky/{}',
    'czen':    'https://slovnik.seznam.cz/preklad/cesky_anglicky/{}',

    # Chinese
    'hanzi': 'https://dictionary.writtenchinese.com/#sk={}=pinyin',

    # ================================== IEEE ==================================
    'ieee':    'https://ieeexplore.ieee.org/search/searchresult.jsp?newsearch=true&queryText={}',

    # ================================ Crates.io ===============================
    'cratesio': 'https://crates.io/search?q={}',
    'crates': 'https://crates.io/search?q={}',
    'cr': 'https://crates.io/search?q={}',

    # ============================== stackoverflow =============================
    'so': 'https://stackoverflow.com/search?q={}',

    # =================================== Go ===================================
    'gl': 'https://pkg.go.dev/search?q={}'
}
