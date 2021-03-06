from conans import ConanFile, CMake, tools
import os
import shutil


class Gl3wConan(ConanFile):
    name = "gl3w"
    version = "0.2"
    license = "Unlicense"
    url = "https://github.com/Tuebel/gl3w-conan"
    description = "Simple OpenGL core profile loading."
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    exports = "CMakeLists.txt"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = "shared=False", "fPIC=True"

    def configure(self):
        if self.settings.compiler == 'Visual Studio':
            del self.options.fPIC

    def source(self):
        if os.path.exists("gl3w_gen.py"):
            os.remove("gl3w_gen.py")
        if os.path.exists("gl3w"):
            shutil.rmtree("gl3w")
        # download and generate the sources
        tools.download(
            "https://raw.githubusercontent.com/skaslev/gl3w/4f1d558410b0938840dc3db98e741d71f382ba22/gl3w_gen.py",
            "gl3w_gen.py")
        self.run("python gl3w_gen.py --root gl3w")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src="gl3w/include", keep_path=True)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["gl3w"]
