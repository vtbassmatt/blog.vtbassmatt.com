This is the source for http://blog.vtbassmatt.com, "Computer Science + Beer".

Initial setup
=============

1. Create a virtualenv and switch into it.
2. `pip install pelican markdown Fabric`
3. Make sure the theme, crowsfoot, is available: `git clone https://github.com/vtbassmatt/crowsfoot.git`
4. Edit pelicanconf.py to make `THEME` point to the theme directory.

Regular publishing
==================

1. Edit or create some content in `content/`.
2. `fab build` to preview locally.
3. `fab preview` to generate the live site without publishing.
4. `fab publish` to go live.
