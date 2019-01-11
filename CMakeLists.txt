project(gl3w)

cmake_minimum_required(VERSION 3.0)

# builds a static library from gl3w which can be linked against
add_library(gl3w)
target_sources(gl3w PRIVATE gl3w/src/gl3w.c)
target_include_directories(gl3w PUBLIC gl3w/include)