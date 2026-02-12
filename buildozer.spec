[app]
title = anjes
package.name = todoapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# المتطلبات الأساسية
requirements = python3,kivy

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

# هذه الإعدادات مهمة لتخطي مشاكل التحميل
android.accept_sdk_license = True
build_mode = debug
