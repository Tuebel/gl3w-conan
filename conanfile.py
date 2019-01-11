from conans import ConanFile, CMake, tools
import os
import shutil


class Gl3wConan(ConanFile):
    name = "gl3w"
    version = "latest"
    license = "Unlicense"
    url = "https://github.com/Tuebel/gl3w-conan"
    description = "Simple OpenGL core profile loading."
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "CMakeLists.txt"

    def source(self):
        if os.path.exists("gl3w_gen.py"):
            os.remove("gl3w_gen.py")
        if os.path.exists("gl3w"):
            shutil.rmtree("gl3w")
        # download and generate the sources
        tools.download(
            "https://github.com/skaslev/gl3w/raw/master/gl3w_gen.py",
            "gl3w_gen.py")
        self.run("python gl3w_gen.py --root gl3w")

    def build(self):
        cmake = CMake(self)
        # build the static library from gl3w.c
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="gl3w/include", keep_path=True)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gl3w"]
