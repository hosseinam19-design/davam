[app]
title = Dovam Samen Card
package.name = dovamsamencard
package.domain = ir.dovamsamen
source.dir = .
source.include_exts = py,png,jpg,jpeg,webp,ttf,json
version = 1.0.0
requirements = python3,kivy,pillow,arabic-reshaper,python-bidi,qrcode
orientation = landscape
fullscreen = 0
android.api = 35
android.minapi = 23
android.archs = arm64-v8a,armeabi-v7a
android.permissions = READ_MEDIA_IMAGES
android.allow_backup = True
android.uses_cleartext_traffic = False
icon.filename = %(source.dir)s/assets/davam_logo_transparent.png

[buildozer]
log_level = 2
warn_on_root = 1
