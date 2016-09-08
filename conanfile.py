from conans import ConanFile, CMake

class HelloConan(ConanFile):
    name = "libfixmatrix"
    version = "20140117"
    url = "https://github.com/sunsided/libfixmatrix.git"
    license = "MIT"
    author = "Petteri Aimonen <jpa at fixmatrix.mail.kapsi.fi>"
    requires = "libfixmath/20141230@sunside/stable"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    exports = "libfixmatrix/*", "CMakeLists.txt"

    def build(self):
        cmake = CMake(self.settings)
        self.run('cmake %s %s' % (self.conanfile_directory, cmake.command_line))
        self.run("cmake --build . %s" % cmake.build_config)

    def package(self):
        self.copy("*.h", dst="include", src="libfixmatrix")
        self.copy("*.hpp", dst="include", src="libfixmatrix")
        self.copy("*.c", dst="src", src="libfixmatrix")
        self.copy("*.lib", dst="lib", src="lib")
        self.copy("*.a", dst="lib", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["libfixmatrix"]