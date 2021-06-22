#include <string>

class Foo {
  public:
    const std::string bar1;
    const std::string bar2;

  private:
    const static std::string bar3;
    static const std::string bar4;
}
