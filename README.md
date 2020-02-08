# Westerly

    A wind blows over the C
    so strong that it moves 'const' you see
    from the west to the east
    some of 'em at least

Westerly is a script to re-arrange `const` in your C/C++ source files to 
follow east-const convention. Plenty of articles have been written about 
why you would want to do that, I'm not going to repeat the arguments here 
and will instead assume that you have arrived here because you are 
convinced of the merits.

## Installation

You can install westerly via pip:

```bash
pip install westerly
```

## Usage


Once installed you can use the following command to run westerly on a 
source file:

```bash
westerly $file
```

By default, the rewritten source will be written to stdout. To perform 
the replacement in-place, pass the `--in-place` option:

```bash
westerly --in-place $file
```

It is highly recommended that you only run westerly on version-controlled 
source-code, so you can go back in case something goes wrong. Westerly uses 
a set of heuristics to determine which consts to move and where, it doesn't 
actually have a full understanding of C++ syntax. No heuristic is perfect. 
**You have been warned.**

It is also highly recommended to pass the changed code through 
`clang-format` (or `git clang-format`) as westerly will sometimes mess up 
formatting a bit. 

## Example

```
> cat example.ccp
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

  return argc < kAConstant ? 0 : -1;
}
```

```
> westerly example.cpp
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

  return argc < kAConstant ? 0 : -1;
}
```

# Limitations

Since the script doesn't have a full understanding of C++, it only uses 
the local token sequence to determine which of the consts are west-const 
that need moving. It does not properly handle the following:

- macros for type attributes places to the left of the type trick 
  `westerly` into thinking that a west-const is an east-const. Example:
  ```cpp
  # define WARN_UNUSED __attribute__((warn_unused))
  WARN_UNUSED const int kSomeConstant = 5
  ```
  The code will be left as is.
- `westerly` does not attempt to move the placement of `const` inside macro 
  definitions.


# FAQ

## Why, oh why?

Because sometimes you have solved all business cases and all that there
is left to do is to cleanup up code and make it consistent. Yes, seriously.

## Is this script save to use?

Short answer: Nope. Long answer: you should most likely be fine running this 
script over a couple of source files at once and then checking by eye (and 
compiler) that everything is fine. I would not recommend to run the script 
over hundreds of source files at once at this stage.

## Why doesn't westerly have options to control spacing around const?

I get it, you don't like the spaces westerly puts around `const`. You 
would rather prefer to have it output `const&` instead of `const &`. You 
are not alone. Surrounding `const` with spaces on boths sides is just 
the pragmatic choice as there is no danger of fusing `const` with 
surrounding tokens by accident. As mentioned above, you should pass your 
code through `clang-format` after running westerly, which has plenty of 
options to configure spaces around `const`.
