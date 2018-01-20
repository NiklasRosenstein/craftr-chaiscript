## @craftr/chaiscript

### Options

* `chaiscript.source_dir` (default: `null`)
* `chaiscript.gitref` (default: `"v6.0.0"`)
* `chaiscript.no_threads` (default: `true`)
* `chaiscript.no_protected_dividebyzero` (default: `false`)

### Example

If you want to avoid compiling the ChaiScript standard library into
every translation unit, you need to use the following includes (below)
and depend on the `//@craftr/chaiscript:chaiscript-static` target.

```cpp
#include <chaiscript/chaiscript_basic.hpp>
#include "../static_libs/chaiscript_parser.hpp"
#include "../static_libs/chaiscript_stdlib.hpp"

// Create the ChaiScript runtime like this:
chaiscript::ChaiScript_Basic chai(create_chaiscript_stdlib(), create_chaiscript_parser());
```

Otherwise, you may simply depend on the `//@craftr/chaiscript:chaiscript`
target and include the full standard library statically into your translation
unit.

```cpp
#include <chaiscript/chaiscript.hpp>

// Create a ChaiScript runtime like this:
chaiscript::ChaiScript chai;
```

### Compile the ChaiScript CLI

    $ craftr --release --configure --build //@craftr/chaiscript:main
