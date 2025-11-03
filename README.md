# CoRT skill icons

This repo includes all icons used by the trainer, and a script allowing to
automatically create new skills icons bars (skillbars), which usage will be
described here.

The icons are used as fair use, and are property of NGE.

## Pre requisites

- Basic (Terminal|Powershell) knowledge, called terminal later
- Python 3 (v3.11 tested)
    - Windows: On Windows 11 at least, open Powershell, type 'python3' and follow Microsoft Store's directives
    - macOs: python3 is already installed if you've Big Sur or newer
- The Python 3 `pillow` (v10 tested) [module](https://pillow.readthedocs.io/en/stable/installation.html#basic-installation)
- A valid `trainerdata.json`

## Installing pillow

Note that you only need to do it once.

### Windows / Mac

```
pip install -r requirements.txt
```

### Linux

You can use pillow from your package manager. (Debian: `python3-pillow`)

## Basic Usage

- Open a terminal
- Type the following command:

```
cd where/is/CoRT-icons
python3 icons_to_skillbar.py where/is/CoRT/data/<your version number>/trainerdata.json
```

You will find the new icons at `where/is/CoRT/data/<your version
number>/icons`. Meaning that if you followed the instructions of CoRT's
`UPDATING.md` the icons will be automatically updated without any further
action needed.

## Testing

Since python is installed, you've already a webserver ready, so you can
checkout the site by doing:

```
cd where/is/CoRT
python3 -m http.server -b localhost 1234
```

And point your browser to [http://localhost:1234](http://localhost:1234).


## Adding a skill/discipline icon

The expected filename is `<skill/discipline name as written in trainerdata.json>.png`, to
be placed in the `original_skills_icons` directory, and dimensions should be
64px\*64px. Note that the icons filename is case-sensitive.

Discipline names do not accept any other special characters than space.

Some icons are old skills that are no more used, and can be seen as symbolic
links to new skills that replaced them.

## A skill discipline name changed

You will need to remove the old WEBP file and regenerate icons.

## How these icons has been extracted?

This has been done by extracting the game's DDS textures `data1.sdb` with
[X-Ripper](https://www.zeus-software.com/downloads/xripper), then triaged by
size (64x64) with [XnView](https://www.xnview.com/en/), and finally sorted...
by hand!

Inquisition had an extractor for sdb files, but probably due to possible legal
concerns they didn't made it public, and nowadays the skill texture names are a
mix of Spanish and English...
