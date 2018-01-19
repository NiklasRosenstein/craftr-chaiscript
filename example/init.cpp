
#include <chaiscript/chaiscript_basic.hpp>
#include "../static_libs/chaiscript_parser.hpp"
#include "../static_libs/chaiscript_stdlib.hpp"

double function(int i, double j) {
  return i * j;
}

void initChai(chaiscript::ChaiScript_Basic& chai) {
  chai.add(chaiscript::fun(&function), "function");
}
