#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#______  ___       ______  ________                _________#             
#___   |/  /______ ___  /_ ___  __/______________ _______  /_____ ________#
#__  /|_/ / _  __ \__  __ \__  /   __  ___/_  __ `/_  __  / _  _ \__  ___/#
#_  /  / /  / /_/ /_  /_/ /_  /    _  /    / /_/ / / /_/ /  /  __/_  /# 
#/_/  /_/   \____/ /_.___/ /_/     /_/     \__,_/  \__,_/   \___/ /_/# 
#FULL MHI V 1.0 - Contato: +55 (11) 9 7615-9233#

import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
