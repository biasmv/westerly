#include <string>

int const kAConstant = 55;

#define SOME_MACRO(arg)

/*
 Using declarations are no issue for us at all
 */
using IntTriplet = int const [3];
using IntPointer = int const *;

static std::string const kPrivateVar1 = "";
static std::string const kPrivateVar2 = "";

/*
 Comments containing const keywords are ignored as they should be.
 */
using ConstStringRef = std::string const &;
using ConstStringRef2 = ::std::string const &;

int main(int argc, char const *const *argv) {
  auto const kUnusedStringLiteral = R"cpp(
       const int kFoo = 33;
  )cpp";
  std::vector<int> const vector_of_ints{
      1, 2, 3, 4, 5, 6,
  };
  std::vector<char const *> const vector_of_strings{
      kUnusedStringLiteral, 
      kUnusedStringLiteral,
  };
  SOME_MACRO(const);
  return argc < kAConstant ? 0 : -1;
}


