#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweet_clean as tc
import re


str1 = u'इंदापूर तालुक्यातील भवानीनगरच्य श्र छत्रपत सहकार साखर कारखान्याच १८ मेगावॅट क्षमतेच सहवीज निर्मि प्रकल्प व'

print tc.clean_tweet(str1)
#print tc.clean_tweet(str2.decode('utf-8'))
