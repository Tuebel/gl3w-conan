#include <GL/gl3w.h>
#include <GLFW/glfw3.h>
#include <iostream>

int main(int argc, char **argv)
{
  int glfw_res = glfwInit();
  if (glfw_res == GLFW_FALSE)
  {
    std::cout << "failed to init glfw"
              << "\n";
    return EXIT_FAILURE;
  }
  else
  {
    std::cout << "succeeded to init glfw"
              << "\n";
  }
  // compability requirements
  glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
  glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 2);
  glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
  glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
  glfwWindowHint(GLFW_RESIZABLE, GL_FALSE);
  auto window = glfwCreateWindow(640, 480, "test_package", NULL, NULL);
  if (!window)
  {
    std::cout << "failed to create glfw context\n";
    return EXIT_FAILURE;
  }
  else
  {
    std::cout << "succeeded to create glfw context\n";
  }
  glfwMakeContextCurrent(window);
  int success = gl3wInit();
  if (gl3wInit())
  {
    std::cout << "failed to init gl3w " << success << "\n";
    glfwDestroyWindow(window);
    glfwTerminate();
    return EXIT_FAILURE;
  }
  if (!gl3wIsSupported(4, 2))
  {
    std::cout << "succeeded to init gl3w\n";
    glfwDestroyWindow(window);
    glfwTerminate();
    return EXIT_SUCCESS;
  }
}
