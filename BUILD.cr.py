
import craftr, {fmt, glob, path} from 'craftr'
import cxx from '@craftr/cxx'

source_dir = craftr.options.get('chaiscript.source_dir')
gitref = craftr.options.get('chaiscript.gitref', 'v6.0.0')
if not source_dir:
  url = fmt('https://github.com/ChaiScript/ChaiScript/archive/{gitref}.zip')
  source_dir = path.join(craftr.get_source_archive(url), 'ChaiScript-' + gitref.lstrip('v'))

defines = []
if craftr.options.get('chaiscript.no_threads', True):
  defines.append('CHAISCRIPT_NO_THREADS')
if craftr.options.get('chaiscript.no_protect_dividebyzero', False):
  defines.append('CHAISCRIPT_NO_PROTECT_DIVIDEBYZERO')

cxx.prebuilt(
  name = 'chaiscript',
  includes = [path.join(source_dir, 'include')],
  defines = defines
)

cxx.library(
  name = 'chaiscript-static',
  public_deps = [':chaiscript'],
  explicit = True,
  srcs = glob('static_libs/*.cpp', parent=source_dir),
  cpp_std = 'c++11',
  options = dict(
    msvc_compile_flags = ['/bigobj']
  )
)

cxx.binary(
  name = 'main',
  deps = [':chaiscript-static'],
  explicit = True,
  srcs = [path.join(source_dir, 'src/main.cpp')]
)
