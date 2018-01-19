
#include <chaiscript/chaiscript_basic.hpp>
#include "../static_libs/chaiscript_parser.hpp"
#include "../static_libs/chaiscript_stdlib.hpp"

void initChai(chaiscript::ChaiScript_Basic&);

int main() {
  chaiscript::ChaiScript_Basic chai(create_chaiscript_stdlib(), create_chaiscript_parser());
  initChai(chai);
  double d = chai.eval<double>("function(3, 4.75);");
  std::cout << d << "\n";
  return 0;
}
