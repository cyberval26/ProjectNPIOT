[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = com.tugasakhiriot.nopark

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) Source files to exclude (let empty to not exclude anything)
#source.exclude_exts = spec

# (list) List of directory to exclude (let empty to not exclude anything)
#source.exclude_dirs = tests, bin

# (list) List of exclusions using pattern matching
#source.exclude_patterns = license,images/*/*.jpg

# (str) Application versioning (method 1)
version = 0.1

# (str) Application versioning (method 2)
# version.regex = __version__ = ['"](.*)['"]
# version.filename = %(source.dir)s/main.py

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3crystax==3.8.8, kivy==2.0.0, kivymd==0.104.2, google-auth, google-auth-oauthlib, google-auth-httplib2, firebase-admin

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (bool) Run the application in debug mode
#build_mode = debug

# (str) Package the application for Android platform, arch can be
# armeabi-v7a (ARM 32bits), arm64-v8a (ARM 64bits), x86 (Intel 32bits),
# x86_64 (Intel 64bits), and all for universal apk
#
# Note that you can run `buildozer android release` to build an apk in release
# mode.
android.arch = armeabi-v7a

# (int) Android API to use
android.api = 30

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
#android.sdk = 20

# (str) Android NDK version to use
#android.ndk
target=android
