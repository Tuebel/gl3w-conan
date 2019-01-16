from conans import ConanFile, CMake
import os


class Gl3wTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "gl3w/0.1@tuebel/experimental", "glfw/3.2.1@bincrafters/stable"
    generators = "cmake"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=True", "fPIC=True"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
