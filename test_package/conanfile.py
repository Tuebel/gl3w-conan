from conans import ConanFile, CMake
import os


class Gl3wTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "gl3w/latest@user/testing", "glfw/3.2.1@bincrafters/stable"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir=self.source_folder, build_dir="./")
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")
        self.copy("*.dylib*", dst="bin", src="lib")

    def test(self):
        os.chdir("bin")
        self.run(".%sexample" % os.sep)
