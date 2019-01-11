project(gl3w)

cmake_minimum_required(VERSION 2.8.12)

# add and depend on OpenGL
find_package(OpenGL REQUIRED)

# builds a static library from gl3w which can be linked against
add_library(gl3w)
target_sources(gl3w PRIVATE gl3w/src/gl3w.c)
target_include_directories(gl3w PUBLIC gl3w/include)
target_link_libraries(gl3w PUBLIC OpenGL::GL OpenGL::GLU)
