#!/usr/bin/env python3
# -*- coding: utf-8 -*-
' 序列化 '

import pickle

d = {
    'name': 'Peter wung',
    'age': 20,
    'score': 88
}

d['name'] = 'Peak'
d['age'] = 21
d['score'] = 99

print(d)

with open('serialization-1', 'wb') as f:
    pickle.dump(d, f)