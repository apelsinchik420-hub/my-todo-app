[app]
title = My Todo App
package.name = mytodoapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy

# Фиксируем стабильные версии Android инструментов, чтобы избежать ошибок
android.sdk = 33
android.ndk = 25b
android.api = 33
android.minapi = 21
android.allow_backup = True

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a
android.accept_sdk_license = True
