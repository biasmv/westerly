/*
 This file contains a bunch of test cases where comments are interleaved
 with type definitions. Some of those are very unlikely to happen in 
 real code-bases, but then again...
 */
#include <string>

// Foo
std::string const kFoo1 = "foo";

// Foo
std::string const kFoo2 = "foo";

std::string 
const // Foo
kFoo3 = "foo";

/* Foo */ std::string const kFoo4 = "foo";
/* Foo */ std::string const kFoo5 = "foo";
std::string const /* Foo */ kFoo6 = "foo";

