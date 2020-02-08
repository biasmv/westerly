/*
 This file contains a bunch of test cases where comments are interleaved
 with type definitions. Some of those are very unlikely to happen in 
 real code-bases, but then again...
 */
#include <string>

// Foo
const std::string kFoo1 = "foo";

const
// Foo
std::string kFoo2 = "foo";

const std::string 
// Foo
kFoo3 = "foo";

/* Foo */ const std::string kFoo4 = "foo";
const /* Foo */ std::string kFoo5 = "foo";
const std::string /* Foo */ kFoo6 = "foo";
