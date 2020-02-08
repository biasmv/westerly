#include <string>

const int kAConstant = 55;

#define SOME_MACRO(arg)

/*
 Using declarations are no issue for us at all
 */
using IntTriplet = const int[3];
using IntPointer = const int*;

const static std::string kPrivateVar1 = "";
static const std::string kPrivateVar2 = "";

/*
 Comments containing const keywords are ignored as they should be.
 */
using ConstStringRef = const std::string&;
using ConstStringRef2 = const ::std::string&;

int main(int argc, const char *const *argv) {
  auto const kUnusedStringLiteral = R"cpp(
       const int kFoo = 33;
  )cpp";
  const std::vector<int> vector_of_ints{
      1, 2, 3, 4, 5, 6,
  };
  const std::vector<const char*> vector_of_strings{
      kUnusedStringLiteral, 
      kUnusedStringLiteral,
  };
  SOME_MACRO(const);
  return argc < kAConstant ? 0 : -1;
}

