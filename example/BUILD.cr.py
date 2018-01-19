
namespace = 'chaiscript-example'

import cxx from 'craftr/lang/cxx'
import 'craftr-chaiscript'

cxx.binary(
  name = 'main',
  deps = ['//craftr-chaiscript:chaiscript-static'],
  srcs = ['main.cpp', 'init.cpp']
)

cxx.run(':main')
